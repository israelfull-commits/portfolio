#!/usr/bin/env python3
"""
Portfolio QA Sentinel v2 — Unified Automated Quality Gate (UX, UI, Gestalt, A11y, Security & Dev)
Runs 9 static gates + 3 live Chromium runtime gates (Gestalt/Whitespace Outside-In,
Computed Typography & Hierarchy, WCAG 2.2 AA/AAA Contrast, Responsive 1440/768/390,
Image Uniqueness/HD, and CaseAccessGate Security).

Usage:
  python scripts/portfolio_qa_sentinel.py           # Full suite (9 static + 3 runtime)
  python scripts/portfolio_qa_sentinel.py --fast    # Static gates only (9 checks)
  python scripts/portfolio_qa_sentinel.py --autofix # Auto-fix punctuation & sync portfolio-verde
  python scripts/portfolio_qa_sentinel.py --sync    # Sync canonical files to portfolio-verde
"""

import os
import re
import sys
import time
import shutil
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE_DIR = ROOT / "site"
SITE_SRC = SITE_DIR / "src"
SITE_PUBLIC = SITE_DIR / "public"
SITE_DIST = SITE_DIR / "dist"
PORTFOLIO_VERDE = ROOT / "portfolio-verde"

DEFENSIVE_PATTERNS = [
    r"conteúdo\s+fictício",
    r"fictício|fictícia|fictícios|fictícias",
    r"não\s+comprova\s+implantação",
    r"não\s+é\s+comprovação",
    r"comprovação\s+de\s+uma\s+versão",
    r"limites\s+das\s+evidências",
    r"relato\s+original",
    r"amostras\s+não\s+se\s+somam",
    r"não\s+representa\s+uma\s+interface",
    r"não\s+substitui\s+as\s+evidências",
    r"posteriormente",
    r"temporário",
    r"rascunho",
    # Negative Words / Marketing Clichés (UX Companion 2026)
    r"interface\s+amigável",
    r"experiência\s+fluida",
    r"mergulhar\s+no\s+problema",
    r"colocar\s+o\s+usuário\s+no\s+centro",
    r"design\s+clean",
    r"disruptivo|disruptiva",
    r"sinergia",
    r"revolucionário|revolucionária",
    r"divisor\s+de\s+águas",
    r"double\s+diamond",
    r"mapa\s+de\s+empatia",
    r"reimagin(?:ar|amos|ou|ado)",
    r"encant(?:ar|amento|ador)",
    r"experiência\s+mágica",
    # Internal Figma Node IDs & Third-Person Audit Leaks
    r"\bnó\s+\d+:\d+",
    r"Figma\s+nó\s+\d+",
    r"confirmad[ao]\s+pelo\s+autor",
    r"fornecid[ao]\s+pelo\s+autor",
]

STRAY_SEMICOLONS = [
    (r"etapa;\s*(\d)", r"etapa \1"),
    (r"service\s*;\s*blueprint", r"service blueprint"),
    (r"prancha;\s*(\d)", r"prancha \1"),
]


# ---------------------------------------------------------------------------
# STATIC GATES (1..9)
# ---------------------------------------------------------------------------

def check_defensive_phrasing():
    errors = []
    for p in SITE_SRC.rglob("*.tsx"):
        text = p.read_text(encoding="utf-8")
        for pat in DEFENSIVE_PATTERNS:
            matches = re.findall(pat, text, re.IGNORECASE)
            if matches:
                errors.append(f"{p.name}: Encontrada expressão defensiva proibida '{matches[0]}'")
    return errors


def check_stray_semicolons(autofix=False):
    errors = []
    for p in SITE_SRC.rglob("*.tsx"):
        text = p.read_text(encoding="utf-8")
        new_text = text
        for pat, repl in STRAY_SEMICOLONS:
            matches = re.findall(pat, text, re.IGNORECASE)
            if matches:
                errors.append(f"{p.name}: Encontrado ponto e vírgula indevido '{matches[0]}'")
                if autofix:
                    new_text = re.sub(pat, repl, new_text, flags=re.IGNORECASE)
        if autofix and new_text != text:
            p.write_text(new_text, encoding="utf-8")
            print(f"   [AUTOFIX] Corrigida pontuação em {p.name}")
    return errors


