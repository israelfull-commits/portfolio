import glob

files = glob.glob('*.md') + glob.glob('site/src/**/*', recursive=True) + glob.glob('C:/Users/Israel Rozar/.gemini/antigravity/brain/ec9956e5-078d-4d87-9a8e-74481434c7dc/*.md')

for f in files:
    try:
        with open(f, 'r', encoding='utf-8', errors='ignore') as fl:
            c = fl.read()
            if '67:2' in c or 'Template-portfolio' in c or 'Template portfolio' in c:
                for line in c.split('\n'):
                    if '67:2' in line or 'Template' in line or 'node-id=' in line:
                        if 'figma' in line.lower():
                            print(f"{f}: {line.strip()}")
    except Exception:
        pass

