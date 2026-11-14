from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page(viewport={'width': 1440, 'height': 900})
    page.goto('http://localhost:8443/cases/einstein-laudos', wait_until='networkidle')
    page.wait_for_timeout(1000)
    page.screenshot(path='output/screenshots/einstein-synced-59-2-hero.png', full_page=False)
    # scroll to chapter 1
    page.locator('#resumo').scroll_into_view_if_needed()
    page.wait_for_timeout(500)
    page.screenshot(path='output/screenshots/einstein-synced-59-2-ch1.png', full_page=False)
    browser.close()

print("Captured einstein-synced-59-2-hero.png and ch1.png")

