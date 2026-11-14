import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={"width": 1440, "height": 1800})
        
        candidates = [
            ("multicanal", "/images/hiae-multicanal-web-celular.webp", "Visão Multicanal (Desktop + Mobile)"),
            ("capa_editorial", "/images/hiae-capa-editorial-1600.webp", "Capa Editorial Design System (1600px)"),
            ("estado_proposto_2000", "/images/hiae-estado-proposto-anotado.webp", "Proposta Anotada Alta Resolução (2000px)"),
            ("ds_componentes", "/images/hiae-ds-componentes-crop-1600.webp", "Componentes e Anatomia Design System"),
        ]
        
        for name, src, label in candidates:
            await page.goto("http://localhost:8443", wait_until="networkidle")
            # swap image src via evaluate
            await page.evaluate(f'''() => {{
                const img = document.querySelector('.pf-case-preview img');
                if (img) {{
                    img.src = "{src}";
                    img.srcset = "";
                }}
            }}''')
            await page.wait_for_timeout(400)
            featured = page.locator(".pf-featured")
            await featured.screenshot(path=f"scripts/featured_option_{name}.png")
            print(f"Captured scripts/featured_option_{name}.png")
            
        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())

