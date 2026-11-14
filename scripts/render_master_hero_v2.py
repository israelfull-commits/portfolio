import os
from PIL import Image, ImageDraw, ImageFilter, ImageFont

# 1. Load pristine original asset
src = Image.open('tmp/einstein-notion-assets/Group_71412.png')

# 2. Exact non-clipped crops
# Sheet 1: (15, 44, 1215, 1470)
# Sheet 2: (1158, 44, 2358, 1470)
s1_raw = src.crop((15, 44, 1215, 1470))
s2_raw = src.crop((1158, 44, 2358, 1470))

raw_w, raw_h = 1200, 1426
sheet_w = 780
sheet_h = int(raw_h * (sheet_w / raw_w)) # 927 px

s1 = s1_raw.resize((sheet_w, sheet_h), Image.Resampling.LANCZOS)
s2 = s2_raw.resize((sheet_w, sheet_h), Image.Resampling.LANCZOS)

# 3. Canvas setup: 2560 x 1440
canvas_w = 2560
canvas_h = 1440
canvas = Image.new('RGBA', (canvas_w, canvas_h), (252, 249, 242, 255)) # #FCF9F2

s1_x = 90
s1_y = 240
s2_x = 920
s2_y = 240

def create_studio_sheet(sheet_img):
    w, h = sheet_img.size
    pad = 90
    box_w = w + pad * 2
    box_h = h + pad * 2
    
    # Layer 1: Contact shadow
    shadow_base = Image.new('RGBA', (box_w, box_h), (0, 0, 0, 0))
    d1 = ImageDraw.Draw(shadow_base)
    d1.rounded_rectangle((pad, pad + 6, pad + w, pad + h + 6), radius=8, fill=(12, 38, 25, 48))
    shadow_base = shadow_base.filter(ImageFilter.GaussianBlur(5))
    
    # Layer 2: Medium ambient occlusion
    layer2 = Image.new('RGBA', (box_w, box_h), (0, 0, 0, 0))
    ImageDraw.Draw(layer2).rounded_rectangle((pad, pad + 16, pad + w, pad + h + 16), radius=12, fill=(12, 38, 25, 30))
    layer2 = layer2.filter(ImageFilter.GaussianBlur(18))
    shadow_base = Image.alpha_composite(shadow_base, layer2)
    
    # Layer 3: Atmospheric soft diffusion
    layer3 = Image.new('RGBA', (box_w, box_h), (0, 0, 0, 0))
    ImageDraw.Draw(layer3).rounded_rectangle((pad, pad + 32, pad + w, pad + h + 32), radius=16, fill=(12, 38, 25, 18))
    layer3 = layer3.filter(ImageFilter.GaussianBlur(40))
    shadow_base = Image.alpha_composite(shadow_base, layer3)
    
    # Sheet 1px crisp architectural border
    bordered_sheet = sheet_img.copy()
    b_draw = ImageDraw.Draw(bordered_sheet)
    b_draw.rounded_rectangle((0, 0, w - 1, h - 1), radius=6, outline=(12, 38, 25, 26), width=1)
    
    shadow_base.paste(bordered_sheet, (pad, pad), bordered_sheet)
    return shadow_base, pad

s1_staged, pad1 = create_studio_sheet(s1)
s2_staged, pad2 = create_studio_sheet(s2)

canvas.paste(s1_staged, (s1_x - pad1, s1_y - pad1), s1_staged)
canvas.paste(s2_staged, (s2_x - pad2, s2_y - pad2), s2_staged)

# 4. Top Headers & Typography
draw = ImageDraw.Draw(canvas)

font_bold_title = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 28)
font_tax_head = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 26)
font_tax_item = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 19)
font_pill = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 13)
font_caption = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 16)

