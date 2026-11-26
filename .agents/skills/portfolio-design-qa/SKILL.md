---
name: portfolio-design-qa
description: >-
  Auditoria técnica, visual, responsiva, WCAG 2.2 AA e Figma do portfólio de
  Israel Rozar. Aplica os códigos congelados AP-01..07, MB-01..06, TH-01..08,
  A-01..28, FG-01..06 e executa o Sentinel v2 (15 gates).
---

# Skill · `portfolio-design-qa` (Figma, Estrutura, Acessibilidade & Sentinel)

> **Fonte única de verdade:** [GUIA_CONSOLIDADO_REGRAS_E_CODIGOS_2026.md](file:///c:/Users/Israel%20Rozar/Documents/ChatGPT/Portfolio/docs/GUIA_CONSOLIDADO_REGRAS_E_CODIGOS_2026.md) e [AGENTS.md](file:///c:/Users/Israel%20Rozar/Documents/ChatGPT/Portfolio/AGENTS.md).

## Regra de Ouro de Auditoria
- Todo apontamento de falha **deve citar um código oficial** (`AP-`, `MB-`, `TH-`, `A-`, `FG-`, `HP-`).
- Sugestões sem código vão para seção separada e **não reprovam** a entrega.
- **Critério de Prontidão Sênior:** `0` falhas em `HP`, `CS`, `TX`, `IA` e `A`; até `2` falhas em `AP`/`MB`/`TH` com prazo (exceção formal registrada em ADR para `TH-01` domínio próprio em favor de `github.io`).

## Códigos Cobertos por Esta Skill
- **Apresentação (`AP-01..07`):** corpo `16–18px` / `line-height 1.5–1.75` (`AP-01`), prosa `65–75ch` (`AP-02`), 1 família tipográfica disciplinada (`AP-03`), WebP/AVIF no tamanho de exibição (`AP-04`), `LCP < 2.5s` (`AP-05`), sem parallax/animação pesada (`AP-06`), contraste AA (`AP-07`).
- **Mobile (`MB-01..06`):** coluna única `< 720px` (`MB-01`), corpo `>= 16px` (`MB-02`), hero sem estouro (`MB-03`), menu hambúrguer/compacto (`MB-04`), legível fim a fim (`MB-05`), alvos `>= 24×24px` WCAG 2.5.8 com padrão do projeto `44–48px` (`MB-06`).
- **Higiene Técnica (`TH-01..08`):** domínio próprio (`TH-01`, ADR `github.io`), SSL válido (`TH-02`), zero 404 (`TH-03`), títulos específicos (`TH-04`), Open Graph & `canonical` apontando para produção (`TH-05`), CV em PDF com nome legível (`TH-06`), zero ferramentas de edição expostas (`TH-07`), revisão ortográfica (`TH-08`).
- **Acessibilidade W3C WCAG 2.2 AA (`A-01..28`):** `1.1.1` alt probatório (`A-01`), `1.3.1` H1 único (`A-02`), `1.4.1` cor não única (`A-03`), `1.4.3` contraste 4.5:1/3:1 (`A-04`), `1.4.4` zoom 200% (`A-05`), `1.4.10` reflow 320px (`A-06`), `1.4.11` contraste não textual 3:1 sem arredondar (`A-07`), `1.4.12` espaçamento (`A-08`), `1.4.13` hover/foco (`A-09`), `2.1.1` teclado (`A-10`), `2.4.1` pular blocos (`A-12`), `2.4.2` título (`A-13`), `2.4.4` finalidade do link sem `"saiba mais"`/`"ver projeto"` genérico (`A-15`), `2.4.6` headings com tema (`A-16`), `2.4.7`/`2.4.11`/`2.4.13` foco visível e não obscurecido (`A-17`, `A-18`), `2.5.8` alvo `44–48px` (`A-20`), `3.1.1` `lang="pt-BR"` (`A-21`), `3.2.3`/`3.2.4`/`3.2.6` navegação/identificação/ajuda consistentes (`A-22..24`), `3.3.8` autenticação acessível com colar/gerenciador de senhas (`A-27`), `4.1.2` nome/função/valor (`A-28`).
- **Figma (`FG-01..06`):** auto layout em todos os nós filhos com `fills = []` em wrappers (`FG-01`), sem hug/fill incorreto/corte/overlay (`FG-02`), sem quebra de texto "uma palavra por linha" (`FG-03`), tokens/estilos vinculados (`FG-04`), responsivo `1280/768/390` (`FG-05`), menor texto `12px` Caption (`FG-06`), + Banner de Proveniência Antigravity obrigatório e validação visual via `get_screenshot`.

## Fluxo Obrigatório de Execução
1. `npm --prefix site run build` (`0` erros + rotas estáticas SPA).
2. `python scripts/portfolio_qa_sentinel.py --sync` (**15/15 PASS** + espelho `portfolio-verde/`).
3. Inspeção visual óptica em `scratch/` (Desktop `1440`, Tablet `768`, Mobile `390`) e `get_screenshot` no Figma antes de concluir.
4. Sincronização omnicanal (`site/`, `portfolio-verde/`, `docs/`, Figma e Notion Portfolio Ops).
