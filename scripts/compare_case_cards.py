from pathlib import Path

# Compare Home.tsx in site vs portfolio-verde around the cases grid
site_home = Path("site/src/pages/Home.tsx").read_text(encoding="utf-8")
pv_home = Path("portfolio-verde/src/pages/Home.tsx").read_text(encoding="utf-8")

def extract_cases_section(text):
    idx = text.find('id="trabalho"')
    idx_end = text.find('id="sobre"')
    return text[idx:idx_end]

print("=== SITE / CASES SECTION ===")
print(extract_cases_section(site_home)[:1500])
print("\n" + "="*50 + "\n")
print("=== PORTFOLIO-VERDE / CASES SECTION ===")
print(extract_cases_section(pv_home)[:1500])

