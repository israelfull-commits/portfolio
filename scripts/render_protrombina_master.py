import os
from PIL import Image, ImageDraw, ImageFilter, ImageFont

# Canvas dimensions: 1800 x 640
canvas_w = 1800
canvas_h = 640
canvas = Image.new('RGBA', (canvas_w, canvas_h), (252, 249, 242, 255)) # #FCF9F2

# Outer frame dimensions
frame_w = 1680
frame_h = 520
frame_x = (canvas_w - frame_w) // 2 # 60
frame_y = (canvas_h - frame_h) // 2 # 60

# 1. Multi-tier studio drop shadow for the frame
pad = 60
shadow_layer = Image.new('RGBA', (frame_w + pad*2, frame_h + pad*2), (0, 0, 0, 0))
s_draw = ImageDraw.Draw(shadow_layer)

# Contact shadow
s_draw.rounded_rectangle((pad, pad + 8, pad + frame_w, pad + frame_h + 8), radius=24, fill=(10, 36, 22, 50))
shadow_layer = shadow_layer.filter(ImageFilter.GaussianBlur(6))

# Ambient occlusion
layer2 = Image.new('RGBA', (frame_w + pad*2, frame_h + pad*2), (0, 0, 0, 0))
ImageDraw.Draw(layer2).rounded_rectangle((pad, pad + 20, pad + frame_w, pad + frame_h + 20), radius=28, fill=(10, 36, 22, 30))
layer2 = layer2.filter(ImageFilter.GaussianBlur(22))
shadow_layer = Image.alpha_composite(shadow_layer, layer2)

# Large diffusion
layer3 = Image.new('RGBA', (frame_w + pad*2, frame_h + pad*2), (0, 0, 0, 0))
ImageDraw.Draw(layer3).rounded_rectangle((pad, pad + 38, pad + frame_w, pad + frame_h + 38), radius=32, fill=(10, 36, 22, 16))
layer3 = layer3.filter(ImageFilter.GaussianBlur(45))
shadow_layer = Image.alpha_composite(shadow_layer, layer3)

canvas.paste(shadow_layer, (frame_x - pad, frame_y - pad), shadow_layer)

# 2. Draw outer dark green frame
draw = ImageDraw.Draw(canvas)
frame_color = (16, 43, 29, 255) # Deep forest pine #102B1D
draw.rounded_rectangle((frame_x, frame_y, frame_x + frame_w, frame_y + frame_h), radius=22, fill=frame_color)

# 3. Draw inner white card
card_pad = 42
card_x = frame_x + card_pad
card_y = frame_y + card_pad
card_w = frame_w - card_pad * 2
card_h = frame_h - card_pad * 2

draw.rounded_rectangle((card_x, card_y, card_x + card_w, card_y + card_h), radius=14, fill=(255, 255, 255, 255))

# 4. Typography setup
font_eyebrow = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 14)
font_title = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 25)
font_sub = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 14)
font_label = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 18)
font_colhead = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 15)
font_val = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 21)
font_val_norm = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 21)
font_badge = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 15)

# Eyebrow
draw.text((card_x + 50, card_y + 36), "PROTÓTIPO DOCUMENTADO  ·  v3", font=font_eyebrow, fill=(37, 99, 235, 255))

# Blue vertical accent bar
draw.rounded_rectangle((card_x + 50, card_y + 70, card_x + 55, card_y + 120), radius=2, fill=(30, 58, 138, 255))

# Title & subtitle
draw.text((card_x + 72, card_y + 68), "TEMPO DE PROTROMBINA (RNI),", font=font_title, fill=(26, 32, 28, 255))
draw.text((card_x + 72, card_y + 102), "PLASMA", font=font_sub, fill=(100, 116, 139, 255))

