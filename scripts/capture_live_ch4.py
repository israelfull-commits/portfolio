from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page(viewport={'width': 1440, 'height': 900})
    page.goto('http://localhost:8443/cases/einstein-laudos', wait_until='networkidle')
    
    # Locate protrombina image and callout list
    target = page.locator('.cp-callout-list')
    target.scroll_into_view_if_needed()
    page.wait_for_timeout(400)
    
    # Screenshot containing both figure and callout list
    parent = page.locator('.cp-callout-list').locator('xpath=..')
    parent.screenshot(path='C:/Users/Israel Rozar/.gemini/antigravity/brain/ec9956e5-078d-4d87-9a8e-74481434c7dc/live_browser_protrombina_v2.png')
    
    browser.close()

print('Protrombina live screenshot captured!')