def check_unwrapped_assets():
    errors = []
    asset_pattern = re.compile(r'<(?:img|a|Link)[^>]+(?:src|href)=["\'](/(?:documents|images|icons)/[^"\']+)["\']')
    for p in SITE_SRC.rglob("*.tsx"):
        text = p.read_text(encoding="utf-8")
        for m in asset_pattern.finditer(text):
            errors.append(f"{p.name}: Tag usando caminho estático sem assetUrl: '{m.group(1)}'")
    return errors


def check_image_assets_exist():
    errors = []
    src_pattern = re.compile(r'src:\s*["\'](/images/[^"\']+)["\']')
    for p in SITE_SRC.rglob("*.tsx"):
        text = p.read_text(encoding="utf-8")
        for m in src_pattern.finditer(text):
            rel_path = m.group(1).lstrip("/")
            full_path = SITE_PUBLIC / rel_path
            if not full_path.exists():
                errors.append(f"{p.name}: Asset referenciado não existe no disco: {rel_path}")
    return errors


def check_metric_consistency():
    errors = []
    home_file = SITE_SRC / "pages" / "Home.tsx"
    case_file = SITE_SRC / "pages" / "CasePages.tsx"
    if not home_file.exists() or not case_file.exists():
        return ["Arquivos Home.tsx ou CasePages.tsx não encontrados."]
    home_text = home_file.read_text(encoding="utf-8")
    case_text = case_file.read_text(encoding="utf-8")
    if "5 distribuidoras" in home_text:
        errors.append("Home.tsx: Referência inconsistente a '5 distribuidoras' (o projeto integrou 4 distribuidoras).")
    if "4 distribuidoras" not in case_text:
        errors.append("CasePages.tsx: Esperado '4 distribuidoras' no escopo do case Neoenergia.")
    if "118 ideias" not in case_text and "118 oportunidades" not in case_text:
        errors.append("CasePages.tsx: Métrica de 118 ideias/oportunidades ausente no case Neoenergia.")
    return errors


def check_circular_navigation():
    errors = []
    case_file = SITE_SRC / "pages" / "CasePages.tsx"
    if not case_file.exists():
        return ["CasePages.tsx não encontrado."]
    text = case_file.read_text(encoding="utf-8")
    if 'href: "/cases/itau/hub-liquidez"' not in text:
        errors.append("Navegação circular: Einstein deve apontar para Itaú.")
    if 'href: "/cases/neoenergia-conexao-digital"' not in text:
        errors.append("Navegação circular: Claro deve apontar para Neoenergia.")
    return errors


def check_spa_routes():
    errors = []
    if not SITE_DIST.exists():
        return ["Diretório site/dist não encontrado. Execute 'npm run build' primeiro."]
    required_paths = [
        SITE_DIST / "index.html",
        SITE_DIST / "404.html",
        SITE_DIST / "cases" / "einstein-laudos" / "index.html",
        SITE_DIST / "cases" / "itau" / "hub-liquidez" / "index.html",
        SITE_DIST / "cases" / "claro-ativacao-simplificada" / "index.html",
        SITE_DIST / "cases" / "neoenergia-conexao-digital" / "index.html",
    ]
    for rp in required_paths:
        if not rp.exists():
            errors.append(f"Rota SPA estática ausente em produção: {rp.relative_to(SITE_DIST)}")
    return errors


def check_inline_styles_and_security_leaks():
    errors = []
    # 1. Zero hardcoded inline styles in case pages (allow CSS custom properties --*)
    for fname in ["CasePages.tsx", "ItauPreparationCase.tsx"]:
        p = SITE_SRC / "pages" / fname
        if not p.exists():
            continue
        for lineno, line in enumerate(p.read_text(encoding="utf-8").splitlines(), 1):
            if "style={{" in line and '"--' not in line and "'--" not in line:
                errors.append(f"{fname}:L{lineno}: Estilo inline hardcoded detectado (use classes do Design System).")

    # 2. Zero plaintext email or password leaks in compiled JS bundle
    if SITE_DIST.exists():
        for js in (SITE_DIST / "assets").glob("*.js"):
            txt = js.read_text(encoding="utf-8", errors="ignore")
            if "irozar@yahoo.com.br" in txt:
                errors.append(f"Vazamento de e-mail em texto claro no bundle: {js.name}")
            if "casosdeuso" in txt.lower():
                errors.append(f"Vazamento de senha em texto claro no bundle: {js.name}")

    # 3. Verify CasePresentation enforces CaseAccessGate by default
    cp_file = SITE_SRC / "components" / "CasePresentation.tsx"
    if cp_file.exists():
        cp_txt = cp_file.read_text(encoding="utf-8")
        if "<CaseAccessGate" not in cp_txt:
            errors.append("CasePresentation.tsx: CaseAccessGate obrigatório por padrão não encontrado.")

    return errors


