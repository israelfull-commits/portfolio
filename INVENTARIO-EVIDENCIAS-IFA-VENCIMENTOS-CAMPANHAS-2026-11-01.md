# Inventário inicial de evidências — IFA, Vencimentos e Campanhas

Data: 01/11/2026

## Objetivo

Organizar as fontes fornecidas para transformar explorações extensas de Figma em cases de portfólio verificáveis, sem confundir artefato de trabalho, hipótese, entrega e resultado.

## 1. Planejamento de iniciativas

Fonte: `klNiUiITLbgRMix1qdQprn`, nó `1398:16429`.

### O que demonstra

- Plano de atuação para IFA — Gestão de Liquidez.
- Horizonte documentado de 01/07/2026 a 30/09/2026.
- Cinco frentes: Extrato EA, Movimentações, DAV Open Finance, Vencimentos e Pesquisa com usuários.
- Decomposição por discovery do problema, discovery da solução, design, teste, especificação de acessibilidade e handoff.
- Dependências, cadência e visão de capacidade do trabalho.

### Uso editorial recomendado

Usar como evidência de atuação sistêmica e priorização, não como prova de implementação ou impacto. O frame completo é amplo demais para publicação direta; deve ser recortado em resumo das frentes, detalhamento de Vencimentos e cronograma/dependências.

## 2. Vencimentos — exploração, documentação e handoff

Fonte principal: `YHCO7Yb3QdKP0nW2ie0tYO`.

### Nós inspecionados

- `1074:17353`: fluxo detalhado de Vencimentos e Eventos Futuros, incluindo etapas, filtros, registros, estados e caminhos de sucesso/falha.
- `1074:2687`: versão consolidada do fluxo de handoff.
- `1074:69184`: referências de telas em produção, versão simplificada e componentes.
- `3:64880`: explorações de tabela, ações, detalhes, feedback e estados.

### O que demonstra

- Inventário do estado existente.
- Evolução por alternativas de menor e maior impacto técnico.
- Jornada de entrada, busca, priorização, visualização e ação.
- Estados vazios, carregamento, sucesso e falha.
- Organização para handoff e relação com componentes.
- Exploração de densidade informacional em ambiente financeiro B2B.

### Uso editorial recomendado

Vencimentos possui material suficiente para um case próprio, desde que o recorte editorial responda:

1. qual problema operacional foi observado;
2. quais restrições técnicas motivaram a versão simplificada;
3. qual decisão foi tomada entre as alternativas;
4. quais partes foram implementadas ou permaneceram em progresso;
5. qual contribuição individual pode ser afirmada.

## 3. Vencimentos — arquivo final

Fonte: `4ufyM9cFiNwi6i3UqPjBTo`, nó `1:2`.

O conector encerrou a leitura durante a captura. A fonte permanece registrada, mas ainda precisa de nova inspeção antes de qualquer afirmação editorial.

### Versão canônica mais recente — confirmação do autor em 02/11/2026

Fonte: `jifEQkL5yQAvfaXsSQtmrH`, nó `582:12520`, arquivo `Gestão de liquidez`.

Israel Rozar confirmou este nó como a **última versão da interface Vencimentos**. Essa confirmação substitui a seleção provisória feita a partir do protótipo completo do IFA.

Características verificadas na captura:

- título `Próximos Vencimentos`;
- abas `Vencimentos`, `Eventos futuros` e `Open Finance`;
- busca por cliente, agência e conta;
- filtros compactos por prazo/janela, status e valor;
- tabela com status, data/prazo, cliente, agência/conta, carteira, produto, valor e ação;
- ações de consulta ou edição variando conforme o estado;
- paginação e indicação do universo de 500 itens.

O conector não forneceu datas de criação ou última edição do nó. A autoridade temporal vem da confirmação direta do autor em 02/11/2026. As capturas `09`, `10` e `11` permanecem preservadas como estados/explorações anteriores e não devem representar a interface vigente.

Captura canônica: `output/figma/ifa-evidencias-2026-11-02/15-vencimentos-versao-canonica-582-12520.png`.

