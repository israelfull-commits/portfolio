# Diagnóstico Comparativo Profundo: Versões de Texto do Portfólio

**Escopo da Varredura:** Histórico completo do Git (`9399562` → `4973062` + working tree), conversas anteriores ([ec9956e5-078d-4d87-9a8e-74481434c7dc](conversation://ec9956e5-078d-4d87-9a8e-74481434c7dc), `1f76c5ad`, `0c9440d3`), documentação versionada (`docs/v1`, `docs/v2`, `docs/v3`, `SENIOR_UX_PORTFOLIO_CANON.md`), frames do Figma (`YIHybVXPe0Hfmja1hAyzQZ` nós `412:6100`, `370:17047`, `59:2`) e script gerador (`scripts/build_portfolio_figma_screens.py`).  
**Comitê de Avaliação:** Design Director / Staff Product Designer · Recrutador Executivo (Triagem 30–90s) · Lead Content Strategist (Plain Language & STAR) · Auditor de Evidências & Risco em Entrevista.

---

## 1. Mapa das 5 Versões de Texto Encontradas no Ecossistema

| Versão | Origem / Onde Existe | Estilo Editorial | Veredito Geral |
| :--- | :--- | :--- | :--- |
| **V1 — Epistêmica / Defensiva** | Git `9399562` (03/Nov), Figma `59:2`, Figma `412:6100` | Longa (~702 linhas na Home), repleta de disclaimers (*"não comprova"*, *"pendente"*, *"amostras não se somam"*). | **Rejeitada.** Comunica lacunas em vez de senioridade; cansa na triagem. |
| **V2A — Technobabble** | Git `c3479c3` / `ba58351` (14/Nov) | Jargão acadêmico/técnico pesado (*"ancoragem determinística"*, *"desacoplamento de metadados"*, *"tolerância dimensional"*). | **Rejeitada.** Afasta PMs, recrutadores e lideranças de negócio. |
| **V2B — Executiva Estruturada** | Git `01faf96` → `166eb4c` (14–15/Nov) | Home rica (386 linhas) com `Decisão:`, `Expertise` e `Trajetória`; cases em português claro com `.cp-split`. Continha algumas alegações causais não medidas (*"ansiedade"*, *"TMA"*). | **Forte na Home, mas precisava de poda factual nos cases.** |
| **V-Figma — STAR Assertivo** | `scripts/build_portfolio_figma_screens.py` (15–25/Nov) | Único com blocos explícitos de *O Que NÃO Foi Construído*, *Desacordo Construtivo* e *O Que Faria Diferente*. **Porém mistura números não comprovados/template** (*"R$ 42B+"*, *"45 min → 3 min"*, *"4 macroáreas"* vs. 3 reais). | **Alto risco em entrevista.** Usar **apenas a estrutura**, nunca os números sem lastro. |
| **V3 — Atual em Produção** | `HEAD 4973062` + `Home.tsx` local (25/Nov) | Cases 100% factuais, sem disclaimers, sem links confidenciais/redundantes. Home ultracompacta (`pf-home-compact`, 111 linhas). | **Melhor base factual nos cases; Home enxugada ligeiramente além do ideal.** |

---

## 2. Análise Comparativa Seção por Seção (Prós, Contras e Recomendação)

### 2.1. Página Inicial (`Home.tsx`)

#### A. Hero (Headline + Lead + CTAs)
* **V1 (`9399562`):** *"Transformo complexidade em produtos claros, inclusivos e escaláveis."*
  * *Contra:* Clichê genérico presente em milhares de portfólios de UX; não diz em quais domínios você atua.
* **V2B (`01faf96` / Figma Plugin):** *"Design Estruturado para Ecossistemas de Alta Criticidade."*
  * *Pró:* Soa sênior e técnico.
  * *Contra:* Abstrato demais (*"ecossistemas de alta criticidade"* exige tradução mental do recrutador).
* **V3 Atual (`Home.tsx`):** *"Design de produtos para saúde, finanças e serviços essenciais."* + Lead: *"Desde 2006, atuo em pesquisa e design de produtos digitais. No Itaú, liderei frentes de design para especialistas de investimentos."*
  * *Prós:* Concreto, humano, sem clichê, comunica senioridade (2006), marca âncora (Itaú) e domínios regulados nos primeiros 5 segundos.
  * **🏆 Versão Recomendada:** **V3 Atual (100% vencedora).**

#### B. Vitrine de Projetos (`#trabalho`)
* **V1:** 3 blocos gigantes + 5 cards Itaú separados + disclaimers de metodologia. *(Muito longa: ~9.200 px).*
* **V2B (`01faf96`):** Einstein em destaque (`14 Famílias`, `121 Pacientes`) + Grid de 3 cards com **linha de `Decisão:`** em cada um + barra compacta de submódulos Itaú (`Vencimentos`, `Movimentações`, `Campanhas`).
* **V3 Atual (`Home.tsx`):** Einstein em destaque + 3 cards curtos com apenas cliente, título, cargo e 1 frase descritiva. Removeu a linha de `Decisão:` e removeu o atalho para `Vencimentos`, `Movimentações` e `Campanhas`.
  * *Prós da V3:* Extremamente limpa e escaneável.
  * *Contras da V3:* Esconde o escopo concreto (ex.: *"4 distribuidoras, 5 blueprints"* na Neoenergia) e torna os outros 3 cases do Itaú invisíveis na Home (o recrutador só descobre se entrar no Hub de Liquidez e rolar até o fim).
  * **🏆 Versão Recomendada:** **Híbrida (Base V3 + 2 resgates cirúrgicos da V2B):** manter a limpeza da V3, mas devolver **1 linha factual de escopo/decisão** nos cards e uma **linha discreta de links para os demais recortes Itaú** (`Vencimentos · Movimentações · Campanhas`).

#### C. Sobre, Especialidades e Trajetória (`#sobre` / `#trajetoria`)
* **Figma `412:6100` & V2B:** Trazem `02 Especialidades` (4 cards) e `03 Trajetória` (5 linhas cronológicas: Consultoria, Itaú 2024–2026, Foursys + Einstein 2022, EY · R/GA 2020–2022, 2006–2019 + Ciência da Computação).
* **V3 Atual (`Home.tsx`):** Substituiu tudo por 2 parágrafos curtos (*"A trajetória completa e a formação estão no currículo"*) + link para baixar o PDF.
  * *Pró da V3:* Home curtíssima (~1.800 px), foco total nos cases.
  * *Contra da V3:* Recrutadores em triagem rápida (30–60s) frequentemente **não baixam PDFs** antes de decidir se avançam o candidato. Ocultar **Itaú, Einstein, EY, R/GA e Ciência da Computação** da tela reduz a prova social imediata e prejudica leitura por ATS/buscadores.
  * **🏆 Versão Recomendada:** **Manter o bloco "Sobre minha atuação" enxuto da V3 + reincorporar uma lista compacta de 5 linhas da Trajetória (estilo V2B)**, sem inflar a página com cards gigantes.

---

### 2.2. Case 1 — Albert Einstein (`einstein-laudos`)

| Elemento | V1 / Figma `59:2` | V2B (`c04be68` / `779f5c6`) | V-Figma Plugin | V3 Atual (`CasePages.tsx`) |
| :--- | :--- | :--- | :--- | :--- |
| **Headline** | *"Clareza não é o mesmo que compreensão."* | *"Uma linguagem visual modular para laudos heterogêneos."* | *"Uma linguagem visual modular para laudos clínicos heterogêneos."* | *"Uma linguagem visual modular para laudos heterogêneos."* |
| **Macroáreas** | Não detalhadas | 3 macroáreas (Metodologia, Resultado, Conclusão) | **4 macroáreas** *(inconsistente)* | 3 macroáreas (Metodologia, Resultado, Conclusão) |
| **Métricas** | `4 médicos`, `Questionário`, `14` + disclaimer | `81,6%` interpretado como *"sem esforço"* | *"78% pulavam texto"*, *"6 componentes"* *(sem lastro)* | `81,6%`, `77,8%`, `58,8%`, `56,2%` estritamente factuais + `14 entregáveis documentados` |
| **Confidencialidade** | Links Notion/Figma expostos | Links Notion/Figma expostos | Sem links | **Links removidos + nota de NDA hospitalar** |

* **Prós da V3 Atual:** É a versão mais rigorosa, defensável em arguição técnica e juridicamente segura (NDA + LGPD). Eliminou a inferência de *"ansiedade do paciente"* (V2) e o technobabble (V2A).
* **Ponto de Melhoria (Gap vs. Cânone Sênior):** A headline da V1 (*"Clareza não é o mesmo que compreensão."*) tinha forte poder memorável como tese (hoje preservada no Capítulo 6), enquanto a V3 é mais descritiva. Além disso, o case ganharia muito peso de liderança sênior com um **micro-bloco factual de "Escopo descartado e trade-offs"** (ex.: por que não recriar um portal novo do zero e priorizar compatibilidade com impressão P&B e sistemas legados) e **"O que eu faria diferente hoje"**.
* **🏆 Versão Recomendada:** **V3 Atual (mantida como base) + adição de 1 bloco conciso de Trade-offs & Reflexão Crítica.**

---

### 2.3. Case 2 — Claro (`claro-ativacao-simplificada`)

* **V1:** Cheia de ressalvas (*"não representa resultados causais"*, *"exigiria comparar conclusões"*).
* **V2B (`fd8d0e8`):** Layout `.cp-split` excelente, mas afirmava *"reduzindo o tempo médio de atendimento (TMA)"* sem baseline medido e mantinha link externo do UXfolio.
* **V-Figma Plugin:** Introduziu números sem lastro documental (*"15 telas → 3 etapas"*, *"40% de quedas"*, *"34M clientes"*).
* **V3 Atual (`CasePages.tsx`):** Removeu a alegação de TMA sem baseline, removeu o link do UXfolio, manteve as 22 jornadas, 20 pessoas em imersão, 10 em entrevista, 70+ em testes e enquadrou os dados sob LGPD.
* **🏆 Versão Recomendada:** **V3 Atual (100% superior em credibilidade).** *Refinamento opcional:* adicionar 2 frases factuais sobre o trade-off de manter visível o resumo financeiro sem sobrecarregar a tela mobile.

---

### 2.4. Case 3 — Neoenergia (`neoenergia-conexao-digital`)

* **V1:** Prosa corrida + apêndice defensivo listando tudo que o projeto *não* comprovava (*"Não são apresentados como comprovados ROI, WCAG..."*).
* **V2B (`166eb4c`) & V3 Atual (`CasePages.tsx`):** Idênticas na narrativa. Estrutura exemplar em `.cp-split`: 34M habitantes, 13,9M clientes, 4 distribuidoras, 11 canais, 5 Service Blueprints P&D ANEEL, Matriz de 118 ideias, Design System Multi-tenant.
* **🏆 Versão Recomendada:** **V3 Atual (já está no padrão ouro).** *Único ajuste recomendado:* garantir que a Home volte a citar os números-chave (*4 distribuidoras · 5 blueprints · 118 ideias*) para manter o gancho executivo antes do clique.

---

### 2.5. Case 4 — Itaú Unibanco (`itau/*`)

* **V1 (`9399562`):** Marcado como *"Case em preparação"*, *"Contribuição individual pendente"*, *"relato de escopo reduzido"*. Prejudicial em processo seletivo.
* **V-Figma Plugin:** Consolida os 5 recortes em uma página só, mas inventa métricas agressivas (*"R$ 42B+"*, *"60% menos tempo"*, *"45 min → 3 min"*). **Perigoso em sabatina com recrutadores ou gestores do setor financeiro.**
* **V3 Atual (`CasePages.tsx` + `ItauPreparationCase.tsx`):** Eliminou todos os disclaimers defensivos, enquadrou 100% sob **sigilo bancário e LGPD**, corrigiu a legenda duplicada em Campanhas e apresentou autoria afirmativa (*"Israel Rozar — Senior Product Designer"*).
* **Ponto de Atenção na V3:** Como o Itaú é dividido em 4–5 subpáginas (`hub-liquidez`, `vencimentos`, `movimentacoes`, `campanhas`, `registros-atendimento`), a Home atual só exibe `Hub de Liquidez`. Os outros módulos ficam ocultos na primeira dobra.
* **🏆 Versão Recomendada:** **V3 Atual nos textos internos + exposição discreta dos submódulos na Home.**

---

## 3. Veredito Final: Qual é a Versão Realmente Recomendada?

> [!IMPORTANT]
> **A versão atual em produção (V3) já é a MELHOR E MAIS SEGURA de todas as versões históricas nos textos internos dos 4 cases.** Ela superou os 3 grandes defeitos das versões anteriores: o tom defensivo (V1), o academicismo hermético (V2A) e o risco de métricas inventadas/não comprovadas (V-Figma Plugin).

Contudo, para atingir **100% de perfeição segundo o `SENIOR_UX_PORTFOLIO_CANON.md`**, a versão ideal recomendada é a **V3.5 (Híbrida Canônica)** — que preserva integralmente a honestidade factual da V3 e aplica **3 ajustes cirúrgicos de alto impacto**:

1. **Na Home (`site/src/pages/Home.tsx`):**
   * **Manter** o Hero da V3 (*"Design de produtos para saúde, finanças e serviços essenciais."*).
   * **Adicionar** 1 linha curta de *escopo/decisão factual* em cada card de projeto + atalho discreto para os demais recortes Itaú (`Vencimentos · Movimentações · Campanhas`).
   * **Reincorporar** uma lista compacta de **Trajetória (5 linhas)** acima do contato, para que recrutadores vejam imediatamente **Itaú · Einstein · EY · R/GA · Ciência da Computação** sem precisar baixar o PDF.
2. **Nos Cases (`site/src/pages/CasePages.tsx`):**
   * **Manter 100%** dos textos factuais, métricas verificadas e enquadramento LGPD/NDA da V3.
   * **Acrescentar** em cada case um micro-bloco sênior objetivo (*"Escopo deliberadamente fora do recorte & O que eu faria diferente hoje"*) baseado exclusivamente em fatos reais do projeto — fechando o último gap em relação ao Cânone Senior UX 2026.
3. **No Plugin Figma (`scripts/build_portfolio_figma_screens.py`):**
   * **Nunca usar** as métricas de template (*"R$ 42B+"*, *"45 min → 3 min"*, *"4 macroáreas"*) fora de rascunho; caso volte a gerar telas no Figma, sincronizar os textos do script com os textos factuais da V3.
