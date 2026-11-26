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

### 2026-11-26 — Versão V3.10.1 (Inspeção Visual Comparativa — Craft da Seção Sobre, Plain Language & Kickers dos Cases)
- **Seção `#sobre` (`Home.tsx` + `portfolio.css`):** removido o box branco solto na coluna esquerda e substituídos os 3 links sublinhados por assinatura tipográfica limpa (`Senior Product Designer · São Paulo, Brasil · Remoto ou híbrido`), pills outline do Design System (`LinkedIn`, `Currículo PDF`) e linha de contato (`#contato`) sem duplicar o botão verde de baixo; fundo unificado em `--paper` com borda superior sutil (zero degrau visual antes de `#contato`).
- **Plain Language (`AGENTS.md` Seção 5):** reescritos os 2 parágrafos de `#sobre` eliminando *keyword stuffing* de IA e mantendo linguagem direta, natural e acessível; bloco `#contato` (`SiteChrome.tsx`) alinhado ao cargo real (**Senior Product Designer**, removendo `"Senior/Staff"`).
- **Kickers dos Cases (`CasePages.tsx`):** eliminadas repetições lado a lado entre pill e contexto em **Einstein** (`Saúde`), **Itaú** (`Itaú Unibanco`) e **Claro** (`Telecom`).

### 2026-11-26 — Versão V3.10.2 (Paridade Omnicanal 100% — Tablet, Submódulos Itaú, Plugin Figma, Figma Online & Notion)
- **Claro Tablet (`768px`, `case-presentation.css`):** ajustado `.cp-split-media .cp-figure-btn img` para `width: auto; max-width: 100%; height: auto; max-height: 420px;`, zerando `aspect_diff` de `claro-jornadas.webp` (`0.552 ➔ 0.000`) em Tablet.
- **Submódulos Itaú (`ItauPreparationCase.tsx`):** eliminada a redundância `summary`/`framing` nos 4 submódulos restantes (`vencimentos`, `movimentacoes`, `campanhas`, `registros-atendimento`) com separação estrita STAR (`Situação/Tarefa` vs. `Ação Técnica`).
- **Script Local do Plugin Figma (`scripts/build_portfolio_figma_screens.py`):** atualizado para `V3.10.2` com histórico completo `v0.1 ➔ v3.10.2` e bundles recompilados em `figma-refine-plugin` e `gemini-figma-plugin`.
- **Figma (`Template-portfolio` · `731:699`) & Notion Portfolio Ops:** página renomeada para `V3.10.2`, histórico atualizado na prancha `732:731`, versões anteriores arquivadas em `🔖 Versões` e subpágina consolidada atualizada para `V3.10.2` como única versão vigente.

### 2026-11-26 — Versão V3.11.0 (Gate 15 Determinístico, Painel de Personas Sintéticas, Open Graph Real & Plain Language Hero)
- **Sentinel v2 expandido para 15 Gates (`scripts/portfolio_qa_sentinel.py`):** novo **Gate 15** que bloqueia em código (`.githooks/pre-push` + CI) violações de Negative Prompting (27 termos proibidos incluindo `transformar`, `transformação`, `ajudo empresas a`), empilhamento de jargões de UX em inglês na Home (`Home.tsx`) e URLs antigas de Open Graph (`chatgpt.site`/`figma.site`).
- **Governança (`AGENTS.md` Seções 5 e 8):** incorporado o **UX Companion Pre-Publish Checklist (35 pontos)** (meta `34/35`, `97,1%`), a **Regra de Camada de Linguagem** (Home = Plain Language · Cases = Técnico Contextualizado) e o **Painel Obrigatório de Personas Sintéticas** (Recrutadora Sênior + Head of Design + UX Writer).
- **Hero Plain Language (`Home.tsx`):** definido pelo Painel de Personas Sintéticas sem repetir o `<h1>` e sem jargões em inglês (*"Atuação desde 2006 conectando pesquisa, fluxos e sistemas de interface com Produto e Engenharia. Recentemente no Itaú Unibanco, à frente do íon for Advisors para especialistas de investimentos."*).
- **Higiene Técnica UX Companion `t-5` & `p-2` (`index.html`, `PageMeta.tsx`, `case-presentation.css`):** `canonical`, `og:url`, `og:image`, `twitter:image` e `JSON-LD` corrigidos para `https://israelfull-commits.github.io/portfolio/`, `assetUrl` aplicado ao `socialImage` e prosa dos cases limitada a `max-width: 68ch`.

