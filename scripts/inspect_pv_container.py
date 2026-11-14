from pathlib import Path

css_pv = Path("portfolio-verde/src/portfolio.css").read_text(encoding="utf-8")
print(css_pv[:1000])

