from pathlib import Path
import difflib

css_site = Path("site/src/portfolio.css").read_text(encoding="utf-8")
css_pv = Path("portfolio-verde/src/portfolio.css").read_text(encoding="utf-8")

print(f"site/src/portfolio.css length: {len(css_site)}")
print(f"portfolio-verde/src/portfolio.css length: {len(css_pv)}")

# Split into selectors
import re
def get_rules(css):
    rules = {}
    for match in re.finditer(r'([^{]+)\{([^}]+)\}', css):
        sel = match.group(1).strip()
        body = match.group(2).strip()
        rules[sel] = body
    return rules

rules_site = get_rules(css_site)
rules_pv = get_rules(css_pv)

all_selectors = sorted(set(rules_site.keys()) | set(rules_pv.keys()))
print(f"\nTotal unique selector blocks: {len(all_selectors)}")

divergences = []
for sel in all_selectors:
    if sel in rules_site and sel in rules_pv:
        if rules_site[sel] != rules_pv[sel]:
            divergences.append((sel, rules_site[sel], rules_pv[sel]))
    elif sel in rules_site:
        divergences.append((sel, rules_site[sel], "[MISSING IN PV]"))
    else:
        divergences.append((sel, "[MISSING IN SITE]", rules_pv[sel]))

print(f"Divergent rules count: {len(divergences)}")
for sel, s, pv in divergences[:30]:
    print(f"\n>>> SELECTOR: {sel}")
    print(f"  SITE: {s}")
    print(f"  PV:   {pv}")

