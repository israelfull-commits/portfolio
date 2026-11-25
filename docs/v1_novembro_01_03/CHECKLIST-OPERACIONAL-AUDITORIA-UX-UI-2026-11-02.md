# Auditoria UX/UI Completa & Checklist Operacional de Correção: Todos os Cases

**Data:** 02 de Novembro de 2026  
**Avaliador:** Antigravity (Pair Programming / Design System & UX/UI Specialist)  
**Escopo da Auditoria:** Varredura total, inspeção visual, análise comparativa e verificação de código e console em **todos os cases do portfólio**:
1. `Einstein — Consumo de Resultados` (`/cases/einstein-laudos`)
2. `Neoenergia — Strategic Discovery & Service Design` (`/cases/neoenergia-conexao-digital`)
3. `Claro — Ativação Simplificada` (`/cases/claro-ativacao-simplificada`)
4. `Itaú — Gestão de Vencimentos` (`/cases/itau/vencimentos`)
5. `Itaú — Movimentações / Extrato EA` (`/cases/itau/movimentacoes`)
6. `Itaú — Gestão de Campanhas IFA` (`/cases/itau/campanhas`)
7. `Home / Showcase Selecionado` (`/`)

---

## 1. Matriz de Análise Comparativa entre Cases

| Critério UX/UI | Einstein (Saúde) | Neoenergia (Utilities) | Claro (Telecom) | Itaú (Fintech) |
| :--- | :--- | :--- | :--- | :--- |
| **Arquitetura Canônica** | 7 Capítulos (0 a 6) | 7 Capítulos (0 a 6) | 7 Capítulos (0 a 6) | 7 Capítulos (0 a 6) |
| **Kicker / Domínio no Hero** | Fixo genérico ("Design de produto") | Fixo genérico ("Design de produto") | Fixo genérico ("Design de produto") | Fixo genérico ("Design de produto") |
| **Métricas Auditadas** | Presente (3 cartões) | Presente (4 cartões) | Presente (4 cartões) | Integrado ao framing |
| **Galeria & Lightbox** | 2 imagens com modal | 8 imagens com modal | 5 imagens com modal | 2 a 4 imagens com modal |
| **Decisões Estratégicas** | Lista numerada (`cp-decisions`) | Lista numerada (`cp-decisions`) | Lista numerada (`cp-decisions`) | Lista numerada (`cp-decisions`) |
| **Evidências & Rastreabilidade** | `cp-appendix` (detalhes/fontes) | `cp-appendix` (detalhes/fontes) | `cp-appendix` (detalhes/fontes) | `cp-appendix` (detalhes/fontes) |
| **Navegação Próximo/Anterior** | ❌ Ausente | ❌ Ausente | ❌ Ausente | ❌ Ausente |
| **Breadcrumb de Topo** | ❌ Apenas na sidebar | ❌ Apenas na sidebar | ❌ Apenas na sidebar | ❌ Apenas na sidebar |
| **Aspect Ratio / CLS** | Alerta no DevTools | Alerta no DevTools | Alerta no DevTools | Alerta no DevTools |

---

## 2. Diagnóstico Detalhado & Problemas Identificados

### 2.1 Wayfinding e Fim de Fluxo (Next/Prev Case)
* **Problema:** Ao concluir a leitura do capítulo 7 ("Evidências e créditos"), o usuário se depara com um final abrupto. Recrutadores e avaliadores de design precisam rolar a página inteira de volta ou procurar o link na sidebar.
* **Impacto UX:** Perda de fluidez na leitura do portfólio e aumento da taxa de rejeição após a leitura do primeiro case.
* **Solução:** Implementar componente de navegação inter-cases (`.cp-case-nav`) com cartões clicáveis de "Case anterior" e "Próximo case", exibindo título, domínio e seta direcional.

