from PIL import Image

src = Image.open('tmp/einstein-notion-assets/Group_71412.png').convert('RGBA')
w, h = src.size
pixels = src.load()

# Remove ANY dark black artifact pixels in the region between the document and annotations (x from 2100 to 2400)
for y in range(h):
    for x in range(2100, 2400):
        r, g, b, a = pixels[x, y]
        # Any dark pixel (r<80, g<80, b<80) that is not part of the colored lines:
        if a > 20 and r < 90 and g < 90 and b < 90:
            pixels[x, y] = (0, 0, 0, 0)

# Also ensure all text on the right (x >= 2350) is deep accessible charcoal (#1A201C: 26, 32, 28)
for y in range(h):
    for x in range(2350, w):
        r, g, b, a = pixels[x, y]
        if a > 30 and r < 235:
            is_colored = (r > 200 and g < 150) or (g > 140 and r < 120) or (b > 140 and g < 140)
            if not is_colored:
                pixels[x, y] = (26, 32, 28, 255)

# Tight crop
bbox = src.getbbox()
cropped = src.crop((bbox[0], bbox[1], bbox[2], bbox[3]))
cw, ch = cropped.size

# Generous studio padding
pad_l, pad_r, pad_t, pad_b = 80, 180, 80, 80
canvas_w = cw + pad_l + pad_r
canvas_h = ch + pad_t + pad_b

canvas = Image.new('RGBA', (canvas_w, canvas_h), (252, 249, 242, 255))
canvas.paste(cropped, (pad_l, pad_t), cropped)

target_w = 2400
target_h = int(canvas_h * (2400 / canvas_w))
final = canvas.resize((target_w, target_h), Image.Resampling.LANCZOS).convert('RGB')

destinations = [
    'site/public/images/hiae-capa-editorial-1600.webp',
    'site/dist/images/hiae-capa-editorial-1600.webp',
    'portfolio-verde/public/images/hiae-capa-editorial-1600.webp',
    'portfolio-verde/dist/images/hiae-capa-editorial-1600.webp'
]
for d in destinations:
    final.save(d, 'WEBP', quality=95)

final.save(r'C:\Users\Israel Rozar\.gemini\antigravity\brain\ec9956e5-078d-4d87-9a8e-74481434c7dc\hero_perfect_clean.png')
print(f"Done! Cleaned master hero: {target_w}x{target_h}")