## 4. Campanhas IFA

Fonte: `YHCO7Yb3QdKP0nW2ie0tYO`, nó `3:2`.

### O que demonstra

- Visão geral e manutenção de campanhas.
- Criação e configuração.
- Processamento de base.
- Estados vazios, carregamento e erro.
- Edição, exclusão e ações administrativas.
- Explorações e screenflows extensos.

### Situação no workspace

Já existe conteúdo editorial em `site/src/pages/ItauPreparationCase.tsx` para Gestão de Campanhas, além de Movimentações e Hub de Liquidez. As rotas não estão registradas em `site/src/app/routes.tsx`; portanto, os links existentes na home podem terminar em 404 até a integração ser concluída.

## 4.1 Hub de Liquidez — interface da solução

Fonte: `jifEQkL5yQAvfaXsSQtmrH`, nó `3:14068`, arquivo `Gestão de liquidez`.

O autor identificou este nó como `Hub de liquidez (Interface da solução)` em 02/11/2026. A captura demonstra:

- total disponível agora, composto por Itaú e Open Finance;
- variação prevista, entradas e saídas;
- liquidez projetada para fim do dia, 7 dias e 30 dias;
- atualização explícita e ação para atualizar;
- proporção entre valores atuados e a atuar;
- lista de recursos por cliente priorizado;
- busca por cliente, agência/conta ou carteira;
- filtros por origem e faixas de valor;
- disponível agora, total projetado e status da atuação por cliente.

O conector não expôs data de criação ou última edição do nó. A classificação como interface da solução vem da confirmação direta do autor, e não deve ser ampliada automaticamente para `implantada`, `em produção` ou `com resultados comprovados`.

Permanecem pendentes: regra de priorização/ordenação, fórmula e reconciliação dos valores, contrato das fontes, validação operacional, autoria detalhada e estágio de implantação.

Captura: `output/figma/ifa-evidencias-2026-11-02/16-hub-liquidez-interface-solucao-3-14068.png`.

## 5. IFA — Protótipo completo e mapa mestre

Fonte: `aASd7epPB9NlC0xIY53eOC`, página inicial `0:1` (`Layout Paginas`).

### O que a estrutura confirma

- O arquivo funciona como mapa amplo do ecossistema IFA, e não como evidência isolada de uma única iniciativa.
- Há páginas dedicadas a `Vencimentos`, `Gestão de campanhas`, `Agrupador de Contas`, `Hub BackOffice`, `Produção Comercial`, componentes de chassi, documentação e source of truth.
- As jornadas estão organizadas por objetivos operacionais e gerenciais, incluindo avaliar cliente, fazer gestão da carteira, alinhar-se ao mercado, definir estratégia, priorizar clientes, recomendar, executar e aproximar.
- O arquivo também preserva abas em produção, visões gerenciais e operacionais, arquivos do projeto, biblioteca de ícones e explorações de Hub de Liquidez.

### Uso editorial recomendado

Este arquivo deve ser tratado como **fonte de contexto e navegação entre evidências**. Ele ajuda a:

1. localizar o frame final de cada iniciativa;
2. demonstrar a complexidade sistêmica e a integração entre jornadas;
3. validar nomenclaturas e relações entre módulos;
4. comparar exploração, produção e estado final;
5. evitar que telas de iniciativas diferentes sejam apresentadas como se pertencessem ao mesmo recorte.

O canvas completo não deve ser publicado como imagem principal: sua dimensão natural é `162570 × 52125 px`, o que torna textos e decisões ilegíveis quando reduzidos. Para o portfólio, devem ser extraídos frames canônicos individuais e, quando necessário, um mapa simplificado com destaques editoriais.

### Páginas relevantes já identificadas

- `664:309644` — Vencimentos
- `661:180876` — Gestão de campanhas
- `806:92714` — Agrupador de Contas
- `661:139948` — Hub BackOffice
- `801:80615` — Produção Comercial
- `663:137949` — Componentes CHASSI
- `40:91515` — IFA — Documentação Gerada
- `86:39649` — IFA — Source of Truth Components
- `1802:82` — alternativas de Hub Liquidez

