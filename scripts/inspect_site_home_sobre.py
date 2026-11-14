from pathlib import Path

text = Path("site/src/pages/Home.tsx").read_text(encoding="utf-8")
idx = text.find('id="sobre"')
if idx != -1:
    print("=== SITE HOME.TSX (#sobre) ===")
    print(text[idx-100:idx+2500])
else:
    print("Not found by id='sobre'")

