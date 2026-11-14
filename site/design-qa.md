# QA da implementação — 2026-11-13

Final result: passed para a home e os fluxos descritos abaixo, com desvios intencionais registrados. Não significa equivalência pixel a pixel nem auditoria completa de acessibilidade.

## Referências e evidências

- Fonte desktop: FigmaYIHybVXPe0Hfmja1hAyzQZ/370:16614; captura `qa/figma-home.png` (1280×4465).
- Fonte mobile: mesmo arquivo/375:366; `qa/figma-mobile.png` (390×8642).
- Implementação: `qa/home-desktop-final.png`, `qa/home-mobile-final.png`; localhost:8443, rota/, topo, menu fechado, tema claro.
- Comparações conjuntas: `qa/compare-desktop-final.png`, `qa/compare-mobile-final.png`; recortes hero correspondentes. Fonte e implementação lado a lado, largura CSS1280/390, density1, sem escala adicional. Alturas variam porque o conteúdo e a foto tiveram ajustes autorizados.
- Interação: `qa/mobile-menu.png`; case funcional: `qa/case-mobile.png`.
- Browser plugin não disponível; CUA/node_repl falhou na inicialização. Foi utilizado Playwright CLI conforme fallback da skill frontend-testing-debugging, neste ambiente Windows portátil.

## Iterações

1. Bloqueada: tracking negativo mudava quebras dos títulos, cabeçalho deslocava a navegação e pseudo-elemento expandia as capturas. Fonte móvel exigia lead20/30, botões em largura total e retrato vertical maior. Ícones de expertise ainda ausentes.
2. Corrigido: tracking zero, texto da hero alinhado ao início, navegação central, pseudo-elemento removido, lead20/30 e layout mobile alinhado à referência. Ícones originais exportados do Figma e integrados.
3. Pós-correção: nova comparação conjunta desktop/mobile; sem diferençasP0/P1/P2 restantes na home. Variações menores de rasterização e alinhamento sãoP3. Foto substituída por versão tratada a pedido do usuário, mantendo o original.

## Cinco superfícies

- Tipografia: Plus Jakarta Sans400/600/700 local; hero64/70 e36/44 mobile, seções40/48 e28/36, corpo16/24, lead20/30. Fallback sans-serif. Quebras e hierarquia conferidas visualmente.
- Espaçamento/layout: container1152, margens64/32/24, seções64/48, grids24, raios16/24; cards com crescimento pelo conteúdo. Sem texto cortado ou overflow nas larguras testadas.
- Cores/tokens: pine, lime, canvas e bordas da paleta aprovada; contraste de textos usa#4A554E, evitando o muted de menor contraste. Sem gradientes na home ou modo escuro automático.
- Imagens: retrato do projeto com tratamento fotográfico via ferramenta nativa de imagem e variantes WebP. Ícones de expertise originais do Figma. Foto preserva proporção vertical. Assets de cases mantidos.
- Conteúdo: estrutura aprovada preservada. Alterações intencionais: substituído trecho incompleto de impacto por nota de método;44 participantes sem afirmar população não verificada; Registros vincula ao relato reduzido disponível; UXfolio substitui GitHub sem URL confirmada; rodapé sem data fixa desatualizada.

## Funcional

- TypeScript --noEmit: passou após reinstalar dependências corrompidas com npm ci.
- Build Vite: passou.
- Clique CTAhero/#trabalho e menu/#experiencia: passou.
- Menu aberto, Escape e restauração de foco: passou.
- Cinco rotas de projetos da home: títulos carregados, sem404 de aplicação.
- PDF: HTTP200 e assinatura%PDF válida.
- Larguras320,390,768,1280,1440: scrollWidth não excede viewport.
- pageerror: nenhum; console final sem erros/avisos.

## Limites

A home foi comparada com o Figma; os cases reais preexistentes foram verificados funcionalmente e em captura mobile, sem alegar comparação com o case exemplo Orbe. Não foram testados leitores de tela reais nem navegadores Safari/Firefox. Envio efetivo de e-mail não foi realizado. O conteúdo pode evoluir nos arquivos indicados no README.

Checklist operacional concluído: assets, tokens, composição, responsivo, navegação, links de case, PDF, metadados, typecheck, build e inspeção visual. Publicação deve usar o mesmo project_id.