### Base de conhecimento dos produtos

Nó: `2041:111285` — `KBS produtos`.

O nó reúne documentação em três níveis — detalhada, FAQ e resumo executivo — para oito frentes:

1. Sistema de Campanhas;
2. Mapeamento de Mercado;
3. Notificações de consentimentos/Open Finance;
4. Potencializador de clientes/insights;
5. Gestão de Vencimentos;
6. Acompanhamento de Movimentações;
7. Lançamentos Online (Cofrinho);
8. Gestão de Fluxo de Caixa.

Esses KBs passam a ser a fonte de apoio para compreender propósito, funcionalidades, regras de negócio, estados, permissões e restrições. Eles **não comprovam isoladamente autoria, participação individual, implantação ou resultados**; essas afirmações devem ser cruzadas com os arquivos de planejamento, explorações, handoff, telas finais e materiais fornecidos pelo autor.

Também foi identificada uma limitação de organização interna: os 24 frames usam repetidamente nomes genéricos como `Campanhas_Detalhado.md`, `Campanhas_FAQ.md` e `Campanhas_Resumido.md`, mesmo quando tratam de outros produtos. Para a curadoria do portfólio, a classificação será feita pelo título real do conteúdo, e não pelo nome da camada.

## 5.1 Extrato EA — discovery, proposta e gates

Fonte: `klNiUiITLbgRMix1qdQprn`, seção `1966:34105` — `Discovery Extrato EA · apresentação e materiais`.

### Estrutura encontrada

O material contém 20 quadros organizados em apresentação principal e apêndice de discovery:

1. capacidade a restaurar após o desligamento da EA;
2. lacuna operacional e impacto;
3. princípio de solução e preservação do contexto persistente;
4. três alternativas de arquitetura e recomendação condicionada;
5. fluxo progressivo de leitura e aprofundamento;
6. proposta de header + resumo complementar;
7. histórico de movimentações;
8. detalhe e composição;
9. estados e comportamento;
10. implicações técnicas e contrato de dados;
11. entrega por fatias verificáveis;
12. decisões, responsáveis e próximos gates;
13–20. limite de confiança, escopo, usuários, arquitetura da informação, dicionário financeiro, exceções, validação/reconciliação e Definition of Done.

### Achados verificáveis

- A capacidade perdida é descrita como acesso a saldo provisionado, CEP de 10 dias sem juros e limite total disponível.
- O problema inclui consulta incompleta, troca de contexto, fontes paralelas e risco de orientação inconsistente.
- Três alternativas são comparadas: expandir o header, criar resumo em Movimentações ou introduzir atalho global.
- A alternativa B — resumo em Movimentações — aparece como recomendação **condicionada** à homologação de semântica, fonte e atualização.
- O fluxo proposto progride de header persistente para liquidez/limites, histórico e detalhes/composição.
- O próprio material separa confirmado, inferido, desconhecido e contraditório, e afirma que desconhecido não deve virar requisito.
- O status apresentado é de prontidão condicionada: desenvolvimento somente após gates P0 homologados; não há comprovação de produção ou resultado.

### Controle temporal e de versão

O conector expôs a estrutura e o conteúdo dos nós, mas **não forneceu data de criação, última edição ou histórico de versões da seção**. A data `22/07/2026 16:03` encontrada em uma tela pertence ao conteúdo demonstrativo da interface e não pode ser usada como data do arquivo. Portanto, esta fonte fica classificada como `cronologia não confirmada` até comparação com histórico do Figma ou artefatos locais datados.

### Comparação com o site de discovery

Fonte complementar: `https://ifa-movimentacoes-redesign.irozar.chatgpt.site/#discovery`.

O site declara no próprio conteúdo: `Documento vivo · Escopo: Extrato EA · revisão profunda · 21 jul. 2026`. O navegador retornou `document.lastModified = 02/11/2026 00:29:34`, mas esse valor pode refletir a resposta/publicação do servidor e **não comprova** quando o conteúdo de discovery foi criado ou aprovado. A data editorial declarada e o timestamp técnico devem permanecer separados.

