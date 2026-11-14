with open('site/src/pages/ItauPreparationCase.tsx', encoding='utf-8') as f:
    text = f.read()

import re
cases = re.findall(r'\"([a-z-]+)\":\s*\{', text)
print("ItauPreparationCase cases:", cases)
