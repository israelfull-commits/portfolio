import re

with open('site/src/pages/ItauPreparationCase.tsx', 'r', encoding='utf-8') as f:
    text = f.read()

# Find case entries
matches = re.findall(r'(\b[a-z-]+)\s*:\s*\{[^}]*title:\s*["\']([^"\']+)["\']', text)
for m in matches:
    print(m)

# Check visuals for hub-liquidez
idx = text.find('"hub-liquidez"')
if idx == -1: idx = text.find("'hub-liquidez'")
if idx != -1:
    print(text[idx:idx+800])

