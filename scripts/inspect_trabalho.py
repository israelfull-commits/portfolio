with open('site/src/pages/Home.tsx', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('trabalho')
print(text[pos:pos+2500])

