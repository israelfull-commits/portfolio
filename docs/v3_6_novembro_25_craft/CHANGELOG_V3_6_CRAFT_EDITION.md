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
- **Curadoria Zero-Duplicidade NN/g + W3C WCAG 2.2 (5 fontes primárias):**
  - Incorporados apenas itens novos/superiores nos docs existentes (sem criar arquivos redundantes): `2.4.11/2.4.12 Focus Not Obscured` (`scroll-padding-top`) e `3.3.8 Accessible Authentication` (`CaseAccessGate`) em `UX_AUDIT_FRAMEWORK_2026.md`; taxonomia Contínuas/Discretas/Binárias + regra *Don't Overthink UX ROI* em `UX_CASE_STUDY_STRUCTURE_2026.md`; *Story Triangle* e *Autoavaliação Anual (1h30–2h)* em `UX_INTERVIEW_AND_CHALLENGE_PLAYBOOK_2026.md`.
- **Auditoria de Governança, Regras, Skills & Higiene do Repositório:**
  - `AGENTS.md` evoluído com **Seção 10** (*Paridade Estrita de Design System Home ↔ Cases*) e **Seção 11** (*Higiene de Repositório & Catálogo dos 2 Scripts Canônicos*).
  - `.agents/skills/senior-portfolio-audit/SKILL.md` deduplicada (aponta para `AGENTS.md` como fonte única de regras e mantém o protocolo operacional de 14 gates + inspeção visual obrigatória).
  - Criado `AUDITORIA_GOVERNANCA_E_HIGIENE_REPO_2026.md` mapeando 15 `.md` duplicados por SHA-256 na raiz, `110,6 MB` de prints/`.gz` soltos e 596 arquivos legados em `scripts/` para arquivamento seguro após consentimento.


### 2026-11-26 — Versão V3.7.0 (Publicada em Produção · GitHub Pages)
- **Combo Campeão de Estúdio (9 artes `2400×1350` 2× Retina WebP, `aspectDiff = 0.0000`):**
  - **Einstein:** `V17` (Hero Bento Clínico), `V03` (Antes vs. Depois), `V13` (Paridade 3 Canais A4/Web/Mobile).
  - **Itaú (`hub-liquidez` e `registros-atendimento`):** `V16` (Hero Fintech Bento) e `V07` (Jornada IA + Human-in-the-Loop).
  - **Claro:** `V08` (Hero Multicanal Desktop + iPhone) e `V10` (Esteira Unificada em 5 Etapas).
  - **Neoenergia:** `V12` (Hero Bento Executivo) e `V11` (Service Blueprints Studio Desk em largura cheia `860×484`).
- **Copy Senior/Staff (Protocolo Antes ➔ Depois):** explicitados desacordos construtivos por papel (corpo clínico no Einstein, lideranças comerciais na Claro, diretorias regionais na Neoenergia) e mentoria/critique.
- **Alinhamento Canônico do Design System (Home ↔ Cases):**
  - Escala tipográfica monotônica na Home (`h1 56px ➔ h2 32px ➔ h3 24px ➔ body 16px`), grid estrito de `8px` nos Cases (`.cp-chapter 72px`, `.cp-split 24px / gap 32px`, `.cp-note 24px 32px`), `.cp-figure` único em todo o site, Heroes `1120×630` *edge-to-edge* e remoção da imagem órfã em meia coluna no Itaú.
