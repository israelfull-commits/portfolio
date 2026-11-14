import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={"width": 1440, "height": 1800})
        await page.goto("http://localhost:8443", wait_until="networkidle")
        
        # Ensure Opcao C is selected
        tab_c = page.locator("button:has-text('Opção C')")
        if await tab_c.count() > 0:
            await tab_c.click()
            await page.wait_for_timeout(300)
            
        # Capture Section Trabalho
        section = page.locator("#trabalho")
        await section.screenshot(path="scripts/section_trabalho.png")
        print("Captured scripts/section_trabalho.png")
        
        # Also capture each project card individually
        projects = await page.locator(".pf-project").all()
        for idx, proj in enumerate(projects):
            await proj.screenshot(path=f"scripts/card_{idx+1}.png")
            print(f"Captured scripts/card_{idx+1}.png")
            
        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())

