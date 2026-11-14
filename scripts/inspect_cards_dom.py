import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={"width": 1440, "height": 1800})
        await page.goto("http://localhost:8443", wait_until="networkidle")
        
        info = await page.evaluate('''() => {
            const cards = Array.from(document.querySelectorAll('.pf-project')).map((el, i) => {
                const rect = el.getBoundingClientRect();
                const title = el.querySelector('h3')?.innerText;
                const theme = el.querySelector('.pf-project-theme')?.innerText;
                const role = el.querySelector('.pf-project-role')?.innerText;
                const desc = el.querySelector('.pf-project-desc')?.innerText;
                const status = el.querySelector('.pf-project-status')?.innerText;
                const decision = el.querySelector('.pf-project-decision')?.innerText;
                const link = el.querySelector('.pf-project-link')?.innerText;
                const headingRect = el.querySelector('.pf-project-heading')?.getBoundingClientRect();
                const descRect = el.querySelector('.pf-project-desc')?.getBoundingClientRect();
                const decRect = el.querySelector('.pf-project-decision')?.getBoundingClientRect();
                return {
                    i: i + 1,
                    title,
                    theme,
                    role,
                    desc,
                    status,
                    decision,
                    link,
                    cardBox: { w: rect.width, h: rect.height, top: rect.top },
                    headingH: headingRect ? headingRect.height : 0,
                    descTop: descRect ? descRect.top : 0,
                    decTop: decRect ? decRect.top : 0,
                };
            });
            return cards;
        }''')
        import pprint
        pprint.pprint(info)
        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())

