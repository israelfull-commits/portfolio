# Diagnóstico integral do portfólio — 25/11/2026

## Parecer

A base de navegação, responsividade e identidade está funcionando. O maior trabalho restante está na precisão editorial, na demonstração de decisões seniores e na apresentação das entregas. O portfólio não precisa de outra identidade visual; precisa que cada afirmação, figura e seção cumpra uma função clara na avaliação de um recrutador.

A auditoria encontrou seis prioridades P1, oito P2 e duas P3. P1 significa impacto relevante na compreensão ou credibilidade; P2, inconsistência ou atrito moderado; P3, refinamento. Nenhum bloqueio P0 de navegação foi observado nos cenários executados. Os achados abaixo são diagnóstico e propostas, não correções já aplicadas.

## Escopo e evidências

- Produção: https://israel-rozar-portfolio.irozar.chatgpt.site/.
- Dez rotas: home, oito cases/módulos e página inexistente. Vinte capturas principais, desktop 1440×900 e mobile 390×844; checagem de reflow 320 px em todas as rotas.
- Figma comparado: frame 412:6100, arquivo YIHybVXPe 0Hfmja 1 hAyzQZ. Comparação de conteúdo e arquitetura; as capturas têm viewports diferentes, portanto não sustentam afirmações de equivalência pixel a pixel.
- Código inspecionado: site/src; HEAD 464ad6118d5647aaeb525865225843e5785b1f24. Produção foi a referência funcional; código foi usado para localizar causas.
- Evidências desta execução: qa/auditoria-integral-2026-11-25/evidence.json, interactions.json e reading-probe.json. Relatórios anteriores serviram para contexto, não como prova de que algo continuava resolvido.
- Browser integrado indisponível nesta execução; captura realizada com Playwright CLI.
- Skill aplicada: Product Design/audit. Não houve pesquisa com recrutadores nesta rodada.

## Jornada avaliada

1. Identificar profissional, cargo, experiência e domínios na home.
2. Comparar quatro projetos e escolher um case.
3. Ler contexto, pesquisa, decisões, solução, resultados e autoria.
4. Ampliar figuras e consultar informações complementares.
5. Continuar para outro case ou retornar à vitrine.
6. Acessar currículo e contato.
7. Navegar por teclado e celular e recuperar-se de endereço inexistente.

## Resultado funcional observado

- Dez rotas carregaram e apresentaram exatamente um H1; oito cases têm sete capítulos cada.
- Nenhum pageerror capturado; nenhuma rolagem horizontal em 1440,390 ou 320 px nas páginas avaliadas.
- Nenhuma violação automática nas regras axe selecionadas: WCAG 2 A/AA,2.1 AA e 2.2 AA, nas dez rotas desktop. Modal aberto também sem violação automática detectada.
- Há verificações incompletas de contraste/ARIA no axe que exigem revisão manual; o resultado não certifica AA ou AAA.
- Salto para conteúdo moveu foco ao main; menu mobile moveu foco para Cases, fechou com Escape e devolveu foco a Menu.
- Ampliação abriu dentro da tela móvel, alternou tamanho original, fechou com Escape e devolveu foco ao acionador.
- Accordion de fontes abriu. PDF respondeu 200, application/pdf e assinatura %PDF.
- Preferência escura manteve canvasrgb(252,249,242) e texto coerente; redução de movimento foi ativada no cenário de preferência.
- Ciclo dos principais cases confirmado: Einstein→ItaúHub→Claro→Neoenergia→Einstein.

## Prioridades e correções propostas

### F01 — P1 — Métrica da Claro mudou de significado entre card e case

**Observado:** o card apresenta “22 jornadas mapeadas ·70+ validações”. O capítulo de resumo do case apresenta 22 jornadas e 70 oportunidades de melhoria. O número parecido não torna as medidas equivalentes.

**Impacto:** o recrutador recebe duas descrições do trabalho e pode interpretar que houve 70 sessões ou verificações de validação.

**Como deve ficar:** usar “22 jornadas mapeadas ·70 oportunidades de melhoria” na vitrine e no Figma, se esse for o dado aprovado; se 70+ validações for outra medida real, documentá-la separadamente no case com método, unidade e fonte. Não transformar oportunidades em testes. Criar registro único de métricas por projeto, incluindo rótulo e unidade, não apenas o número.

**Evidência:** home-desktop.png; claro-desktop.png; evidence.json/home.links e capítulos do Claro. O Sentinel atual não detecta essa divergência semântica.

