import { useParams } from "react-router"
import { ArrowIcon, Link, Pill, Text } from "../design-system"
import { PageMeta } from "../components/PageMeta"
import { SiteFooter, SiteHeader } from "../components/SiteChrome"
import NotFound from "./NotFound"

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
}

const cases: Record<string, PreparationCase> = {
  movimentacoes: {
    title: "Movimentações",
    subtitle: "Transição do Extrato EA para o IFA",
    discipline: "Operação financeira · Arquitetura",
    stage: "Discovery e prototipagem",
    framing:
      "Os registros disponíveis enquadram a iniciativa como uma tentativa de recuperar, no IFA, contexto complementar de liquidez antes consultado em outra experiência. A hipótese precisava preservar o histórico de movimentações sem duplicar saldos já visíveis.",
    question:
      "Como tornar o saldo provisionado encontrável e investigável sem transformar uma hipótese de interface em decisão de produção?",
    verified: [
      "Um frame de Movimentações apresenta saldo provisionado no resumo do cliente e acesso à composição.",
      "O conteúdo da página combina limites de crédito, disponibilidade, histórico, busca, filtros e estados de movimentação.",
      "A documentação compara três alternativas de arquitetura para visibilidade e aprofundamento.",
      "A alternativa de header condicional com aprofundamento lateral foi priorizada para validação.",
    ],
    decisions: [
      {
        label: "Alternativa A",
        title: "Contexto em Movimentações",
        description:
          "Concentra interpretação e histórico na área em que os eventos financeiros já são consultados.",
      },
      {
        label: "Alternativa B",
        title: "Sinal no header + composição",
        description:
          "Propõe descoberta transversal e aprofundamento sob demanda quando existe provisionamento.",
      },
      {
        label: "Alternativa C",
        title: "Combinação dos dois pontos",
        description:
          "Amplia cobertura, mas introduz redundância e maior necessidade de governança.",
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
      "Hipótese priorizada para uma etapa posterior de validação",
    ],
    missing: [
      "Referência equivalente da experiência EA",
      "Escolha final e justificativa aprovada",
      "Contratos e regras confirmados pelo domínio",
      "Responsabilidades individuais, créditos e evidência de produção",
    ],
    nextValidation:
      "Recuperar a referência da EA e comparar tarefas equivalentes de continuidade operacional, medindo encontrabilidade, interpretação da composição e necessidade de troca de contexto.",
    interviewQuestions: [
      "Qual problema foi observado diretamente e em qual fonte ele está registrado?",
      "Quem participou da formulação e da avaliação das três alternativas?",
      "A alternativa B avançou além de protótipo? Qual registro comprova esse estágio?",
    ],
  },
  "hub-liquidez": {
    title: "Hub de Liquidez e Oportunidades",
    subtitle: "Dados, priorização e próxima ação",
    discipline: "Discovery · Pensamento sistêmico",
    stage: "Discovery e protótipo",
    framing:
      "Os frames organizam sinais de liquidez, clientes para atuação e acesso à composição em uma mesma visão. O material torna visível uma hipótese de priorização, mas não comprova a regra do score nem a adoção da proposta.",
    question:
      "Como transformar sinais financeiros dispersos em uma fila de trabalho cuja origem e próxima ação possam ser explicadas?",
    verified: [
      "O protótipo separa valor disponível agora, projeção e atualização do dado.",
      "Uma tabela reúne clientes para atuação, valores e status da atuação.",
      "A composição pode ser aprofundada a partir da lista.",
      "Há registro de prontidão V55, enquanto score, contratos e validação formal permanecem pendentes.",
    ],
    decisions: [
      {
        label: "Leitura",
        title: "Liquidez como contexto",
        description:
          "Disponibilidade atual e projeção aparecem separadas para evitar tratar momentos diferentes como um único valor.",
      },
      {
        label: "Priorização",
        title: "Clientes para atuação",
        description:
          "A lista aproxima sinal, valor e status, sem publicar como validada a lógica que ordena o trabalho.",
      },
      {
        label: "Aprofundamento",
        title: "Composição e próxima ação",
        description:
          "O acesso à composição sustenta investigação antes de uma ação, ainda sem evidência de uso em produção.",
      },
    ],
    sources: [
      "Frame principal do Hub de liquidez e oportunidades.",
      "Frames relacionados de lista, composição e próxima ação.",
      "Registro de prontidão V55 localizado no material do projeto.",
    ],
    demonstrated: [
      "Hierarquia entre disponibilidade atual e projeção",
      "Lista de clientes vinculada a status de atuação",
      "Ponto de entrada para composição da liquidez",
      "Estrutura visual de uma hipótese de priorização",
    ],
    missing: [
      "Fórmula, pesos e denominadores do score",
      "Contratos e regras confirmados pelo domínio",
      "Protocolo de validação com especialistas",
      "Responsabilidades individuais, créditos e evidência de produção",
    ],
    nextValidation:
      "Validar regras e denominadores com o domínio e testar se especialistas conseguem explicar a origem do sinal, distinguir disponibilidade de projeção e justificar a próxima ação.",
    interviewQuestions: [
      "Quais dados alimentavam cada valor e qual era a frequência real de atualização?",
      "Como a ordem da lista era calculada e quem aprovou essa regra?",
      "O que significa V55 no processo e qual evidência define o estágio alcançado?",
    ],
  },
  campanhas: {
    title: "Gestão de Campanhas",
    subtitle: "Configuração, dados, estados e manutenção",
    discipline: "Interaction design · Operação em lote",
    stage: "Fluxos documentados",
    framing:
      "O screenflow documenta uma jornada administrativa que conecta consulta, criação, processamento de base, publicação e manutenção. Os frames são evidência de cobertura de estados, não de implantação ou resultado operacional.",
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
  },
}

export default function ItauPreparationCase() {
  const { caseSlug = "" } = useParams()
  const project = cases[caseSlug]

  if (!project) {
    return <NotFound />
  }

  return (
    <>
      <PageMeta
        title={`${project.title} — Dossiê editorial em preparação`}
        description={`${project.title}: evidências verificadas, lacunas e próximos passos editoriais de um case em preparação.`}
      />
      <Link className="skip-link" href="#conteudo">
        Pular para o conteúdo
      </Link>
      <SiteHeader casePage />

      <main id="conteudo">
        <section
          className="case-page-hero preparation-hero"
          id="topo"
          aria-labelledby="case-page-title"
        >
          <Link className="case-back-link" href="/#trabalho">
            ← Voltar ao trabalho selecionado
          </Link>
          <Pill tone="accent">Case em preparação · Itaú Unibanco</Pill>
          <Text as="h1" id="case-page-title">
            {project.title}
          </Text>
          <Text className="case-page-deck">{project.subtitle}</Text>
          <div className="case-page-meta" aria-label="Estado editorial do case">
            <div>
              <Text as="span">Recorte</Text>
              <Text as="strong">{project.discipline}</Text>
            </div>
            <div>
              <Text as="span">Estágio demonstrável</Text>
              <Text as="strong">{project.stage}</Text>
            </div>
            <div>
              <Text as="span">Contribuição individual</Text>
              <Text as="strong">Pendente de confirmação</Text>
            </div>
          </div>
        </section>

        <section
          className="section case-page-content preparation-case"
          aria-labelledby="dossier-title"
        >
          <article className="preparation-overview">
            <div>
              <Text as="span">Leitura editorial</Text>
              <Text as="h2" id="dossier-title">
                Evidência suficiente para discussão. Ainda não para atribuição
                ou resultado.
              </Text>
            </div>
            <Text>{project.framing}</Text>
          </article>

          <div className="preparation-question">
            <Text as="span">Pergunta de design reconstruída</Text>
            <Text as="h3">{project.question}</Text>
          </div>

          <section
            className="preparation-section"
            aria-labelledby="verified-title"
          >
            <div className="preparation-section-heading">
              <Text as="span">01 · O que os artefatos mostram</Text>
              <Text as="h3" id="verified-title">
                Estruturas verificáveis, sem extrapolar o estágio.
              </Text>
            </div>
            <ol className="verified-list">
              {project.verified.map((item, index) => (
                <li key={item}>
                  <Text as="span">{String(index + 1).padStart(2, "0")}</Text>
                  <Text>{item}</Text>
                </li>
              ))}
            </ol>
          </section>

          <section
            className="preparation-section"
            aria-labelledby="decision-title"
          >
            <div className="preparation-section-heading">
              <Text as="span">02 · Rastro de decisão</Text>
              <Text as="h3" id="decision-title">
                A interface como hipótese documentada.
              </Text>
            </div>
            <div className="decision-map">
              {project.decisions.map((decision, index) => (
                <article key={decision.title}>
                  <Text as="span">
                    {String(index + 1).padStart(2, "0")} · {decision.label}
                  </Text>
                  <Text as="h4">{decision.title}</Text>
                  <Text>{decision.description}</Text>
                </article>
              ))}
            </div>
          </section>

          <section
            className="preparation-section source-section"
            aria-labelledby="sources-title"
          >
            <div className="preparation-section-heading">
              <Text as="span">03 · Fontes e rastreabilidade</Text>
              <Text as="h3" id="sources-title">
                Fontes usadas neste recorte.
              </Text>
            </div>
            <ul className="source-list">
              {project.sources.map((source) => (
                <li key={source}>
                  <Text>{source}</Text>
                </li>
              ))}
            </ul>
          </section>

          <div className="preparation-boundaries">
            <div>
              <Text as="span">Demonstrado</Text>
              <ul>
                {project.demonstrated.map((item) => (
                  <li key={item}>{item}</li>
                ))}
              </ul>
            </div>
            <div>
              <Text as="span">Ainda não demonstrado</Text>
              <ul>
                {project.missing.map((item) => (
                  <li key={item}>{item}</li>
                ))}
              </ul>
            </div>
            <div className="preparation-next">
              <Text as="span">Próxima validação recomendada</Text>
              <Text>{project.nextValidation}</Text>
            </div>
          </div>

          <section
            className="preparation-interview"
            aria-labelledby="interview-title"
          >
            <div>
              <Text as="span">Roteiro de verificação</Text>
              <Text as="h3" id="interview-title">
                Perguntas antes de promover este material a case completo.
              </Text>
            </div>
            <ol>
              {project.interviewQuestions.map((question) => (
                <li key={question}>
                  <Text>{question}</Text>
                </li>
              ))}
            </ol>
          </section>

          <aside className="case-disclosure">
            <Text as="strong">Nota de transparência</Text>
            <Text>
              Este dossiê organiza artefatos históricos para apresentação
              controlada em entrevistas. Não declara autoria individual,
              implantação, decisão final, resultado de negócio ou autorização
              formal das demais partes. Essas confirmações permanecem como
              condição para um case completo.
            </Text>
          </aside>

          <div className="preparation-return">
            <Link className="button button--primary" href="/#trabalho">
              Voltar aos projetos <ArrowIcon />
            </Link>
          </div>
        </section>
      </main>

      <SiteFooter />
    </>
  )
}

