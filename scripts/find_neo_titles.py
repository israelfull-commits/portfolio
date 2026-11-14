import re

with open('site/src/pages/CasePages.tsx', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('neoenergiaPresentation')
end_pos = text.find('export function NeoenergiaPresentation', pos)
neo_block = text[pos:end_pos]

for m in re.finditer(r'title:\s*"([^"]+)"', neo_block):
    print("Neo title:", m.group(1))

