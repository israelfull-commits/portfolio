from pathlib import Path
import re

txt_path = Path(r"C:\Users\Israel Rozar\.gemini\antigravity\brain\ec9956e5-078d-4d87-9a8e-74481434c7dc\.system_generated\steps\3279\output.txt")
text = txt_path.read_text(encoding="utf-8")

matches = re.findall(r'<p[^>]*>([^<]+)</p>', text)
for i, m in enumerate(matches):
    print(f"[{i}] {m}")

