# Varredura Exaustiva de Versões & Auditoria Editorial dos Cases (`V0 ➔ V4.2.0`)

> **Proveniência & Rastreabilidade**  
> - **IA / Plataforma:** Antigravity — Google DeepMind  
> - **Data de criação:** 2026-11-26  
> - **Última atualização:** 2026-11-26  
> - **Conversa de origem:** [66417f41-f841-4d50-a701-e678302e3ec2](conversation://66417f41-f841-4d50-a701-e678302e3ec2)  
> - **Agentes & Skills aplicados:** 4 auditores paralelos por case (`Einstein`, `Itaú IFA 5 módulos`, `Claro Brasil`, `Neoenergia`) · `portfolio-writing` · `portfolio-banca` (rubrica ponderada `/10` de 7 papéis) · `portfolio-design-qa` · `senior-portfolio-audit` · `figma-use` · `portfolio_qa_sentinel.py` (15 gates)  
> - **Fontes varridas:** Histórico completo Git (`9399562` ➔ `45d1957` + branch `feat/cases-editoriais-revisao`), `figma-make-reference/`, `docs/v1..v3.6/`, `scripts/build_portfolio_figma_screens.py`, `site/public/llms.txt` & `ai-catalog.json`, Figma `Template-portfolio` (`YIHybVXPe0Hfmja1hAyzQZ` — páginas `30:2`, `67:2`, `232:312`, `480:9183`, `563:2552`, `731:699`), Figma `Case Editorial | Hub de Liquidez` (`0sQ9hoPAkVCtyyEsxOzy9j`) e Notion Portfolio Ops.  
> - **Norma aplicada:** [GUIA_CONSOLIDADO_REGRAS_E_CODIGOS_2026.md](../GUIA_CONSOLIDADO_REGRAS_E_CODIGOS_2026.md) (90 códigos congelados) & [AGENTS.md](../../AGENTS.md)

---

## 1. Resumo Executivo & Comparativo Consolidado (`Score Ponderado da Banca /10`)

> **Pesos oficiais da banca (`portfolio-banca`):** Resultado c/ baseline (`20`) · Decisões e trade-offs (`15`) · Liderança e influência (`15`) · Papel declarado (`10`) · Problema e enquadramento (`10`) · Pesquisa por insight (`10`) · Legibilidade (`10`) · Acessibilidade (`10`).

| Case Study | Total de Versões Mapeadas | Pior Versão (Score) | Versão Anterior `V4.1.0` | **Versão Campeã `V4.2.0`** | Principais Ganhos da `V4.2.0` |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **01 · Hospital Albert Einstein** | **15** *(V0 ➔ V4.2 + Figma `v-banca` + Plugin)* | Plugin legado (`3,45/10`) | `8,55 / 10` | **`9,75 / 10`** | Resumo `CS-01` 4 frases + `metaDescription` (`TH-05`); Decisão 03 factual (Word/cabeçalho comum) fechando 3 decisões completas `CS-06`; diferenças explícitas **`21,6 p.p.`** e **`25,4 p.p.`** (`CS-08`); triangulação 4 frentes sem inferência (`TX-09`); dead code `einsteinImages` removido; plugin Figma livre de `DICOM` e `6 componentes mestres`. |
| **02 · Itaú IFA (5 módulos)** | **13** *(V0 ➔ V4.2 + Figma `0sQ9ho` `v-banca` + `783:*` + Plugin)* | V0 Figma Make (`3,30/10`) / Plugin (`4,10/10`) | `7,80 / 10` | **`9,35 / 10`** | Headlines declarativas + resumos `CS-01` completos + `metaDescription` nos 5 módulos; 15 decisões completas no micro-template `CS-06` (`Pergunta → Opções → Decisão/trade-off → Evidência`); bloco explícito `Estágio da entrega e escopo de medição` (`CS-08`/`CS-14`/`TX-06`); `reverteria` (`CS-09`); links cruzados entre os 5 módulos no Apêndice (`HP-07`); remoção de ~350 linhas mortas V1 de `ItauPreparationCase.tsx`; erradicação de `R$ 42.4B` / `transformando` / `em segundos` no plugin Figma. |
| **03 · Claro Brasil** | **13** *(V0.1 ➔ V4.2 + Figma `61:2`/`486:14029` + Plugin)* | UXfolio (`2,70/10`) / Plugin (`3,55/10`) | `8,43 / 10` | **`9,55 / 10`** | `CS-01` de 4 frases + `metaDescription`; micro-template completo nas Decisões 2 e 3 + correção `TX-05`; período `2017–2018` (`CS-04`); Cap. 5 reestruturado (`Entrega, Escopo e Reflexão` · `A-16`) com efeito no time (`CS-12`) e nota explícita de NDA (`CS-15`); eliminação de `handoff`/`celular`/`limite das medições`; erradicação no plugin de `5G`, `carrinho B2C`, `10 entrevistas` e `70+ testes`; remoção de `"até 40%"` do Figma `731:699`. |
| **04 · Neoenergia (P&D ANEEL)** | **11** *(V0 Dossiê ➔ V4.2 + Figma `486:13375`/`574:2386` + Plugin)* | V1 (`4,70/10`) / Plugin (`4,70/10`) | `8,19 / 10` | **`9,41 / 10`** | **Correção crítica `A-01`/`TX-09`/`CS-07` na Figura 5** (`neoenergia-entregaveis-ui-design-system.webp` é o slide EY `Relação de Entregáveis Etapas 4–6`, não um portal pronto); micro-template completo nas 3 decisões com evidência factual (3 notas de OS desintegradas); `co-construí` corrigido (`TH-08` + `CS-03`); `Quick Wins` e `esteira` removidos (`TX-04`); `34M de habitantes` unificado até em Einstein `prevCase` (`TX-08`); Google Slides `/edit` ➔ `/preview` (`TH-07`); plugin sincronizado 1:1. |

*(Registro de acervo arquivado: `docs/v2_novembro_14_15/salarynow_case_star_synthesis.md` e `CASE_SALARYNOW` no plugin representam um 5º case — desafio prático PM3 — mantido intencionalmente fora das rotas do site em produção.)*

---

## 2. Mapeamento Detalhado de Todas as Versões por Case

### 2.1. Case 01 · Hospital Albert Einstein (`einstein-laudos`) — 15 Versões

| ID | Origem / Artefato | Score `/10` | Principais Falhas / Achados |
| :--- | :--- | :---: | :--- |
| **E-V0** | `figma-make-reference/.../EinsteinCase.tsx` | `5,12` | Disclaimers defensivos (*"conteúdo fictício"*, *"não se somam"*), voz impessoal, sem trade-offs/reflexão/NDA (`CS-06/09/12/15`, `TX-01/05`). |
| **E-V1** | Git `9399562` · Figma `59:2` / `574:2344` | `5,08` | 7 caps idênticos (`CS-10`), links internos Notion/Figma expostos (`CS-15`), disclaimers defensivos, sem resultado no Hero (`CS-01`). |
| **E-V2.0** | Git `01faf96` | `5,22` | Remove parte dos disclaimers, adiciona detalhes de Protrombina (`plasma/Atividade/RNI`), mas mantém Ch6 defensivo e links expostos. |
| **E-V2A.1–2** | Git `c3479c3` / `ba58351` | `4,80–5,00` | Pico de jargão acadêmico (`ancoragem determinística`, `desacoplamento de metadados`, `rigorosa`, `transformar`, `LIS/PACS` sem lastro · `TX-03/04/07/09`). |
| **E-V2B.1–2** | Git `f79cb41` / `779f5c6` | `5,80–6,48` | Resgata pergunta norteadora autêntica, Zera 1.0 e Q1–Q4 (`81,6%/77,8%/58,8%/56,2%`), mas sem trade-offs/reflexão e com `"visual bonito"` (`TX-04`). |
| **E-V3.5–V3.10** | Git `dfa8b19` ➔ `3eb51d2` · Figma `737:707` (v3.8) | `7,00–7,15` | Adiciona NDA (`7ae34e9`), 6 caps sob medida (`7c6dde2`) e Escopo/Reflexão, porém introduz `WCAG 2.2 AAA` anacrônico (2022), `"em produção"` e especialidades sem lastro (`TX-09`). |
| **E-Figma `v-banca`** | Figma `Template-portfolio` `67:2` · `783:1224` | `6,80` | Headline boa (*"Laudos clínicos: clareza não é o mesmo que compreensão."*), mas herda corpo antigo de `59:2` sem decisões `CS-06` nem `p.p.`. |
| **E-Plugin (antigo)** | `build_portfolio_figma_screens.py` (pré-V4.2) | `3,45` | **Alto risco `TX-09`/`IA-02`:** inventava `visualizadores DICOM`, `6 componentes mestres`, `aprovada pela diretoria clínica`, `WCAG AAA rigorosamente testadas`, `América Latina`. |
| **E-V4.1.0** | Git `a9ef404` | `8,55` | Limpa anacronismos e adiciona 2 decisões + reflexão, mas faltava problema no Hero (`CS-01`), Decisão 03 (`CS-06`), `p.p.` (`CS-08`), `einsteinImages` morto e 5 variações terminológicas (`TX-08`). |
| **E-V4.2.0 🏆** | **Produção atual + Figma `737:707` + Plugin** | **`9,75`** | **0 falhas congeladas.** 3 decisões `CS-06`, `21,6 p.p.` e `25,4 p.p.`, 4 frentes factuais de descoberta, `metaDescription` + OG estático, terminologia única (`sistemas laudadores`, `celular`, `impressão P&B`, `proposta v3`). |

### 2.2. Case 02 · Itaú Unibanco · Plataforma IFA (5 Módulos) — 13 Versões

| ID | Origem / Artefato | Score `/10` | Principais Falhas / Achados |
| :--- | :--- | :---: | :--- |
| **I-V0** | `figma-make-reference/.../ItauPreparationCase.tsx` | `3,30` | 3 dossiês *"em preparação"*, *"Contribuição individual: Pendente"*, `150→27s` sem protocolo (`TX-09`). |
| **I-V1** | Git `9399562` · Figma `60:2..64:2` | `4,30` | 7 caps idênticos, 3ª pessoa (*"confirmada pelo autor"*), IDs internos de Figma no texto, disclaimers defensivos. |
| **I-V2–V3.1** | Git `573bd82` ➔ `a35d800` | `5,30–5,50` | Remove disclaimers e IDs internos, enquadra LGPD, mas mantém clichê `"no centro da decisão"` e `assessor` como sinônimo (`TX-04/08`). |
| **I-V3.5–V3.12.2** | Git `dfa8b19` ➔ `8e4ffcd` · Figma `737:778` | `5,90–6,70` | Arquitetura 5 caps Decision-Led (`7c6dde2`) e distinção `Especialista × Assessor` (`8e4ffcd`), mas Escopo/Reflexão idênticos nos 5 módulos (`CS-09/10`) e decisões sem `TX-05`. |
| **I-Figma `0sQ9ho`** | Figma `0sQ9hoPAkVCtyyEsxOzy9j` (Hub Editorial) | `6,40` | Boa tese (*"Qual cliente precisa de atenção imediata — e por quê?"*) e temporalidades `D-1/D-2`, porém usa `"Transformar"` (`TX-04`), bloco defensivo `"Status das evidências"` e 0 reflexão crítica (`CS-09`). |
| **I-Figma `v-banca`** | Figma `67:2` · `783:1674`, `783:2070`, `783:2426` | `6,10` | Declara `"em produção"` sem lastro reconciliado (`TX-09`) e mantém estrutura antiga sem `CS-06`/`CS-09`. |
| **I-Plugin (antigo)** | `build_portfolio_figma_screens.py` (pré-V4.2) | `4,10` | **Alto risco `TX-04`/`TX-08`/`TX-09`:** `R$ 42.4B`, `R$ 8.2B`, `R$ 3.1B`, `142 Ativas`, `"transformando"`, `"sugerindo automaticamente produtos"`, `"disparar propostas"`, `"em segundos"`, `"atuação do assessor"`. |
| **I-V4.1.0** | Git `a9ef404` | `7,80` | Escopo/Reflexão exclusivos por módulo e 15 decisões com trade-offs, mas `subtitle` de 5–7 palavras (`CS-01`), sem bloco de estágio/medição (`CS-08`/`CS-14`), 4 submódulos órfãos (`HP-07`) e código morto V1 em `ItauPreparationCase.tsx`. |
| **I-V4.2.0 🏆** | **Produção atual + Figma `737:778` + Plugin** | **`9,35`** | Headlines declarativas + `CS-01` completo + `metaDescription` nos 5 módulos; 15 decisões completas `CS-06`; bloco explícito `Estágio da entrega e escopo de medição`; `reverteria` (`CS-09`); navegação interna entre os 5 módulos; 0 código morto V1; plugin 100% factual. |

### 2.3. Case 03 · Claro Brasil (`Ativação Simplificada`) — 13 Versões

| ID | Origem / Artefato | Score `/10` | Principais Falhas / Achados |
| :--- | :--- | :---: | :--- |
| **C-V0.1** | UXfolio (baseline pré-Nov/2026) | `2,70` | Plataforma genérica sem trade-offs, a11y ou profundidade sênior. |
| **C-V1.0–V2.0** | Git `9399562` ➔ `573bd82` · Figma `61:2` | `4,30–4,97` | 7 caps idênticos, `"sem poluição visual"`, `"estreita colaboração"`, link UXfolio e disclaimers defensivos. |
| **C-V2.1–V3.10** | Git `fd8d0e8` ➔ `de55343` · Figma `737:846` | `5,22–7,05` | Evolui para 5 caps sob medida (`7c6dde2`) e desacordo construtivo (`7b08fdb`), mas carregou `"até 40% do tempo"` sem protocolo (`TX-09`), `"validação instantânea"` (`TX-03`) e `< 1.000w` (`CS-11`). |
| **C-Figma `STAR v1`** | Figma `480:9183` · `486:14029` | `3,90` | Atribuía indevidamente `"34M de clientes"` (dado da Neoenergia) à Claro (`TX-09`). |
| **C-Plugin (antigo)** | `build_portfolio_figma_screens.py` (pré-V4.2) | `3,55` | **Alucinação grave (`TX-09`/`IA-02`):** invertia `20 entrevistas / 10 perfis`, falava em `70+ testes`, `5G` (em 2017–2018!) e inventava carrinho e-commerce B2C com retirada de chip no balcão. |
| **C-V4.1.0** | Git `a9ef404` | `8,43` | Removeu `"40%"` e `"instantânea"`, mas Decisões 2 e 3 ficaram incompletas (`CS-06`/`TX-05`), faltava NDA (`CS-15`), `Escopo/Reflexão` estavam dentro de `#multicanal` (`A-16`) e `handoff`/`celular` variavam (`TX-08`). |
| **C-V4.2.0 🏆** | **Produção atual + Figma `737:846` + Plugin** | **`9,55`** | **0 falhas congeladas.** `CS-01` 4 frases + `metaDescription`, 3 decisões completas `CS-06`, Cap. 5 `Entrega, Escopo e Reflexão` (`A-16`) com efeito no time (`CS-12`) + nota de NDA (`CS-15`), `~1.400w` (`7 min`), Figma e plugin 100% saneados. |

### 2.4. Case 04 · Neoenergia (`Service Design · P&D ANEEL`) — 11 Versões

| ID | Origem / Artefato | Score `/10` | Principais Falhas / Achados |
| :--- | :--- | :---: | :--- |
| **N-V0 Dossiê** | `docs/v1/.../RELATORIO-SINTESE-DESCOBERTAS-NEOENERGIA` | `5,47` | Rica fonte primária (3 notas de OS, 3 perfis, slides 63–64), mas tom hiperbólico (*"brutais"*, *"hercúlea"*) e inversão `km/km²` na L37. |
| **N-V1–V2.1** | Git `9399562` ➔ `166eb4c` | `4,70–5,70` | Disclaimers defensivos, `;` indevidos, `"transformação"`/`"inovação"`, renomeou `5. Abandono` ➔ `Encerramento` e inseriu `"em tempo real"`. |
| **N-V3.5–V3.10** | Git `dfa8b19` ➔ `3eb51d2` · Figma `737:914` | `6,10–6,64` | 6 caps sob medida (`7c6dde2`) e desacordo multi-tenant (`7b08fdb`), mas manteve overclaim de código/WCAG e misturou `pessoas`/`habitantes` e `ideias`/`oportunidades`. |
| **N-Plugin (antigo)** | `build_portfolio_figma_screens.py` (pré-V4.2) | `4,70` | Estagnado em 7 caps sem decisões/trade-offs/reflexão, com `"plano diretor de inovação"` (`TX-04`), `"infraestrutura crítica"` (`TX-03`) e `"eliminamos barreiras"` (`TX-09`). |
| **N-V4.1.0** | Git `a9ef404` | `8,19` | Restaurou `5. Abandono`, papel e 3 decisões, mas a **inspeção visual da Fig. 5** revelou desalinhamento factual (`A-01`/`TX-09`), além de `co-construí` (`TH-08`), `/edit` nos Slides (`TH-07`), `Quick Wins` (`TX-04`) e frases de 44w (`TX-07`). |
| **N-V4.2.0 🏆** | **Produção atual + Figma `737:914` + Plugin** | **`9,41`** | **0 falhas congeladas.** `alt`/legenda da Fig. 5 100% fiéis ao slide EY `Relação de Entregáveis (Etapas 4–6)`, 3 decisões completas `CS-06` com evidência real (3 notas de OS), `TH-07` (`/preview`), `TH-08` (papel limpo), `TX-08` (`34M de habitantes` em todo o site), Figma e plugin sincronizados. |

---

## 3. Higiene Técnica, Acessibilidade & Sincronização Omnicanal (`V4.2.0`)

- **Rotas Estáticas SPA (`site/scripts/generate_spa_routes.js`):** agora injeta `<title>`, `<meta name="description">`, `og:title`, `og:description`, `og:url`, `twitter:*` e `canonical` específicos em cada uma das **8 rotas estáticas** (`TH-04`/`TH-05` 100% estático + dinâmico).
- **Acessibilidade (`CasePresentation.tsx`):** botões `Ver ampliado` agora recebem `aria-label="Ver ampliado: ${image.alt}"` único por figura (`A-15`/`A-28`).
- **Saneamento de Metadados Públicos (`site/public/llms.txt`, `ai-catalog.json`, `.well-known/ai-catalog.json`):** removido e-mail em texto aberto de `llms.txt`, substituída URL obsoleta `draw-lapis-96488079.figma.site` pela URL real de produção (`https://israelfull-commits.github.io/portfolio/llms.txt`) e alinhados os 4 cases + 5 módulos Itaú.
- **Validação & Paridade:** `npm --prefix site run build` (`0` erros, 8 rotas + `404.html`), **`15/15 PASS`** no `portfolio_qa_sentinel.py --sync`, espelho `portfolio-verde/` sincronizado, `build_portfolio_figma_screens.py` recompilado (`figma-refine-plugin` + `gemini-figma-plugin`), e 49 nós + Proveniência `V4.2.0` atualizados e verificados por screenshot no Figma `731:699`.

---

## 4. Pendências Factuais para Confirmação de Israel (`TX-09` — Sem Estimação)

Todas as lacunas abaixo foram tratadas de forma conservadora e transparente na `V4.2.0` (sem inventar dados):
1. **Einstein (`CS-08` / `CS-14`):** qual o denominador `n` exato dos testes `EN-7/EN-14` (`81,6% / 77,8% / 58,8% / 56,2%`)? A proposta v3 entrou em produção após a entrega da consultoria em 2022?
2. **Itaú IFA (`CS-12` / `CS-14` / `CS-15` / `IA-01`):** em qual módulo deseja registrar um episódio nominal de desacordo construtivo + quem aprovou? Qual o status real de produção de cada um dos 5 módulos? Os 8 links diretos de Figma no Apêndice do Itaú e os 6 links de Drive/Slides/Figma na Neoenergia devem permanecer ou virar nota institucional sob NDA (como no Einstein)? Em `Home.tsx`, manter `"4 módulos operacionais"` ou atualizar para `"5 módulos operacionais"`?
3. **Claro & Neoenergia (`TX-09` / `CS-14`):** confirmar se os episódios de desacordo (tela única × etapas progressivas na Claro; 4 portais × multi-tenant na Neoenergia) refletem 100% o ocorrido, e se a especificação V.2 da Claro chegou a produção após sua saída.