def check_case_image_quality_and_uniqueness():
    errors = []
    try:
        from PIL import Image
    except ImportError:
        return ["Pillow não instalado para auditar resolução de imagens."]

    for fname in ["CasePages.tsx", "ItauPreparationCase.tsx"]:
        p = SITE_SRC / "pages" / fname
        if not p.exists():
            continue
        txt = p.read_text(encoding="utf-8")
        refs = re.findall(r'/images/[^\s\'"`)]+', txt)
        seen = {}
        for ref in refs:
            seen[ref] = seen.get(ref, 0) + 1
            if ref.lower().endswith((".png", ".jpg", ".jpeg")):
                errors.append(f"{fname}: Imagem raster não convertida para WebP: {ref}")
            full = SITE_PUBLIC / ref.lstrip("/")
            if full.exists() and not ref.lower().endswith(".svg"):
                with Image.open(full) as im:
                    if im.width < 1100:
                        errors.append(f"{fname}: Imagem de baixa resolução (<1100px): {ref} ({im.width}x{im.height})")
        for ref, count in seen.items():
            if count > 1:
                errors.append(f"{fname}: Imagem duplicada {count}x no mesmo arquivo: {ref}")
    return errors


# ---------------------------------------------------------------------------
# RUNTIME CHROMIUM GATES (10..12)
# ---------------------------------------------------------------------------

