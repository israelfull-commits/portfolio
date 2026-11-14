import re
import os

with open('site/src/pages/CasePages.tsx', 'r', encoding='utf-8') as f:
    text = f.read()

cases_info = [
    ('Einstein', 'export function EinsteinPresentation', 'export function ClaroPresentation'),
    ('Claro', 'export function ClaroPresentation', 'export function NeoenergiaPresentation'),
    ('Neoenergia', 'export function NeoenergiaPresentation', 'export function ItauPresentation'),
    ('Itau', 'export function ItauPresentation', None)
]

for name, start_tok, end_tok in cases_info:
    start = text.find(start_tok)
    end = text.find(end_tok) if end_tok else len(text)
    block = text[start:end]
    
    images = re.findall(r'src:\s*[\"\']([^\"\']+)[\"\']', block)
    chapters = re.findall(r'title:\s*[\"\']([^\"\']+)[\"\']', block)
    
    print(f'=== {name} ===')
    print(f'Length: {len(block)} chars')
    print(f'Chapters count: {len(chapters)}')
    for ch in chapters[:6]:
        print(f'  - {ch}')
    print(f'Images count: {len(images)}')
    for img in images:
        exists = os.path.exists(f'site/public{img}') or os.path.exists(f'site{img}')
        print(f'  - {img} (exists: {exists})')
    print()

