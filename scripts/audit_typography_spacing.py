from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={'width': 1280, 'height': 900})
        page.goto('http://localhost:8443', wait_until='networkidle')

        sections_info = page.evaluate('''() => {
            const sections = document.querySelectorAll('.pf-hero, .pf-section, .pf-contact-wrap');
            const data = [];
            sections.forEach(s => {
                const cs = window.getComputedStyle(s);
                const headings = Array.from(s.querySelectorAll('h1, h2, h3, h4, .pf-label, .pf-lead, p, a, figcaption, span')).map(h => {
                    const hcs = window.getComputedStyle(h);
                    return {
                        tag: h.tagName.toLowerCase(),
                        cls: h.className,
                        text: (h.innerText || '').substring(0, 35).replace(/\\n/g, ' '),
                        fontSize: hcs.fontSize,
                        lineHeight: hcs.lineHeight,
                        fontWeight: hcs.fontWeight,
                        marginTop: hcs.marginTop,
                        marginBottom: hcs.marginBottom,
                        paddingTop: hcs.paddingTop,
                        paddingBottom: hcs.paddingBottom,
                        color: hcs.color
                    };
                });
                data.push({
                    id: s.id || s.className,
                    paddingTop: cs.paddingTop,
                    paddingBottom: cs.paddingBottom,
                    marginTop: cs.marginTop,
                    marginBottom: cs.marginBottom,
                    elements: headings
                });
            });
            return data;
        }''')

        for s in sections_info:
            print(f"\n=======================================================")
            print(f"SECTION: {s['id']} | pt={s['paddingTop']} pb={s['paddingBottom']} mt={s['marginTop']} mb={s['marginBottom']}")
            print(f"=======================================================")
            seen = set()
            for el in s['elements']:
                key = (el['tag'], el['cls'], el['fontSize'], el['fontWeight'])
                if key not in seen and el['text'].strip():
                    seen.add(key)
                    print(f"  [{el['tag']}.{el['cls']}] \"{el['text']}\"")
                    print(f"      Size: {el['fontSize']} / Line: {el['lineHeight']} | Weight: {el['fontWeight']} | Color: {el['color']}")
                    print(f"      Margin: t={el['marginTop']} b={el['marginBottom']} | Padding: t={el['paddingTop']} b={el['paddingBottom']}")

        browser.close()

if __name__ == '__main__':
    run()

