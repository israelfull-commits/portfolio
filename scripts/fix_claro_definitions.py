with open('site/src/pages/CasePages.tsx', 'r', encoding='utf-8') as f:
    text = f.read()

target = 'export const claroPresentation: CasePresentationData = {'
replacement = '''const claroHero: CaseImage = {
  src: "/images/claro-capa-editorial-1600.webp",
  width: 1600,
  height: 900,
  alt: "Visão editorial multicanal da Ativação Simplificada Claro: interfaces desktop e mobile com resumo financeiro integrado",
  caption:
    "Ecossistema multicanal: composição de interfaces desktop e mobile com carrinho de contratação em tempo real e detalhamento transparente de planos.",
}

const claroImages: CaseImage[] = [
  {
    src: "/images/claro-ativacao-desktop.webp",
    width: 775,
    height: 486,
    alt: "Ativação desktop com resumo financeiro lateral",
    caption:
      "Ativação e resumo da oferta: composição financeira visível durante a escolha do produto.",
  },
  {
    src: "/images/claro-workshop.webp",
    width: 720,
    height: 720,
    alt: "Workshop do projeto com post-its na parede",
    caption: "Registro de workshop colaborativo do acervo original.",
  },
  {
    src: "/images/claro-jornadas.webp",
    width: 720,
    height: 720,
    alt: "Mapa da jornada de troca de chip no Miro",
    caption:
      "Validações, etapas da troca de chip, resumo e oferta organizados na jornada.",
  },
  {
    src: "/images/claro-multicanal.webp",
    width: 1376,
    height: 932,
    alt: "Composição de interfaces desktop e mobile",
    caption:
      "Propostas históricas para desktop e mobile, com agrupamentos de oferta e serviços.",
  },
  {
    src: "/images/claro-detalhe-linha.webp",
    width: 775,
    height: 486,
    alt: "Detalhe da linha com dados do cliente e grupos expansíveis",
    caption:
      "Cliente, linha, plano e fatura agrupados, com acesso às jornadas relacionadas.",
  },
  {
    src: "/images/claro-confirmacao-mobile.webp",
    width: 280,
    height: 606,
    alt: "Confirmação mobile da troca de chip",
    caption:
      "Confirmação mobile reúne cliente, linha, chip e promoção. Exportação original de 280 px.",
  },
]

export const claroPresentation: CasePresentationData = {'''

if target in text:
    text = text.replace(target, replacement, 1)
    with open('site/src/pages/CasePages.tsx', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Inserted claroHero and claroImages successfully.")
else:
    print("Target not found!")

