with open('site/src/pages/ItauPreparationCase.tsx', 'r', encoding='utf-8') as f:
    text = f.read()

target = '''    visuals: [
      {
        src: "/images/itau-hub-liquidez-solucao.png",'''

replacement = '''    visuals: [
      {
        src: "/images/mockup-hero-itau-liquidez.webp",
        width: 1376,
        height: 768,
        alt: "Instalação física e mockup 3D volumétrico da Matriz de Liquidez B2B",
        label: "Direção de Arte e Mockup 3D · Matriz de Liquidez",
        caption:
          "Instalação escultural com blocos de acrílico flutuantes sobre pedestal de basalto negro escuro, representando a projeção temporal e a densidade analítica da mesa de operações.",
      },
      {
        src: "/images/itau-hub-liquidez-solucao.png",'''

if target in text:
    text = text.replace(target, replacement, 1)
    with open('site/src/pages/ItauPreparationCase.tsx', 'w', encoding='utf-8') as f:
        f.write(text)
    print("SUCCESS: Updated hub-liquidez visuals!")
else:
    print("ERROR: Target not found in ItauPreparationCase.tsx!")

