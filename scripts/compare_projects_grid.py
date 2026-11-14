from pathlib import Path

site_home = Path("site/src/pages/Home.tsx").read_text(encoding="utf-8")
pv_home = Path("portfolio-verde/src/pages/Home.tsx").read_text(encoding="utf-8")

def get_projects_grid(text):
    idx = text.find('className="pf-projects"')
    if idx == -1:
        idx = text.find('pf-project')
    return text[idx:idx+2500]

print("=== SITE / PROJECTS ===")
print(get_projects_grid(site_home)[:1200])
print("\n" + "="*50 + "\n")
print("=== PORTFOLIO-VERDE / PROJECTS ===")
print(get_projects_grid(pv_home)[:1200])

