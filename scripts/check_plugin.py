with open(r'C:\Users\Israel Rozar\figma-refine-plugin\code.js', 'r', encoding='utf-8') as f:
    c = f.read()

import re
print('Has neoenergia in code.js?', 'neoenergia' in c.lower())
# Find case keys or objects
for line in c.split('\n')[:80]:
    if 'id:' in line or 'title:' in line or 'case' in line.lower():
        print(line.strip())

