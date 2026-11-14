from pathlib import Path
import re

css = Path("site/src/components/case-presentation.css").read_text(encoding="utf-8")
font_matches = re.findall(r'font[^;]+;', css)
for m in set(font_matches):
    print("-", m)

