import re

files = [
    'site/src/pages/Home.tsx',
    'site/src/components/CasePresentation.tsx',
    'site/src/components/SiteChrome.tsx'
]

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        text = f.read()
    
    print(f"=== {file} ===")
    # Look for section id="contato" or similar
    lines = text.split('\n')
    for i, line in enumerate(lines):
        if 'id="contato"' in line or 'className="pf-contact' in line or 'className="cp-contact' in line or 'id="cp-contato' in line:
            start = max(0, i - 1)
            end = min(len(lines), i + 40)
            print(f"Found around line {i}:")
            print('\n'.join(lines[start:end]))
            print("-" * 50)

