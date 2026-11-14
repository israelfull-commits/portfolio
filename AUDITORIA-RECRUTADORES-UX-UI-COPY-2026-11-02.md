# Auditoria UX/UI, Copy e Credibilidade para Recrutadores

Data: 2 de novembro de 2026  
Superfície auditada: https://draw-lapis-96488079.figma.site/  
Objetivo: reduzir riscos de desqualificação, dúvida sobre autoria, inconsistência profissional, confidencialidade e baixa eficiência de leitura.

## Veredito executivo

O portfólio tem identidade visual forte, boa responsividade, excelente estrutura semântica e um case principal apresentado com transparência incomum. Entretanto, **não deve ser tratado como versão final de alto alcance sem uma rodada de correção editorial e de governança**.

Os três riscos mais importantes são:

1. **Materiais públicos do Itaú ainda não confirmados**: páginas exibem `Case em preparação`, `Contribuição individual — Pendente de confirmação` e ausência de autorização formal. Para um recrutador ou líder de design, isso pode levantar dúvidas de autoria, confidencialidade e julgamento profissional.
2. **SEO e compartilhamento apontam para a versão anterior**: canonical, `og:url`, imagem social, JSON-LD, sitemap e robots ainda usam `amity-cast-92973331.figma.site`, embora a versão divulgada seja `draw-lapis-96488079.figma.site`.
3. **Narrativa excessivamente defensiva**: a transparência é positiva, mas a repetição de `não demonstrado`, `pendente`, `em preparação`, `não comprova` e `não declara` reduz a percepção de conclusão e impacto.

Recomendação de decisão: **manter público o case Einstein e remover temporariamente da navegação pública os dossiês Itaú até autoria, permissão e evidências estarem confirmadas**.

## Escopo e evidências

Fluxo auditado:

1. Página inicial — desktop.
2. Página inicial — mobile 390 × 844.
3. Menu móvel e comportamento por teclado.
4. Case documentado Einstein — mobile.
5. Dossiê Hub de Liquidez — mobile, como representante dos cases em preparação.
6. Currículo público em PDF.
7. Metadados, URLs, imagens, semântica, links e disponibilidade das rotas.

Evidências visuais:

- `output/audit-recrutadores-2026-11-02/01-home-mobile.png`
- `output/audit-recrutadores-2026-11-02/02-einstein-mobile.png`
- `output/audit-recrutadores-2026-11-02/03-hub-mobile.png`
- `output/audit-recrutadores-2026-11-02/04-home-desktop.png`
- `tmp/pdfs/curriculo-1.png`

## Pontos fortes confirmados

- Direção visual distinta, madura e coerente com senioridade.
- Hero claro, memorável e diretamente associado a sistemas complexos.
- Retrato profissional bem integrado e com texto alternativo.
- Hierarquia semântica correta: um único H1 e sequência coerente de H2–H4.
- Skip link presente, foco visível e menu móvel com `aria-expanded`.
- Menu móvel move foco para o primeiro item e fecha com Escape, devolvendo foco ao botão.
- Nenhum controle interativo sem nome acessível foi encontrado.
- Sem overflow horizontal no viewport móvel auditado.
- Todas as rotas principais, PDF e imagem social responderam com HTTP 200.
- Case Einstein separa percepção de compreensão e evita transformar resultados diferentes em comparação causal.
- Métricas Einstein são acompanhadas por escopo, limites e transparência.
- Currículo de uma página tem boa leitura, hierarquia e alinhamento geral com o site.
- Conteúdo evita atribuir resultados coletivos como conquistas exclusivamente individuais.

## Achados críticos — corrigir antes de ampla divulgação

### P0.1 — Autoria, autorização e confidencialidade ainda não resolvidas

Evidência:

- Hub de Liquidez mostra `Contribuição individual — Pendente de confirmação`.
- A nota pública informa que não há autorização formal das demais partes.
- O conteúdo menciona termos internos como EA, IFA, V55, score, contratos, regras do domínio e prontidão.
- Três páginas estão marcadas como `Case em preparação · Itaú Unibanco`.