#### Divergência de decisão encontrada

- Apresentação Figma `1966:34105`: alternativa B — **resumo em Movimentações** — aparece como recomendação para o cenário, condicionada à homologação.
- Site de discovery: registra como alternativa ideal mais recente **saldo provisionado no header**, mantendo CEP, CEP Plus e limite no contexto de Movimentações; também informa que falta registrar aprovador e decisão final.

Consequência: os materiais representam estados diferentes da decisão e não podem ser combinados como uma única solução final. Até recuperar histórico, aprovador e data da mudança, a classificação correta é:

- `resumo em Movimentações` — recomendação documentada em uma apresentação, versão temporal não confirmada;
- `provisionado no header + limites em Movimentações` — hipótese mais recente segundo o documento vivo de 21/07/2026, ainda em validação e sem decisão final formal.

#### Confirmação do autor — 02/11/2026

Israel Rozar confirmou diretamente a decisão vigente:

> O saldo provisionado é necessário em diferentes jornadas; deve permanecer visível sem exigir troca de aba. CEP, CEP Plus e limite continuam contextualizados em Movimentações.

Com essa confirmação, a classificação editorial passa a ser:

- **solução definida:** saldo provisionado transversal no header;
- **contexto complementar:** CEP, CEP Plus e limite total em Movimentações;
- **alternativa histórica:** concentrar o resumo completo em Movimentações;
- **pendências que permanecem:** registro histórico da aprovação, responsáveis, contrato dos dados, semântica financeira, validação operacional e evidência de implantação.

A confirmação do autor resolve qual foi a solução definida e qual proposta deve orientar a narrativa. Ela não deve ser rebaixada a hipótese ou alternativa candidata. Permanecem como comprovações separadas o registro documental da aprovação, o estágio de implantação e os resultados.

### Nó demonstrativo do discovery

Fonte: `klNiUiITLbgRMix1qdQprn`, nó `1926:38396` — `Container (Starter Project)`.

O nó reproduz uma versão longa do discovery dentro do Figma e deve ser classificado como **artefato demonstrativo/intermediário anterior à definição**, não como fonte vigente da decisão. Evidências do próprio conteúdo:

- título `JIP + Ways of Working 2.1 · discovery limitado`;
- estado `Em validação` e `Decisões financeiras e de dados ainda abertas`;
- recomendação para não declarar a capacidade restaurada antes da homologação;
- saldo provisionado no header e CEP/CEP Plus/limite em Movimentações aparecem como alternativas candidatas;
- meta e baseline permanecem a definir;
- texto final identifica `versão demonstrativa do discovery`.

#### Posição na cronologia editorial

O conector novamente não forneceu criação, última edição nem histórico do nó. Pela semântica do conteúdo, ele representa um estágio anterior à confirmação direta do autor em 02/11/2026, porque ainda rotula a arquitetura como candidata. A cronologia técnica continua sem timestamp comprovado, mas o status editorial foi esclarecido pelo autor: a solução foi definida como provisionado no header, com CEP, CEP Plus e limite em Movimentações.

Captura privada: `output/figma/ifa-evidencias-2026-11-02/14-extrato-ea-discovery-demonstrativo.png`.

#### Informações adicionais do site

- Estado do discovery: `Em validação`.
- Confirmado: problema, objetivo, desligamento da EA, perda da capacidade e três saldos já persistentes no header.
- Pendente: semântica financeira, contrato da fonte, validação operacional, aceite e governança.
- A restauração é explicitamente bloqueada até fechar os gates P0.
- São comparadas seis alternativas, não apenas as três resumidas na apresentação.
- Baseline, metas, amostra, tolerância e métricas quantitativas permanecem a definir.
- O site identifica uma inconsistência crítica: “posição líquida” e valor negativo aparecem no protótipo, mas a regra financeira continua desconhecida.

### Restrições de publicação

Algumas telas incluem nome completo, CPF e dados bancários. Até confirmação explícita de que esses dados são fictícios ou autorização de uso, esses frames não devem ser publicados sem substituição/anonimização. A captura geral serve apenas para auditoria privada.