### 2026-11-26 — Versão V3.12.0 (Guia Consolidado 2026: 90 Códigos Congelados, 3 Skills Especializadas & Gate 15 Expandido)
- **Documento-Fonte Canônico:** criado [GUIA_CONSOLIDADO_REGRAS_E_CODIGOS_2026.md](../../docs/GUIA_CONSOLIDADO_REGRAS_E_CODIGOS_2026.md) com os **90 códigos congelados** (`HP`, `CS`, `TX`, `IA`, `AP`, `MB`, `TH`, `A`, `FG`), ordem de prioridade, níveis de confiabilidade (`N1`–`N4`) e resolução explícita de conflitos entre fontes.
- **3 Skills Especializadas em `.agents/skills/`:** criadas `portfolio-writing` (`TX-01..09`, `IA-01..04`, `CS-01..15`), `portfolio-design-qa` (`AP`, `MB`, `TH`, `A-01..28`, `FG`, Sentinel) e `portfolio-banca` (7 papéis calibrados com rubrica ponderada `/10` e âncoras `10` vs. `2`).
- **Governança (`AGENTS.md` Seção 12) & Gate 15 (`portfolio_qa_sentinel.py`):** expandido o bloqueio determinístico para novos termos `TX-03`/`TX-04` (`alta criticidade`, `desafiador`, `rigorosa`, `expertise`, `telemetria quantitativa`, `fui responsável por`) + guarda `TH-03`/`TH-06` contra caminho duplicado `/portfolio/portfolio/`. Corrigida ocorrência de `"Alta criticidade"` em `CasePages.tsx` e confirmado **HTTP 200 OK** no CV PDF em produção (`58.669 bytes`).

### 2026-11-26 — Versão V3.12.1 (Alinhamento ATS / Gupy / LinkedIn `HP-06`: "Mais de 15 anos de experiência")
- **Home, Meta Tags & Figma (`Home.tsx`, `index.html`, Figma `Home 1440`):** padronizado `"Mais de 15 anos de experiência"` na 1ª dobra, seção `#sobre`, `meta description`/`og:description` e kicker do Figma para máxima compatibilidade com filtros ATS/Gupy/LinkedIn e paridade `HP-06` (mantendo o histórico exato `2006 – 2026` na lista estruturada de trajetória).

### 2026-11-26 — Versão V3.12.2 (Precisão de Domínio Itaú IFA `TX-08` / `TX-09`: Especialistas × Assessores)
- **Home & Cases Itaú (`Home.tsx`, `CasePages.tsx`, `ItauPreparationCase.tsx`):** corrigida a distinção de cargos no ecossistema íon for Advisors (IFA) — **Especialistas de investimentos** e **Assessores** (que auxiliam os especialistas no acompanhamento das carteiras) nunca mais usados como sinônimos; glossário registrado em `TX-08` de `GUIA_CONSOLIDADO_REGRAS_E_CODIGOS_2026.md`.

### 2026-11-26 — Versão V4.0.0 (Híbrida Definitiva — Direção de Arte V3 Figma + Rigor Técnico, WCAG 2.2 & ATS da V3.12.2)
- **Hero (`Home.tsx` + `portfolio.css`):** restaurada legenda de credenciais no retrato (`Israel Rozar · Itaú · Einstein · R/GA · EY`), mantendo texto Plain Language + ATS (`"Mais de 15 anos de experiência"`).
- **Seção `#sobre` / Trajetória Editorial (`.pf-trajectory` + `.pf-timeline` + `.pf-education`):** restaurada a arquitetura editorial de 2 colunas da `V3 Figma Canônica` — coluna esquerda com cargo atual, 2 parágrafos curtos, pills `LinkedIn` + `Currículo (PDF)` e card dedicado de **Formação Acadêmica & Contínua** (`Ciência da Computação — Univali`); coluna direita com **Timeline Editorial em `24px`**, divisórias horizontais e pills de período (`2024 – 2026` ➔ `2006 – 2019`).
- **Contato Full-Craft (`Home.tsx` + `SiteChrome.tsx`):** substituído `<ContactSection compact />` pelo `<ContactSection />` completo com badge sólido `Contato` (`#16472A` WCAG AAA), divisória horizontal, CTA lima `Enviar e-mail` à esquerda e `Baixar currículo (PDF) • LinkedIn` (`>= 44px`) na barra inferior.
- **Validação:** build `0` erros, **15/15 PASS** no Sentinel v2, `0` erros em 18 viewports e inspeção visual óptica em Desktop (`1440px`) e Mobile (`390px`).