Risco:

- Recrutadores podem interpretar como falta de acabamento ou ausência de domínio sobre a própria contribuição.
- Lideranças podem questionar discernimento sobre material confidencial e políticas do empregador.
- A exposição do nome da organização junto a artefatos históricos não autorizados pode criar risco profissional desnecessário.

Correção recomendada:

- Remover temporariamente os três dossiês Itaú da navegação e do site público.
- Manter versões privadas para entrevistas, protegidas ou apresentadas ao vivo.
- Só republicar quando papel individual, autorização, estágio e evidências puderem ser afirmados positivamente.
- Revisar termos internos e generalizar nomes quando não forem essenciais à história.

### P0.2 — Metadados da versão pública apontam para outro site

Confirmado na versão publicada:

- canonical: `https://amity-cast-92973331.figma.site/`
- `og:url`: `https://amity-cast-92973331.figma.site/`
- `og:image` e Twitter image usam o domínio antigo.
- JSON-LD usa o domínio antigo.
- `robots.txt` e `sitemap.xml` usam o domínio antigo.
- O sitemap lista apenas a home e o case Einstein.

Risco:

- Mecanismos de busca podem considerar a versão antiga como principal.
- Compartilhamentos podem exibir URL ou conteúdo da versão anterior.
- Métricas e autoridade ficam divididas entre dois domínios.
- Um recrutador pode chegar a uma versão diferente da apresentada.

Correção recomendada:

- Escolher uma única URL canônica, idealmente um domínio próprio.
- Atualizar canonical, Open Graph, Twitter, JSON-LD, robots e sitemap.
- Criar metadados específicos por rota para o case Einstein.
- Redirecionar ou despublicar versões antigas quando possível.

### P0.3 — Métrica `150 → 27s / −82%` sem fonte primária recuperada

Evidência:

- A métrica aparece com grande destaque na página inicial.
- O próprio texto informa que protocolo, amostra, dispersão e telas equivalentes não foram recuperados.

Risco:

- Pode ser percebida como número de impacto selecionado para causar impressão sem lastro suficiente.
- Em entrevista, uma pergunta simples sobre método pode expor fragilidade da evidência.

Correção recomendada:

- Remover a métrica da home até recuperar a fonte primária.
- Alternativa segura: apresentar apenas `redução de tempo reportada em teste interno`, sem número.
- Se mantida, adicionar contexto mínimo: tarefa, amostra, mediana/média, cenário e quem mediu.

## Achados de alta prioridade

### P1.1 — Transparência excessiva transforma o portfólio em relatório de lacunas

Expressões recorrentes:

- `em preparação`
- `pendente de confirmação`
- `ainda não demonstrado`
- `não comprova`
- `não declara autoria individual`
- `não equivale a uma decisão de produção`

Risco:

- A leitura comunica mais o que falta do que a capacidade demonstrada.
- O recrutador precisa trabalhar demais para descobrir sua contribuição e senioridade.

Correção recomendada:

- Mudar a estrutura para `Contexto → Meu papel → Decisão → Evidência → Resultado/aprendizado`.
- Manter limitações em uma única nota curta ao final.
- Não publicar um card quando a contribuição individual ainda não pode ser declarada.

### P1.2 — Apenas um case está realmente concluído

Evidência:

- Einstein é o único case completo.
- Três cases Itaú são dossiês editoriais em preparação.
- Registros de Atendimento não possui página própria.

Risco:

- Para vagas seniores, um único case comprovado pode parecer insuficiente para demonstrar amplitude recente.
- A home promete quatro dimensões de senioridade, mas entrega três materiais incompletos e um item sem rota.

Correção recomendada:

- Publicar dois ou três cases fortes, não cinco materiais com estágios diferentes.
- Se não houver autorização para Itaú, adicionar um segundo case anterior ou um case anonimizado completo.
- Transformar `Registros de Atendimento` em insight secundário, não em card equivalente a case.

