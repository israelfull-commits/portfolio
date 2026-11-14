with open('site/src/pages/Home.tsx', 'r', encoding='utf-8') as f:
    text = f.read()

old_intro = '''              <div className="roadmap-intro">
                <Text>
                  Problemas, decisões e aprendizados organizados em páginas
                  próprias. Os relatos distinguem propostas de resultados
                  demonstrados.
                </Text>
                <Text>
                  As evidências visuais serão ampliadas em atualizações
                  posteriores.
                </Text>
              </div>'''

new_intro = '''              <div className="roadmap-intro">
                <Text>
                  Problemas, decisões e aprendizados organizados em páginas
                  próprias. Os relatos distinguem propostas de resultados
                  demonstrados.
                </Text>
                <Text>
                  Todas as páginas contam com evidências reais de handoff,
                  telas canônicas em alta resolução 16:9 e recortes focais de discovery.
                </Text>
              </div>'''

if old_intro in text:
    text = text.replace(old_intro, new_intro, 1)
    with open('site/src/pages/Home.tsx', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Updated roadmap-intro in Home.tsx")
else:
    print("Could not find old_intro in Home.tsx")

