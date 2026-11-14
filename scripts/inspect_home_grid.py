with open('site/src/pages/Home.tsx', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('function Home()')
print(text[idx:idx+200])

idx2 = text.find('pf-project-grid')
print(text[idx2-50:idx2+600])

