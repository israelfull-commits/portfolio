with open('site/src/pages/Home.tsx', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines[220:380]):
    print(f"{i+221}: {line}", end='')