RUNTIME_AUDIT_JS = """() => {
  const res = {
    overflow: document.documentElement.scrollWidth - window.innerWidth,
    h1Count: document.querySelectorAll('h1').length,
    desktopNavCount: document.querySelectorAll('header .desktop-nav a, header .desktop-nav button').length,
    minBodyFontSize: 99,
    missingAlt: [],
    brokenImgs: [],
    duplicateVisibleImgs: [],
    fonts: new Set(),
    captionSizes: new Set(),
    cardH3Sizes: new Set(),
    splitAligns: [],
    gestaltViolations: [],
    smallTargets: [],
    contrastFails: [],
  };

  // Images
  const seenSrcs = new Set();
  for (const img of document.querySelectorAll('main img')) {
    if (img.closest('dialog')) continue;
    const alt = img.getAttribute('alt');
    const src = img.getAttribute('src') || '';
    if (alt === null) res.missingAlt.push(src);
    if (img.complete && img.naturalWidth === 0) res.brokenImgs.push(src);
    if (img.closest('figure')) {
      if (seenSrcs.has(src)) res.duplicateVisibleImgs.push(src);
      seenSrcs.add(src);
    }
  }

  // Fonts & computed typography
  for (const el of document.querySelectorAll('main h1, main h2, main h3, main p')) {
    const cs = getComputedStyle(el);
    res.fonts.add(cs.fontFamily.split(',')[0].replace(/['"]/g, '').trim());
  }
  for (const el of document.querySelectorAll('.cp-chapter-content > p')) {
    const fs = parseFloat(getComputedStyle(el).fontSize);
    if (fs > 0 && fs < res.minBodyFontSize) res.minBodyFontSize = fs;
  }
  for (const el of document.querySelectorAll('.cp-figure-caption-text')) {
    res.captionSizes.add(getComputedStyle(el).fontSize);
  }
  for (const el of document.querySelectorAll('.cp-feature-card h3, .cp-split-content h3, .cp-note h3, .cp-decisions h3')) {
    res.cardH3Sizes.add(getComputedStyle(el).fontSize);
  }

  // Split top-to-top alignment & Gestalt outside-in spacing check
  for (const sp of document.querySelectorAll('.cp-split')) {
    const cs = getComputedStyle(sp);
    res.splitAligns.push(cs.alignItems);
    const padTop = parseFloat(cs.paddingTop) || 0;
    const content = sp.querySelector('.cp-split-content');
    if (content) {
      const innerGap = parseFloat(getComputedStyle(content).rowGap) || 0;
      if (innerGap > padTop) {
        res.gestaltViolations.push(`cp-split innerGap (${innerGap}px) > padding (${padTop}px)`);
      }
    }
  }

  // Interactive target size >= 24x24px (WCAG 2.2 AA 2.5.8)
  for (const el of document.querySelectorAll('main button, main a')) {
    if (el.closest('dialog')) continue;
    const r = el.getBoundingClientRect();
    if (r.width === 0 || r.height === 0) continue;
    // Inline text links inside paragraphs are exempt by WCAG 2.5.8
    if (el.tagName === 'A' && el.closest('p, li')) continue;
    if (r.width < 24 || r.height < 24) {
      res.smallTargets.push(`${el.tagName}:${(el.textContent || '').trim().slice(0, 25)} (${Math.round(r.width)}x${Math.round(r.height)})`);
    }
  }

  // WCAG 2.2 AA Contrast check on key headings/paragraphs/buttons
  function parseRGB(str) {
    const m = str.match(/rgba?\\((\\d+),\\s*(\\d+),\\s*(\\d+)(?:,\\s*([\\d.]+))?\\)/);
    if (!m) return null;
    return [Number(m[1]), Number(m[2]), Number(m[3]), m[4] === undefined ? 1 : Number(m[4])];
  }
  function lum([r, g, b]) {
    const a = [r, g, b].map(v => {
      v /= 255;
      return v <= 0.03928 ? v / 12.92 : Math.pow((v + 0.055) / 1.055, 2.4);
    });
    return 0.2126 * a[0] + 0.7152 * a[1] + 0.0722 * a[2];
  }
  function effectiveBg(el) {
    let cur = el;
    while (cur && cur !== document.documentElement) {
      const bg = parseRGB(getComputedStyle(cur).backgroundColor);
      if (bg && bg[3] > 0.85) return bg;
      cur = cur.parentElement;
    }
    return [250, 248, 245, 1];
  }
  for (const el of document.querySelectorAll('main h1, main h2, main h3, main p, main .pf-button')) {
    if (el.closest('dialog') || el.classList.contains('pf-sr-only')) continue;
    const r = el.getBoundingClientRect();
    if (r.width === 0 || r.height === 0) continue;
    const cs = getComputedStyle(el);
    const fg = parseRGB(cs.color);
    const bg = effectiveBg(el);
    if (!fg || !bg) continue;
    const l1 = lum(fg), l2 = lum(bg);
    const ratio = (Math.max(l1, l2) + 0.05) / (Math.min(l1, l2) + 0.05);
    const fs = parseFloat(cs.fontSize);
    const bold = parseInt(cs.fontWeight, 10) >= 600;
    const isLarge = fs >= 24 || (fs >= 18.66 && bold);
    const minRatio = isLarge ? 3.0 : 4.5;
    if (ratio < minRatio) {
      res.contrastFails.push(`${el.tagName}.${el.className}: ${ratio.toFixed(2)}:1 < ${minRatio}:1 ("${(el.textContent||'').trim().slice(0,30)}")`);
    }
  }

  return {
    ...res,
    fonts: Array.from(res.fonts),
    captionSizes: Array.from(res.captionSizes),
    cardH3Sizes: Array.from(res.cardH3Sizes),
  };
}"""


