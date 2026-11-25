#!/usr/bin/env python3
"""
Portfolio QA Sentinel — Automated Quality & Consistency Auditor & Autofix
Verifies Senior Product Designer editorial standards, asset URL safety,
SPA routing coverage, cross-section metric consistency, circular navigation,
and physical asset existence. Includes --autofix and --sync flags.
"""

import os
import re
import sys
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE_SRC = ROOT / "site" / "src"
SITE_PUBLIC = ROOT / "site" / "public"
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
]

STRAY_SEMICOLONS = [
    (r"etapa;\s*(\d)", r"etapa \1"),
    (r"service\s*;\s*blueprint", r"service blueprint"),
    (r"prancha;\s*(\d)", r"prancha \1"),
]

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

def check_spa_routes():
    errors = []
    dist = ROOT / "site" / "dist"
    if not dist.exists():
        return ["Diretório site/dist não encontrado. Execute 'npm run build' primeiro."]
        
    required_paths = [
        dist / "index.html",
        dist / "404.html",
        dist / "cases" / "einstein-laudos" / "index.html",
        dist / "cases" / "itau" / "hub-liquidez" / "index.html",
        dist / "cases" / "claro-ativacao-simplificada" / "index.html",
        dist / "cases" / "neoenergia-conexao-digital" / "index.html",
    ]
    
    for rp in required_paths:
        if not rp.exists():
            errors.append(f"Rota SPA estática ausente em produção: {rp.relative_to(dist)}")
            
    return errors

def sync_portfolio_verde():
    if not PORTFOLIO_VERDE.exists():
        print("   [SYNC] portfolio-verde não encontrado.")
        return
    files_to_sync = [
        (ROOT / "site" / "src" / "pages" / "CasePages.tsx", PORTFOLIO_VERDE / "src" / "pages" / "CasePages.tsx"),
        (ROOT / "site" / "src" / "pages" / "ItauPreparationCase.tsx", PORTFOLIO_VERDE / "src" / "pages" / "ItauPreparationCase.tsx"),
        (ROOT / "site" / "src" / "pages" / "Home.tsx", PORTFOLIO_VERDE / "src" / "pages" / "Home.tsx"),
        (ROOT / "site" / "src" / "components" / "SiteChrome.tsx", PORTFOLIO_VERDE / "src" / "components" / "SiteChrome.tsx"),
        (ROOT / "site" / "src" / "components" / "case-presentation.css", PORTFOLIO_VERDE / "src" / "components" / "case-presentation.css"),
        (ROOT / "site" / "src" / "components" / "CasePresentation.tsx", PORTFOLIO_VERDE / "src" / "components" / "CasePresentation.tsx"),
    ]
    for src, dst in files_to_sync:
        if src.exists():
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dst)
            print(f"   [SYNC] Espelhado 1:1: {src.name} -> {dst.relative_to(ROOT)}")

def main():
    autofix = "--autofix" in sys.argv
    sync_mode = "--sync" in sys.argv or autofix
    
    print("=" * 68)
    print("   PORTFOLIO QA SENTINEL — AUDITORIA AUTOMATIZADA DE QUALIDADE")
    print("=" * 68)
    
    checks = [
        ("Expressões Defensivas / Rascunhos", check_defensive_phrasing),
        ("Sintaxe e Pontuação Tipográfica", lambda: check_stray_semicolons(autofix=autofix)),
        ("Resolução Dinâmica de Ativos (assetUrl)", check_unwrapped_assets),
        ("Existência Física de Assets no Disco", check_image_assets_exist),
        ("Consistência de Métricas Cross-Case", check_metric_consistency),
        ("Navegação Circular Entre Cases", check_circular_navigation),
        ("Estrutura e Rotas Estáticas SPA (GitHub Pages)", check_spa_routes),
    ]
    
    total_errors = 0
    for name, fn in checks:
        errs = fn()
        if errs:
            print(f"\n[FAIL] {name}:")
            for e in errs:
                print(f"   ✖ {e}")
            total_errors += len(errs)
        else:
            print(f"[PASS] {name}")
            
    if sync_mode:
        print("\n" + "-" * 68)
        print("Sincronização Canônica de Repositórios (portfolio-verde):")
        sync_portfolio_verde()
        
    print("\n" + "-" * 68)
    if total_errors == 0:
        print("✓ TODOS OS CRITÉRIOS DE QUALIDADE FORAM ATENDIDOS COM SUCESSO!")
        print("-" * 68)
        sys.exit(0)
    else:
        print(f"✖ FORAM ENCONTRADOS {total_errors} PONTOS DE ATENÇÃO/ERRO.")
        print("-" * 68)
        sys.exit(1)

if __name__ == "__main__":
    main()
