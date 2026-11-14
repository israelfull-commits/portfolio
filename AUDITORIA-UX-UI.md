# Auditoria comparativa UX/UI — Portfólio Israel Rozar

Data: 1 de novembro de 2026  
Escopo: duas versões publicadas, um arquivo Figma Design e dois projetos Figma Make.

## Veredito

A versão publicada em `amity-cast` é a melhor base operacional: possui posicionamento específico, conteúdo autoral, case estruturado, identidade consistente, semântica acessível e metadados mais maduros. No arquivo Design, o frame `16:2` é a melhor síntese visual; ele deve incorporar a profundidade de evidências do frame `12:7409`. O frame `19:2` é apenas uma referência mobile parcial.

## Ranking

1. `amity-cast` — melhor versão executável e publicável.
2. Frame Design `16:2` — melhor síntese visual editável.
3. Frame Design `12:7409` — maior profundidade de conteúdo e evidências.
4. `flop-shield` — ainda parece template, com metadados genéricos.

## Achados prioritários

### P0 — antes de divulgar

- Remover `noindex, nofollow` quando o conteúdo estiver autorizado e pronto para descoberta.
- Transformar os cases prioritários em páginas completas ou reduzir sua presença na home para evitar promessas incompletas.
- Produzir uma versão mobile equivalente, não apenas resumida, e validar 320, 390, 768, 1280 e 1536 px.
- Preservar fonte, contexto, amostra, limites e contribuição individual para cada métrica ou afirmação de impacto.

### P1 — qualidade de sistema

- Criar componentes, variáveis, estilos locais e estados interativos no Figma.
- Consolidar versões antigas em uma área de arquivo, preservando histórico sem competir com o master.
- Validar teclado, foco, zoom de 200%, reflow, contraste e leitor de tela.
- Completar SEO com canonical, sitemap, imagem social e dados estruturados.

### P2 — otimização

- Medir Core Web Vitals, peso de imagens e JavaScript.
- Reduzir densidade textual da home e mover detalhes para cases.
- Revisar todos os links, estados de erro, carregamento e navegação entre rotas.

## Checklist executado

- [x] Comparar as cinco fontes disponíveis.
- [x] Definir versão-base publicada e masters candidatos no Design.
- [x] Corrigir duas ocorrências de `TrabalhoS selecionadoS`.
- [x] Renomear os frames `16:2` e `19:2` com status explícito.
- [x] Criar a página `Auditoria UX-UI • 2026-11-01` no Figma.
- [x] Validar a estrutura e renderização da página de auditoria.
- [ ] Remover bloqueio de indexação após autorização editorial.
- [ ] Completar os cases prioritários e validar as evidências.
- [ ] Construir design system e protótipo navegável no Figma.
- [ ] Executar testes de acessibilidade em código e com tecnologia assistiva.

## Limites de evidência

Screenshots e estrutura visual não comprovam conformidade WCAG. Os arquivos Figma Make não aceitam `get_metadata`, `get_screenshot` ou `use_figma`; a revisão deles foi complementada pelos arquivos-fonte expostos pelo conector e pelos sites publicados. Afirmações profissionais e métricas não foram alteradas sem fonte primária.

## Critério de aceite final

A versão está pronta quando a home leva ao case principal em até duas ações; todos os links funcionam; nenhuma afirmação crítica está sem fonte; teclado, foco, reflow e zoom preservam todo o conteúdo; mobile mantém a mesma narrativa; e o arquivo Design usa componentes e tokens reutilizáveis.
