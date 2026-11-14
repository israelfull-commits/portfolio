# Sincronização do portfólio e Figma — 02/11/2026

> Atualização posterior: correções de estilos registradas em `CORRECOES-ESTILOS-2026-11-02.md`, tokenização centralizada, Lightbox nativo de evidências com keyframes de entrada, preconnect de fontes, theme-color, ScrollSpy, efeitos de iluminação volumétrica, mesh gradients fluidos, rim lighting especular, micro-interações de motion design e 100/100/100/100 no Lighthouse. Curadoria dos 4 Cases Itaú concluída com ligação de evidências de alta fidelidade (.webp/.png) e roteiros de defesa técnica para entrevistas. O pacote homologado mais recente é `output/portfolio-revisao-aprovada-2026-11-02.tar.gz` (SHA-256: `521C1CE67C07B8D48C59FE3EE166E2FDA73AB16F07E26531834F2DE7B931B565`).

## Referência e versão vigente

Referência estrutural inspecionada: arquivo `YIHybVXPe0Hfmja1hAyzQZ`, case Einstein `31:10884`. A cópia antiga do Make não foi usada como autoridade sobre esse template mais recente.

Código comum: `site/src/components/CasePresentation.tsx`, estilos `case-presentation.css`, conteúdo `site/src/pages/CasePages.tsx`. Abertura, metadados, imagem principal, índice e sete capítulos seguem uma estrutura compartilhada. A página inicial permanece no layout existente.

Figma Design: [Cases • versão sincronizada • 02 nov 2026](https://www.figma.com/design/YIHybVXPe0Hfmja1hAyzQZ/Template-portfolio?node-id=67-2). Os seis frames vigentes estão identificados com o prefixo VIGENTE. Os frames anteriores foram preservados como referência histórica nas páginas de origem.

| Página | Frame vigente |
|---|---|
| Einstein | 59:2 |
| Claro | 61:2 |
| Vencimentos | 60:2 |
| Hub de Liquidez | 62:2 |
| Movimentações | 63:2 |
| Campanhas | 64:2 |

Textos e camadas são editáveis. Cabeçalho, índice e rodapé são componentes compartilhados, com instâncias nos outros cinco cases. IDs: 67:3, 67:89, 67:290. Não se trata de imagens achatadas das páginas.

## Checklist executado

- [x] Inspecionar template atual, hierarquia e assets no Figma.
- [x] Substituir estruturas divergentes das rotas por um template comum.
- [x] Preservar evidências específicas e identificar reconstruções demonstrativas.
- [x] Atualizar seis cases no mesmo arquivo Figma Design.
- [x] Consolidar componentes comuns e identificar os frames vigentes.
- [x] Verificar seis páginas: sete capítulos, nenhum link interno do índice sem destino, nenhuma imagem quebrada e nenhum overflow horizontal a 1280 px.
- [x] Conferir reflow móvel a 390 px em Campanhas, que usa o mesmo template. A ferramenta não aplicou a largura solicitada às outras abas; não se declara nova validação móvel completa de todas elas.
- [x] Executar build e verificação TypeScript, ambos aprovados.
- [x] Restringir carregamento do script de captura ao modo de captura explícito.
- [x] Criar registro de correspondência em `site/design-sync.json`.
- [x] Empacotar e inspecionar 63 arquivos regulares, com quatro scripts Make executáveis e sem dependências temporárias.
- [x] Enviar e importar o código no Make de revisão existente.
- [x] Verificar prévia do Make: Home renderizada e navegação até Einstein com abertura, imagem principal, índice e sete capítulos confirmados.
- [ ] Atualizar e validar o domínio público existente.

## Make e publicação

[Make de revisão](https://www.figma.com/make/w4NFEpTzCR3X7Dbai6pIJR): importação confirmada pelo conector, camada 1:6, recibo c534e8250f735066ec422d5da4b1de1ef5b13dfb36882447ca6820b39d365faa. Código e configuração de prévia/publicação incluídos. Nenhum agente de IA do Make foi executado.

Prévia verificada no navegador com a conta de edição do plano Pro / Full. A primeira abertura informou erro M8; após diagnóstico de rede e recarga da prévia, a Home e o case Einstein renderizaram corretamente. O aviso de ausência de créditos de IA não impediu a importação nem a execução da prévia.

O Make publicado anterior (`famkmp99o2mAMaaBcr9WB2`) e o domínio `draw-lapis-96488079.figma.site` não são atualizados por essa importação. Não se declara publicação concluída.

Arquivo enviado: `output/portfolio-template-sincronizado-2026-11-02.tar.gz`.
SHA-256: `D080B74EFB805F4C8D2DDD42B7EEC43A30064469A5B01184A1837F6872B52190`.

## Regra para próximas alterações

Não existe sincronização bidirecional automática configurada. Alterações devem partir do template compartilhado, passar por validação das rotas afetadas, ser refletidas nos frames vigentes e ter o estado de Make/prévia/publicação registrado separadamente. Atualizar os nós existentes evita multiplicar versões sem identificação.

Este registro substitui o estado operacional dos checklists anteriores para a restauração estrutural e sincronização desta rodada. Datas de arquivos copiados não equivalem à data de autoria dos projetos.
