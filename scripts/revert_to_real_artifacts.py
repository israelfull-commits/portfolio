import glob, os, re

# 1. Revert CasePages.tsx heroes
with open('site/src/pages/CasePages.tsx', 'r', encoding='utf-8') as f:
    case_pages = f.read()

# Einstein
case_pages = re.sub(
    r"kicker:\s*'Saúde · Laudos Médicos',\s*hero:\s*\{[^\}]+\},",
    "kicker: 'Saúde · Laudos Médicos',\n  hero: einsteinImages[0],",
    case_pages
)

# Claro
case_pages = re.sub(
    r"kicker:\s*'Telecom · Enterprise UX',\s*hero:\s*\{[^\}]+\},",
    "kicker: 'Telecom · Enterprise UX',\n  hero: claroImages[0],",
    case_pages
)

# Neoenergia
case_pages = re.sub(
    r"kicker:\s*'Utilities · Service Design & Discovery',\s*hero:\s*\{[^\}]+\},",
    """kicker: 'Utilities · Service Design & Discovery',
  hero: {
    src: '/images/neoenergia-capa-conexao-digital.webp',
    width: 1600,
    height: 900,
    alt: 'Capa oficial do projeto P&D Conexão Digital Neoenergia com consórcio EY e Livework',
    caption: 'Artefato original de P&D Conexão Digital ANEEL: Experiência do Consumidor e Service Design para o Grupo Neoenergia (Iberdrola Brasil).',
  },""",
    case_pages
)

with open('site/src/pages/CasePages.tsx', 'w', encoding='utf-8') as f:
    f.write(case_pages)
print("SUCCESS: Reverted heroes in CasePages.tsx to real project artifacts!")

# 2. Revert ItauPreparationCase.tsx
with open('site/src/pages/ItauPreparationCase.tsx', 'r', encoding='utf-8') as f:
    itau = f.read()

mockup_block = '''      {
        src: "/images/mockup-hero-itau-liquidez.webp",
        width: 1376,
        height: 768,
        alt: "Instalação física e mockup 3D volumétrico da Matriz de Liquidez B2B",
        label: "Direção de Arte e Mockup 3D · Matriz de Liquidez",
        caption:
          "Instalação escultural com blocos de acrílico flutuantes sobre pedestal de basalto negro escuro, representando a projeção temporal e a densidade analítica da mesa de operações.",
      },
'''

if mockup_block in itau:
    itau = itau.replace(mockup_block, '')
    with open('site/src/pages/ItauPreparationCase.tsx', 'w', encoding='utf-8') as f:
        f.write(itau)
    print("SUCCESS: Removed synthetic mockup from hub-liquidez visuals in ItauPreparationCase.tsx!")

# 3. Remove generated mockup files from site/public/images/
dest_dir = r"c:\Users\Israel Rozar\Documents\ChatGPT\Portfolio\site\public\images"
for f in glob.glob(os.path.join(dest_dir, "mockup-hero-*")):
    os.remove(f)
    print(f"Deleted synthetic file: {f}")

