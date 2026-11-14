from pathlib import Path
import re

css_index = Path("site/src/index.css").read_text(encoding="utf-8")
css_portfolio = Path("site/src/portfolio.css").read_text(encoding="utf-8")

def get_selectors(css):
    return set(re.findall(r'([.#][a-zA-Z0-9_-]+)', css))

sels_index = get_selectors(css_index)
sels_port = get_selectors(css_portfolio)

common = sorted(sels_index & sels_port)
print(f"Common selectors defined in both index.css and portfolio.css ({len(common)}):")
for c in common:
    print(" -", c)

