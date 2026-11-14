import json, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('output/autofix-pagina30-registro.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

print("=== PÁGINA 30:2 - ESTRUTURA DOS FRAMES ===")
for b in d.get('before', []):
    print(f"\nFrame: {b.get('name')} (ID: {b.get('id')})")
    print(f"  Frames filhos: {b.get('frames')} | Textos: {b.get('texts')} | Overflows originais: {b.get('overflowCount')}")
    if b.get('overflows'):
        print(f"  Detalhes de overflows:")
        for ov in b.get('overflows')[:5]:
            print(f"    - {ov.get('name')} (ID: {ov.get('id')}): {ov.get('w')}x{ov.get('h')} [{ov.get('layout')}]")

if 'passes' in d:
    print("\n=== PASSES EXECUTADOS NO AUTOFIX ===")
    for idx, p in enumerate(d.get('passes')):
        print(f"Pass {idx+1}: {p}")

print("\n=== VALIDAÇÃO FINAL ===")
val = d.get('validation', {})
print(f"Frames validados: {len(val.get('frames', []))}")
for vf in val.get('frames', []):
    print(f"  {vf.get('name')}: overflows={len(vf.get('overflow', []))}, clipped={vf.get('clipped')}, texts={vf.get('texts')}, images={vf.get('images')}, bodyOverflow={vf.get('bodyOverflow')}")

