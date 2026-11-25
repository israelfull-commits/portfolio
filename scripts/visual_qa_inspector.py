import asyncio
import os
import json
from playwright.async_api import async_playwright

output_dir = "output/visual_qa"
os.makedirs(output_dir, exist_ok=True)

routes = [
    ("/cases/einstein-laudos", "Einstein"),
    ("/cases/itau/vencimentos", "Itau Vencimentos"),
    ("/cases/itau/hub-liquidez", "Itau Hub Liquidez"),
    ("/cases/claro-ativacao-simplificada", "Claro"),
    ("/cases/neoenergia-conexao-digital", "Neoenergia")
]

async def run_visual_qa():
    results = []
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={"width": 1440, "height": 900})

        print("=== INICIANDO INSPEÇÃO VISUAL AUTOMATIZADA DOS MODAIS (LIGHTBOX) ===")

        for route, name in routes:
            url = f"http://localhost:8443{route}"
            await page.goto(url, wait_until="networkidle")
            
            figures = await page.query_selector_all(".cp-figure-btn")
            print(f"\n[Verificando {name}] {len(figures)} figuras encontradas...")

            for idx, btn in enumerate(figures[:3]):  # Test up to first 3 figures per case deeply
                await btn.click()
                await page.wait_for_timeout(300)

                # Inspect modal geometry
                modal_info = await page.eval_on_selector("dialog.cp-lightbox[open]", """
                    dialog => {
                        const img = dialog.querySelector('.cp-lightbox-viewport img');
                        const viewport = dialog.querySelector('.cp-lightbox-viewport');
                        const rect = img ? img.getBoundingClientRect() : null;
                        const vRect = viewport ? viewport.getBoundingClientRect() : null;
                        return {
                            isOpen: dialog.open,
                            imgWidth: rect ? Math.round(rect.width) : 0,
                            imgHeight: rect ? Math.round(rect.height) : 0,
                            viewportWidth: vRect ? Math.round(vRect.width) : 0,
                            viewportHeight: vRect ? Math.round(vRect.height) : 0,
                            naturalWidth: img ? img.naturalWidth : 0,
                            naturalHeight: img ? img.naturalHeight : 0,
                            src: img ? img.src.split('/').pop() : ''
                        };
                    }
                """)

                # Take screenshot of open modal
                snap_name = f"{name.lower().replace(' ', '_')}_fig_{idx+1}.png"
                snap_path = os.path.join(output_dir, snap_name)
                await page.screenshot(path=snap_path)

                # Test 'Ver em tamanho original'
                size_btn = await page.query_selector("dialog.cp-lightbox[open] .cp-lightbox-size")
                actual_size_ok = False
                if size_btn:
                    await size_btn.click()
                    await page.wait_for_timeout(200)
                    
                    zoom_info = await page.eval_on_selector("dialog.cp-lightbox[open] .cp-lightbox-viewport", """
                        vp => {
                            const img = vp.querySelector('img');
                            return {
                                scrollWidth: vp.scrollWidth,
                                clientWidth: vp.clientWidth,
                                imgWidth: img ? img.offsetWidth : 0,
                                canScroll: vp.scrollWidth > vp.clientWidth
                            };
                        }
                    """)
                    actual_size_ok = zoom_info["imgWidth"] >= modal_info["naturalWidth"] or zoom_info["imgWidth"] > modal_info["imgWidth"]

                # Close
                close_btn = await page.query_selector("dialog.cp-lightbox[open] .cp-lightbox-close")
                if close_btn:
                    await close_btn.click()
                    await page.wait_for_timeout(150)
                else:
                    await page.keyboard.press("Escape")
                    await page.wait_for_timeout(150)

                status = "PASS" if modal_info["isOpen"] and modal_info["imgWidth"] > 0 else "FAIL"
                record = {
                    "case": name,
                    "figureIndex": idx + 1,
                    "image": modal_info["src"],
                    "renderedSize": f"{modal_info['imgWidth']}x{modal_info['imgHeight']}",
                    "naturalSize": f"{modal_info['naturalWidth']}x{modal_info['naturalHeight']}",
                    "zoomWorked": actual_size_ok,
                    "screenshot": snap_path,
                    "status": status
                }
                results.append(record)
                print(f"  [{status}] Fig {idx+1} ({record['image']}): Renderizado {record['renderedSize']} px (Nativo: {record['naturalSize']} px) | Zoom: {'Sim' if actual_size_ok else 'Não'}")

        await browser.close()

    summary_file = os.path.join(output_dir, "visual_qa_report.json")
    with open(summary_file, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    print(f"\n=======================================================")
    print(f"✓ Inspeção visual concluída. Relatório salvo em {summary_file}")
    print(f"✓ Total de figuras analisadas: {len(results)}")
    print(f"✓ Aprovadas: {sum(1 for r in results if r['status'] == 'PASS')}/{len(results)}")
    print(f"=======================================================")

if __name__ == "__main__":
    asyncio.run(run_visual_qa())

