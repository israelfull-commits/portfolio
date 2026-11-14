from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page(viewport={'width': 1440, 'height': 900})
    page.goto('http://localhost:8443/cases/einstein-laudos', wait_until='networkidle')
    page.wait_for_timeout(1000)
    
    # 1. Hero
    page.screenshot(path='output/screenshots/einstein-v59-hero.png', full_page=False)
    
    # 2. Scroll to chapter 1 (resumo)
    page.locator('#resumo').scroll_into_view_if_needed()
    page.wait_for_timeout(500)
    page.screenshot(path='output/screenshots/einstein-v59-ch1-resumo.png', full_page=False)
    
    # 3. Scroll to chapter 4 (decisoes)
    page.locator('#decisoes').scroll_into_view_if_needed()
    page.wait_for_timeout(500)
    page.screenshot(path='output/screenshots/einstein-v59-ch4-decisoes.png', full_page=False)
    
    # 4. Scroll to chapter 5 (solucao)
    page.locator('#solucao').scroll_into_view_if_needed()
    page.wait_for_timeout(500)
    page.screenshot(path='output/screenshots/einstein-v59-ch5-solucao.png', full_page=False)
    
    browser.close()

print("Captured all Einstein screenshots successfully!")

