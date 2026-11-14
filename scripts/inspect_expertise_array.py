from pathlib import Path

text = Path("site/src/pages/Home.tsx").read_text(encoding="utf-8")
idx = text.find('const expertise')
print(text[idx:idx+1000])

