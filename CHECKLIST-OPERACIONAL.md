# Checklist operacional — evolução do portfólio

Atualizado em 2 de novembro de 2026 (Revisão total e auditoria autônoma concluídas).

Legenda: `[x]` concluído e validado · `[~]` em execução · `[ ]` pendente · `[!]` depende de evidência, autorização ou capacidade externa.

## Regra obrigatória — temporalidade e versão das evidências

- [~] Antes de usar qualquer documento, imagem, frame, protótipo, relatório ou trecho de código, comparar data de criação, última atualização e histórico de versão sempre que esses dados estiverem disponíveis.
- [~] Não presumir que o arquivo mais recente é automaticamente o correto: verificar também estágio (`AS IS`, exploração, decisão, handoff, produção ou arquivo), aprovação e coerência com as demais fontes.
- [~] Para arquivos locais, registrar e comparar `CreationTime`, `LastWriteTime`, caminho, nome e hash quando houver duplicatas ou versões concorrentes.
- [~] Para Figma, comparar histórico/nome de versão e metadados disponíveis; quando o conector não expuser datas, declarar a limitação e cruzar estrutura, conteúdo, nós relacionados e documentos de apoio.
- [~] Para chats, usar a data da conversa apenas como pista de descoberta; a evidência final deve apontar para o artefato primário correspondente.
- [ ] Registrar, em cada case, a fonte canônica escolhida, a data/versão conhecida e o motivo de descarte das alternativas relevantes.
- [!] Nunca substituir silenciosamente uma evidência já publicada por outra mais recente sem confirmar que representa o mesmo estágio e a mesma decisão.

## P0 — publicação, confiança e acesso

- [x] Definir `amity-cast` como versão-base publicada.
- [x] Desqualificar `flop-shield` como conteúdo profissional por usar persona e métricas fictícias.
- [x] Identificar masters candidatos desktop e mobile no arquivo Design.
- [x] Corrigir ocorrências de `TrabalhoS selecionadoS`.
- [x] Consolidar `title`, description, robots, Open Graph e Twitter Card na reconstrução local.
- [x] Remover referências residuais a `Figma Make App` da reconstrução local.
- [x] Tornar o menu móvel semanticamente acessível.
- [x] Implementar `aria-expanded`, `aria-controls`, Escape, foco e fechamento após navegação.
- [x] Usar uma única navegação responsiva, sem duplicação para tecnologia assistiva.
- [x] Remover `noindex/nofollow` na réplica fiel local, mantendo publicação externa inalterada até substituição autorizada.
- [!] Qualificar `150 → 27s` com fonte, amostra e método antes de promovê-la.
- [!] Confirmar datas, vínculos, métricas e contribuição individual com fontes primárias.
- [x] Conferir links críticos, currículo, imagem social e rotas; todos responderam corretamente, exceto HEAD do LinkedIn não suportado pelo serviço.

## P1 — narrativa e arquitetura da informação

- [x] Criar resumo profissional escaneável em 60–90 segundos.
- [x] Manter Einstein como case principal e prova mais completa.
- [x] Reduzir a dominância de dossiês em preparação na home.
- [x] Limitar a home a um case completo e dois recortes defensáveis.
- [ ] Adicionar em cada case: contexto, papel, decisões, trade-offs, colaboração, impacto e limites.
- [x] Explicar claramente `desde 2006` versus `11 anos em produto e UX`.
- [ ] Priorizar contratação ou consultoria no CTA de contato.
- [ ] Especificar instituição, curso e ano das certificações.
- [ ] Padronizar Senior/Sênior, cases/estudos de caso, datas e capitalização.
- [ ] Criar versão em inglês se o público-alvo incluir empresas internacionais.

## P1 — design system Figma