## 6. Evidências locais encontradas

- `site/src/pages/ItauPreparationCase.tsx`
- `figma-make-reference/wu8RFWqSsQKt4SgrBqgGEf/src/pages/ItauPreparationCase.tsx`
- `figma-make-reference/wu8RFWqSsQKt4SgrBqgGEf/EXTRACTION-REPORT.md`
- `output/playwright/amity-source/INVENTARIO-VISUAL.md`
- `AUDITORIA-RECRUTADORES-UX-UI-COPY-2026-11-02.md`

### Chats e projetos do Codex triados

- `019fe47b-8a1e-79c2-8652-4674dd37e2d7` — **Analisar arquivo Figma IFA (2)**. Contém auditorias e governança da reconstrução iDS, matrizes de evidência, classificação de component sets e relatórios salvos em `C:\Users\Israel Rozar\Documents\Codex\2026-07-20\ifa-movimenta-es-redesign-ux-sites\outputs`.
- `019f361b-fdad-72e2-89bc-72c5dc9345e0` — **Analisar specs de acessibilidade**. Apesar do título, os turnos recentes incluem reconstrução, organização e polimento do screenflow de Gestão de Campanhas, com uso de componentes iDS, estados, ausência de sobreposições e nós Figma identificados.
- `019e576f-a06b-73b1-89c8-224932fd0249` — **Explorar projeto a fundo**. Registra evolução do catálogo/componentes iDS, tokens, ícones oficiais, responsividade, testes e correções no projeto `C:\Users\Israel Rozar\Music\IFA`.
- `019ee6a5-bef6-7831-a280-1ac20d64e435` — chat do projeto `C:\Users\Israel Rozar\Desktop\IFA`. Registra auditoria do orquestrador, componentes, Web Components e validações, mas parte do histórico recente é operacional e não deve entrar diretamente na narrativa dos cases.
- `019f7dff-36fd-78f1-8532-d0baa3b23bc2` — **Analisar arquivo Figma IFA - iDS Consolidated Library**. O histórico contém ao menos um turno grande demais para leitura pelo conector; permanece indexado para consulta pontual, sem inferências editoriais ainda.

#### Critério de uso

Chats servem para localizar decisões, experimentações, artefatos e caminhos de arquivos. Eles não serão usados sozinhos para afirmar impacto, autoria ou implantação. Informações aproveitáveis devem ser confirmadas em pelo menos uma fonte primária: arquivo Figma, código, relatório, teste, documento de projeto ou material fornecido pelo autor.

## 7. Capturas preservadas

Pasta: `output/figma/ifa-evidencias-2026-11-01/`

- `01-planejamento-iniciativas.png`
- `02-vencimentos-exploracao-a.png`
- `03-vencimentos-exploracao-b.png`
- `04-vencimentos-exploracao-c.png`
- `05-vencimentos-exploracao-d.png`
- `06-campanhas-screenflow.png`
- `07-ifa-prototipo-completo.png`
- `08-kbs-produtos-itau.png`
- `09-vencimentos-canonico-a.png` — estado de carregamento
- `10-vencimentos-canonico-b.png` — ausência de resultados
- `11-vencimentos-canonico-c.png` — eventos futuros com dados
- `12-vencimentos-documentacao.png` — comparação documental de versões

## 8. Próxima execução recomendada

1. [Concluído para o primeiro lote de Vencimentos] Extrair frames individuais canônicos, evitando screenshots de páginas inteiras.
2. [Em execução] Separar AS IS, exploração, decisão, handoff e estado final.
3. Remover placeholders, versões descartadas e anotações internas sem valor narrativo.
4. Confirmar autoria, colaboração e estágio de cada iniciativa.
5. [Dossiê controlado implementado] Criar primeiro o case de Vencimentos, que apresenta a cadeia de evidências mais completa.
6. Refinar e ativar o dossiê de Campanhas somente após selecionar os frames canônicos.
7. Revisar confidencialidade antes de publicar qualquer tela com dados operacionais.

