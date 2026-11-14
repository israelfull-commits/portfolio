with open('site/src/pages/Home.tsx', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i in range(200, 260):
    if i < len(lines):
        print(f"{i+1}: {lines[i]}", end='')

