# Auditoria Profunda de Governança, Automações, Skills & Higiene do Repositório (2026)

**Data:** 26 de Novembro de 2026  
**Escopo:** Raiz do repositório, `AGENTS.md`, `SENIOR_UX_PORTFOLIO_CANON.md`, `.agents/`, `.github/`, `scripts/` e `docs/`.

---

## 1. Raio-X Atual do Repositório (Achados Objetivos)

| Área | Volume Encontrado | Diagnóstico | Ação Recomendada |
| :--- | :---: | :--- | :--- |
| **Raiz — `.md`** | 19 arquivos | **15 são duplicatas exatas (SHA-256)** de arquivos já arquivados em `docs/v1_*`, `docs/v2_*` e `docs/v3_*`. Apenas 4 são únicos (`AGENTS.md`, `SENIOR_UX_PORTFOLIO_CANON.md`, `AUDITORIA-UX-UI.md`, `CHECKLIST-OPERACIONAL.md`). | Manter só `AGENTS.md` na raiz; arquivar os 2 únicos antigos em `docs/` e remover os 15 duplicados (após consentimento). |
| **Raiz — `.png` e `.gz`** | 126 `.png` (`23,4 MB`) + 8 `.gz` (`87,2 MB`) | **110,6 MB** de prints antigos e backups soltos (0 rastreados no Git). | Arquivar fora do repo (`D:\arquivo-morto-portfolio\`) ou remover após consentimento. |
| **`scripts/`** | **598 arquivos** (`317 .py` + `258 .png` = `41,2 MB`) | Apenas **2 scripts são canônicos e ativos** (`portfolio_qa_sentinel.py` e `build_portfolio_figma_screens.py`). Os outros ~315 `.py` e 258 `.png` são scripts descartáveis e prints de sessões anteriores. | Mover legados para `D:\arquivo-morto-portfolio\scripts-legados\` (ou remover do Git após consentimento), mantendo `scripts/` limpo com os 2 motores canônicos. |
| **Pastas temporárias/legado** | `.audit/` (19), `.playwright-cli/` (12), `.playwright-mcp/` (26), `qa/` (234), `output/` (845), `tmp/` (143), `figma-make-reference/` (1.282) | Pastas de apoio de sessões antigas acumuladas na raiz. | Adicionar ao `.gitignore` e arquivar em `D:\arquivo-morto-portfolio\` quando autorizado. |
| **Regras & Skills** | `AGENTS.md` + `SKILL.md` + `docs/v3_6_*` | Sobreposição editorial entre `AGENTS.md` e `SKILL.md`; faltavam regras explícitas de **Paridade Design System (Home ↔ Cases)** e **Higiene de Repositório**. | **CORRIGIDO AGORA:** `AGENTS.md` evoluído com Seções 10 e 11; `SKILL.md` enxugada para apontar para `AGENTS.md` sem duplicar regras. |
| **CI/CD (`.github/`)** | 1 workflow (`deploy.yml`) | Limpo, 2 estágios (`build` ➔ `deploy`), zero duplicidade. | **Manter intacto.** |

---

## 2. Arquitetura Canônica Consolidada (Alvo Limpo)

1. **Fonte Única de Regras:** `AGENTS.md` (Seções 1–11).
2. **Skill Operacional Única:** `.agents/skills/senior-portfolio-audit/SKILL.md` (execução + inspeção visual + checklist omnicanal).
3. **2 Scripts Canônicos em `scripts/`:**
   - `scripts/portfolio_qa_sentinel.py` (Sentinela v2 — 14 gates + sync `portfolio-verde/`)
   - `scripts/build_portfolio_figma_screens.py` (Compilador oficial Figma Desktop)
4. **Documentação Ativa em `docs/v3_6_novembro_25_craft/`:**
   - `CHANGELOG_V3_6_CRAFT_EDITION.md`
   - `UX_PORTFOLIO_REVIEW_CHECKLIST_2026.md`
   - `UX_AUDIT_FRAMEWORK_2026.md`
   - `SENIOR_PORTFOLIO_SIGNALS_2026.md`
   - `UX_CASE_STUDY_STRUCTURE_2026.md`
   - `UX_INTERVIEW_AND_CHALLENGE_PLAYBOOK_2026.md`
   - `SCORECARD_VERSOES_E_VARIACOES_2026.md`
   - `AUDITORIA_GOVERNANCA_E_HIGIENE_REPO_2026.md` (este documento)
5. **Governança Externa Sincronizada:** Notion Portfolio Ops (`4168db39b34f805884bad8f933e004dd`).

