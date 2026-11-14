import re

with open('site/src/pages/CasePages.tsx', 'r', encoding='utf-8') as f:
    text = f.read()

# Find itauChapterTitles block
start = text.find('const itauChapterTitles')
end = text.find('const titles = itauChapterTitles')
block = text[start:end]

lines = [l.strip().strip("',") for l in block.split('\n') if l.strip().startswith("'")]
print(f"Total Itaú chapter titles: {len(lines)}")
from collections import Counter
counts = Counter(lines)
dups = {t: c for t, c in counts.items() if c > 1}
print("Duplicates in Itaú chapter titles:", dups)

