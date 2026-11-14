from pathlib import Path
import re

txt_path = Path(r"C:\Users\Israel Rozar\.gemini\antigravity\brain\ec9956e5-078d-4d87-9a8e-74481434c7dc\.system_generated\steps\3047\output.txt")
text = txt_path.read_text(encoding="utf-8")

def find_block(name, length=1200):
    idx = text.find(f'data-name="{name}"')
    if idx != -1:
        print(f"=== {name} ===")
        print(text[idx:idx+length])
        print("\n" + "="*50 + "\n")

find_block("Metadata Specs Grid (4 Cols)", 1800)
find_block("Aside - Sticky Sidebar Case Index", 1500)
find_block("Big Lime Highlight: How Might We", 1200)
find_block("Trade-off Decision Box", 1500)
find_block("Navegação / Outros projetos", 1200)

