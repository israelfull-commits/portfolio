with open('site/src/pages/Home.tsx', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('Projetos selecionados')
if pos == -1:
    pos = text.find('Trabalho')
print(text[pos:pos+3500])

