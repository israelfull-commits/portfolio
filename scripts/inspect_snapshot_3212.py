from pathlib import Path

txt_path = Path(r"C:\Users\Israel Rozar\.gemini\antigravity\brain\ec9956e5-078d-4d87-9a8e-74481434c7dc\.system_generated\steps\3212\output.txt")
text = txt_path.read_text(encoding="utf-8")
print("Snapshot length:", len(text))
print(text[:2500])

