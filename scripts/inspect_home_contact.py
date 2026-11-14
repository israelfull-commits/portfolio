from pathlib import Path

text = Path("site/src/pages/Home.tsx").read_text(encoding="utf-8")
idx = text.find('id="contato"')
if idx != -1:
    print(text[idx-100:idx+1500])
else:
    idx2 = text.find("contato")
    print(text[idx2-100:idx2+1500])

