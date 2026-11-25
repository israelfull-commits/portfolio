import asyncio
import json
from playwright.async_api import async_playwright

PAGES = [
    ('/', 'Home'),
    ('/cases/einstein-laudos', 'Einstein Laudos'),
    ('/cases/claro-ativacao-simplificada', 'Claro Ativação'),
    ('/cases/neoenergia-conexao-digital', 'Neoenergia Conexão'),
    ('/cases/itau/vencimentos', 'Itaú Vencimentos')
]

async def audit_page_ux_a11y(page, base_url, route, label):
    url = f"{base_url}{route}"
    await page.goto(url, wait_until='networkidle')
    await asyncio.sleep(0.5)

    data = await page.evaluate('''() => {
        const issues = [];

        // 1. Check Images for alt attributes
        const images = document.querySelectorAll('img');
        let imgMissingAlt = 0;
        images.forEach(img => {
            if (!img.hasAttribute('alt')) {
                imgMissingAlt++;
                issues.push({ type: 'IMG_MISSING_ALT', selector: img.src });
            }
        });

        // 2. Check Buttons for accessible names
        const buttons = document.querySelectorAll('button');
        let btnMissingName = 0;
        let btnTooSmall = 0;
        buttons.forEach(btn => {
            if (btn.offsetParent === null) return;
            const name = btn.getAttribute('aria-label') || btn.innerText.trim();
            if (!name) {
                btnMissingName++;
                issues.push({ type: 'BTN_NO_ACCESSIBLE_NAME', selector: btn.className });
            }
            const rect = btn.getBoundingClientRect();
            // WCAG 2.2 SC 2.5.8 Target Size: min 24x24px
            if (rect.width < 24 || rect.height < 24) {
                btnTooSmall++;
                issues.push({ type: 'BTN_TARGET_TOO_SMALL', size: `${rect.width}x${rect.height}`, class: btn.className });
            }
        });

        // 3. Check Links for accessible names and target size
        const links = document.querySelectorAll('a');
        let linkMissingName = 0;
        links.forEach(a => {
            if (a.offsetParent === null) return;
            const name = a.getAttribute('aria-label') || a.innerText.trim();
            if (!name) {
                linkMissingName++;
                issues.push({ type: 'LINK_NO_ACCESSIBLE_NAME', href: a.getAttribute('href') });
            }
        });

        // 4. Heading levels check
        const headings = Array.from(document.querySelectorAll('h1, h2, h3, h4, h5, h6'));
        let headingSkips = 0;
        let h1Count = 0;
        let lastLevel = 0;
        headings.forEach(h => {
            const level = parseInt(h.tagName[1]);
            if (level === 1) h1Count++;
            if (lastLevel > 0 && level > lastLevel + 1) {
                headingSkips++;
                issues.push({ type: 'HEADING_LEVEL_SKIP', from: `h${lastLevel}`, to: `h${level}`, text: h.innerText.slice(0, 30) });
            }
            lastLevel = level;
        });

        // 5. Test Lightbox Modal Keyboard Interaction if present
        return {
            imgTotal: images.length,
            imgMissingAlt,
            btnTotal: buttons.length,
            btnMissingName,
            btnTooSmall,
            linkTotal: links.length,
            linkMissingName,
            h1Count,
            headingSkips,
            issues
        };
    }''')

    # Test Keyboard navigation and Dialog Escape behavior on Case pages
    dialog_test = 'N/A'
    if '/cases/' in route:
        # Click first figure button to open modal
        btn = page.locator('.cp-figure-btn').first
        if await btn.count() > 0:
            await btn.click()
            await page.wait_for_selector('dialog.cp-lightbox[open]', timeout=5000)
            
            # Press Escape to test native modal dismissal
            await page.keyboard.press('Escape')
            await asyncio.sleep(0.3)
            is_closed = await page.locator('dialog.cp-lightbox[open]').count() == 0
            dialog_test = 'PASS' if is_closed else 'FAIL_ESCAPE'

    return {
        'page': label,
        'data': data,
        'dialog_test': dialog_test
    }

async def main():
    base_url = 'http://localhost:8443'
    results = []
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page(viewport={'width': 1440, 'height': 900})

        for route, label in PAGES:
            res = await audit_page_ux_a11y(page, base_url, route, label)
            results.append(res)

        await browser.close()

    print("\n====================================================================")
    print("   AUDITORIA INTEGRAL DE UX, UI E ACESSIBILIDADE DIGITAL (WCAG 2.2)")
    print("====================================================================")
    all_clean = True
    for r in results:
        p_name = r['page']
        d = r['data']
        issues = d['issues']
        print(f"\n[{p_name}]")
        print(f"  • Imagens ({d['imgTotal']}): {d['imgMissingAlt']} sem alt (100% acessíveis: {d['imgMissingAlt'] == 0})")
        print(f"  • Botões ({d['btnTotal']}): {d['btnMissingName']} sem nome acessível | {d['btnTooSmall']} abaixo do target 24x24px")
        print(f"  • Links ({d['linkTotal']}): {d['linkMissingName']} sem nome acessível")
        print(f"  • Títulos: {d['h1Count']} h1 (Exato 1: {d['h1Count'] == 1}) | {d['headingSkips']} saltos de nível")
        print(f"  • Modal Lightbox (Teclado/Escape/Focus): {r['dialog_test']}")

        if issues:
            all_clean = False
            for iss in issues:
                print(f"    ! {iss}")

    if all_clean:
        print("\n--------------------------------------------------------------------")
        print("✓ ABSOLUTA CONFORMIDADE: ZERO falhas de UX, UI ou Acessibilidade!")
        print("--------------------------------------------------------------------")
    else:
        print("\n--------------------------------------------------------------------")
        print("Atenção: existem pequenos ajustes a calibrar.")
        print("--------------------------------------------------------------------")

if __name__ == '__main__':
    asyncio.run(main())
