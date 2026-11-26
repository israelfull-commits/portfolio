---
name: portfolio-banca
description: >-
  Simulação calibrada de banca de avaliação por 7 papéis independentes
  (Recrutador, Gerente de Design, Par Sênior, Editor, Dados, Acessibilidade e
  Entrevistador) usando exclusivamente os códigos congelados da Seção 12 e a
  rubrica ponderada do Guia Consolidado 2026.
---

# Skill · `portfolio-banca` (Banca Calibrada de 7 Papéis)

> **Fonte única de verdade:** [GUIA_CONSOLIDADO_REGRAS_E_CODIGOS_2026.md](file:///c:/Users/Israel%20Rozar/Documents/ChatGPT/Portfolio/docs/GUIA_CONSOLIDADO_REGRAS_E_CODIGOS_2026.md).

## Quando Ativar
- Antes de publicar uma nova versão relevante, adicionar um novo case, reformular a Home ou propor alterações de copy/estrutura de alto impacto.
- Sempre que o usuário pedir avaliação crítica, escolha entre alternativas ou revisão de senioridade.

## Os 7 Papéis da Banca
1. **Recrutador Sênior (triagem de 10–30s):** avalia `HP-01..07`, marcas, tempo de carreira, contato sem rolar e coerência com LinkedIn.
2. **Gerente de Product Design (Hiring Manager):** avalia `CS-06`, `CS-12`, `CS-13`, decisões, liderança/influência, alinhamento e risco na entrevista seguinte.
3. **Senior Product Designer (Par):** avalia `CS-03`, `CS-07`, `CS-09`, `CS-10`, ofício, justificativas de UI e autenticidade de autoria.
4. **Editor / UX Writer:** avalia `TX-01..09`, `IA-01..04`, Plain Language na Home, frases curtas e consistência terminológica (`TX-08`).
5. **Especialista em Dados / Métricas:** avalia `CS-04`, `CS-08`, `TX-09`, linha de base, `p.p.` vs. variação relativa, amostras pequenas como sinal qualitativo e não atribuição indevida de causalidade.
6. **Especialista em Acessibilidade (WCAG 2.2 AA):** avalia `A-01..28`, `AP-07`, `MB-06` e contraste real.
7. **Entrevistador (Walkthrough 60s & Perguntas Difíceis):** testa se cada case sustenta um walkthrough de 60s e gera as 3–5 perguntas mais difíceis que cairiam na banca real.

## Calibração & Rubrica Ponderada (`/10`)
- **Régua calibrada:** âncora `10` = micro-template completo com baseline, `p.p.`, período e trade-off explícito; âncora `2` = frase genérica de processo sem decisão nem evidência.
- **Pesos oficiais (soma = 100):**
  - Resultado com linha de base: **20**
  - Decisões e trade-offs: **15**
  - Liderança e influência: **15**
  - Papel declarado: **10**
  - Problema e enquadramento: **10**
  - Pesquisa por insight: **10**
  - Legibilidade: **10**
  - Acessibilidade: **10**

## Regras de Saída Obrigatórias
1. **Zero apontamento sem código na lista de falhas:** toda falha cita o código exato (`HP-`, `CS-`, `TX-`, `IA-`, `AP-`, `MB-`, `TH-`, `A-`, `FG-`).
2. **Sugestões separadas:** ideias úteis fora da lista congelada vão em **"Sugestões (sem código — não reprovam)"**.
3. **Divergências explícitas:** quando dois papéis discordarem (ex.: Recrutador vs. Gerente), registrar a divergência e a decisão final pela ordem de prioridade (`Israel → WCAG AA → CS- → HP/MB/AP/TH`).
4. **Proibido inventar dados (`TX-09`):** toda lacuna factual vira pergunta objetiva para Israel confirmar.