- **Sentinel v2 expandido para 14 Gates (`14/14 PASS`):** novos Gates 13 (`WCAG 2.2 2.4.11 Focus Not Obscured` + `3.3.8 Accessible Auth`) e 14 (contraste `:hover` + `2.4.13 :focus-visible`).
- **Higiene Segura do Repositório:** raiz reduzida para 3 arquivos canônicos (`.gitignore`, `AGENTS.md`, `SENIOR_UX_PORTFOLIO_CANON.md`), `scripts/` reduzido para 2 motores canônicos (`portfolio_qa_sentinel.py` e `build_portfolio_figma_screens.py`), legados preservados em `D:\arquivo-morto-portfolio\`.


### 2026-11-26 — Versão V3.8.0 (Anti-Template · 4 Arquiteturas Narrativas Sob Medida · Publicada em Produção)
- **Eliminação Total de "Sinal de Bootcamp" (`CasePresentation.tsx` + `CasePages.tsx`):**
  - `CaseChapter` agora aceita `id` e `tag` próprios por case, removendo a obrigatoriedade do template idêntico de 7 capítulos iguais.
  - **Einstein (`6` caps):** `01 Tese Clínica` · `02 Tela & Papel (Antes/Depois)` · `03 Taxonomia de Dados` · `04 Anatomia do Componente` · `05 Escala em 80+ Exames` · `06 Compreensão, Escopo & NDA`.
  - **Itaú IFA (`5` caps · Decision-Led):** `01 Gargalo Operacional` · `02 3 Decisões de Arquitetura` (promovidas para o cap. 2) · `03 Fluxo & Interface Canônica` · `04 Salvaguardas & Aprendizado` · `05 Escopo & Conformidade` (títulos específicos por módulo, zero *"O projeto em perspectiva"*).
  - **Claro (`5` caps · Multicanal):** `01 Operação Fragmentada` · `02 22 Jornadas ➔ 5 Etapas` · `03 Contexto Fixo & Resumo Lateral` · `04 Paridade Desktop & Mobile` · `05 Escopo, Reflexão & Equipe`.
  - **Neoenergia (`6` caps · Service Design):** `01 Escala Nacional (34M)` · `02 Auditoria de Backstage` · `03 5 Service Blueprints` · `04 Design System Multi-Tenant` · `05 Matriz de 118 Ideias` · `06 Governança P&D ANEEL`.
- **Governança (`AGENTS.md` Seção 10):** regra permanente Anti-Template de Bootcamp adicionada.
- **Validação:** build `0` erros (`4.12s`), **14/14 PASS** no Sentinel v2 e inspeção visual em Chromium (`1440×900`) nos 4 índices e capítulos.
- **Automação Contínua do Script Único de Validação (3 camadas):**
  - `.githooks/pre-push` ativado via `git config core.hooksPath .githooks` (bloqueia qualquer `git push` fora do padrão 14/14 PASS).
  - Scripts npm em `site/package.json`: `qa` (estático), `qa:full` (build + 14 gates) e `qa:sync` (build + 14 gates + espelho `portfolio-verde/`).
  - Gate automático no CI/CD (`.github/workflows/deploy.yml`) executando `portfolio_qa_sentinel.py --fast` antes do upload para GitHub Pages.
- **Sincronização Figma Desktop V3.8.0 + Bloco de Proveniência (`build_portfolio_figma_screens.py`):**
  - Criado componente reutilizável `buildProvenanceBanner()` injetado automaticamente na Home, nos 4 Cases e na Prancha de Documentação/Handoff V3.8.0 com **IA (`Antigravity — Google DeepMind`)**, **Data de criação (`2026-11-01`)**, **Última atualização (`2026-11-26 07:37 BRT`)** e **ID/Link da conversa (`b9eff66e-96f2-48ed-af7d-28e8cea0dfad`)**.
  - Prancha de Documentação expandida para 6 blocos completos (Paleta & WCAG 2.2 AAA, Tipografia & Grid 8px, Biblioteca de Componentes, Regras `AGENTS.md` + Anti-Template, Handoff Técnico + Sentinel 14 Gates e Histórico `v0.1 ➔ v3.8.0`).
  - Plugins recompilados e sincronizados em `figma-refine-plugin` e `gemini-figma-plugin` (ES5/ES6 clássico).


### 2026-11-26 — Versão V3.9.0 (Auditoria Editorial STAR, Negative Prompting, ATS & Seção Sobre Reestruturada)
- **Correção de 2 Inconsistências Factuais/Numéricas em Produção:**
  - Corrigido vazamento de `34M de clientes` (dado da Neoenergia) nos cards de navegação da **Claro** (`CasePages.tsx`) para `22 jornadas unificadas`.
  - Sincronizado o escopo da Claro na Home (`Home.tsx`) de `"70+ validações"` para `"22 jornadas unificadas · 20 entrevistas · 70 oportunidades"` (paridade 1:1 com o case).
- **Reestruturação UX/UI da Seção `#sobre` (`Home.tsx` + `portfolio.css`):**
  - Layout em 2 colunas equilibradas (`1fr 1.5fr`, grid estrito de `8px`): coluna esquerda com título, card de **cargo atual claro** (`Senior Product Designer · São Paulo, BR · Remoto / Híbrido`) e ações diretas de prova social e contato (`LinkedIn`, `Currículo PDF`, `Enviar e-mail` protegido anti-spam, alvos `>= 44px`).
  - Coluna direita com **2 parágrafos curtos** técnicos (STAR + ATS: `Human-Centered Design (HCD)`, `Product Discovery`, `Arquitetura da Informação`, `componentes escaláveis`, `WCAG 2.2`, `automação de processos`) e trajetória resumida.
