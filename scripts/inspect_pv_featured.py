from pathlib import Path

css_pv = Path("portfolio-verde/src/portfolio.css").read_text(encoding="utf-8")
idx = css_pv.find(".pf-featured")
print(css_pv[idx:idx+1000])

