# Changelog & Histórico de Auditorias, Correções e Evoluções

Todas as intervenções, auditorias visuais e funcionais, correções de bugs, evoluções de design system e atualizações de conteúdo do **Portfólio de Israel Rozar** são devidamente documentadas neste registro cronológico, seguindo os padrões de rastreabilidade e governança de produto.

---













## [2026-11-14] — Paridade 1:1 com Figma 59:2, Citação Conceitual e Recorte Macro de Componente
* **Reordenação Canônica dos Capítulos 02 e 03:** Restabelecida a ordem original do Figma 59:2: o Capítulo 02 agora apresenta o *Cenário e Mandato* (restrições do Word, papel e sistemas legados), seguido pelo Capítulo 03 com a *Descoberta e Triangulação* (4 entrevistas, questionário e 80 laudos).
* **Citação Conceitual de Liderança (Capítulo 04):** Adicionado bloco de citação com destaque editorial e barra lateral verde (`.cp-quote`): *"Modular não é simplificar. É manter o contexto clínico no lugar onde a pessoa o espera."*
* **Recorte Macro de Componente (Capítulo 04):** Integrado espécime em alta resolução do módulo de exame (`hiae-componente-protrombina-crop.webp`, 1408×534px), demonstrando em tamanho 1:1 a anatomia estável dos componentes `DataField` e `ExamTitle`, valores numéricos e parâmetros de referência.
* **Sincronização Plena:** Atualizadas ambas as bases (`site/` e `portfolio-verde/`) com validação de build sem erros.

## [2026-11-14] — Auditoria e Otimização Estrutural do Case Einstein (/cases/einstein-laudos)
* **Ativação de Grid Comparativo em `.cp-gallery`:** Implementado grid de 2 colunas (`repeat(2, minmax(0, 1fr))` com gap de 24px) no desktop para as galerias do Capítulo 05. Isso permitiu a comparação direta lado a lado dos pares (*Original × Proposta Demonstrativa* e *Mamografia × Ressonância*), reduzindo o scroll vertical do capítulo de 4.444px para 2.786px (-1.658px de respiro).
* **Responsividade Aderente:** No mobile (`<= 768px`), as galerias colapsam automaticamente para 1 coluna fluida com gap de 20px, sem qualquer overflow horizontal.
* **Consistência de Tokens e Hierarquia:** Verificados os tokens oficiais 1:1 com o Figma (Nó 370:17047): `--cp-canvas` (`#FCF9F2`), `--cp-surface` (`#F6F3EC`), `--cp-pine` (`#0A3622`), `--cp-border` (`#EDE9DE`) e tipografia `Plus Jakarta Sans`.

## [2026-11-14] — Consolidação do Mockup de Alta Fidelidade no Case em Destaque (MacBook Pro 16" Retina)
* **Substituição de Print por Mockup de Hardware Apple:** Removido o antigo print de navegador com abas e barra de favoritos do Chrome, substituindo-o por um mockup de hardware autêntico do **MacBook Pro 16"** em acabamento de estúdio fotográfico.
* **Interface Clínica 100% Limpa e em Alta Definição:** Inserida a proposta demonstrativa de alta fidelidade do laudo clínico modular (`hiae-mockup-macbook-retina.webp`, 2400×1400px), sem qualquer barra de navegador, abas ou anotações invasivas de auditoria.
* **Proporção Geométrica e Prevenção de CLS:** Configurada a proporção nativa exata de 12:7 (`width="1200"` e `height="700"`), garantindo renderização instantânea sem deslocamento cumulativo de layout (Cumulative Layout Shift = 0).
* **Paridade Plena e Sincronização:** Atualizadas ambas as bases de código (`site/` e `portfolio-verde/`) com builds validados e 0 erros.


* **Evidência Visual da Proposta Anotada:** Integrado o preview visual de alta resolução do laudo modular (`/images/hiae-estado-proposto-anotado-preview.webp`) na coluna da direita do card em destaque, comprovando instantaneamente a entrega de Design System e arquitetura clínica.
* **Badges e Narrativa de Liderança Reforçados:** Atualizado o cabeçalho para `★ Case em destaque · Saúde` e refinada a narrativa para evidenciar o papel de UX Lead e o desafio de estruturar mais de 80 exames distintos.
* **Métricas de Discovery Integradas:** Os números de pesquisa (`14 famílias`, `121 pacientes`, `04 entrevistas`, `44 testes`) foram reorganizados em harmonia com a imagem e a assinatura de parceria (`Hospital Albert Einstein × Foursys Design`).
]

site/CHANGELOG.md

CHANGELOG.md

