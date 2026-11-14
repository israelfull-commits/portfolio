import os
from PIL import Image, ImageEnhance, ImageFilter

OUTPUT_DIR = 'site/public/images'

def make_editorial_frame(
    src_path,
    out_path,
    target_size=(1600, 900),
    crop_box=None,
    bg_color=(23, 32, 25), # dark slate forest background for matte framing
    scale_fit=True,
    add_subtle_border=True
):
    """
    Creates an editorial 16:9 master image with authentic evidence,
    crisp cropping, subtle matte framing, and premium agency polish.
    """
    if not os.path.exists(src_path):
        print(f"File not found: {src_path}")
        return False
        
    img = Image.open(src_path).convert("RGBA")
    
    if crop_box:
        img = img.crop(crop_box)
        
    w, h = img.size
    tw, th = target_size
    
    # If crop_box is not provided and aspect ratio is close to 16:9
    if scale_fit:
        # Create high-res editorial canvas with subtle gradient / luxury dark matte
        canvas = Image.new("RGBA", (tw, th), bg_color + (255,))
        
        # Calculate fit with padding
        pad_x = 40
        pad_y = 30
        max_w = tw - (pad_x * 2)
        max_h = th - (pad_y * 2)
        
        ratio = min(max_w / w, max_h / h)
        new_w = int(w * ratio)
        new_h = int(h * ratio)
        
        resized = img.resize((new_w, new_h), Image.Resampling.LANCZOS)
        
        # Add subtle shadow / border to evidence
        pos_x = (tw - new_w) // 2
        pos_y = (th - new_h) // 2
        
        # Paste onto canvas
        canvas.paste(resized, (pos_x, pos_y), resized)
        final_img = canvas.convert("RGB")
    else:
        # Direct high-res crop to 16:9
        target_ratio = tw / th
        src_ratio = w / h
        if src_ratio > target_ratio:
            # Source is wider than 16:9 -> crop sides
            new_crop_w = int(h * target_ratio)
            left = (w - new_crop_w) // 2
            cropped = img.crop((left, 0, left + new_crop_w, h))
        else:
            # Source is taller -> crop top/bottom
            new_crop_h = int(w / target_ratio)
            top = 0 # keep top aligned for UI headers
            cropped = img.crop((0, top, w, top + new_crop_h))
            
        final_img = cropped.resize((tw, th), Image.Resampling.LANCZOS).convert("RGB")
        
    # Save optimized WebP
    final_img.save(out_path, format="WEBP", quality=92, method=6)
    print(f"Created: {out_path} ({final_img.size}) from {src_path}")
    return True

print("Ready to generate covers.")

