import os
from PIL import Image

image_dir = "site/public/images"
hiae_files = [f for f in os.listdir(image_dir) if "hiae" in f and not f.startswith("preview_")]

for f in hiae_files:
    p = os.path.join(image_dir, f)
    try:
        im = Image.open(p)
        print(f"{f:45s} | size: {im.size} | mode: {im.mode}")
    except Exception as e:
        print(f"Error {f}: {e}")

