# Regras Canônicas de Qualidade: Portfólio & Cases Senior Product Designer

Este documento consolida os aprendizados, convenções arquiteturais e diretrizes de craft estabelecidas para a evolução contínua deste portfólio. Qualquer agente ou automação deve seguir rigorosamente estes princípios.

---

## 1. Postura e Calibre Editorial (Senior Product Designer)
- **Linguagem Executiva e Afirmativa:** Nunca utilizar expressões defensivas, autocríticas ou disclaimers de rascunho (ex.: *"conteúdo fictício"*, *"não comprova implantação"*, *"limites das evidências"*, *"relato original"*, *"amostras não se somam"*).
- **Enquadramento de Proteção de Dados:** Interfaces e protótipos em domínios regulados (Saúde, Finanças) devem ser descritos sob a ótica de **dados sintetizados/anonimizados para conformidade com a LGPD, sigilo médico ou sigilo bancário**, preservando a hierarquia visual real e os contratos de dados acordados com especialistas.
- **Triangulação e Rigor de Pesquisa:** Descrever metodologias como **pesquisa quantitativa combinada a entrevistas semiestruturadas em profundidade**, evidenciando o cruzamento entre dores de usuários e requisitos de negócio/operação.
- **Consistência Numérica Estrita:** Números e métricas apresentados na vitrine da Home devem ser 100% idênticos aos detalhes do case correspondente (ex.: 4 distribuidoras integradas e 5 blueprints de serviço no case Neoenergia).

---

## 2. Padrões de Imagem e Craft Visual
- **Tratamento de Estúdio (Master Hero):** Imagens principais de cases devem receber acabamento fotográfico editorial com sombreamento multi-tier (drop-shadow suave e difuso), moldura externa de contenção física (ex.: pine casing `#102B1D`), cantos arredondados e badges informativos de alta legibilidade.
- **Recortes Precisos (Bezel Elimination):** Ao realizar recortes de telas a partir de assets compostos, calcular as coordenadas exatas para eliminar bordas de dispositivos ou molduras de laptops antigas sem cortar textos clínicos ou elementos de interface.
- **Acessibilidade Visual (WCAG AAA):** Vetores conectores, callouts e textos anotados sobre imagens devem manter contraste superior a 12:1 contra o fundo, usando tipografia proporcional e badges numerados legíveis.

---

## 3. Arquitetura de Software e Deploy (GitHub Pages SPA)
- **Resolução Dinâmica de Ativos (`assetUrl`):** Nunca inserir caminhos absolutos estáticos como `<img src="/images/..." />` ou `<a href="/documents/..." />` diretamente no JSX. Sempre envolver com `assetUrl(path)` para garantir que o prefixo de subdiretório do GitHub Pages (`/portfolio/`) seja injetado dinamicamente em produção.
- **Geração Estática de Rotas SPA:** O script `site/scripts/generate_spa_routes.js` deve ser executado obrigatoriamente no pós-build (`npm run build`). Ele gera diretórios estáticos correspondentes a cada rota (`cases/.../index.html`) e o `404.html`, garantindo resposta direta com **HTTP 200 OK** em qualquer navegação direta ou atualização de página.
- **Navegação Circular Entre Cases:** O rodapé de cada case deve alimentar o fluxo contínuo de leitura do recrutador, apontando ciclicamente para o próximo case da esteira: **Einstein ➔ Itaú ➔ Claro ➔ Neoenergia ➔ Einstein**.

---

## 4. Governança de Repositório e Sincronização
- **Sincronia 1:1:** O projeto `site/` é o ambiente canônico de produção. O diretório `portfolio-verde/` deve ser mantido rigorosamente sincronizado.
- **Proteção do Git Index:** O diretório `portfolio-verde/` contém seu próprio controle local e deve sempre ser ignorado no `.gitignore` raiz para evitar o erro de *embedded git repository*.
- **Pre-push Verification:** Antes de realizar push para a branch `main`, validar que ambos os projetos compilam com 0 erros (`npm --prefix site run build`) e executar a suíte de validação automatizada `python scripts/portfolio_qa_sentinel.py`.

