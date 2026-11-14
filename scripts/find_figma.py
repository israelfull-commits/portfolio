import os, glob, re

matches = []
files = glob.glob('*.md') + glob.glob('site/src/**/*', recursive=True) + glob.glob('C:/Users/Israel Rozar/.gemini/antigravity/brain/ec9956e5-078d-4d87-9a8e-74481434c7dc/*.md')

pattern = re.compile(r'https://(?:www\.)?figma\.com/(?:file|design)/[a-zA-Z0-9]+[^\s"\'\)>]*')

for f in files:
    if os.path.isfile(f):
        try:
            with open(f, 'r', encoding='utf-8', errors='ignore') as fl:
                c = fl.read()
                for m in pattern.finditer(c):
                    matches.append((m.group(0), f))
        except Exception:
            pass

seen = set()
for url, src in matches:
    clean_url = url.split('?')[0]
    if clean_url not in seen:
        seen.add(clean_url)
        print(f"{url} | {src}")
