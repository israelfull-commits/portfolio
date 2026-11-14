from pathlib import Path
import re

txt_path = Path(r"C:\Users\Israel Rozar\.gemini\antigravity\brain\ec9956e5-078d-4d87-9a8e-74481434c7dc\.system_generated\steps\3279\output.txt")
text = txt_path.read_text(encoding="utf-8")

matches = re.findall(r'<p[^>]*>([^<]+)</p>', text)
print(f"Total <p> matches: {len(matches)}")
for i, m in enumerate(matches):
    if any(k in m for k in ["Discovery", "ponte", "Posicionamento", "Expertise", "craft", "IA", "Sistemas", "negócio"]):
        print(f"[{i}] {m}")