### 2026-11-26 — Versão V4.0.1 (Correção Integral dos 7 Desvios Visuais & de Design System nos Cases)
- **Header Scrolled 100% Opaco (`site/src/index.css`):** elevado `.site-header` para `z-index: 40` e definido `.site-header.is-scrolled` com `background: var(--paper)` 100% opaco + sombra suave (`A-13` / `AP-07`), eliminando sangramento de headings, sidebar e cards escuros atrás da barra fixa durante a rolagem. Adicionado `site/src/index.css` ao espelhamento automático `--sync` do Sentinel (`portfolio-verde/src/index.css`).
- **Sidebar `NESTE CASE` & Rodapé de Navegação Full-Width (`CasePresentation.tsx` + `case-presentation.css`):** movido `.cp-explore-section` (*Continue explorando os projetos* + cards *Case anterior / Próximo case*) para fora de `.cp-body`, alinhando os cards em `1152px` sobre `<ContactSection />` e eliminando o corte abrupto do índice lateral no rodapé (`AP-06`).
- **Prosa Unificada 68ch no Capítulo 01 (`case-presentation.css`):** convertido `.cp-summary` de grid 2 colunas desalinhado (`18px` escuro vs `16px` cinza lado a lado) para coluna única editorial `max-width: 68ch` (`AP-02`), garantindo ritmo tipográfico idêntico nos 4 cases.
- **Lista Ordenada Decimal no Fluxo Itaú (`case-presentation.css`):** adicionado `ol.cp-list { list-style: decimal; }` para que etapas sequenciais (`<ol>`) exibam numeração `1. 2. 3. 4.` em vez de marcadores circulares.
- **Proporção Natural 1:1 na Galeria do Einstein (`case-presentation.css`):** ajustado `.cp-gallery .cp-figure-btn` para `aspect-ratio: auto` (`img { width: auto; max-width: 100%; height: auto; max-height: 360px; }`), zerando a compressão `aspectDiff = 0.113` nas imagens `mamografia` e `ressonancia` (`AP-04`).
- **Respiro da Legenda Hero & Padronização dos Cards de Navegação (`case-presentation.css`, `CasePages.tsx`, `CasePresentation.tsx`):** padding horizontal na legenda do Hero (`.cp-hero-visual figcaption`), unificação de `"Itaú Corretora"` ➔ `"Itaú Unibanco"`, `"Service design"` ➔ `"Service Design"`, `"Utilities"` ➔ `"Energia"` e substituição do fallback `"Alta criticidade"` por `"Operação financeira"` (`TX-03`).

### 2026-11-26 — Versão V4.0.2 (Varredura Total da Hero Home · 12 Versões Auditadas · Paridade Omnicanal 100%)
- **Varredura Completa & Banca Calibrada (`AUDITORIA_COMPARATIVA_HERO_HOME_2026.md`):** mapeadas todas as **12 versões/variações históricas da Hero da Home** (Git `9399562` ➔ `de55343`, Figma `Template-portfolio` páginas `0:1`, `563:2552` e `731:699`, plugin local `build_portfolio_figma_screens.py`, docs e Notion) avaliadas pelas 3 skills (`portfolio-writing`, `portfolio-banca` 7 papéis e `portfolio-design-qa`) sob os 90 códigos congelados (`GUIA_CONSOLIDADO_REGRAS_E_CODIGOS_2026.md`).
- **Refinamento Cirúrgico do Lead na Produção (`site/src/pages/Home.tsx`):** mantido o H1 vencedor (*"Design de produtos para saúde, finanças e serviços essenciais."*) e corrigidos 3 desvios sutis no Lead (`TX-01`/`TX-02` voz ativa em 1ª pessoa `"estruturo"` / `"conduzi"`, `TX-06`/`TX-09` removendo o ambíguo `"à frente do íon for Advisors"`, e `TX-08` alinhando ao glossário oficial Itaú IFA `"para especialistas de investimentos e assessores"`).
- **Eliminação de Drift Omnicanal (`scripts/build_portfolio_figma_screens.py` + Figma `731:699`):**
  - Substituído no gerador do plugin o resíduo V2B (*"Alta Criticidade"*, *"Expertise"*, *"rigorosa"*, *"TELEMETRIA QUANTITATIVA"*, texto `11px`) pela Hero V4.0.2 (`>= 12px` `FG-06`), com bundles recompilados em `figma-refine-plugin` e `gemini-figma-plugin`.
  - Sincronizados no Figma (`731:699` · `Tela 01 · Home · Desktop 1440`) o kicker (`11px → 12px` `FG-06`), H1 (`críticos → essenciais`), Lead, CTAs e documentação (`17+ anos → Mais de 15 anos` `HP-06`), validados por screenshot.
- **Proveniência:** IA `Antigravity — Google DeepMind` · Atualização `2026-11-26` · Conversa `conversation://66417f41-f841-4d50-a701-e678302e3ec2`.

