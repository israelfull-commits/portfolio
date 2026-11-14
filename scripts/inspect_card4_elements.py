from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={'width': 1280, 'height': 900})
        page.goto('http://localhost:8443', wait_until='networkidle')

        card4 = page.locator('#project-registros-atendimento')
        children = card4.locator('> *').all()
        print('Card 4 children count:', len(children))
        for c in children:
            tag = c.evaluate("el => el.tagName.toLowerCase() + '.' + el.className")
            box = c.bounding_box()
            text = c.inner_text()[:30].replace('\n', ' ')
            print(f"{tag}: x={round(box['x'],1)} y={round(box['y'],1)} w={round(box['width'],1)} h={round(box['height'],1)} | \"{text}\"")

        browser.close()

if __name__ == '__main__':
    run()

