# Guia Estruturado de UX Audit (2026) — Síntese & Curadoria Aplicável ao Portfólio

> **Fonte original:** [UX Companion — The Complete Guide to UX Audits (2026)](https://uxcompanion.co.uk/ux-audit)  
> **Curadoria:** Síntese filtrada contendo o framework completo e destacando exclusivamente o que gera valor prático para o portfólio, os estudos de caso e o `portfolio_qa_sentinel.py`.

---

## 1. Definição & Postura Técnica
- **O que é:** Revisão estruturada de um produto digital contra frameworks objetivos de **usabilidade (Nielsen)**, **acessibilidade (WCAG 2.2)** e **comportamento**, produzindo achados priorizados por severidade, regra violada e correção recomendada.
- **O que NÃO é:** Brief de redesign, lista de desejos de features ou preferência pessoal (*"eu teria feito diferente"*).
- **Regra de ouro:** **Cite a regra, não a opinião** (*"Falha WCAG 2.2 1.4.3"* ou *"Viola Heurística #1 de Nielsen"*).

---

## 2. Os 4 Tipos de Auditoria & Pacote Padrão
| Tipo | Escopo | Quando Usar |
| :--- | :--- | :--- |
| **1. Heurística** | 10 Heurísticas de Nielsen | Ponto de partida rápido para superfície geral |
| **2. Acessibilidade** | WCAG 2.2 AA/AAA | **Maior alavancagem:** achados objetivos e não-negociáveis |
| **3. Conversão / Fluxo** | 1 fluxo crítico + dados | Onboarding, checkout, funil de conversão |
| **4. Produto Completo** | IA, fluxos, estados, mobile, performance | Pré-redesign, replataforma ou pós-aquisição |

> **Pacote Padrão Recomendado:** **Heurística + Acessibilidade juntos** — produtos que falham em um quase sempre falham no outro.

---

## 3. Processo Canônico em 6 Etapas
1. **Escopo (Scope):** Definir o que entra, o que fica fora e o critério de sucesso.
2. **Planejamento (Plan):** Escolher frameworks, rubrica de severidade e stakeholders.
3. **Evidência (Evidence):** Percorrer fluxos, capturar telas, rodar ferramentas e mapear falhas contra as regras.
4. **Pontuação (Score):** Aplicar rubrica de severidade e agrupar achados correlatos.
5. **Recomendação (Recommend):** Para cada achado, propor correção comportamental com esforço e impacto estimados.
6. **Apresentação (Present):** Abrir com os **Top 3 achados críticos**, citar as regras violadas e converter em roadmap acionável.

---

## 4. Os 10 Problemas Mais Comuns em Auditorias UX (Checklist Direto)

| # | Problema Recorrente | Critério WCAG / Heurística | Status no Portfólio Hoje |
| :-: | :--- | :--- | :---: |
| 1 | **Contraste de CTA primário falha em `:hover` ou `:focus`** *(passa no padrão, quebra no estado interativo)* | WCAG 2.2 `1.4.3` / `1.4.11` | **Oportunidade:** adicionar teste de `:hover`/`:focus` no Sentinel v2 |
| 2 | Inputs usando `placeholder` no lugar de `<label>` | WCAG `3.3.2` | **Atendido** (`CaseAccessGate` usa `<label htmlFor>`) |
| 3 | Indicadores de foco removidos (`outline: none` sem substituto) | WCAG `2.4.7` / `2.4.13` | **Atendido** (`:focus-visible` preservado) |
| 4 | Mensagens de erro tardias ou sem contexto | Nielsen `#9` / `role="alert"` | **Atendido** (`role="alert"` + limpeza no `onChange`) |
| 5 | Hierarquia de headings quebrada (múltiplos `<h1>`, pulos `h1→h3`) | WCAG `1.3.1` / `2.4.6` | **Atendido** (validado no Sentinel v2) |
| 6 | Alvos de toque abaixo de `24×24px` | WCAG 2.2 `2.5.8` | **Atendido** (validado no Sentinel v2) |
| 7 | Navegação inconsistente entre seções | WCAG `3.2.3` | **Atendido** (`SiteHeader` + breadcrumbs + navegação circular) |
| 8 | Falta de confirmação em ações destrutivas | WCAG `3.3.4` | N/A (portfólio de leitura) |
| 9 | Banners de cookies bloqueando teclado/leitor de tela | WCAG `2.1.1` | N/A (zero cookies de terceiros) |
| 10 | Estados de carregamento ausentes ou enganosos | Nielsen `#1` | **Atendido** (`RouteLoading` com `role="status"` + estado `"Verificando…"`) |

---

## 5. Espinha Dorsal: 10 Heurísticas de Nielsen & WCAG 2.2 Prioritários
- **Nielsen (1–10):** (1) Visibilidade do status do sistema · (2) Correspondência com o mundo real · (3) Controle e liberdade do usuário · (4) Consistência e padrões · (5) Prevenção de erros · (6) Reconhecimento em vez de memorização · (7) Flexibilidade e eficiência · (8) Estética e design minimalista · (9) Ajudar a reconhecer, diagnosticar e recuperar erros · (10) Ajuda e documentação.
- **Critérios WCAG 2.2 oficiais prioritários (W3C Quick Reference — alto diferencial sênior):**
  - `2.4.11` / `2.4.12` **Focus Not Obscured (AA/AAA):** elemento focado via teclado nunca pode ficar oculto atrás do header fixo (`SiteHeader`) ou mídia sticky — aplicar `scroll-padding-top` global.
  - `2.4.13` **Focus Appearance (AAA):** indicador de foco com perímetro mínimo `>= 2px` e contraste `>= 3:1`.
  - `2.5.7` **Dragging Movements (AA):** toda ação por arraste (ex.: pan no Lightbox em zoom 1:1) precisa de alternativa de clique simples / teclado / scroll.
  - `2.5.8` **Target Size (Minimum) (AA):** alvos de toque `>= 24×24 CSS px` (já validado no Sentinel v2).
  - `3.3.8` **Accessible Authentication (AA):** aplicável diretamente ao `CaseAccessGate.tsx` — campo de senha deve sempre permitir `paste` e gerenciadores de senha, sem testes cognitivos/CAPTCHA.

---

## 6. Matriz de Priorização (Esforço × Impacto)
- **Alto Impacto / Baixo Esforço (`Quick Wins`):** Entregar imediatamente na semana atual.
- **Alto Impacto / Alto Esforço (`Estruturantes`):** Próximo ciclo / direção de Design System.
- **Baixo Impacto / Baixo Esforço (`Backlog`):** Limpar em sprints tranquilos.
- **Baixo Impacto / Alto Esforço (`Estacionar`):** Revisitar apenas se o contexto de negócio mudar.

---

## 7. Curadoria: O Que Adotar vs. O Que Descartar

### Vale adotar como prática permanente
1. **Teste de contraste em `:hover` e `:focus-visible`** no `portfolio_qa_sentinel.py` (o achado de acessibilidade nº 1 mais ignorado segundo o guia).
2. **Formato "Regra violada + Severidade + Top 3"** em qualquer relatório futuro de auditoria do portfólio (sempre citando WCAG 2.2 ou Heurística de Nielsen, nunca opinião subjetiva).
3. **Uso estratégico nos textos dos cases:** reforçar o vocabulário técnico de auditoria (critérios WCAG 2.2 específicos e matriz Esforço × Impacto) onde já há evidência real (Einstein e Neoenergia).

### Descartar (irrelevante para o portfólio)
- Precificação de consultoria (`£2.500–£30.000`), M&A due diligence, cookie banners e dinâmicas de workshop corporativo.
