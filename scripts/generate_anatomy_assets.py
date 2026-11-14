import os
from PIL import Image

src_path = 'tmp/einstein-notion-assets/Group_71412.png'
raw = Image.open(src_path).convert('RGBA')

# 1. ASSET 1: Complete Trio (Original + Anotado + Taxonomia)
# Content bbox is (3, 2, 2860, 1567)
trio_crop = raw.crop((0, 0, 2870, 1568))
w1, h1 = trio_crop.size

# Generous studio canvas padding: 60px left, 140px right (for text breathing room), 60px top, 70px bottom
pad_l, pad_r, pad_t, pad_b = 60, 140, 60, 70
canvas1_w = w1 + pad_l + pad_r
canvas1_h = h1 + pad_t + pad_b

canvas1 = Image.new('RGBA', (canvas1_w, canvas1_h), (252, 249, 242, 255))
canvas1.paste(trio_crop, (pad_l, pad_t), trio_crop)

# Resize to 2400px width Retina
trio_2400 = canvas1.resize((2400, int(canvas1_h * (2400 / canvas1_w))), Image.Resampling.LANCZOS)
trio_rgb = trio_2400.convert('RGB')
trio_rgb.save('site/public/images/hiae-anatomia-completa-trio.webp', 'WEBP', quality=95)
trio_rgb.save('site/dist/images/hiae-anatomia-completa-trio.webp', 'WEBP', quality=95)
trio_rgb.save('portfolio-verde/public/images/hiae-anatomia-completa-trio.webp', 'WEBP', quality=95)
trio_rgb.save('portfolio-verde/dist/images/hiae-anatomia-completa-trio.webp', 'WEBP', quality=95)
print(f"Asset 1 (Trio) saved: {trio_rgb.size}")

# 2. ASSET 2: Macro Specimen (Anotado + Taxonomia)
# Crop center page + right annotations: x=1120 to 2870, y=15 to 1560
macro_crop = raw.crop((1120, 15, 2870, 1560))
w2, h2 = macro_crop.size

pad2_l, pad2_r, pad2_t, pad2_b = 60, 100, 50, 60
canvas2_w = w2 + pad2_l + pad2_r
canvas2_h = h2 + pad2_t + pad2_b

canvas2 = Image.new('RGBA', (canvas2_w, canvas2_h), (252, 249, 242, 255))
canvas2.paste(macro_crop, (pad2_l, pad2_t), macro_crop)

# Resize to 2000px width Retina
macro_2000 = canvas2.resize((2000, int(canvas2_h * (2000 / canvas2_w))), Image.Resampling.LANCZOS)
macro_rgb = macro_2000.convert('RGB')
macro_rgb.save('site/public/images/hiae-anatomia-specimen-macro.webp', 'WEBP', quality=95)
macro_rgb.save('site/dist/images/hiae-anatomia-specimen-macro.webp', 'WEBP', quality=95)
macro_rgb.save('portfolio-verde/public/images/hiae-anatomia-specimen-macro.webp', 'WEBP', quality=95)
macro_rgb.save('portfolio-verde/dist/images/hiae-anatomia-specimen-macro.webp', 'WEBP', quality=95)
print(f"Asset 2 (Macro) saved: {macro_rgb.size}")
