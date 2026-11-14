import os
from PIL import Image

sources = [
    ('Einstein DS Doc', 'site/public/images/hiae-documentacao-design-system.png'),
    ('Einstein Taxonomia', 'site/public/images/hiae-taxonomia-laudo.png'),
    ('Einstein Proposta', 'site/public/images/hiae-laudo-proposta-demonstrativa-1600.webp'),
    ('Einstein Template Fonte', 'site/public/images/hiae-template-fonte.png'),
    ('Einstein Original Recorte', 'site/public/images/hiae-laudo-original-recorte.webp'),
    ('Claro Hero', 'site/public/images/claro-ativacao-hero.webp'),
    ('Claro Multicanal', 'site/public/images/claro-multicanal.webp'),
    ('Claro Desktop', 'site/public/images/claro-ativacao-desktop.webp'),
    ('Claro Detalhe Linha', 'site/public/images/claro-detalhe-linha.webp'),
    ('Claro Confirmacao Mobile', 'site/public/images/claro-confirmacao-mobile.webp'),
    ('Claro Workshop', 'site/public/images/claro-workshop.webp'),
    ('Claro Jornadas', 'site/public/images/claro-jornadas.webp'),
    ('Neo Conexao Capa', 'site/public/images/neoenergia-capa-conexao-digital.webp'),
    ('Neo Blueprint 1', 'site/public/images/neoenergia-blueprint-1-contrato-instalo.webp'),
    ('Neo Matriz 118', 'site/public/images/neoenergia-matriz-118-ideias.webp'),
    ('Neo Outputs To-Be', 'site/public/images/neoenergia-outputs-tobe.webp'),
    ('Itau Hub Solucao', 'site/public/images/itau-hub-liquidez-solucao.png'),
    ('Itau Vencimentos Canonico', 'site/public/images/itau-vencimentos-canonico.png'),
    ('Itau Vencimentos 582-12520', 'output/figma/ifa-evidencias-2026-11-02/15-vencimentos-versao-canonica-582-12520.png'),
    ('Itau Hub 3-14068', 'output/figma/ifa-evidencias-2026-11-02/16-hub-liquidez-interface-solucao-3-14068.png'),
    ('Itau Extrato EA 13', 'output/figma/ifa-evidencias-2026-11-02/13-extrato-ea-discovery-apresentacao.png'),
    ('Itau Extrato EA 14', 'output/figma/ifa-evidencias-2026-11-02/14-extrato-ea-discovery-demonstrativo.png'),
    ('Itau Campanhas Acervo', 'output/campanhas-configuracao-acervo.png'),
    ('Itau Campanhas Screenflow', 'site/public/images/itau-campanhas-screenflow.webp'),
]

for label, p in sources:
    if os.path.exists(p):
        with Image.open(p) as img:
            print(f"{label:30} {p:65} {img.size} {img.format}")
    else:
        print(f"{label:30} MISSING: {p}")

