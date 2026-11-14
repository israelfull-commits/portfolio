from PIL import Image

def inspect(name, path):
    im = Image.open(path)
    print(f"=== {name} ({im.size}) ===")
    print(f"Format: {im.format}, Mode: {im.mode}")

inspect("Einstein Taxonomia", "site/public/images/hiae-taxonomia-laudo.png")
inspect("Einstein DS Doc", "site/public/images/hiae-documentacao-design-system.png")
inspect("Claro Hero", "site/public/images/claro-ativacao-hero.webp")
inspect("Claro Multicanal", "site/public/images/claro-multicanal.webp")
inspect("Itau Vencimentos 582-12520", "output/figma/ifa-evidencias-2026-11-02/15-vencimentos-versao-canonica-582-12520.png")
inspect("Itau Hub 3-14068", "output/figma/ifa-evidencias-2026-11-02/16-hub-liquidez-interface-solucao-3-14068.png")
inspect("Itau Extrato EA 13", "output/figma/ifa-evidencias-2026-11-02/13-extrato-ea-discovery-apresentacao.png")
inspect("Itau Campanhas Acervo", "output/campanhas-configuracao-acervo.png")

