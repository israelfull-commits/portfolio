with open('site/src/pages/CasePages.tsx', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('Sistematização de templates e limites declarados de validação')
if pos == -1:
    pos = text.find('Sistematiza')
print(text[pos:pos+3000])