## [### 📄 Integração de Alta Conversão do Currículo no Hero e Header
* **Dupla de Alta Conversão no Hero:** Substituído o botão de saída prematura para o LinkedIn por `Baixar currículo (PDF) ⤓` com ícone SVG dedicado de download (`DownloadIcon`). A dupla `Conhecer meu trabalho ↓` (Primário) e `Baixar currículo (PDF) ⤓` (Secundário) atende perfeitamente os dois perfis centrais de visitantes (Hiring Managers e Recrutadores rápidos) sem sobrecarga visual (Hick's Law).
* **Currículo Permanente no Header Superior:** Incluído link direto para download do currículo na barra de navegação desktop (`Cases · Expertise · Trajetória · Currículo · Entrar em contato →`), eliminando a duplicação anterior do link "Contato" e garantindo acesso ao PDF em qualquer scroll.
]

site/CHANGELOG.md

CHANGELOG.md

## [### 💬 Refinamento da Seção de Contato e CTAs dos Cases
* **Substituição do "04" na Seção de Contato:** Removido o número sequencial `04` da área de contato, eliminando a colisão com o Card 04 do Itaú. Implementada a tag em cápsula com ícone de diálogo elegante em SVG (`💬 CONTATO`).
* **Botão de E-mail com Ícone de Envelope:** Atualizado o botão de ação principal com o ícone de envelope SVG (`Enviar um e-mail ✉`), garantindo maior affordance visual e clareza de canal.
* **Agrupamento dos Links Secundários:** Links de apoio organizados com bullets separadores (`•`), facilitando o escaneamento horizontal (`Baixar currículo (PDF) • LinkedIn • GitHub`).
* **Evolução do Microcopy dos CTAs:** Substituído `Ler case completo →` por `Explorar o case →` em todos os cards e `Explorar estudo de caso completo →` no case de destaque (Einstein), reduzindo o atrito cognitivo percebido e prometendo a imersão nos artefatos visuais e funcionais internos.
]

site/CHANGELOG.md

CHANGELOG.md

## [### 🏆 Consolidação Definitiva da Opção C e Eliminação de Redundâncias
* **Consolidação Editorial Permanente:** Removido o componente de abas temporário (`pf-layout-switcher`) após aprovação da Opção C, fixando o grid no modelo editorial sênior limpo.
* **Eliminação de Redundância Quádrupla:** Removida a linha `Meu papel: Product Design` repetida em todos os 4 cards, permitindo que a competência técnica em cada projeto seja expressa pelo tema (`Arquitetura da informação`, `Discovery e visão sistêmica`, `Fluxos e operação em lote`, `IA aplicada à operação`).
* **Paridade no Card 04:** Removida a nota autodepreciativa obsoleta sobre "telas não incorporadas", e padronizado o CTA para `Ler case completo →`, alinhando 100% dos cards ao mesmo padrão de qualidade.
* **Nivelamento Subpixel Perfeito:** Ajustada a altura de `.pf-project-heading` para 94px, eliminando o desvio anterior de 10px entre títulos de 1 e 2 linhas. Todas as descrições agora iniciam exatamente em `top = 1694px` (variação 0.0px).
* **Limpeza de Código Morto:** Removidas propriedades `focus` não utilizadas e estado desnecessário `useState` em `Home.tsx`.
]

site/CHANGELOG.md

CHANGELOG.md

## [### 💎 Integração da Opção C (Editorial Sênior sem Miniaturas na Home)
* **Adição da Opção C no Switcher Interativo:** Incluída a terceira modalidade no controle de alternância da Home (`Opção C · Editorial Sênior (Sem Miniatura)`), permitindo inspecionar os cards Itaú com foco 100% tipográfico na decisão e no problema, com altura compacta de ~350px.
* **Carrossel Comparativo Triplo:** Atualizado o artefato `COMPARATIVO-A-B-LAYOUT-CARDS-ITAU-2026-11-14.md` com as 3 opções para comparação lado a lado.
]

site/CHANGELOG.md

CHANGELOG.md

## [### 🔀 Implementação de Comparador Interativo A/B dos Cards Itaú
* **Controle de Alternância em Tempo Real:** Criado o componente de switcher de abas (`pf-layout-switcher`) acima do grid de projetos Itaú, permitindo alternar instantaneamente entre a Opção A (Contexto no Topo / Recomendada) e a Opção B (Imagem no Topo / Atual).
* **Artefato com Carrossel Comparativo:** Documentado formalmente em `COMPARATIVO-A-B-LAYOUT-CARDS-ITAU-2026-11-14.md` com capturas em alta resolução de ambas as abordagens para inspeção visual.
]

