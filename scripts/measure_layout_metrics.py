from playwright.sync_api import sync_playwright

def audit_url(url, label):
    print(f"\n==========================================")
    print(f"AUDIT FOR {label} ({url})")
    print(f"==========================================")
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 1280, "height": 900})
        page.goto(url)
        page.wait_for_selector("h1")

        # 1. Header alignment
        header_box = page.eval_on_selector(".site-header", "el => { const r = el.getBoundingClientRect(); const s = getComputedStyle(el); return { x: r.x, width: r.width, padLeft: s.paddingLeft, padRight: s.paddingRight }; }")
        brand_box = page.eval_on_selector(".site-header .brand", "el => el.getBoundingClientRect().x")
        print(f"Header: x={header_box['x']}, width={header_box['width']}, padLeft={header_box['padLeft']}")
        print(f"Brand left edge: x={brand_box}")

        # 2. Main Container / Hero alignment
        container_box = page.eval_on_selector(".pf-container", "el => { const r = el.getBoundingClientRect(); return { x: r.x, width: r.width }; }")
        hero_title_box = page.eval_on_selector("#hero-title", "el => el.getBoundingClientRect().x")
        print(f"pf-container: x={container_box['x']}, width={container_box['width']}")
        print(f"Hero Title left edge: x={hero_title_box}")
        print(f"--> Header Brand vs Hero Title alignment delta: {brand_box - hero_title_box}px")

        # 3. Section paddings and gaps
        sections = [".pf-hero", ".pf-work", ".pf-about", ".pf-trajectory", ".pf-contact-wrap"]
        for s in sections:
            info = page.eval_on_selector(s, "el => { const r = el.getBoundingClientRect(); const st = getComputedStyle(el); return { x: r.x, width: r.width, padTop: st.paddingTop, padBottom: st.paddingBottom, marTop: st.marginTop, marBottom: st.marginBottom }; }")
            print(f"Section {s}: padTop={info['padTop']}, padBottom={info['padBottom']}, marTop={info['marTop']}, marBottom={info['marBottom']}")

        # 4. Featured card internal spacing
        featured_info = page.eval_on_selector(".pf-featured", "el => { const r = el.getBoundingClientRect(); const s = getComputedStyle(el); return { x: r.x, width: r.width, marBottom: s.marginBottom, gridCols: s.gridTemplateColumns }; }")
        story_info = page.eval_on_selector(".pf-featured-story", "el => { const s = getComputedStyle(el); return { pad: s.padding }; }")
        evidence_info = page.eval_on_selector(".pf-featured-evidence", "el => { const s = getComputedStyle(el); return { pad: s.padding }; }")
        print(f"Featured: width={featured_info['width']}, gridCols={featured_info['gridCols']}, storyPad={story_info['pad']}, evidencePad={evidence_info['pad']}")

        # 5. Project cards grid & cards
        cards_info = page.eval_on_selector_all(".pf-project", "els => els.map((el, i) => { const r = el.getBoundingClientRect(); const s = getComputedStyle(el); return { i, x: r.x, y: r.y, w: r.width, h: r.height, pad: s.padding }; })")
        print(f"Project cards count: {len(cards_info)}")
        for c in cards_info:
            print(f"  Card {c['i']+1}: w={c['w']}px, h={c['h']}px, pad={c['pad']}, x={c['x']}")

        # 6. Expertise grid & cards
        exp_info = page.eval_on_selector_all(".pf-expertise", "els => els.map((el, i) => { const r = el.getBoundingClientRect(); const s = getComputedStyle(el); return { i, x: r.x, y: r.y, w: r.width, h: r.height, pad: s.padding }; })")
        print(f"Expertise cards count: {len(exp_info)}")
        for e in exp_info:
            print(f"  Exp Card {e['i']+1}: w={e['w']}px, h={e['h']}px, pad={e['pad']}, x={e['x']}")

        # 7. Contact card
        contact_info = page.eval_on_selector(".pf-contact", "el => { const r = el.getBoundingClientRect(); const s = getComputedStyle(el); return { w: r.width, h: r.height, pad: s.padding, rad: s.borderRadius }; }")
        print(f"Contact card: w={contact_info['w']}px, pad={contact_info['pad']}, rad={contact_info['rad']}")

        browser.close()

try:
    audit_url("http://localhost:8443", "SITE (PORT 8443)")
except Exception as e:
    print("Error on 8443:", e)

try:
    audit_url("http://localhost:8444", "PORTFOLIO-VERDE (PORT 8444)")
except Exception as e:
    print("Error on 8444:", e)

