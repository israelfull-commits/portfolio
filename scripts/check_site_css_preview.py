from pathlib import Path

css = Path("site/src/portfolio.css").read_text(encoding="utf-8")
print("pf-project-preview in site/src/portfolio.css:", "pf-project-preview" in css)
idx = css.find("pf-project")
print(css[idx:idx+1000])

