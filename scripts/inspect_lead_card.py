from pathlib import Path

txt_path = Path(r"C:\Users\Israel Rozar\.gemini\antigravity\brain\ec9956e5-078d-4d87-9a8e-74481434c7dc\.system_generated\steps\3047\output.txt")
text = txt_path.read_text(encoding="utf-8")

idx = text.find('Leadership Card in Forest Green')
print("=== LEADERSHIP CARD ===")
print(text[idx:idx+1500])

