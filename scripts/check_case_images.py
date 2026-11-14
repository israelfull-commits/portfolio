import os, re, sys

sys.stdout.reconfigure(encoding='utf-8')

# Check CaseImage objects in CasePages.tsx
with open('site/src/pages/CasePages.tsx', 'r', encoding='utf-8') as f:
    text = f.read()

# Match objects with src:
matches = re.findall(r"\{[^{}]*src:[^{}]*\}", text)
print(f"CasePages image objects found: {len(matches)}")
for m in matches:
    if '/images/' in m:
        has_w = 'width' in m
        has_h = 'height' in m
        has_alt = 'alt' in m
        has_caption = 'caption' in m
        print(f"Image: {re.search(r'src:\s*[\'\"]([^\'\"]+)[\'\"]', m).group(1)} | w:{has_w} h:{has_h} alt:{has_alt} caption:{has_caption}")

