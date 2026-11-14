from PIL import Image

descriptions = {
    "hiae-multicanal-web-celular.webp": "Mockup 3D contemporâneo com dois dispositivos: um desktop monitor exibindo a página web do laudo e um smartphone na frente exibindo o app mobile do laudo com interface elegante.",
    "hiae-laudo-proposta-demonstrativa-1600.webp": "Interface limpa de alta fidelidade do laudo médico completo, com cabeçalho institucional do Einstein, parâmetros do exame de sangue, gráficos de referência, observações clínicas e assinatura do patologista clínico.",
    "hiae-capa-editorial-1600.webp": "Capa editorial estilizada de Design System, com tipografia, grid modular, paleta de cores e anatomia dos módulos de laudos.",
    "hiae-taxonomia-laudo-2000.webp": "Prancha completa de taxonomia de design de informação clínica: mostra a dissecação da anatomia de cada campo (título, método, material, resultado, valor de referência, notas explicativas).",
    "hiae-documentacao-design-system.png": "Documentação técnica oficial do Design System no Figma: bibliotecas de componentes, variantes, tokens de espaçamento e regras de acessibilidade WCAG.",
    "hiae-visao-futura-ressonancia.webp": "Interface conceitual futura para exames de imagem complexos (Ressonância Magnética com cortes tomográficos e painel de achados radiológicos)."
}

for k, v in descriptions.items():
    im = Image.open(f"site/public/images/{k}")
    print(f"[{k}] ({im.size[0]}x{im.size[1]}):\n  -> {v}\n")

