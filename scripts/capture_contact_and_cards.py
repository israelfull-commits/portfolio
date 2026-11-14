import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={"width": 1440, "height": 1800})
        await page.goto("http://localhost:8443", wait_until="networkidle")
        
        # Capture contact section
        contact = page.locator("#contato")
        await contact.screenshot(path="scripts/contact_section.png")
        print("Captured scripts/contact_section.png")
        
        # Capture project cards grid
        grid = page.locator(".pf-project-grid")
        await grid.screenshot(path="scripts/cards_grid_explorar.png")
        print("Captured scripts/cards_grid_explorar.png")
        
        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())

