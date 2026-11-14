import glob, os, shutil
from PIL import Image

brain_dir = r"C:\Users\Israel Rozar\.gemini\antigravity\brain\ec9956e5-078d-4d87-9a8e-74481434c7dc"
dest_dir = r"c:\Users\Israel Rozar\Documents\ChatGPT\Portfolio\site\public\images"

targets = {
    "mockup_hero_neoenergia": "mockup-hero-neoenergia",
    "mockup_hero_einstein": "mockup-hero-einstein",
    "mockup_hero_claro": "mockup-hero-claro",
    "mockup_hero_itau_liquidez": "mockup-hero-itau-liquidez"
}

for prefix, dest_name in targets.items():
    matches = glob.glob(os.path.join(brain_dir, f"{prefix}_*.jpg"))
    if matches:
        src = matches[0]
        # Open with PIL
        with Image.open(src) as img:
            w, h = img.size
            print(f"{prefix}: {w}x{h}")
            
            # Save as webp
            webp_path = os.path.join(dest_dir, f"{dest_name}.webp")
            img.save(webp_path, "WEBP", quality=90)
            print(f"Saved: {webp_path} ({os.path.getsize(webp_path)} bytes)")
            
            # Save as jpg
            jpg_path = os.path.join(dest_dir, f"{dest_name}.jpg")
            img.save(jpg_path, "JPEG", quality=92)
            print(f"Saved: {jpg_path} ({os.path.getsize(jpg_path)} bytes)")

