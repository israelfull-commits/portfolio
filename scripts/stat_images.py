from PIL import Image, ImageStat

files = [
    "preview_hiae-capa-editorial-1600.png",
    "preview_hiae-documentacao-design-system.png",
    "preview_hiae-ds-componentes-crop-1600.png",
    "preview_hiae-estado-proposto-anotado.png",
    "preview_hiae-taxonomia-laudo-2000.png",
    "preview_hiae-multicanal-web-celular.png",
    "preview_hiae-laudo-proposta-demonstrativa-1600.png"
]

for f in files:
    im = Image.open(f"scripts/{f}")
    stat = ImageStat.Stat(im)
    print(f"{f}: size={im.size}, mean_rgb={stat.mean[:3]}")

