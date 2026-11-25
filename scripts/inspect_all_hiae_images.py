from PIL import Image
import os

images = [
    'hiae-mockup-macbook-retina.webp',
    'hiae-mockup-studio-pro.webp',
    'hiae-laudo-proposta-demonstrativa-1600.webp',
    'hiae-multicanal-web-celular.webp',
    'hiae-capa-editorial-tight.webp',
    'hiae-capa-editorial-1600.webp',
    'hiae-taxonomia-laudo-2000.webp',
    'hiae-taxonomia-macroareas.webp'
]

for name in images:
    path = f'site/public/images/{name}'
    if os.path.exists(path):
        im = Image.open(path)
        size_kb = os.path.getsize(path) / 1024
        print(f"{name:45}: {im.size} aspect={im.width/im.height:.2f} ({size_kb:.1f} KB)")
    else:
        print(f"{name:45}: NOT FOUND")
