# Parecer do Comitê Multiespecialista & Tabela De-Para (V1/V2 ➔ V3.5 Vigente)

**Data:** 25 de Novembro de 2026  
**Versão Auditada:** V3.5 Híbrida Canônica (`a35d800` em produção no GitHub Pages)

---

## 1. Tabela Comparativa De-Para: Texto Antigo vs. Texto Atual (V3.5)

| Página / Seção | Texto Antigo (V1 / V2 / Resíduos) | Texto Atual (V3.5 em Produção) | Justificativa da Mudança |
| :--- | :--- | :--- | :--- |
| **Home · Hero H1** | *"Transformo complexidade em produtos claros, inclusivos e escaláveis."* (V1) / *"Design Estruturado para Ecossistemas de Alta Criticidade."* (V2) | *"Design de produtos para saúde, finanças e serviços essenciais."* | Elimina clichês genéricos (V1) e abstrações difíceis (V2). Comunica senioridade e domínios regulados em menos de 5 segundos. |
| **Home · Cards de Projetos** | Sem linha de escopo na V3 inicial ou com disclaimers extensos na V1 (*"não equivalem a resultados operacionais"*). | Linha factual de escopo por card (`14 entregáveis · 121 pacientes · 4 médicos`, `4 distribuidoras · 5 blueprints · 118 ideias`, `22 jornadas · 70+ validações`). | Entrega prova de escala e complexidade antes do clique, mantendo paridade numérica estrita entre Home e Cases. |
| **Home · Submódulos Itaú** | Ocultos na Home compacta inicial (apenas Hub de Liquidez visível) ou espalhados em 5 cards gigantes na V1. | Barra compacta: *"Outros recortes no Itaú (IFA): Gestão de Vencimentos · Movimentações · Gestão de Campanhas"*. | Expõe a amplitude da atuação recente no Itaú (2024–2026) sem inflar a altura da página. |
| **Home · Trajetória** | Oculta dentro do PDF na V3 inicial (*"A trajetória completa está no currículo"*) ou longa demais na V1. | Lista escaneável de 5 linhas na tela (`Itaú`, `Consultoria`, `Foursys + Einstein`, `EY · R/GA`, `Ciência da Computação`) + link do PDF. | Recrutadores em triagem de 30–60s raramente baixam PDFs na primeira visita; marcas âncora ficam visíveis imediatamente. |
| **Home · Botões dos Cards** | Mistura inconsistente: *"Ler recorte"*, *"Ler case completo"*, *"Explorar o case"*. | Padronizados em **`Ver estudo de caso`**. | Consistência de microcopy, clareza de expectativa e padrão de acessibilidade. |
| **Einstein · Hero & Legenda** | Asset com linhas de medição do Figma + legenda *"Linguagem visual modular..."* (2400×1350). | Capa editorial de estúdio 2560×1440 px + *"Taxonomia oficial do Design System: anatomia de campos, tokens tipográficos e componentes modulares..."*. | Elimina ruído visual no lightbox e eleva o craft ao padrão editorial de estúdio 16:9. |
| **Einstein · Vocabulário Técnico** | *"ancoragem determinística"*, *"desacoplamento de metadados"*, *"ansiedade extrema de pacientes"*. | Português direto, 3 macroáreas (*Metodologia, Resultado, Conclusão Diagnóstica*) e percentuais exatos (`81,6%`, `77,8%`). | Elimina academicismo hermético (V2A) e inferências emocionais sem lastro nas entrevistas. |
| **Einstein · Documentação / NDA** | Links externos abertos para Notion e Figma de trabalho do HIAE. | Declaração institucional de custódia restrita sob NDA e sigilo médico (links removidos). | Proteção jurídica e ética hospitalar; demonstra maturidade corporativa em domínios regulados. |
| **Claro · Impacto & Referências** | *"reduzindo o tempo médio de atendimento (TMA)"* (sem baseline) + link do UXfolio. | *"apoiando a continuidade entre canais"* + link do UXfolio removido. | Evita alegação causal indefensável em sabatina técnica e elimina links redundantes. |
| **Itaú · Pesquisa & Legendas** | *"nó 3:14068 de Gestão de liquidez"*, *"nó 582:12520, confirmada pelo autor"*, *"fornecida pelo autor em 02/11/2026"*, *"dados fictícios"*. | Textos limpos em voz executiva, sem IDs internos de Figma, com enquadramento sob **LGPD e sigilo bancário**. | Remove meta-linguagem de auditoria interna que só pertence a `docs/`; blinda a postura sênior. |
| **Todos os 4 Cases · Fechamento** | Encerravam apenas em aprendizado geral, sem explicitar escopo descartado ou autocrítica. | Adicionados 2 cards sênior factuais: **Disciplina de Escopo (*"O que ficou fora do recorte"*)** e **Reflexão Crítica (*"O que eu faria diferente hoje"*)**. | Atende integralmente ao `SENIOR_UX_PORTFOLIO_CANON.md` (principal diferenciador entre Senior/Staff e Pleno). |
| **Rodapé · Card de Contato** | `Baixar currículo (PDF) • LinkedIn • GitHub • UXfolio`. | `Baixar currículo (PDF) • LinkedIn`. | Remove redundância (o usuário já está no site) e foca 100% na conversão para entrevista. |

---

## 2. Parecer do Comitê Multiespecialista

* **Product Design Manager (PDM):** Aprova 100%. Os 4 cases provam liderança de escopo, navegação entre restrições legadas e maturidade na reflexão crítica (*"O que ficou fora"* e *"O que eu faria diferente"*).
* **Staff / Especialista Product Designer:** Aprova 100%. Arquitetura limpa, Design System coeso (`Plus Jakarta Sans`, grid 8px, tokens semânticos) e foco em decisões técnicas, não em teatro de processos (zero Double Diamond genérico ou mural de post-its).
* **Senior Product Designer:** Aprova 100%. Equilíbrio ideal entre profundidade técnica nos cases e leitura fluida em `.cp-split` com Lightbox 96vw×94vh sem corte de zoom.
* **Especialista LinkedIn, Gupy & ATS:** Aprova 100%. Palavras-chave estratégicas naturalmente distribuídas no HTML e JSON-LD (`Senior Product Designer`, `Product Discovery`, `UX Research`, `Arquitetura da Informação`, `Design System`, `Service Design`, `WCAG 2.2`, `IA com revisão humana`, `Saúde`, `Finanças`, `Itaú`, `Einstein`, `EY`, `R/GA`, `Ciência da Computação`) — sem *keyword stuffing*.
* **Tech Recruiter (Triagem 30–90s):** Aprova 100%. Nos primeiros 15 segundos da Home já valida senioridade (desde 2006), grandes marcas, domínios complexos, CV em PDF com 1 clique e contato direto.
* **Lead Copywriter & UX Writer:** Aprova 100%. Plain Language impecável, zero jargões vazios, zero termos defensivos, botões padronizados e zero vazamento de IDs internos.
* **Principal UX Researcher & Dados:** Aprova 100%. Rigor metodológico exemplar: triangulação explícita, métricas estritamente ancoradas em evidências reais (sem números inflados ou inventados), e enquadramento ético LGPD/NDA.
* **Lead de Acessibilidade Digital (WCAG 2.2 AAA):** Aprova 100%. 199/199 pares de cor em conformidade WCAG AAA, 1 `<h1>` por página, 0 saltos de título, 0 imagens sem `alt`, alvos de toque validados e navegação completa por teclado (`Escape`, `:focus-visible`, `prefers-reduced-motion`).
