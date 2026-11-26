# Scorecard Comparativo — Versões do Portfólio (`v0.1` ➔ `v3.6.0`) & Variações Visuais (`V01`–`V19`)

**Data:** 26 de Novembro de 2026  
**Rubricas aplicadas:**
1. **Scorecard Geral do Portfólio (`0–100`):** Rubrica ponderada do Notion Portfolio Ops (`C1–C8`, notas `0–5` × peso ÷ 5).
2. **Scorecard de Variações Visuais (`0–100`):** Rubrica de Craft & Evidência Senior ancorada no UX Companion 2026 e `AGENTS.md`:
   - **Legibilidade real da UI (`30%`):** nitidez 1:1 dos pixels do Figma, sem rotação ou blur que impeça ler dados.
   - **Prova narrativa (`25%`):** comunica decisão, sistema ou antes/depois em até 5 segundos.
   - **Coerência com a marca do portfólio (`20%`):** harmonia com `#FCF9F2` / `#0A3622` / `#C4F042` e tom executivo.
   - **Craft visual (`15%`):** iluminação, sombra multi-camada e respiro *Gestalt Outside-In*.
   - **Versatilidade responsiva (`10%`):** legibilidade preservada em desktop (`1440px`) e mobile (`390px`).

---

## Parte 1 — Evolução das Versões do Portfólio (`v0.1` ➔ `v3.6.0`)

| Versão | Ambiente | Score (`/100`) | Δ vs. Anterior | Faixa | Por que é melhor ou pior |
| :--- | :--- | :---: | :---: | :---: | :--- |
| **v0.1.0** | UXfolio (baseline) | **52** | — | Insuficiente | **Pior:** formato genérico de plataforma, pouca profundidade técnica, zero controle de acessibilidade/SEO e cases sem trade-offs documentados. |
| **v2.0.0** | Figma Make (`casual-saint`) | **67** | `+15` | Adequado | **Avanço visual, mas incompleto:** ganhou identidade própria e 1 case estruturado (Einstein), porém tinha 3 dossiês inacabados, Itaú sem autoria declarada, anos de experiência inconsistentes e mobile não validado. |
| **v3.0.0** | Figma Make (`dig-next`) | **73** | `+6` | Forte | **Mais completo, mas disperso:** trouxe autoria no Itaú e 8 recortes, porém pecava por excesso de cases (C3=3), 3 cases sem imagem (C5=3), métricas divergentes e limitações de hospedagem/acessibilidade do Figma Sites. |
| **v3.5.0** | GitHub Pages (Híbrida Canônica) | **87** | `+14` | Excelente | **Virada estrutural:** código React/Vite próprio, curadoria focada em 4 cases âncora, Home executiva com trajetória visível, remoção de IDs internos de Figma, zero linguagem defensiva e rotas estáticas SPA `200 OK`. |
| **v3.6.0** | **GitHub Pages (Craft Edition — VIGENTE)** | **95** | **`+8`** | **Excelente** | **Melhor versão até hoje:** deduplicação 100% de imagens nos 4 cases, proteção híbrida `CaseAccessGate` SHA-256 por padrão, diagramas 2× Retina WCAG AAA, autofix profundo de Design System (`0` inline styles), **12/12 PASS** no Sentinel v2 e **`28/30` (`34/35`)** no UX Companion 2026. |

### O que separa a `v3.6.0` (`95/100`) de uma `v3.7.0` (`98–100/100`)
- **C4 Senioridade (`4.5 → 5.0`):** tornar explícitos *Framing inicial*, *Desacordo construtivo por papel* e *Mentoria/Crítica* nos 4 cases.
- **C6 Acessibilidade (`4.8 → 5.0`):** adicionar gate automático de contraste em `:hover` e `:focus-visible` no Sentinel v2.
- **C8 Conversão (`4.5 → 5.0`):** domínio próprio customizado (fechando `35/35` no checklist UX Companion) + paridade 1:1 com CV/LinkedIn.

---

## Parte 2 — Score & Ranking das 19 Variações de Estúdio (`V01`–`V19`)

### 1. Case Hospital Albert Einstein

| Rank | ID | Estilo | Score (`/100`) | Papel Ideal | Por que é melhor ou pior |
| :---: | :---: | :--- | :---: | :--- | :--- |
| **1º** | **V17** | Clean Light Bento Grid (`AeroLoad`) | **95** | **Hero / Visão Geral** | **Melhor equilíbrio executivo:** 100% ortogonal (zero distorção de texto clínico), estética hospitalar limpa, alinha perfeitamente com o fundo `#FCF9F2` e destaca multicanal + componente Protrombina com clareza imediata. |
| **2º** | **V03** | Comparativo Antes vs. Depois | **93** | **Evidência de Impacto** | **Melhor prova narrativa:** em 3 segundos o recrutador enxerga a transformação do laudo legado para o sistema modular. Altíssima legibilidade em desktop e mobile. |
| **3º** | **V13** | Estúdio 3 Canais (A4 + MacBook + iPhone) | **91** | **Hero Editorial** | **Melhor prova omnicanal real:** mostra a folha A4 impressa real de mamografia lado a lado com Web e Mobile. Levemente mais denso no mobile (`390px`), por isso fica 4 pts atrás do V17 em versatilidade. |
| **4º** | **V02** | Bento Grid Modular (`LS.Graphics`) | **86** | **Resumo de Sistema** | **Bom, mas menos clínico:** mistura métricas + DS + telas com boa síntese, porém o bloco escuro compete um pouco com a sobriedade do domínio de saúde. |
| **5º** | **V01** | Editorial Diagonal em Camadas | **79** | **Apoio / Thumbnail** | **Pior para leitura clínica:** a rotação de `-14°` dá apelo de Dribbble, mas reduz a legibilidade imediata dos valores de referência do exame (penalizado em L1). |
| **6º** | **V19** | Studio Display Low-Angle Verde-Lima | **74** | **Capa de Social / Behance** | **Pior para o case técnico:** ângulo contra-plongée dramático + fundo verde-lima vibrante chamam atenção visual, mas distorcem a perspectiva da UI e fogem da sobriedade hospitalar. |

