import os
from PIL import Image

src_path = 'tmp/einstein-notion-assets/Group_71412.png'
im = Image.open(src_path).convert('RGBA')

# Crop content tightly
cropped = im.crop((0, 0, 2870, 1568))

w, h = cropped.size
pixels = cropped.load()

# Darken only the text pixels on the right (x >= 2200), keeping white background and colored lines intact
for y in range(h):
    for x in range(2200, w):
        r, g, b, a = pixels[x, y]
        # Ignore transparent or near-white background
        if a > 40 and r < 230:
            is_colored_line = (r > 200 and g < 150) or (g > 140 and r < 120) or (b > 140 and g < 140)
            if not is_colored_line:
                # Text pixel! Darken to high-contrast charcoal (#1A201C)
                pixels[x, y] = (26, 32, 28, 255)

# Create clean canvas with generous padding so right text has breathing room
pad_l, pad_r, pad_t, pad_b = 60, 140, 60, 70
master_w = w + pad_l + pad_r
master_h = h + pad_t + pad_b

master = Image.new('RGBA', (master_w, master_h), (252, 249, 242, 255))
master.paste(cropped, (pad_l, pad_t), cropped)

# Target resolution: 2400px wide
target_w = 2400
target_h = int(master_h * (target_w / master_w))
final_img = master.resize((target_w, target_h), Image.Resampling.LANCZOS)

final_img.save(r'C:\Users\Israel Rozar\.gemini\antigravity\brain\ec9956e5-078d-4d87-9a8e-74481434c7dc\refined_master_anatomy_clean.png')
final_rgb = final_img.convert('RGB')
final_rgb.save(r'C:\Users\Israel Rozar\.gemini\antigravity\brain\ec9956e5-078d-4d87-9a8e-74481434c7dc\refined_master_anatomy_clean.webp', 'WEBP', quality=95)
print(f"Generated clean master anatomy: {target_w}x{target_h}")
