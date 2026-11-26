---
name: senior-portfolio-audit
description: >-
  Protocolo operacional de auditoria contínua, validação visual, Sentinel v2 (14 gates) e
  sincronização omnicanal do portfólio de Senior Product Designer de Israel Rozar.
---

# Senior Portfolio Audit — Protocolo Operacional Canônico

> **Fonte única de regras:** todas as normas editoriais, visuais, WCAG 2.2, segurança SHA-256, Design System (Home ↔ Cases), higiene de repositório e sincronização omnicanal vivem centralizadas em [AGENTS.md](file:///c:/Users/Israel%20Rozar/Documents/ChatGPT/Portfolio/AGENTS.md) (Seções 1 a 11) — esta skill não duplica essas regras, apenas define o **fluxo de execução obrigatório**.

---

## 1. Script Único de Validação (`portfolio_qa_sentinel.py`)

Execute sempre o sentinela unificado (14 gates: 9 estáticos + 5 runtime em Chromium):

```bash
python scripts/portfolio_qa_sentinel.py
```

Ele substitui integralmente scripts legados de auditoria (`audit_*`, `verify_*`, `test_*`), validando:
- Expressões defensivas, pontuação, `assetUrl`, integridade física de assets, paridade de métricas, navegação circular e rotas estáticas SPA;
- Zero inline styles, zero vazamento de e-mail/senha, unicidade/WebP/HD de imagens;
- Gestalt Outside-In, alinhamento de splits, `0px` overflow em `1440/768/390`, tipografia computada, contraste WCAG 2.2 AA/AAA, `2.4.11 Focus Not Obscured`, `3.3.8 Accessible Auth`, contraste `:hover` e `2.4.13 :focus-visible`.

---

## 2. Inspeção Visual Obrigatória (Antes de Apresentar ou Publicar)

Testes programáticos não substituem inspeção óptica:
1. Capturar no diretório de scratch da sessão (nunca na raiz nem em `scripts/`) os elementos alterados em **Desktop (`1440×900`)** e **Mobile (`390×844`)**.
2. Conferir `aspectDiff = 0.0000` (zero faixas laterais/letterboxing em Heroes `16:9`), ausência de IDs internos em legendas, zero imagens órfãs em grids de 2 colunas e consistência de tokens Home ↔ Cases.

---

## 3. Checklist de Entrega & Sincronização Omnicanal (`AGENTS.md` Seção 9)

1. `npm --prefix site run build` (`0` erros + rotas estáticas SPA).
2. `python scripts/portfolio_qa_sentinel.py` (**14/14 PASS**).
3. Espelhamento 1:1 para `portfolio-verde/`.
4. Atualização de `docs/v3_6_novembro_25_craft/CHANGELOG_V3_6_CRAFT_EDITION.md` e `docs/INDEX_GOVERNANCA_E_DECISOES.md`.
5. `git push origin main` (apenas após aprovação quando o usuário pedir prévia).
6. Sincronização automática no **Notion Portfolio Ops** (`4168db39b34f805884bad8f933e004dd` e subpágina `4248db39b34f81a6b708c51aefce7209`), sem senhas em texto claro.
