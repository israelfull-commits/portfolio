import time
import json
import re
from playwright.sync_api import sync_playwright

def test_alternatives():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        
        # 1. Read current Home.tsx
        with open('site/src/pages/Home.tsx', 'r', encoding='utf-8') as f:
            original = f.read()
            
        # 2. Build Alternativa A: 2 key metrics
        alt_a_code = original.replace(
            '''                    ["04", "Entrevistas médicas com especialistas"],
                    ["121", "Respostas de pacientes crônicos"],
                    ["14", "Famílias de laudos sistematizadas"],
                    ["44", "Participantes em testes reportados"],''',
            '''                    ["14", "Famílias de laudos sistematizadas"],
                    ["121", "Pacientes em discovery e testes"],'''
        )
        
        with open('site/src/pages/Home.tsx', 'w', encoding='utf-8') as f:
            f.write(alt_a_code)
            
        time.sleep(2) # wait for vite HMR
        
        page = browser.new_page(viewport={'width': 1440, 'height': 900}, device_scale_factor=2)
        page.goto('http://localhost:8443/#trabalho', wait_until='networkidle')
        
        metrics_a = page.evaluate('''() => {
            const card = document.querySelector('.pf-featured');
            const story = document.querySelector('.pf-featured-story');
            const evidence = document.querySelector('.pf-featured-evidence');
            return {
                cardH: card.offsetHeight,
                storyH: story.offsetHeight,
                evidenceH: evidence.offsetHeight,
                deltaH: Math.abs(story.offsetHeight - evidence.offsetHeight)
            };
        }''')
        
        card = page.locator('.pf-featured')
        card.screenshot(path='C:/Users/Israel Rozar/.gemini/antigravity/brain/ec9956e5-078d-4d87-9a8e-74481434c7dc/compare_alt_a_desktop.png')
        page.locator('#trabalho').screenshot(path='C:/Users/Israel Rozar/.gemini/antigravity/brain/ec9956e5-078d-4d87-9a8e-74481434c7dc/compare_alt_a_section.png')
        
        page_m = browser.new_page(viewport={'width': 375, 'height': 812}, device_scale_factor=2)
        page_m.goto('http://localhost:8443/#trabalho', wait_until='networkidle')
        page_m.locator('.pf-featured').screenshot(path='C:/Users/Israel Rozar/.gemini/antigravity/brain/ec9956e5-078d-4d87-9a8e-74481434c7dc/compare_alt_a_mobile.png')
        page_m.close()
        
        # 3. Build Alternativa B: Zero metric boxes
        alt_b_code = re.sub(
            r'<h4>Evidências de discovery e testes</h4>\s*<dl className="pf-evidence-grid">[\s\S]*?</dl>',
            '',
            original
        )
        
        with open('site/src/pages/Home.tsx', 'w', encoding='utf-8') as f:
            f.write(alt_b_code)
            
        time.sleep(2) # wait for vite HMR
        page.reload(wait_until='networkidle')
        
        metrics_b = page.evaluate('''() => {
            const card = document.querySelector('.pf-featured');
            const story = document.querySelector('.pf-featured-story');
            const evidence = document.querySelector('.pf-featured-evidence');
            return {
                cardH: card.offsetHeight,
                storyH: story.offsetHeight,
                evidenceH: evidence.offsetHeight,
                deltaH: Math.abs(story.offsetHeight - evidence.offsetHeight)
            };
        }''')
        
        card = page.locator('.pf-featured')
        card.screenshot(path='C:/Users/Israel Rozar/.gemini/antigravity/brain/ec9956e5-078d-4d87-9a8e-74481434c7dc/compare_alt_b_desktop.png')
        page.locator('#trabalho').screenshot(path='C:/Users/Israel Rozar/.gemini/antigravity/brain/ec9956e5-078d-4d87-9a8e-74481434c7dc/compare_alt_b_section.png')
        
        page_m = browser.new_page(viewport={'width': 375, 'height': 812}, device_scale_factor=2)
        page_m.goto('http://localhost:8443/#trabalho', wait_until='networkidle')
        page_m.locator('.pf-featured').screenshot(path='C:/Users/Israel Rozar/.gemini/antigravity/brain/ec9956e5-078d-4d87-9a8e-74481434c7dc/compare_alt_b_mobile.png')
        page_m.close()
        
        # Restore original
        with open('site/src/pages/Home.tsx', 'w', encoding='utf-8') as f:
            f.write(original)
            
        browser.close()
        
        print('METRICS_A:', json.dumps(metrics_a))
        print('METRICS_B:', json.dumps(metrics_b))

if __name__ == '__main__':
    test_alternatives()