def run_runtime_suite():
    gestalt_errors = []
    typo_errors = []
    a11y_security_errors = []

    if not SITE_DIST.exists():
        msg = "site/dist não encontrado; pulei runtime checks (execute npm run build)."
        return [msg], [msg], [msg], [msg], [msg]

    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        msg = "Playwright não instalado; runtime checks indisponíveis."
        return [msg], [msg], [msg], [msg], [msg]

    port = 4189
    srv = subprocess.Popen(
        f"npm run preview -- --port {port} --strictPort",
        cwd=str(SITE_DIR),
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        shell=True,
    )
    time.sleep(1.0)
    import socket
    for _ in range(30):
        try:
            with socket.create_connection(("127.0.0.1", port), timeout=0.5):
                break
        except OSError:
            time.sleep(0.5)
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(args=["--disable-gpu"])
            page = browser.new_page(viewport={"width": 1440, "height": 900})
            console_errors = []
            page.on("pageerror", lambda e: console_errors.append(str(e)))

            # 1. Verify Home open & CaseAccessGate security
            page.goto(f"http://localhost:{port}/", wait_until="networkidle")
            if page.locator("#case-access-password").count() != 0:
                a11y_security_errors.append("Home não deve exigir senha.")

            page.goto(f"http://localhost:{port}/cases/einstein-laudos", wait_until="networkidle")
            if not page.locator("#case-access-password").is_visible():
                a11y_security_errors.append("CaseAccessGate não bloqueou /cases/einstein-laudos.")
            else:
                page.fill("#case-access-password", "senha_errada")
                page.click(".cp-gate-submit")
                page.wait_for_selector(".cp-gate-error", timeout=3000)
                if not page.locator(".cp-gate-error[role='alert']").is_visible():
                    a11y_security_errors.append("Erro de senha sem role='alert'.")
                page.fill("#case-access-password", "casosdeuso")
                page.click(".cp-gate-submit")
                page.wait_for_selector(".case-presentation", timeout=5000)

            routes = [
                "/",
                "/cases/einstein-laudos",
                "/cases/itau/hub-liquidez",
                "/cases/itau/registros-atendimento",
                "/cases/claro-ativacao-simplificada",
                "/cases/neoenergia-conexao-digital",
            ]

            # 2. Desktop (1440) full audit across all 5 routes
            for r in routes:
                page.set_viewport_size({"width": 1440, "height": 900})
                page.goto(f"http://localhost:{port}{r}", wait_until="networkidle")
                page.evaluate("async () => { for (let y = 0; y < document.body.scrollHeight; y += 700) { window.scrollTo(0, y); await new Promise(r => setTimeout(r, 40)); } window.scrollTo(0, 0); }")
                time.sleep(0.25)
                rep = page.evaluate(RUNTIME_AUDIT_JS)

                if rep["overflow"] > 0:
                    gestalt_errors.append(f"{r} (1440px): Overflow horizontal de {rep['overflow']}px.")
                for sa in rep["splitAligns"]:
                    if sa not in ("start", "flex-start"):
                        gestalt_errors.append(f"{r}: .cp-split com align-items='{sa}' (esperado 'start').")
                for gv in rep["gestaltViolations"]:
                    gestalt_errors.append(f"{r}: Violação Gestalt Outside-In: {gv}")

                if rep["h1Count"] != 1:
                    typo_errors.append(f"{r}: Esperado exatamente 1 <h1>, encontrado {rep['h1Count']}.")
                if rep["desktopNavCount"] > 6:
                    typo_errors.append(f"{r}: Navegação principal excede 6 itens ({rep['desktopNavCount']}).")
                if rep["minBodyFontSize"] < 15.5:
                    typo_errors.append(f"{r}: Corpo de texto abaixo de 16px ({rep['minBodyFontSize']}px).")
                non_jakarta = [f for f in rep["fonts"] if "Plus Jakarta Sans" not in f]
                if non_jakarta:
                    typo_errors.append(f"{r}: Fonte divergente encontrada: {non_jakarta}")
                if len(rep["captionSizes"]) > 1:
                    typo_errors.append(f"{r}: .cp-figure-caption-text com múltiplos tamanhos: {rep['captionSizes']}")
                if len(rep["cardH3Sizes"]) > 1:
                    typo_errors.append(f"{r}: h3 de cards/splits/notes inconsistente: {rep['cardH3Sizes']}")

                if rep["missingAlt"]:
                    a11y_security_errors.append(f"{r}: Imagens sem alt: {rep['missingAlt']}")
                if rep["brokenImgs"]:
                    a11y_security_errors.append(f"{r}: Imagens quebradas (naturalWidth=0): {rep['brokenImgs']}")
                if rep["duplicateVisibleImgs"]:
                    a11y_security_errors.append(f"{r}: Imagens duplicadas visíveis: {rep['duplicateVisibleImgs']}")
                if rep["smallTargets"]:
                    a11y_security_errors.append(f"{r}: Alvos interativos <24px: {rep['smallTargets'][:5]}")
                if rep["contrastFails"]:
                    a11y_security_errors.append(f"{r}: Falhas de contraste WCAG AA: {rep['contrastFails'][:5]}")

            # 3. Responsive Tablet (768px) & Mobile (390px) overflow check on Home + Einstein + Neoenergia
            for vp_w, vp_h in [(768, 1024), (390, 844)]:
                page.set_viewport_size({"width": vp_w, "height": vp_h})
                for r in ["/", "/cases/einstein-laudos", "/cases/neoenergia-conexao-digital"]:
                    page.goto(f"http://localhost:{port}{r}", wait_until="networkidle")
                    ov = page.evaluate("() => document.documentElement.scrollWidth - window.innerWidth")
                    if ov > 0:
                        gestalt_errors.append(f"{r} ({vp_w}px): Overflow horizontal de {ov}px.")

            # 4. Gate 13: WCAG 2.2 2.4.11 (Focus Not Obscured scroll-padding-top) & 3.3.8 (Accessible Auth)
            wcag22_extra_errors = []
            page.set_viewport_size({"width": 1440, "height": 900})
            page.goto(f"http://localhost:{port}/", wait_until="networkidle")
            scroll_pad = page.evaluate("() => parseFloat(getComputedStyle(document.documentElement).scrollPaddingTop || '0')")
            header_h = page.evaluate("() => { const h = document.querySelector('header'); return h ? h.getBoundingClientRect().height : 0; }")
            if scroll_pad < header_h:
                wcag22_extra_errors.append(f"WCAG 2.2 2.4.11: scroll-padding-top ({scroll_pad}px) < altura do header ({header_h}px).")
            gate_src = (SITE_SRC / "components" / "CaseAccessGate.tsx").read_text(encoding="utf-8")
            if "onPaste" in gate_src or "preventDefault" in gate_src.split("handleSubmit")[0]:
                wcag22_extra_errors.append("WCAG 2.2 3.3.8: CaseAccessGate não deve bloquear paste no campo de senha.")
            if 'autoComplete="current-password"' not in gate_src:
                wcag22_extra_errors.append("WCAG 2.2 3.3.8: CaseAccessGate deve declarar autoComplete='current-password'.")

            # 5. Gate 14: Interactive :hover & :focus-visible contrast on primary CTAs & nav links
            hover_focus_errors = []
            for sel in [".pf-button-primary", ".pf-nav a", ".pf-home-card-cta"]:
                loc = page.locator(sel).first
                if loc.count() > 0 and loc.is_visible():
                    loc.hover()
                    time.sleep(0.08)
                    hover_ratio = page.evaluate("""(el) => {
                        const parse = (c) => {
                            const m = (c||'').match(/rgba?\\((\\d+),\\s*(\\d+),\\s*(\\d+)(?:,\\s*([\\d.]+))?\\)/);
                            return m ? [+m[1], +m[2], +m[3], m[4]===undefined?1:+m[4]] : null;
                        };
                        const lum = ([r,g,b]) => [r,g,b].map(v => { v/=255; return v<=0.03928?v/12.92:Math.pow((v+0.055)/1.055,2.4); })
                            .reduce((a,v,i) => a + v * [0.2126,0.7152,0.0722][i], 0);
                        const fg = parse(getComputedStyle(el).color);
                        let bg = null, cur = el;
                        while (cur && cur !== document.documentElement) {
                            const p = parse(getComputedStyle(cur).backgroundColor);
                            if (p && p[3] > 0.1) { bg = p; break; }
                            cur = cur.parentElement;
                        }
                        if (!bg) bg = [244, 242, 233, 1];
                        if (!fg) return 21;
                        const l1 = Math.max(lum(fg), lum(bg)), l2 = Math.min(lum(fg), lum(bg));
                        return (l1 + 0.05) / (l2 + 0.05);
                    }""", loc.element_handle())
                    if hover_ratio < 4.5:
                        hover_focus_errors.append(f"Contraste :hover insuficiente em {sel}: {hover_ratio:.2f}:1 < 4.5:1.")
                    loc.focus()
                    outline_w = page.evaluate("(el) => parseFloat(getComputedStyle(el).outlineWidth || '0')", loc.element_handle())
                    if outline_w < 2.0:
                        hover_focus_errors.append(f"WCAG 2.2 2.4.13: outline-width em foco de {sel} é {outline_w}px (< 2px).")

            if console_errors:
                a11y_security_errors.append(f"Erros de runtime JS: {console_errors[:3]}")

            browser.close()
    finally:
        srv.terminate()

    return gestalt_errors, typo_errors, a11y_security_errors, wcag22_extra_errors, hover_focus_errors