### 2.2 Tag de Domínio no Hero (Personalização do Kicker)
* **Problema:** O componente `CasePresentation` renderizava `<Pill tone="accent">Design de produto</Pill>` estático em todos os cases, ignorando a especialidade de cada projeto.
* **Impacto UI:** Falta de diferenciação imediata entre Saúde de Alta Complexidade, Utilities/Infraestrutura Crítica, Telecomunicação e Fintech B2B.
* **Solução:** Adicionar campo opcional `kicker?: string` em `CasePresentationData` e utilizá-lo no `Pill`.

### 2.3 Breadcrumb de Acesso Rápido no Topo
* **Problema:** Em telas móveis (smartphones), a sidebar fica no topo do fluxo, mas em visualizações diretas de cases falta um link claro de retorno aos projetos logo acima do título principal.
* **Impacto Acessibilidade:** Facilita a orientação espacial de usuários que chegam através de links compartilhados ou buscas.
* **Solução:** Inserir trilha de navegação acessível `<nav aria-label="Trilha de navegação" className="cp-breadcrumb">` com link "← Voltar aos projetos selecionados".

### 2.4 Prevenção de Cumulative Layout Shift (CLS) em Imagens Lazy
* **Problema:** O Chrome DevTools emite alerta informando que imagens com `loading="lazy"` sem `aspect-ratio` explícito podem provocar pequenos saltos de renderização durante o carregamento de imagens de alta resolução.
* **Solução:** Incluir `aspectRatio: `${image.width} / ${image.height}`` inline na tag `<img>` de `CaseFigure`.

### 2.5 Interconexão dos Dossiês Confidenciais Itaú
* **Problema:** Os três dossiês do Itaú (`vencimentos`, `movimentacoes`, `campanhas`) estavam isolados entre si.
* **Solução:** Conectar a navegação entre os três dossiês confidenciais em um loop integrado.

---

## 3. Checklist Operacional de Execução

- [x] **Item 1:** Atualizar a interface `CasePresentationData` em `site/src/components/CasePresentation.tsx` com `kicker`, `prevCase` e `nextCase`.
- [x] **Item 2:** Atualizar o componente `CaseFigure` para definir `aspectRatio` inline e prevenir layout shift.
- [x] **Item 3:** Adicionar a barra de navegação inter-cases (`.cp-case-nav`) no rodapé de `CasePresentation`.
- [x] **Item 4:** Estilizar `.cp-case-nav` e `.cp-breadcrumb` em `site/src/components/case-presentation.css` com suporte responsivo e hover states.
- [x] **Item 5:** Configurar `kicker`, `prevCase` e `nextCase` em `einsteinPresentation`, `neoenergiaPresentation` e `claroPresentation` em `site/src/pages/CasePages.tsx`.
- [x] **Item 6:** Configurar `kicker`, `prevCase` e `nextCase` para os dossiês Itaú em `ItauPresentation` (`vencimentos` -> `movimentacoes` -> `campanhas`).
- [x] **Item 7:** Compilar com `npm run build` e validar ausência de erros TypeScript/Vite.
- [x] **Item 8:** Inspecionar visualmente e verificar mensagens no console via Chrome DevTools.
- [x] **Item 9:** Atualizar o pacote de entrega `output/portfolio-revisao-aprovada-2026-11-02.tar.gz`.
- [x] **Item 10:** Eliminar placeholders repetidos ("A história em 90 segundos", "Decisões conectadas ao problema", "Evidências e créditos") em todos os 7 cases.
- [x] **Item 11:** Eliminar duplicação verbatim de `{project.framing}` entre os Capítulos 1 e 2 nos cases Itaú.
- [x] **Item 12:** Mapear títulos jornalísticos e narrativos únicos para cada capítulo de cada projeto (Einstein, Neoenergia, Claro, Vencimentos, Hub de Liquidez, Movimentações, Campanhas, Registros com IA).
- [x] **Item 13:** Integrar pranchas de alta resolução dos Blueprints de Serviço (1. Contrato e Instalo, 2. Uso e Pago, Jornada To-Be e Matriz de 118 Ideias) na galeria do Case Neoenergia.
- [x] **Item 14:** Validar rotas com 100% de status HTTP 200 OK e compilação limpa no Vite.

---
*Checklist 100% executado e homologado em 02 de novembro de 2026.*
