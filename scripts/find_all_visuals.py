with open('site/src/pages/ItauPreparationCase.tsx', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'visuals:' in line or 'src:' in line:
        print(f"{i+1}: {line.strip()[:100]}")

