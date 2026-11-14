from pathlib import Path

text = Path("portfolio-verde/src/pages/Home.tsx").read_text(encoding="utf-8")
idx = text.find('const expertise')
if idx != -1:
    print("=== PORTFOLIO-VERDE EXPERTISE ===")
    print(text[idx:idx+1000])
else:
    idx2 = text.find('id="sobre"')
    print("=== PORTFOLIO-VERDE #sobre ===")
    print(text[idx2-100:idx2+1200])