# Helper to draw lime circular callout badges
def draw_callout_badge(cx, cy, number_str):
    r = 17
    # Soft badge shadow
    draw.ellipse((cx - r, cy - r + 2, cx + r, cy + r + 2), fill=(10, 36, 22, 40))
    # Lime fill with crisp dark border
    draw.ellipse((cx - r, cy - r, cx + r, cy + r), fill=(162, 236, 75, 255), outline=(16, 43, 29, 255), width=2)
    # Text centered
    bbox = draw.textbbox((0, 0), number_str, font=font_badge)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    draw.text((cx - tw//2, cy - th//2 - 2), number_str, font=font_badge, fill=(16, 43, 29, 255))

# Badge 1: next to title
draw_callout_badge(card_x + 520, card_y + 82, "1")

# Helper to draw a verified checkmark icon inside result boxes
def draw_check_icon(cx, cy):
    r = 13
    draw.ellipse((cx - r, cy - r, cx + r, cy + r), fill=(34, 139, 64, 255))
    # White checkmark lines
    draw.line([(cx - 6, cy), (cx - 2, cy + 5), (cx + 6, cy - 4)], fill=(255, 255, 255, 255), width=3)

# Column coordinates
col_label_x = card_x + 50
col_res_x = card_x + 390
col_res_w = 460
col_ref_x = card_x + 900
col_ref_w = 580

# --- ROW 1: ATIVIDADE ---
r1_y = card_y + 175
draw.text((col_label_x, r1_y + 18), "Atividade:", font=font_label, fill=(26, 32, 28, 255))
# Badge 2
draw_callout_badge(col_label_x + 108, r1_y + 28, "2")

# Headers
draw.text((col_res_x, r1_y - 8), "Resultado", font=font_colhead, fill=(100, 116, 139, 255))
draw.text((col_ref_x, r1_y - 8), "Referência", font=font_colhead, fill=(100, 116, 139, 255))

# Result input pill
draw.rounded_rectangle((col_res_x, r1_y + 14, col_res_x + col_res_w, r1_y + 64), radius=8, fill=(241, 245, 249, 255), outline=(203, 213, 225, 255), width=1)
draw_check_icon(col_res_x + 28, r1_y + 39)
draw.text((col_res_x + 56, r1_y + 26), "79", font=font_val, fill=(26, 32, 28, 255))

# Badge 3: directly to the left of the result pill
draw_callout_badge(col_res_x - 32, r1_y + 39, "3")

# Reference input pill
draw.rounded_rectangle((col_ref_x, r1_y + 14, col_ref_x + col_ref_w, r1_y + 64), radius=8, fill=(255, 255, 255, 255), outline=(203, 213, 225, 255), width=1)
draw.text((col_ref_x + 24, r1_y + 26), "70 - 100", font=font_val_norm, fill=(26, 32, 28, 255))
draw.text((col_ref_x + col_ref_w - 38, r1_y + 26), "%", font=font_colhead, fill=(100, 116, 139, 255))

# Badge 4: directly to the right of reference box
draw_callout_badge(col_ref_x + col_ref_w + 34, r1_y + 39, "4")

# --- ROW 2: RELAÇÃO (RNI) ---
r2_y = card_y + 280
draw.text((col_label_x, r2_y + 18), "Relação (RNI):", font=font_label, fill=(26, 32, 28, 255))

# Headers
draw.text((col_res_x, r2_y - 8), "Resultado", font=font_colhead, fill=(100, 116, 139, 255))
draw.text((col_ref_x, r2_y - 8), "Referência", font=font_colhead, fill=(100, 116, 139, 255))

# Result input pill
draw.rounded_rectangle((col_res_x, r2_y + 14, col_res_x + col_res_w, r2_y + 64), radius=8, fill=(241, 245, 249, 255), outline=(203, 213, 225, 255), width=1)
draw_check_icon(col_res_x + 28, r2_y + 39)
draw.text((col_res_x + 56, r2_y + 26), "1,16", font=font_val, fill=(26, 32, 28, 255))

# Reference input pill
draw.rounded_rectangle((col_ref_x, r2_y + 14, col_ref_x + col_ref_w, r2_y + 64), radius=8, fill=(255, 255, 255, 255), outline=(203, 213, 225, 255), width=1)
draw.text((col_ref_x + 24, r2_y + 26), "0,96 - 1,30", font=font_val_norm, fill=(26, 32, 28, 255))

# Export Master
final_rgb = canvas.convert('RGB')
final_rgb.save(r'C:\Users\Israel Rozar\.gemini\antigravity\brain\ec9956e5-078d-4d87-9a8e-74481434c7dc\master_protrombina_v2.png')

destinations = [
    'site/public/images/hiae-componente-protrombina-crop.webp',
    'site/dist/images/hiae-componente-protrombina-crop.webp',
    'portfolio-verde/public/images/hiae-componente-protrombina-crop.webp',
    'portfolio-verde/dist/images/hiae-componente-protrombina-crop.webp'
]
for d in destinations:
    final_rgb.save(d, 'WEBP', quality=95)

print("Master Protrombina Crop v2 generated and deployed successfully!")