### F02 — P1 — Escopo e reflexão idênticos nos cinco módulos do Itaú

**Observado:** Hub, Vencimentos, Movimentações, Campanhas e Registros repetem os mesmos parágrafos “Mantivemos fora da primeira camada visual configurações avançadas...” e “Ampliaria o acompanhamento longitudinal após o handoff...”.

**Impacto:** a presença formal do bloco não demonstra reflexão específica; casos de tarefas diferentes parecem preenchidos pelo mesmo template.

**Como deve ficar:** registrar um corte e uma reflexão próprios de cada projeto, com decisão, motivo operacional e consequência. Pautas a confirmar com o autor: janela de projeção no Hub; tratamento de urgência em Vencimentos; persistência do provisionado em Movimentações; publicação e processamento em lote em Campanhas; revisão humana e fidelidade do resumo em Registros. Essas pautas não são fatos adicionais nem justificam inventar acontecimentos.

**Evidência:** evidence.json, capítuloimpacto dos cinco módulos; registros-desktop.png e demais rotasItaú.

### F03 — P1 — Decisões ainda não demonstram completamente o raciocínio sênior

**Observado:** módulosItaú listam três decisões, mas frequentemente apresentam apenas a solução e uma justificativa. Claro e Neoenergia descrevem organização de fluxos/serviços. A sequência gatilho→alternativas→trade-off→restrição→validação não aparece de forma completa e rastreável em três decisões de cada case. O desacordo construtivo e a autoria individual também não ficam claros na leitura principal.

**Como deve ficar:** para cada decisão real, usar cinco linhas curtas: problema observado; alternativas consideradas; escolha e custo aceito; restrição técnica/operacional; evidência usada para conferir a escolha. Separar “minha contribuição” de “entrega da equipe”. Relatar desacordo somente quando houver um episódio real documentado. Na ausência de registro, solicitar os dados ao autor em vez de preencher uma história.

**Evidência:** capítulosdecisoes capturados e cabeçalhos/credits. Referência: SENIOR_UX_PORTFOLIO_CANON.md.

### F04 — P1 — Capas e figuras principais reduzem a capacidade de avaliar o trabalho

**Observado:** as áreas de imagem das quatro capas principais medem aproximadamente 3,46:1 nesta composição, com conteúdo contido e pequeno. Einstein mostra dois documentos com anotações; Claro, laptop+ celular; Neoenergia, capa institucional; Movimentações e Campanhas, mosaicos de telas. A regra canônica pede uma entrega principal 16:9. No celular, vários rótulos internos não são legíveis antes da ampliação.

**Como deve ficar:** uma figura principal 16:9 por case com recorte preciso e texto de apoioHTML. Einstein: um componente/laudo com resultado e referência; Hub: uma tela com resumo financeiro e fila; Claro: uma etapa de contratação com oferta/resumo; Neoenergia: recorte de um blueprint que mostre a relação atendimento/operação. Manter acervo e mosaicos como documentação complementar. Não esticar telas nem cortar texto clínico para obter a proporção.

**Evidência:** cases-principais.png, modulos-itau.png, mobile-main.png e mobile-more.png; medidas em evidence.json. A ampliação funciona, mas não substitui uma boa leitura inicial.

### F05 — P1 — Figma e produção ainda representam estruturas diferentes

**Observado:** seleção de quatro projetos e paleta geral coincidem. Figma mantém navegação com Especialidades/Trajetória, quatro cards de especialidade, trajetória separada, hero com LinkedIn e contato amplo. Produção usaCases/Sobre/Currículo, seçãoSobre com trajetória condensada, CTA dePDF e contato compacto.

**Como deve ficar:** adotar a home compacta atual como estrutura de referência, conforme a seleção confirmada; atualizar o frame com as mesmas seções, rótulos e ações. Vincular os componentes às mesmas definições de conteúdo e tokens. Se houver uma versão exploratória maior, identificá-la como alternativa, sem apresentá-la como re produção da publicação.

**Evidência:** figma-home.png versus home-desktop.png. A diferença é estrutural, não apenas uma margem fora do padrão.

### F06 — P1 — Afirmações empíricas e de conformidade precisam de contexto verificável

**Observado:** há afirmações como “até 40%do tempo” na Claro, necessidade de identificação em“3 segundos” no Einstein, percentuais 81,6/77,8/58,8/56,2 e texto de conformidadeWCAG AAA em figura. A apresentação não associa sistematicamente cada afirmação a amostra, tarefa, período e verificação correspondente.

