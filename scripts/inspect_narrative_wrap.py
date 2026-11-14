from pathlib import Path

txt_path = Path(r"C:\Users\Israel Rozar\.gemini\antigravity\brain\ec9956e5-078d-4d87-9a8e-74481434c7dc\.system_generated\steps\3047\output.txt")
text = txt_path.read_text(encoding="utf-8")

idx = text.find('data-name="Deep Dive Narrative: Sticky Sub-navigation + Content"')
print("=== DEEP DIVE NARRATIVE WRAPPER ===")
print(text[idx-200:idx+800])

