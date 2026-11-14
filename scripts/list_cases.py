import re

for base in ['site', 'portfolio-verde']:
    path = f'{base}/src/pages/CasePages.tsx'
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find all CasePresentation usages or exports
    cases = re.findall(r'export function (\w+CasePage)', content)
    titles = re.findall(r'title:\s*\"([^\"]+)\"', content)
    urls = re.findall(r'shareUrl:\s*\"([^\"]+)\"', content)
    
    print(f'=== {base} ===')
    print('Exported Case Components:', cases)
    print('Case URLs:', urls)

