type PreparationCase = {
  title: string
  subtitle: string
  discipline: string
  stage: string
  framing: string
  question: string
  verified: string[]
  decisions: Array<{
    label: string
    title: string
    description: string
  }>

  sources: string[]
  demonstrated: string[]
  missing: string[]
  nextValidation: string
  interviewQuestions: string[]

  visuals?: Array<{
    src: string
    width: number
    height: number
    alt: string
    label: string
    caption: string
  }>
}

export const cases: Record<string, PreparationCase> = {
  "registros-atendimento": {
    title: "Registros de Atendimento",

    subtitle: "Resumos assistidos por IA com revisão humana",

    discipline: "Product design · IA aplicada à operação",

    stage: "Estudo de caso estruturado · IA generativa e supervisão humana",

    framing:
      "Documentar um atendimento e recuperar seu contexto são tarefas conectadas. O recorte explora como resumos assistidos por IA podem apoiar o registro e a consulta do histórico sem retirar do profissional a responsabilidade pela informação registrada.",

    question:
      "Como reduzir o esforço de registro e facilitar a recuperação de contexto, mantendo fidelidade ao atendimento e controle humano sobre o conteúdo?",

    verified: [
      "Discovery e desenho de fluxo assistido por IA para geração de atas e sínteses de atendimento.",

      "Aproximação dos cinco resumos recentes diretamente no momento de consulta e registro do assessor.",

      "Delimitação de salvaguardas de conformidade: o texto gerado é uma sugestão editável, exigindo validação humana antes da persistência bancária.",
    ],

    decisions: [
      {
        label: "Contexto",

        title: "Histórico próximo da ação",

        description:
          "Aproximar os cinco resumos recentes da tarefa de atendimento para apoiar a retomada de contexto sem depender exclusivamente da memória do profissional.",
      },

      {
        label: "Assistência",

        title: "IA como apoio ao registro",

        description:
          "Usar o resumo como ponto de partida para o trabalho do profissional. A geração de texto, por si só, não demonstra que o registro esteja correto ou completo.",
      },

      {
        label: "Avaliação",

        title: "Qualidade além do tempo de tarefa",

        description:
          "A evolução do fluxo precisa considerar fidelidade, omissões, esforço de correção e consulta ao registro original, além da velocidade de preenchimento.",
      },
    ],

    sources: [
      "Acervo de exploração e design de produto íon for Advisors: Registros de Atendimento — Resumos inteligentes com IA.",
    ],

    demonstrated: [
      "Direção da proposta: consulta dos resumos recentes integrada ao contexto de atendimento.",

      "Apoio à elaboração do registro, preservando a revisão do profissional como critério de qualidade.",

      "Recorte de interação e critérios de avaliação apresentados nesta versão técnica.",
    ],

    missing: [
      "Os registros visuais mantêm dados cadastrais sintetizados e anonimizados para conformidade com a política de sigilo bancário (LGPD).",

      "Ganhos operacionais são estimados pelo tempo de transcrição manual vs. síntese assistida e não por medição causal automatizada.",

      "A implantação em produção plena segue o cronograma de releases corporativas da plataforma.",
    ],

    nextValidation:
      "Acrescentar as telas equivalentes do fluxo, identificar as contribuições de cada disciplina e relacionar o protocolo de avaliação às decisões descritas. A comparação deverá considerar qualidade e esforço de revisão do registro, além do tempo de tarefa.",

    interviewQuestions: [
      "Como o histórico recente ajuda o profissional a retomar o contexto do atendimento?",

      "Quais omissões ou alterações de sentido tornariam um resumo inadequado?",

      "Como avaliar o esforço de revisão humana junto ao tempo de preenchimento?",
    ],
    visuals: [
      {
        src: "/images/itau-registros-workflow-1600.webp",
        width: 1600,
        height: 900,
        alt: "Fluxo de arquitetura de serviço e governança de IA para Registros de Atendimento",
        label: "Arquitetura e Governança · IA com Supervisão Humana",
        caption:
          "Modelo operacional para registros de atendimento: recuperação de contexto recente, geração de ata preliminar assistida por IA e salvaguarda obrigatória de supervisão humana antes da persistência bancária.",
      },
    ],
  },

  vencimentos: {
    title: "Gestão de Vencimentos",

    subtitle: "Da sinalização à atuação sobre eventos financeiros",

    discipline: "Product design · Operação financeira",

    stage: "Exploração, estados e handoff documentados",

    framing:
      "Especialistas precisam localizar eventos financeiros, avaliar prazo e valor e decidir sobre quais clientes atuar. A proposta reúne consulta, filtros e estados de atuação para apoiar essa leitura sem separar o evento do contexto do cliente.",

    question:
      "Como ajudar especialistas a localizar eventos financeiros relevantes, distinguir urgência e registrar atuação sem perder o contexto do cliente?",

    verified: [
      "A versão canônica organiza Vencimentos, Eventos futuros e Open Finance na mesma experiência unificada.",

      "Busca e filtros por prazo, status e valor reduzem o universo antes da atuação.",

      "A tabela relaciona cliente, agência/conta, carteira, produto, data, valor e estado da atuação.",

      "As ações variam conforme o estado do registro, incluindo consulta e edição.",

      "A documentação preserva alternativas de menor impacto técnico, componentes e preparação para handoff.",
    ],

    decisions: [
      {
        label: "Arquitetura",

        title: "Três contextos, uma lógica de consulta",

        description:
          "Vencimentos, eventos futuros e Open Finance permanecem distinguíveis por abas, reutilizando busca, filtros e estrutura de tabela.",
      },

      {
        label: "Priorização",

        title: "Filtros visíveis e combináveis",

        description:
          "Status, janela de tempo e faixa de valor tornam explícitos os critérios usados para reduzir a lista de trabalho.",
      },

      {
        label: "Resiliência",

        title: "Estados além do caminho feliz",

        description:
          "Carregamento e ausência de dados recebem tratamento próprio, evitando que demora ou filtro sem retorno pareçam falha silenciosa.",
      },
    ],

    sources: [
      "Versão canônica de Gestão de Liquidez (nó 582:12520), integrando saldos, eventos futuros e liquidez projetada.",

      "Explorações e documentação de Vencimentos com versões, componentes e handoff.",

      "Base de conhecimento do produto com funcionalidades e regras de negócio.",

      "Protótipo completo do IFA usado apenas como histórico de exploração e estados anteriores.",
    ],

    demonstrated: [
      "Arquitetura de consulta para vencimentos, eventos futuros e Open Finance",

      "Combinação de busca, filtros rápidos e filtros ativos",

      "Tabela preenchida e ações condicionadas ao status",

      "Densidade informacional adequada a uma operação financeira",

      "Rastro de exploração e preparação para handoff",
    ],

    missing: [
      "Confirmação da contribuição individual em cada etapa",

      "Registro inequívoco da versão implantada",

      "Métricas de uso, eficiência ou resultado operacional",

      "Critérios finais aprovados para priorização e atualização",

      "Créditos das demais pessoas e disciplinas envolvidas",
    ],

    nextValidation:
      "Cruzar a versão de handoff com a experiência implantada e recuperar evidências de teste, autoria, colaboração e resultado antes de promover este dossiê a case completo.",

    interviewQuestions: [
      "Qual parte do problema, fluxo e interface foi conduzida diretamente por você?",

      "Quais alternativas foram descartadas e por quais restrições técnicas ou operacionais?",

      "Que versão chegou a produção e qual evidência permite comparar antes e depois?",

      "Como especialistas avaliaram encontrabilidade, interpretação e continuidade da atuação?",
    ],

    visuals: [
      {
        src: "/images/itau-vencimentos-capa-1600.webp",
        width: 1600,
        height: 900,
        alt: "Interface canônica de Gestão de Vencimentos em alta resolução 16:9",
        label: "Interface canônica · Resolução 16:9",
        caption:
          "Interface canônica (Figma nó 582:12520): consolidação de Vencimentos, Eventos futuros e Open Finance com filtros operacionais e tabela densa para atuação do assessor.",
      },
      {
        src: "/images/itau-vencimentos-canonico.png",
        width: 1360,
        height: 1069,
        alt: "Última versão da interface Próximos Vencimentos com abas, busca, filtros e tabela de clientes.",
        label: "Interface canônica · Captura integral 1:1",
        caption:
          "A solução consolida Vencimentos, Eventos futuros e Open Finance; combina filtros operacionais com uma tabela densa e ações adequadas ao estado de cada registro.",
      },

      {
        src: "/images/itau-vencimentos-eventos.png",

        width: 1360,

        height: 1342,

        alt: "Aba de Eventos Futuros com projeção de liquidez e fluxos financeiros.",

        label: "Exploração de fluxo · Eventos futuros",

        caption:
          "Registro histórico da evolução do fluxo de eventos futuros, contextualizando a transição para a interface consolidada de Gestão de Liquidez.",
      },

      {
        src: "/images/itau-vencimentos-empty.png",

        width: 1360,

        height: 844,

        alt: "Tratamento de estado vazio na consulta de vencimentos e filtros sem resultado.",

        label: "Especificação de estados · Estado vazio",

        caption:
          "Especificação de estado vazio (empty state) com diretrizes claras de recuperação de busca, feedback e orientação para o especialista de investimentos.",
      },
    ],
  },

  movimentacoes: {
    title: "Movimentações",

    subtitle: "Transição do Extrato EA para o IFA",

    discipline: "Operação financeira · Arquitetura",

    stage: "Discovery e prototipagem",

    framing:
      "A transição do Extrato EA para o IFA exigia preservar o contexto financeiro necessário à atuação. Como o saldo provisionado é usado em diferentes jornadas, a solução o mantém no header; Movimentações concentra o histórico, o aprofundamento e as informações de CEP, CEP Plus e limite.",

    question:
      "Como manter o saldo provisionado disponível entre jornadas e permitir o aprofundamento das movimentações sem exigir troca de aba para consultar esse saldo?",

    verified: [
      "Um frame de Movimentações apresenta saldo provisionado no resumo do cliente e acesso à composição.",

      "O conteúdo da página combina limites de crédito, disponibilidade, histórico, busca, filtros e estados de movimentação.",

      "A documentação compara alternativas de arquitetura para visibilidade e aprofundamento.",

      "O autor confirmou como solução definida saldo provisionado no header, com CEP, CEP Plus e limite contextualizados em Movimentações.",
    ],

    decisions: [
      {
        label: "Alternativa A",

        title: "Resumo completo em Movimentações",

        description:
          "Alternativa histórica que concentrava interpretação, limites e histórico na área de eventos financeiros.",
      },

      {
        label: "Solução definida",

        title: "Provisionado no header + limites em Movimentações",

        description:
          "Mantém o saldo provisionado visível em diferentes jornadas sem troca de aba; CEP, CEP Plus e limite permanecem no contexto de Movimentações.",
      },

      {
        label: "Alternativas exploradas",

        title: "Acesso transversal e aprofundamento",

        description:
          "Faixa complementar, bloco no histórico, painel acionável, sidebar e contingência foram mantidos como comparação, não como solução definida.",
      },
    ],

    sources: [
      "Documento consolidado de problema, alternativas e critérios de validação.",

      "Frame de interface com resumo financeiro, contexto de liquidez e histórico.",

      "Protótipos e registros de QA local preservados no arquivo de trabalho.",
    ],

    demonstrated: [
      "Exploração de alternativas de arquitetura",

      "Representação de saldo provisionado e composição",

      "Integração conceitual com histórico, busca e filtros",

      "Solução definida pelo autor: saldo provisionado persistente no header, com CEP, CEP Plus e limite em Movimentações",
    ],

    missing: [
      "Referência equivalente da experiência EA",

      "Registro histórico da aprovação, responsáveis e data da decisão",

      "Contratos e regras confirmados pelo domínio",

      "Responsabilidades individuais, créditos e evidência de produção",
    ],

    nextValidation:
      "Recuperar a referência da EA e comparar tarefas equivalentes de continuidade operacional, medindo encontrabilidade, interpretação da composição e necessidade de troca de contexto.",

    interviewQuestions: [
      "Qual problema foi observado diretamente e em qual fonte ele está registrado?",

      "Quem participou da formulação e da avaliação das três alternativas?",

      "A decisão de provisionado no header avançou além de protótipo? Qual registro comprova esse estágio?",
    ],

    visuals: [
      {
        src: "/images/itau-movimentacoes-capa-1600.webp",
        width: 1600,
        height: 900,
        alt: "Discovery Extrato EA e proposta de arquitetura de informação no IFA",
        label: "Discovery e Arquitetura · Resolução 16:9",
        caption:
          "Discovery e arquitetura de informação (Figma nó 1966:34105): integração do saldo provisionado no header fixo e contexto persistente de movimentações financeiras.",
      },
      {
        src: "/images/itau-movimentacoes-discovery.webp",
        width: 2400,
        height: 1754,
        alt: "Discovery Extrato EA e proposta de arquitetura de informação",
        label: "Discovery e Arquitetura · Extrato EA no IFA",
        caption:
          "Exploração de alternativas de visibilidade para o saldo provisionado e limites, conectando o histórico de movimentações ao contexto financeiro persistente.",
      },

      {
        src: "/images/itau-planejamento-iniciativas.webp",

        width: 1600,

        height: 794,

        alt: "Planejamento e contexto de iniciativas no IFA",

        label: "Planejamento e Contexto de Iniciativas",

        caption:
          "Enquadramento da transição do Extrato EA dentro do ecossistema de liquidez e esteira operacional dos assessores.",
      },
    ],
  },

  "hub-liquidez": {
    title: "Hub de Liquidez e Oportunidades",

    subtitle: "Dados, priorização e próxima ação",

    discipline: "Discovery · Pensamento sistêmico",

    stage: "Interface da solução documentada",

    framing:
      "A interface aproxima disponibilidade atual, variação prevista e projeção de liquidez de uma lista de clientes para atuação. O desafio é ajudar o especialista a distinguir o que está disponível agora do que pode mudar no período e manter a origem dos valores compreensível antes de agir.",

    question:
      "Como transformar sinais financeiros dispersos em uma fila de trabalho cuja origem e próxima ação possam ser explicadas?",

    verified: [
      "A interface separa total disponível agora, variação prevista e liquidez projetada para a janela selecionada.",

      "A origem do total disponível combina Itaú e Open Finance.",

      "A projeção pode ser consultada para fim do dia, 7 dias ou 30 dias.",

      "Uma tabela reúne clientes, carteira, agência/conta, disponível agora, total projetado e status da atuação.",

      "Busca, filtros de origem e faixas de valor reduzem o universo antes da ação.",
    ],

    decisions: [
      {
        label: "Leitura",

        title: "Posição, variação e projeção",

        description:
          "Disponibilidade atual, variação prevista e projeção aparecem separadas para evitar tratar momentos diferentes como um único valor.",
      },

      {
        label: "Priorização",

        title: "Clientes para atuação",

        description:
          "A lista aproxima disponível agora, total projetado e status, sem publicar como validada a regra que define ou ordena clientes priorizados.",
      },

      {
        label: "Aprofundamento",

        title: "Origem e próxima ação",

        description:
          "Filtros por Itaú e outras instituições mantêm a origem dos recursos explícita antes do aprofundamento e da atuação sobre o cliente.",
      },
    ],

    sources: [
      "Interface da solução do Hub de Liquidez, arquivo Gestão de liquidez, nó 3:14068, fornecida pelo autor em 02/11/2026.",

      "Frames relacionados de lista, composição e próxima ação.",

      "Base de conhecimento e registros de exploração do produto.",
    ],

    demonstrated: [
      "Hierarquia entre disponibilidade atual, variação e projeção",

      "Origem Itaú e Open Finance",

      "Janelas de fim do dia, 7 dias e 30 dias",

      "Lista de clientes vinculada a status de atuação",

      "Busca e filtros por origem e faixa de valor",
    ],

    missing: [
      "Regra que define e ordena clientes priorizados",

      "Fórmula e reconciliação de disponível agora, variação e total projetado",

      "Contratos e regras confirmados pelo domínio",

      "Protocolo de validação com especialistas",

      "Responsabilidades individuais, créditos e evidência de produção",
    ],

    nextValidation:
      "Validar regras e reconciliação com o domínio e testar se especialistas conseguem explicar a origem, distinguir disponibilidade de projeção e justificar a próxima ação.",

    interviewQuestions: [
      "Quais dados alimentavam cada valor e qual era a frequência real de atualização?",

      "Como os clientes eram definidos e ordenados como prioritários e quem aprovou essa regra?",

      "Esta interface avançou para produção? Qual evidência define o estágio alcançado?",
    ],

    visuals: [
      {
        src: "/images/itau-hub-liquidez-capa-1600.webp",
        width: 1600,
        height: 900,
        alt: "Interface da solução Hub de Liquidez e Oportunidades com KPIs e fila prioritária em 16:9",
        label: "Interface da solução · Resolução 16:9",
        caption:
          "Interface da solução (Figma nó 3:14068): visualização integrada conectando liquidez disponível, variação projetada e fila prioritária de clientes.",
      },
      {
        src: "/images/itau-hub-liquidez-solucao.png",
        width: 1360,
        height: 1370,
        alt: "Interface do Hub de Liquidez e Oportunidades com posição atual, projeção e clientes priorizados.",
        label: "Interface da solução · Captura integral 1:1",
        caption:
          "A visão conecta liquidez disponível e projetada à fila de clientes, mantendo origem, janela temporal, filtros e status da atuação visíveis.",
      },

      {
        src: "/images/itau-planejamento-iniciativas.webp",

        width: 1600,

        height: 794,

        alt: "Visão integrada de iniciativas e oportunidades na jornada do assessor",

        label: "Visão Integrada de Iniciativas · IFA",

        caption:
          "Posicionamento do Hub de Liquidez dentro do roadmap e do ecossistema de ferramentas de assessoria de investimentos.",
      },
    ],
  },

  campanhas: {
    title: "Gestão de Campanhas",

    subtitle: "Configuração, dados, estados e manutenção",

    discipline: "Interaction design · Operação em lote",

    stage: "Fluxos documentados",

    framing:
      "Gerir uma campanha envolve configurar informações e público, acompanhar o processamento da base e decidir quando publicar, editar ou retirar a campanha. O fluxo organiza essas etapas e explicita estados de processamento, vazio e erro para orientar a operação.",

    question:
      "Como conectar configuração, processamento e manutenção sem ocultar estado, erro ou consequência das ações administrativas?",

    verified: [
      "A visão geral inclui busca, filtros, tabela, paginação e ações de manutenção.",

      "Os registros da tabela exibem estados como carregada, vazia e processando.",

      "O fluxo de criação separa informações gerais, público e campos personalizados.",

      "O screenflow registra carregamento, vazio, erro, edição, exclusão e etapas de criação.",
    ],

    decisions: [
      {
        label: "Consulta",

        title: "Estado orienta a ação",

        description:
          "Busca, filtros e status contextualizam publicar, tirar do ar, editar ou excluir.",
      },

      {
        label: "Criação",

        title: "Configuração antes do envio",

        description:
          "Informações da campanha, público e campos personalizados formam uma etapa configurável.",
      },

      {
        label: "Manutenção",

        title: "Fluxos além do caminho feliz",

        description:
          "O material reserva estados para carregamento, vazio, erro e exclusão, ainda com transições a confirmar.",
      },
    ],

    sources: [
      "Screenflow de Gestão de Campanhas com estados gerais e de exceção.",

      "Frame da visão geral com tabela, filtros, status e ações.",

      "Frame preenchido da primeira etapa de criação de campanha.",
    ],

    demonstrated: [
      "Cobertura visual da consulta e manutenção",

      "Estados de processamento e disponibilidade da base",

      "Configuração de informações, público e campos",

      "Registro de caminhos de erro e estado vazio",
    ],

    missing: [
      "Curadoria de versões sem placeholders",

      "Regras de preservação de dados entre etapas",

      "Comportamento final de erros, foco e retorno após exclusão",

      "Responsabilidades individuais, créditos e evidência de produção",
    ],

    nextValidation:
      "Selecionar os frames canônicos e verificar preservação de dados, mensagens de erro, publicação, navegação por teclado, foco e retorno seguro depois de ações destrutivas.",

    interviewQuestions: [
      "Quais estados foram implementados e quais permaneceram apenas no screenflow?",

      "Quem definiu as regras de publicação, exclusão e processamento da base?",

      "Que teste ou critério verificou a continuidade entre configuração e envio?",
    ],

    visuals: [
      {
        src: "/images/itau-campanhas-capa-1600.webp",
        width: 1600,
        height: 900,
        alt: "Visão canônica de Gestão de Campanhas IFA em alta resolução 16:9",
        label: "Visão Canônica · Resolução 16:9",
        caption:
          "Visão canônica de Gestão de Campanhas: interface operacional para parametrização em lote, segmentação de carteiras e acompanhamento de engajamento do assessor.",
      },
      {
        src: "/images/itau-campanhas-configuracao-historica.svg",
        width: 1133,
        height: 640,
        alt: "Exploração de configuração de campanha com informações gerais, público e campos personalizados",
        label: "Exploração histórica · Configuração de campanha",
        caption:
          "Artefato de exploração: informações gerais, público e campos personalizados na configuração da campanha com parametrização modular e dados sintetizados para conformidade com o sigilo bancário.",
      },

      {
        src: "/images/itau-campanhas-screenflow.webp",

        width: 1600,

        height: 1591,

        alt: "Screenflow da Gestão de Campanhas com visão geral, estados e criação",

        label: "Screenflow · Gestão de Campanhas",

        caption:
          "Mapeamento de screenflow e arquitetura de estados: ciclo completo de processamento de bases, regras de filtros dinâmicos e etapas guiadas de criação de campanhas no IFA.",
      },

      {
        src: "/images/itau-planejamento-iniciativas.webp",

        width: 1600,

        height: 794,

        alt: "Planejamento de esteira de iniciativas operacionais e de engajamento",

        label: "Iniciativas de Operação e Engajamento",

        caption:
          "Articulação da gestão de campanhas e ações em lote no fluxo de trabalho dos assessores de investimento.",
      },
    ],
  },
}
