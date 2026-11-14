import re

with open(r'C:\Users\Israel Rozar\.gemini\antigravity\brain\ec9956e5-078d-4d87-9a8e-74481434c7dc\.system_generated\steps\2781\output.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# find chapter headings (01, 02, 03... or h2 equivalents)
chapters = re.findall(r'data-name="Heading 2"[^>]*>[\s\S]*?<p[^>]*>([^<]+)</p>', text)
print(f"Chapter Headings in Figma 59:2 ({len(chapters)}):")
for i, c in enumerate(chapters):
    print(f"  {i+1}: {c.strip()}")

# find all images and their captions
figures = re.findall(r'data-name="CaseFigure"[\s\S]*?data-name="Figcaption"[^>]*>[\s\S]*?<p[^>]*>([^<]+)</p>', text)
print(f"\nFigures in Figma 59:2 ({len(figures)}):")
for i, f in enumerate(figures):
    print(f"  Figure {i+1}: {f.strip()[:100]}...")

