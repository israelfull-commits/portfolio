from pathlib import Path

css = Path("portfolio-verde/src/portfolio.css").read_text(encoding="utf-8")
print("pf-project-preview in portfolio-verde:", "pf-project-preview" in css)
idx = css.find("pf-project-preview")
print(css[idx-100:idx+800])

