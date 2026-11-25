import asyncio
from playwright.async_api import async_playwright

routes = [
    "/",
    "/cases/einstein-laudos",
    "/cases/itau/vencimentos",
    "/cases/itau/hub-liquidez",
    "/cases/itau/movimentacoes",
    "/cases/itau/campanhas",
    "/cases/itau/registros-atendimento",
    "/cases/claro-ativacao-simplificada",
    "/cases/neoenergia-conexao-digital"
]

base_url = "http://localhost:8443"

async def test_all():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={"width": 1440, "height": 1000})

        console_errors = []
        page.on("console", lambda msg: console_errors.append(msg.text) if msg.type == "error" else None)

        total_figures_tested = 0
        total_images_verified = 0

        print(f"=== INICIANDO AUDITORIA E2E DE IMAGENS E LIGHTBOX ===")

        for r in routes:
            url = f"{base_url}{r}"
            await page.goto(url, wait_until="networkidle")
            
            # Verify all page images are loaded and non-broken
            imgs = await page.eval_on_selector_all("img", """
                elements => elements.map(img => ({
                    src: img.src,
                    complete: img.complete,
                    naturalWidth: img.naturalWidth,
                    naturalHeight: img.naturalHeight,
                    alt: img.alt
                }))
            """)
            
            broken_on_page = [img for img in imgs if not img["complete"] or img["naturalWidth"] == 0]
            if broken_on_page:
                print(f"[FAIL] {r}: Imagens quebradas encontradas: {broken_on_page}")
            else:
                print(f"[PASS] {r}: {len(imgs)} imagens renderizadas na página (100% OK, naturalWidth > 0)")
            total_images_verified += len(imgs)

            # Test lightboxes on case pages
            figure_buttons = await page.query_selector_all(".cp-figure-btn")
            if figure_buttons:
                print(f"       -> Testando {len(figure_buttons)} modais/lightboxes em {r}...")
                for idx, btn in enumerate(figure_buttons):
                    # Click to open lightbox
                    await btn.click()
                    await page.wait_for_timeout(150)
                    
                    # Verify dialog is open
                    dialog = await page.query_selector("dialog.cp-lightbox[open]")
                    if not dialog:
                        print(f"       [ERRO] Modal {idx+1} não abriu ao clicar!")
                        continue
                    
                    # Check modal image
                    modal_img_data = await page.eval_on_selector("dialog.cp-lightbox[open] .cp-lightbox-viewport img", """
                        img => ({
                            src: img ? img.src : null,
                            complete: img ? img.complete : false,
                            naturalWidth: img ? img.naturalWidth : 0,
                            naturalHeight: img ? img.naturalHeight : 0,
                            visible: img ? (img.offsetWidth > 0 && img.offsetHeight > 0) : false
                        })
                    """)
                    
                    caption_text = await page.eval_on_selector("dialog.cp-lightbox[open] .cp-lightbox-caption", "el => el ? el.textContent : ''")
                    size_text = await page.eval_on_selector("dialog.cp-lightbox[open] .cp-lightbox-footer span", "el => el ? el.textContent : ''")

                    if modal_img_data["complete"] and modal_img_data["naturalWidth"] > 0:
                        total_figures_tested += 1
                    else:
                        print(f"       [ERRO] Imagem ampliada falhou: {modal_img_data}")
                    
                    # Close modal
                    close_btn = await page.query_selector("dialog.cp-lightbox[open] .cp-lightbox-close")
                    if close_btn:
                        await close_btn.click()
                        await page.wait_for_timeout(100)
                    else:
                        await page.keyboard.press("Escape")
                        await page.wait_for_timeout(100)

        await browser.close()

        print(f"\n=======================================================")
        print(f"RESULTADO FINAL:")
        print(f"✓ Total de imagens base verificadas: {total_images_verified}")
        print(f"✓ Total de modais ampliados testados e aprovados: {total_figures_tested}")
        print(f"✓ Erros de console durante o teste: {len(console_errors)}")
        if console_errors:
            print("Erros:", console_errors)
        print(f"=======================================================")

if __name__ == "__main__":
    asyncio.run(test_all())

