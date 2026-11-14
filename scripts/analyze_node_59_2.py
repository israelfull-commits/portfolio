import re

with open(r'C:\Users\Israel Rozar\.gemini\antigravity\brain\ec9956e5-078d-4d87-9a8e-74481434c7dc\.system_generated\steps\2781\output.txt', 'r', encoding='utf-8') as f:
    text = f.read()

names = re.findall(r'data-name="([^"]+)"', text)
print("Unique data-name:", len(set(names)))
for n in list(dict.fromkeys(names))[:35]:
    print("  ", n)

for line in text.splitlines():
    if "function " in line:
        print("Function:", line.strip())

