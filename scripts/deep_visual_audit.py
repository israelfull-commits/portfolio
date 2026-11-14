import json
from playwright.sync_api import sync_playwright

def audit_full_page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={'width': 1280, 'height': 900})
        page.goto('http://localhost:8443', wait_until='networkidle')

        audit_results = page.evaluate('''() => {
            const issues = [];

            // 1. Check all headings for baseline, margin collapse, empty voids
            const cards = document.querySelectorAll('.pf-project');
            cards.forEach((c, idx) => {
                const h3 = c.querySelector('h3');
                const theme = c.querySelector('.pf-project-theme');
                const role = c.querySelector('.pf-project-role');
                const desc = c.querySelector('p:not(.pf-project-theme):not(.pf-project-role):not(.pf-project-decision):not(.pf-project-status)');
                const decision = c.querySelector('.pf-project-decision');
                const link = c.querySelector('a.pf-project-link, a');

                if (h3 && theme) {
                    const h3Box = h3.getBoundingClientRect();
                    const themeBox = theme.getBoundingClientRect();
                    const gap = themeBox.top - h3Box.bottom;
                    if (gap > 20) {
                        issues.push({
                            section: 'Projects',
                            element: `Card ${idx + 1} (${h3.innerText.trim()})`,
                            type: 'Gestalt Proximity Gap',
                            detail: `Gap between H3 and Theme is ${gap.toFixed(1)}px (too large due to min-height on H3). Title and subtitle look detached.`
                        });
                    }
                }
            });

            // 2. Check font weights, sizes, and contrast across entire page
            const textNodes = document.querySelectorAll('h1, h2, h3, h4, p, span, a, figcaption');
            textNodes.forEach(node => {
                const cs = window.getComputedStyle(node);
                const rect = node.getBoundingClientRect();
                // Check if text is hidden or cut off
                if (rect.width === 0 && !node.classList.contains('pf-sr-only')) {
                    issues.push({
                        section: 'Text Visibility',
                        element: node.tagName + '.' + node.className,
                        type: 'Zero Width',
                        detail: `Text "${node.innerText.substring(0, 20)}" has 0 width.`
                    });
                }
            });

            // 3. Check section padding rhythm
            const sections = document.querySelectorAll('.pf-section, .pf-hero, .pf-contact-wrap');
            const rhythms = [];
            sections.forEach(s => {
                const cs = window.getComputedStyle(s);
                rhythms.push({ id: s.id || s.className, pt: cs.paddingTop, pb: cs.paddingBottom });
            });

            // 4. Check horizontal alignment of cards in .pf-expertise-grid
            const expCards = document.querySelectorAll('.pf-expertise');
            const expHeights = Array.from(expCards).map((e, i) => {
                const rect = e.getBoundingClientRect();
                return { idx: i + 1, height: rect.height, top: rect.top };
            });

            // 5. Check mobile view (simulate via evaluation or resize)
            return {
                issues,
                rhythms,
                expHeights,
                projectCount: cards.length
            };
        }''')

        print(json.dumps(audit_results, indent=2))
        browser.close()

if __name__ == '__main__':
    audit_full_page()