**Como deve ficar:** para cada dado, apresentar medida, denominador/amostra, procedimento, período e referência. Distinguir objetivo de design de resultado observado. Para acessibilidade, informar critérios efetivamente verificados e evidências, em vez de deduzir conformidade integral de tamanho de fonte e uso redundante de cor. Manter dados de saúde/finanças sintetizados ou anonimizados e preservar termos clínicos/financeiros acordados.

**Evidência:** capítulosdescoberta/impacto e figuras do Einstein e Claro em evidence.json. É uma necessidade de rastreabilidade da apresentação, não conclusão sobre a veracidade histórica dos dados.

### F07 — P2 — “Resultado-chave” agrupa entregas e efeitos de natureza diferente

**Observado:**14 entregáveis,5 blueprints e descrições de interface aparecem sob o mesmo rótuloResultado-chave. Isso informa escopo ou produção, mas não necessariamente efeito de negócio ou mudança observada.

**Como deve ficar:** usar “Entrega principal” para artefatos. Reservar “Resultado observado” para efeitos com critério e base identificados. Se ambos existirem, mostrá-los em campos separados. Preservar números sem transformar quantidades de artefatos em percentuais de impacto.

### F08 — P2 — Tempo de leitura incompleto e método contaminado por elementos ocultos

**Observado:** Vencimentos não mostra relógio/tempo. Estimativas existentes foram calculadas comtextContent dos capítulos, que inclui cópias das legendas em modais fechados e controles comoFechar/Ver em tamanho original. Uma conferência cominnerText encontrou 1260 palavras visíveis no Einstein,909 na Claro e 1082 na Neoenergia, ante tempos exibidos 8/6/7 min. A200 palavras/minuto, o cálculo exclusivamente textual desses trechos seria 7/5/6 min; figuras podem justificar outra estimativa se o método for declarado.

**Como deve ficar:** criar cálculo reproduzível sobre texto editorial, excluindo modais, controles e anexos fechados; escolher explicitamente se haverá tempo adicional para figuras. Aplicar a mesma regra a todos os casos, incluindoVencimentos, e compartilhar o resultado com cards/cabeçalhos/Figma.

**Evidência:** reading-probe.json; vencimentos-mobile.png; CaseReadingTime.tsx.

### F09 — P2 — Tokens de texto e escalas diferem entre home e cases

**Observado:**H1 da home usa#1A201C; H1 dos cases usa#111B15. Texto secundário também varia de#4A554Epara#3B4740. A fonte se mantémPlus Jakarta Sans, mas há aliases e sobrescritas que produzem resultados distintos. Rótulos dos cases são 12 px, enquanto os metadados refinados dos cards são 14 px.

**Como deve ficar:** definir um token semântico por função e mapear seu valor ao sistema aprovado. Consolidar a cascata e documentar quando 12 px é aceitável para etiquetas e quando 14 pxé necessário para metadados de leitura. Não trocar a fonte aprovada apenas por preferência estética. Cores originais dentro das interfaces dos projetos devem continuar preservadas.

**Evidência:** estilos computados de h 1/.cp-meta-label/.case-reading-time em evidence.json. As cores atuais não foram classificadas como falha de contraste por esse motivo.

### F10 — P2 — Trajetória mistura vínculo, atividade paralela e formação

**Observado:** a home apresentaItaú 2024–2026 antes da consultoria 2022–atual e termina com“Formação&Base ·Ciência da Computação...2006–2019”. A composição não esclarece simultaneidade e pode parecer atribuir esse intervalo ao curso. NoFigma a narrativa é diferente.

**Como deve ficar:** manter vínculos em ordem cronológica; marcar consultoria como atividade paralela quando aplicável; separar formação dos empregos anteriores. Confirmar as datas reais antes de associá-las a uma titulação. Exemplo estrutural: experiência recente → atuação independente(paralela) → experiências anteriores → formação.

### F11 — P2 — Siglas e termos internos ainda elevam o custo de leitura

**Observado:**IFA, EA, CEP, CEPPlus, frontstage/backstage, multi-tenant e nomes de componentes aparecem em alguns trechos sem tradução imediata para o problema de produto.

**Como deve ficar:** explicar a primeira ocorrência e o efeito na tarefa; manter o nome técnico entre parênteses quando útil. Exemplo: “Saldo provisionado persistente no cabeçalho: consulta entre jornadas sem abrir o extrato”. Usar detalhes técnicos completos nos blocos de decisão/apêndice, sem retirar vocabulário relevante para lideranças e ATS.

