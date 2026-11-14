from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={'width': 1280, 'height': 900})
        page.goto('http://localhost:8443#cases-itau', wait_until='networkidle')

        # Opcao C (Editorial - default)
        grid = page.locator('.pf-project-grid')
        grid.screenshot(path='opcao-c-editorial-senior.png')
        print('Captured Opcao C')

        # Opcao A
        btn_a = page.locator('button:has-text("Opção A")')
        btn_a.click()
        page.wait_for_timeout(300)
        grid.screenshot(path='opcao-a-contexto-no-topo.png')
        print('Captured Opcao A')

        # Opcao B
        btn_b = page.locator('button:has-text("Opção B")')
        btn_b.click()
        page.wait_for_timeout(300)
        grid.screenshot(path='opcao-b-imagem-no-topo.png')
        print('Captured Opcao B')

        browser.close()

if __name__ == '__main__':
    run()

