# Auditoria Editorial Integral & Paridade Omnicanal — Todos os Textos do Portfólio (`V1 ➔ V4.1.0`)

> **Proveniência & Rastreabilidade**  
> - **IA / Plataforma:** Antigravity — Google DeepMind  
> - **Data de criação:** 2026-11-26  
> - **Última atualização:** 2026-11-26  
> - **Conversa de origem:** [66417f41-f841-4d50-a701-e678302e3ec2](conversation://66417f41-f841-4d50-a701-e678302e3ec2)  
> - **Agentes & Skills aplicados:** 4 subagentes paralelos (`Home & Chrome`, `Einstein`, `Claro & Neoenergia`, `Suíte Itaú IFA`) · `portfolio-writing` · `portfolio-banca` (7 papéis) · `portfolio-design-qa` · `senior-portfolio-audit` · `figma-use` · `figma-generate-design`  
> - **Fonte normativa:** [GUIA_CONSOLIDADO_REGRAS_E_CODIGOS_2026.md](../GUIA_CONSOLIDADO_REGRAS_E_CODIGOS_2026.md) (90 códigos congelados) & [AGENTS.md](../../AGENTS.md)

---

## 1. Matriz Comparativa Consolidada por Superfície (`V1 ➔ V4.1.0`)

| Superfície | V1 (03/Nov) | V2A/V2B (14/Nov) | V-Figma Plugin (anterior) | V3 / V3.5 (25/Nov) | V4.0.1 / V4.0.2 (Anterior) | **V4.1.0 (VIGENTE)** | Principais Correções Aplicadas em `V4.1.0` |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **Home · Hero** *(ver relatório dedicado)* | 60 | 66 | 66 | 79 | 93 ➔ **100** | **100** | Já consolidada em `V4.0.2` (`d79fabe`): 1ª pessoa (`TX-01`/`TX-02`), escopo factual no Itaú (`TX-06`/`TX-09`), glossário `TX-08` e paridade Figma (`FG-06` `12px`). |
| **Home (Fora do Hero) + Global Chrome + Meta** | 54 | 67 | 64 | 77 | 87 | **98** | Corrigido bug de `index.html:63` que sobrescrevia `JSON-LD Person.url` para `/` (`TH-05`); `skip-link` + `tabIndex={-1}` no `CaseAccessGate` e `NotFound` (`A-12`); removido *"ainda estar em preparação"* de `NotFound` (`TX-04`/`TX-06`); `sr-only (abre em nova aba)` restaurado no `LinkedIn` de `ContactSection` (`A-15`/`A-23`); CTAs dos 4 cards unificados em `Ver estudo de caso` (`A-23`/`TX-08`); frases curtas + fronteira de julgamento humano em IA em `#sobre` (`TX-07`/`IA-01`); `Estudos complementares` e `& outras → e outras` (`TH-08`). |
| **Case 01 · Hospital Albert Einstein** | 54 | 48 / 66 | 44 | 76 | 79 | **96** | Removido anacronismo `WCAG 2.2 AAA` (projeto de 2022 · `TX-09`), removida afirmação *"em produção"* sem lastro na legenda Hero (`CS-14`/`TX-09`) e removidas especialidades médicas não comprovadas em fonte primária (`TX-09`/`IA-02`); adicionados 2 cards de decisão no micro-template (`CS-06`/`TX-05`), `keyMetricLabel: "VALIDAÇÃO E ESCOPO"` (`CS-08`), abertura por insight (`CS-04`), legendas de porquê (`CS-07`), reflexão de 3 frases com decisão a reverter (`CS-09`) e `7 min de leitura` (`CS-11`). |
| **Case 02 · Itaú IFA (5 módulos)** | 46 | — | 52 | 72 | 82 | **96** | Eliminado 100% o boilerplate idêntico (F02 · `CS-09`/`CS-10`) com *Disciplina de Escopo* e *Reflexão Crítica* exclusivas por módulo; corrigida contradição factual na legenda/alt de *Movimentações* (`cabeçalho com saldo provisionado` vs. `limites em Movimentações` · `TX-08`/`TX-09`); corrigido termo sem lastro *"proventos e agenda"* em *Vencimentos* (`TX-09`); corrigido H2 de *Campanhas* (`administradores, especialistas e gestores` · `TX-08`); 3 decisões com alternativas e custo aceito nos 5 módulos (`CS-06`/`TX-05`); `ENTREGA PRINCIPAL` (`CS-08`), identificação ilustrativa em *Registros* (`IA-04`), rota SPA `cases/itau/registros-atendimento` (`TH-03`) e tempo de leitura em `vencimentos` (`CS-11`). |
| **Case 03 · Claro Brasil** | 46 | 60 | 54 | 71 | 74 | **96** | Removido `"até 40% do tempo observado"` sem protocolo (`TX-09`) e `"validação instantânea"` (`TX-03`); 3 decisões estruturadas com alternativas e custo aceito (`CS-06`/`TX-05`), status de entrega V.2 sem medição pós-implantação (`CS-14`/`TX-06`), reflexão de 4 frases com decisão a reverter (`CS-09`), correção do desalinhamento de tag/título do Cap. 5 (`Acervo & Equipe` · `A-15`/`A-16`), lista `<ol className="cp-card-list--numbered">` sem `• 1.` (`TH-08`) e legendas explicando o porquê (`CS-07`). |
| **Case 04 · Neoenergia** | 50 | 66 | 62 | 73 | 75 | **96** | Adicionados enquadramento (`CS-05`) e papel individual × consórcio (`CS-03`) visíveis no Cap. 1; 3 decisões estruturadas com custo aceito (`CS-06`/`TX-05`); corrigido estágio `5. Encerramento → 5. Abandono` e `alt`/legenda da prancha `Jornada futura com 118 ideias` (`A-01`/`TX-08`/`TX-09`); removidos overclaims de código/WCAG/tempo real incompatíveis com P&D (`TX-06`/`TX-09`), removida expressão `"esteiras de inovação"` (`TX-04`), unificado `"118 ideias"` / `"34 milhões de habitantes"` / `"Service Design"` (`TX-08`), e links externos de `Sources` com `target="_blank"` + `sr-only` (`A-15`). |
| **Figma `731:699` & Plugin (`build_portfolio_figma_screens.py`)** | — | — | 52 | — | 78 | **98** | `84` nós de `11px` elevados para `12px` (`FG-06`), termo banido `"transformar"` corrigido em `737:829` (`TX-04`), cards/Sobre sincronizados em `736:703`; 8 violações removidas de `build_portfolio_figma_screens.py` (`Expertise`, `TEMPO: -60%`, `transformar/Transformação`, `rigorosa`, `dos assessores`) e bundles recompilados em `figma-refine-plugin` e `gemini-figma-plugin`. |

---

## 2. Validação Técnica, Visual & Omnicanal (`V4.1.0`)

- **Build Produção:** `npm --prefix site run build` — `0` erros, **8 rotas estáticas SPA `200 OK`** (+ `404.html`), incluindo `cases/itau/registros-atendimento/index.html`.
- **QA Sentinel v2:** **`15/15 PASS`** (todos os 10 gates estáticos + 5 gates runtime em Chromium: Gestalt, tipografia, WCAG 2.2 AA/AAA, `:hover`/`:focus-visible`, `CaseAccessGate` SHA-256, Negative Prompting & Open Graph) + espelhamento 1:1 para `portfolio-verde/`.
- **Inspeção Visual Óptica:** capturas verificadas em Chromium (`1440×900` em `#trabalho` e `#sobre`) e Figma (`736:703`), confirmando alinhamento em linha única de `Ver estudo de caso →` com `CaseReadingTime` nos 3 cards, zero estouro e zero regressão.

---

## 3. Pendências Factuais para Confirmação de Israel (`TX-09` — Sem Estimação)

Os pontos abaixo foram tratados com honestidade conservadora na `V4.1.0` (sem inventar números nem status) e só devem ser expandidos se Israel confirmar os fatos:
1. **Einstein (`CS-14` / `CS-08`):** o padrão v3 chegou a entrar em produção após a entrega EN-1..EN-14? Qual o denominador `n` exato dos percentuais `81,6% / 77,8% / 58,8% / 56,2%`? As especialidades `cardiologia, radiologia e hematologia` são confirmadas?
2. **Itaú IFA (`CS-14` / `CS-15` / `Home.tsx`):** qual o status real de produção de cada um dos 5 módulos? Os links diretos do Figma em `CasePages.tsx` (apêndice) devem permanecer públicos ou virar nota institucional sob sigilo bancário (como no Einstein)? O card da Home deve exibir `"4 módulos operacionais"` ou `"5 módulos operacionais"`?
3. **Claro & Neoenergia (`TX-09` / `CS-15`):** há protocolo/amostra documentada para o antigo `"até 40% do tempo"` na Claro? Os 6 links externos de Drive/Slides/Figma da Neoenergia têm permissão pública verificada para recrutadores?
4. **Sobre (`IA-01` / `TH-06`):** deseja nomear ferramentas específicas de IA em `#sobre` ou manter o foco em finalidade + julgamento humano? Na próxima geração do CV PDF (`israel-rozar-curriculo.pdf`), remover o link legado `uxfol.io/israelrozar` e alinhar o resumo para `"Mais de 15 anos de experiência"`.