### F12 — P2 — Página inexistente é apresentada como 404, mas respondeHTTP 200

**Observado:**/pagina-inexistente-auditoriaexibe a recuperação correta e noindex, mas a respostaHTTP é 200.

**Como deve ficar:** manterHTTP 200 nas rotas válidas e HTTP 404 para destinos inexistentes, preservando a tela de recuperação. Ajustar tratamento de rotas na hospedagem atual; a presença de 404.html no pacote não garante o códigoHTTPcorreto na configuraçãoSPA.

### F13 — P2 — Fontes têm alvos menores que o padrão interno

**Observado:** alguns links de fonte dos módulosItaú têm 21 pxde altura no celular. O padrão interno adotado para controles é 44 px.

**Como deve ficar:** ampliar área clicável e espaçamento dos links de fonte. Isso é uma divergência do padrão de conforto do projeto; não é automaticamente violaçãoWCAG 2.5.8, que admite exceções de espaçamento e links em linha.

### F14 — P2 — Registros tem descoberta menos direta na home

**Observado:**Registros está publicado e conectado à sequência de módulos, mas a barraOutros recortes lista apenasVencimentos, Movimentações e Campanhas.

**Como deve ficar:** manter os quatro projetos principais e oferecer “Outros módulos do IFA” com os quatro recortes, incluindoRegistros; preferir expansão discreta ou página de índice se a barra ficar extensa. Evitar que a descoberta dependa de percorrerPróximo case.

### F15 — P3 — Texto introdutório dos cases adia o acesso à entrega

**Observado:** no celular, introdução, quatro campos de metadados e figura ocupam uma longa sequência antes do Resumoexecutivo. OEinsteintem subtítulo especialmente extenso.

**Como deve ficar:** título concreto, subtítulo curto, papel/período visíveis, entrega principal e resumo rápido de problema→contribuição→entrega; metadados complementares podem vir depois. Preservar a estrutura completa para leitura aprofundada. Conferir a ordem com recrutadores em uma tarefa curta de identificação.

### F16 — P3 — Rótulos de ação variam entre arquivo de design e site

**Observado:**Conhecer meu trabalho / Ver projetos, Ver projeto completo/Ver estudo de caso / Ver case e contatos amplos/compactos convivem entre os artefatos.

**Como deve ficar:** definir rótulos por contexto: Ver projetos na hero, Ver case nos cards, Voltar aos cases nos artigos e Enviar e-mailno contato. Diferenciar variação deliberada de texto esquecido na sincronização.

## Matriz da home: elemento por elemento

|Elemento/componente|Diagnóstico|Recomendação concreta|
|---|---|---|
|MarcaIR e nome|Reconhecíveis; retorno à home disponível|Manter e preservar área de foco|
|Cabeçalho desktop|Cases, Sobre, Currículo e contato operáveis|Sincronizar os rótulos do Figma(F05)|
|Menu mobile|Expansão, foco e Escape passaram|Preservar comportamento; repetir teste após mudanças|
|Salto para conteúdo|Foco foi ao main|Manter destino focável|
|Badge de cargo|Senior Product Designer visível no início|Manter; não substituir por slogan|
|Localização|São Paulo · Brasil legível|Manter concisa|
|H1|Explica os domínios, sem frase genérica decomplexidade|Preservar direção e especificidade|
|Introdução|Experiência desde 2006 e atuação recente explícitas|Acrescentar contribuição somente com fatos confirmados|
|Ver projetos|Âncora clara|Manter como ação principal|
|CurrículoPDF|Documento válido e acessível|Manter data/conteúdo do PDF sob revisão editorial|
|E-mail na hero|Contato direto|Preservar; testar também com cliente de e-mail real|
|Retrato|Carregado, comalt e proporção preservada|Manter qualidade e corte responsivo|
|Título da vitrine|Seção identificável|Manter|
|Texto da vitrine|Explica o que será encontrado|Evitar repetir domínios em vários parágrafos|
|Einstein destacado|Boa prioridade e acesso evidente|AplicarF04, F06 e F07 na apresentação do case|
|Imagem do destaque|Entrega concreta presente na home|Manter equivalência visual ao entrar no case|
|CardItaú|Papel, escopo e ação claros|Explicar contagem dos quatro módulos no aprofundamento|
|CardClaro|Boa hierarquia, métrica semântica divergente|CorrigirF01 antes de novo polimento|
|CardNeoenergia|Quantidades 4/5/118 coincidem com o relato|Manter unidades e fonte junto ao aprofundamento|
|Rodapés dos cards|Relógios e ações alinhados; CTA44 px|Automatizar cálculoF08|
|Barra de módulosItaú|Compacta e diferenciada dos casos principais|Completar descoberta com Registros(F14)|
|Sobre minha atuação|Leitura direta, sem duplicar toda a trajetória|Conectar especialidades aos exemplos dos cases|
|Menção aIAeWCAG|Temas relevantes, apresentados sucintamente|Demonstrar decisões correspondentes nos cases|
|Lista de trajetória|Conteúdo disponível, agrupamento ambíguo|AplicarF10|
|Formação|Misturada à trajetória|Separar titulação, instituição e período confirmado|
|Contato compacto|E-mail e LinkedIn evidentes|Uniformizar rótulo com contexto F16|
|Footer/Voltar ao topo|Retorno e identificação presentes|Preservar|

