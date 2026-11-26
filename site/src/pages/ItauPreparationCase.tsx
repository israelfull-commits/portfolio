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
      "Conduzi o desenho de interação e governança de IA no fluxo de especialistas e assessores, aproximando os 5 resumos recentes no painel lateral e exigindo revisão e confirmação humana obrigatória antes da gravação no prontuário bancário.",

    question:
      "Como reduzir o esforço de registro e facilitar a recuperação de contexto, mantendo fidelidade ao atendimento e controle humano sobre o conteúdo?",

    verified: [
      "Discovery e desenho de fluxo assistido por IA para geração de atas e sínteses de atendimento.",

      "Aproximação dos cinco resumos recentes diretamente no momento de consulta e registro do especialista e do assessor.",

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
        src: "/images/v07-itau-jornada-studio-frame.webp",
        width: 2400,
        height: 1350,
        alt: "Fluxo comparativo da jornada de especialistas e assessores no IFA em moldura de estúdio: estado anterior fragmentado versus esteira integrada com síntese por IA e gate de revisão humana obrigatória",
        label: "Fluxo da Jornada · Antes vs. Esteira Integrada com IA",
        caption:
          "Jornada ponta a ponta de especialistas e assessores: eliminação da busca manual em abas com aproximação dos 5 últimos eventos, minuta preliminar assistida por IA e aprovação humana obrigatória (Human-in-the-Loop).",
      },
      {
        src: "/images/itau-registros-workflow-1600.webp",
        width: 1600,
        height: 900,
        alt: "Fluxo de arquitetura de serviço e governança de IA para Registros de Atendimento",
        label: "Arquitetura e Governança · Pilares de Conformidade",
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
      "Conduzi a Arquitetura da Informação e a especificação de filtros combináveis, estados vazios e tabela densa no Design System (iDS), unificando Vencimentos, Eventos futuros e Open Finance em uma única lógica de consulta e atuação.",

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
      "Versão canônica de Gestão de Liquidez, integrando saldos, eventos futuros e liquidez projetada.",

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
      "Cruzar a especificação de handoff com a telemetria de produção para comparar tempo de consulta e taxa de registro de ações.",

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
        label: "Interface canônica · Próximos Vencimentos",
        caption:
          "Interface canônica: consolidação de Vencimentos, Eventos futuros e Open Finance com filtros operacionais e tabela densa para atuação de especialistas e assessores.",
      },

      {
        src: "/images/itau-vencimentos-eventos.webp",

        width: 1360,

        height: 1342,

        alt: "Aba de Eventos Futuros com projeção de liquidez e fluxos financeiros.",

        label: "Exploração de fluxo · Eventos futuros",

        caption:
          "Registro histórico da evolução do fluxo de eventos futuros, contextualizando a transição para a interface consolidada de Gestão de Liquidez.",
      },

      {
        src: "/images/itau-vencimentos-empty.webp",

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
      "Conduzi o Product Discovery e a comparação de alternativas de arquitetura entre cabeçalho persistente e consulta detalhada, preservando o saldo provisionado transversalmente entre jornadas e contextualizando CEP, CEP Plus e limites em Movimentações.",

    question:
      "Como manter o saldo provisionado disponível entre jornadas e permitir o aprofundamento das movimentações sem exigir troca de aba para consultar esse saldo?",

    verified: [
      "Um frame de Movimentações apresenta saldo provisionado no resumo do cliente e acesso à composição.",

      "O conteúdo da página combina limites de crédito, disponibilidade, histórico, busca, filtros e estados de movimentação.",

      "A documentação compara alternativas de arquitetura para visibilidade e aprofundamento.",

      "Solução definida em arquitetura: saldo provisionado persistente no cabeçalho, com CEP, CEP Plus e limite contextualizados em Movimentações.",
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

      "Solução adotada: saldo provisionado persistente no header, com CEP, CEP Plus e limite em Movimentações",
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
        src: "/images/itau-movimentacoes-telas-1800.webp",
        width: 1800,
        height: 333,
        alt: "Três telas da proposta de Movimentações no IFA: header com liquidez e limites, histórico priorizado e detalhe contextual",
        label: "Arquitetura de Interface · Fluxo em 3 telas",
        caption:
          "Proposta em três camadas: header fixo com saldo provisionado e limites, tabela de histórico priorizado e painel de detalhamento com rastreabilidade.",
      },
    ],
  },

  "hub-liquidez": {
    title: "Hub de Liquidez e Oportunidades",

    subtitle:
      "Arquitetura da Informação e contratos de dados para consolidar saldo disponível, projeção temporal e fila prioritária de especialistas e assessores no íon for Advisors.",

    discipline: "Discovery · Pensamento sistêmico",

    stage: "Interface da solução documentada",

    framing:
      "Conduzi o Product Discovery, a Arquitetura da Informação e a modelagem de contratos de dados com componentes escaláveis do Design System (iDS), conectando resumo consolidado, filtros combináveis e fila operacional com status de atuação.",

    question:
      "Como organizar sinais financeiros dispersos em uma fila de trabalho cuja origem e próxima ação possam ser explicadas?",

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
      "Interface consolidada do Hub de Liquidez integrando posição atual, projeção e clientes priorizados.",

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
        src: "/images/v16-itau-bento-fintech-elegostra-aeroload.webp",
        width: 2400,
        height: 1350,
        alt: "Visão modular do ecossistema íon for Advisors (IFA): Hub de Liquidez, Próximos Vencimentos e filtros operacionais para especialistas de investimentos e assessores",
        label: "Ecossistema IFA · Hub de Liquidez e Oportunidades",
        caption:
          "Arquitetura modular de liquidez no íon for Advisors: consolidação de saldo disponível, projeção temporal e fila prioritária de clientes com filtros combináveis.",
      },
      {
        src: "/images/itau-hub-liquidez-solucao.webp",
        width: 1360,
        height: 1370,
        alt: "Interface detalhada do Hub de Liquidez e Oportunidades com posição atual, projeção e clientes priorizados.",
        label: "Interface detalhada · Hub de Liquidez e Oportunidades",
        caption:
          "A visão conecta liquidez disponível e projetada à fila prioritária de clientes, mantendo origem, janela temporal, filtros e status da atuação visíveis.",
      },
    ],
  },

  campanhas: {
    title: "Gestão de Campanhas",

    subtitle: "Configuração, dados, estados e manutenção",

    discipline: "Interaction design · Operação em lote",

    stage: "Fluxos documentados",

    framing:
      "Conduzi a modelagem dos screenflows de criação, importação de base e manutenção em lote, especificando estados de carregamento, vazio, processamento e erro para conectar administradores de backoffice, especialistas e gestores.",

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
        src: "/images/itau-campanhas-configuracao-historica.svg",
        width: 1133,
        height: 640,
        alt: "Exploração de configuração de campanha com informações gerais, público e campos personalizados",
        label: "Arquitetura de Interface · Configuração de campanha",
        caption:
          "Parametrização modular: informações gerais, segmentação de público e campos personalizados com dados sintetizados para conformidade com o sigilo bancário.",
      },
    ],
  },
}