def sync_portfolio_verde():
    if not PORTFOLIO_VERDE.exists():
        print("   [SYNC] portfolio-verde não encontrado.")
        return
    files_to_sync = [
        (SITE_SRC / "pages" / "CasePages.tsx", PORTFOLIO_VERDE / "src" / "pages" / "CasePages.tsx"),
        (SITE_SRC / "pages" / "ItauPreparationCase.tsx", PORTFOLIO_VERDE / "src" / "pages" / "ItauPreparationCase.tsx"),
        (SITE_SRC / "pages" / "Home.tsx", PORTFOLIO_VERDE / "src" / "pages" / "Home.tsx"),
        (SITE_SRC / "components" / "SiteChrome.tsx", PORTFOLIO_VERDE / "src" / "components" / "SiteChrome.tsx"),
        (SITE_SRC / "components" / "CaseAccessGate.tsx", PORTFOLIO_VERDE / "src" / "components" / "CaseAccessGate.tsx"),
        (SITE_SRC / "components" / "case-presentation.css", PORTFOLIO_VERDE / "src" / "components" / "case-presentation.css"),
        (SITE_SRC / "components" / "CasePresentation.tsx", PORTFOLIO_VERDE / "src" / "components" / "CasePresentation.tsx"),
    ]
    for src, dst in files_to_sync:
        if src.exists():
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dst)
            print(f"   [SYNC] Espelhado 1:1: {src.name} -> {dst.relative_to(ROOT)}")


