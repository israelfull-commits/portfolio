import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={"width": 1440, "height": 1800})
        await page.goto("http://localhost:8443", wait_until="networkidle")
        
        # Capture the entire pf-featured card
        featured = page.locator(".pf-featured")
        await featured.screenshot(path="scripts/featured_einstein_novo.png")
        print("Captured scripts/featured_einstein_novo.png")
        
        # Also capture Section Trabalho to see how it fits with the editorial cards below
        section = page.locator("#trabalho")
        await section.screenshot(path="scripts/section_trabalho_completa_com_destaque.png")
        print("Captured scripts/section_trabalho_completa_com_destaque.png")
        
        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())

