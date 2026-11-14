with open('site/src/pages/CasePages.tsx', 'r', encoding='utf-8') as f:
    text = f.read()

target = '<div className="cp-gallery">\n            <CaseFigure\n              image={{\n                src: "/images/neoenergia-blueprint-2-uso-pago.webp",'
replacement = '''<div className="cp-gallery">
            <CaseFigure
              image={{
                src: "/images/neoenergia-blueprint-crop-contrato-1600.webp",
                width: 1600,
                height: 900,
                alt: "Recorte editorial em alta resolução do Blueprint 1: Contrato e Instalação com jornada do cliente e pontos de contato da operação",
                caption:
                  "Recorte editorial do Blueprint 1 (Contrato e Instalação): visão de alta densidade da jornada do cliente, evidências físicas e pontos de contato da linha de frente.",
              }}
            />
            <CaseFigure
              image={{
                src: "/images/neoenergia-blueprint-2-uso-pago.webp",'''

if target in text:
    text = text.replace(target, replacement, 1)
    with open('site/src/pages/CasePages.tsx', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Inserted blueprint crop into Neoenergia Chapter 5")
else:
    print("Target not found in Neoenergia Chapter 5")

