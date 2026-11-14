import re
from pathlib import Path

txt_path = Path(r"C:\Users\Israel Rozar\.gemini\antigravity\brain\ec9956e5-078d-4d87-9a8e-74481434c7dc\.system_generated\steps\3047\output.txt")
text = txt_path.read_text(encoding="utf-8")

# Extract colors, fonts, font sizes, margins, paddings, borders
fonts = set(re.findall(r"font-\['([^']+)'\]", text))
colors = set(re.findall(r"#[0-9a-fA-F]{3,8}", text))
bg_colors = set(re.findall(r"bg-\[([^\]]+)\]", text))
text_colors = set(re.findall(r"text-\[([^\]]+)\]", text))
paddings = set(re.findall(r"p[xytb]?-\[([^\]]+)\]", text))

print("=== FONTS ===")
for f in sorted(fonts):
    print(f" - {f}")

print("\n=== TOP COLORS ===")
for c in sorted(colors):
    print(f" - {c}")

print("\n=== TEXT COLORS ===")
for tc in sorted(text_colors):
    print(f" - {tc}")

print("\n=== BG COLORS ===")
for bc in sorted(bg_colors):
    print(f" - {bc}")

