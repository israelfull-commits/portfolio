from pathlib import Path

css_site = Path("site/src/portfolio.css").read_text(encoding="utf-8")
css_pv = Path("portfolio-verde/src/portfolio.css").read_text(encoding="utf-8")

def get_block(css, name):
    idx = css.find(name)
    if idx != -1:
        return css[idx:idx+600]
    return "NOT FOUND"

print("=== SITE .pf-trajectory ===")
print(get_block(css_site, ".pf-trajectory"))
print("\n=== PV .pf-trajectory ===")
print(get_block(css_pv, ".pf-trajectory"))

