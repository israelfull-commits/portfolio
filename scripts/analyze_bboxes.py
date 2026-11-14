from PIL import Image

def analyze_quadrants(path):
    im = Image.open(path)
    w, h = im.size
    print(f"=== {path} ({w}x{h}) ===")
    # sample bounding box of non-transparent or non-white
    bbox = im.getbbox()
    print("Bounding box:", bbox)

analyze_quadrants("site/public/images/hiae-taxonomia-laudo.png")
analyze_quadrants("site/public/images/hiae-documentacao-design-system.png")
analyze_quadrants("output/figma/ifa-evidencias-2026-11-02/15-vencimentos-versao-canonica-582-12520.png")
analyze_quadrants("output/figma/ifa-evidencias-2026-11-02/16-hub-liquidez-interface-solucao-3-14068.png")
analyze_quadrants("output/figma/ifa-evidencias-2026-11-02/13-extrato-ea-discovery-apresentacao.png")

