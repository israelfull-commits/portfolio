with open('site/src/pages/CasePages.tsx', 'r', encoding='utf-8') as f:
    text = f.read()

import re
pos = text.find('einsteinPresentation')
end_pos = text.find('claroPresentation')
chunk = text[pos:end_pos]

titles = re.findall(r'title:\s*"([^"]+)"', chunk)
print("Einstein Titles in CasePages.tsx:")
for i, t in enumerate(titles):
    print(f"  {i+1}: {t}")

