#!/usr/bin/env python3
"""
scripts/update_changelog.py
Script de automação para registrar e manter o histórico de auditorias, correções,
evoluções e log de mudanças (CHANGELOG.md) do projeto Portfolio.
"""

import os
import sys
import subprocess
from datetime import datetime
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
CHANGELOG_PATH = ROOT_DIR / "CHANGELOG.md"
SITE_CHANGELOG_PATH = ROOT_DIR / "site" / "CHANGELOG.md"
DOCS_AUDIT_LOG_PATH = ROOT_DIR / "docs" / "LOG-AUDITORIAS-E-EVOLUCOES.md"

def run_git(args):
    try:
        res = subprocess.run(["git"] + args, cwd=ROOT_DIR, capture_output=True, text=True, check=True)
        return res.stdout.strip()
    except Exception as e:
        return ""

def ensure_dirs():
    (ROOT_DIR / "docs").mkdir(exist_ok=True)
    (ROOT_DIR / "site").mkdir(exist_ok=True)

def append_or_create_log_entry(entry_text, section_date=None):
    ensure_dirs()
    if not section_date:
        section_date = datetime.now().strftime("%Y-%m-%d")

    # Atualiza CHANGELOG.md
    if not CHANGELOG_PATH.exists():
        content = "# Changelog & Histórico de Auditorias e Evoluções\n\n"
        content += "Todas as alterações notáveis, auditorias de design/código, correções e evoluções deste projeto são registradas neste arquivo.\n\n"
        content += f"## [{section_date}] — Evolução e Auditoria Contínua\n\n"
        content += entry_text.strip() + "\n\n"
        CHANGELOG_PATH.write_text(content, encoding="utf-8")
    else:
        current = CHANGELOG_PATH.read_text(encoding="utf-8")
        header = f"## [{section_date}]"
        if header in current:
            # Insere no bloco existente
            parts = current.split(header, 1)
            # Insere após o cabeçalho
            lines = parts[1].split("\n", 1)
            new_content = parts[0] + header + lines[0] + "\n\n" + entry_text.strip() + "\n" + lines[1]
            CHANGELOG_PATH.write_text(new_content, encoding="utf-8")
        else:
            # Insere logo abaixo da introdução
            first_h2 = current.find("\n## ")
            if first_h2 != -1:
                new_content = current[:first_h2] + f"\n\n## [{section_date}]\n\n" + entry_text.strip() + "\n" + current[first_h2:]
            else:
                new_content = current + f"\n\n## [{section_date}]\n\n" + entry_text.strip() + "\n"
            CHANGELOG_PATH.write_text(new_content, encoding="utf-8")

    # Sincroniza em site/CHANGELOG.md
    SITE_CHANGELOG_PATH.write_text(CHANGELOG_PATH.read_text(encoding="utf-8"), encoding="utf-8")
    print(f"Log atualizado com sucesso em {CHANGELOG_PATH} e {SITE_CHANGELOG_PATH}")

if __name__ == "__main__":
    ensure_dirs()
    status = run_git(["status", "--short"])
    print("Git status:", status)