### 2026-11-26 — Versão V4.1.0 (Varredura Editorial Integral de Todos os Textos · 4 Subagentes Paralelos · Paridade Omnicanal)
- **Auditoria Completa Consolidada (`AUDITORIA_INTEGRAL_TEXTOS_PORTFOLIO_V4_1_2026.md`):** mapeadas e pontuadas todas as gerações (`V1 ➔ V4.1.0`) de Home fora do Hero, Global Chrome (`SiteHeader`, `ContactSection`, `CaseAccessGate`, `NotFound`), Meta/JSON-LD, Einstein, Claro, Neoenergia, Suíte Itaú IFA (5 módulos), Figma `731:699` e `build_portfolio_figma_screens.py` sob os 90 códigos congelados.
- **Home (fora do Hero), Global Chrome & Higiene Técnica (`Home.tsx`, `SiteChrome.tsx`, `CaseAccessGate.tsx`, `NotFound.tsx`, `index.html`, `PageMeta.tsx`):**
  - Corrigido bug em `site/index.html:63` que sobrescrevia `JSON-LD Person.url` para `/` em runtime (`TH-05`), unificada `meta description` com `Home.tsx` e restaurado `max-image-preview:large` em `PageMeta.tsx`.
  - Adicionados `skip-link` e `tabIndex={-1}` em `CaseAccessGate` e `NotFound` (`A-12`), removido `"ou ainda estar em preparação"` de `NotFound` (`TX-04`/`TX-06`), restaurado `sr-only (abre em nova aba)` no `LinkedIn` de `ContactSection` (`A-15`/`A-23`) e unificados os 4 CTAs da Home em `Ver estudo de caso` (`A-23`/`TX-08`).
  - Refinada a seção `#sobre` com frases curtas (`TX-07`), fronteira explícita de julgamento humano em IA (`IA-01`), `Estudos complementares` e `e outras` (`TH-08`).
- **4 Flagship Cases (`CasePages.tsx`, `ItauPreparationCase.tsx`, `CasePresentation.tsx`, `CaseReadingTime.tsx`, `generate_spa_routes.js`):**
  - **Einstein:** removidos anacronismo `WCAG 2.2 AAA` (2022), *"em produção"* sem lastro e especialidades sem fonte (`TX-09`/`CS-14`); adicionados 2 cards de decisão no micro-template (`CS-06`/`TX-05`), legendas de porquê (`CS-07`), reflexão de 3 frases (`CS-09`) e `7 min de leitura`.
  - **Itaú IFA (5 módulos):** eliminado boilerplate idêntico (F02 · `CS-09`/`CS-10`) com Escopo e Reflexão exclusivos por módulo; corrigida contradição factual na legenda/alt de *Movimentações*, termo sem lastro em *Vencimentos*, H2 `TX-08` em *Campanhas*, 3 decisões com trade-offs nos 5 módulos (`CS-06`), `ENTREGA PRINCIPAL` (`CS-08`), identificação ilustrativa em *Registros* (`IA-04`), rota SPA `cases/itau/registros-atendimento` (`TH-03`) e tempo de leitura de `vencimentos` (`CS-11`).
  - **Claro & Neoenergia:** 3 decisões estruturadas com custo aceito em cada case (`CS-06`/`TX-05`), declarações honestas de status/medição (`CS-14`/`TX-06`), remoção de `"até 40%"` sem protocolo na Claro e de overclaims de código/WCAG/tempo real na Neoenergia (`TX-09`), correção do estágio `5. Abandono` e `alt` da prancha Neoenergia (`A-01`/`TX-08`), correção da tag/H2 do Cap. 5 da Claro (`Acervo & Equipe` · `A-15`/`A-16`) e `target="_blank"` acessível em `Sources` (`A-15`).
- **Figma `731:699` & Plugin (`build_portfolio_figma_screens.py`):** `84` nós elevados de `11px → 12px` (`FG-06`), `"transformar"` corrigido em `737:829` (`TX-04`), cards/Sobre sincronizados em `736:703` e 8 violações limpas no gerador do plugin com recompilação em `figma-refine-plugin` e `gemini-figma-plugin`.
- **Validação:** build `0` erros (8 rotas estáticas SPA `200 OK`), **15/15 PASS** no Sentinel v2, espelho `portfolio-verde/` sincronizado e inspeção visual óptica em Desktop (`1440px`) e Figma.
- **Proveniência:** IA `Antigravity — Google DeepMind` · Atualização `2026-11-26` · Conversa `conversation://66417f41-f841-4d50-a701-e678302e3ec2`.
