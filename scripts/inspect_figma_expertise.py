from pathlib import Path

txt_path = Path(r"C:\Users\Israel Rozar\.gemini\antigravity\brain\ec9956e5-078d-4d87-9a8e-74481434c7dc\.system_generated\steps\3279\output.txt")
text = txt_path.read_text(encoding="utf-8")

idx = text.find("Discovery e estratégia")
if idx != -1:
    print("=== FIGMA 370:16614 EXPERTISE ===")
    print(text[idx-300:idx+2000])
else:
    idx2 = text.find("Posicionamento")
    print("=== FIGMA 370:16614 POSICIONAMENTO ===")
    print(text[idx2-100:idx2+2000])

