import re

with open('site/src/pages/CasePages.tsx', 'r', encoding='utf-8') as f:
    text = f.read()

# Find all 'title:' occurrences
titles = re.findall(r"title:\s*['\"]([^'\"]+)['\"]", text)
print(f"Total titles found: {len(titles)}")

# Check for duplicates
from collections import Counter
counts = Counter(titles)
duplicates = {t: c for t, c in counts.items() if c > 1}
print("Duplicate titles across CasePages.tsx:")
for t, c in duplicates.items():
    print(f"  {c}x: {t}")

