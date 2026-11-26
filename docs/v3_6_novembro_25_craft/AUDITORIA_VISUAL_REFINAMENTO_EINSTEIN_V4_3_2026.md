# Auditoria Visual Profunda & Loop Autônomo de Refinamento — Case Hospital Albert Einstein (V4.3.0)

> **Proveniência & Rastreabilidade**
> - **IA / Plataforma:** Antigravity — Google DeepMind
> - **Data de criação:** 2026-11-26
> - **Última atualização:** 2026-11-26
> - **Conversa de origem:** [66417f41-f841-4d50-a701-e678302e3ec2](conversation://66417f41-f841-4d50-a701-e678302e3ec2)
> - **Rota auditada:** `/cases/einstein-laudos` (`site/src/pages/CasePages.tsx` + `site/src/components/case-presentation.css`)
> - **Skills & Scripts mobilizados:** `portfolio-design-qa`, `portfolio-writing`, `portfolio-banca` (7 papéis), `senior-portfolio-audit`, `scripts/portfolio_qa_sentinel.py` (15 gates) e inspeção visual Chromium multi-viewport (21 capturas por iteração).

---

## 1. Resumo Executivo do Loop Autônomo (3 Iterações)

O case do **Hospital Albert Einstein** foi submetido a um ciclo autônomo de inspeção visual real em Chromium (Desktop `1440×900`, Tablet `768×1024`, Mobile `390×844`, Reflow `320×720` e modal Lightbox), cruzado com auditoria completa de CSS (`case-presentation.css`), JSX (`CasePages.tsx`) e telemetria DOM.

O loop identificou **10 desvios na Iteração 0 (`D01`–`D10`)**, corrigiu todos na **Iteração 1**, validou opticamente na **Iteração 2** — onde a telemetria revelou **1 regressão sutil em Tablet (`D11`)** na faixa de 3 métricas — e encerrou a **Iteração 3** com **`0` desvios visuais, responsivos ou de acessibilidade** e **15/15 PASS** no Sentinel v2.

> [!IMPORTANT]
> Como `D01`, `D02`, `D04`, `D05`, `D06`, `D07`, `D08`, `D09`, `D10` e `D11` foram corrigidos no motor compartilhado (`case-presentation.css`), os ganhos de responsividade mobile, affordance de acordeões, corpo `16px`, medida `42rem` e alvos `>= 44px` beneficiam automaticamente **todos os 4 cases do portfólio** (Einstein, Itaú IFA, Claro e Neoenergia).

---

## 2. Desvios Identificados e Corrigidos (`D01`–`D11`)

| ID | Prioridade | Código Congelado | Diagnóstico (Iteração 0 / 2) | Correção Executada (Iteração 1 / 3) | Status |
| :--- | :---: | :---: | :--- | :--- | :---: |
| **D01** | **P0** | `MB-01` | `.cp-cards-grid` permanecia em 2 colunas em Mobile `390px` (`167px` por card, `117px` de texto útil ≈ `15ch`/linha), esticando cards para até `1.320px` de altura. | Adicionado `@media (max-width: 720px)` colapsando `.cp-cards-grid` para 1 coluna (`358px` totais, `308px` úteis ≈ `37ch`). | **CORRIGIDO** |
| **D02** | **P0** | `A-28` / `AP-07` | `<summary>` dentro de `.cp-appendix` usava `display: flex`, ocultando o marcador nativo do navegador e deixando acordeões fechados parecidos com texto estático sem affordance. | Aplicado `font-weight: 600`, `min-height: 48px`, indicador circular `+` / `−` (`::after`), borda inferior no último item e `max-width: 42rem` nos parágrafos internos. | **CORRIGIDO** |
| **D03** | **P0** | `TH-08` / `AP-06` | Lista *As 3 Macroáreas do Exame* (Cap. 3) combinava `<ul className="cp-card-list">` com prefixos manuais `1.`, `2.`, `3.`, gerando marcadores duplicados (`• 1.`, `• 2.`, `• 3.`). | Convertido para `<ol className="cp-card-list cp-card-list--numbered">` em `CasePages.tsx`, eliminando bullets redundantes. | **CORRIGIDO** |
| **D04** | **P1** | `AP-01` / `MB-02` | Corpo de leitura em `.cp-split-content p`, `.cp-feature-card p`, `.cp-card-list`, `.cp-note p`, `.cp-decisions p` e `.cp-callout-item` renderizava a `15px` (e `.cp-metrics-footnote` a `14px`). | Elevado todo corpo editorial para `1rem` (`16px`) e `.cp-metrics-footnote` para `0.9375rem` (`15px`). | **CORRIGIDO** |
| **D05** | **P1** | `AP-02` | Medida `68ch` em *Plus Jakarta Sans* resultava em linhas largas (`796–860px` / `92–102ch` efetivos) e blocos densos em Decisão 01/02 e na nota do Cap. 6. | Ajustada medida editorial para `42rem` (`672px`), `44rem` no lead e `46rem` no subtítulo; cards de Decisão 01/02 segmentados em 4 `<p>` escaneáveis (`Opções`, `Trade-offs`, `Decisão e custo aceito`, `Evidência`), Decisão 03 e nota do Cap. 6 em 2 `<p>`. | **CORRIGIDO** |
| **D06** | **P1** | `A-20` / `MB-06` | Botão `.cp-back` (*Voltar aos cases*) media `40px` de altura e `.cp-lightbox-close` media `36px` (abaixo do piso tátil `44px`). | Elevados `.cp-back` e `.cp-lightbox-close` para `min-height: 2.75rem` (`44px`), zerando `smallTargets (<44px)` em Desktop e Mobile. | **CORRIGIDO** |
| **D07** | **P1** | `MB-03` | Subtítulo `.cp-subtitle` fixo em `20px` empurrava o badge `8 min de leitura` para fora da 1ª dobra em Mobile `390×844`. | Alterado para `clamp(1rem, 1.6vw, 1.1875rem)` (`16px` no mobile, `19px` no desktop), trazendo título, subtítulo e tempo de leitura para a dobra inicial. | **CORRIGIDO** |
| **D08** | **P2** | `MB-01` / `AP-06` | Em Tablet `768px`, a faixa de 4 métricas do Cap. 6 comprimia cada coluna em `180px`, e `.cp-split-media` mantinha `position: sticky` mesmo empilhado. | Resetado `.cp-split-media { position: static; }` em `<= 860px` e aplicada matriz `2×2` (`359px × 2`) para faixas de 4 métricas em Tablet. | **CORRIGIDO** |
| **D09** | **P2** | `FG-06` / Grid 8px | Padding superior de `.cp-hero` era `36px` (`2.25rem`, fora da grade de 8px), `.cp-chapter-num-box` tinha `11px`, `.cp-note` no mobile mantinha padding horizontal `32px` e havia declarações CSS duplicadas. | Corrigido `.cp-hero` para `2rem` (`32px`), `.cp-chapter-num-box` para `12px` (`22×22px`), `.cp-note` mobile para `1.5rem` (`24px`) e removidas duplicações CSS. | **CORRIGIDO** |
| **D10** | **P2** | `AP-06` | Identificadores técnicos inline (`examTitle`, `dataField`) renderizavam sem estilização diferenciada do texto corrido. | Estilizados `.case-presentation code` e `.cp-note code` como pílulas monoespaçadas semânticas de alto contraste. | **CORRIGIDO** |
| **D11** *(Iter. 2→3)* | **P2** | `AP-06` / Gestalt | Na Iteração 2, a regra `.cp-metrics` em `<= 860px` também converteu a faixa de **3 métricas** do Cap. 1 (`121 / 4 / 14`) em grid 2×2, criando 1 célula órfã vazia em Tablet `768px`. | Restringida a matriz `2×2` a `@media (min-width: 641px) and (max-width: 860px)` com `.cp-metrics:has(> div:nth-child(4))` — mantendo `3×1` (`239px`) para 3 itens e `2×2` (`359px`) para 4 itens. | **CORRIGIDO** |

---

## 3. Telemetria Comparativa — Antes (Iteração 0) × Depois (Iteração 3)

| Métrica Medida em Chromium Real | Antes (Iteração 0) | Depois (Iteração 3) | Critério |
| :--- | :---: | :---: | :---: |
| **Overflow horizontal (`1440 / 768 / 390 / 320px`)** | `0 / 0 / 0 / 0 px` | **`0 / 0 / 0 / 0 px`** | `A-06` / `MB-01` |
| **Alvos táteis `< 44px` (Desktop / Tablet / Mobile)** | `1 / 1 / 1` (`.cp-back` 40px + close 36px) | **`0 / 0 / 0`** | `A-20` / `MB-06` |
| **Largura útil dos cards em Mobile `390px`** | `117px` (`~15ch`, 2 colunas esmagadas) | **`308px` (`~37ch`, 1 coluna limpa)** | `MB-01` |
| **Altura máxima dos cards em Mobile `390px`** | `1.320px` | **`603px` (-54%)** | `MB-01` |
| **Corpo de leitura em cards/notas/splits** | `15px` | **`16px` (`1rem`)** | `AP-01` / `MB-02` |
| **Largura de prosa Desktop (`.cp-chapter-content` / `.cp-note`)** | `796px` / `794px` (`96–102ch`) | **`672px` (`42rem`)** | `AP-02` |
| **Faixas de métricas em Tablet `768px` (3 itens / 4 itens)** | `3×239px` / `4×180px` (apertado) | **`3×239px` / `2×2 de 359px`** | `AP-06` |
| **Proporção das 8 imagens (`aspectDiff` / quebradas)** | `<= 0.0001` / `0` | **`<= 0.0001` / `0`** | `AP-04` / `TH-03` |
| **Equalização de altura em grids 2 colunas (`1440px` / `768px`)** | `maxDiffPx = 0` | **`maxDiffPx = 0`** | `AP-06` |
| **Padding superior `.cp-hero` (grade 8px)** | `36px` | **`32px`** | Grid 8px |
| **Sentinel v2 (`scripts/portfolio_qa_sentinel.py`)** | `15/15 PASS` | **`15/15 PASS`** | Governança |

---

## 4. Parecer da Banca Calibrada (7 Papéis · `portfolio-banca`)

- **Recrutador (`9,8/10`):** 1ª dobra no mobile e desktop comunica cargo, escopo, status real em produção e tempo de leitura (`8 min`) sem ruído.
- **Gerente de Design (`9,8/10`):** 3 decisões estruturadas com opções, trade-offs, custo aceito e evidência agora escaneáveis em blocos curtos; recorte explícito do que ficou fora e do que seria revertido.
- **Par Sênior (`9,7/10`):** anatomia do componente, taxonomia de 3 macroáreas sem marcadores duplicados (`• 1.`), tokens e pílulas `examTitle`/`dataField` com rigor técnico de Design System.
- **Editor (`9,7/10`):** medida tipográfica reduzida para `42rem`, parágrafos quebrados em unidades de leitura confortáveis e zero violações `TX-01..09`.
- **Dados (`9,8/10`):** separação clara entre descoberta (`121` pacientes, `4` médicos), avaliação v3 (`27` participantes, diferenças de `21,6 p.p.` e `25,4 p.p.`) e transparência sobre ausência de telemetria pós-lançamento (`CS-14` / `TX-09`).
- **Acessibilidade (`9,8/10`):** `0` alvos `< 44px` (`A-20`), `0px` reflow a `320px` (`A-06`), acordeões com affordance visual claro (`+`/`−`), contraste WCAG 2.2 AA/AAA e `focus-visible` íntegro (Gates 12–14 PASS).
- **Entrevistador (`9,7/10`):** artefatos reais em 2× Retina no Lightbox (`Fechar` `44px`, zoom 1:1) e apêndices colapsáveis prontos para defesa oral em entrevista técnica.
- **Média Ponderada Final do Case Einstein (`V4.3.0`):** **`9,76 / 10`** (`0` falhas nos 90 códigos congelados).
