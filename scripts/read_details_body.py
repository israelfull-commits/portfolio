with open(r'C:\Users\Israel Rozar\.gemini\antigravity\brain\ec9956e5-078d-4d87-9a8e-74481434c7dc\.system_generated\steps\2781\output.txt', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = re.findall(r'data-node-id="59:(?:39|40|41)\d"[\s\S]*?<p[^>]*>([^<]+)</p>', text)
for m in matches:
    print("-", m.strip())