site/CHANGELOG.md

CHANGELOG.md

## [### 📐 Correção de Respiro e Padding Simétrico na Linha Divisória dos Cards
* **Diagnóstico e Resolução do "Texto Colado":** Identificada a sobreposição da regra global de reset `margin: 0` que anulava o espaçamento superior da divisória.
* **Padding Simétrico de 16px:** Implementado `padding-bottom: 16px` no parágrafo descritivo (`.pf-project-desc`) e `padding-top: 16px` no bloco de decisão (`.pf-project-decision`), garantindo exatamente 16px de respiro acima e 16px abaixo da linha divisória (`1px solid var(--line)`).
* **Harmonia Óptica:** O texto deixa de encostar na borda, restabelecendo o conforto de leitura e o agrupamento visual de Gestalt.
]

site/CHANGELOG.md

CHANGELOG.md

## [### 🛡️ Auditoria Visual Total, Resolução da Proximidade Gestalt e Checklist Operacional
* **Resolução da Quebra de Proximidade (Cards 1 a 3):** Removido `min-height` da tag `<h3>` e criado o contêiner semântico `.pf-project-heading` com `min-height: 130px`. O título e o tema/subtítulo voltam a ficar unidos (espaçamento de 6px), eliminando o vácuo artificial observado na imagem enviada pelo usuário.
* **Alinhamento do Topo do Hero:** Ajustado `.pf-hero` para `align-items: start`, alinhando a foto do autor com o início do bloco de texto e kicker da página.
* **Checklist Operacional e Relatório de Auditoria:** Documentado formalmente no artefato `CHECKLIST-AUDITORIA-GESTAO-E-CORRECOES-2026-11-14.md` com matriz completa de coordenadas em pixels para cada seção.
]

site/CHANGELOG.md

CHANGELOG.md

## [### 📐 Calibração Geométrica e Alinhamento dos Cards de Projetos Itaú
* **Eliminação do Desvio de Linha de Base dos Títulos:** Definida altura mínima de 64px (`min-height: 64px`) para os títulos H3 dos cards, eliminando a quebra visual entre títulos de 1 e 2 linhas e nivelando milimetricamente as linhas de Tema, Papel, Descrição e Decisão no mesmo pixel (`y = 1935.9px`, `y = 1963.9px`, `y = 1995.9px` e `y = 2043.9px`).
* **Delimitação Gestalt da Decisão de Design:** Adicionada linha divisória sutil (`border-top: 1px solid var(--line)`) sobre o bloco de decisão (`.pf-project-decision`), separando visualmente o contexto do problema da contribuição estratégica do designer.
* **Eliminação do Vácuo no Rodapé:** Acomodação harmônica do link de ação (`Ler case completo →`) alinhado na base inferior dos 3 cards.
]

site/CHANGELOG.md

CHANGELOG.md

## [### 💎 Restauração e Refinamento dos 4 Cards de Expertise (Posicionamento)
* **Retorno ao Formato Modular em Cards:** Restaurado o formato de 4 cards em linha (`repeat(4, 1fr)` com gap de 24px) na seção 02 (Expertise / Posicionamento), com fundo branco sólido (`#FFFFFF`), bordas estruturadas (`1px solid var(--line)`), cantos de 16px e sombra suave de elevação.
* **Alinhamento dos Ícones e Tipografia:** Cada card apresenta o identificador de categoria à esquerda (`01 / DISCOVERY`), ícone vetorial SVG temático à direita (topo), título H3 com altura mínima de 52px (evitando desalinhamento óptico) e parágrafo de síntese.
* **Consistência de Família Morfológica:** Eliminação da lista plana em 2 colunas, restabelecendo a identidade visual de contêineres uniformes presente nos cases do portfólio.
]

site/CHANGELOG.md

CHANGELOG.md

## [### 🎨 Correção de Fundo e Consistência do Card 04 (Registros de Atendimento)
* **Eliminação do "Ghost Card":** Removido `background: transparent;` do seletor `.pf-project-partial`, aplicando o mesmo fundo branco sólido (`background: #fff`), padding (32px) e borda dos demais cards.
* **Harmonização com o Canvas:** O card 04 deixa de herdar o fundo off-white da página (`#FCF9F2`), integrando-se à mesma linguagem de contêineres dos cards 01, 02 e 03.
]

site/CHANGELOG.md

CHANGELOG.md

