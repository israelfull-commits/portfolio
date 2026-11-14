from playwright.sync_api import sync_playwright

def inspect_all():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={'width': 1280, 'height': 900})
        page.goto('http://localhost:8443', wait_until='networkidle')

        data = page.evaluate('''() => {
            const getBox = sel => {
                const el = document.querySelector(sel);
                if (!el) return null;
                const r = el.getBoundingClientRect();
                const cs = window.getComputedStyle(el);
                return { sel, top: r.top, left: r.left, width: r.width, height: r.height, pt: cs.paddingTop, pb: cs.paddingBottom, pl: cs.paddingLeft, pr: cs.paddingRight, mt: cs.marginTop, mb: cs.marginBottom };
            };

            return {
                hero: getBox('.pf-hero'),
                heroCopy: getBox('.pf-hero-copy'),
                heroPortrait: getBox('.pf-portrait'),
                featured: getBox('.pf-featured'),
                featuredStory: getBox('.pf-featured-story'),
                featuredEvidence: getBox('.pf-featured-evidence'),
                projectGrid: getBox('.pf-project-grid'),
                card1: getBox('#project-movimentacoes'),
                card2: getBox('#project-hub-liquidez'),
                card3: getBox('#project-campanhas'),
                card4: getBox('#project-registros-atendimento'),
                expertiseGrid: getBox('.pf-expertise-grid'),
                trajectory: getBox('.pf-trajectory'),
                timeline: getBox('.pf-timeline'),
                education: getBox('.pf-education'),
                contact: getBox('.pf-contact'),
                footer: getBox('.portfolio-site footer')
            };
        }''')

        for k, v in data.items():
            if v:
                print(f"{k.upper()}: w={round(v['width'],1)} h={round(v['height'],1)} top={round(v['top'],1)} | pad={v['pt']}/{v['pb']} mar={v['mt']}/{v['mb']}")

        browser.close()

if __name__ == '__main__':
    inspect_all()

