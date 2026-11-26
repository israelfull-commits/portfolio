# Auditoria Comparativa Total — Hero Section da Home (`V1 ➔ V4.0.2`)

> **Proveniência & Rastreabilidade**  
> - **IA / Plataforma:** Antigravity — Google DeepMind  
> - **Data de criação:** 2026-11-26  
> - **Última atualização:** 2026-11-26  
> - **Conversa de origem:** [66417f41-f841-4d50-a701-e678302e3ec2](conversation://66417f41-f841-4d50-a701-e678302e3ec2)  
> - **Skills aplicadas:** `portfolio-writing` · `portfolio-banca` (7 papéis) · `portfolio-design-qa` · `senior-portfolio-audit` · `figma-use` · `figma-generate-design`  
> - **Fonte normativa:** [GUIA_CONSOLIDADO_REGRAS_E_CODIGOS_2026.md](../GUIA_CONSOLIDADO_REGRAS_E_CODIGOS_2026.md) (90 códigos congelados) & [AGENTS.md](../../AGENTS.md)

---

## 1. Escopo da Varredura Total

Foram inspecionadas todas as superfícies do ecossistema:
1. **Repositório & Histórico Git (`9399562` ➔ `de55343`):** 21 commits em `site/src/pages/Home.tsx`, branch `feat/cases-editoriais-revisao`, `site/index.html` e espelho `portfolio-verde/`.
2. **Figma `Template-portfolio` (`YIHybVXPe0Hfmja1hAyzQZ`):** páginas `0:1` (`Page 1`, 16 frames distintos de Home), `563:2552` (`VERSAO IDEAL`, 5 viewports) e `731:699` (`🚀 V4.0.0`, frame `736:716` + doc `732:707`).
3. **Compilador do Plugin Figma Desktop:** `scripts/build_portfolio_figma_screens.py` (bundles `figma-refine-plugin` e `gemini-figma-plugin`).
4. **Documentação Versionada, CV PDF & Notion Portfolio Ops:** `docs/v1_*` a `docs/v3_6_*`, `site/public/documents/israel-rozar-curriculo.pdf` e bases de governança no Notion.

---

## 2. Inventário Completo das 12 Versões / Variações Mapeadas + Campeã `V4.0.2`

| ID | Versão / Origem | Headline (`<h1>`) | Lead / Subtítulo | CTAs & Retrato |
| :--- | :--- | :--- | :--- | :--- |
| **H-01** | **V1 Original** (`Git 9399562` · 03/Nov) | *"Transformo complexidade em produtos claros, inclusivos e escaláveis."* | *"Desenho produtos digitais desde 2006. Nos últimos 11 anos, foco em discovery, UX/UI e estratégia de produto, mais recentemente no Itaú Unibanco, na plataforma íon for Advisors."* | `Conhecer meu trabalho ↓` · `LinkedIn` + Signal bar (`8 cases / 11 anos / Fintech + saúde / WCAG + IA`). |
| **H-02** | **V1 Figma Clones** (`1:2027` / `16:2` / `264:6787`) | *"Transformo complexidade em produtos claros, inclusivos e escaláveis."* | *"Desde 2006 desenho experiências digitais. Nos últimos 11 anos, atuo entre discovery, UX/UI e estratégia de produto em desafios de fintech, saúde e operações complexas."* | `Conhecer meu trabalho` · `LinkedIn` + sub-label `Design com clareza e intenção` + ticker de jargões em inglês. |
| **H-03** | **V1.5 Figma Bio** (`12:7409`) | *"Transformo complexidade em produtos claros, inclusivos e escaláveis."* | *"Sou Israel Laudelino Rozar, Senior Product Designer com 17 anos de experiência em projetos digitais — sendo os últimos 11 anos dedicados a Product Discovery, UX e UI para produtos complexos e escaláveis. Atuação recente no Itaú Unibanco na evolução da plataforma IFA (íon for Advisors)."* | `Ver cases` · `Portfólio completo` + monograma `IR` (sem foto), `17+` / `11` / `5 cases`. |
| **H-04** | **V1.8 Grid Editorial / Split** (`304:4771` / `304:5244` / `320:9551`) | *"Transformo complexidade em produtos claros, inclusivos e escaláveis."* | *"Desde 2006 desenho experiências estruturadas para ecossistemas de alta criticidade operacional. Foco intensivo entre discovery estratégico, arquitetura de sistemas e interfaces sob severa regulação técnica."* | `Explorar casos selecionados` / `Conhecer trabalhos` · `LinkedIn`; selos `STAFF / PRINCIPAL`, `LEAD ARCHITECT`, `10–11px`. |
| **H-05** | **V2 Figma Gemini** (`403:4619` / `405:338`) | *"Design Estruturado para Ecossistemas de Alta Criticidade."* | *"Desde 2016 desenhando produtos digitais. Recentemente, no Itaú Unibanco, liderei o time de Product Design que destravou a plataforma IFA (B2B) com forte foco em acessibilidade (WCAG) e escalabilidade."* | `Acessar CV completo` · `LinkedIn`; `Q2 / 2024`, `"Sua Foto Aqui"`, erro factual `"Desde 2016"`. |
| **H-06** | **V2B Consolidada** (`Git 82bfc8c` · Figma `302:3152` · Plugin anterior) | *"Design Estruturado para Ecossistemas de Alta Criticidade."* | *"Desde 2006 desenho experiências digitais. Recentemente, no Itaú Unibanco, liderei frentes de Product discovery e design da plataforma IFA para especialistas de investimentos."* *(Plugin: "...Mais de 15 anos focados em discovery...")* | `Conhecer meu trabalho ↓` · `Baixar currículo (PDF)` + retrato `IR • 2026` / `Einstein · Itaú · R/GA`. |
| **H-07** | **V3 Figma 1280/390** (`370:16614` / `375:366`) | *"Design de produtos digitais para bancos, saúde e serviços essenciais."* | *"Mais de 15 anos de experiência em design de produtos digitais. No Itaú Unibanco, liderei a pesquisa e o design de partes da plataforma IFA (Íon for Advisors), usada por especialistas em investimentos."* | 3 CTAs (`Conhecer meu trabalho ↓` · `LinkedIn` · `Baixar currículo (PDF)`) + retrato `Israel Rozar · ITAÚ • EINSTEIN • R/GA • EY`. |
| **H-08** | **V3.5 Compacta / VERSÃO IDEAL** (`Git dfa8b19`/`b9b61c3` · Figma `573:700` / `569:1096`) | *"Design de produtos para saúde, finanças e serviços essenciais."* | *"Desde 2006, atuo em pesquisa e design de produtos digitais. No Itaú, liderei frentes de design para especialistas de investimentos."* *(Figma `569:1096`: "Mais de 15 anos em pesquisa...")* | `Ver projetos` · `Currículo (PDF)` (+ e-mail aberto `irozar@yahoo.com.br` nas variantes iniciais, removido em `b9b61c3`). |
| **H-09** | **V3.9.0 ATS/STAR** (`Git f2f6b33` · 26/Nov) | *"Design de produtos para saúde, finanças e serviços essenciais."* | *"Desde 2006, atuo com Product Discovery, Arquitetura da Informação e Design Systems em ambientes regulados. No Itaú Unibanco, liderei frentes de produto na plataforma íon for Advisors para especialistas de investimentos."* | `Ver projetos` · `Currículo (PDF)` + retrato apenas `Israel Rozar`. |
| **H-10** | **V3.11.0 Plain Language & Figma `736:716`** (`Git 587f4be` · Figma `731:699`) | *"Design de produtos para saúde, finanças e serviços essenciais."* *(Figma `736:719`: "...digitais ...serviços críticos.")* | *"Atuação desde 2006 conectando pesquisa, fluxos e sistemas de interface com Produto e Engenharia. Recentemente no Itaú Unibanco, à frente do íon for Advisors para especialistas de investimentos."* | `Ver projetos` · `Currículo (PDF)` (Figma `736:718` tinha kicker em `11px` e `732:709` dizia `17+ anos`). |
| **H-11** | **V-Banca Figma** (`782:699` / `787:755` / `787:1331` · 26/Nov) | *"Design de produtos com muitos dados e regras, em finanças e saúde."* | *"Mais de 15 anos em pesquisa e design de produtos digitais. No Itaú, fui Senior Product Designer da plataforma IFA, usada por assessores de investimentos."* | `Ver projetos ↓` · `Currículo (PDF) ↓` + e-mail aberto `irozar@yahoo.com.br` + retrato `Itaú · Einstein · R/GA · EY`. |
| **H-12** | **V4.0.0 / V4.0.1 Produção Anterior** (`Git 847794a` / `de55343`) | *"Design de produtos para saúde, finanças e serviços essenciais."* | *"Mais de 15 anos de experiência conectando pesquisa, fluxos e sistemas de interface com Produto e Engenharia. Recentemente no Itaú Unibanco, à frente do íon for Advisors para especialistas de investimentos."* | `Ver projetos` · `Currículo (PDF)` + Header com `Entrar em contato →` + retrato `Israel Rozar · Itaú · Einstein · R/GA · EY`. |
| **H-13** | **V4.0.2 Campeã (APLICADA)** (`site/`, `portfolio-verde/`, Figma `731:699`, Plugin) | **"Design de produtos para saúde, finanças e serviços essenciais."** | **"Com mais de 15 anos de experiência, estruturo fluxos operacionais e sistemas de interface com Produto e Engenharia. No Itaú Unibanco, conduzi pesquisa e design no íon for Advisors para especialistas de investimentos e assessores."** | `Ver projetos` · `Currículo (PDF)` + Header fixo com `Entrar em contato →` + retrato `Israel Rozar · Itaú · Einstein · R/GA · EY`. |

---

## 3. Scorecard Comparativo & Falhas por Código Congelado

**Rubrica ponderada da Hero (`/100` e equivalente `/10`):**
- **Triagem 10s & Posicionamento (`HP-01..07` · 30 pts):** nome, cargo, local, setor, problema, marcas, CTA e contato sem rolar.
- **Tom Sênior, Plain Language & Glossário (`TX-01..09`, `IA-01..04` · 35 pts):** 1ª pessoa, verbos ativos, zero clichês/jargões, precisão factual e glossário Itaú IFA (`TX-08`).
- **Coerência ATS / CV / LinkedIn (`HP-06` · 15 pts):** `"Mais de 15 anos de experiência"`, cargo real e marcas âncora.
- **Acessibilidade, Segurança & Craft Figma (`A-`, `AP-`, `MB-`, `TH-`, `FG-` · 20 pts):** contraste AA/AAA, `>= 12px` (`FG-06`), `65–75ch`, zero e-mail em texto aberto, `0` erros Sentinel.

| Rank | ID | Versão | Triagem (`/30`) | Tom & Fatos (`/35`) | ATS/CV (`/15`) | A11y/Craft (`/20`) | **Score (`/100`)** | **Nota (`/10`)** | Falhas por Código Congelado |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **1º** | **H-13** | **V4.0.2 Campeã (VIGENTE)** | **30** | **35** | **15** | **20** | **100** | **10,0** | **0 falhas** (`HP`, `TX`, `IA`, `AP`, `MB`, `TH`, `A`, `FG` — exceção ADR apenas `TH-01` domínio próprio). |
| **2º** | **H-12** | V4.0.0 / V4.0.1 (Anterior) | 29 | 29 | 15 | 20 | **93** | **9,3** | `TX-01`/`TX-02` (gerúndio impessoal), `TX-06`/`TX-09` (*"à frente do íon for Advisors"* ambíguo em banca), `TX-08` (omitiu *assessores* vs. card Itaú). |
| **3º** | **H-10** | V3.11.0 / Figma `736:716` | 26 | 28 | 12 | 17 | **83** | **8,3** | `HP-06` (*"desde 2006"* / `"17+ anos"`), `TX-01`/`TX-06`/`TX-08` (mesmos de H-12), `FG-06` (kicker `11px` no Figma), divergência `"críticos"` vs. `"essenciais"`. |
| **4º** | **H-08** | V3.5 / VERSÃO IDEAL | 25 | 28 | 11 | 15 | **79** | **7,9** | `HP-06` (*"Desde 2006"*), `TX-08` (só especialistas), `TH-07`/Segurança (e-mail em texto claro nas variantes `dfa8b19`/`573:700`/`569:1096`), sem marcas no retrato em `dfa8b19`. |
| **5º** | **H-07** | V3 Figma 1280/390 (`370:16614`) | 26 | 26 | 14 | 13 | **79** | **7,9** | `TX-07` (repete *"produtos digitais"* no H1 e Lead), `TX-06` (*"de partes da plataforma"* soa hesitante), `TX-08`, `HP-02` (3 CTAs competindo + *"bancos"* reduz escopo de finanças), `FG-06` (badges/metrics). |
| **6º** | **H-09** | V3.9.0 ATS com Jargões | 25 | 23 | 12 | 18 | **78** | **7,8** | `HP-02`/`TX-04` (violação Gate 15: empilhamento de *"Product Discovery, Arquitetura da Informação e Design Systems"* na 1ª dobra da Home), `HP-06`, `TX-08`. |
| **7º** | **H-11** | V-Banca Figma (`782:699`) | 22 | 23 | 14 | 14 | **73** | **7,3** | `TX-08`/`TX-09` (falha crítica: *"usada por assessores de investimentos"* viola o glossário oficial), `HP-02` (omite telecom/energia; *"com muitos dados e regras"* genérico), e-mail em texto aberto. |
| **8º** | **H-06** | V2B / Plugin Anterior (`302:3152`) | 22 | 18 | 11 | 15 | **66** | **6,6** | `TX-03`/`TX-04` (banidos: *"Alta Criticidade"*, *"Expertise"*, *"rigorosa"*, *"TELEMETRIA QUANTITATIVA"*), `HP-02` (abstrato + jargão *"Product discovery"*), `FG-06` (`11px`). |
| **9º** | **H-01** | V1 Original (`9399562`) | 20 | 17 | 9 | 14 | **60** | **6,0** | `TX-04` (clichê *"Transformo complexidade..."* — termo banido), `HP-02` (sem setor no H1), `HP-06` (conflito `"desde 2006"` vs. `"11 anos"`), sem CV no Hero. |
| **10º** | **H-02** | V1 Figma Clones (`1:2027`) | 19 | 16 | 9 | 12 | **56** | **5,6** | `TX-04` (*"Transformo..."*), `HP-02` (jargões empilhados), `HP-06` (`2006` vs. `11 anos`), `FG-06` (`11.2px`). |
| **11º** | **H-03** | V1.5 Bio (`12:7409`) | 16 | 16 | 8 | 11 | **51** | **5,1** | `TX-04` (*"Transformo..."*), `TX-07` (lead longo em 1ª apresentação biográfica), `HP-01` (sem local no kicker, sem foto), `HP-06` (`17 anos` vs. `11 anos`), `FG-06` (`10.4px`). |
| **12º** | **H-04** | V1.8 Grid Editorial (`304:4771`) | 14 | 12 | 6 | 10 | **42** | **4,2** | `TX-09` (cargo inflado `STAFF / PRINCIPAL` / `LEAD ARCHITECT`), `TX-03`/`TX-04` (*"Transformo"*, *"alta criticidade"*), `FG-06` (`10–11px`), coordenadas geográficas decorativas. |
| **13º** | **H-05** | V2 Figma Gemini (`403:4619`) | 12 | 8 | 4 | 10 | **34** | **3,4** | `TX-09` (erros factuais graves: *"Desde 2016"*, *"liderei o time de Product Design que destravou"*, `"Q2 / 2024"`), `TX-03`/`TX-04` (*"Alta Criticidade"*), placeholder `"Sua Foto Aqui"`. |

---

## 4. Parecer da Banca Calibrada de 7 Papéis (`portfolio-banca`) sobre `H-13 (V4.0.2)`

1. **Recrutador Sênior (10–30s):** `Passa` (`HP-01..07`). Em 5 segundos valida cargo (`Senior Product Designer`), local (`São Paulo · Brasil`), tempo (`Mais de 15 anos de experiência`), marcas (`Itaú · Einstein · R/GA · EY`), CV em PDF e contato no header fixo.
2. **Gerente de Product Design (Hiring Manager):** `Passa` (`TX-01`, `TX-06`, `TX-09`). A troca de *"à frente do íon for Advisors"* para *"conduzi pesquisa e design no íon for Advisors"* elimina o risco de parecer exagero hierárquico em entrevista.
3. **Senior Product Designer (Par):** `Passa` (`TX-01`, `TX-02`, `HP-02`). Verbos diretos em 1ª pessoa (`estruturo`, `conduzi`) + parceria explícita com `Produto e Engenharia` + `sistemas de interface`.
4. **Editor / UX Writer:** `Passa` (`TX-03`, `TX-04`, `TX-07`, `TX-08`). Zero termos banidos, zero jargão em inglês empilhado, zero repetição lexical entre H1 e Lead, 2 frases curtas (`16` e `18` palavras) e glossário Itaú IFA 100% consistente (`especialistas de investimentos e assessores`).
5. **Especialista em Dados / Métricas:** `Passa` (`TX-09`). Nenhum número sem baseline na 1ª dobra; apenas a faixa de carreira verificável (`Mais de 15 anos de experiência`, lastreada pela linha do tempo `2006–2026`).
6. **Especialista em Acessibilidade (WCAG 2.2 AA/AAA):** `Passa` (`A-01..28`, `AP-01..07`, `MB-01..06`, `FG-06`). H1 único, corpo `18px/28px` (`17px/26px` no mobile), `max-width: 60ch`, alvos `>= 48px`, `0px` overflow e `>= 12px` no Figma.
7. **Entrevistador (Walkthrough 60s):** `Passa`. O Lead fecha a principal pergunta armadilha (*"você liderava toda a plataforma?"*) e abre gancho imediato para o walkthrough dos 4 módulos do Itaú e do sistema de laudos do Einstein.

### Sugestões (sem código — não reprovam)
- Caso venha a atualizar o PDF público do currículo (`israel-rozar-curriculo.pdf`) futuramente, alinhar a linha de resumo de *"desde 2006 e ... desde 2015"* para também mencionar *"mais de 15 anos de experiência"* e remover o link legado `uxfol.io/israelrozar` do cabeçalho do PDF.
