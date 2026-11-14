import re
from pathlib import Path

txt_path = Path(r"C:\Users\Israel Rozar\.gemini\antigravity\brain\ec9956e5-078d-4d87-9a8e-74481434c7dc\.system_generated\steps\3047\output.txt")
text = txt_path.read_text(encoding="utf-8")

data_names = re.findall(r'data-name="([^"]+)"', text)
print(f"Total data-names found: {len(data_names)}")
unique_names = list(dict.fromkeys(data_names))
print("Unique data-names (first 60):")
for n in unique_names[:60]:
    print(f" - {n}")

# Search for main structural sections
sections = re.findall(r'<div[^>]*data-name="([^"]*Section[^"]*|[^"]*Hero[^"]*|[^"]*Header[^"]*|[^"]*Footer[^"]*|[^"]*Capítulo[^"]*|[^"]*Story[^"]*|[^"]*Case[^"]*)"[^>]*>', text, re.IGNORECASE)
print(f"\nPotential section names: {len(sections)}")
for s in list(dict.fromkeys(sections))[:40]:
    print(f" * {s}")

