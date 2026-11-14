# Changelog & Documentação de Decisões: Case Albert Einstein

**Data:** 14/11/2026  
**Projeto:** Consumo de Resultados — Hospital Israelita Albert Einstein × Foursys  
**Papel:** UX Lead  
**Arquivo Figma Mestre:** `MhzG5b6F1NIob0tL9lq5dF/HIAE---Laudos--c%C3%B3pia-`

---

## 1. Contexto e Motivação das Mudanças

Este documento registra formalmente as decisões de revisão textual, metodológica e visual do case **Albert Einstein**, garantindo rastreabilidade histórica e conformidade com as evidências documentadas no Figma oficial do projeto.

### Problemas Diagnosticados na Rodada Anterior:
1. **Jargões excessivos e academicismo:** Tentativas anteriores de evitar linguagem de marketing acabaram resultando em termos tecnocráticos e rebuscados (*"ancoragem determinística"*, *"desacoplamento de metadados"*, *"tolerância dimensional"*, *"fadiga cognitiva médica"*). Isso criava uma barreira para recrutadores, gestores de produto e profissionais não especialistas em UX.
2. **Inferência indevida de dores:** O termo *"ansiedade do paciente"* foi identificado como uma suposição interpretativa não respaldada pelos dados brutos das entrevistas.
3. **Desalinhamento com a tese histórica:** Os arquivos originais do projeto continham formulações autênticas mais sólidas e equilibradas para sintetizar o desafio ético do design em saúde: facilitar a leitura sem simplificar indevidamente o contexto médico.

---

## 2. Decisões Editoriais e Evidências do Figma

### A. Título e Headline do Hero
- **Versão Adotada:**
  - **Título:** *Albert Einstein · Consumo de Resultados*
  - **Headline:** *Uma linguagem visual modular para laudos heterogêneos.*
  - **Subtítulo:** *"Um trabalho coletivo entre pesquisa, conteúdo, interface e viabilidade técnica para facilitar a criação dos laudos e a localização de informações sem simplificar indevidamente o contexto clínico."*
- **Fundamentação & Evidência:**
  - Encontrado literalmente nos frames do Figma: `id=7339:67542` (Consumo de Resultados — Mobile), `id=7339:65714` (Consumo de Resultados — Desktop) e no entregável de boas práticas `EN - 4 / EN - 11`.
  - Articula os 4 eixos essenciais do trabalho: **pesquisa**, **conteúdo (UX Writing)**, **interface (Design System Zera 1.0)** e **viabilidade técnica (sistemas hospitalares LIS/PACS)**.
  - Aborda os dois lados da cadeia de valor: **facilitar a emissão/criação** e **a localização de informações**.
  - Estabelece a fronteira ética mandatória: *"sem simplificar indevidamente o contexto clínico"*.

---

### B. Pergunta Norteadora e Abertura do Capítulo 1
- **Versão Adotada:**
  - **Pergunta em Destaque:** *"Como facilitar a localização e a leitura do laudo sem induzir uma interpretação clínica isolada?"*
  - **Contexto Operacional:** *"Laudos de diferentes laboratórios e hospitais parceiros reuniam informações críticas em estruturas variáveis. O projeto desenhou uma linguagem modular previsível para mais de 80 tipos de exames, permitindo que médicos cruzem resultados, métodos e referências com agilidade, e que pacientes localizem seus dados com facilidade para levar à conversa médica."*
- **Fundamentação & Evidência:**
  - Transcrição exata da pergunta de pesquisa documentada no nó de enquadramento do desafio: `id=7303:75341` e `figma-make-reference/EinsteinCase.tsx` (linhas 106-129).
  - Define o papel do paciente de acordo com a pesquisa real: **localizar com facilidade o que importa para levar à consulta com o médico**, eliminando inferências sobre ansiedade e evitando a automedicação/diagnóstico desacompanhado.

---

### C. Métricas de Validação e Pesquisa
- **Métricas do Painel Sincronizado:**
  - **121:** pacientes responderam ao questionário de hábitos de leitura.
  - **4:** médicos especialistas entrevistados em profundidade.
  - **14:** entregáveis canônicos e famílias de laudos estruturadas (`EN - 1` a `EN - 14`).
- **Resultados de Teste Documentados no Figma (`EN - 7 / EN - 14`):**
  - **81,58%** dos participantes reconheceram de imediato que se tratava de um exame médico (Q1).
  - **77,78%** identificaram a hierarquia direta entre Título, Resultado e Referência (Q2).
  - **58,82%** compreenderam o nome e objetivo do exame (Q3).
  - **56,25%** interpretaram corretamente a situação do resultado com apoio de status visual e cores semafóricas (Q4).
  - **Conclusão:** *"Clareza percebida não é o mesmo que compreensão causal"*, justificando por que a interface apoia a conversa clínica em vez de substituir o médico.

---

## 3. Log de Alterações no Repositório (Git Commits)

| Commit | Escopo | Descrição das Modificações |
| :--- | :--- | :--- |
| `b872a77` | UI Craft & Grid | Equalização de proporções da galeria (16:10), remoção de títulos repetidos em mockups e conformidade 100% WCAG AAA. |
| `c3479c3` | Estrutura | Aplicação de simetria nos cards métricos e eliminação de disclaimers defensivos. |
| `ba58351` | Qualidade | Inclusão de regras anti-marketing no sentinela automatizado (`AGENTS.md` e `portfolio_qa_sentinel.py`). |
| `d69463d` | Redação | Desjargonização do vocabulário para português claro, humano e compreensível por qualquer leitor. |
| `ae042f3` | Fidelidade | Remoção de inferência não documentada sobre "ansiedade" e alinhamento estrito aos dados reais da pesquisa. |
| `[atual]` | Harmonização | Implantação da tese executiva autêntica e da pergunta norteadora no Hero e Capítulo 1. |

---

## 4. Estado de Publicação
- **URL Canônica em Produção:** [https://israelfull-commits.github.io/portfolio/cases/einstein-laudos](https://israelfull-commits.github.io/portfolio/cases/einstein-laudos)
- **Status do Build:** 100% PASS (0 erros, 0 alertas, rotas estáticas SPA geradas).
