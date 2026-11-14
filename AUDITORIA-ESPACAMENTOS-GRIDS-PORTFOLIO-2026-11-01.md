# Auditoria de espaçamentos, grids e margens do portfólio

Data: 01/11/2026

## Escopo

- Home (`/`)
- Case Einstein (`/cases/einstein-laudos`)
- Estado 404
- Desktop: viewport de 1200 × 900 px
- Mobile: viewport de 390 × 844 px, área útil de 375 px

## Veredito

O sistema espacial é consistente no nível estrutural e está pronto para apresentação. Containers, margens externas, responsividade e ritmo entre grandes seções seguem uma lógica comum. A principal oportunidade é normalizar o padding interno dos cards do case no mobile: atualmente há três recuos visuais próximos, porém diferentes, sem função semântica clara.

## Evidências e saúde por etapa

1. **Home desktop — saudável.** Hero e seções usam container de até 76 rem, gutter observado de 24 px e seções principais com 120 px de respiro vertical no viewport auditado. Não há overflow horizontal.
2. **Case desktop — saudável.** Hero e conteúdo compartilham o mesmo container e eixo da home. Os blocos do case usam intervalo recorrente de 24 px e os cards principais preservam uma hierarquia espacial coerente.
3. **Home mobile — saudável.** Container útil de 343 px com 16 px de margem em cada lado. Seções editoriais usam 88 px de padding vertical; hero e contato adotam ritmos menores de forma coerente com suas funções. Não há overflow horizontal.
4. **Case mobile — saudável com refinamento recomendado.** Todos os blocos respeitam a largura de 343 px e o grid colapsa corretamente para uma coluna. Entretanto, os eixos internos variam: aproximadamente 20 px em evidências/comparação, 28 px na nota de transparência e 32 px em summary/details/teste.
5. **Estado 404 — saudável.** Usa o mesmo container, gutter, cabeçalho e rodapé das demais páginas. A composição tem espaço suficiente e mantém a ação principal visível.

## Achados

### P0 — nenhum problema crítico

- Nenhum conteúdo estoura horizontalmente nos viewports auditados.
- Não há cards colidindo, margens quebradas ou grids incompletos.
- Cabeçalho, conteúdo e rodapé compartilham os mesmos eixos externos.

### P1 — normalizar padding interno dos cards no mobile

- `case-evidence-visuals` e `case-comparison`: cerca de 20 px.
- `case-disclosure`: cerca de 28 px.
- `featured-case`, `case-detail` e `case-test`: cerca de 32 px.

Recomendação: definir dois níveis explícitos, não três valores implícitos:

- `--card-padding-mobile: 1.25rem` para cards densos e visuais.
- `--panel-padding-mobile: 2rem` para blocos editoriais de destaque.

A nota de transparência deve aderir a um desses níveis, preferencialmente 20 px por ser um bloco compacto.

### P2 — formalizar a escala espacial em tokens

O CSS possui bom ritmo visual, mas muitos `gap`, `padding` e `margin` são definidos localmente. Recomenda-se uma escala base de 4 px ou 8 px com tokens para 8, 12, 16, 20, 24, 32, 48, 64, 88 e 120 px. Isso reduz divergências em novos cases sem alterar o layout atual.

### P2 — documentar os dois ritmos verticais

- Home: ritmo editorial amplo de 88 px no mobile e 120 px no desktop auditado.
- Case: ritmo de narrativa contínua com 24 px entre cards.

Os dois ritmos são adequados, mas devem ser registrados como padrões distintos para que uma futura página não misture ambos arbitrariamente.

## Limites

- A inspeção visual não certifica conformidade de acessibilidade.
- Zoom de 200%, fontes personalizadas desativadas e larguras intermediárias adicionais não foram testados nesta rodada.
- Capturas de página completa podem registrar imagens lazy-load antes do carregamento; isso não afeta as medições de grid e espaçamento desta auditoria.

