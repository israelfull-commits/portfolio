#!/usr/bin/env python3
"""
Portfolio QA Sentinel — Automated Quality & Consistency Auditor
Verifies Senior Product Designer editorial standards, asset URL safety,
SPA routing coverage, and cross-section metric consistency.
"""

import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE_SRC = ROOT / "site" / "src"

DEFENSIVE_PATTERNS = [
    r"conteúdo\s+fictício",
    r"não\s+comprova\s+implantação",
    r"limites\s+das\s+evidências",
    r"relato\s+original",
    r"amostras\s+não\s+se\s+somam",
    r"posteriormente",
    r"temporário",
    r"rascunho",
]

STRAY_SEMICOLONS = [
    r"etapa;\s*\d",
    r"service\s*;\s*blueprint",
    r"prancha;\s*\d",
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

def check_stray_semicolons():
    errors = []
    for p in SITE_SRC.rglob("*.tsx"):
        text = p.read_text(encoding="utf-8")
        for pat in STRAY_SEMICOLONS:
            matches = re.findall(pat, text, re.IGNORECASE)
            if matches:
                errors.append(f"{p.name}: Encontrado ponto e vírgula indevido '{matches[0]}'")
    return errors

def check_unwrapped_assets():
    errors = []
    img_pattern = re.compile(r'<img[^>]+src=["\'](/(?:images|icons)/[^"\']+)["\']')
    a_pattern = re.compile(r'<a[^>]+href=["\'](/(?:documents|cases)/[^"\']+)["\']')
    
    for p in SITE_SRC.rglob("*.tsx"):
        text = p.read_text(encoding="utf-8")
        # Check raw static img src without assetUrl
        for m in img_pattern.finditer(text):
            errors.append(f"{p.name}: Tag <img> usando caminho absoluto estático sem assetUrl: '{m.group(1)}'")
        # Exclude standard internal anchor links that are handled by React Router Link
        if p.name == "Home.tsx":
            for m in a_pattern.finditer(text):
                if "/documents/" in m.group(1):
                    errors.append(f"{p.name}: Link de documento sem assetUrl: '{m.group(1)}'")
    return errors

def check_metric_consistency():
    errors = []
    home_file = SITE_SRC / "pages" / "Home.tsx"
    case_file = SITE_SRC / "pages" / "CasePages.tsx"
    
    if not home_file.exists() or not case_file.exists():
        return ["Arquivos Home.tsx ou CasePages.tsx não encontrados."]
        
    home_text = home_file.read_text(encoding="utf-8")
    case_text = case_file.read_text(encoding="utf-8")
    
    # Check Neoenergia distributor count
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

def main():
    print("=" * 65)
    print("   PORTFOLIO QA SENTINEL — AUDITORIA AUTOMATIZADA DE QUALIDADE")
    print("=" * 65)
    
    checks = [
        ("Expressões Defensivas / Rascunhos", check_defensive_phrasing),
        ("Sintaxe e Pontuação Tipográfica", check_stray_semicolons),
        ("Resolução Dinâmica de Ativos (assetUrl)", check_unwrapped_assets),
        ("Consistência de Métricas Cross-Case", check_metric_consistency),
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
            
    print("\n" + "-" * 65)
    if total_errors == 0:
        print("✓ TODOS OS CRITÉRIOS DE QUALIDADE FORAM ATENDIDOS COM SUCESSO!")
        print("-" * 65)
        sys.exit(0)
    else:
        print(f"✖ FORAM ENCONTRADOS {total_errors} PONTOS DE ATENÇÃO/ERRO.")
        print("-" * 65)
        sys.exit(1)

if __name__ == "__main__":
    main()

