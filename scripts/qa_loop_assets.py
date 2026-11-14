import os, re, sys, glob
from PIL import Image

sys.stdout.reconfigure(encoding='utf-8')

print("=== [QA LOOP 1: ASSET INTEGRITY AUDIT] ===")
public_dir = r"c:\Users\Israel Rozar\Documents\ChatGPT\Portfolio\site\public"
missing_assets = []
checked_assets = []

# Scan all tsx files for image references
for root, dirs, files in os.walk(r"c:\Users\Israel Rozar\Documents\ChatGPT\Portfolio\site\src"):
    for f in files:
        if f.endswith(('.tsx', '.ts')):
            path = os.path.join(root, f)
            with open(path, 'r', encoding='utf-8', errors='ignore') as fl:
                content = fl.read()
                matches = re.findall(r"src:\s*['\"](/images/[^'\"]+)['\"]", content)
                for m in matches:
                    local_path = os.path.join(public_dir, m.lstrip('/\\').replace('/', os.sep))
                    checked_assets.append((m, local_path, os.path.exists(local_path)))
                    if not os.path.exists(local_path):
                        missing_assets.append((m, f))

print(f"Total image references checked: {len(checked_assets)}")
if missing_assets:
    print(f"FAILED: {len(missing_assets)} missing image(s):")
    for m, src_file in missing_assets:
        print(f"  ❌ {m} referenced in {src_file}")
else:
    print("✔ All referenced images exist on disk!")

print("\n=== [QA LOOP 2: EXPLICIT DIMENSIONS AUDIT (CLS PRESERVATION)] ===")
dimension_issues = []
for root, dirs, files in os.walk(r"c:\Users\Israel Rozar\Documents\ChatGPT\Portfolio\site\src"):
    for f in files:
        if f.endswith(('.tsx', '.ts')):
            path = os.path.join(root, f)
            with open(path, 'r', encoding='utf-8', errors='ignore') as fl:
                content = fl.read()
                # Find image object blocks with src, width, height
                img_blocks = re.findall(r"\{[^{}]*src:\s*['\"](/images/[^'\"]+)['\"][^{}]*\}", content)
                for block in img_blocks:
                    has_width = 'width:' in block or 'width :' in block
                    has_height = 'height:' in block or 'height :' in block
                    if not (has_width and has_height):
                        dimension_issues.append((block, f))

print(f"Total image objects inspected: {len(img_blocks)}")
if dimension_issues:
    print(f"WARNING: {len(dimension_issues)} image object(s) lack explicit dimensions:")
    for b, src_file in dimension_issues[:5]:
        print(f"  ⚠️ In {src_file}: {b[:80]}...")
else:
    print("✔ 100% of image objects have explicit width and height declared!")

