# Polimento do portfólio — 25/11/2026

Seleção confirmada pelo usuário: Einstein, Itaú, Claro e Neoenergia. Identidade preservada: Plus Jakarta Sans, canvas claro, pine e lime.

## Aplicado
- Cards com hierarquia cliente → título → papel → escopo → descrição → rodapé.
- Rodapé compartilhado com relógio e estimativa de leitura, acesso ao case e área de toque mínima44px.
- Mesma estimativa no topo do case. Componente: src/components/CaseReadingTime.tsx.
- Cards3colunas em desktop, lista em tablet/mobile para evitar títulos excessivamente estreitos.
- Tipografia auxiliar14/20–22, descrição16/26, títulos24/32; alinhamento das ações e estados de foco/hover.
- FrameFigma412:6100 atualizado com a seleção confirmada, textos mais diretos, destaque visual e cards mais compactos.

## Estimativas de leitura
Texto dos capítulos renderizados, 200palavras/minuto, arredondado para cima; leitura de figuras pode ampliar o tempo. Recalcular ao alterar conteúdo.

|Case|Palavras|Minutos|
|---|---:|---:|
|Einstein|1502|8|
|Itaú / Hub|716|4|
|Claro|1013|6|
|Neoenergia|1291|7|
|Movimentações|754|4|
|Campanhas|811|5|
|Registros|642|4|

## Validação
- TypeScript: passou.
- Builds site e portfolio-verde: passaram, incluindo geração de rotas estáticas.
- Sentinel: sete verificações passaram com python-Xutf8.
- Browser: quatro cards e quatro cabeçalhos com leitura; sem pageerror e sem overflow em320/390/768/1280.
- Capturas: qa/polish-2026-11-25/cards-desktop.png e cards-mobile.png; inspeção visual realizada.
- Detector: um aviso de fonte popular; mantida Plus Jakarta Sans por ser a tipografia aprovada, sem trocar identidade como efeito do polimento.
- src/, public/, scripts/ e configurações de build espelhados em portfolio-verde; controle Git e identidade de hospedagem preservados.

Esta entrega refina componentes e a vitrine. As narrativas dos cases existentes foram preservadas.
