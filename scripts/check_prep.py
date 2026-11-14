with open('site/src/pages/ItauPreparationCase.tsx', encoding='utf-8') as f:
    lines = f.readlines()
for i, line in enumerate(lines):
    if ': {' in line and not line.strip().startswith('image:') and not line.strip().startswith('style:'):
        print(f'{i+1}: {line.strip()[:60]}')
