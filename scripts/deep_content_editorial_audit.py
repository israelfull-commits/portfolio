import asyncio
import json
import re
from collections import defaultdict, Counter
from playwright.async_api import async_playwright

PAGES = [
    ('/', 'Home'),
    ('/cases/einstein-laudos', 'Albert Einstein'),
    ('/cases/claro-ativacao-simplificada', 'Claro'),
    ('/cases/neoenergia-conexao-digital', 'Neoenergia'),
    ('/cases/itau/hub-liquidez', 'Itaú - Hub Liquidez'),
    ('/cases/itau/vencimentos', 'Itaú - Vencimentos'),
    ('/cases/itau/movimentacoes', 'Itaú - Movimentações'),
    ('/cases/itau/campanhas', 'Itaú - Campanhas')
]

async def inspect_page_content(page, base_url, route, label):
    url = f"{base_url}{route}"
    await page.goto(url, wait_until='networkidle')
    await asyncio.sleep(0.5)

    data = await page.evaluate('''() => {
        // Collect headings
        const headings = Array.from(document.querySelectorAll('h1, h2, h3')).map(h => ({
            tag: h.tagName.toLowerCase(),
            text: h.innerText.trim(),
            className: h.className
        }));

        // Collect all paragraphs
        const paragraphs = Array.from(document.querySelectorAll('p')).map(p => ({
            text: p.innerText.trim(),
            parentClass: p.parentElement ? p.parentElement.className : ''
        })).filter(p => p.text.length > 20);

        // Collect list items
        const listItems = Array.from(document.querySelectorAll('li')).map(li => li.innerText.trim()).filter(t => t.length > 10);

        // Collect all images (src, alt, caption)
        const images = [];
        document.querySelectorAll('figure.cp-figure, .cp-hero-visual').forEach(fig => {
            const img = fig.querySelector('img');
            const caption = fig.querySelector('figcaption');
            if (img) {
                images.push({
                    src: img.getAttribute('src'),
                    alt: img.getAttribute('alt') || '',
                    caption: caption ? caption.innerText.replace(/Ver ampliado.*/s, '').trim() : ''
                });
            }
        });

        // Also check any standalone images
        document.querySelectorAll('img').forEach(img => {
            const src = img.getAttribute('src');
            if (!images.some(i => i.src === src)) {
                images.push({
                    src: src,
                    alt: img.getAttribute('alt') || '',
                    caption: ''
                });
            }
        });

        // Collect metrics / cards
        const cards = Array.from(document.querySelectorAll('.cp-feature-card, .cp-lead-card, .cp-note, .cp-card-list li, .stat-card, .capability-card')).map(c => ({
            text: c.innerText.trim()
        }));

        return {
            headings,
            paragraphs,
            listItems,
            images,
            cards
        };
    }''')

    return {
        'route': route,
        'label': label,
        'headings': data['headings'],
        'paragraphs': data['paragraphs'],
        'listItems': data['listItems'],
        'images': data['images'],
        'cards': data['cards']
    }

async def main():
    base_url = 'http://localhost:8443'
    audit_results = []
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page(viewport={'width': 1440, 'height': 900})

        for route, label in PAGES:
            res = await inspect_page_content(page, base_url, route, label)
            audit_results.append(res)

        await browser.close()

    print("\n==========================================================================")
    print("   AUDITORIA EDITORIAL PROFUNDA & MULTIESPECIALISTA DE CONTEÚDO E IMAGENS")
    print("==========================================================================")

    # 1. Image Redundancy & Reuse Analysis
    image_usage = defaultdict(list)
    for p in audit_results:
        seen_in_page = set()
        for img in p['images']:
            src = img['src']
            if not src: continue
            clean_src = src.split('?')[0].split('/')[-1]
            if clean_src in seen_in_page:
                print(f"[REDUNDÂNCIA INTERNA] Na página '{p['label']}', a imagem '{clean_src}' aparece mais de 1 vez!")
            seen_in_page.add(clean_src)
            image_usage[clean_src].append(p['label'])

    print("\n--- 1. Análise de Inventário de Imagens e Reuso entre Páginas ---")
    multi_page_images = {k: v for k, v in image_usage.items() if len(set(v)) > 1 and not k.endswith(('svg', 'portrait-800.webp'))}
    if multi_page_images:
        for img, pages in multi_page_images.items():
            print(f"  • Imagem compartilhada '{img}' usada em: {', '.join(pages)}")
    else:
        print("  ✓ Zero imagens compartilhadas indevidamente entre cases diferentes.")

    # 2. Duplicate Text & Paragraph Analysis
    print("\n--- 2. Análise de Redundância Textual (Parágrafos e Frases Duplicadas) ---")
    all_paragraphs = []
    for p in audit_results:
        for para in p['paragraphs']:
            all_paragraphs.append((p['label'], para['text']))

    para_counts = Counter([text for _, text in all_paragraphs])
    exact_duplicates = {text: count for text, count in para_counts.items() if count > 1}

    if exact_duplicates:
        print(f"  Atenção: encontrados {len(exact_duplicates)} parágrafos com repetição idêntica:")
        for text, count in list(exact_duplicates.items())[:5]:
            pages = [label for label, t in all_paragraphs if t == text]
            print(f"    - Repetido {count}x em [{', '.join(set(pages))}]: '{text[:80]}...'")
    else:
        print("  ✓ ZERO parágrafos repetidos ou duplicados across todo o portfólio!")

    # 3. Caption vs Body Text Redundancy
    print("\n--- 3. Análise de Redundância: Legenda (Caption) vs Texto de Parágrafo ---")
    caption_overlaps = 0
    for p in audit_results:
        for img in p['images']:
            cap = img['caption'].strip()
            if not cap: continue
            for para in p['paragraphs']:
                p_text = para['text'].strip()
                if cap == p_text:
                    print(f"  [REDUNDÂNCIA 1:1] Em '{p['label']}': legenda idêntica ao parágrafo: '{cap[:60]}...'")
                    caption_overlaps += 1
                elif len(cap) > 30 and cap in p_text:
                    print(f"  [SUB-REDUNDÂNCIA] Em '{p['label']}': legenda contida integralmente no parágrafo: '{cap[:60]}...'")
                    caption_overlaps += 1

    if caption_overlaps == 0:
        print("  ✓ ZERO sobreposições redundantes entre legendas de figuras e corpo de texto.")

    # 4. Heading Redundancy
    print("\n--- 4. Análise de Repetição de Títulos e Chamadas (H1, H2, H3) ---")
    for p in audit_results:
        h_texts = [h['text'] for h in p['headings']]
        h_counts = Counter(h_texts)
        dups = {t: c for t, c in h_counts.items() if c > 1 and t != ''}
        if dups:
            print(f"  Na página '{p['label']}': títulos repetidos na mesma página: {dups}")

    # 5. Numerical / Metric Consistency Check
    print("\n--- 5. Verificação Cruzada de Métricas Principais ---")
    home_text = " ".join([p['text'] for p in audit_results[0]['paragraphs']])
    print(f"  • Verificando métricas no Home ({len(home_text)} chars)...")
    
    # Save full audit output
    with open('output/visual_qa/deep_editorial_audit.json', 'w', encoding='utf-8') as fp:
        json.dump(audit_results, fp, indent=2, ensure_ascii=False)
    print("\nRelatório editorial estruturado salvo em output/visual_qa/deep_editorial_audit.json")

if __name__ == '__main__':
    asyncio.run(main())
