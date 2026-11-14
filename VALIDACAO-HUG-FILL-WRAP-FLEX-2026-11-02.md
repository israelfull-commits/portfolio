# Validação de Hug, Fill, Wrap, Flex e Grid — 02/11/2026

## Escopo

Home e seis rotas de cases no site local. No Figma Design `YIHybVXPe0Hfmja1hAyzQZ`, os seis frames vigentes 59:2, 61:2, 60:2, 62:2, 63:2 e 64:2, totalizando 1.322 frames/componentes internos. Referências históricas não foram convertidas em versões vigentes.

## Correções feitas nesta rodada

- Oito blocos de metadados apresentavam altura insuficiente após a quebra do texto. A linha fixa dos seis grids foi convertida em flexível, com células em Hug na vertical.
- Onze painéis fechados no Figma mantinham conteúdo visível fora da área do painel. O conteúdo desses estados fechados foi ocultado, preservando o resumo visível e a camada original para edição.
- Altura dos painéis ajustada ao conteúdo; os limites dos frames externos foram recalculados.

Hug, Fill, Flex e Wrap são recursos válidos. A correção trata combinações incompatíveis e dimensões rígidas indevidas; não remove esses recursos indiscriminadamente.

## Resultado das verificações

- Figma: nos seis cases, zero contêineres de auto-layout com filhos visíveis fora dos limites, usando tolerância de 2 px para arredondamento.
- Figma: zero ciclos em que um eixo Hug dependia de um filho Fill no mesmo eixo.
- Figma: zero filhos Fill sem contêiner de layout na auditoria e nenhum corpo excedendo o frame externo.
- Site: 35 combinações verificadas — sete páginas nas larguras 320, 672, 960, 1024 e 1440 px. Nenhum overflow horizontal da página ou dos elementos internos visíveis analisados.
- Site: controles de expansão acionados nos seis cases a 320 px, sem overflow após a mudança de estado.
- Site: em 1024 × 360 px, índice lateral limitado a 296 px e rolagem interna funcional para 430 px de conteúdo.

O CSS vigente passou nessas verificações e não precisou de nova alteração nesta rodada. Assim, os três arquivos já conferidos entre código local e Make permanecem iguais. As correções novas foram feitas diretamente nos mesmos nós do Figma Design.

## Limites da conclusão

Os testes cobrem o conteúdo atual, as larguras e os estados indicados. Não equivalem a uma garantia sobre qualquer conteúdo futuro, qualquer redimensionamento arbitrário de um frame no editor ou todos os navegadores e dispositivos físicos. Frames de apresentação no Figma não reproduzem automaticamente os breakpoints de CSS. Alterações de conteúdo ou estrutura devem repetir essa validação.

A publicação pública e a falha de rede M8 da prévia do Make não foram alteradas por esta auditoria de layout.
