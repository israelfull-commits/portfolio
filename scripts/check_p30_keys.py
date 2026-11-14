import json

with open('output/autofix-pagina30-registro.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

for b in d.get('before', []):
    print(f"ID: {b.get('id')} | Name: {b.get('name')} | Keys: {list(b.keys())}")

