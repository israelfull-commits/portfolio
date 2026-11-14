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
  - **81,6%** dos participantes reconheceram de imediato que se tratava de um laudo médico (Q1).
  - **77,8%** focaram a atenção no conjunto primordial: Título do Exame, Resultado e Referência (Q2).
  - **58,8%** compreenderam com clareza o objetivo daquele exame (Q3).
  - **56,2%** interpretaram a condição clínica sem apoio de um profissional (Q4).
  - **Conclusão:** *"Clareza percebida não é o mesmo que compreensão causal"*, justificando por que a interface apoia a conversa clínica em vez de tentar substituir o diagnóstico do médico.

---

### D. Capítulos 5, 6 e 7 (Solução, Validação e Governança)
- **Capítulo 5 — Uma estrutura única para qualquer tipo de exame:**
  - Redação simples e direta demonstrando a versatilidade da anatomia modular para exames descritivos (mamografia/biópsias) e tabulares (ressonâncias/hemogramas).
  - Galeria de imagens balanceada com proporção 16:10, eliminando ruídos visuais e preservando a continuidade multicanal (web, mobile e folha A4 impressa).
- **Capítulo 6 — Clareza de leitura e diagnóstico clínico: papéis complementares:**
  - Substituição de notas defensivas ou de rascunho pelo painel de 4 métricas oficiais do Figma em `<dl className="cp-metrics">`.
  - Conclusão afirmativa e madura: o design elimina o ruído e guia o olhar (80%+ de facilidade de localização), mas preserva a premissa ética de apoiar a relação médico-paciente.
- **Capítulo 7 — Pesquisa, entregáveis e colaboração:**
  - Enquadramento executivo e transparente das fontes oficiais, governança de dados (LGPD) e colaboração multidisciplinar (Foursys × Einstein).

---

## 3. Log de Alterações no Repositório (Git Commits)

| Commit | Escopo | Descrição das Modificações |
| :--- | :--- | :--- |
| `b872a77` | UI Craft & Grid | Equalização de proporções da galeria (16:10), remoção de títulos repetidos em mockups e conformidade 100% WCAG AAA. |
| `c3479c3` | Estrutura | Aplicação de simetria nos cards métricos e eliminação de disclaimers defensivos. |
| `ba58351` | Qualidade | Inclusão de regras anti-marketing no sentinela automatizado (`AGENTS.md` e `portfolio_qa_sentinel.py`). |
| `d69463d` | Redação | Desjargonização do vocabulário para português claro, humano e compreensível por qualquer leitor. |
| `ae042f3` | Fidelidade | Remoção de inferência não documentada sobre "ansiedade" e alinhamento estrito aos dados reais da pesquisa. |
| `088b70f` | Hero & Ch 1-4 | Implantação da tese executiva autêntica e pergunta norteadora no Hero e Capítulos 1 a 4. |
| `[atual]` | Ch 5, 6 e 7 | Refinamento da anatomia modular, painel de validação Q1-Q4 e governança ética nos Capítulos 5, 6 e 7. |

---

## 4. Estado de Publicação
- **URL Canônica em Produção:** [https://israelfull-commits.github.io/portfolio/cases/einstein-laudos](https://israelfull-commits.github.io/portfolio/cases/einstein-laudos)
- **Status do Build:** 100% PASS (0 erros, 0 alertas, rotas estáticas SPA geradas).
