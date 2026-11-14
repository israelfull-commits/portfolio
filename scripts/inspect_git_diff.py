import subprocess

def run_cmd(cmd):
    res = subprocess.run(cmd, shell=True, capture_output=True, text=True, encoding='utf-8', errors='replace')
    return res.stdout

print("=== Diff summary of modified files ===")
for path in ['site/src/pages/Home.tsx', 'site/src/components/SiteChrome.tsx', 'site/src/components/PageMeta.tsx', 'site/index.html', 'site/src/index.css']:
    diff = run_cmd(f'git diff {path}')
    print(f"\n--- {path} (diff length: {len(diff)} chars) ---")
    lines = diff.splitlines()
    # print up to 40 lines
    for l in lines[:40]:
        print(" ", l)