## [### ⚖️ Avaliação Comparativa de Versões e Harmonização Definitiva de Layout
* **Avaliação Crítica (site vs portfolio-verde):** Conclusão técnica e de design demonstrando que a versão `site/` (Porta 8443) é a base de produção definitiva e superior devido à arquitetura modular em React/TypeScript, páginas de case canônicas (Figma node `370:17047`), integridade editorial e SEO/Acessibilidade completos.
* **Harmonização do Grid de Projetos Itaú:** Incorporado a `site/src/portfolio.css` o grid 3+1 com 3 colunas de 368px (`repeat(3, minmax(0, 1fr))`) e card horizontal full-width de 1152px (`.pf-project-partial`), padding interno otimizado de 24px e badges lime.
* **Harmonização da Seção Expertise:** Atualizado `.pf-expertise-grid` para 2 colunas amplas de 556px com separadores editoriais (`border-top: 1px solid var(--line)`), eliminando caixas brancas com sombras artificiais e garantindo legibilidade perfeita para os 2 parágrafos de cada competência.
* **Verificação Automatizada via Playwright:** Validado alinhamento exato e proporções nos viewports desktop (1280px), tablet e mobile, com build limpo sem erros em 5.82s.
]

site/CHANGELOG.md

CHANGELOG.md

## [2026-11-14] — Auditoria Profunda, Paridade com Figma Nó 59:2 e Padronização de Evidências

### 🎨 Unificação Visual dos Cards da Home e Alinhamento de Expertise
* **Sincronia Literal de Navegação:** Rótulo da seção 02 atualizado de `02 / Posicionamento` para `02 / Expertise`, em paridade 1:1 com o item de menu do cabeçalho.
* **Cards dos Projetos com Thumbnail Visual:** Integração dos previews visuais (`pf-project-preview`) nos cards do Itaú na Home (`site/src/pages/Home.tsx` e `portfolio.css`), incluindo thumbnails autênticos em WebP, legendas técnicas, badges numéricos em verde-limão, papel e linha de decisão de design destacada.

### 🔍 Auditorias Concluídas
* **Auditoria de Paridade Visual e Editorial (Figma Nó `59:2`):**
  * Comparação profunda do nó canônico `VIGENTE • Einstein • Consumo de Resultados • Israel Rozar` contra a implementação React (`CasePages.tsx`).
  * Inspeção automatizada de títulos, subtítulos, métricas, limitações de pesquisa e hierarquia clínica.
* **Auditoria de Integridade de Ativos Visuais e Direção de Arte:**
  * Verificação das capas dos 8 cases editoriais contra a diretriz de **Evidências Reais**.
  * Reversão e eliminação de qualquer imagem sintética/3D/IA.
* **Auditoria de Rotas e Integridade de Execução (Vite/Playwright):**
  * Teste automatizado nas 9 rotas ativas (`/`, `/cases/einstein-laudos`, `/cases/claro-multicanal`, `/cases/neoenergia-conexao-digital`, `/cases/itau/movimentacoes`, `/cases/itau/hub-liquidez`, `/cases/itau/campanhas`, `/cases/itau/registros-atendimento`, `/cases/itau/vencimentos`).
  * Status: **100% HTTP 200 OK**, zero erros no console do navegador, CLS = 0.

### 🎨 Design & Direção de Arte
* **Padronização 16:9 em Alta Resolução (1600 × 900 px) com Evidências Autênticas:**
  * `site/public/images/hiae-capa-editorial-1600.webp` (240 KB): Extraído da documentação taxonômica do Design System hospitalar.
  * `site/public/images/claro-capa-editorial-1600.webp` (72 KB): Interface operacional de atendimento multicanal.
  * `site/public/images/neoenergia-capa-conexao-digital.webp` (77 KB): Identidade e entregáveis do programa P&D ANEEL Conexão Digital.
  * `site/public/images/itau-vencimentos-capa-1600.webp` (118 KB): Tela canônica do nó mestre Figma `582:12520`.
  * `site/public/images/itau-hub-liquidez-capa-1600.webp` (92 KB): Interface da solução do nó Figma `3:14068`.
  * `site/public/images/itau-movimentacoes-capa-1600.webp` (109 KB): Artefatos de discovery do nó Figma `1966:34105`.
  * `site/public/images/itau-campanhas-capa-1600.webp` (53 KB): Screenflow de configuração e gestão de campanhas.
  * `site/public/images/itau-registros-workflow-1600.webp` (83 KB): Diagrama da governança em 3 etapas com inteligência artificial assistida.
* **Novos Recortes Ideais de Evidência Técnica:**
  * **Einstein (Capítulo 4):** Adição de `hiae-ds-componentes-crop-1600.webp` documentando os tokens `DataField` e `ExamTitle` do Design System.
  * **Neoenergia (Capítulo 5):** Adição de `neoenergia-blueprint-crop-contrato-1600.webp` exibindo a jornada e os pontos de contato frontstage do Blueprint de Contratação.
