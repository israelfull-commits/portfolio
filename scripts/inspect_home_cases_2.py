with open('site/src/pages/Home.tsx', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines[420:550]):
    print(f"{i+421}: {line}", end='')

