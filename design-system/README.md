# Sistema visual do portfólio

Versão 1.1 — 13/11/2026. Escopo: página principal desktop e novas telas do portfólio. Este guia substitui orientações anteriores conflitantes sobre Newsreader e cores avulsas.

## Fontes de verdade

- Página principal: https://www.figma.com/design/YIHybVXPe0Hfmja1hAyzQZ/Template-portfolio?node-id=302-3152
- Paleta aprovada: https://www.figma.com/design/YIHybVXPe0Hfmja1hAyzQZ/Template-portfolio?node-id=304-4060
- Documentação visual: https://www.figma.com/design/YIHybVXPe0Hfmja1hAyzQZ/Template-portfolio?node-id=333-3
- Figma: usar estilos com prefixo `Portfolio v1 /`. Não modificar estilos antigos sem esse prefixo. A versão atual utiliza Plus Jakarta Sans; Newsreader não integra o sistema vigente.

## Tipografia

Família: Plus Jakarta Sans, fallback system-ui, sans-serif. Pesos 400, 600 e 700. Usar estilos locais, sem tamanhos avulsos.

| Estilo | Tamanho / entrelinha | Peso | Uso |
|---|---|---|---|
| Display | 64 / 70 px | 700 | Título da hero |
| Section | 40 / 48 px | 600 | Títulos de seção |
| Case | 32 / 40 px | 600 | Case em destaque |
| Title | 24 / 32 px | 600 | Empresas e títulos de cards |
| Card | 18 / 26 px | 600 | Especialidades |
| Lead | 20 / 30 px | 400 | Introdução da hero |
| Body | 16 / 24 px | 400 | Descrições |
| Small | 14 / 20 px | 400 | Datas e informação secundária |
| Action | 14 / 20 px | 600 | Ações e navegação |
| Label | 12 / 18 px | 600 | Categorias, tags e números de seção |
| Caption | 12 / 18 px | 400 | Notas e fontes |

Evitar caixa alta em frases, cargos e parágrafos. Rótulos curtos podem usar caixa alta. Não inserir quebras manuais para encaixar texto no desktop. Usar altura automática e conferir títulos longos. Na implementação, estilos visuais não substituem elementos HTML semânticos.

## Cores e aplicação

Usar exclusivamente os HEX do arquivo `tokens.json`. Superfícies: Canvas #FCF9F2, Subtle #F6F3EC, Card #FFFFFF e Elevated #EDE9DE. Texto: Primary #1A201C e Secondary #4A554E. Deep Pine #0A3622 ancora fundos e ações; Acid Lime #CEFF1A destaca ações e identificadores.

Lima requer texto Deep Pine, nunca branco. Sobre Pine, usar Canvas para texto principal; a variação secundária autorizada é Canvas a 76%. Texto Muted #7D8A82 não deve ser presumido acessível em qualquer tamanho/fundo: verificar contraste da combinação. Cores clínicas são reservadas a estados semânticos; não usar como decoração.

Não criar cinzas por aproximação. Não alterar fotografias para limitar seus pixels à paleta. Imagens raster são uma exceção ao inventário dos valores editáveis. Estados hover previstos nos tokens precisam ser implementados e testados.

## Layout e espaçamento

- Desktop de referência: 1280 px, margens laterais 64 px, conteúdo 1152 px.
- Seções principais: padding vertical 80 px. Hero e contato podem encerrar com 64 px. Cabeçalho usa densidade própria.
- Escala base: múltiplos de 4 px. Tokens principais: 4, 8, 12, 16, 20, 24, 28, 32, 40, 48, 56, 64, 80, 96.
- Categorias e títulos: 16 px. Título e descrição: 24 px em blocos narrativos; 20 px nos cards de especialidade.
- Blocos principais: gap 32 px. Grid 2 × 2: 24 px; cards de 564 px. Grid de quatro especialidades: 24 px; cards de 270 px.
- Distribuição entre extremidades: Space between, sem simular com gaps enormes. Medidas fracionárias calculadas por layout não são, por si, erros; tokens manuais devem ser inteiros.
- Texto acompanha a largura do pai; altura HUG. Filhos de auto-layout usam FILL quando apropriado. Não esconder transbordamentos de texto com clipping.

