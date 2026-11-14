import urllib.request

images_to_check = [
    '/images/hiae-capa-editorial-1600.webp',
    '/images/hiae-ds-componentes-crop-1600.webp',
    '/images/hiae-laudo-original-recorte.webp',
    '/images/hiae-laudo-proposta-demonstrativa-1600.webp',
    '/images/claro-capa-editorial-1600.webp',
    '/images/claro-multicanal.webp',
    '/images/claro-detalhe-linha.webp',
    '/images/neoenergia-capa-conexao-digital.webp',
    '/images/neoenergia-blueprint-crop-contrato-1600.webp',
    '/images/neoenergia-outputs-tobe.webp',
    '/images/itau-vencimentos-capa-1600.webp',
    '/images/itau-vencimentos-canonico.png',
    '/images/itau-hub-liquidez-capa-1600.webp',
    '/images/itau-hub-liquidez-solucao.png',
    '/images/itau-movimentacoes-capa-1600.webp',
    '/images/itau-movimentacoes-discovery.webp',
    '/images/itau-campanhas-capa-1600.webp',
    '/images/itau-campanhas-screenflow.webp',
    '/images/itau-registros-workflow-1600.webp',
]

print("Checking HTTP status of all evidence images on dev server:")
for img_path in images_to_check:
    url = f"http://localhost:8443{img_path}"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as resp:
            content_length = resp.headers.get('Content-Length')
            content_type = resp.headers.get('Content-Type')
            print(f"  200 OK: {img_path:45} ({content_length} bytes, {content_type})")
    except Exception as e:
        print(f"  FAILED: {img_path:45} -> {e}")

