from pathlib import Path

css_site = Path("site/src/index.css").read_text(encoding="utf-8")
css_pv = Path("portfolio-verde/src/index.css").read_text(encoding="utf-8")

def get_header(css):
    idx = css.find(".site-header")
    return css[idx:idx+600]

print("=== SITE .site-header ===")
print(get_header(css_site))
print("\n=== PV .site-header ===")
print(get_header(css_pv))

