import re
from pathlib import Path

txt_path = Path(r"C:\Users\Israel Rozar\.gemini\antigravity\brain\ec9956e5-078d-4d87-9a8e-74481434c7dc\.system_generated\steps\3047\output.txt")
text = txt_path.read_text(encoding="utf-8")

# Let's inspect the sections in output.txt
sections = [
    "Portfolio / Header / Desktop",
    "MasterCaseStudySection (Orbe Incident Triage)",
    "Metadata Specs Grid (4 Cols)",
    "Master Interface Mockup (Orbe Dark/Forest Dashboard)",
    "Aside - Sticky Sidebar Case Index",
    "Section - 01 RESUMO EXECUTIVO",
    "Section - 02 CONTEXTO E DESAFIO",
    "Section - 03 DESCOBERTA E RECORTE",
    "Big Lime Highlight: How Might We",
    "Section - 04 ESTRATÉGIA E DECISÕES",
    "Section - 05 SOLUÇÃO E VALIDAÇÃO",
    "Section - 06 IMPACTO E REFLEXÃO",
    "Navegação / Outros projetos",
    "Portfolio / Contato / Desktop",
    "Portfolio / Footer / Desktop"
]

for s in sections:
    idx = text.find(f'data-name="{s}"')
    print(f"=== {s} (found: {idx != -1}) ===")
    if idx != -1:
        # print snippet around it
        print(text[idx:idx+600])
        print("-" * 50)