# Eyebrow Pills above sheets
def draw_pill(x, y, text, is_active=False):
    bbox = draw.textbbox((0, 0), text, font=font_pill)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    pw, ph = tw + 28, th + 14
    bg_col = (235, 244, 238, 255) if is_active else (240, 238, 232, 255)
    border_col = (54, 138, 92, 100) if is_active else (140, 145, 140, 80)
    text_col = (18, 85, 48, 255) if is_active else (80, 95, 88, 255)
    
    draw.rounded_rectangle((x, y, x + pw, y + ph), radius=ph//2, fill=bg_col, outline=border_col, width=1)
    draw.text((x + 14, y + 6), text, font=font_pill, fill=text_col)

draw_pill(s1_x, s1_y - 48, "01  ·  DOCUMENTO FONTE (ORIGINAL)", is_active=False)
draw_pill(s2_x, s2_y - 48, "02  ·  ANATOMIA SISTÊMICA (DESIGN SYSTEM)", is_active=True)

# 5. Brackets & Taxonomy Hierarchy
scale = sheet_h / raw_h

# Region 1: Peach (Metodologia)
p_top = s2_y + int(284 * scale)
p_bot = s2_y + int(416 * scale)
p_mid = (p_top + p_bot) // 2

# Region 2: Green (Resultado)
g_top = s2_y + int(434 * scale)
g_bot = s2_y + int(1120 * scale)
g_mid = (g_top + g_bot) // 2

# Region 3: Purple (Conclusão diagnóstica)
u_top = s2_y + int(1134 * scale)
u_bot = s2_y + int(1248 * scale)
u_mid = (u_top + u_bot) // 2

bracket_x = s2_x + sheet_w + 14
tax_x = bracket_x + 90

# Palette
col_peach = (226, 115, 85, 255)
col_green = (42, 153, 94, 255)
col_purple = (142, 92, 195, 255)
col_heading = (24, 32, 28, 255)
col_item = (48, 58, 52, 255)

# --- PEACH SECTION (Metodologia) ---
# Bracket hugging peach region
draw.line([(bracket_x, p_top), (bracket_x + 28, p_top), (bracket_x + 28, p_bot), (bracket_x, p_bot)], fill=col_peach, width=3)
# Connecting line stepping up to Metodologia title underline at y=235
draw.line([(bracket_x + 28, p_top), (bracket_x + 28, 235), (tax_x - 14, 235)], fill=col_peach, width=3)

# Title & underline
draw.text((tax_x, 196), "Metodologia", font=font_tax_head, fill=col_heading)
draw.line([(tax_x, 235), (tax_x + 160, 235)], fill=col_peach, width=3)

# Items
met_items = [
    "Material",
    "Radiofármaco",
    "Indicador",
    "Tempo",
    "Cortes tomográficos nos planos",
    "Técnica (método)",
    "Indicação clínica (prescrição)"
]
cur_y = 250
for it in met_items:
    draw.text((tax_x + 8, cur_y), it, font=font_tax_item, fill=col_item)
    cur_y += 31

# --- GREEN SECTION (Resultado) ---
draw.line([(bracket_x, g_top), (bracket_x + 28, g_top), (bracket_x + 28, g_bot), (bracket_x, g_bot)], fill=col_green, width=3)
# Horizontal arm at y=685
draw.line([(bracket_x + 28, 685), (tax_x - 14, 685)], fill=col_green, width=3)

draw.text((tax_x, 646), "Resultado", font=font_tax_head, fill=col_heading)
draw.line([(tax_x, 685), (tax_x + 130, 685)], fill=col_green, width=3)

res_items = ["Relatório (análise)", "Achados"]
cur_y = 700
for it in res_items:
    draw.text((tax_x + 8, cur_y), it, font=font_tax_item, fill=col_item)
    cur_y += 31

# --- PURPLE SECTION (Conclusão diagnóstica) ---
draw.line([(bracket_x, u_top), (bracket_x + 28, u_top), (bracket_x + 28, u_bot), (bracket_x, u_bot)], fill=col_purple, width=3)
# Horizontal arm at y=1035
draw.line([(bracket_x + 28, 1035), (tax_x - 14, 1035)], fill=col_purple, width=3)

draw.text((tax_x, 996), "Conclusão diagnóstica", font=font_tax_head, fill=col_heading)
draw.line([(tax_x, 1035), (tax_x + 275, 1035)], fill=col_purple, width=3)

draw.text((tax_x + 8, 1050), "Impressão", font=font_tax_item, fill=col_item)

# Bottom Studio Caption
draw.text((s1_x, canvas_h - 44), "Taxonomia oficial do Design System: anatomia de campos, tokens tipográficos e componentes modulares para estruturação de laudos.", font=font_caption, fill=(110, 125, 118, 255))

# Export Master
final_rgb = canvas.convert('RGB')
final_rgb.save(r'C:\Users\Israel Rozar\.gemini\antigravity\brain\ec9956e5-078d-4d87-9a8e-74481434c7dc\master_hero_v2.png')

destinations = [
    'site/public/images/hiae-capa-editorial-1600.webp',
    'site/dist/images/hiae-capa-editorial-1600.webp',
    'portfolio-verde/public/images/hiae-capa-editorial-1600.webp',
    'portfolio-verde/dist/images/hiae-capa-editorial-1600.webp'
]
for d in destinations:
    final_rgb.save(d, 'WEBP', quality=95)

print("Master Hero v2 generated and deployed successfully!")
