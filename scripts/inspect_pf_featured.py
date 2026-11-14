import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={"width": 1440, "height": 1800})
        await page.goto("http://localhost:8443", wait_until="networkidle")
        
        info = await page.evaluate('''() => {
            const el = document.querySelector('.pf-featured');
            const rect = el.getBoundingClientRect();
            const story = document.querySelector('.pf-featured-story').getBoundingClientRect();
            const evidence = document.querySelector('.pf-featured-evidence').getBoundingClientRect();
            return {
                featuredBox: { w: rect.width, h: rect.height, top: rect.top, left: rect.left },
                storyBox: { w: story.width, h: story.height },
                evidenceBox: { w: evidence.width, h: evidence.height }
            };
        }''')
        import pprint
        pprint.pprint(info)
        await page.locator('.pf-featured').screenshot(path='scripts/pf_featured_actual.png')
        print("Captured pf_featured_actual.png")
        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())

