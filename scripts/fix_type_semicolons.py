import os, re

pattern = re.compile(r'(\b\w+:\s*[^;,{}]+)\s+(\w+:)')

for root, dirs, files in os.walk('site/src'):
    for f in files:
        if f.endswith(('.ts', '.tsx')):
            p = os.path.join(root, f)
            with open(p, 'r', encoding='utf-8') as fl:
                content = fl.read()
            
            # Find any missing semicolon/comma between type properties
            # e.g. { heading: string items: string[] }
            def repl(m):
                return m.group(1) + '; ' + m.group(2)
            
            new_content = content
            # apply until no more matches
            while True:
                mod = pattern.sub(repl, new_content)
                if mod == new_content:
                    break
                new_content = mod
            
            if new_content != content:
                print(f"Fixed missing semicolons in: {p}")
                with open(p, 'w', encoding='utf-8') as fl:
                    fl.write(new_content)

