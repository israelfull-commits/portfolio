import json
import re

with open(r'C:\Users\Israel Rozar\.gemini\antigravity\brain\ec9956e5-078d-4d87-9a8e-74481434c7dc\.system_generated\steps\2781\output.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's extract everything from VigenteEinsteinConsumoDeResultadosIsraelRozar
pos = text.find('export default function VigenteEinsteinConsumoDeResultadosIsraelRozar')
func_text = text[pos:]

# Find all data-names and their immediate contents
blocks = re.findall(r'data-name="([^"]+)"[\s\S]*?<p[^>]*>([^<]+)</p>', func_text)
print(f"Total named blocks: {len(blocks)}")

# Let's save a structured text file of all content in node 59:2
with open('output/figma_59_2_full_content.txt', 'w', encoding='utf-8') as out:
    for name, content in blocks:
        out.write(f"[{name}]\n{content.strip()}\n\n")

print("Saved output/figma_59_2_full_content.txt")