---

## 5. Protocolo de Redação Técnica Documental (Plain Language, Zero Jargão & Estrutura STAR)
- **Tom Estritamente Factual, Direto e Simples:** Proibição absoluta de linguagem publicitária, superlativos ou clichês corporativos. O texto deve ser simples, acessível e claro para qualquer profissional ou stakeholder de negócio, explicando o projeto com naturalidade técnica, sem jargões herméticos ou pedantes.
- **Fornecimento de Dados Brutos (Estrutura STAR):** Toda narrativa deve se ancorar exclusivamente em dados técnicos brutos estruturados (Situação, Tarefa, Ação Técnica e Resultado Concreto), sem suposições, floreios ou narrativas romanciadas.
- **Geração Modular (Seção por Seção):** A redação deve ocorrer bloco a bloco (Visão Geral ➔ Discovery ➔ Decisões de UI/AI/Acessibilidade ➔ Escopo ➔ Métricas), garantindo densidade técnica e profundidade uniforme.
- **Lista de Exclusão Estrita (Negative Prompting — validada em código no Gate 15 do Sentinel):** É proibido utilizar: *"interface amigável"*, *"experiência fluida"*, *"mergulhar no problema"*, *"colocar o usuário no centro"*, *"no centro da decisão"*, *"design limpo/clean"*, *"cabeçalho limpo"*, *"colunas limpas"*, *"visual bonito"*, *"sem poluição visual"*, *"disruptivo"*, *"sinergia"*, *"revolucionário"*, *"incrível"*, *"inovador"*, *"inovações"*, *"divisor de águas"*, *"encantar o usuário"*, *"experiência mágica"*, *"double diamond"*, *"mapa de empatia"*, *"reimaginar"*, *"transformar"*, *"transformação"*, *"ajudo empresas a"*, *"estreita colaboração"*.
- **Painel Obrigatório de Personas Sintéticas:** Antes de propor ou aprovar qualquer copy, estrutura ou decisão de UI relevante, simular explicitamente o parecer de 3 personas sintéticas (**Recrutadora Sênior em triagem de 10s**, **Head of Design avaliando senioridade/decisão** e **UX Writer de Plain Language**) para eliminar opções inferiores e entregar a recomendação vencedora fundamentada.
- **Substituição por Engenharia de Design e Princípios Gestalt:**
  - Em vez de adjetivos vagos, descrever: **heurísticas de usabilidade (Nielsen)**, **princípios Gestalt (região comum, proximidade)**, **tokens de Design System (espaçamento 8px, tipografia)**, **critérios de conformidade WCAG 2.2 AA/AAA**, **arquitetura da informação**, **contratos de dados** e **Product Discovery**.
- **Vocabulário Técnico Canônico (Otimização para Lideranças & ATS):**
  - *Human-Centered Design (HCD)*, *Product Discovery*, *Arquitetura da Informação*, *Design System Modular*, *Tokens Semânticos*, *Heurísticas de Usabilidade*, *WCAG 2.2 AAA*, *Taxonomia de Dados*, *Interoperabilidade Legada*, *Modelagem de Componentes*, *Custo Efetivo Total (CET)*.
- **Mandato para o Plugin do Figma:** O gerador de telas do plugin deve seguir compulsoriamente estas regras em todos os textos de cases, capítulos, cards e callouts, garantindo redações de fácil compreensão, sem jargões vazios e com máximo rigor técnico.


---