## Matriz dos componentes compartilhados dos cases

|Componente|Diagnóstico|Como deve ficar|
|---|---|---|
|Cabeçalho compartilhado|Coerente entre rotas|Mesmo contrato de navegação e foco|
|Voltar aos cases|Destino disponível|Manter retorno à vitrine|
|Badge de domínio|Identifica setor|Usar linguagem compreensível|
|Cliente/equipe/período|Dados úteis; períodos Itaú menos explícitos|Padronizar informação temporal confirmada|
|Título do case|NívelH1 único, títulos concretos|Evitar amplitude maior que o conteúdo|
|Subtítulo|Varia de frase curta a parágrafo extenso|AplicarF15|
|Tempo de leitura|Presente em sete dos oito cases|AplicarF08 em todos|
|Meu papel|Distingue função no projeto|Separar autoria individual e colaboração no corpo|
|Equipe|Visível no topo|Manter nomes/funções confirmados|
|Escopo|Presente|Descrever fronteira técnica, não apenas método|
|Resultado-chave|Mistura artefato e efeito|AplicarF07|
|Figura principal|Qualidade varia entre interface, mosaico e capa institucional|AplicarF04|
|Legenda|Explica conteúdo; algumas longas|Dizer o que observar na figura em uma frase|
|Ver ampliado|Funciona com botão e nome acessível|Preservar; usar recorte legível antes do clique|
|Modal de imagem|Cabe na tela; abre/fecha e restaura foco|Manter; complementar descriçãoHTMLde conteúdo essencial|
|Tamanho original|Alternância operável|Manter controles de zoom visíveis|
|Abrir original|Acesso à imagem disponível|Manter indicação de nova aba|
|Índice de capítulos|Sete entradas coerentes com o template|Manter nomes orientados à pergunta do leitor|
|Numeração/etiquetas|Ajuda localização; etiquetas 12 px|Documentar escalaF09 e evitar duplicação ornamental|
|Títulos de capítulos|HierarquiaH2/H3 preservada|Títulos curtos seguidos de descrição concreta|
|Texto corrido|Família coerente, tom técnico irregular|AplicarF11 e especificidade por projeto|
|Cards de conteúdo|Agrupam público, decisões e reflexão|Conter uma ideia completa por card|
|Painéis numéricos|Há dados de escopo e pesquisa|AplicarF01, F06 e F07|
|Callouts|Destacam aprendizado|Ancorar em uma decisão ou observação específica|
|Imagens inline|Carregaram; escalas e proporções variadas|Separar evidência principal de acervo amplo|
|Accordions de fontes|Operáveis e com agrupamento temático|Completar rastreabilidadeF06 e áreas de toqueF13|
|Navegação anterior/próximo|Ciclo principal passou|Preservar; completar descoberta dos módulos|
|Contato dos cases|Ações disponíveis|Alinhar linguagem à home sem eliminar profundidade útil|
|Footer|Identificação e retorno presentes|Manter|
|Estado 404|Recuperação visual clara|AplicarHTTP 404 real(F12)|

## Comparação entre cases

