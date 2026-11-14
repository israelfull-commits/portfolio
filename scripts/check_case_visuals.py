import re

with open('site/src/pages/ItauPreparationCase.tsx', 'r', encoding='utf-8') as f:
    text = f.read()

# Find case blocks
cases_keys = ["registros-atendimento", "vencimentos", "movimentacoes", "hub-liquidez", "campanhas"]
for key in cases_keys:
    pos = text.find(f'"{key}":')
    if pos != -1:
        # find visuals in this block
        end_pos = text.find('decisions:', pos)
        next_case_pos = text.find('title:', pos + len(key) + 10)
        block = text[pos:pos+2500]
        v_pos = block.find('visuals:')
        if v_pos != -1:
            print(f"=== Case: {key} ===")
            print(block[v_pos:v_pos+600])
        else:
            print(f"=== Case: {key} (NO VISUALS) ===")