## 6. Diretrizes Canônicas Senior UX (UX Companion 2026)
Consolidação das regras de ouro de *Senior UX Portfolio Examples* e *20 UX Portfolio Mistakes*:
- **Decisões como Unidade de Valor:** Todo case deve conter no mínimo 3 decisões técnicas documentadas (Gatilho ➔ Alternativas Consideradas ➔ Trade-off Aceito ➔ Restrição Operacional ➔ Validação). Métodos e processos não substituem decisões.
- **Sinalização Sênior Acima da Dobra:** Cargo ("Senior Product Designer"), anos de experiência e domínios essenciais visíveis nos primeiros 5 segundos da Home e no topo de cada case.
- **Disciplina de Escopo ("O Que Não Foi Construído"):** Explicitar o escopo deliberadamente cortado e as justificativas técnicas/negociais.
- **Enfrentamento de Desacordo Construtivo:** Relatar com maturidade divergências com engenharia ou liderança de produto e como a resolução foi alcançada.
- **Reflexão Crítica Obrigatória:** Todo case deve encerrar com "O que eu faria diferente hoje / Trade-offs residuais".
- **Eliminação de Vícios de Portfólio:** Proibido culto a processos genéricos (Double Diamond sem contexto), mosaicos de post-its/personas, métricas fictícias sem baseline ou pronomes vagos ("nós fizemos" sem especificar autoria individual).
- **Proporção Única de Evidência:** Hero e figuras de entrega sempre em proporção 16:9 singular em alta resolução (1152×648 ou 856×482), eliminando mosaicos de telas miniaturizadas.
- **Documento Normativo Completo:** Consulte [SENIOR_UX_PORTFOLIO_CANON.md](file:///c:/Users/Israel%20Rozar/Documents/ChatGPT/Portfolio/SENIOR_UX_PORTFOLIO_CANON.md) para a especificação detalhada de cada pilar e bloco.





## 7. Proteção de Acesso Padrão nos Cases (Modelo Híbrido)
- **Home Aberta, Cases Protegidos por Padrão:** A Home (`/`) permanece aberta para conversão de recrutadores; todos os estudos de caso (atuais e futuros) que utilizam `CasePresentation` herdam automaticamente o componente `CaseAccessGate` (`site/src/components/CaseAccessGate.tsx`).
- **Segurança no Código:** A senha **nunca** deve ser gravada em texto claro no código-fonte, em documentação pública ou no bundle (`dist/`). A validação ocorre exclusivamente por comparação de hash **SHA-256**, com desbloqueio persistido apenas em `sessionStorage` para navegação contínua durante a sessão.


## 8. Gate Permanente de Efetividade & Pré-Publicação — UX Companion (2026)
- **Dupla Governança Obrigatória (Efetividade + Completude):**
  1. **Review Scorecard (`/30`):** avaliar nas 6 seções de [UX_PORTFOLIO_REVIEW_CHECKLIST_2026.md](file:///c:/Users/Israel%20Rozar/Documents/ChatGPT/Portfolio/docs/v3_6_novembro_25_craft/UX_PORTFOLIO_REVIEW_CHECKLIST_2026.md) (*Homepage, Navigation, Case Studies, Presentation, Mobile, Credibility*), mantendo **meta mínima `>= 27/30`**.
  2. **Pre-Publish Checklist 35 Pontos (`https://uxcompanion.co.uk/ux-portfolio-checklist`):** executar antes de toda release relevante nas 5 categorias (*Homepage 6, Case Studies 8, Presentation 7, Mobile 6, Technical Hygiene 8*), mantendo **meta `>= 95%` (`34/35`, considerando a exceção formal registrada em ADR para `t-1` domínio próprio em favor de `github.io`)**:
     - **Prosa & Tipografia (`p-1`–`p-3`):** corpo `16–18px` (`line-height 1.5–1.75`), comprimento máximo de linha **`65–75ch`** em parágrafos corridos, 1 família tipográfica disciplinada.
     - **Performance (`p-4`–`p-5`):** imagens comprimidas em WebP/AVIF no tamanho de exibição e **Hero LCP `< 2.5s`**.
     - **Anotação com Racional (`cs-5`):** telas finais e legendas devem explicar o **porquê da decisão**, não apenas descrever o layout.
     - **Higiene Técnica (`t-2`–`t-8`):** SSL válido, `0` links quebrados/404, `<title>` específico por rota, **Open Graph / `og:image` / `canonical` estáticos apontando para a URL real de produção (`https://israelfull-commits.github.io/portfolio/`)**, CV em PDF com nome legível, zero botões de edição expostos e revisão ortográfica completa.
- **Regra de Camada de Linguagem (Home vs. Cases):**
  - **Home (Hero, Cards, Sobre, Contato):** **100% Plain Language** — posicionamento de 1 linha compreensível em `< 10s` por RH e negócios, sem listas de termos em inglês ou siglas empilhadas.
  - **Dentro dos Cases:** termos técnicos (`Product Discovery`, `Design System`, `WCAG 2.2`, `contratos de dados`) aplicados apenas quando explicam uma ação ou decisão concreta.
- **Critérios Técnicos Automatizados no Sentinel (`portfolio_qa_sentinel.py` v2):**
  - Navegação principal com no máximo **4–6 itens** claros e contato acessível em toda página.
  - Corpo de texto legível (**`>= 16px`**), contraste mínimo **WCAG 2.2 AA/AAA**, alvos táteis `>= 44px` (`WCAG 2.5.8`), espaço em branco *outside-in* (Gestalt) e `0px` overflow em `1440px / 768px / 390px`.
  - **Screenshots reais acima de mockups decorativos:** qualquer acabamento de estúdio deve preservar **100% dos pixels reais das telas do Figma**, sem distorcer textos.
- **Documentação & Versionamento Contínuo:** Toda entrega deve atualizar automaticamente o changelog ativo em `docs/v3_6_novembro_25_craft/CHANGELOG_V3_6_CRAFT_EDITION.md` e o índice `docs/INDEX_GOVERNANCA_E_DECISOES.md`.


## 9. Sincronização Omnicanal Obrigatória (Git + Espelho Local + Notion Portfolio Ops)
Toda evolução, correção, auditoria ou nova versão do portfólio e dos cases **DEVE** ser sincronizada automaticamente em **todos os 4 pontos de verdade** antes de concluir a entrega, garantindo paridade 1:1 de versões, links, scores e decisões:
1. **Produção (`site/` → GitHub Pages `main`):** build com `0` erros (`npm --prefix site run build`), **12/12 PASS** no `python scripts/portfolio_qa_sentinel.py` e push para `origin/main`.
2. **Espelho Local (`portfolio-verde/`):** manter 100% sincronizado com `site/` (permanecendo ignorado no `.gitignore` raiz).
3. **Documentação Versionada no Repositório (`docs/`):** atualizar automaticamente `docs/v3_6_novembro_25_craft/CHANGELOG_V3_6_CRAFT_EDITION.md` e `docs/INDEX_GOVERNANCA_E_DECISOES.md`.
4. **Notion Portfolio Ops (`notion_notion` MCP):** manter atualizados sem sobrescrever histórico anterior:
   - **Hub Principal:** `https://app.notion.com/p/4168db39b34f805884bad8f933e004dd`
   - **Subpágina Consolidada V3.6:** `https://app.notion.com/p/4248db39b34f81a6b708c51aefce7209`
   - **Bases Relacionais:**
     - `🗂️ Ativos`: `collection://adee0322-c2a3-4666-a54c-47f837bd6496` (status e URLs publicadas)
     - `🔖 Versões`: `collection://e0c08f7f-825b-4340-9a67-54d165d4e05e` (nova linha semver + changelog + link)
     - `🔍 Diagnósticos`: `collection://68a1754f-2dd7-4fd1-9e12-14f49a05bf68` (auditorias Sentinel v2 / UX Companion)
     - `💡 Recomendações & Decisões`: `collection://6db1c32b-e538-4a31-8b88-c2964ed69c96` (ADRs e status de implementação)
     - `⭐ Scorecard Geral`: `collection://1636d9a7-c819-41e6-85af-92d091999523` (reavaliação a cada versão Major/Minor)
   - **Regra de Segurança no Notion:** nunca gravar senhas em texto claro em páginas ou propriedades do Notion; referenciar apenas a existência do gate SHA-256.


## 10. Paridade Estrita de Design System (Home ↔ Cases)
- **Paleta Única Semântica:** Home (`index.css`) e Cases (`case-presentation.css`) devem consumir os **mesmos tokens canônicos** de papel, verde-pinho, lima e tinta (proibição de duas paletas paralelas no mesmo site).
- **Escala Tipográfica Monotônica:** `h1 > h2 > h3 > body >= 16px` sem inversão nem sobreposição entre Home e Cases.
- **Grid Estrito de 8px:** paddings, gaps e ritmos verticais de seção devem ser múltiplos exatos de `8px` (`16 / 24 / 32 / 48 / 64 / 80px`), proibindo valores quebrados como `86.4px`, `28px` ou `36px`.
- **Unicidade de Componentes:** `.cp-figure` deve ter o mesmo tratamento visual em todos os contextos; nunca deixar 1 imagem órfã em grid de 2 colunas; Heroes `16:9` devem renderizar *edge-to-edge* (`aspectDiff = 0.0000`, zero faixas laterais).
- **Anti-Template de Bootcamp (Narrativas Sob Medida):** todos os cases compartilham o mesmo Design System (tokens, tipografia, grid 8px), mas **nunca** podem repetir os mesmos rótulos de capítulo, a mesma ordem nem a mesma contagem mecânica de seções. Cada case define seus próprios `id` e `tag` em `CaseChapter` conforme a natureza do problema (Sistema Clínico, Decision-Led Fintech, Unificação Multicanal, Service Design).


## 11. Higiene de Repositório & Catálogo de Scripts Canônicos
- **Scripts Canônicos Ativos (apenas 2):**
  1. `scripts/portfolio_qa_sentinel.py` — Sentinela unificado (14 gates estáticos + Chromium runtime + WCAG 2.2 + sync `portfolio-verde/`). Substitui todos os scripts `audit_*`, `verify_*` e `test_*` legados.
  2. `scripts/build_portfolio_figma_screens.py` — Compilador oficial do plugin Figma Desktop.
- **Proibição de Acúmulo na Raiz e em `scripts/`:** nunca salvar screenshots temporários (`.png`), arquivos `.gz`, dumps `.json` ou scripts descartáveis na raiz do repositório nem em `scripts/`. Todo artefato temporário de inspeção deve ficar no diretório de scratch da sessão (`<appDataDir>/brain/<conversation-id>/scratch/`) ou em `D:\mockups-portfolio-studio\`.
- **Zero Duplicidade Documental:** documentos históricos vivem exclusivamente em `docs/v1_*`, `docs/v2_*`, `docs/v3_*`, `docs/v3_5_*` e `docs/v3_6_*` — nunca duplicados na raiz.
- **Proveniência & Rastreabilidade Obrigatória (Figma + Docs):** toda prancha gerada no Figma (Home, Cases, Design System e Handoff via `use_figma` ou `scripts/build_portfolio_figma_screens.py`) e toda documentação canônica devem incluir explicitamente o bloco de Proveniência contendo: **IA/Plataforma** (`Antigravity — Google DeepMind`), **Data de criação**, **Última atualização** e **ID/Link da conversa** (`conversation://<conversation-id>`).
- **Regras Anti-Regressão do Figma (`REGRAS_PERMANENTES_DESIGN_FIGMA_2026.md`):** sempre zerar `fills = []` em containers estruturais após `figma.createAutoLayout()` (zero fundos brancos fantasma), chamar `resize()` antes de `primaryAxisSizingMode = 'AUTO'`, equalizar alturas de cards irmãos em grids horizontais, reutilizar componentes nativos (`SiteHeader`, `Provenance Banner`) e validar visualmente via `get_screenshot` antes de concluir.
