# QA visual e funcional — réplica Amity Cast

Data: 2026-11-01 (America/São_Paulo)  
final result: passed

Nenhum achado P0, P1 ou P2 permanece aberto.

## Escopo e fonte de verdade

A implementação em `site/` foi reconstruída a partir do código-fonte integral extraído do Figma Make, preservando componentes, conteúdo, tipografia, cores, espaçamento, imagens, rotas e regras responsivas. Os assets usados pela interface estão em `site/public/`; não há dependência dos bundles, CSS ou imagens hospedados pela publicação Figma.

Referências visuais:

- Desktop original, 1440 × 9227 px: `C:\Users\Israel Rozar\Documents\ChatGPT\Portfolio\output\playwright\amity-source\home-desktop-1440.png`
- Mobile original, viewport 390 × 844 px e página 390 × 13129 px: `C:\Users\Israel Rozar\Documents\ChatGPT\Portfolio\output\playwright\amity-source\home-mobile-390x844.png`
- Menu móvel original aberto, 390 × 844 px: `C:\Users\Israel Rozar\Documents\ChatGPT\Portfolio\output\playwright\amity-source\mobile-menu-open-390x844.png`

Evidências da réplica:

- Desktop, 1440 × 1000: `C:\Users\Israel Rozar\AppData\Local\Temp\replica-desktop.png`
- Mobile, 390 × 844: `C:\Users\Israel Rozar\AppData\Local\Temp\replica-mobile.png`
- Menu móvel aberto, 390 × 844: `C:\Users\Israel Rozar\AppData\Local\Temp\replica-mobile-menu.png`
- Mobile estreito, 320 × 900: `C:\Users\Israel Rozar\AppData\Local\Temp\replica-320.png`
- Tablet, 768 × 900: `C:\Users\Israel Rozar\AppData\Local\Temp\replica-768.png`
- Desktop, 1280 × 1000: `C:\Users\Israel Rozar\AppData\Local\Temp\replica-1280.png`
- Desktop amplo, 1536 × 1000: `C:\Users\Israel Rozar\AppData\Local\Temp\replica-1536.png`

## Ledger de comparação visual

| Área | Evidência da fonte | Evidência renderizada | Resultado |
|---|---|---|---|
| Header | Marca circular IR, navegação horizontal e CTA sublinhado | Mesmos elementos, dimensões e alinhamento | Passou |
| Hero | Manrope em escala editorial, retrato com placa lima inclinada | Composição, quebra, imagem e legenda preservadas | Passou |
| Barra de sinais | Quatro métricas com divisores | Grade e reflow 2 × 2 preservados | Passou |
| Posicionamento | Título amplo, copy em duas colunas e quatro capacidades | Hierarquia, cards e ritmo vertical preservados | Passou |
| Case Einstein | Card floresta + painel de evidências | Cores, proporção, métricas e CTA preservados | Passou |
| Dossiês Itaú | Grade 2 × 2 com primeiro card em destaque | Conteúdo e estilos integralmente preservados | Passou |
| Trajetória | Timeline tripartida e tags | Colunas desktop e empilhamento mobile preservados | Passou |
| Contato | Painel floresta com CTA lima | Layout, tipografia e links preservados | Passou |
| Mobile | Hero empilhado, retrato à direita, menu compacto | Sem overflow a 390 px; mesma ordem e escala | Passou |

## Melhorias aplicadas sem redesign

- `robots` alterado para indexação e canonical adicionado.
- Metadados duplicados do shell Figma removidos; permanece uma descrição e um `og:title`.
- Imagens sociais e JSON-LD consolidados.
- Menu móvel convertido de `details/summary` para `button` com `aria-expanded` e `aria-controls`.
- Ao abrir, o foco segue para “Sobre”; `Escape` fecha e devolve o foco ao botão.
- Clique externo e seleção de link também fecham o menu.
- Assets visuais, PDF e favicon armazenados localmente.

## Checks automatizados

| Check | Desktop 1440 | Mobile 390 |
|---|---:|---:|
| Página e título corretos | Passou | Passou |
| Conteúdo significativo / H1 | Passou | Passou |
| Overlay de erro | Ausente | Ausente |
| Erros no console | 0 | 0 |
| Overflow horizontal | 0 px | 0 px |
| Controles sem nome | 0 | 0 |
| Description única | 1 | 1 |
| `og:title` único | 1 | 1 |
| Screenshot full-page | Gerado | Gerado |
| Interação de menu | N/A | Passou |

### Matriz responsiva adicional

| Viewport | H1 | Headings | Overflow | Console | Controles sem nome | Menu |
|---:|---:|---:|---:|---:|---:|---|
| 320 px | 1 | 20 | 0 px | 0 erros | 0 | Abre, foca “Sobre”, fecha com Escape e restaura foco |
| 768 px | 1 | 20 | 0 px | 0 erros | 0 | Abre, foca “Sobre”, fecha com Escape e restaura foco |
| 1280 px | 1 | 20 | 0 px | 0 erros | 0 | Navegação desktop corretamente exibida |
| 1536 px | 1 | 20 | 0 px | 0 erros | 0 | Navegação desktop corretamente exibida |

As quatro capturas full-page foram inspecionadas durante a validação. Nenhuma quebra, recorte, colisão, ausência de asset ou regressão de hierarquia exigiu alteração visual.

## Histórico do fluxo testado

1. Build de produção com `npm run build`: 47 módulos transformados, sem erros.
2. Preview em `http://127.0.0.1:4174/`.
3. Desktop: carregamento → H1 e 20 headings presentes → screenshot full-page → console limpo.
4. Mobile: carregamento em 390 px → botão Menu → `aria-expanded=true` → foco em “Sobre”.
5. Mobile: tecla `Escape` → `aria-expanded=false` → menu oculto e foco restaurado ao botão.
6. Verificação de largura: `scrollWidth === innerWidth` em desktop e mobile.
7. Segunda rodada responsiva em 320, 768, 1280 e 1536 px com os mesmos checks estruturais, captura full-page e interação do menu nos dois breakpoints aplicáveis.

## Risco residual

O CSS importa DM Sans e Manrope do Google Fonts, como na fonte original. Há fallback de sistema caso a fonte remota não esteja disponível. Não foram observadas diferenças de layout nas capturas validadas.
