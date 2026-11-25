# Autofix da página 30:2 — 02/11/2026

Destino solicitado: [página 30:2 do Template portfolio](https://www.figma.com/design/YIHybVXPe0Hfmja1hAyzQZ/Template-portfolio?node-id=30-2).

Foram inspecionados e corrigidos os dez layouts existentes nessa página: Registros e IA, Movimentações, Hub de Liquidez, Visão Geral, Gestão de Campanhas, Gestão de Incentivos, On Demand, Expansão B2B2C, Arquitetura e qualidade e Einstein — Laudos. A página mantém sua identificação como referência anterior; não substitui a página de cases vigentes 67:2.

## Principais problemas identificados

1. Textos dos links do índice tinham a largura total do link além do espaço já ocupado pelo número, ultrapassando o limite horizontal.
2. Linhas de grid mantinham dimensões capturadas que não acompanhavam o conteúdo. Colunas, métricas e textos de descoberta se sobrepunham ou ultrapassavam os limites; outros blocos deixavam vazios excessivos.
3. Trinta combinações de Hug no pai e Fill no filho dependiam do mesmo eixo de altura.
4. Imagens e legendas desconsideravam parte do padding lateral de nove contêineres.
5. O degradê radial capturado no corpo inteiro alterava a cor de fundo durante a apresentação.
6. Os indicadores não mantinham bordas e alturas visuais alinhadas quando um valor ocupava mais linhas.

## Correções executadas

- [x] Corrigir quebra e largura dos 70 links de índice.
- [x] Resolver os 30 conflitos Hug/Fill.
- [x] Corrigir o dimensionamento de 190 trechos originalmente organizados em grids com altura automática; os trechos afetados usam Auto Layout com altura intrínseca e colunas preservadas.
- [x] Alinhar os 20 grupos de indicadores com altura mínima compatível com o conteúdo atual, mantendo crescimento por conteúdo.
- [x] Adequar imagens e legendas à largura interna dos nove contêineres de evidências.
- [x] Delimitar o fundo radial nos dez layouts, preservando as cores existentes.
- [x] Ajustar os contêineres dos artigos e o crescimento dos frames externos.
- [x] Preservar textos, imagens, tipografia, posição dos cases no canvas e IDs dos frames originais.

## Validação final

A auditoria inicial encontrou 127 contêineres com filhos visíveis ultrapassando limites e 30 conflitos Hug/Fill. Ao final, os dez layouts apresentaram zero ocorrências nesses critérios, zero textos recortados pelo contêiner e nenhum corpo excedendo o frame externo. Não há sobreposição entre os dez frames no canvas. Tolerância de arredondamento: 2 px.

As contagens foram preservadas: 1.574 camadas de texto e 14 camadas de imagem. Nenhuma afirmação factual foi reescrita nesta rodada.

A validação estrutural cobre os layouts atuais a 1280 px; não equivale a testar breakpoints de CSS ou conteúdo futuro. Foram inspecionados visualmente recortes de resumo e contexto para confirmar o ritmo vertical e o ajuste das métricas.

Registro técnico com os IDs afetados e resultados antes/depois: `output/autofix-pagina30-registro.json`.

Esta rodada alterou diretamente a página solicitada no Figma Design. Não realizou nova importação no Make nem publicação do site.
