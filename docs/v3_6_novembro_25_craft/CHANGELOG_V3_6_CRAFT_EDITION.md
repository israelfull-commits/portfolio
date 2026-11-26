# Changelog Detalhado — Versão V3.6 (Craft Edition & Documentação Figma)

**Data:** 25 de Novembro de 2026  
**Conversa de Origem:** `b9eff66e-96f2-48ed-af7d-28e8cea0dfad`  
**Base Anterior:** Versão V3.5 (`e8fecf8`)

---

## 1. Melhorias de Craft Visual & Experiência de Interface

Implementados os 4 refinamentos funcionais de alto impacto (evitando intencionalmente *Scroll Reveal* que oculta conteúdo na triagem rápida de recrutadores):

1. **Barra de Progresso de Leitura nos Cases (`Site / CasePresentation.tsx` & `case-presentation.css`):**
   * Linha fixa de `3px` no topo da viewport (`.cp-reading-progress`) em gradiente `var(--cp-pine)` ➔ `#1b6b45` ➔ `var(--cp-lime)`.
   * Atualizada de forma passiva via `requestAnimationFrame`, sem impacto em performance ou layout shift.
2. **Microinterações Táteis nos Cards e CTAs (`portfolio.css`):**
   * Elevação física suave nos cards da Home (`translateY(-4px)` + sombra multi-camada difusa em tom pine).
   * Zoom sutil (`scale(1.015)`) no preview do tablet do Einstein ao passar o mouse no card destaque.
   * Micro-deslocamento da seta (`translateX(3px)`) nos botões e CTAs.
   * Realce suave nos links de submódulos do Itaú.
3. **Header Inteligente com Profundidade no Scroll (`SiteChrome.tsx` & `index.css`):**
   * Classe dinâmica `.is-scrolled` ativada acima de `12px` de scroll, aplicando `backdrop-filter: blur(12px)` e sombra difusa sutil.
4. **Lightbox com Zoom Direto na Imagem (`CasePresentation.tsx` & `case-presentation.css`):**
   * Clique direto na imagem ampliada alterna entre *Ajustar à tela* e *Tamanho original 1:1* com cursor contextual (`zoom-in` / `zoom-out`) e animação suave de entrada (`180ms cubic-bezier`).
5. **Proteção Vestibular Integral:**
   * 100% das novas transições e animações respeitam `@media (prefers-reduced-motion: reduce)`.

---

## 2. Sincronização de Design & Documentação no Figma Desktop

* **Gerador Atualizado ([build_portfolio_figma_screens.py](../../scripts/build_portfolio_figma_screens.py)):**
  * Adicionada a prancha canônica **`buildDesignSystemDocsFrame`** (`create_ds_docs`) contendo: Paleta Semântica & Matriz WCAG 2.2 AAA, Tipografia & Grid 8px, Especificação de Microinterações V3.6 e Histórico Completo de Versões (V1 ➔ V3.6).
  * Integrada tanto no botão dedicado da UI do plugin quanto na geração completa (`create_all_screens`).
  * Bundle `code.js` e `ui.html` recompilados e sincronizados em `figma-refine-plugin` e `gemini-figma-plugin` (sintaxe ES5/ES6 clássica compatível com Figma Desktop no Windows).


---

## 3. Atualização Incremental (V3.6.1)
* **Home (`Home.tsx` & `portfolio.css`):** Links da barra *"Outros recortes no Itaú (IFA)"* (`Gestão de Vencimentos`, `Movimentações`, `Gestão de Campanhas`) desativados e convertidos em tags informativas estáticas (`.pf-home-submodules-item`, `<div>` semântico), preservando os `href` no array `itauSubmodules` para reativação rápida quando desejado.
* **Hero (`Home.tsx`):** Removido o link de e-mail em texto aberto abaixo dos botões do Hero para proteger contra scrapers/bots de spam e manter a dobra inicial limpa com `Ver projetos` + `Currículo (PDF)`.
* **Contato Anti-Spam (`SiteChrome.tsx`):** Padronizado o CTA do rodapé da Home e dos Cases para `Enviar um e-mail` com montagem dinâmica do `mailto:` apenas no evento de clique (`openProtectedEmail`), eliminando 100% de endereços de e-mail em texto aberto no HTML/bundle contra robôs de scraping.
* **Auditoria Integral de Imagens & 100% WebP (`ItauPreparationCase.tsx`):** Auditadas todas as 42 declarações de imagens do portfólio (0 distorções de proporção, 0 imagens quebradas). Convertidos os últimos 4 `.png` legados do Itaú (`itau-vencimentos-canonico`, `itau-vencimentos-eventos`, `itau-vencimentos-empty`, `itau-hub-liquidez-solucao`) para WebP de alta fidelidade (`q=92`, economia de 28% mantendo nitidez 1:1 de tipografia UI).
* **Substituição de Imagens Sintéticas por Evidências Reais do Figma (`CasePages.tsx`):**
  * **Tempo de Protrombina (RNI):** Removido o card sintético redesenhado (`76fe885`) e restaurado o recorte real do protótipo v3 do Figma (`1800×640 px`) com moldura pine e marcadores 1–4 alinhados à legenda.
  * **As 3 Macroáreas do Exame:** Substituído o diagrama sintético (`hiae-taxonomia-macroareas.webp`) pela prancha real de taxonomia clínica do Figma (`hiae-taxonomia-laudo-2000.webp`, `2000×1097 px`).
