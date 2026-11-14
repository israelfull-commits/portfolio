from PIL import Image, ImageDraw, ImageFilter, ImageFont
import math

def create_studio_mockup():
    # Source high-res image: 2000x1125
    src = Image.open("site/public/images/hiae-estado-proposto-anotado.webp").convert("RGBA")
    
    # Canvas dimensions (16:9 widescreen canvas: 2400 x 1350)
    canvas_w, canvas_h = 2400, 1350
    
    # Elegant studio background with very soft radial warmth matching #F6F3EC
    bg = Image.new("RGBA", (canvas_w, canvas_h), (242, 239, 230, 255))
    
    # Device / Window container dimensions
    win_w = 2080
    # Window header height
    header_h = 56
    
    # Scale source to fit window content
    content_w = win_w
    content_h = int(src.height * (content_w / src.width))
    src_scaled = src.resize((content_w, content_h), Image.Resampling.LANCZOS)
    
    total_win_h = header_h + content_h
    
    # Create window surface with rounded corners (radius 24)
    win_img = Image.new("RGBA", (win_w, total_win_h), (255, 255, 255, 255))
    draw_win = ImageDraw.Draw(win_img)
    
    # Draw Window Header (Mac / Studio browser bar)
    draw_win.rectangle([(0, 0), (win_w, header_h)], fill=(248, 246, 240, 255))
    draw_win.line([(0, header_h), (win_w, header_h)], fill=(225, 220, 208, 255), width=2)
    
    # Draw 3 subtle traffic lights (14px diameter)
    dot_y = header_h // 2
    dots = [
        (48, (255, 95, 87)),   # Red
        (76, (255, 189, 46)),  # Yellow
        (104, (39, 201, 63))   # Green
    ]
    for x, color in dots:
        r = 7
        draw_win.ellipse([(x - r, dot_y - r), (x + r, dot_y + r)], fill=color)
        
    # URL bar / Title pill in header
    pill_w = 640
    pill_h = 32
    pill_x0 = (win_w - pill_w) // 2
    pill_y0 = (header_h - pill_h) // 2
    draw_win.rounded_rectangle([(pill_x0, pill_y0), (pill_x0 + pill_w, pill_y0 + pill_h)], radius=16, fill=(238, 235, 226, 255), outline=(220, 215, 202, 255), width=1)
    
    # Paste scaled content below header
    win_img.paste(src_scaled, (0, header_h))
    
    # Draw border directly on win_img
    draw_win.rounded_rectangle([(0, 0), (win_w - 1, total_win_h - 1)], radius=24, outline=(210, 205, 190, 255), width=2)
    
    # Mask window with rounded corners
    mask = Image.new("L", (win_w, total_win_h), 0)
    draw_mask = ImageDraw.Draw(mask)
    draw_mask.rounded_rectangle([(0, 0), (win_w, total_win_h)], radius=24, fill=255)
    
    # Multi-layer soft studio shadow
    # Layer 1: Deep ambient blur
    shadow_pad = 120
    shadow_w = win_w + shadow_pad * 2
    shadow_h = total_win_h + shadow_pad * 2
    shadow_layer = Image.new("RGBA", (shadow_w, shadow_h), (0, 0, 0, 0))
    draw_s = ImageDraw.Draw(shadow_layer)
    
    # Soft shadow box
    s_x0 = shadow_pad
    s_y0 = shadow_pad + 28
    draw_s.rounded_rectangle([(s_x0, s_y0), (s_x0 + win_w, s_y0 + total_win_h)], radius=28, fill=(10, 54, 34, 45))
    shadow_layer = shadow_layer.filter(ImageFilter.GaussianBlur(36))
    
    # Composite shadow onto bg
    win_pos_x = (canvas_w - win_w) // 2
    win_pos_y = (canvas_h - total_win_h) // 2 + 10
    
    bg.paste(shadow_layer, (win_pos_x - shadow_pad, win_pos_y - shadow_pad), shadow_layer)
    
    # Composite window onto bg
    bg.paste(win_img, (win_pos_x, win_pos_y), mask)
    
    # Save as high-res webp and png
    out_webp = "site/public/images/hiae-mockup-studio-pro.webp"
    out_png = "site/public/images/hiae-mockup-studio-pro.png"
    bg.convert("RGB").save(out_webp, "WEBP", quality=95)
    bg.convert("RGB").save(out_png, "PNG")
    print(f"Generated {out_webp} and {out_png} ({canvas_w}x{canvas_h})")

if __name__ == "__main__":
    create_studio_mockup()

