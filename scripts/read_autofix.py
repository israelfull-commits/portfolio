import json, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('output/autofix-pagina30-registro.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

print('Target:', d.get('target'))
print(f"Number of before items: {len(d.get('before', []))}")
for b in d.get('before', []):
    print(f"ID: {b.get('id')} | Name: {b.get('name')} | Frames: {b.get('frames')} | Texts: {b.get('texts')} | Overflows: {b.get('overflowCount')}")

print("\nPasses:")
for p in d.get('passes', []):
    print(f"Pass {p.get('pass')}: modified={p.get('modified')} | details={p.get('details')}")

print("\nValidation:")
print(d.get('validation'))

