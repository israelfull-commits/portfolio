from PIL import Image

for name in [
    "hiae-estado-proposto-anotado-preview.webp",
    "hiae-capa-editorial-1600.webp",
    "hiae-ds-componentes-crop-1600.webp",
    "hiae-taxonomia-laudo-1000.webp",
    "hiae-multicanal-web-celular.webp"
]:
    p = f"site/public/images/{name}"
    try:
        im = Image.open(p)
        print(f"{name}: {im.size}, aspect: {im.size[0]/im.size[1]:.2f}")
    except Exception as e:
        print(f"{name}: {e}")

