import glob, re, sys
sys.stdout.reconfigure(encoding='utf-8')

pattern = re.compile(r'https?://[^\s"\'\)>]+', re.IGNORECASE)
urls = set()

for f in glob.glob('*.md'):
    try:
        with open(f, 'r', encoding='utf-8', errors='ignore') as fl:
            for m in pattern.finditer(fl.read()):
                u = m.group(0)
                if any(k in u.lower() for k in ['israel', 'portfolio', 'vercel', 'pages', 'preview']):
                    urls.add((u, f))
    except:
        pass

for u, f in sorted(urls):
    print(f"{u} ({f})")

