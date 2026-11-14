from pathlib import Path
import re

txt_path = Path(r"C:\Users\Israel Rozar\.gemini\antigravity\brain\ec9956e5-078d-4d87-9a8e-74481434c7dc\.system_generated\steps\3279\output.txt")
text = txt_path.read_text(encoding="utf-8")

# Let's inspect paddings, gaps, and widths in step 3279 (Figma 370:16614)
print("=== FIGMA 370:16614 LAYOUT DATA ===")
# Find containers and frames
frames = re.findall(r'<frame[^>]+name="([^"]+)"[^>]*width="([^"]+)"[^>]*height="([^"]+)"[^>]*>', text)
for f in frames[:25]:
    print(f"Frame: {f[0]} ({f[1]} x {f[2]})")

