from PIL import Image

for f in [
    "hiae-capa-editorial-1600.webp",
    "hiae-documentacao-design-system.png",
    "hiae-ds-componentes-crop-1600.webp",
    "hiae-estado-proposto-anotado.webp",
    "hiae-taxonomia-laudo-2000.webp",
    "hiae-multicanal-web-celular.webp",
    "hiae-laudo-proposta-demonstrativa-1600.webp"
]:
    im = Image.open(f"site/public/images/{f}")
    # copy a resized preview to scripts/
    thumb = im.copy()
    thumb.thumbnail((800, 600))
    clean_name = f.replace(".webp", "").replace(".png", "")
    thumb.save(f"scripts/preview_{clean_name}.png")
    print(f"Generated scripts/preview_{clean_name}.png")