def main():
    autofix = "--autofix" in sys.argv
    sync_mode = "--sync" in sys.argv or autofix
    fast_mode = "--fast" in sys.argv

    print("=" * 72)
    print("   PORTFOLIO QA SENTINEL v2 — AUDITORIA UNIFICADA (UX/UI/GESTALT/A11Y)")
    print("=" * 72)

    static_checks = [
        ("1. Expressões Defensivas / Rascunhos", check_defensive_phrasing),
        ("2. Sintaxe e Pontuação Tipográfica", lambda: check_stray_semicolons(autofix=autofix)),
        ("3. Resolução Dinâmica de Ativos (assetUrl)", check_unwrapped_assets),
        ("4. Existência Física de Assets no Disco", check_image_assets_exist),
        ("5. Consistência de Métricas Cross-Case", check_metric_consistency),
        ("6. Navegação Circular Entre Cases", check_circular_navigation),
        ("7. Estrutura e Rotas Estáticas SPA (GitHub Pages)", check_spa_routes),
        ("8. Zero Estilos Inline & Segurança (Email/Senha/Gate)", check_inline_styles_and_security_leaks),
        ("9. Unicidade, Formato WebP & Resolução HD de Imagens", check_case_image_quality_and_uniqueness),
    ]

    total_errors = 0
    for name, fn in static_checks:
        errs = fn()
        if errs:
            print(f"\n[FAIL] {name}:")
            for e in errs:
                print(f"   ✖ {e}")
            total_errors += len(errs)
        else:
            print(f"[PASS] {name}")

    if not fast_mode:
        gestalt_errs, typo_errs, a11y_errs, wcag22_errs, hover_focus_errs = run_runtime_suite()
        runtime_checks = [
            ("10. Gestalt Outside-In, Splits & Responsividade (1440/768/390)", gestalt_errs),
            ("11. Tipografia & Hierarquia Computada (Chromium)", typo_errs),
            ("12. Acessibilidade WCAG 2.2, Imagens & CaseAccessGate (Chromium)", a11y_errs),
            ("13. WCAG 2.2 2.4.11 Focus Not Obscured & 3.3.8 Accessible Auth", wcag22_errs),
            ("14. Contraste em :hover & WCAG 2.2 2.4.13 :focus-visible (Chromium)", hover_focus_errs),
        ]
        for name, errs in runtime_checks:
            if errs:
                print(f"\n[FAIL] {name}:")
                for e in errs:
                    print(f"   ✖ {e}")
                total_errors += len(errs)
            else:
                print(f"[PASS] {name}")

    if sync_mode:
        print("\n" + "-" * 72)
        print("Sincronização Canônica de Repositórios (portfolio-verde):")
        sync_portfolio_verde()

    print("\n" + "-" * 72)
    if total_errors == 0:
        print("✓ TODOS OS CRITÉRIOS DE QUALIDADE FORAM ATENDIDOS COM SUCESSO!")
        print("-" * 72)
        sys.exit(0)
    else:
        print(f"✖ FORAM ENCONTRADOS {total_errors} PONTOS DE ATENÇÃO/ERRO.")
        print("-" * 72)
        sys.exit(1)


if __name__ == "__main__":
    main()
