from pathlib import Path
import re

css = Path("site/src/components/case-presentation.css").read_text(encoding="utf-8")
print("CSS Length:", len(css))

# Look at variables defined at the top
top_vars = re.findall(r'--[a-zA-Z0-9_-]+:[^;]+;', css[:1000])
print("Top vars:")
for v in top_vars:
    print(" ", v)