### 2. Case Itaú (íon for Advisors — IFA)

| Rank | ID | Estilo | Score (`/100`) | Papel Ideal | Por que é melhor ou pior |
| :---: | :---: | :--- | :---: | :--- | :--- |
| **1º** | **V16** | Light Fintech Bento Grid (`Elegostra` + `AeroLoad`) | **96** | **Hero Principal** | **Campeão geral do portfólio:** cara de produto financeiro institucional de alto nível, 100% ortogonal, legibilidade impecável de tabelas/filtros e integração natural com a paleta clara do site. |
| **2º** | **V14** | Editorial Bento Split (`Ref 10`) | **92** | **Abertura de Módulo** | **Excelente narrativa executiva:** combina título editorial à esquerda com recortes reais de Vencimentos/filtros à direita. Perde 4 pts só porque texto embutido na imagem reduz flexibilidade em telas pequenas. |
| **3º** | **V07** | Jornada em Moldura Studio | **90** | **Capítulo de Fluxo/IA** | **Ótima moldura de processo:** eleva o diagrama 2× Retina (*Antes vs. IFA + Human-in-the-Loop*) sem distorcer nenhum rótulo. |
| **4º** | **V04** | Dark Studio 3D Showcase | **84** | **Destaque Visual / Capa** | **Forte impacto visual**, mas a sobreposição 3D em perspectiva oculta parte do Hub de Liquidez atrás de Vencimentos — mais vitrine do que prova técnica. |
| **5º** | **V05** | Warm Minimalist Studio Desk (iPad) | **81** | **Apoio Fotográfico** | **Elegante**, porém o IFA é uma ferramenta desktop de alta densidade; mostrar apenas em iPad com sombra de folhagem reduz o realismo operacional. |
| **6º** | **V06** | Liquid Glass / Glassmorphism 2.0 | **76** | **Experimental** | **Tendência decorativa:** o vidro translúcido e os cards flutuantes competem com os dados financeiros reais e reduzem contraste em algumas bordas. |
| **7º** | **V18** | Macro Depth-of-Field (`Tilt-Shift f/1.4`) | **72** | **Teaser / Social** | **Pior para recrutador técnico:** o desfoque artístico (`f/1.4`) propositalmente borra parte da interface — ótimo para Dribbble, ruim para quem avalia arquitetura de informação. |

### 3. Case Claro (Ativação Simplificada)

| Rank | ID | Estilo | Score (`/100`) | Papel Ideal | Por que é melhor ou pior |
| :---: | :---: | :--- | :---: | :--- | :--- |
| **1º** | **V08** | Multicanal Desktop + iPhone | **94** | **Hero Principal** | **Melhor prova de paridade omnicanal:** mostra Desktop (loja/televendas) e Mobile juntos sem poluição, com ótima proporção e legibilidade dos campos reais. |
| **2º** | **V10** | Jornada Editorial Elevada | **91** | **Capítulo de Arquitetura** | **Clareza total de fluxo:** enquadra a Esteira Unificada de 5 etapas (22 jornadas) em palco claro limpo, 100% alinhado ao visual do portfólio. |
| **3º** | **V09** | Leque Escalonado de 3 Telas | **80** | **Apoio Visual** | **Pior que V08 para leitura:** o escalonamento em 3 planos sobrepõe bordas das telas laterais (CPF e Oferta), sacrificando área útil por efeito de profundidade. |

### 4. Case Neoenergia (Service Design P&D ANEEL)

| Rank | ID | Estilo | Score (`/100`) | Papel Ideal | Por que é melhor ou pior |
| :---: | :---: | :--- | :---: | :--- | :--- |
| **1º** | **V12** | Bento Executivo Service Design | **95** | **Hero Principal** | **Melhor tradução de Service Design para executivos:** une Blueprint real + Grandes Números (4 distribuidoras) + Matriz de 118 Ideias em grade ortogonal super escaneável. |
| **2º** | **V11** | Blueprint Studio Desk | **90** | **Capítulo de Blueprints** | **Excelente estética editorial:** valoriza o artefato físico/impresso do Service Blueprint com luz quente de estúdio; só perde 5 pts por ter um pouco menos de área útil de leitura que o V12. |
| **3º** | **V15** | Dark Energy Studio | **78** | **Alternativa Dark** | **Pior coerência com o portfólio:** fundo escuro contrasta bruscamente com o restante do case de Service Design e reduz a sensação de transparência documental dos blueprints. |

---

## Combo Campeão Recomendado para `v3.7.0`
- **Einstein:** `V17` (Hero) + `V03` (Antes vs. Depois) + `V13` (Visão 3 Canais A4/Web/Mobile)
- **Itaú:** `V16` (Hero) + `V07` (Jornada IA + Human-in-the-Loop)
- **Claro:** `V08` (Hero Multicanal) + `V10` (Esteira Unificada)
- **Neoenergia:** `V12` (Hero Bento Executivo) + `V11` (Blueprints em Mesa Editorial)
