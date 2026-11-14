import asyncio
from playwright.async_api import async_playwright

async def check_port(port):
    print(f"\n--- Checking http://localhost:{port} ---")
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        
        failed_requests = []
        page.on("requestfailed", lambda req: failed_requests.append((req.url, req.failure)))
        
        responses = []
        page.on("response", lambda res: responses.append((res.url, res.status, res.headers.get("content-type"))))
        
        await page.goto(f"http://localhost:{port}", wait_until="networkidle")
        
        # Check image in .pf-case-preview
        img_info = await page.evaluate('''() => {
            const img = document.querySelector('.pf-case-preview img');
            if (!img) return { found: false };
            return {
                found: true,
                src: img.src,
                currentSrc: img.currentSrc,
                naturalWidth: img.naturalWidth,
                naturalHeight: img.naturalHeight,
                complete: img.complete
            };
        }''')
        print("Image info:", img_info)
        print("Failed requests:", failed_requests)
        for r in responses:
            if "hiae" in r[0]:
                print("HIAE response:", r)
        await browser.close()

async def main():
    await check_port(8443)
    await check_port(8444)

if __name__ == "__main__":
    asyncio.run(main())

