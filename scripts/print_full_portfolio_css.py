from pathlib import Path

css = Path("site/src/portfolio.css").read_text(encoding="utf-8")
print(css)

