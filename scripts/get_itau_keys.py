with open('site/src/pages/CasePages.tsx', encoding='utf-8') as f:
    text = f.read()

import re
match = re.search(r'const itauNarratives = \{([\s\S]*?)\n\};', text)
if match:
    for m in re.finditer(r'^  ([\"\w-]+): \{', match.group(1), re.M):
        print(m.group(1))
