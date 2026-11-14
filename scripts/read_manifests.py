import json, sys
sys.stdout.reconfigure(encoding='utf-8')

for fname in ['output/make-transfer-manifest.json', 'output/publication-routes.json']:
    print(f"=== {fname} ===")
    try:
        with open(fname, 'r', encoding='utf-8') as f:
            print(json.dumps(json.load(f), indent=2)[:1000])
    except Exception as e:
        print(e)

