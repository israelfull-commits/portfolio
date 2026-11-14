with open(r'C:\Users\Israel Rozar\.gemini\antigravity\brain\ec9956e5-078d-4d87-9a8e-74481434c7dc\.system_generated\steps\2781\output.txt', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('export default function VigenteEinsteinConsumoDeResultadosIsraelRozar')
end_pos = len(text)

# Let's inspect sections from pos to pos+12000
chunk = text[pos:pos+15000]

import re
# Find all text strings in chunk
matches = re.findall(r'>\s*([^<>\n]+)\s*<', chunk)
cleaned = [m.strip() for m in matches if m.strip() and not m.strip().startswith('{')]
print("First 50 text nodes in 59:2:")
for t in cleaned[:50]:
    print("  ", t)

