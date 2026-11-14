import urllib.request
import re

routes = [
    '/',
    '/cases/einstein-laudos',
    '/cases/neoenergia-conexao-digital',
    '/cases/claro-ativacao-simplificada',
    '/cases/itau/vencimentos',
    '/cases/itau/hub-liquidez',
    '/cases/itau/movimentacoes',
    '/cases/itau/campanhas',
    '/cases/itau/registros-atendimento'
]

for r in routes:
    url = f"http://localhost:8443{r}"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as resp:
            status = resp.status
            html = resp.read().decode('utf-8')
            print(f"OK ({status}): {r} -> {len(html)} bytes")
    except Exception as e:
        print(f"ERROR: {r} -> {e}")

