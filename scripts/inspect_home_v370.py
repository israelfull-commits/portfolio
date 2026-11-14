import re

with open('site/src/pages/Home.tsx', 'r', encoding='utf-8') as f:
    text = f.read()

sections = re.findall(r'<section[^>]*id="([^"]+)"', text)
print("Sections in Home.tsx:", sections)

headings = re.findall(r'<h[1-4][^>]*>([^<]+)</h[1-4]>', text)
print("\nHeadings in Home.tsx:")
for h in headings:
    print("  -", h.strip())

# Check links in Home.tsx
links = re.findall(r'href="([^"]+)"', text)
print("\nLinks in Home.tsx:")
for l in list(dict.fromkeys(links)):
    print("  -", l)

