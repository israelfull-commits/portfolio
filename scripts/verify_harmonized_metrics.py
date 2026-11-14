from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={'width': 1280, 'height': 900})
        page.goto('http://localhost:8443', wait_until='networkidle')
        
        grid = page.locator('.pf-project-grid').bounding_box()
        cards = page.locator('.pf-project').all()
        print('Grid width:', round(grid['width'], 1))
        for i, c in enumerate(cards):
            box = c.bounding_box()
            print(f"Card {i+1}: width={round(box['width'], 1)}, height={round(box['height'], 1)}, x={round(box['x'], 1)}, y={round(box['y'], 1)}")
            
        exp_grid = page.locator('.pf-expertise-grid').bounding_box()
        exp_items = page.locator('.pf-expertise').all()
        print('Expertise grid width:', round(exp_grid['width'], 1))
        for i, e in enumerate(exp_items):
            box = e.bounding_box()
            print(f"Expertise {i+1}: width={round(box['width'], 1)}, height={round(box['height'], 1)}, x={round(box['x'], 1)}")
            
        browser.close()

if __name__ == '__main__':
    run()

