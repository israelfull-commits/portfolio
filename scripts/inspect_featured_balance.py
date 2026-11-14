import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={"width": 1440, "height": 1800})
        await page.goto("http://localhost:8443", wait_until="networkidle")
        
        info = await page.evaluate('''() => {
            const featured = document.querySelector('.pf-featured').getBoundingClientRect();
            const story = document.querySelector('.pf-featured-story').getBoundingClientRect();
            const evidence = document.querySelector('.pf-featured-evidence').getBoundingClientRect();
            return {
                featuredBox: { w: featured.width, h: featured.height },
                storyBox: { w: story.width, h: story.height },
                evidenceBox: { w: evidence.width, h: evidence.height }
            };
        }''')
        import pprint
        pprint.pprint(info)
        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())