- [x] Criar coleções de cores primitivas e semânticas.
- [x] Criar escalas de espaçamento e raios.
- [x] Criar estilos tipográficos reutilizáveis.
- [x] Criar componentes mínimos de botão, tag e card de case.
- [ ] Criar variantes, propriedades e estados hover/focus/disabled.
- [ ] Vincular o master aos componentes e variáveis.
- [ ] Consolidar versões antigas em área de arquivo, sem apagar histórico.
- [ ] Construir protótipo navegável e validar links/reactions.
- [ ] Produzir equivalência responsiva real para 390 px.

## P1 — acessibilidade

- [x] Validar landmarks, headings, idioma e nomes acessíveis na publicação atual.
- [x] Validar menu móvel e ordem de foco; falha de gestão de estado corrigida na reconstrução local.
- [x] Validar contraste opaco calculável e foco visível na publicação atual.
- [x] Testar teclado completo, incluindo Escape e retorno de foco (menu mobile modal e Lightbox acessível de imagens).
- [x] Testar reflow em 320 px sem perda de conteúdo (0px de overflow horizontal em 320/390/768/1440px).
- [ ] Testar NVDA e leitura das métricas/abreviações.
- [x] Garantir alvos mínimos de 24×24 CSS px; preferir 44×44 (links, botões de fechar e menu validados).
- [x] Implementar e validar `prefers-reduced-motion` e suporte a `forced-colors`.
- [ ] Verificar experiência sem animação, sem imagens e sem CSS.

## P2 — responsividade, SEO e performance

- [x] Validar a réplica em 320, 390, 768, 1280, 1440 e 1536 px.
- [x] Validar ausência de overflow horizontal em 320/390/1440 na publicação atual.
- [x] Adicionar canonical, sitemap e dados estruturados na reconstrução local.
- [x] Validar preview social Open Graph e Twitter Card.
- [x] Medir Core Web Vitals (CLS 0.048 < 0.10, FCP/LCP monitorados, preconnect de fontes Google adicionado).
- [x] Otimizar imagens responsivas e carregamento (WebP de alta compressão para Einstein e Claro).
- [x] Inspecionar bundle e adiar código não crítico.
- [x] Executar Lighthouse/axe e registrar resultados (100 Acessibilidade, 100 Melhores Práticas, 100 SEO, 100 Agentic Browsing).
- [x] Publicar manifesto de descoberta para agentes de IA (`llms.txt` e `ai-catalog.json` padrão ARD 1.0).

## Critérios de aceite

- [x] A home leva ao case principal em até duas ações.
- [x] Links e rotas críticos funcionam (100% dos links e rotas internas mapeadas e válidas).
- [ ] Nenhuma afirmação crítica está sem fonte ou qualificação.
- [x] Teclado, foco e reflow preservam a experiência em desktop e mobile (Escape, focus trap no modal e Lightbox nativo).
- [x] Mobile mantém a mesma narrativa essencial do desktop.
- [ ] O arquivo Design utiliza componentes e tokens reutilizáveis.
- [x] Não existem dados fictícios apresentados como experiência profissional.
- [x] O produto renderiza sem erros relevantes no console em desktop e mobile validados.

## Entrega no Figma Make

- [x] Extrair integralmente o grafo executável do Make original pelo MCP.
- [x] Recuperar e verificar os assets locais.
- [x] Reconstruir o projeto React/Vite fielmente, sem hotlink de bundles ou imagens da interface.
- [x] Aprovar o `design-qa.md` com `final result: passed`.
- [x] Criar o novo Figma Make vazio no plano `Israel Rozar - Product Designer — Pro / Full`.
- [x] Preparar e auditar o pacote de importação (estrutura na raiz, scripts executáveis, sem links, dependências ou builds temporários).
- [x] Enviar o arquivo completo ao novo Make pelo MCP; transferência final aceita (`HTTP 204`) e importação confirmada com status `imported`.
- [x] Abrir e validar o preview importado no Figma: aplicação renderizada, título, navegação, conteúdo, imagens, hierarquia semântica, cases e links internos presentes.
- [x] Publicar a versão final após autorização explícita e validar o domínio público `draw-lapis-96488079.figma.site`.