### P1.3 — Experiência paralela pode gerar dúvida de conflito ou disponibilidade

Evidência:

- `Consultoria independente — 2022–atual` se sobrepõe ao Itaú `2024–2026`.
- O texto menciona projetos `entre vínculos ou em paralelo`.

Risco:

- Pode provocar dúvida sobre conflito de interesse, dedicação ou vínculo.

Correção recomendada:

- Se verdadeiro, escrever `Consultoria pontual e projetos autorais — 2022–atual (fora do horário de vínculos principais)`.
- Se não houve atividade contínua, usar anos específicos em vez de `atual`.

### P1.4 — Formação contínua parece vaga e não verificável

Evidência:

- `Product Launches · UX Design · Data & Analytics` não informa instituição, programa, ano ou carga.
- O currículo repete os mesmos termos sem credenciais.

Risco:

- Pode parecer preenchimento por palavras-chave.

Correção recomendada:

- Informar curso, instituição e ano.
- Remover itens que não possam ser comprovados ou que sejam introdutórios demais para o nível sênior.

### P1.5 — Claims de WCAG e IA precisam de evidência proporcional

Evidência:

- Hero e currículo destacam `WCAG + IA`, `Prompt Engineering` e `Fluxos com IA`.
- O case Einstein declara corretamente que não houve certificação de acessibilidade.
- Não há case completo de IA com método, limites e resultado verificável.

Risco:

- Pode soar como keyword stacking se o entrevistador procurar aplicação concreta.

Correção recomendada:

- Trocar `WCAG` isolado por `práticas de acessibilidade baseadas em WCAG` quando aplicável.
- Demonstrar um exemplo real: critério, decisão, teste e resultado.
- Só manter `Prompt Engineering` como competência se houver caso e profundidade defendível.

## Achados de média prioridade

### P2.1 — Comprimento e densidade prejudicam leitura de triagem

- Home: aproximadamente 9.227 px em desktop e 13.260 px em mobile.
- A narrativa é forte, mas extensa para a primeira leitura de 30–90 segundos.
- Cards Itaú concentram texto técnico e ressalvas antes de uma evidência visual convincente.

Recomendação:

- Resumir a home para posicionamento, dois cases, experiência e contato.
- Levar detalhes editoriais e limitações para dentro dos cases.
- Criar resumo de cada case com: problema, papel, decisão e resultado em quatro linhas.

### P2.2 — Copy mistura português e inglês sem regra clara

Exemplos: `Senior Product Designer`, `Product Discovery`, `UX Strategy`, `Design Systems`, `craft`, `prompt engineering`, `screenflows`, `AS IS`.

Recomendação:

- Manter nomes de cargos e termos consagrados em inglês.
- Traduzir termos operacionais quando houver equivalente natural.
- Definir uma convenção e aplicá-la no site e currículo.

### P2.3 — Erro de concordância na home

Texto atual: `Registros com IA complementa o conjunto...`  
Correção: `Registros com IA complementam o conjunto...`

### P2.4 — Endereço público pouco memorável

`draw-lapis-96488079.figma.site` funciona, mas parece provisório e não reforça marca pessoal.

Recomendação:

- Conectar domínio próprio curto, como `israelrozar.com.br` ou equivalente disponível.
- Usar o mesmo domínio no currículo, LinkedIn, canonical e compartilhamentos.

### P2.5 — E-mail Yahoo reduz levemente a percepção de acabamento

Não é um erro nem motivo isolado de desqualificação, mas um endereço no domínio próprio ou um Gmail profissional tende a transmitir maior atualidade e consistência de marca.

## UX/UI por etapa

### Etapa 1 — Home desktop: saudável com ressalvas editoriais

Saúde geral: **boa**.

