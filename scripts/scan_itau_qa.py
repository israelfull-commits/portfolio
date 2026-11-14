import re, sys

sys.stdout.reconfigure(encoding='utf-8')

with open('site/src/pages/ItauPreparationCase.tsx', 'r', encoding='utf-8') as f:
    text = f.read()

# Check each case for visuals
print("=== ITAU CASES QA SCAN ===")
cases_matches = re.findall(r'\"([a-zA-Z0-9_-]+)\":\s*\{\s*title:\s*\"([^\"]+)\"', text)
for slug, title in cases_matches:
    print(f"\nCase: {title} (slug: {slug})")
    # find visuals for this slug
    sub = text[text.find(f'"{slug}":'):]
    sub = sub[:sub.find('  },')]
    visuals = re.findall(r'src:\s*\"([^\"]+)\"', sub)
    print(f"  Visuals ({len(visuals)}): {visuals}")
    # check if missing or stage has 'em atualização'
    has_atualizacao = 'atualização' in sub or 'atualizacao' in sub
    print(f"  Has 'atualização' flag: {has_atualizacao}")

