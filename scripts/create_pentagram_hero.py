import os
from PIL import Image, ImageDraw, ImageFilter, ImageFont

# Load pristine original
src = Image.open('tmp/einstein-notion-assets/Group_71412.png')

# 1. Precise crop of Sheet 1 and Sheet 2
s1_raw = src.crop((30, 44, 1060, 1478))
s2_raw = src.crop((1150, 44, 2180, 1478))

# Target sheet dimensions on final 2560x1440 canvas:
# Width = 840, Height = int(1434 * (840/1030)) = 1170
sheet_w = 840
sheet_h = 1170
s1 = s1_raw.resize((sheet_w, sheet_h), Image.Resampling.LANCZOS)
s2 = s2_raw.resize((sheet_w, sheet_h), Image.Resampling.LANCZOS)

# Canvas settings
canvas_w = 2560
canvas_h = 1400
canvas = Image.new('RGBA', (canvas_w, canvas_h), (252, 249, 242, 255))

# Coordinates for sheets
s1_x = 70
s1_y = 100
s2_x = 960
s2_y = 100

def create_shadowed_sheet(sheet_img):
    w, h = sheet_img.size
    pad = 80
    box_w = w + pad * 2
    box_h = h + pad * 2
    
    shadow_layer = Image.new('RGBA', (box_w, box_h), (0, 0, 0, 0))
    s_draw = ImageDraw.Draw(shadow_layer)
    
    # Layer 1: Contact shadow
    s_draw.rounded_rectangle((pad, pad + 4, pad + w, pad + h + 4), radius=10, fill=(10, 54, 34, 45))
    shadow_layer = shadow_layer.filter(ImageFilter.GaussianBlur(5))
    
    # Layer 2: Ambient occlusion
    layer2 = Image.new('RGBA', (box_w, box_h), (0, 0, 0, 0))
    ImageDraw.Draw(layer2).rounded_rectangle((pad, pad + 14, pad + w, pad + h + 14), radius=14, fill=(10, 54, 34, 28))
    layer2 = layer2.filter(ImageFilter.GaussianBlur(16))
    shadow_layer = Image.alpha_composite(shadow_layer, layer2)
    
    # Layer 3: Atmospheric soft diffusion
    layer3 = Image.new('RGBA', (box_w, box_h), (0, 0, 0, 0))
    ImageDraw.Draw(layer3).rounded_rectangle((pad, pad + 28, pad + w, pad + h + 28), radius=18, fill=(10, 54, 34, 16))
    layer3 = layer3.filter(ImageFilter.GaussianBlur(36))
    shadow_layer = Image.alpha_composite(shadow_layer, layer3)
    
    # Sheet border 1px
    sheet_with_border = sheet_img.copy()
    b_draw = ImageDraw.Draw(sheet_with_border)
    b_draw.rounded_rectangle((0, 0, w - 1, h - 1), radius=8, outline=(10, 54, 34, 28), width=1)
    
    shadow_layer.paste(sheet_with_border, (pad, pad), sheet_with_border)
    return shadow_layer, pad

s1_staged, pad1 = create_shadowed_sheet(s1)
s2_staged, pad2 = create_shadowed_sheet(s2)

canvas.paste(s1_staged, (s1_x - pad1, s1_y - pad1), s1_staged)
canvas.paste(s2_staged, (s2_x - pad2, s2_y - pad2), s2_staged)

# 2. Vector Brackets & Typography
draw = ImageDraw.Draw(canvas)

# Fonts
try:
    font_h = ImageFont.truetype("arialbd.ttf", 30)
    font_item = ImageFont.truetype("arial.ttf", 21)
    font_sub = ImageFont.truetype("arial.ttf", 16)
except:
    font_h = ImageFont.load_default()
    font_item = ImageFont.load_default()
    font_sub = ImageFont.load_default()

# Vertical positions of the regions on Sheet 2 (scaled)
# Sheet 2 y = 100.
# Region 1 (Peach): scaled y from 270*(1170/1434) to 403*(1170/1434) => 220 to 329 => global y = 320 to 429
peach_top = s2_y + int(270 * (sheet_h / 1434))
peach_bot = s2_y + int(403 * (sheet_h / 1434))
peach_mid = (peach_top + peach_bot) // 2

