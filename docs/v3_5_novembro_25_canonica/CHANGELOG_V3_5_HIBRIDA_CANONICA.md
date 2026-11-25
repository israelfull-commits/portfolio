# Changelog Detalhado — Versão V3.5 (Híbrida Canônica)

**Data:** 25 de Novembro de 2026  
**Conversa de Origem:** `b9eff66e-96f2-48ed-af7d-28e8cea0dfad`  
**Base Anterior:** Versão V3 (`4973062`)  
**Documento de Diagnóstico:** [DIAGNOSTICO-COMPARATIVO-TEXTOS-PORTFOLIO.md](./DIAGNOSTICO-COMPARATIVO-TEXTOS-PORTFOLIO.md)

---

## 1. Motivação Executiva

A auditoria comparativa entre as 5 versões históricas do portfólio (V1 Epistêmica, V2A Technobabble, V2B Executiva, V-Figma Plugin e V3 Produção) demonstrou que:
1. Os **textos internos da V3 nos 4 cases** eram os mais precisos, honestos e juridicamente seguros (NDA + LGPD), mas faltavam os micro-blocos explícitos de *Disciplina de Escopo* e *Reflexão Crítica* exigidos pelo `SENIOR_UX_PORTFOLIO_CANON.md`.
2. A **Home da V3 (`pf-home-compact`)** tinha o melhor Hero do histórico, mas ao ocultar a Trajetória apenas no PDF e remover a linha de escopo dos cards e os atalhos dos submódulos Itaú, perdia prova social na triagem rápida de 30–60s.
3. O **gerador de telas do Figma (`scripts/build_portfolio_figma_screens.py`)** ainda carregava métricas de template sem lastro documental (`R$ 42B+`, `60% menos tempo`, `45 min → 3 min`, `4 macroáreas`).

---

## 2. Alterações Aplicadas (V3 ➔ V3.5)

### A. Home (`site/src/pages/Home.tsx` & `site/src/portfolio.css`)
* **Preservado:** Hero canônico da V3 (*"Design de produtos para saúde, finanças e serviços essenciais."*).
* **Adicionado — Linha factual de escopo nos cards (`.pf-home-scope`):**
  * **Einstein:** `14 entregáveis · 121 pacientes · 4 médicos especialistas`
  * **Itaú Hub de Liquidez:** `íon for Advisors · 4 módulos operacionais`
  * **Claro:** `22 jornadas mapeadas · 70+ validações`
  * **Neoenergia:** `4 distribuidoras · 5 blueprints · 118 ideias` (paridade 100% com o case e `portfolio_qa_sentinel.py`)
* **Adicionado — Navegação de submódulos Itaú (`.pf-home-submodules`):**
  * Barra discreta abaixo da grade de projetos com links diretos para `Gestão de Vencimentos`, `Movimentações` e `Gestão de Campanhas`.
* **Adicionado — Trajetória Resumida na Tela (`.pf-home-trajectory`):**
  * 5 linhas escaneáveis dentro de `#sobre`: Itaú Unibanco (`2024 – 2026`), Consultoria Independente (`2022 – atual`), Foursys + Hospital Albert Einstein (`2022`), EY · R/GA (`2020 – 2022`), Ciência da Computação — Univali (`2006 – 2019`), mantendo o CTA de download do currículo completo em PDF.

### B. Cases (`site/src/pages/CasePages.tsx`)
* **Adicionado em todos os 4 cases emblemáticos (Einstein, Claro, Neoenergia e Itaú):**
  * Grid de 2 cards sênior ao final do Capítulo 6 (`.cp-cards-grid` / `.cp-feature-card`):
    1. **Disciplina de Escopo — "O que ficou fora do recorte"** (decisões factuais de foco e trade-offs reais).
    2. **Reflexão Crítica — "O que eu faria diferente hoje"** (aprendizado técnico maduro sem jargão).

### C. Alinhamento Factual do Plugin Figma (`scripts/build_portfolio_figma_screens.py`)
* **Removidas todas as métricas de template sem lastro documental:**
  * Einstein: corrigido *"4 macroáreas fixas"* ➔ **3 macroáreas canônicas (Metodologia, Resultado, Conclusão Diagnóstica)**; substituído *"78% dos médicos pulavam / ansiedade extrema"* pelos dados reais verificados (**81,6% reconhecimento / 77,8% atenção no núcleo**).
  * Itaú: removidos *"R$ 42B+"*, *"60% menos tempo"* e *"45 minutos para 3 minutos"*; alinhado ao escopo real dos 5 recortes na plataforma íon for Advisors (2024–2026) sob sigilo bancário.
  * Claro: removidos *"15 telas → 3 etapas"*, *"40% das quedas"* e *"34M clientes"*; alinhado às evidências reais (**22 jornadas, 20 pessoas em imersão, 10 entrevistas, 70+ validações**).
* **Recompilado e sincronizado:** `code.js` e `ui.html` atualizados em `figma-refine-plugin` e `gemini-figma-plugin`.

### D. Limpeza de Metadados Internos de Auditoria e Nós do Figma (`CasePages.tsx`, `ItauPreparationCase.tsx`, `portfolio_qa_sentinel.py`)
* **Removidos todos os IDs internos de nós do Figma visíveis ao leitor final:** `nó 3:14068`, `nó 582:12520`, `nó 1966:34105` (mantidos exclusivamente na documentação histórica em `docs/`).
* **Removida meta-linguagem de auditoria em terceira pessoa:** expressões como *"confirmada pelo autor"*, *"fornecida pelo autor em 02/11/2026"*, *"os demais frames são tratados como histórico"* e *"acervo de 2017–2018"* foram reescritas em linguagem executiva direta para o leitor do portfólio.
* **Proteção Permanente no Sentinela:** adicionados filtros regex em `scripts/portfolio_qa_sentinel.py` para bloquear futuros vazamentos de IDs de nó do Figma ou frases de auditoria interna na interface pública.

---

## 3. Validação Técnica (Gates de Aprovação)
* `npm --prefix site run build`: 0 erros, 7 rotas SPA estáticas + `404.html`.
* `npm --prefix portfolio-verde run build`: 0 erros, sincronia 1:1 mantida.
* `python scripts/portfolio_qa_sentinel.py`: 7/7 PASS.
* `python scripts/test_color_accessibility.py`: 100% WCAG AA & WCAG AAA.
* `python scripts/test_ux_a11y_comprehensive.py`: 0 falhas de acessibilidade, `alt`, alvos de toque ou hierarquia.

