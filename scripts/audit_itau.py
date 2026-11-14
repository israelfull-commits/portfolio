import asyncio
from playwright.async_api import async_playwright

async def audit_itau():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={'width': 1440, 'height': 900})
        
        # Test Hub Liquidez
        await page.goto('http://localhost:8443/cases/itau/hub-liquidez', wait_until='networkidle')
        await page.screenshot(path=r'C:\Users\Israel Rozar\.gemini\antigravity\brain\ec9956e5-078d-4d87-9a8e-74481434c7dc\audit_itau_liquidez_desktop.png', full_page=True)
        
        # Test Vencimentos
        await page.goto('http://localhost:8443/cases/itau/vencimentos', wait_until='networkidle')
        await page.screenshot(path=r'C:\Users\Israel Rozar\.gemini\antigravity\brain\ec9956e5-078d-4d87-9a8e-74481434c7dc\audit_itau_vencimentos_desktop.png', full_page=True)
        
        await browser.close()

asyncio.run(audit_itau())
print('Done auditing itau cases')
