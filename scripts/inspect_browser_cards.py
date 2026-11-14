from pathlib import Path

txt_path = Path(r"C:\Users\Israel Rozar\.gemini\antigravity\brain\ec9956e5-078d-4d87-9a8e-74481434c7dc\.system_generated\steps\3372\output.txt")
text = txt_path.read_text(encoding="utf-8")

idx = text.find("Movimentações e Extrato")
print("=== CARDS IN BROWSER ===")
print(text[idx-200:idx+1200])

idx_exp = text.find("Expertise")
print("\n=== EXPERTISE IN BROWSER ===")
print(text[idx_exp-50:idx_exp+600])

