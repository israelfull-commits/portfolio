# CANON SENIOR UX & PRODUCT DESIGNER (UX COMPANION 2026)
## Diretrizes Operacionais, Heurísticas de Avaliação e Regras Permanentes para Portfólio e Cases

Este documento consolida integralmente os princípios técnicos, estruturais, editoriais e visuais extraídos das referências canônicas da **UX Companion 2026** (*Senior UX Portfolio Examples* e *20 UX Portfolio Mistakes That Cost You Interviews*). Ele atua como **especificação normativa obrigatória** para a arquitetura do site, a redação dos cases e a geração automatizada de telas e templates no plugin do Figma.

---

# PARTE I: A TRANSIÇÃO DIAGNÓSTICA (MID-LEVEL ➔ SENIOR ➔ LEAD)

Hiring managers e comitês executivos de design não avaliam se um designer sênior "sabe desenhar telas" — essa competência é pré-requisito presumido. O teste diagnóstico real avalia se o profissional **opera acima da tela (*operating above the screen*)**:
- **Junior (0–2 anos):** Foco em capacidade de produção, execução de tarefas bem delimitadas e primeiras noções de enquadramento de problema.
- **Mid-level (3–6 anos):** Julgamento sob restrição em projetos autocontidos, navegação com stakeholders diretos e autonomia de ponta a ponta na entrega de fluxos.
- **Senior (6–10 anos):** Julgamento sobre o sistema circundante: **gestão estratégica de stakeholders, contexto de negócio, direcionamento de equipe, restrições operacionais e clareza sobre o que NÃO foi construído e por quê**.
- **Lead / Principal (10+ anos):** Direcionamento estratégico, filosofia de contratação, modelos operacionais de design (*DesignOps*), alinhamento executivo e artefatos estratégicos que moldam a visão corporativa.

---

# PARTE II: OS 6 PILARES DE SINALIZAÇÃO SÊNIOR

### 1. Evidência de Liderança (Sem Necessidade de Cargo Formal)
A liderança em nível sênior não exige o título de "Gerente" ou "Head". Ela se manifesta através de ações documentadas:
- Mentoria ativa de designers juniores e plenos.
- Condução e facilitação de rituais de crítica de design (*critiques*) estruturados contra os objetivos do projeto.
- Definição de rumo em projetos de alta ambiguidade.
- Instituição de rituais e esteiras de trabalho que aumentaram a maturidade ou velocidade do time.
- **Fórmula de Redação:** Nomeie o movimento de liderança ➔ Nomeie o impacto concreto no time/operação ➔ Mantenha os fatos específicos e mensuráveis.

