from PIL import Image

candidates = [
    "hiae-multicanal-web-celular.webp",
    "hiae-laudo-proposta-demonstrativa-1600.webp",
    "hiae-capa-editorial-1600.webp",
    "hiae-taxonomia-laudo-2000.webp",
    "hiae-documentacao-design-system.png",
    "hiae-visao-futura-ressonancia.webp"
]

for c in candidates:
    im = Image.open(f"site/public/images/{c}")
    thumb = im.copy()
    thumb.thumbnail((1000, 600))
    clean = c.replace(".webp", "").replace(".png", "")
    out_path = f"C:/Users/Israel Rozar/.gemini/antigravity/brain/ec9956e5-078d-4d87-9a8e-74481434c7dc/candidate_{clean}.png"
    thumb.save(out_path)
    print(f"Saved {out_path}")