|Case|Força atual|Principal oportunidade|
|---|---|---|
|Einstein|Relaciona pesquisa, conteúdo clínico e sistema de componentes; traz indicadores|Apresentar uma entrega principal legível; explicitar método dos indicadores; estruturar decisões e autoria|
|ItaúHub|Interface concreta e três decisões sobre informação financeira|Documentar alternativas/restrições; particularizar reflexão; distinguir entrega de efeito|
|Claro|Relaciona atendimento,22 jornadas e paridade de canais|Corrigir 70 oportunidades/validações; mostrar uma etapa-chave; contextualizar 40%|
|Neoenergia|Explicita 4 distribuidoras,5 blueprints e 118 ideias|Abrir com recorte de serviço em vez da capa institucional; separar mapa do processo de decisões de priorização|
|Vencimentos|Consulta e atuação bem delimitadas|Adicionar leitura; mostrar tratamento de urgência/estados; reflexão própria|
|Movimentações|Distingue informação persistente e contextual|Trocar mosaico por uma tela explicativa e comparar a alternativa escolhida com a descartada|
|Campanhas|Explica configuração, processamento e acompanhamento|Mostrar uma transição de estado legível; particularizar restrição de publicação e reflexão|
|Registros|Relaciona resumo assistido, histórico e revisão humana|Tornar descoberta direta; aproximar diagrama de uma interação concreta; definir qualidade do resumo com procedimento|

## Capítulo por capítulo

A matriz seguinte cobre os 56 capítulos dos oito cases. “Conferido” significa que o capítulo foi lido no DOM capturado; não representa confirmação independente do evento histórico.


### einstein

|Capítulo capturado|Diagnóstico e evolução recomendada|
|---|---|
|resumo — Organizar resultados sem perder o contexto clínico.|Escopo e números reconhecíveis; separar entrega de impacto(F07).|
|contexto — Uma hierarquia que funcione na tela e no papel.|Problema clínico e públicos identificados; explicitar minha contribuição e fronteiras.|
|descoberta — Do documento ao dado.|Taxonomia e pesquisa presentes; contextualizar 80+ exames e a afirmação de 3 segundos(F06).|
|decisoes — Preservar relações entre resultado, referência e contexto.|Anatomia de componente bem ilustrada; faltam alternativas/custo aceito/checagem por decisão(F03).|
|solucao — Uma estrutura única para qualquer tipo de exame.|Exemplos por tipo de exame; selecionar figura principal legível e manter texto clínico(F04).|
|impacto — Clareza de leitura e diagnóstico clínico: papéis complementares.|Quatro percentuais apresentados; associar denominadores/método e preservar interpretação correta(F06).|
|evidencias — Pesquisa, entregáveis e colaboração.|Créditos e conformidade organizados; vincular cada indicador ao registro correspondente.|

### itau

|Capítulo capturado|Diagnóstico e evolução recomendada|
|---|---|
|resumo — O projeto em perspectiva.|Objetivo financeiro claro; rótuloResultado-chave descreve entrega(F07).|
|contexto — Contexto, problema e objetivo.|Público e objetivo apresentados; explicar termos financeiros na primeira ocorrência(F11).|
|descoberta — Descoberta e critérios de decisão.|Recorte de interface descrito; explicitar a evidência que orientou cada decisão.|
|decisoes — Decisões e suas razões.|Três decisões listadas; acrescentar alternativas, restrição e validação(F03).|
|solucao — Como a solução organiza a jornada.|Interface e sequência da tarefa disponíveis; focalizar valores e janela temporal na figura(F04).|
|impacto — Entregas e aprendizado.|Texto de escopo/reflexão repetido nos outros quatro módulos(F02).|
|evidencias — Fontes, colaboração e alcance.|Fontes e autoria disponíveis; links de 21 pxno mobile(F13).|

### claro

|Capítulo capturado|Diagnóstico e evolução recomendada|
|---|---|
|resumo — Redesenho da operação comercial e redução de atrito na venda multicanal.|70 oportunidades no case versus 70+ validações na vitrine(F01).|
|contexto — Uma operação de alta densidade dividida entre balcão físico e mobilidade.|Cenários de operação comercial definidos; explicitar autoria individual.|
|descoberta — Compreender a rotina real dos atendentes antes de desenhar interfaces.|20 entrevistas/três dias deworkshops; contextualizar 40%do tempo(F06).|
|decisoes — Decomposição de 22 jornadas de atendimento e aprendizados operacionais.|22 jornadas e lógica de fluxo; ampliar raciocínio de escolha, não só a solução(F03).|
|solucao — Navegação progressiva, resumo financeiro visível e preservação do contexto do cliente.|Interfaces e componentes presentes; uma tela ou etapa por figura(F04).|
|impacto — Da jornada do chip às interfaces desktop e mobile padronizadas.|Demonstra paridade de canais; separar entrega de resultado observado(F07).|
|evidencias — Governança do projeto, colaboração multidisciplinar e impacto.|Fontes/colaboração presentes; identificar fonte de cada número apresentado.|

