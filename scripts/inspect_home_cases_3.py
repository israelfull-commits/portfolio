with open('site/src/pages/Home.tsx', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines[550:650]):
    print(f"{i+551}: {line}", end='')

