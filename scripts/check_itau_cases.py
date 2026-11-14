with open('site/src/pages/ItauPreparationCase.tsx', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'title:' in line or 'export const cases' in line:
        print(f"{i+1}: {line.strip()}")

