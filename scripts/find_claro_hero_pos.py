with open('site/src/pages/CasePages.tsx', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('claroPresentation')
print(text[pos-400:pos+300])

