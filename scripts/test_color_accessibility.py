import asyncio
import math
import json
import re
from playwright.async_api import async_playwright

def parse_rgb(rgb_str):
    m = re.match(r'rgba?\((\d+),\s*(\d+),\s*(\d+)(?:,\s*([\d.]+))?\)', rgb_str)
    if m:
        r, g, b = int(m.group(1)), int(m.group(2)), int(m.group(3))
        a = float(m.group(4)) if m.group(4) is not None else 1.0
        return r, g, b, a
    return 0, 0, 0, 1.0

def luminance(r, g, b):
    vals = []
    for c in (r, g, b):
        c = c / 255.0
        vals.append(c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4)
    return 0.2126 * vals[0] + 0.7152 * vals[1] + 0.0722 * vals[2]

def contrast_ratio(rgb1, rgb2):
    l1 = luminance(*rgb1[:3])
    l2 = luminance(*rgb2[:3])
    lighter = max(l1, l2)
    darker = min(l1, l2)
    return (lighter + 0.05) / (darker + 0.05)

ROUTES = [
    ('/', 'Home'),
    ('/cases/einstein-laudos', 'Einstein Laudos'),
    ('/cases/claro-ativacao-simplificada', 'Claro Ativação'),
    ('/cases/neoenergia-conexao-digital', 'Neoenergia Conexão'),
    ('/cases/itau/vencimentos', 'Itaú Vencimentos')
]

async def audit_page_colors(page, base_url, route, label):
    url = f"{base_url}{route}"
    await page.goto(url, wait_until='networkidle')
    await asyncio.sleep(0.5)

    results = await page.evaluate('''() => {
        function getEffectiveBg(el) {
            let cur = el;
            while (cur && cur !== document.documentElement) {
                // Check if element has a dark gradient card class
                if (cur.classList.contains('cp-note') || 
                    cur.classList.contains('cp-lead-card') || 
                    cur.classList.contains('cp-cover-flow')) {
                    return 'rgb(10, 54, 34)'; // #0A3622
                }
                if (cur.classList.contains('cp-how-might-we') || cur.classList.contains('header-cta')) {
                    return 'rgb(206, 255, 26)'; // #CEFF1A
                }

                const style = window.getComputedStyle(cur);
                const bg = style.backgroundColor;
                if (bg && bg !== 'rgba(0, 0, 0, 0)' && bg !== 'transparent') {
                    const m = bg.match(/rgba?\\((\\d+),\\s*(\\d+),\\s*(\\d+)(?:,\\s*([\\d.]+))?\\)/);
                    if (m && m[4] && parseFloat(m[4]) < 0.9) {
                        // Partial alpha, continue
                    } else {
                        return bg;
                    }
                }
                cur = cur.parentElement;
            }
            return 'rgb(252, 249, 242)'; // default canvas #FCF9F2
        }

        const elements = document.querySelectorAll('h1, h2, h3, h4, p, span, a, button, li, label, strong');
        const data = [];
        const seen = new Set();

        elements.forEach(el => {
            if (el.offsetParent === null && el.tagName !== 'BODY') return;
            const text = (el.innerText || '').trim();
            if (!text || text.length === 0) return;

            const style = window.getComputedStyle(el);
            const color = style.color;
            const bg = getEffectiveBg(el);
            const fontSize = parseFloat(style.fontSize);
            const fontWeight = parseInt(style.fontWeight) || 400;

            const key = `${color}_${bg}_${fontSize}_${fontWeight}`;
            if (!seen.has(key)) {
                seen.add(key);
                data.push({
                    tag: el.tagName.toLowerCase(),
                    textSample: text.slice(0, 30),
                    className: el.className ? (typeof el.className === 'string' ? el.className.slice(0, 40) : '') : '',
                    color,
                    bg,
                    fontSize,
                    fontWeight,
                    isLargeText: fontSize >= 24 || (fontSize >= 18.66 && fontWeight >= 700)
                });
            }
        });
        return data;
    }''')

    report = []
    for item in results:
        rgb_fg = parse_rgb(item['color'])
        rgb_bg = parse_rgb(item['bg'])
        cr = contrast_ratio(rgb_fg, rgb_bg)
        
        min_aa = 3.0 if item['isLargeText'] else 4.5
        min_aaa = 4.5 if item['isLargeText'] else 7.0

        pass_aa = cr >= min_aa
        pass_aaa = cr >= min_aaa

        report.append({
            'route': label,
            'tag': item['tag'],
            'sample': item['textSample'],
            'class': item['className'],
            'color': item['color'],
            'bg': item['bg'],
            'ratio': round(cr, 2),
            'fontSize': item['fontSize'],
            'fontWeight': item['fontWeight'],
            'isLarge': item['isLargeText'],
            'passAA': pass_aa,
            'passAAA': pass_aaa
        })

    return report

async def main():
    base_url = "http://localhost:8443"
    all_reports = []
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page(viewport={'width': 1440, 'height': 900})
        
        for route, label in ROUTES:
            rep = await audit_page_colors(page, base_url, route, label)
            all_reports.extend(rep)
        
        await browser.close()

    total_checks = len(all_reports)
    aa_passes = [r for r in all_reports if r['passAA']]
    aa_fails = [r for r in all_reports if not r['passAA']]
    aaa_passes = [r for r in all_reports if r['passAAA']]
    aaa_fails = [r for r in all_reports if not r['passAAA']]

    print(f"\n=======================================================")
    print(f"   AUDITORIA DE ACESSIBILIDADE DE CORES & CONTRASTE   ")
    print(f"=======================================================")
    print(f"Total de pares de cor (Foreground / Background) analisados: {total_checks}")
    print(f"Conformidade WCAG AA : {len(aa_passes)}/{total_checks} ({len(aa_passes)/total_checks*100:.1f}%)")
    print(f"Conformidade WCAG AAA: {len(aaa_passes)}/{total_checks} ({len(aaa_passes)/total_checks*100:.1f}%)")

    if aa_fails:
        print("\n--- ATENÇÃO: Falhas em WCAG AA (Mínimo 4.5:1 / 3.0:1) ---")
        for f in aa_fails:
            print(f"[{f['route']}] <{f['tag']} class='{f['class']}'> text='{f['sample']}'")
            print(f"  Ratio: {f['ratio']}:1 | color={f['color']} on bg={f['bg']} (size={f['fontSize']}px, w={f['fontWeight']})")
    else:
        print("\n✓ ZERO falhas em WCAG AA em todas as páginas!")

    if aaa_fails:
        print(f"\n--- Pares que não atingem WCAG AAA (Mínimo 7.0:1 / 4.5:1) ({len(aaa_fails)}) ---")
        for f in aaa_fails[:10]:
            print(f"[{f['route']}] <{f['tag']} class='{f['class']}'> text='{f['sample']}'")
            print(f"  Ratio: {f['ratio']}:1 | color={f['color']} on bg={f['bg']} (size={f['fontSize']}px, w={f['fontWeight']})")
    else:
        print("\n✓ 100% DE CONFORMIDADE WCAG AAA!")

    with open('output/visual_qa/color_contrast_report.json', 'w', encoding='utf-8') as fp:
        json.dump(all_reports, fp, indent=2, ensure_ascii=False)
    print("\nRelatório completo salvo em output/visual_qa/color_contrast_report.json")

if __name__ == '__main__':
    asyncio.run(main())
