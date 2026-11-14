import os
import sys
from playwright.sync_api import sync_playwright

os.makedirs('output/screenshots', exist_ok=True)

pages_to_capture = [
    ('home', 'http://localhost:8443/'),
    ('einstein', 'http://localhost:8443/cases/einstein-laudos'),
    ('claro', 'http://localhost:8443/cases/claro-ativacao-simplificada'),
    ('neoenergia', 'http://localhost:8443/cases/neoenergia-conexao-digital'),
    ('itau-vencimentos', 'http://localhost:8443/cases/itau/vencimentos'),
    ('itau-hub', 'http://localhost:8443/cases/itau/hub-liquidez'),
]

try:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(viewport={'width': 1440, 'height': 900})
        page = context.new_page()
        
        for name, url in pages_to_capture:
            print(f"Navigating to {url}...")
            page.goto(url, wait_until='networkidle')
            page.wait_for_timeout(1000)
            
            # Screenshot hero / top fold
            out_file = f'output/screenshots/{name}-hero-1440.png'
            page.screenshot(path=out_file, full_page=False)
            print(f"Captured {out_file}")
            
        browser.close()
    print("All screenshots captured successfully.")
except Exception as e:
    print("Playwright capture error:", e)

