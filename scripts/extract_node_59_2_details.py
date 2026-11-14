import re

with open(r'C:\Users\Israel Rozar\.gemini\antigravity\brain\ec9956e5-078d-4d87-9a8e-74481434c7dc\.system_generated\steps\2781\output.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# Extract paragraphs and headings
paragraphs = re.findall(r'<p[^>]*>([^<]+)</p>', text)
print(f"Total <p> elements: {len(paragraphs)}")

# Extract images
images = re.findall(r'const (img\w+) = "([^"]+)";', text)
print("\nImages declared:")
for var, url in images:
    print(f"  {var}: {url}")

# Extract Headings (h1, h2, h3, h4)
headings = re.findall(r'<h[1-6][^>]*>([^<]+)</h[1-6]>', text)
print(f"\nHeadings found ({len(headings)}):")
for h in headings:
    print(f"  - {h.strip()}")

# Extract metrics
dd_list = re.findall(r'<dd[^>]*>([^<]+)</dd>', text)
dt_list = re.findall(r'<dt[^>]*>([^<]+)</dt>', text)
print("\nMetrics found:")
for dt, dd in zip(dt_list, dd_list):
    print(f"  {dt.strip()}: {dd.strip()}")

