# Auditoria de qualidade do portfólio — 25/11/2026

## Escopo e método

Home e quatro cases principais: Einstein, Itaú Hub de Liquidez, Claro e Neoenergia. Revisão integrada de conteúdo, arquitetura da informação, interface, acessibilidade e implementação, com duas revisões independentes por agentes. A home compacta permanece preservada.

Referências: regras do projeto, SENIOR_UX_PORTFOLIO_CANON.md, CHANGELOG-EINSTEIN-DECISOES.md, componentes e fontes locais. Critérios de acessibilidade: [WCAG 2.2](https://www.w3.org/TR/WCAG22/). Scores de alternativas são avaliações heurísticas de adequação, robustez e custo; não representam pesquisa com usuários nem certificação.

## Achados e três alternativas por achado

### 1. Currículo com prefixo de endereço duplicado — P1, corrigido

Chamadas combinadas de Link e assetUrl duplicavam `/portfolio/`.

| Alternativa | Score | Justificativa |
|---|---:|---|
| **A. Resolução idempotente — aplicada** | 9,7 | Corrige todos os consumidores centralmente. |
| B. Usar caminhos brutos apenas no Link | 9,0 | Funciona, mas exige disciplina em cada chamada. |
| C. Adicionar propriedade de endereço resolvido | 7,5 | Amplia a API e mantém dois fluxos de resolução. |

### 2. Mistura de temas claro e escuro — P1, corrigido

Uma preferência escura alterava tokens secundários, enquanto a camada final mantinha superfícies claras.

| Alternativa | Score | Justificativa |
|---|---:|---|
| **A. Manter tema claro coerente — aplicada** | 9,8 | Preserva a identidade existente e elimina a combinação incompleta. |
| B. Desenvolver dois temas completos | 9,1 | Viável se houver demanda de produto; amplia manutenção e testes. |
| C. Repetir resets de todos os tokens | 8,0 | Resolve a cascata, mas conserva regras conflitantes. |

### 3. Foco pouco visível sobre verde — P1, corrigido

O contorno usava a mesma cor de superfícies destacadas.

| Alternativa | Score | Justificativa |
|---|---:|---|
| **A. Anel com duas cores — aplicada** | 9,6 | Mantém uma borda contrastante sobre fundos claros, verdes e lima; inclui cores forçadas. |
| B. Foco por superfície | 9,2 | Bom controle, com maior dependência dos containers. |
| C. Cor única alternativa | 8,0 | Simples, mas exige validar cada combinação. |

### 4. Fontes dependentes da raiz do domínio — P2, corrigido

As fontes passam a ser processadas no build, com referências e pré-carregamento consistentes.

| Alternativa | Score | Justificativa |
|---|---:|---|
| **A. Arquivos processados pelo build — aplicada** | 9,5 | Resolve prefixo, hash e cache sem mudar a tipografia. |
| B. Injetar a base nas declarações | 8,8 | Exige uma camada adicional de configuração. |
| C. Usar fonte do sistema | 7,6 | Robusto, mas altera a identidade visual. |

### 5. Reconhecimento tratado como facilidade de localização — P1, corrigido

No Einstein, 81,6% medem reconhecimento do documento. A conclusão anterior os descrevia como localização sem esforço.

| Alternativa | Score | Justificativa |
|---|---:|---|
| **A. Usar os indicadores exatos — aplicada** | 9,6 | Distingue reconhecimento, atenção e compreensão. |
| B. Síntese qualitativa entre os indicadores | 9,1 | Mais curta, mas menos explícita sobre os percentuais. |
| C. Remover a conclusão e manter o painel | 8,5 | Conserva os dados, oferecendo menos interpretação. |

### 6. Redução de tempo e prevenção clínica sem medida correspondente — P1, corrigido

O texto foi ajustado para descrever a organização e a finalidade das macroáreas, preservando o contexto clínico.

| Alternativa | Score | Justificativa |
|---|---:|---|
| **A. Descrever mecanismo e finalidade — aplicada** | 9,5 | Sustenta o valor da solução sem criar um efeito medido. |
| B. Descrever somente a ação de organização | 9,0 | Preciso, mas comunica menos sobre a finalidade. |
| C. Apresentar comparação temporal documentada | 8,3 | Depende da recuperação de um registro que contenha essa medida. |

### 7. Redução de TMA sem comparação apresentada — P1, corrigido

No Claro, o texto agora descreve a continuidade de taxonomia e confirmação entre canais.

| Alternativa | Score | Justificativa |
|---|---:|---|
| **A. Descrever paridade de estrutura — aplicada** | 9,5 | Contribuição observável, sem atribuir uma redução operacional não medida. |
| B. Descrever a sequência de consulta e confirmação | 9,0 | Concreto, com menos contexto multicanal. |
| C. Incluir TMA antes/depois documentado | 8,4 | Requer relatório operacional, período e população. |

### 8. Unidade ambígua do indicador 14 — P2, corrigido

O histórico local associa o número ao inventário EN-1 a EN-14. Resumo e painel passam a dizer “14 entregáveis documentados”, sem combinar entregáveis com famílias na mesma unidade.

| Alternativa | Score | Justificativa |
|---|---:|---|
| A. Usar famílias após confirmar a contagem no inventário | 9,4 | Exige demonstrar a correspondência de cada família. |
| **B. Usar entregáveis documentados — aplicada** | 9,0 | Vincula o número aos objetos EN-1 a EN-14 citados na fonte local. |
| C. Retirar o número e listar o inventário | 8,6 | Remove a ambiguidade, mas reduz a síntese do resumo. |

### 9. Campos completos de decisões não igualmente documentados — P2, pendência documental

As decisões do Hub têm títulos e descrições, mas nem todas explicitam alternativas, trade-off, restrição e validação. Não foram acrescentados acontecimentos ou alternativas por inferência.

| Alternativa | Score | Justificativa |
|---|---:|---|
| **A. Completar três decisões com registros recuperados — recomendada** | 9,5 | Cumpre o canon com rastreabilidade. |
| B. Aprofundar a decisão mais documentada | 9,1 | Melhora a narrativa, mas atende parcialmente à exigência de três decisões completas. |
| C. Tabela de alternativas documentadas | 8,7 | Facilita a comparação, desde que as fontes mostrem opções realmente consideradas. |

### 10. Cores comuns declaradas em camadas independentes — P2, corrigido no núcleo compartilhado

Canvas, superfície, bordas, verde e lima dos cases agora referenciam os tokens semânticos compartilhados; corpo e cabeçalho deixam de repetir parte dos valores literais. Cores específicas de artefatos continuam preservadas.

| Alternativa | Score | Justificativa |
|---|---:|---|
| **A. Aliases semânticos — aplicada** | 9,5 | Reduz divergência sem mudar a composição existente. |
| B. Migrar toda a camada visual de uma vez | 8,6 | Maior alcance, com risco de regressão desnecessário nesta revisão. |
| C. Verificar manualmente valores repetidos | 7,8 | Mantém o custo recorrente e permite novas divergências. |

### 11. Navegação isolada com área de interação pequena — P2, corrigido

Links de fontes e “Ver todos os projetos” receberam área mínima de 44px de altura; o destino de “Pular para o conteúdo” nos cases passou a receber foco explicitamente.

| Alternativa | Score | Justificativa |
|---|---:|---|
| **A. Ampliar alvos e corrigir destino de foco — aplicada** | 9,6 | Preserva rótulos e estrutura, com operação mais previsível. |
| B. Converter fontes em cartões | 8,2 | Aumenta área, mas acrescenta peso visual. |
| C. Manter alvos menores com espaçamento adicional | 7,9 | Pode atender exceções, mas oferece menor conforto de toque. |

### 12. Tipagem do ambiente de build ausente — P2, corrigido

A compilação visual funcionava, mas a checagem de tipos não reconhecia import.meta.env.

| Alternativa | Score | Justificativa |
|---|---:|---|
| **A. Referência aos tipos do ambiente — aplicada** | 9,8 | Corrige a causa sem desabilitar verificações. |
| B. Declarar interface local equivalente | 8,2 | Duplica definições mantidas pela dependência. |
| C. Ignorar os erros na checagem | 2,0 | Oculta o problema e enfraquece a manutenção. |

### 13. Validação com especialistas sem registro correspondente no Hub — P1, corrigido

A busca complementar localizou o inventário IFA de 01/11/2026, linhas 98–118, e o dataset em ItauPreparationCase.tsx. Ambos descrevem a interface e deixam o protocolo de validação pendente. O texto do Hub agora refere as regras apresentadas no artefato, sem atribuir uma validação histórica não registrada.

| Alternativa | Score | Justificativa |
|---|---:|---|
| **A. Descrever as regras do artefato — aplicada** | 9,6 | Preserva a informação verificável e corrige a atribuição. |
| B. Remover a frase sobre as regras | 8,8 | Preciso, mas perde contexto útil sobre a interface. |
| C. Manter validação mediante protocolo recuperado | 8,5 | Depende de uma fonte posterior com participantes, tarefas e resultados. |

O inventário aponta um histórico de alternativas no Figma, arquivo aASd7epPB9NlC0xIY53eOC, nó 1802:82. A referência local não descreve os motivos das escolhas; por isso não foi convertida em narrativa de trade-offs.

## Validações e checklist

- [x] Revisão independente de conteúdo e implementação por agentes.
- [x] Home compacta preservada; quatro projetos mantidos.
- [x] Dez combinações de página e viewport: cinco páginas em 1440px e 390px.
- [x] Nenhum transbordamento horizontal nessas combinações.
- [x] Um título principal por página e sete capítulos em cada case.
- [x] Nenhuma violação detectada pelo axe-core 4.10.3 nas regras WCAG A/AA selecionadas, incluindo WCAG 2.2 AA.
- [x] Preferência escura mantém o tema claro coerente.
- [x] Salto para conteúdo e abertura/fechamento da ampliação verificados no componente compartilhado, em desktop e celular.
- [x] Currículo com quatro links corretos sob `/portfolio/`, todos com resposta HTTP 200.
- [x] Fontes carregadas sob o prefixo de publicação.
- [x] Compilação dos dois projetos e checagem de tipos.
- [x] Sentinel: redação, ativos, números, navegação circular e rotas estáticas.
- [ ] Recuperar registros completos de alternativas, trade-offs e validação das decisões.
- [ ] Pesquisa com participantes reais e avaliação manual abrangente com tecnologias assistivas.

## Cenários de avaliação

Recrutador em leitura rápida: identificar cargo, experiência, projetos e contato. Liderança de design: aprofundar contexto, decisões e evidências. Leitor no celular: acessar os mesmos capítulos e ampliar figuras. Pessoa navegando por teclado: alcançar conteúdo e operar a ampliação. Estes são cenários de inspeção e testes automatizados, não personas validadas por pesquisa nem sessões realizadas com pessoas.

## Diagnóstico

O núcleo de apresentação e navegação ficou mais consistente, com correções verificáveis de endereços, tema, foco, fontes e precisão editorial. A preservação do sistema visual existente foi deliberada. O detector também sinaliza preferências estéticas, como família tipográfica e numeração de capítulos; elas não foram tratadas como defeitos porque pertencem à identidade e à estrutura já definidas no projeto.

Os testes automatizados não certificam conformidade integral AA/AAA, não avaliam todos os textos dentro das imagens e não comprovam compreensão ou redução de esforço com usuários reais. A revisão documental das decisões permanece uma necessidade específica; não foi substituída por narrativa inventada.
