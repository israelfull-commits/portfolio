from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={'width': 1280, 'height': 900})
        page.goto('http://localhost:8443', wait_until='networkidle')

        cards = page.locator('.pf-project').all()
        for i in range(3):
            c = cards[i]
            desc = c.locator('p:not(.pf-project-theme):not(.pf-project-role):not(.pf-project-decision)').bounding_box()
            dec = c.locator('.pf-project-decision').bounding_box()
            print(f"Card {i+1}: desc y={round(desc['y'],1)} h={round(desc['height'],1)} | dec y={round(dec['y'],1)} h={round(dec['height'],1)}")

        browser.close()

if __name__ == '__main__':
    run()
