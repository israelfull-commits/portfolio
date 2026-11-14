import json, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('output/autofix-pagina30-registro.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

for b in d.get('before', []):
    print(f"=== {b.get('name')} ===")
    # Look for any text samples if present
    for k, v in b.items():
        if k not in ['overflows', 'frames']:
            print(f"  {k}: {v}")

