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

## 5. Protocolo de Redação Técnica Documental (Zero Jargão / Estrutura STAR)
- **Tom Estritamente Técnico e Direto:** Proibição absoluta de linguagem publicitária, superlativos ou clichês de autoajuda corporativa.
- **Lista de Exclusão Estrita (Negative Words):** É proibido utilizar: *"interface amigável"*, *"experiência fluida"*, *"mergulhar no problema"*, *"colocar o usuário no centro"*, *"design limpo/clean"*, *"disruptivo"*, *"sinergia"*, *"revolucionário"*, *"incrível"*, *"inovador"*, *"divisor de águas"*.
- **Substituição por Métricas e Padrões de Engenharia de Design:**
  - Em vez de adjetivos vagos, descrever: **heurísticas de usabilidade (Nielsen)**, **tokens de Design System (espaçamento 8px, tipografia)**, **critérios de conformidade WCAG 2.1/2.2 AA/AAA**, **arquitetura da informação**, **contratos de dados** e **Product Discovery**.
- **Vocabulário Técnico Canônico (Otimização para Lideranças & ATS):**
  - *Human-Centered Design (HCD)*, *Product Discovery*, *Arquitetura da Informação*, *Design System Modular*, *Tokens de Espaçamento*, *Heurísticas de Usabilidade*, *WCAG 2.2 AAA*, *Taxonomia de Dados*, *Interoperabilidade Legada*, *Modelagem de Componentes*.
- **Estruturação STAR por Seção:** Toda seção deve se basear exclusivamente em fatos e restrições verificáveis (Situação, Tarefa, Ação Técnica e Resultado Concreto), sem suposições ou floreios.


