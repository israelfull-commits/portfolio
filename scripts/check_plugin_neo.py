with open(r'C:\Users\Israel Rozar\figma-refine-plugin\code.js', 'r', encoding='utf-8') as f:
    c = f.read()

for i, line in enumerate(c.split('\n')):
    if 'neoenergia' in line.lower():
        print(f"{i+1}: {line}")

