import json
from playwright.sync_api import sync_playwright

def run_audit():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1440, "height": 900}, device_scale_factor=2)
        page.goto("http://localhost:8443/cases/einstein-laudos", wait_until="networkidle")
        
        js_code = """
        () => {
            function getStyles(sel) {
                const el = document.querySelector(sel);
                if (!el) return null;
                const cs = window.getComputedStyle(el);
                return {
                    selector: sel,
                    fontFamily: cs.fontFamily,
                    fontSize: cs.fontSize,
                    fontWeight: cs.fontWeight,
                    lineHeight: cs.lineHeight,
                    color: cs.color,
                    backgroundColor: cs.backgroundColor,
                    border: cs.border,
                    borderRadius: cs.borderRadius,
                    boxShadow: cs.boxShadow,
                    margin: cs.margin,
                    padding: cs.padding
                };
            }
            
            return {
                title: getStyles(".cp-title"),
                kicker: getStyles(".cp-kicker"),
                headline: getStyles(".cp-headline"),
                metaStrip: getStyles(".cp-meta"),
                heroFigure: getStyles(".cp-hero-figure"),
                summaryParagraph: getStyles(".cp-summary p"),
                chapterTitle: getStyles(".cp-chapter-title"),
                chapterBody: getStyles(".cp-chapter p"),
                figure: getStyles(".cp-figure"),
                figcaption: getStyles(".cp-figure figcaption"),
                metricItem: getStyles(".cp-metrics-item")
            };
        }
        """
        
        res = page.evaluate(js_code)
        browser.close()
        
        with open("scripts/computed_styles_audit.json", "w", encoding="utf-8") as f:
            json.dump(res, f, indent=2)
            
        print("Computed styles saved successfully!")

if __name__ == "__main__":
    run_audit()