- **Erradicação de 7 Violações de Negative Prompting & Clichês de IA (`CasePages.tsx` + `ItauPreparationCase.tsx` + `SiteChrome.tsx` + `CaseAccessGate.tsx`):**
  - Removidos `"Cabeçalho limpo"`, `"colunas limpas"`, `"visual bonito"`, `"sem poluição visual"`, `"permanece no centro da decisão"`, `"em estreita colaboração"`, `"Inovações de Longo Prazo"`, `"Exploro recursos de IA"`, `"3 segundos"`, `"plantão cansativo"` e resíduos em 3ª pessoa (`"O autor confirmou"`).
  - Eliminada redundância entre `summary` e `framing` no Capítulo 1 do **Itaú (`hub-liquidez`)** com separação estrita `Situação/Tarefa` vs. `Ação Técnica` (STAR) e novo subtítulo técnico.
  - Atualizados Hero Lead, Bloco de Contato Compacto e microcopy de NDA no `CaseAccessGate`.


### 2026-11-26 — Versão V3.10.0 (Auditoria UX/UI Profunda em 18 Viewports + Correção de 6 Defeitos Reais)
- **P0 — Botão Submit do `CaseAccessGate` (`CaseAccessGate.tsx`):** corrigida classe inexistente `.pf-button-primary` para `.pf-button-pine`, restaurando o preenchimento verde-pinho `#0A3622` e contraste WCAG AAA (`13.8:1`) no CTA *"Acessar estudo de caso →"*.
- **P1 — Conformidade Total WCAG 2.2 `2.5.8 Target Size` (`>= 44px`):** elevados alvos de toque abaixo de 44px em `.cp-gate-back` (`23px ➔ 44px`), `.cp-gate-request` (`40px ➔ 44px`), `.cp-appendix summary` (`26px ➔ 44px`), `.cp-appendix .cp-list a` (`21px ➔ 44px`), `.pf-contact-links a` (`36px ➔ 44px`), `.cp-breadcrumb a` (`40px ➔ 44px`), `.cp-lightbox-trigger` (`40px ➔ 44px`) e `.cp-lightbox-size` (`32px ➔ 44px`).
- **P1 — Proporção Natural em `.cp-split-media` (`case-presentation.css`):** removido o `aspect-ratio: 16 / 10` forçado que comprimia `claro-jornadas.webp` (`1440×1440`, `aspect_diff = 0.65`) e `claro-multicanal.webp` (`aspect_diff = 0.12`), preservando a proporção real de cada evidência (`aspect-ratio: auto; max-height: 420px;`).
- **P2 — Contraste Sólido no Badge `.pf-contact-label` (`portfolio.css`):** trocado `rgba(206, 255, 26, 0.16)` pelo tom sólido equivalente `#16472A` com texto `--lime` (`> 9.5:1` WCAG AAA, zero falsos positivos).
- **P3 — Pintura Instantânea no Preview Mobile (`Home.tsx`):** aplicado `decoding="sync"` e `fetchPriority="high"` no preview do tablet Einstein na Home.
