import os
from PIL import Image, ImageDraw, ImageFont

# Open clean protrombina crop
im = Image.open('site/public/images/hiae-componente-protrombina-crop.webp').convert('RGBA')
w, h = im.size
print("Base image size:", w, h)

# We want 4 circular badges:
# Background: #CBF637 (Lime: r=203, g=246, b=55)
# Border: #0A3622 (Pine: r=10, g=54, b=34)
# Text: #0A3622, bold, centered

def draw_badge(img, x, y, number, radius=22):
    # Draw at 4x for smooth antialiased circles
    scale = 4
    s_radius = radius * scale
    badge = Image.new('RGBA', (s_radius * 2, s_radius * 2), (0, 0, 0, 0))
    draw = ImageDraw.Draw(badge)
    
    # Circle fill
    draw.ellipse((2, 2, s_radius * 2 - 3, s_radius * 2 - 3), fill=(203, 246, 55, 255), outline=(10, 54, 34, 255), width=scale * 2)
    
    # Number text
    try:
        font = ImageFont.truetype("arialbd.ttf", 22 * scale)
    except:
        font = ImageFont.load_default()
    
    text = str(number)
    # text bbox
    bbox = draw.textbbox((0, 0), text, font=font)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    tx = (s_radius * 2 - tw) // 2
    ty = (s_radius * 2 - th) // 2 - (scale * 2)
    draw.text((tx, ty), text, fill=(10, 54, 34, 255), font=font)
    
    badge = badge.resize((radius * 2, radius * 2), Image.Resampling.LANCZOS)
    img.paste(badge, (x - radius, y - radius), badge)

# Coordinates matching the user reference print:
# Badge 1: next to TEMPO DE PROTROMBINA (RNI),
draw_badge(im, 595, 110, 1)

# Badge 2: next to Atividade:
draw_badge(im, 120, 175, 2)

# Badge 3: next to Resultado / 79
draw_badge(im, 475, 225, 3)

# Badge 4: next to Referência / %
draw_badge(im, 1220, 175, 4)

# Save to public and dist in both projects
destinations = [
    'site/public/images/hiae-componente-protrombina-crop.webp',
    'site/dist/images/hiae-componente-protrombina-crop.webp',
    'portfolio-verde/public/images/hiae-componente-protrombina-crop.webp',
    'portfolio-verde/dist/images/hiae-componente-protrombina-crop.webp'
]

im_rgb = im.convert('RGB')
for d in destinations:
    im_rgb.save(d, 'WEBP', quality=95)
    print("Saved badge-annotated image to", d)

im.save(r'C:\Users\Israel Rozar\.gemini\antigravity\brain\ec9956e5-078d-4d87-9a8e-74481434c7dc\test_protrombina_badged.png')
print("Done creating badged protrombina")