### 2. Pensamento Estratégico & Reenquadramento (Hardest to Fake)
É o sinal mais difícil de forjar e o mais valorizado por comitês de contratação:
- **Reenquadramento de Briefing (*Reframing*):** O momento em que o designer desafiou a solicitação inicial (ex.: *"A liderança solicitou uma nova tela; demonstrei com dados que o problema subjacente era de arquitetura de dados e redirecionamos o escopo"*).
- **Disciplina de Escopo (*What Wasn't Built*):** Documentar explicitamente as hipóteses, fluxos e componentes que foram intencionalmente descartados e as justificativas técnicas/negociais desse corte.
- **Ancoragem em Metas Estratégicas:** Conectar cada decisão de arquitetura da informação e interface às metas trimestrais (OKRs) da unidade de negócio.

### 3. Resultados de Negócio Triangulados (Além da Satisfação do Usuário)
Sêniores entendem o papel do design na viabilidade da empresa. Os resultados devem se enquadrar em três categorias canônicas:
- **Resultados de Receita (*Revenue-linked*):** Taxa de conversão, redução de churn ou evasão de funil comparada a uma linha de base histórica (*baseline*).
- **Resultados de Eficiência/Custo (*Cost-linked*):** Redução no volume de chamados de suporte, diminuição do tempo operacional de atendimento e economia de horas técnicas.
- **Resultados de Risco e Conformidade (*Risk-linked*):** Cruciais em indústrias reguladas (Saúde, Fintech, Energia). Redução de não conformidades regulatórias (BACEN, ANS, ANEEL, LGPD), eliminação de erros críticos em laudos médicos ou operações financeiras.

### 4. Gestão de Conflitos e Influência com Stakeholders
Comitês de entrevista buscam evidências de maturidade relacional. Três padrões de case se destacam:
- **O Case de Desacordo Construtivo (*The Disagreement Case Study*):** Situação em que o designer discordou tecnicamente de um PM, líder de engenharia ou executivo e conduziu o debate a uma resolução produtiva. Deve nomear a tensão, a estratégia de argumentação, concessões aceitas e aprendizados. **Este formato supera consistentemente cases que relatam apenas "vitórias fáceis".**
- **A Parceria Multidisciplinar (*Cross-Functional Partnership*):** Integração ativa de engenharia, jurídico, dados e pesquisa desde o D0 para co-construir restrições e contratos de serviço.
- **A Escalada Executiva (*Executive Escalation*):** Tradução de riscos de experiência em relatórios executivos para diretoria e C-level.

### 5. A Decisão como Unidade de Valor (*Decision Evidence*)
**"Decisões são a unidade de valor em um portfólio."** Diagramas de processos, personas genéricas e jornadas fictícias não substituem evidências de decisão.
Todo case sênior deve detalhar **pelo menos 3 decisões críticas de design**, cobrindo rigorosamente a estrutura:
1. **O Gatilho / Problema Real:** A restrição ou descoberta técnica que impôs a decisão.
2. **As Alternativas Consideradas:** No mínimo duas rotas de arquitetura/layout avaliadas.
3. **O Trade-off Aceito:** O que foi sacrificado (ex.: velocidade de carregamento vs. riqueza visual; densidade de dados vs. curva de aprendizado).
4. **A Restrição Operacional:** Limitações de API legada, prazos regulatórios ou capacidade de engenharia.
5. **A Validação:** Como a decisão foi testada e sustentada (telemetria, testes de usabilidade com especialistas ou benchmark).

### 6. Pensamento Sistêmico & Governança (Systems Thinking)
Em um portfólio de 3 a 4 cases, **pelo menos 1 case deve ser puramente sistêmico**:
- Criação, expansão ou governança de Design System (tokens semânticos, componentização, paridade código↔Figma).
- Framework transversal de Acessibilidade (auditorias WCAG 2.2 AA/AAA, fluxos assistivos).
- Estruturação de ResearchOps ou rituais de critique.

---

# PARTE III: OS 20 ERROS FATAIS DE PORTFÓLIO & ANTÍDOTOS OPERACIONAIS

### Falhas Estruturais (1 a 6)
1. **Excesso de Cases:** Portfólios com 7 a 10 cases diluem a média e mostram incapacidade de priorização. **Regra:** Manter estritamente **3 cases profundos (no máximo 4)**.
2. **Inconsistência de Profundidade:** Um case de 10 minutos seguido por um case de 1 minuto denota falta de rigor. **Regra:** Todos os cases mestres devem ter estrutura e densidade comparáveis.
3. **Falta de Declaração Clara do Problema:** Abrir com *"O cliente queria um app"* falha nos primeiros 30 segundos. **Regra:** O primeiro parágrafo do case deve sintetizar a dor real de negócio e usuário subjacente ao briefing.
4. **Ausência de Decisões Visíveis:** Se o revisor ler o case e não souber nomear 3 decisões exclusivas do designer, o case falhou.
5. **Contato Oculto:** Forçar cliques para achar e-mail ou LinkedIn derruba conversões com recrutadores. **Regra:** Contato claro e visível no cabeçalho e na dobra inicial da Home.
6. **Sinal de Senioridade Oculto:** O recrutador precisa saber o nível nos primeiros 5 segundos. **Regra:** Posicionar acima da dobra: *"Senior Product Designer · 15+ anos · Saúde, Fintech & Energia"*.

### Falhas de Redação (7 a 12)
7. **Culto ao Processo (*Process Worship*):** Explicações longas sobre o *Double Diamond* ou metodologias teóricas que todo gestor já conhece. **Regra:** Cortar exposição de processo; focar nas decisões originadas por ele.
8. **Montagem de Métodos (*Methods Montage*):** Grades com 8 ícones genéricos (Personas, Mapa de Empatia, Card Sorting). **Regra:** Citar apenas os 1 ou 2 métodos que alteraram a rota do projeto e as descobertas específicas derivadas deles.
9. **Pronomes Vagos ("Nós fizemos", "Nós decidimos"):** O comitê avalia o candidato, não o coletivo. **Regra:** Especificar o papel individual: *"Liderei a pesquisa...", "Estruturei a taxonomia...", "Propus a arquitetura de tokens que o time de engenharia adotou"*.
10. **Métricas Infladas sem Linha de Base:** Números mágicos (*"Aumentou engajamento em 350%"*) destroem credibilidade. **Regra:** Evidências qualitativas honestas superam dados quantitativos sem contexto. Sempre apresentar métricas vinculadas a baselines claros.
11. **Linguagem Publicitária (*PR-Speak*):** Frases vazias como *"Reimaginamos a jornada para encantar o usuário"*. **Regra:** Proibição absoluta de clichês corporativos; usar tom técnico, direto e documental.
12. **Ausência de Reflexão Crítica:** Cases que terminam em triunfos perfeitos parecem artificiais. **Regra:** Toda conclusão deve conter o bloco *"O que eu faria diferente hoje / Trade-offs não resolvidos"*.

### Falhas Visuais (13 a 16)
13. **Sinal de Template de Bootcamp:** Personas roxas padronizadas e colagens de post-its. **Regra:** Layout editorial suíço, sóbrio, minimalista e com tipografia profissional.
14. **Intros Animadas e Splash Screens:** Telas de carregamento atrasam o revisor, que gasta apenas 30 segundos na triagem inicial. **Regra:** Zero telas de loading ou bloqueios de rolagem.
15. **Mosaicos de Imagens Ilegíveis (*Montage Hero Images*):** Compor 8 a 12 telas pequenas em um mockup distorcido. **Regra:** Cada evidência deve ser uma figura única em **16:9 de alta resolução**, onde textos e componentes são 100% legíveis.
16. **Falhas de Acessibilidade:** Textos de baixo contraste ou fontes menores que 14px em parágrafos. **Regra:** Conformidade estrita com **WCAG 2.2 AA/AAA** (contraste > 7:1 em texto e > 12:1 em badges).

### Falhas Meta (17 a 20)
17. **Portfólio Desatualizado:** Último case de 3 anos atrás comunica estagnação. **Regra:** Destacar o case mais recente e contextualizar projetos sob sigilo com entregáveis anonimizados.
18. **Ausência de Posicionamento sobre IA:** Em 2026, ignorar IA demonstra descompasso com a indústria. **Regra:** Apresentar posicionamento claro sobre automação assistida, aceleração de protótipos e supervisão humana crítica.
19. **Falta de Página/Seção "Sobre":** O recrutador busca entender princípios e motivações. **Regra:** Seção biográfica e de princípios executivos bem articulada na Home.
20. **Domínio Genérico ou Difícil:** Utilizar URLs de plataformas gratuitas. **Regra:** Identidade profissional consolidada e canônica.

---

# PARTE IV: ARQUITETURA CANÔNICA DE UM CASE STUDY SÊNIOR (9 BLOCOS)

Todo case gerado para o portfólio (seja no código React ou no template do Figma) deve seguir a estrutura de 9 blocos modulares:

```
[BLOCO 1: CABEÇALHO & SINALIZADORES]
- Breadcrumb (Voltar aos cases)
- Kicker: Tag da Indústria (ex.: SAÚDE DIAGNÓSTICA) + Empresa / Parceria + Ano
- Headline Executiva: O que foi solucionado em alto nível
- Subtítulo Técnico: Resumo do escopo de discovery, arquitetura e entrega

[BLOCO 2: TABELA DE METADADOS EXECUTIVOS]
- Papel Individual (ex.: Lead Designer / Senior Product Designer)
- Equipe Envolvida (ex.: Engenharia, Médicos Especialistas, PM)
- Metodologias Chave (1 a 2 métodos aplicados com impacto real)
- Período e Restrição Operacional

[BLOCO 3: MASTER HERO (FIGURA ÚNICA 16:9)]
- Interface principal canônica em alta definição (1152 × 648 px no Figma, moldura estúdio, zero bezel cortado).

[BLOCO 4: BARRA DE MÉTRICAS TRIANGULADAS]
- 3 a 5 cartões de métricas (Volume, Taxa de Erro, Redução de Tempo ou Cobertura Regulatória), ancorados em baseline.

[BLOCO 5: O PROBLEMA REAL & REENQUADRAMENTO]
- Situação herdada e limitações da abordagem anterior.
- O momento do reframing: como o briefing original foi questionado e redirecionado com dados.

[BLOCO 6: TRÊS DECISÕES ESTRUTURADAS DE DESIGN]
- Decisão 01: Modelo mental / Arquitetura da Informação (Gatilho ➔ Alternativas ➔ Trade-off).
- Decisão 02: Sistema de componentes / Paridade técnica (Restrição de API ➔ Solução).
- Decisão 03: Governança de acessibilidade e segurança clínica/financeira.

[BLOCO 7: O QUE NÃO FOI CONSTRUÍDO & GESTÃO DE CONFLITO]
- Escopo cortado intencionalmente e justificativas de negócio/engenharia.
- Desacordo construtivo: ponto de divergência com engenharia/PM e resolução adotada.

[BLOCO 8: IMPACTO DE NEGÓCIO & ENTREGÁVEIS TÉCNICOS]
- Resultados divididos por Receita, Custo ou Redução de Risco Regulatório.
- Lista objetiva de artefatos de entrega (Design Tokens, Specs de Handoff, Blueprints).

[BLOCO 9: REFLEXÃO CRÍTICA & NAVEGAÇÃO CIRCULAR]
- "O que eu faria diferente hoje com os recursos e tecnologias atuais".
- Próximo Case da esteira contínua de leitura.
```

---

# PARTE V: PROTOCOLO OPERACIONAL PARA O PLUGIN DO FIGMA

Para garantir que o gerador de telas do Figma reflita com 100% de fidelidade este calibre sênior e elimine erros de auto-layout e cortes:

1. **Auto-Layout e Dimensionamento de Telas:**
   - Todo container vertical principal de tela deve ter `primaryAxisSizingMode = 'AUTO'` (Hug Contents em altura) e `counterAxisSizingMode = 'FIXED'` (largura 1280px).
   - `clipsContent = false` em todas as seções e containers internos para evitar cortes de texto e sombras.
   - Textos que quebram linha devem possuir `textAutoResize = 'HEIGHT'` com largura calculada baseada na coluna (`layoutAlign = 'STRETCH'` / `layoutSizingHorizontal = 'FILL'`).

2. **Proporção Imutável de Imagens e Placeholders (16:9):**
   - Imagens de largura total: `1152 × 648 px` (16:9 exato).
   - Imagens de coluna de artigo (grid suíço): `856 × 482 px` (16:9 exato).
   - Imagens de cards complementares na Home: `508 × 286 px` (16:9 exato).
   - Zero colagens de mini-telas; uma única tela ou fluxo articulado com acabamento de estúdio fotográfico.

3. **Injeção de Blocos Sênior no Template de Case:**
   - O botão **"📄 Criar case template"** deve gerar rigorosamente a estrutura canônica dos 9 blocos, incluindo o bloco de **Decisões Estruturadas**, o bloco de **O que não foi construído** e o bloco de **Reflexão Crítica**.

4. **Zero Jargão e Respeito aos Tokens de Cor e Tipografia:**
   - Tipografia estrita: **Plus Jakarta Sans** (Regular 400, SemiBold 600, Bold 700).
   - Paleta oficial: Canvas `#FCF9F2`, Deep Pine `#0A3622`, Acid Lime `#CEFF1A`, Subtle `#F6F3EC`, Card `#FFFFFF`, Border Subtle `#EDE9DE`.

---

# PARTE VI: DIRETRIZES ESTRUTURAIS DE REDAÇÃO DOCUMENTAL (PLAIN LANGUAGE & ZERO JARGÃO)

Para evitar jargões genéricos, textos desconexos e viés publicitário ao utilizar IA para redigir cases e alimentar o plugin do Figma, é obrigatório seguir rigorosamente estas 5 práticas estruturais:

### 1. Definição Técnica de Papel e Tom de Voz
- **Papel:** Senior Product Designer com foco em UX, UI, Arquitetura da Informação e Acessibilidade.
- **Tom de Voz:** Estritamente objetivo, técnico, factual e direto, porém **simples e acessível**. Escreva como um especialista sênior explicando o projeto para um colega em uma conversa técnica franca.
- **Proibição de Subjetividade:** Proibição absoluta de adjetivos vagos, superlativos ou clichês de marketing (*"incrível"*, *"inovador"*, *"revolucionário"*, *"experiência fluida"*). Foque em documentar a arquitetura da informação, o discovery e as decisões de design.

### 2. Fornecimento de Dados Brutos (Estrutura STAR Estrita)
- Não solicite nem redija "histórias romanciadas". Toda narrativa deve ser construída pela articulação lógica de dados técnicos brutos estruturados:
  - **Situação:** Contexto real de negócios, dores operacionais e limitações técnicas herdadas.
  - **Tarefa:** Desafio estratégico delimitado em escopo e tempo (ex.: horizonte de 6 a 12 meses, metas OKR).
  - **Ação:** Métodos aplicados (governança de Design System, auditoria WCAG 2.2 AAA, heurísticas de Nielsen, prototipagem, contratos de interface).
  - **Resultado:** Dados exatos, métricas trianguladas (Receita, Custo, Risco) e entregáveis concretos.
- **Restrição de Fato:** Não adicionar informações ou inferências que não estejam amparadas nos fatos e premissas declaradas.

### 3. Geração Modular (Seção por Seção)
- A redação de um case deve ocorrer por blocos modulares estanques para preservar a especificidade técnica e profundidade uniforme:
  - *Etapa 1:* Visão Geral e Enquadramento do Problema de Negócio (Situação / Tarefa).
  - *Etapa 2:* Processo de Discovery e Pesquisa Contextual com Usuários.
  - *Etapa 3:* Decisões de Arquitetura de Informação, UI, Heurísticas e Acessibilidade (Ação).
  - *Etapa 4:* Disciplina de Escopo ("O Que NÃO Foi Construído") e Desacordo Construtivo.
  - *Etapa 5:* Resultados Mensuráveis e Reflexão Crítica Honesta (Resultados / Aprendizados).

### 4. Aplicação de Restrições (Negative Prompting & Vocabulário Proibido)
- **Lista de Exclusão Estrita:** É proibido utilizar os seguintes termos e suas variações:
  - *"interface amigável"*, *"experiência fluida"*, *"mergulhar no problema"*, *"colocar o usuário no centro"*, *"design limpo/clean"*, *"disruptivo"*, *"sinergia"*, *"revolucionário"*, *"divisor de águas"*, *"encantar o usuário"*, *"experiência mágica"*, *"double diamond"*, *"mapa de empatia"*, *"reimaginar"*.
- **Substituição Obrigatória por Engenharia de Design:** Em vez de clichês, descreva especificamente:
  - Quais **heurísticas de usabilidade (Nielsen)** foram aplicadas (ex.: visibilidade do status, prevenção de erros).
  - Quais **princípios Gestalt** organizam a visão (ex.: região comum, proximidade).
  - Quais **critérios WCAG 2.2** foram atendidos (ex.: contraste de texto > 7:1, badges > 12:1).
  - Como a **arquitetura de tokens** garante paridade 1:1 com a engenharia.

### 5. Injeção de Terminologia Técnica Canônica & Compreensível (Otimização para ATS & Lideranças)
- O texto deve incorporar de forma natural, simples e contextualizada os termos operacionais reconhecidos por sistemas de rastreamento de candidatos (ATS) e lideranças de produto:
  - *Human-Centered Design (HCD)*, *Product Discovery*, *Arquitetura da Informação*, *Design System Modular*, *Tokens Semânticos*, *Heurísticas de Usabilidade*, *WCAG 2.2 AAA*, *Taxonomia de Dados*, *Interoperabilidade Legada*, *Modelagem de Componentes*, *Custo Efetivo Total (CET)*.

### 6. Mandato de Aplicação no Plugin do Figma
- O plugin `Sincronizador Portfólio 1:1` e todos os scripts geradores de telas (`build_portfolio_figma_screens.py`) devem seguir integralmente estas regras de redação. Qualquer texto gerado para tela, capítulo, card ou callout técnico deve ser simples de entender, livre de jargões ocos e rigorosamente ancorado em dados factuais.


