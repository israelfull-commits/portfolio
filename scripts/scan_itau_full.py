import re, sys

sys.stdout.reconfigure(encoding='utf-8')

with open('site/src/pages/ItauPreparationCase.tsx', 'r', encoding='utf-8') as f:
    text = f.read()

# Keys
keys = ['registros-atendimento', 'vencimentos', 'movimentacoes', 'hub-liquidez', 'campanhas']
for k in keys:
    start = text.find(f'"{k}":')
    if start != -1:
        # find next key or end of object
        next_pos = len(text)
        for nk in keys:
            if nk != k:
                p = text.find(f'"{nk}":', start + len(k))
                if p != -1 and p < next_pos:
                    next_pos = p
        case_block = text[start:next_pos]
        title_m = re.search(r'title:\s*\"([^\"]+)\"', case_block)
        title = title_m.group(1) if title_m else k
        visuals = re.findall(r'src:\s*\"([^\"]+)\"', case_block)
        print(f"[{k}] {title}: {len(visuals)} visuals -> {visuals}")