# Region 2 (Green): scaled y from 419 to 1118 => global y = 442 to 1012
green_top = s2_y + int(419 * (sheet_h / 1434))
green_bot = s2_y + int(1118 * (sheet_h / 1434))
green_mid = (green_top + green_bot) // 2

# Region 3 (Purple): scaled y from 1118 to 1234 => global y = 1012 to 1107
purple_top = s2_y + int(1118 * (sheet_h / 1434))
purple_bot = s2_y + int(1234 * (sheet_h / 1434))
purple_mid = (purple_top + purple_bot) // 2

# Taxonomy X positions
tax_x = s2_x + sheet_w + 80
bracket_x = s2_x + sheet_w

# Peach Bracket & Text
peach_col = (226, 125, 96, 255)
# Bracket path
draw.line([(bracket_x, peach_top), (bracket_x + 30, peach_top), (bracket_x + 30, peach_bot), (bracket_x, peach_bot)], fill=peach_col, width=3)
draw.line([(bracket_x + 30, 200), (tax_x - 15, 200)], fill=peach_col, width=3)
draw.line([(bracket_x + 30, peach_mid), (bracket_x + 30, 200)], fill=peach_col, width=3)

# Metodologia Title
draw.text((tax_x, 180), "Metodologia", font=font_h, fill=(26, 32, 28, 255))
draw.line([(tax_x, 222), (tax_x + 160, 222)], fill=peach_col, width=3)

met_items = [
    "Material",
    "Radiofármaco",
    "Indicador",
    "Tempo",
    "Cortes tomográficos nos planos",
    "Técnica (método)",
    "Indicação clínica (prescrição)"
]
cur_y = 240
for it in met_items:
    draw.text((tax_x + 10, cur_y), it, font=font_item, fill=(50, 60, 54, 255))
    cur_y += 34

# Green Bracket & Text
green_col = (65, 179, 117, 255)
draw.line([(bracket_x, green_top), (bracket_x + 30, green_top), (bracket_x + 30, green_bot), (bracket_x, green_bot)], fill=green_col, width=3)
draw.line([(bracket_x + 30, 680), (tax_x - 15, 680)], fill=green_col, width=3)

draw.text((tax_x, 660), "Resultado", font=font_h, fill=(26, 32, 28, 255))
draw.line([(tax_x, 702), (tax_x + 125, 702)], fill=green_col, width=3)

res_items = ["Relatório (análise)", "Achados"]
cur_y = 720
for it in res_items:
    draw.text((tax_x + 10, cur_y), it, font=font_item, fill=(50, 60, 54, 255))
    cur_y += 34

# Purple Bracket & Text
purple_col = (155, 114, 207, 255)
draw.line([(bracket_x, purple_top), (bracket_x + 30, purple_top), (bracket_x + 30, purple_bot), (bracket_x, purple_bot)], fill=purple_col, width=3)
draw.line([(bracket_x + 30, 1020), (tax_x - 15, 1020)], fill=purple_col, width=3)

draw.text((tax_x, 1000), "Conclusão diagnóstica", font=font_h, fill=(26, 32, 28, 255))
draw.line([(tax_x, 1042), (tax_x + 290, 1042)], fill=purple_col, width=3)

draw.text((tax_x + 10, 1060), "Impressão", font=font_item, fill=(50, 60, 54, 255))

# Bottom Caption on Canvas
draw.text((s1_x, canvas_h - 60), "Exemplo: Laudo Imagem / Tomografia", font=font_sub, fill=(120, 135, 125, 255))

# Export at high quality
final_rgb = canvas.convert('RGB')
final_rgb.save(r'C:\Users\Israel Rozar\.gemini\antigravity\brain\ec9956e5-078d-4d87-9a8e-74481434c7dc\master_pentagram_hero.png')

# Deploy to all destinations
destinations = [
    'site/public/images/hiae-capa-editorial-1600.webp',
    'site/dist/images/hiae-capa-editorial-1600.webp',
    'portfolio-verde/public/images/hiae-capa-editorial-1600.webp',
    'portfolio-verde/dist/images/hiae-capa-editorial-1600.webp'
]
for d in destinations:
    final_rgb.save(d, 'WEBP', quality=95)

print("Master Pentagram Hero saved successfully!")