### neoenergia

|Capítulo capturado|Diagnóstico e evolução recomendada|
|---|---|
|resumo — Unificação da infraestrutura de atendimento para 34 milhões de pessoas.|Dados 4/5/118 e abrangência explícitos; distinguir número de artefatos e efeito(F07).|
|contexto — Cadeia de serviços fragmentada em um ecossistema de infraestrutura crítica.|Relação entre atendimento eoperação clara.|
|descoberta — Auditoria de backstage: quando a insatisfação com a fatura revela silos operacionais.|Jornadas e necessidadesapresentadas; explicitar papel individual e critérios do estudo.|
|decisoes — Os 5 estágios do ciclo de vida do cliente mapeados em Service Blueprints.|Cinco estágios representam organização do serviço; acrescentar decisões de corte/priorização e alternativas(F03).|
|solucao — Desburocratização de backoffice antes de redesenho de portal e Design System multi-tenant.|Blueprints demonstram frente e bastidores; usar recorte com leitura orientada(F04).|
|impacto — Matriz de 118 ideias priorizadas e baseline para o plano diretor de inovação.|Matriz 118 e prioridades presentes; separar plano de investimento de resultado executado.|
|evidencias — Fontes oficiais de P&D ANEEL, governança executiva e equipe EY × Livework.|Fontes em Drive/Slides/Figma agrupadas; testar permissões dos destinos com acesso externo.|

### vencimentos

|Capítulo capturado|Diagnóstico e evolução recomendada|
|---|---|
|resumo — O projeto em perspectiva.|Recorte de consulta/atuação claro; falta tempo de leitura(F08).|
|contexto — Contexto, problema e objetivo.|Evento financeiro e continuidade de atuação compreensíveis.|
|descoberta — Descoberta e critérios de decisão.|Distinguir hipótese, documento funcional e observação de uso.|
|decisoes — Decisões e suas razões.|Três decisões listadas; documentar alternativa/restrição e critério de tratamento deurgência(F03).|
|solucao — Como a solução organiza a jornada.|Tela concreta; destacar um estado e sua consequência(F04).|
|impacto — Entregas e aprendizado.|Reflexão e corte de escopo idênticos aos demais módulos(F02).|
|evidencias — Fontes, colaboração e alcance.|Fontes disponíveis com alvos de 21 px(F13).|

### movimentacoes

|Capítulo capturado|Diagnóstico e evolução recomendada|
|---|---|
|resumo — O projeto em perspectiva.|Objetivo de transiçãoEA→IFAcompreensível.|
|contexto — Contexto, problema e objetivo.|Explicar siglas e necessidade de consulta entre jornadas(F11).|
|descoberta — Descoberta e critérios de decisão.|Há referência a alternativas; mostrar comparação que levou à escolha(F03).|
|decisoes — Decisões e suas razões.|Três decisões específicas; completar custos aceitos e evidência da escolha(F03).|
|solucao — Como a solução organiza a jornada.|Mosaico prejudica leitura; mostrar tela final e relação com cabeçalho(F04).|
|impacto — Entregas e aprendizado.|Corte e reflexão repetidos; particularizar a decisão de persistência(F02).|
|evidencias — Fontes, colaboração e alcance.|Referências disponíveis com alvos de 21 px(F13).|

### campanhas

|Capítulo capturado|Diagnóstico e evolução recomendada|
|---|---|
|resumo — O projeto em perspectiva.|Escopo administrativo claro.|
|contexto — Contexto, problema e objetivo.|Distingue configuração, execução e acompanhamento.|
|descoberta — Descoberta e critérios de decisão.|Regras e objetos presentes; ligar cada regra a uma necessidade operacional.|
|decisoes — Decisões e suas razões.|Há decisões de estado; explicitar alternativa, restrição e checagem(F03).|
|solucao — Como a solução organiza a jornada.|Screenflows em escala reduzida; focalizar uma transição real(F04).|
|impacto — Entregas e aprendizado.|Corte/reflexão genéricos; particularizar publicação eprocessamento(F02).|
|evidencias — Fontes, colaboração e alcance.|Fontes do produto disponíveis; ampliar alvos de 21 px(F13).|

### registros

