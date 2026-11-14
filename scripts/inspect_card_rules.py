from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={'width': 1280, 'height': 900})
        page.goto('http://localhost:8443')
        page.wait_for_selector('#project-movimentacoes')

        matched = page.evaluate('''() => {
            const el = document.querySelector("#project-movimentacoes .pf-project-decision");
            const matchedRules = [];
            for (const s of document.styleSheets) {
                try {
                    for (const r of s.cssRules) {
                        if (r.selectorText && el.matches(r.selectorText)) {
                            matchedRules.push({ sel: r.selectorText, text: r.cssText });
                        }
                    }
                } catch(e) {}
            }
            return matchedRules;
        }''')
        for m in matched:
            print(m)

        browser.close()

if __name__ == '__main__':
    run()

