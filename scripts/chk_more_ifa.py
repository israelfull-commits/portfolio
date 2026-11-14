from PIL import Image

def chk(p):
    im = Image.open(p)
    print(f"{p}: {im.size} {im.format} {im.mode}")

chk("output/figma/ifa-evidencias-2026-11-01/01-planejamento-iniciativas.png")
chk("output/figma/ifa-evidencias-2026-11-01/07-ifa-prototipo-completo.png")
chk("output/figma/ifa-evidencias-2026-11-01/08-kbs-produtos-itau.png")