|Capítulo capturado|Diagnóstico e evolução recomendada|
|---|---|
|resumo — O projeto em perspectiva.|Resumo assistido e históricoexplicitados; acesso indireto pela home(F14).|
|contexto — Contexto, problema e objetivo.|Responsabilidade humana e documentação do atendimento presentes.|
|descoberta — Descoberta e critérios de decisão.|Critérios de qualidade necessitam tarefas e procedimento demonstráveis.|
|decisoes — Decisões e suas razões.|Três direções listadas; documentar escolhas de revisão e fidelidade sem inventar sessão de teste(F03/F06).|
|solucao — Como a solução organiza a jornada.|Diagrama ajuda a orientação; complementar com interação concreta e dados sintetizados(F04).|
|impacto — Entregas e aprendizado.|Texto reaproveitado de outras operações; refletir sobre revisão e precisão de resumos(F02).|
|evidencias — Fontes, colaboração e alcance.|Créditos presentes; ligar cada mecanismo descrito ao artefato correspondente.|

## Evidências visuais aceitas

Capturas principais desta execução, na jornada de navegação:

1. Home desktop/mobile: home-desktop.png, home-mobile.png.
2. Abertura dos cases: cases-principais.png, mobile-main.png, mobile-more.png.
3. Módulos adicionais: modulos-itau.png, mobile-last.png.
4. Menu:11-menu-mobile.png.
5. Ampliação:12-ampliacao-mobile.pnge 13-original-mobile.png.
6. Fontes expandidas:14-fontes-expandidas.png.
7. Figma atual: figma-home.png.

Todos estão emqa/auditoria-integral-2026-11-25/. Os arquivos originais de cada rota permitem inspeção além das pranchas de comparação. As pranchas usam capturas reais; não são novas propostas de interface. Foram inspecionadas composição, primeiras dobras, figuras, conteúdo e estados selecionados. A leitura textual dos 56 capítulos foi cruzada com os registros de DOM da execução.

## Ordem operacional recomendada

1. Corrigir a semântica das métricasF01 e qualificar os dados/afirmaçõesF06.
2. Particularizar reflexão e escopoF02; completar decisões reaisF03.
3. Ajustar as capas/figurasF04 e os rótulos de resultadoF07.
4. Sincronizar a estrutura aprovada no FigmaF05.
5. Completar/automatizar leituraF08, consolidartokensF09 e reorganizar trajetóriaF10.
6. Reduzir siglas sem explicaçãoF11, corrigirHTTP 404F12, ampliar alvosF13 e completar descobertaF14.
7. Validar sequência móvelF15 e padronizar açõesF16.
8. Reexecutar testes das rotas afetadas e fazer uma tarefa de leitura rápida com recrutadores; registrar tempo para identificar contexto, contribuição e entrega, sem usar a inspeção técnica como substituto de pesquisa.

## Critérios de aceite para a próxima rodada

- Mesma unidade/rótulo de métrica em home, case e Figma.
- Cinco módulosItaú com escopo/reflexão próprios.
- Três decisões completas por case, apoiadas por registros reais.
- Uma entrega 16:9 legível como figura principal; nenhuma informação essencial apenas em imagem.
- Leitura presente em todos os cases com cálculo definido e atualizado.
- Mesma arquitetura aprovada no Figma e produção, ou variantes explicitamente identificadas.
- Rotas válidas 200; inválidas 404 com recuperação funcional.
- Reflow 320 px, teclado, foco, modal e fontes verificados.
- Revisão manual de contraste, especialmente em figuras/callouts, e testes com tecnologias assistivas.

## Referências e critérios

- [WCAG 2.2 — Reflow](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html): referência de 320 CSS px e exceções para conteúdo bidimensional.
- [WCAG 2.2 — Contrast Minimum](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html):4,5:1 para texto normal e 3:1 para texto grande.
- [WCAG 2.2 — Target Size Minimum](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html):24×24 CSS px com exceções; 44×44 é o critério aprimorado e padrão adotado no projeto.
- AGENTS.md e SENIOR_UX_PORTFOLIO_CANON.md: critérios editoriais, STAR, decisões, figuras, tokens e governança.

O axe inspeciona a interface HTML nas regras executadas; não certifica a legibilidade dos textos rasterizados nem a compreensão das narrativas. Não foram realizados testes com leitores de tela reais, Safari/Firefox ou participantes humanos nesta execução. Destinos externos de documentação e a entrega real de e-mail precisam de verificação específica de permissões/cliente. Esses pontos permanecem identificados para execução, sem receber status de aprovados.


Evidência focal de F01: [comparação de métrica](../qa/auditoria-integral-2026-11-25/diagnostico-metrica-claro.png).