- Hero, retrato, proposta de valor e CTA têm ótima hierarquia.
- A seção de trabalhos perde força por misturar um case completo, três dossiês incompletos e uma métrica sem rota.
- A densidade aumenta muito depois da primeira dobra.

### Etapa 2 — Home mobile: saudável

Saúde geral: **boa**.

- Reflow correto, sem overflow horizontal.
- Tipografia mantém impacto e legibilidade.
- O hero ocupa várias telas antes de apresentar prova do trabalho; pode ser reduzido para acelerar triagem.

### Etapa 3 — Navegação móvel: saudável

Saúde geral: **boa**.

- Botão possui estado expandido/fechado.
- Foco é levado ao primeiro item.
- Escape fecha e restaura foco.
- Alvos têm tamanho adequado.

### Etapa 4 — Case Einstein: forte

Saúde geral: **muito boa**.

- Contexto, papel, decisões, evidências e limites estão claros.
- Separar 84,3% de percepção e 56,25% de interpretação é intelectualmente honesto.
- A abertura poderia declarar a contribuição de Israel em uma frase mais direta.
- O título `Consumo de Resultados` é genérico; um título orientado ao problema seria mais memorável.

### Etapa 5 — Hub de Liquidez: inadequado para publicação ampla

Saúde geral: **crítica**.

- Visual e estrutura são bons.
- `Contribuição individual pendente de confirmação` compromete o objetivo de demonstrar senioridade.
- A página declara ausência de autorização formal e usa termos internos.
- Deve migrar para apresentação privada até validação.

### Etapa 6 — Currículo: bom, com ajustes de credibilidade

Saúde geral: **boa**.

- Uma página, escaneável e coerente com o portfólio.
- Datas principais estão alinhadas com o site.
- Formação contínua precisa de instituição e ano.
- Sobreposição da consultoria precisa de explicação mais precisa.
- A seção `Trabalho selecionado` inclui projetos ainda não atribuídos/publicáveis.

## Checklist operacional recomendado

### Antes de enviar a recrutadores

- [ ] Remover ou ocultar os três dossiês Itaú públicos.
- [ ] Remover `150 → 27s / −82%` da home até recuperar a fonte.
- [ ] Corrigir `Registros com IA complementam o conjunto`.
- [ ] Atualizar canonical, Open Graph, Twitter, JSON-LD, robots e sitemap.
- [ ] Garantir que somente uma versão pública seja tratada como canônica.
- [ ] Revisar autorização e confidencialidade de todo material associado a empregadores.
- [ ] Explicar corretamente a sobreposição de consultoria e vínculos.
- [ ] Informar instituição e ano de cada formação contínua.
- [ ] Remover competências que não possam ser defendidas com exemplos.

### Para elevar a qualidade competitiva

- [ ] Manter apenas dois ou três cases fortes na home.
- [ ] Adicionar um segundo case completo com contribuição individual clara.
- [ ] Resumir cards para problema, papel, decisão e evidência.
- [ ] Reduzir ressalvas repetidas e concentrá-las em uma nota final.
- [ ] Conectar domínio próprio.
- [ ] Considerar e-mail profissional no domínio próprio.
- [ ] Validar contraste automatizado e navegação completa apenas por teclado.
- [ ] Testar zoom de 200%, leitor de tela e estados de foco em todas as rotas.

## Limites da auditoria

- A auditoria não confirma fatos profissionais externos, autorização de empregadores ou conformidade com NDA.
- Não confirma conformidade WCAG integral; foram verificados estrutura, nomes acessíveis, foco, menu, reflow e sinais visuais observáveis.
- Não substitui revisão jurídica de confidencialidade.
- A autenticidade e atualidade do retrato devem ser confirmadas pelo autor.

## Recomendação final

O portfólio já demonstra craft e pensamento crítico. Para maximizar confiança com recrutadores, a próxima versão deve ser **mais seletiva, afirmativa e verificável**: um case completo excelente vale mais do que vários dossiês que dizem explicitamente ainda não poder atribuir autoria ou resultado.
