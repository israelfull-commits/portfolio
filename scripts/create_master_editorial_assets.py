import os
from PIL import Image, ImageEnhance, ImageFilter

OUTPUT = 'site/public/images'

def crop_and_export(src, out_name, box=None, target_size=(1600, 900), enhance=True):
    im = Image.open(src).convert('RGB')
    if box:
        im = im.crop(box)
    
    # Resize to target
    im = im.resize(target_size, Image.Resampling.LANCZOS)
    
    if enhance:
        # Subtle unsharp mask to ensure pixel-level crispness of typography and lines
        im = im.filter(ImageFilter.UnsharpMask(radius=1.2, percent=110, threshold=3))
        # Subtle contrast enhancement (1.02)
        enhancer = ImageEnhance.Contrast(im)
        im = enhancer.enhance(1.02)
        
    out_path = os.path.join(OUTPUT, out_name)
    im.save(out_path, format='WEBP', quality=92, method=6)
    size_kb = os.path.getsize(out_path) // 1024
    print(f"Generated: {out_name:35} {im.size} {size_kb} KB")
    return out_path

# 1. Einstein Master Cover (1600x900)
# From hiae-taxonomia-laudo.png (3098x1576)
# Bounding box is (3, 2, 2860, 1567). 2785 x 1567 is 16:9.
crop_and_export(
    'site/public/images/hiae-taxonomia-laudo.png',
    'hiae-capa-editorial-1600.webp',
    box=(0, 0, 2785, 1567),
    target_size=(1600, 900)
)

# 2. Claro Master Cover (1600x900)
# From claro-multicanal.webp (1376x932)
# 1376 x 774 is 16:9
crop_and_export(
    'site/public/images/claro-multicanal.webp',
    'claro-capa-editorial-1600.webp',
    box=(0, 40, 1376, 40 + int(1376 * 9 / 16)),
    target_size=(1600, 900)
)

# 3. Itaú Vencimentos Master Cover (1600x900)
# From 15-vencimentos-versao-canonica-582-12520.png (1360x1069)
# 1360 x 765 is 16:9
crop_and_export(
    'output/figma/ifa-evidencias-2026-11-02/15-vencimentos-versao-canonica-582-12520.png',
    'itau-vencimentos-capa-1600.webp',
    box=(0, 0, 1360, 765),
    target_size=(1600, 900)
)

# 4. Itaú Hub de Liquidez Master Cover (1600x900)
# From 16-hub-liquidez-interface-solucao-3-14068.png (1360x1370)
# 1360 x 765 is 16:9
crop_and_export(
    'output/figma/ifa-evidencias-2026-11-02/16-hub-liquidez-interface-solucao-3-14068.png',
    'itau-hub-liquidez-capa-1600.webp',
    box=(0, 0, 1360, 765),
    target_size=(1600, 900)
)

# 5. Itaú Movimentações Master Cover (1600x900)
# From 13-extrato-ea-discovery-apresentacao.png (2400x1754)
# 2400 x 1350 is 16:9
crop_and_export(
    'output/figma/ifa-evidencias-2026-11-02/13-extrato-ea-discovery-apresentacao.png',
    'itau-movimentacoes-capa-1600.webp',
    box=(0, 0, 2400, 1350),
    target_size=(1600, 900)
)

# 6. Itaú Campanhas Master Cover (1600x900)
# From itau-campanhas-screenflow.webp (1600x1591)
crop_and_export(
    'site/public/images/itau-campanhas-screenflow.webp',
    'itau-campanhas-capa-1600.webp',
    box=(0, 0, 1600, 900),
    target_size=(1600, 900)
)

# 7. Neoenergia Blueprint Focal Crop (1600x900)
# From neoenergia-blueprint-1-contrato-instalo.webp (2000x3656)
# Let's crop a high-detail horizontal slice showing the customer journey & frontstage touchpoints
crop_and_export(
    'site/public/images/neoenergia-blueprint-1-contrato-instalo.webp',
    'neoenergia-blueprint-crop-contrato-1600.webp',
    box=(0, 200, 2000, 200 + int(2000 * 9 / 16)),
    target_size=(1600, 900)
)

# 8. Einstein Design System Focal Crop (1600x900)
# From hiae-documentacao-design-system.png (1820x872)
# 1550 x 872 is ~16:9
crop_and_export(
    'site/public/images/hiae-documentacao-design-system.png',
    'hiae-ds-componentes-crop-1600.webp',
    box=(0, 0, int(872 * 16 / 9), 872),
    target_size=(1600, 900)
)

