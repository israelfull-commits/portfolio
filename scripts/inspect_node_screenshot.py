from PIL import Image
import os

img_path = r'C:\Users\Israel Rozar\.gemini\antigravity\brain\ec9956e5-078d-4d87-9a8e-74481434c7dc\.system_generated\steps\2791\media_0.png'
if os.path.exists(img_path):
    with Image.open(img_path) as im:
        print(f"Screenshot size: {im.size}, format: {im.format}, mode: {im.mode}")
else:
    print("Screenshot not found")