* **Refinamento de Molduras em CSS Studio Frame:**
  * Atualização de `.cp-hero-visual` em `site/src/components/case-presentation.css` com borda de contenção de 1px (`rgba(23, 32, 25, 0.09)`), sombreamento multicamada e `backdrop-filter: blur(20px)` para evitar sangria de interfaces claras no fundo da página.

### ✏️ Conteúdo & Copywriting
* **Alinhamento dos 7 Capítulos do Case Einstein:**
  1. *Organizar resultados sem perder o contexto clínico.*
  2. *Uma hierarquia que funcione na tela e no papel.*
  3. *Do documento ao dado.*
  4. *Preservar relações entre resultado, referência e contexto.*
  5. *Uma estrutura comum para conteúdos diferentes.*
  6. *Clareza percebida e interpretação exigem avaliações distintas.*
  7. *Pesquisa, entregáveis e colaboração.*
* **Correções Textuais e de Pontuação:**
  * Removidos pontos e vírgulas indevidos (`Do documento ao; dado:` e `Decisões de; design:`).
  * Consolidação da amostra metodológica: `4 médicos especialistas`, `121 pacientes crônicos`, `14 categorias de laudos`.
  * Preservação explícita da nota: *"Amostras de métodos diferentes não se somam. O estudo de caso apresenta o contexto e os limites de cada evidência."*

### 🛠️ Correções e Arquitetura de Código
* **Home Page (`site/src/pages/Home.tsx`):**
  * Sincronização com o Figma Nó `370:16614` e adaptação mobile `375:366`.
  * Tipografia configurada para `Plus Jakarta Sans` como fonte principal, complementada por `DM Sans` e `Manrope`.
* **Acessibilidade e Menu Mobile (`site/src/components/SiteChrome.tsx`):**
  * Implementação de `Escape listener` para fechamento do menu modal móvel.
  * Adição de bloqueio de rolagem (`overflow: hidden`) no body enquanto o menu estiver aberto.
  * Gerenciamento de foco e restauração para o botão disparador.
* **Automação de Documentação:**
  * Criação do script `scripts/update_changelog.py` para registro automatizado de futuras alterações e auditorias.

---

## [2026-11-13] — Implementação da Nova Home e QA Visual

### 🚀 Novas Funcionalidades & Componentes
* Implementação da Home React 19 + Vite com `portfolio.css`, baseada no layout canônico do Figma `370:16614`.
* Criação dos cards de projeto com estados hover/focus aprimorados e metadados contextuais (papel, parceiros, período).
* Integração dos ícones vetoriais de expertise oficiais exportados do Figma.
* Adição de retrato tratado profissionalmente em WebP (`israel-rozar-treated-800.webp` e `480.webp`).

### 🔍 Testes & QA
* Validação via Playwright CLI em múltiplas viewports (320px, 390px, 768px, 1280px, 1440px).
* Verificação de ausência de overflow horizontal (`scrollWidth <= clientWidth`).
* Validação do download do currículo oficial em PDF (`israel-rozar-curriculo.pdf`).

---

## [2026-11-03] — Reestruturação Editorial dos Cases e Acessibilidade

### 📐 Estrutura Editorial
* Reorganização dos capítulos dos cases Einstein, Claro e Neoenergia na sequência lógica: Contexto → Discovery → Proposta → Validação → Fontes e limites.
* Implementação do componente compartilhado `CasePresentation.tsx` com navegação por sumário lateral (Sticky TOC).
* Conversão de todos os formatos legados de imagem (PNG/JPG pesados) para WebP otimizado.

### ♿ Acessibilidade (a11y)
* Atribuição de `role="group"` e `aria-label` para blocos compostos de evidência.
* Garantia de contraste mínimo de 4.5:1 em todos os textos sobre o fundo canvas (`#FCF9F2`).
* Exibição completa das especialidades no mobile, sem ocultação indevida de itens.

---

## [2026-11-02] — Auditoria Comparativa contra Figma Página 30 e Consolidação IFA

### 📋 Mapeamento e Auditoria
* Auditoria comparativa detalhada entre os fluxos da Página 30 do Figma e os cases do Itaú BBA (Vencimentos, Gestão de Campanhas, Movimentações, Hub de Liquidez).
* Consolidação das interfaces do Design System íon (`IfaTable`, `IfaPagination`, filtros e drawers).
* Remoção de mocks e protótipos desconectados, unificando os dados nas rotas `/cases/itau/*`.

