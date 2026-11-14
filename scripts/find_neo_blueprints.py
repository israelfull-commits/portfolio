with open('site/src/pages/CasePages.tsx', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('Os 5 estágios do ciclo de vida do cliente mapeados em Service Blueprints')
if pos == -1:
    pos = text.find('Os 5')
print(text[pos:pos+1200])