* **Upgrade Ultra-HD Retina em 10 Imagens de Evidência:**
  * `hiae-componente-protrombina-crop.webp`: re-renderizada em **2400×880 px** (2× Retina) com marcadores vetoriais anti-aliased (`1, 2, 3, 4` em Plus Jakarta Sans 700, zero serrilhado, zero sobreposição) sobre o recorte real v3 do Figma.
  * `hiae-taxonomia-laudo-2000.webp`: re-exportada diretamente do master PNG 3K (`3098×1576`) para **2560×1302 px** (`WebP q=95`).
  * Elevadas para **1440px–2000px** (Lanczos + micro-nitidez `UnsharpMask` + `WebP q=95`) todas as imagens abaixo de 1600px de Claro e Einstein (`claro-workshop`, `claro-jornadas`, `claro-detalhe-linha`, `claro-busca-cliente`, `hiae-ds-tokens-clean-1280`, `hiae-triangulacao-pesquisa-1200`, `hiae-visao-futura-mamografia`, `hiae-visao-futura-ressonancia`), com `width`/`height` sincronizados 1:1 em `CasePages.tsx`.
* **Enquadramento Full-Bleed do Hero (`case-presentation.css`, `hiae-capa-editorial-1600.webp`, `hiae-taxonomia-laudo-2000.webp`):**
  * Expandida a altura máxima do Master Hero de `clamp(280px, 36vh, 380px)` para **`clamp(340px, 58vh, 640px)`**, eliminando as faixas laterais vazias em todos os cases.
  * Recorte editorial fechado da capa Einstein (`2560×1271 px`) diretamente do master 3K com composição alfa em fundo branco puro (`#FFFFFF`), preenchendo ~95% da área útil com nitidez imediata na página.


### 2026-11-25 (Auditoria Visual Completa — Zero Duplicatas, Zero Baixa Resolução, Zero WIP)
- **Einstein (`CasePages.tsx`):**
  - Substituído Hero duplicado (`hiae-capa-editorial-1600.webp`, idêntico à taxonomia) por `hiae-multicanal-web-celular.webp` (`2000×1032`, Versões Digitais Tablet + Mobile + Versão Impressa A4).
  - Removida `hiae-laudo-proposta-demonstrativa-1600.webp` (duplicata da tela de Ressonância já apresentada em `hiae-visao-futura-ressonancia.webp`).
- **Claro (`CasePages.tsx`):**
  - Substituído Hero duplicado/com artefato (`claro-capa-editorial-1600.webp`) por `claro-ativacao-hero.webp` (`1440×680`), mantendo `claro-multicanal.webp` (`1376×932`) uma única vez na seção Multicanal.
  - Removida `claro-confirmacao-mobile.webp` (`280×606 px`, baixa resolução) e `claro-workshop.webp` (foto de parede com post-its ilegíveis).
