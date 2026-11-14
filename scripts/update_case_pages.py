with open('site/src/pages/CasePages.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update einsteinImages and einsteinHero
old_einstein_images = '''const einsteinImages: CaseImage[] = [
  {
    src: "/images/hiae-template-fonte.png",'''

new_einstein_images = '''const einsteinHero: CaseImage = {
  src: "/images/hiae-capa-editorial-1600.webp",
  width: 1600,
  height: 900,
  alt: "Taxonomia do Design System e modelagem visual modular dos laudos do Hospital Israelita Albert Einstein",
  caption:
    "Taxonomia oficial do Design System: anatomia de campos, tokens tipográficos e componentes modulares para estruturação de laudos laboratoriais.",
}

const einsteinImages: CaseImage[] = [
  {
    src: "/images/hiae-template-fonte.png",'''

if old_einstein_images in content:
    content = content.replace(old_einstein_images, new_einstein_images, 1)
    print("Added einsteinHero")
else:
    print("Could not find old_einstein_images")

# Update einsteinPresentation hero
old_einstein_hero = '''  kicker: "Saúde · Laudos Médicos",

  hero: einsteinImages[0],'''

new_einstein_hero = '''  kicker: "Saúde · Laudos Médicos",

  hero: einsteinHero,'''

if old_einstein_hero in content:
    content = content.replace(old_einstein_hero, new_einstein_hero, 1)
    print("Updated einsteinPresentation hero")
else:
    print("Could not find old_einstein_hero")

# 2. Add hiae-ds-componentes-crop-1600.webp to Einstein Chapter 4 (Decisões)
old_einstein_decisions = '''          ].map(([title, copy]) => (
            <li key={title}>
              <h3>{title}</h3>
              <p>{copy}</p>
            </li>
          ))}
        </ol>'''

new_einstein_decisions = '''          ].map(([title, copy]) => (
            <li key={title}>
              <h3>{title}</h3>
              <p>{copy}</p>
            </li>
          ))}
        </ol>
        <CaseFigure
          image={{
            src: "/images/hiae-ds-componentes-crop-1600.webp",
            width: 1600,
            height: 900,
            alt: "Documentação dos componentes DataField e ExamTitle com tokens e anatomia modular",
            caption:
              "Documentação dos componentes estruturais: DataField e ExamTitle com tokens de espaçamento e regras de anatomia modular.",
          }}
        />'''

if old_einstein_decisions in content:
    content = content.replace(old_einstein_decisions, new_einstein_decisions, 1)
    print("Added Design System evidence crop to Einstein Chapter 4")
else:
    print("Could not find old_einstein_decisions")

# 3. Update claroHero
old_claro_hero_def = '''const claroImages: CaseImage[] = ['''

new_claro_hero_def = '''const claroHero: CaseImage = {
  src: "/images/claro-capa-editorial-1600.webp",
  width: 1600,
  height: 900,
  alt: "Visão editorial multicanal da Ativação Simplificada Claro: interfaces desktop e mobile com resumo financeiro integrado",
  caption:
    "Ecossistema multicanal: composição de interfaces desktop e mobile com carrinho de contratação em tempo real e detalhamento transparente de planos.",
}

const claroImages: CaseImage[] = ['''

if old_claro_hero_def in content:
    content = content.replace(old_claro_hero_def, new_claro_hero_def, 1)
    print("Added claroHero")
else:
    print("Could not find old_claro_hero_def")

old_claro_hero_ref = '''  kicker: "Telecom · Enterprise UX",

  hero: claroImages[0],'''

new_claro_hero_ref = '''  kicker: "Telecom · Enterprise UX",

  hero: claroHero,'''

if old_claro_hero_ref in content:
    content = content.replace(old_claro_hero_ref, new_claro_hero_ref, 1)
    print("Updated claroPresentation hero")
else:
    print("Could not find old_claro_hero_ref")

# 4. Add neoenergia blueprint crop to neoenergia chapter 4
old_neo_decisions = '''          ].map(([title, copy]) => (
            <li key={title}>
              <h3>{title}</h3>
              <p>{copy}</p>
            </li>
          ))}
        </ol>'''

# find second occurrence for neoenergia
parts = content.split(old_neo_decisions)
if len(parts) >= 3:
    # parts[0] is before einstein (which was already replaced above)
    # parts[1] is between einstein and neoenergia
    # parts[2] is after neoenergia
    new_neo_decisions = '''          ].map(([title, copy]) => (
            <li key={title}>
              <h3>{title}</h3>
              <p>{copy}</p>
            </li>
          ))}
        </ol>
        <CaseFigure
          image={{
            src: "/images/neoenergia-blueprint-crop-contrato-1600.webp",
            width: 1600,
            height: 900,
            alt: "Recorte focal do Blueprint 1: Contrato e Instalação com jornada do cliente e pontos de contato da operação",
            caption:
              "Recorte editorial do Blueprint 1 (Contrato e Instalação): detalhamento da jornada do cliente, evidências físicas e pontos de contato da operação.",
          }}
        />'''
    content = parts[0] + old_neo_decisions + parts[1] + new_neo_decisions + parts[2]
    print("Added Blueprint crop to Neoenergia Chapter 4")
else:
    print(f"parts length: {len(parts)}")

# 5. Update ItauPresentation visuals filter
old_visuals_filter = '''  const visuals =
    project.visuals?.filter(
      (image) =>
        !/planejamento-iniciativas|prototipo-completo|kbs-produtos|campanhas-screenflow|movimentacoes-discovery/.test(
          image.src,
        ),
    ) || []'''

new_visuals_filter = '''  const visuals = project.visuals || []'''

if old_visuals_filter in content:
    content = content.replace(old_visuals_filter, new_visuals_filter, 1)
    print("Updated visuals filter in ItauPresentation")
else:
    print("Could not find old_visuals_filter")

with open('site/src/pages/CasePages.tsx', 'w', encoding='utf-8') as f:
    f.write(content)

print("Saved updated CasePages.tsx")

