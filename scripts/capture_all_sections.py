from playwright.sync_api import sync_playwright

def capture_sections():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={'width': 1280, 'height': 900})
        page.goto('http://localhost:8443', wait_until='networkidle')

        sections = ['#topo', '#trabalho', '#sobre', '#experiencia', '#contato']
        for s in sections:
            el = page.locator(s)
            if el.count() > 0:
                name = s.replace('#', '')
                el.screenshot(path=f'audit-sec-{name}-desktop.png')
                print(f'Captured {name} desktop')

        # Also capture mobile
        page.set_viewport_size({'width': 390, 'height': 844})
        for s in sections:
            el = page.locator(s)
            if el.count() > 0:
                name = s.replace('#', '')
                el.screenshot(path=f'audit-sec-{name}-mobile.png')
                print(f'Captured {name} mobile')

        browser.close()

if __name__ == '__main__':
    capture_sections()