- **Neoenergia (`CasePages.tsx`):**
  - Substituída `neoenergia-canais-atendimento.webp` (carimbo vermelho "Work in progress" + placeholder `~ X SEMANAS`) por `neoenergia-grandes-numeros.webp` (`1600×900`, limpo e factual).
  - Removida `neoenergia-jornada-futuro-tobe.webp` (marca d'água "WORK IN PROGRESS" e duplicata da matriz) e os verticais esmagados `blueprint-1` / `blueprint-2`.
  - Gerado recorte fechado 16:9 `neoenergia-blueprint-crop-uso-pago-1600.webp` (`1600×900`) em paridade visual com `neoenergia-blueprint-crop-contrato-1600.webp`.
- **Itaú (`ItauPreparationCase.tsx`):**
  - Removida `itau-planejamento-iniciativas.webp` (mosaico ilegível repetido 3x em Movimentações, Hub de Liquidez e Campanhas).
  - Removidas duplicatas idênticas entre Hero e evidências em Vencimentos (`itau-vencimentos-canonico.webp`), Hub de Liquidez (`itau-hub-liquidez-capa-1600.webp`), Movimentações (`itau-movimentacoes-capa/discovery.webp` substituídos pelo recorte focado `itau-movimentacoes-telas-1800.webp`) e Campanhas (`itau-campanhas-capa/screenflow.webp`, mantendo `itau-campanhas-configuracao-historica.svg` vetorial).


### 2026-11-25 (Diagramas Visuais de Fluxo de Jornada · Retina 2400×1350 + Proteção por Senha Padrão)
- **Proteção por Senha Padrão (`CaseAccessGate.tsx` + `CasePresentation.tsx`):**
  - Home (`/`) aberta; todos os cases atuais e futuros herdam proteção SHA-256 por padrão via `CasePresentation` (desbloqueio único por sessão em `sessionStorage`, zero senha em texto claro no código ou bundle).
- **Diagramas de Fluxo de Jornada em 2× Retina (`2400×1350`, WCAG AAA > 12:1, `Plus Jakarta Sans`):**
  - **Itaú (`itau-jornada-assessor-fluxo-2400.webp`):** Comparativo visual da jornada do assessor (*Estado Anterior Fragmentado* vs. *Esteira Integrada no Chassi IFA* com os 5 últimos eventos, síntese assistida por IA e gate obrigatório *Human-in-the-Loop*) + 3 barreiras de compliance.
  - **Claro (`claro-fluxo-esteira-unificada-2400.webp`):** Arquitetura da Esteira Unificada de 22 Jornadas em 5 Etapas (CPF → Elegibilidade → Contexto da Linha → Oferta + Resumo Lateral → Confirmação) com camada persistente de contexto e paridade Desktop/Mobile.
  - *Einstein* e *Neoenergia* mantidos sem diagramas sintéticos adicionais para evitar redundância com os entregáveis reais (taxonomia 3K e Service Blueprints oficiais).


### 2026-11-25 (Auditoria Profunda de Design System, Tipografia, Alinhamento & Quebras de Texto)
- **Especificidade e Escala Tipográfica Unificada (`case-presentation.css`):**
  - Corrigida especificidade destrutiva de `.cp-chapter-content p` / `h3` para filhos diretos (`> p` / `> h3`), blindando `.case-presentation .cp-figure-caption-text` (`14px` / `400` / `var(--cp-muted)` 100% idêntico no Hero, Capítulos, Splits e Galerias).
  - Unificados todos os `h3` de cards, splits, notes e decisões para a mesma escala (`1.1875rem` / `19px`, `600`, `line-height: 1.32`, `text-wrap: balance`).
  - Unificados tokens de cor de texto entre Home e Cases (`--cp-text: var(--ink, #1A201C)` e `--cp-text-muted: var(--muted, #4A554E)`) e tokens de border-radius (`--cp-radius-sm/md/lg/pill`).
- **Alinhamento & Quebras de Texto (`case-presentation.css` + `CasePages.tsx`):**
  - `.cp-split` atualizado para `align-items: start` (topo alinhado ao topo), proporção `minmax(0, 1.08fr) minmax(0, 1fr)` com `gap: 2.25rem`, `padding: 1.75rem` e `.cp-split-media { position: sticky; top: 5.5rem; }`.
  - Aplicado `text-wrap: balance` em todos os títulos e rótulos de métricas (`.cp-metrics dt`), `text-wrap: pretty` em parágrafos e listas, e `font-variant-numeric: tabular-nums` em `.cp-metrics dd`.
  - Removidos **100% dos estilos inline hardcoded** (`0` ocorrências em todos os cases), corrigida a dupla marcação (`• 1.`) na lista numerada da Neoenergia (`.cp-card-list--numbered`) e movido `.cp-note` para fora de `.cp-split-content` na Neoenergia.


### 2026-11-26 (QA Sentinel v2 · 12 Gates + UX Portfolio Review Checklist 2026 + Biblioteca de 19 Variações)
- **QA Sentinel v2 (`scripts/portfolio_qa_sentinel.py`):**
  - Expandido de 7 para **12 gates automatizados** (9 estáticos + 3 runtime reais no Chromium): zero estilos inline, zero vazamento de senha/e-mail, unicidade/WebP/HD de imagens, Gestalt Outside-In, alinhamento top-to-top, responsividade `1440/768/390`, tipografia computada, contraste WCAG 2.2, limite de navegação (`<= 6` itens), corpo `>= 16px` e validação E2E do `CaseAccessGate`.
- **Governança Permanente (`UX_PORTFOLIO_REVIEW_CHECKLIST_2026.md` + `AGENTS.md` Seção 8):**
  - Consolidado o framework operacional de 30 pontos (6 seções × 5 pontos) da UX Companion 2026 com scorecard inicial do portfólio em **`28/30`** (*Pronto para vagas Sênior/Staff*) e instituído como regra permanente de revisão.
- **Biblioteca de Direção de Arte (`D:\mockups-portfolio-studio\`):**
  - Arquivadas **28 referências visuais** (`ref-01` a `ref-28`, incluindo `Rabt`, `AeroLoad`, `Elegostra`, `FinChat`, `Nexus`, `Hornet`, `GridNest`) e geradas **19 variações em 2× Retina (`2400×1350`)** aplicadas sobre as telas reais dos 4 cases, com catálogo interativo (`catalogo-interativo.html`) e documentação (`CATALOGO_REFERENCIAS_E_VARIACOES.md`).


### 2026-11-26 (Consolidação da Trilogia Editorial UX Companion 2026)
- Documentados e indexados no repositório os 3 guias complementares curados:
  - `UX_AUDIT_FRAMEWORK_2026.md` (auditoria heurística + WCAG 2.2 + contraste em `:hover`/`:focus` + formato Top 3 por regra).
  - `SENIOR_PORTFOLIO_SIGNALS_2026.md` (os 6 sinais de banca Senior/Lead/Principal e Gap Analysis real do portfólio).
  - `UX_CASE_STUDY_STRUCTURE_2026.md` (anatomia de 7 seções em `1.000–1.800` palavras, 5 arquétipos de case e checklist pré-envio).

- Incorporado o **Template de 9 Blocos + Micro-Template de Decisão** (`ux-case-study-template`) em `UX_CASE_STUDY_STRUCTURE_2026.md` como modelo reutilizável para novos cases.


### 2026-11-26 (Integração Notion Portfolio Ops + Regra Permanente de Sincronização Omnicanal)
- **Notion Portfolio Ops (`4168db39b34f805884bad8f933e004dd`):**
  - Criada subpágina consolidada V3.6 (`4248db39b34f81a6b708c51aefce7209`), atualizados os 5 `🗂️ Ativos` principais para `Publicado` com URLs oficiais do GitHub Pages, registrada a versão vigente `v3.6.0` em `🔖 Versões` (`4248db39b34f81e1a8f6e1f99640b0f3`), criado o registro consolidado em `🔍 Diagnósticos` (`4248db39b34f81cab3d9caec248cdcee`) e registrada a avaliação `v3.6.0` em `⭐ Scorecard Geral` (`4248db39b34f81d5b498f527aad04b63`).
- **Governança Permanente (`AGENTS.md` Seção 9 + `senior-portfolio-audit/SKILL.md` + `INDEX_GOVERNANCA_E_DECISOES.md`):**
  - Instituída a obrigatoriedade de sincronização omnicanal automática em toda entrega: `site/` (GitHub Pages) + `portfolio-verde/` + `docs/` + **Notion Portfolio Ops**.
- **Consolidação Final do Cluster UX Companion 2026 (Antes/Depois + Entrevistas Sênior/Staff):**
  - Incorporado protocolo `ux-case-study-before-and-after` (Seção 7 de `UX_CASE_STUDY_STRUCTURE_2026.md`).
  - Criado `UX_INTERVIEW_AND_CHALLENGE_PLAYBOOK_2026.md` consolidando Apresentação de Portfólio (30/45/60 min), Whiteboard Challenge (45 min) e Take-Home Assignment (6h).
  - Criado `SCORECARD_VERSOES_E_VARIACOES_2026.md` com pontuação ponderada `v0.1 ➔ v3.6.0` e ranking das 19 variações `V01`–`V19`.
