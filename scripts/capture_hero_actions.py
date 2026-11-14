import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={"width": 1440, "height": 1200})
        await page.goto("http://localhost:8443", wait_until="networkidle")
        
        # Capture header + hero
        header = page.locator(".site-header")
        await header.screenshot(path="scripts/header_curriculo.png")
        print("Captured scripts/header_curriculo.png")
        
        hero = page.locator(".pf-hero")
        await hero.screenshot(path="scripts/hero_actions_curriculo.png")
        print("Captured scripts/hero_actions_curriculo.png")
        
        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())

