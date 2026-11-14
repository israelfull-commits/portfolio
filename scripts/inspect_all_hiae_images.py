from PIL import Image

files = [
    "hiae-capa-editorial-1600.webp",
    "hiae-documentacao-design-system.png",
    "hiae-ds-componentes-crop-1600.webp",
    "hiae-estado-proposto-anotado.webp",
    "hiae-laudo-proposta-demonstrativa-1600.webp",
    "hiae-taxonomia-laudo-2000.webp",
    "hiae-multicanal-web-celular.webp"
]

for f in files:
    try:
        im = Image.open(f"site/public/images/{f}")
        print(f"{f}: format={im.format}, size={im.size}, mode={im.mode}")
    except Exception as e:
        print(f"{f}: error {e}")

