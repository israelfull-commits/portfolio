export type ItauModuleSpec = {
  title: string
  headline: string
  subtitle: string
  metaDescription: string
  stage: string
  framing: string
  question: string
  visuals?: Array<{
    src: string
    width: number
    height: number
    alt: string
    label: string
    caption: string
  }>
}

export const cases: Record<string, ItauModuleSpec> = {
  "registros-atendimento": {
    title: "Registros de Atendimento",
    headline:
      "Aproximar os 5 últimos resumos e exigir confirmação humana antes de gravar notas assistidas por IA.",
    subtitle:
      "Como Senior Product Designer no Itaú Unibanco (íon for Advisors), conduzi a arquitetura de interação e a governança de IA nos Registros de Atendimento. Entre um contato e outro, especialistas e os assessores que os auxiliam perdiam tempo recuperando o histórico do cliente e digitando atas manualmente. Aproximei os 5 últimos resumos do campo de registro com minuta preliminar editável e confirmação humana obrigatória antes da gravação, sem métricas causais publicadas neste recorte.",
    metaDescription:
      "Senior Product Designer no Itaú íon for Advisors (2024–2026): histórico dos 5 últimos resumos e minuta assistida por IA com revisão humana obrigatória.",
    stage: "Arquitetura de interação e diretrizes de governança de IA documentadas",
    framing:
      "Conduzi o desenho de interação e a governança de IA no fluxo de especialistas e assessores. Aproximei os 5 resumos recentes no painel lateral e exigi revisão e confirmação humana obrigatória antes da gravação no prontuário bancário.",
    question:
      "Como reduzir o esforço de registro e facilitar a recuperação de contexto, mantendo fidelidade ao atendimento e controle humano sobre o conteúdo?",
    visuals: [
      {
        src: "/images/v07-itau-jornada-studio-v2.webp",
        width: 2400,
        height: 1350,
        alt: "Diagrama ilustrativo comparando a jornada de especialistas e assessores no IFA: fluxo anterior em abas separadas versus fluxo integrado com os 5 últimos resumos, minuta assistida por IA e aprovação humana obrigatória.",
        label: "Fluxo da Jornada · Antes vs. Esteira Integrada com IA",
        caption:
          "Diagrama de fluxo (ilustrativo, sem captura real por sigilo bancário): aproximei os 5 últimos resumos e a minuta preliminar para evitar perda de contexto entre atendimentos. A aprovação humana obrigatória (Human-in-the-Loop) precede a gravação no prontuário.",
      },
      {
        src: "/images/itau-registros-workflow-v2.webp",
        width: 2400,
        height: 1350,
        alt: "Diagrama ilustrativo dos pilares de governança de IA em Registros de Atendimento: recuperação dos 5 últimos resumos, geração de ata preliminar editável e validação humana obrigatória antes da persistência bancária.",
        label: "Arquitetura e Governança · Pilares de Conformidade",
        caption:
          "Diagrama de arquitetura e governança (ilustrativo): a revisão humana precede a persistência bancária para mitigar omissões e preservar a fidelidade técnica dos registros de carteira.",
      },
    ],
  },

  vencimentos: {
    title: "Gestão de Vencimentos",
    headline:
      "Unificar vencimentos, eventos futuros e Open Finance sob uma mesma lógica de atuação.",
    subtitle:
      "Como Senior Product Designer no Itaú Unibanco (íon for Advisors), conduzi a arquitetura de consulta, filtros e estados da Gestão de Vencimentos. Especialistas, assessores e gestores precisavam localizar vencimentos, eventos futuros e sinais de Open Finance sem perder o contexto do cliente nem o histórico de atuação. Unifiquei os três contextos em abas com busca, filtros combináveis e tabela operacional, entregando a interface canônica e a especificação de estados para handoff.",
    metaDescription:
      "Senior Product Designer no Itaú íon for Advisors (2024–2026): consulta unificada de vencimentos, eventos futuros e Open Finance com filtros combináveis e estados.",
    stage: "Interface canônica, especificação de estados e handoff documentados",
    framing:
      "Conduzi a arquitetura da informação e a especificação de filtros combináveis, estados vazios e tabela densa no Design System (iDS). A estrutura unifica Vencimentos, Eventos futuros e Open Finance sob uma mesma lógica de consulta e atuação.",
    question:
      "Como permitir que especialistas localizem eventos financeiros relevantes, distingam urgência e registrem atuação sem perder o contexto do cliente?",
    visuals: [
      {
        src: "/images/itau-vencimentos-capa-v2.webp",
        width: 1600,
        height: 900,
        alt: "Interface canônica de Gestão de Vencimentos no IFA com abas de Vencimentos, Eventos futuros e Open Finance, filtros combináveis de prazo, status e valor, e tabela operacional de clientes.",
        label: "Interface canônica · Próximos Vencimentos",
        caption:
          "Abas separam Vencimentos, Eventos futuros e Open Finance mantendo a mesma estrutura de busca, filtros e tabela para que especialistas e assessores atuem sem reaprender a navegação.",
      },
      {
        src: "/images/itau-vencimentos-eventos-v2.webp",
        width: 1360,
        height: 1342,
        alt: "Aba de Eventos Futuros com projeção de liquidez, descrição sintética de eventos financeiros e tabela operacional.",
        label: "Exploração de fluxo · Eventos futuros",
        caption:
          "A exploração de Eventos futuros motivou o reaproveitamento da mesma tabela e dos mesmos filtros de Vencimentos, evitando telas isoladas para eventos relacionados à liquidez.",
      },
      {
        src: "/images/itau-vencimentos-empty.webp",
        width: 1360,
        height: 844,
        alt: "Tratamento de estado vazio na consulta de vencimentos e filtros sem resultado.",
        label: "Especificação de estados · Estado vazio",
        caption:
          "O estado vazio foi especificado com orientação de recuperação de busca para evitar que um filtro sem retorno ou demora de carga pareçam falha silenciosa ao especialista.",
      },
    ],
  },

  movimentacoes: {
    title: "Movimentações",
    headline:
      "Manter o saldo provisionado no cabeçalho sem duplicar o extrato na navegação global.",
    subtitle:
      "Como Senior Product Designer no Itaú Unibanco (íon for Advisors), conduzi o discovery de arquitetura na transição do Extrato EA para o IFA. Concentrar todos os saldos em uma única aba obrigaria especialistas e assessores a sair da tarefa atual para consultar o saldo provisionado. Comparei seis alternativas e defini o saldo provisionado persistente no cabeçalho, mantendo CEP, CEP Plus, limite e lançamentos em Movimentações, em etapa de discovery e prototipagem.",
    metaDescription:
      "Senior Product Designer no Itaú íon for Advisors (2024–2026): transição do Extrato EA para o IFA com saldo provisionado no cabeçalho e limites em Movimentações.",
    stage: "Discovery de arquitetura e prototipagem documentados",
    framing:
      "Conduzi o Product Discovery e comparei alternativas de arquitetura entre cabeçalho persistente e consulta detalhada. A solução mantém o saldo provisionado visível entre jornadas e contextualiza CEP, CEP Plus e limite em Movimentações.",
    question:
      "Como manter o saldo provisionado disponível entre jornadas e permitir o aprofundamento das movimentações sem exigir troca de aba para consultar esse saldo?",
    visuals: [
      {
        src: "/images/itau-movimentacoes-bento-2400.webp",
        width: 2400,
        height: 1350,
        alt: "Arquitetura em 3 camadas de Movimentações no IFA com dados sintetizados: cabeçalho persistente com saldo provisionado, limites CEP e CEP Plus, histórico priorizado de lançamentos e painel lateral de detalhamento.",
        label: "Arquitetura de Interface · Fluxo em 3 camadas",
        caption:
          "Separei o saldo provisionado no cabeçalho fixo para consulta entre jornadas sem troca de aba. Limites de crédito (CEP, CEP Plus e limite), histórico e detalhamento permanecem contextualizados em Movimentações.",
      },
    ],
  },

  "hub-liquidez": {
    title: "Hub de Liquidez e Oportunidades",
    headline:
      "Separar saldo disponível, variação prevista e liquidez projetada em uma única leitura.",
    subtitle:
      "Como Senior Product Designer no Itaú Unibanco (íon for Advisors), conduzi a arquitetura da informação e os contratos de visualização do Hub de Liquidez. Especialistas de investimentos e os assessores que os auxiliam cruzavam múltiplas abas para conciliar saldo em conta, Open Finance e liquidez projetada. Estruturei posição atual, projeção por janela (fim do dia, 7 e 30 dias) e fila de clientes na mesma tela, entregando a interface documentada da solução sem medição pós-produção neste recorte.",
    metaDescription:
      "Senior Product Designer no Itaú íon for Advisors (2024–2026): hierarquia de saldo disponível, projeção temporal (dia, 7d, 30d) e fila de clientes no Hub de Liquidez.",
    stage: "Interface da solução documentada",
    framing:
      "Conduzi o Product Discovery, a arquitetura da informação e a modelagem de contratos de dados com componentes do Design System (iDS). A estrutura conecta resumo consolidado, filtros combináveis e fila operacional com status de atuação.",
    question:
      "Como organizar sinais financeiros dispersos em uma fila de trabalho cuja origem e próxima ação possam ser explicadas?",
    visuals: [
      {
        src: "/images/v16-itau-bento-fintech-elegostra-aeroload.webp",
        width: 2400,
        height: 1350,
        alt: "Visão modular do ecossistema íon for Advisors (IFA): Hub de Liquidez, Próximos Vencimentos e filtros operacionais para especialistas de investimentos e assessores",
        label: "Ecossistema IFA · Hub de Liquidez e Oportunidades",
        caption:
          "Separei saldo disponível agora, variação prevista e liquidez projetada acima da fila de clientes para impedir que valores futuros sejam lidos como disponibilidade imediata antes da abordagem.",
      },
      {
        src: "/images/itau-hub-liquidez-solucao.webp",
        width: 1360,
        height: 1370,
        alt: "Interface detalhada do Hub de Liquidez e Oportunidades com posição atual, projeção e clientes priorizados.",
        label: "Interface detalhada · Hub de Liquidez e Oportunidades",
        caption:
          "Origem (Itaú e Open Finance), janela temporal (fim do dia, 7 e 30 dias) e status ficam visíveis na mesma tela. Assim, o especialista e o assessor filtram e justificam a próxima ação sem cruzar abas.",
      },
    ],
  },

  campanhas: {
    title: "Gestão de Campanhas",
    headline:
      "Sincronizar configuração da base, execução comercial e visão gerencial por estados explícitos.",
    subtitle:
      "Como Senior Product Designer no Itaú Unibanco (íon for Advisors), conduzi os fluxos de tela de configuração, importação de base e manutenção em lote da Gestão de Campanhas. Sem estados explícitos de processamento, backoffice, especialistas e gestores perdiam sincronia sobre quais campanhas estavam aptas para atuação. Separei configuração e ativação e mapeei estados de carregamento, vazio, processamento e erro em fluxos documentados para handoff.",
    metaDescription:
      "Senior Product Designer no Itaú íon for Advisors (2024–2026): fluxos de configuração, importação de base, estados de processamento e manutenção em lote.",
    stage: "Fluxos de tela e especificação de estados documentados",
    framing:
      "Conduzi a modelagem dos fluxos de tela de criação, importação de base e manutenção em lote. Especifiquei estados de carregamento, vazio, processamento e erro para alinhar administradores de backoffice, especialistas e gestores.",
    question:
      "Como conectar configuração, processamento e manutenção sem ocultar estado, erro ou consequência das ações administrativas?",
    visuals: [
      {
        src: "/images/itau-campanhas-configuracao-v2.webp",
        width: 1600,
        height: 900,
        alt: "Tela de configuração de campanha no IFA com etapas de informações gerais, segmentação de público e campos personalizados.",
        label: "Arquitetura de Interface · Configuração de campanha",
        caption:
          "Separei informações gerais, segmentação de público e campos personalizados antes da ativação para evitar publicação de campanhas com base incompleta. Dados sintetizados para sigilo bancário.",
      },
    ],
  },
}
