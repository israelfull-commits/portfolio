# Script to update ItauPreparationCase.tsx with complete high-res 16:9 covers and evidence galleries

with open('site/src/pages/ItauPreparationCase.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update registros-atendimento visuals
old_registros_tail = '''      "Qual parte do fluxo gerado pela IA foi aceita sem edição nos testes com especialistas?",

      "Como os cinco resumos recentes foram priorizados em relação ao histórico completo?",

      "Qual área do banco validou o protocolo de responsabilidade e auditoria?",
    ],
  },'''

new_registros_tail = '''      "Qual parte do fluxo gerado pela IA foi aceita sem edição nos testes com especialistas?",

      "Como os cinco resumos recentes foram priorizados em relação ao histórico completo?",

      "Qual área do banco validou o protocolo de responsabilidade e auditoria?",
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
  },'''

if old_registros_tail in content:
    content = content.replace(old_registros_tail, new_registros_tail, 1)
    print("Updated registros-atendimento")
else:
    print("Could not find old_registros_tail")

# 2. Update vencimentos visuals
old_vencimentos_visuals = '''    visuals: [
      {
        src: "/images/itau-vencimentos-canonico.png",

        width: 1360,

        height: 1069,

        alt: "Última versão da interface Próximos Vencimentos com abas, busca, filtros e tabela de clientes.",

        label: "Interface canônica · Última versão confirmada",

        caption:
          "A solução consolida Vencimentos, Eventos futuros e Open Finance; combina filtros operacionais com uma tabela densa e ações adequadas ao estado de cada registro.",
      },'''

new_vencimentos_visuals = '''    visuals: [
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
      },'''

if old_vencimentos_visuals in content:
    content = content.replace(old_vencimentos_visuals, new_vencimentos_visuals, 1)
    print("Updated vencimentos")
else:
    print("Could not find old_vencimentos_visuals")

# 3. Update movimentacoes visuals
old_movimentacoes_visuals = '''    visuals: [
      {
        src: "/images/itau-movimentacoes-discovery.webp",

        width: 2400,

        height: 1754,

        alt: "Discovery Extrato EA e proposta de arquitetura de informação",

        label: "Discovery e Arquitetura · Extrato EA no IFA",

        caption:
          "Exploração de alternativas de visibilidade para o saldo provisionado e limites, conectando o histórico de movimentações ao contexto financeiro persistente.",
      },'''

new_movimentacoes_visuals = '''    visuals: [
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
      },'''

if old_movimentacoes_visuals in content:
    content = content.replace(old_movimentacoes_visuals, new_movimentacoes_visuals, 1)
    print("Updated movimentacoes")
else:
    print("Could not find old_movimentacoes_visuals")

# 4. Update hub-liquidez visuals
old_hub_visuals = '''    visuals: [
      {
        src: "/images/itau-hub-liquidez-solucao.png",

        width: 1360,

        height: 1370,

        alt: "Interface do Hub de Liquidez e Oportunidades com posição atual, projeção e clientes priorizados.",

        label: "Interface da solução · Hub de Liquidez",

        caption:
          "A visão conecta liquidez disponível e projetada à fila de clientes, mantendo origem, janela temporal, filtros e status da atuação visíveis.",
      },'''

new_hub_visuals = '''    visuals: [
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
      },'''

if old_hub_visuals in content:
    content = content.replace(old_hub_visuals, new_hub_visuals, 1)
    print("Updated hub-liquidez")
else:
    print("Could not find old_hub_visuals")

# 5. Update campanhas visuals
old_campanhas_visuals = '''    visuals: [
      {
        src: "/images/itau-campanhas-configuracao-historica.svg",

        width: 1133,

        height: 640,

        alt: "Exploração de configuração de campanha com informações gerais, público e campos personalizados",

        label: "Exploração histórica · Configuração de campanha",

        caption:
          "Artefato de; exploração: informações gerais, público e campos personalizados na configuração da campanha. Textos e valores exemplificativos do protótipo; não é comprovação de uma versão implantada.",
      },'''

new_campanhas_visuals = '''    visuals: [
      {
        src: "/images/itau-campanhas-capa-1600.webp",
        width: 1600,
        height: 900,
        alt: "Screenflow e arquitetura de estados da Gestão de Campanhas IFA em 16:9",
        label: "Screenflow e Arquitetura · Resolução 16:9",
        caption:
          "Mapeamento de estados de processamento da base, filtros, tabela operacional e etapas de criação e manutenção de campanhas no IFA.",
      },
      {
        src: "/images/itau-campanhas-configuracao-historica.svg",
        width: 1133,
        height: 640,
        alt: "Exploração de configuração de campanha com informações gerais, público e campos personalizados",
        label: "Exploração histórica · Configuração de campanha",
        caption:
          "Artefato de exploração: informações gerais, público e campos personalizados na configuração da campanha. Textos e valores exemplificativos do protótipo; não é comprovação de uma versão implantada.",
      },'''

if old_campanhas_visuals in content:
    content = content.replace(old_campanhas_visuals, new_campanhas_visuals, 1)
    print("Updated campanhas")
else:
    print("Could not find old_campanhas_visuals")

with open('site/src/pages/ItauPreparationCase.tsx', 'w', encoding='utf-8') as f:
    f.write(content)

print("Saved updated ItauPreparationCase.tsx")

