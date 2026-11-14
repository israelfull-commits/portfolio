from pathlib import Path

pv_home = Path("portfolio-verde/src/pages/Home.tsx").read_text(encoding="utf-8")
idx = pv_home.find('const projects = [')
idx_end = pv_home.find('const expertise = [')
print(pv_home[idx:idx_end])

