from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    
    errors = []
    page.on("console", lambda msg: print(f"BROWSER CONSOLE [{msg.type}]: {msg.text}"))
    page.on("pageerror", lambda err: print(f"BROWSER ERROR: {err}"))
    
    page.goto('http://localhost:8443/cases/einstein-laudos')
    page.wait_for_timeout(2000)
    print("Page Title:", page.title())
    print("Main content text:", page.locator('body').inner_text()[:400])
    browser.close()

