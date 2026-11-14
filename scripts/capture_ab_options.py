from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={'width': 1280, 'height': 900})
        page.goto('http://localhost:8443#trabalho', wait_until='networkidle')

        # Opcao A
        cards = page.locator('.pf-project-grid')
        cards.screenshot(path='opcao-a-contexto-no-topo.png')
        print('Captured Opcao A')

        # Click Opcao B
        btn_b = page.locator('button:has-text("Opção B")')
        btn_b.click()
        page.wait_for_timeout(300)
        cards.screenshot(path='opcao-b-imagem-no-topo.png')
        print('Captured Opcao B')

        browser.close()

if __name__ == '__main__':
    run()

