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
- **Lista de Exclusão Estrita (Negative Prompting):** É proibido utilizar: *"interface amigável"*, *"experiência fluida"*, *"mergulhar no problema"*, *"colocar o usuário no centro"*, *"design limpo/clean"*, *"disruptivo"*, *"sinergia"*, *"revolucionário"*, *"incrível"*, *"inovador"*, *"divisor de águas"*, *"encantar o usuário"*, *"experiência mágica"*, *"double diamond"*, *"mapa de empatia"*, *"reimaginar"*.
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


## 8. Gate Permanente de Efetividade — UX Portfolio Review Checklist (2026)
- **Scorecard Obrigatório (`/30`):** Toda evolução relevante do portfólio (novo case, reformulação de Home ou atualização visual) deve ser avaliada nas 6 seções do [UX_PORTFOLIO_REVIEW_CHECKLIST_2026.md](file:///c:/Users/Israel%20Rozar/Documents/ChatGPT/Portfolio/docs/v3_6_novembro_25_craft/UX_PORTFOLIO_REVIEW_CHECKLIST_2026.md) (*Homepage, Navigation, Case Studies, Presentation, Mobile, Credibility*), mantendo **meta mínima `>= 27/30`** (nível Sênior/Staff).
- **Critérios Técnicos Automatizados no Sentinel (`portfolio_qa_sentinel.py` v2):**
  - Navegação principal com no máximo **4–6 itens** claros e contato acessível em toda página.
  - Corpo de texto legível (**`>= 16px`**), contraste mínimo **WCAG 2.2 AA/AAA**, espaço em branco *outside-in* (Gestalt) e `0px` overflow em `1440px / 768px / 390px`.
  - **Screenshots reais acima de mockups decorativos:** qualquer acabamento de estúdio (luz, sombra, Bento Grid, perspectiva) deve preservar **100% dos pixels reais das telas do Figma**, sem distorcer textos.
- **Documentação & Versionamento Contínuo:** Toda entrega deve atualizar automaticamente o changelog ativo em `docs/v3_6_novembro_25_craft/CHANGELOG_V3_6_CRAFT_EDITION.md` e o índice `docs/INDEX_GOVERNANCA_E_DECISOES.md`.
