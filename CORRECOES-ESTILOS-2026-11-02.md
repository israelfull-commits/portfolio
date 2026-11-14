# Correções de design e estilos — 02/11/2026

> Complemento posterior: `VALIDACAO-HUG-FILL-WRAP-FLEX-2026-11-02.md` registra a auditoria dos contêineres, a correção dos estados fechados no Figma e a liberação das linhas dos grids de metadados.

## Escopo efetivamente corrigido

Template compartilhado dos seis cases vigentes, código local e os mesmos arquivos no Make `w4NFEpTzCR3X7Dbai6pIJR`. Frames preservados: Einstein 59:2, Claro 61:2, Vencimentos 60:2, Hub 62:2, Movimentações 63:2 e Campanhas 64:2, no arquivo Design `YIHybVXPe0Hfmja1hAyzQZ`.

## Defeitos e correções

- Dimensões declaradas incorretas na imagem principal Einstein: 1152 × 640 substituídos por 1142 × 1150, conforme arquivo real. A reserva de espaço passa a respeitar a proporção da imagem.
- Limite genérico de altura nas evidências removido da galeria. Imagens respeitam proporção e resolução nativa; o limite de 640 px permanece apenas na abertura.
- Margens do template alinhadas ao cabeçalho e rodapé. As diferentes larguras de contêiner causavam desalinhamento quando a barra de rolagem reduzia a área útil.
- Índice com altura máxima e rolagem própria em telas baixas; comportamento normal no mobile.
- Espaço superior indevido nos primeiros subtítulos das colunas removido.
- Metadados com separação consistente entre rótulo e valor.
- Regras dos controles de expansão aplicadas também ao elemento `details` independente, com alvo de interação, espaçamento e contraste do marcador.
- Links de fontes no corpo do texto com sublinhado e quebra de URLs longas.
- Espaçamento final dos capítulos ajustado para a transição ao rodapé.
- Figma: fundo radial capturado incorretamente no corpo completo substituído por luz radial de tamanho delimitado, sobre a cor de fundo existente.
- Figma: imagens com dimensões proporcionais, galerias com auto-layout vertical, artigos com altura automática e frames dimensionados para conter o corpo.
- Figma: metadados, subtítulos e controles de expansão ajustados nos mesmos nós, sem multiplicar versões.

Tipografia e escala dos títulos foram comparadas com o template original `31:10884`: os valores coincidem. Foram preservadas, assim como o conteúdo factual e os sete capítulos.

## Validação executada

- [x] Build de produção e TypeScript aprovados.
- [x] Detector de estilos Impeccable executado nos três arquivos alterados: nenhuma ocorrência.
- [x] Seis rotas × três larguras reais verificadas: 390, 768 e 1280 px. Todas com margens alinhadas, sete capítulos e sem overflow horizontal.
- [x] Imagem principal Einstein verificada no navegador com dimensões naturais e declaradas iguais.
- [x] Três arquivos no Make relidos após salvar: conteúdo integral idêntico ao código local.
- [x] Seis frames Figma: nenhum texto recortado pelo contêiner, corpo contido pelo frame e nenhum degradê radial aplicado à altura inteira do corpo.
- [x] Inspeção visual da abertura Einstein e galeria Claro no Figma.
- [x] Pacote atualizado criado e inspecionado: 63 arquivos regulares.

Impressões de comparação de conteúdo normalizado (FNV-1a, apenas identificação de igualdade): CSS `da0a8eaf`; CasePresentation `2ed27bc8`; CasePages `cc06e4ab`.

## Publicação

As correções estão no código local, no Design e no Make de revisão existente. O domínio público anterior não foi republicado nesta rodada. As versões antigas e o pacote anterior são históricos; não devem ser apresentados como a versão mais recente.

A nova prévia do Make apresentou erro de rede M8, inclusive após recarga. O código salvo foi relido e comparado integralmente com o local; isso confirma a atualização dos arquivos, mas não confirma a renderização atual da prévia remota. A validação responsiva desta rodada foi feita no portfólio local.
