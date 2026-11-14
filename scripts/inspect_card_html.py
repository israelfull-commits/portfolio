from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={'width': 1280, 'height': 900})
        page.goto('http://localhost:8443')
        page.wait_for_selector('#project-movimentacoes')

        html = page.evaluate('() => document.querySelector("#project-movimentacoes").outerHTML')
        print(html)

        browser.close()

if __name__ == '__main__':
    run()