## Bordas, raios e elevação

| Padrão | Valor |
|---|---|
| Identificador pequeno | raio 4 px |
| Painel interno / estado | raio 12 px |
| Card de especialidade ou secundário | raio 16 px |
| Destaque e contato | raio 24 px |
| Botão e pill | raio 9999 px |
| Borda em superfície clara | 1 px #EDE9DE |
| Divisor sobre Pine | 1 px #114B31 |
| Elevação Raised | 0 8px 24px rgba(10,54,34,.05) |

Elevação é opcional, não universal. Cards planos podem usar apenas borda. Nunca duplicar sombras nem usar sombra preta avulsa. Header com blur é uma exceção funcional; não reproduzir blur como decoração em todos os cards. Uma forma pill não é uma elipse de raio inventado.

## Receitas de componentes

- Botão: Action, padding horizontal 20–24 px e vertical 12 px; pill; ícone com gap 8 px. Garantir alvo de interação suficiente na implementação.
- Card secundário de case: largura 564 px no grid desktop, padding 32 px, gap 16 px, raio 16 px, borda 1 px, sem sombra. Altura comum ao conjunto calculada pelo maior conteúdo; 360 px é referência do conteúdo atual, não limite universal.
- Destaque de case: 1152 px; raio 24 px; narrativa com padding 48 px; painel complementar independente; altura automática pelo maior bloco. Clipping apenas para cantos/imagens.
- Especialidades: padding 28 px, títulos alinhados em área de duas linhas quando necessário; descrições em 16/24 px.
- Trajetória: composição de duas colunas, gap 32 px; datas e cargos em Small/Label; divisores entre experiências. Não confundir datas com status ativo.
- Contato: card 1152 px, padding 48 px, título Section, corpo Body, ações agrupadas abaixo, separação por divisor Pine Surface.
- Retrato: largura contida na coluna, foto sem distorção, proporção de referência 4:5; etiquetas absolutas contidas na imagem. Metadados são Caption/Label, sem fonte de 10 px.

## Novas telas e manutenção

1. Começar pela página principal e pelo guia vigente, não por uma alternativa antiga.
2. Aplicar estilos de texto, cor e efeito existentes. Criar um novo token somente quando houver necessidade de uso recorrente e documentá-lo antes de replicar.
3. Reutilizar receitas; não tratar grupos soltos como componentes publicados. O arquivo possui estilos locais; não foi criada uma biblioteca publicada nem todos os padrões foram convertidos em componentes.
4. Validar títulos de uma, duas e três linhas; descrições curtas e longas; datas, acentos e nomes extensos. Conferir padding após cada alteração de conteúdo.
5. Revisar visualmente a tela em tamanho natural e verificar limites dos contêineres. Estilos corretos não garantem boa composição automaticamente.
6. Para mobile e tablet, empilhar colunas, manter altura automática e testar navegação. Margens de 24 px e hero 40/46 px são orientações iniciais, ainda não validadas em frames responsivos.
7. Testar contraste por combinação, zoom, foco, teclado e leitores de tela no site. Este guia não representa certificação WCAG.
8. Registrar versão/data e atualizar simultaneamente Figma, guia e tokens quando houver mudança de regra.

## Checklist de revisão

- [ ] Toda cor editável pertence à paleta; fotografia é tratada separadamente.
- [ ] Toda fonte é Plus Jakarta Sans e todo texto está vinculado a um estilo.
- [ ] Nenhuma sombra preta ou duplicada; elevações seguem Raised.
- [ ] Padding e gaps manuais seguem a escala; distribuição automática usa auto-layout.
- [ ] Raios correspondem à função do componente.
- [ ] Nenhum elemento não intencional ultrapassa o pai; textos não estão cortados.
- [ ] Conteúdo, links e estados de interação foram validados separadamente.
- [ ] Desktop, tablet e mobile foram verificados antes da entrega de implementação.

Garantia de consistência depende de aplicar esses padrões e repetir a verificação após cada edição. O guia documenta regras; não bloqueia alterações manuais futuras.
