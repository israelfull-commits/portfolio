import { ArrowIcon, Link, Pill, SectionLabel, Text } from "../design-system"

import { PageMeta } from "../components/PageMeta"

import { SiteFooter, SiteHeader } from "../components/SiteChrome"

const capabilities = [
  {
    index: "01",

    title: "Discovery e estratégia",

    description:
      "Enquadramento de problemas, pesquisa, síntese, experimentação e priorização para reduzir incerteza antes da entrega.",
  },

  {
    index: "02",

    title: "UX/UI para produtos complexos",

    description:
      "Jornadas, arquitetura de informação e interfaces para operações de alta densidade e contextos regulados.",
  },

  {
    index: "03",

    title: "Design systems e acessibilidade",

    description:
      "Governança, documentação e handoff com práticas de acessibilidade baseadas em WCAG e consistência em escala.",
  },

  {
    index: "04",

    title: "IA responsável",

    description:
      "Exploração de fluxos assistidos por IA com critérios de qualidade, rastreabilidade e supervisão humana.",
  },
]

const experience = [
  {
    period: "2024 — 2026",

    company: "Itaú Unibanco",

    role: "Senior Product Designer",

    description:
      "Discovery e design de produto para a plataforma íon for Advisors e ferramentas operacionais de assessoria de investimentos.",

    tags: ["Fintech", "B2B", "IA", "Design system"],
  },

  {
    period: "2022 — atual",

    company: "Consultoria independente",

    role: "Senior UX Consultant",

    description:
      "Projetos independentes selecionados, realizados entre vínculos ou em paralelo, em experiência e evolução de produtos digitais.",

    tags: ["Estratégia", "Discovery", "UX/UI"],
  },

  {
    period: "2022",

    company: "Foursys · Hospital Israelita Albert Einstein",

    role: "UX Lead",

    description:
      "Liderança de uma squad multidisciplinar na redefinição da jornada de criação e leitura de laudos médicos.",

    tags: ["Saúde", "Liderança", "Acessibilidade"],
  },

  {
    period: "2020 — 2022",

    company: "EY · R/GA",

    role: "Senior UX Consultant / Designer",

    description:
      "Atuação sênior em consultoria e design de experiências digitais para organizações de grande porte.",

    tags: ["Consultoria", "Produtos digitais"],
  },

  {
    period: "2006 — 2019",

    company: "Moot · Walmart · GFT · Principia e outras",

    role: "UX/UI, direção de arte e design",

    description:
      "Base multidisciplinar construída entre produto, interface, comunicação e tecnologia.",

    tags: ["UX/UI", "E-commerce", "Interface"],
  },
]

const additionalCases = [
  {
    slug: "vencimentos",

    title: "Gestão de Vencimentos",

    theme: "Operação financeira",

    description:
      "Consulta, filtros e estados de atuação para conectar eventos financeiros ao contexto do cliente.",

    focus: "Hierarquia de informação, urgência e continuidade da atuação.",
  },

  {
    slug: "hub-liquidez",

    title: "Hub de Liquidez e Oportunidades",

    theme: "Discovery e visão sistêmica",

    description:
      "Posição financeira, composição da liquidez e priorização de clientes em uma mesma lógica de consulta.",

    focus: "Origem do dado, contexto e próxima ação explicável.",
  },

  {
    slug: "movimentacoes",

    title: "Movimentações e Extrato",

    theme: "Arquitetura da informação",

    description:
      "Transição do Extrato EA para o IFA com saldo provisionado visível entre jornadas e aprofundamento em Movimentações.",

    focus: "Provisionado transversal; CEP, CEP Plus e limite contextualizados.",
  },

  {
    slug: "campanhas",

    title: "Gestão de Campanhas",

    theme: "Fluxos e operação em lote",

    description:
      "Configuração de campanhas, tratamento de bases, estados e manutenção em um fluxo administrativo coerente.",

    focus: "Informações, público e feedback orientando a próxima ação.",
  },

  {
    slug: "registros-atendimento",

    title: "Registros de Atendimento",

    theme: "IA aplicada à operação",

    description:
      "Resumos assistidos por IA e consulta ao histórico recente para apoiar a documentação do atendimento.",

    focus: "Contexto, fidelidade do resumo e revisão humana.",
  },
]

function SectionHeading({
  index,

  eyebrow,

  title,

  id,
}: {
  index: string
 ; eyebrow: string
 ; title: string
 ; id: string
}) {
  return (
    <div className="section-heading">
      <SectionLabel index={index}>{eyebrow}</SectionLabel>
      <Text as="h2" className="display-md" id={id}>
        {title}
      </Text>
    </div>
  )
}

export default function Home() {
  return (
    <>
      <PageMeta
        title="Israel Rozar — Senior Product Designer"
        description="Portfólio de Israel Rozar: product design, discovery, sistemas complexos, acessibilidade e IA."
      />
      <Link className="skip-link" href="#conteudo">
        Pular para o conteúdo
      </Link>

      <SiteHeader />

      <main id="conteudo">
        <section className="hero" id="topo" aria-labelledby="hero-title">
          <div className="hero-kicker">
            <Pill tone="accent">Senior Product Designer</Pill>
            <Text>São Paulo · Brasil</Text>
          </div>

          <div className="hero-feature">
            <div className="hero-copy">
              <Text as="h1" className="display-xl" id="hero-title">
                Transformo complexidade em produtos claros, inclusivos e
                escaláveis.
              </Text>
              <div className="hero-intro">
                <Text className="hero-deck">
                  Desenho produtos digitais desde 2006. Nos últimos 11 anos,
                  foco em discovery, UX/UI e estratégia de produto, mais
                  recentemente no Itaú Unibanco, na plataforma íon for
                  Advisors.
                </Text>
                <div className="hero-actions">
                  <Link className="button button--primary" href="#trabalho">
                    Conhecer meu trabalho <ArrowIcon direction="down" />
                  </Link>
                  <Link
                    className="button button--secondary"
                    href="https://www.linkedin.com/in/israelrozar/"
                  >
                    LinkedIn <ArrowIcon />
                  </Link>
                </div>
              </div>
            </div>
            <figure className="portrait">
              <div className="portrait-frame">
                <img
                  src="/images/israel-rozar-portrait-800.webp"
                  srcSet="/images/israel-rozar-portrait-480.webp 480w, /images/israel-rozar-portrait-800.webp 800w"
                  sizes="(max-width: 672px) 58vw, (max-width: 960px) 32vw, 22rem"
                  width="800"
                  height="1000"
                  alt="Retrato profissional de Israel Rozar"
                  decoding="async"
                  fetchPriority="high"
                />
              </div>
            </figure>
          </div>

          <div className="signal-bar" role="group" aria-label="Resumo profissional">
            <div>
              <Text as="strong">8 cases</Text>
              <Text>documentados neste portfólio</Text>
            </div>
            <div>
              <Text as="strong">11 anos</Text>
              <Text>dedicados a produto e UX</Text>
            </div>
            <div>
              <Text as="strong">Fintech + saúde</Text>
              <Text>experiência em domínios complexos</Text>
            </div>
            <div>
              <Text as="strong">WCAG + IA</Text>
              <Text>práticas inclusivas e experimentação responsável</Text>
            </div>
          </div>
        </section>

        <section className="specialties-band" aria-label="Áreas de especialidade">
          <div>
            <span>Product Discovery</span>
            <span aria-hidden="true">•</span>
            <span>UX Strategy</span>
            <span aria-hidden="true">•</span>
            <span>Design Systems</span>
            <span aria-hidden="true">•</span>
            <span>Acessibilidade</span>
            <span aria-hidden="true">•</span>
            <span>IA responsável</span>
          </div>
        </section>

        <section className="section about" aria-labelledby="sobre">
          <SectionHeading
            index="01"
            eyebrow="Posicionamento"
            id="sobre"
            title="Design como ponte entre pessoas, negócio e tecnologia."
          />
          <div className="about-grid">
            <Text className="lead">
              Atuo onde o problema ainda não está claro e a solução precisa
              equilibrar necessidades humanas, viabilidade técnica e objetivos
              de negócio.
            </Text>
            <div className="about-copy">
              <Text>
                Minha experiência combina repertório de interface com visão
                sistêmica. Conduzo discovery, estruturo jornadas e interfaces,
                facilito decisões com times multidisciplinares e conecto
                qualidade da experiência a resultados observáveis.
              </Text>
              <Text>
                Em trabalhos recentes, aproximei design systems, acessibilidade
                e inteligência artificial para melhorar consistência,
                documentação e fluxos de trabalho — sem perder rigor ou
                responsabilidade.
              </Text>
            </div>
          </div>

          <div className="capability-grid">
            {capabilities.map((capability) => (
              <article className="capability-card" key={capability.index}>
                <Text as="span">{capability.index}</Text>
                <Text as="h3">{capability.title}</Text>
                <Text>{capability.description}</Text>
              </article>
            ))}
          </div>
        </section>

        <section className="section work" aria-labelledby="trabalho">
          <SectionHeading
            index="02"
            eyebrow="Cases"
            id="trabalho"
            title="Decisões documentadas em jornadas críticas."
          />

          <article className="featured-case">
            <div className="case-summary">
              <div className="case-kicker">
                <Pill>Saúde · UX Lead</Pill>
                <Text>Einstein × Foursys · registros de 2022</Text>
              </div>
              <Text as="h3">
                <Link className="card-link" href="/cases/einstein-laudos">
                  Uma linguagem visual modular para laudos heterogêneos.
                </Link>
              </Text>
              <Text className="case-lead">
                Um trabalho coletivo entre pesquisa, conteúdo, interface e
                viabilidade técnica para facilitar a localização de informações
                sem simplificar indevidamente o contexto clínico.
              </Text>
              <div className="case-role">
                <Text as="strong">Atuação documentada</Text>
                <ul>
                  <li>Israel Rozar — UX Lead</li>
                  <li>Pesquisa com médicos e questionário com pacientes</li>
                  <li>Sistematização de dados, exceções e componentes</li>
                  <li>Testes, revisão pós-teste e discussão com arquitetura</li>
                </ul>
              </div>
            </div>

            <div className="case-evidence" role="group" aria-label="Escopo da pesquisa">
              <Text as="span">Universos de evidência</Text>
              <div className="evidence-grid">
                <div>
                  <Text as="strong">4</Text>
                  <Text>entrevistas médicas semiestruturadas</Text>
                </div>
                <div>
                  <Text as="strong">121</Text>
                  <Text>respostas no questionário exploratório</Text>
                </div>
                <div>
                  <Text as="strong">14</Text>
                  <Text>categorias de laudos no escopo</Text>
                </div>
                <div>
                  <Text as="strong">80+</Text>
                  <Text>laudos no inventário descrito</Text>
                </div>
              </div>
              <Text className="evidence-note">
                Amostras com objetivos diferentes: não se somam e não
                representam conquistas individuais.
              </Text>
            </div>
          </article>

          <div className="case-summary-cta">
            <Text>
              Pesquisa, sistema modular, comparação visual, resultados de teste
              e limites documentados em uma leitura dedicada.
            </Text>
            <Link
              className="button button--primary"
              href="/cases/einstein-laudos"
              ariaLabel="Ler case completo: Einstein · Laudos médicos"
              tabIndex={-1}
            >
              Ler case completo <ArrowIcon />
            </Link>
          </div>

          <article className="featured-case featured-case--secondary">
            <div className="case-summary">
              <div className="case-kicker">
                <Pill>Energia · Service design</Pill>
                <Text>Neoenergia · EY × Livework · P&D ANEEL</Text>
              </div>
              <Text as="h3">
                <Link className="card-link" href="/cases/neoenergia-conexao-digital">
                  Discovery e service design para o ecossistema Neoenergia
                </Link>
              </Text>
              <Text className="case-lead">
                Mapeamento integral e redesenho de processos omnicanal no setor
                elétrico, identificando oportunidades sistêmicas de automação
                para reduzir gargalos operacionais e atritos de faturamento para
                34 milhões de pessoas em 4 distribuidoras.
              </Text>
              <div className="case-role">
                <Text as="strong">Atuação documentada</Text>
                <ul>
                  <li>
                    Israel Rozar — Senior Product Designer / Service Designer
                  </li>
                  <li>
                    Pesquisa qualitativa, shadowing e auditoria de silos
                    operacionais
                  </li>
                  <li>
                    5 macro-etapas do ciclo de vida em blueprints de serviço
                  </li>
                  <li>Jornadas, oportunidades e visão futura de serviço</li>
                </ul>
              </div>
            </div>

            <div
              className="case-evidence"
              role="group"
              aria-label="Escala oficial da concessão"
            >
              <Text as="span">Escala oficial</Text>
              <div className="evidence-grid">
                <div>
                  <Text as="strong">34M</Text>
                  <Text>habitantes atendidos</Text>
                </div>
                <div>
                  <Text as="strong">13,9M</Text>
                  <Text>clientes faturados</Text>
                </div>
                <div>
                  <Text as="strong">5</Text>
                  <Text>estágios em blueprints</Text>
                </div>
                <div>
                  <Text as="strong">4</Text>
                  <Text>distribuidoras no contexto</Text>
                </div>
              </div>
              <Text className="evidence-note">
                Dados históricos da organização e recorte de discovery. A escala
                da concessão não representa um resultado de implantação do
                projeto.
              </Text>
            </div>
          </article>

          <div className="case-summary-cta">
            <Text>
              Auditoria de silos operacionais, blueprints das 5 etapas da
              jornada, oportunidades e visão futura em uma leitura dedicada.
            </Text>
            <Link
              className="button button--primary"
              href="/cases/neoenergia-conexao-digital"
              ariaLabel="Ler case completo: Neoenergia · Service design"
              tabIndex={-1}
            >
              Ler case completo <ArrowIcon />
            </Link>
          </div>

          <article className="featured-case featured-case--secondary">
            <div className="case-summary">
              <div className="case-kicker">
                <Pill>Telecom · UX corporativo</Pill>
                <Text>Claro · acervo de 2017–2018</Text>
              </div>
              <Text as="h3">
                <Link className="card-link" href="/cases/claro-ativacao-simplificada">
                  Simplificando o atendimento em múltiplos canais.
                </Link>
              </Text>
              <Text className="case-lead">
                Discovery com profissionais da operação e stakeholders,
                mapeamento de jornadas e exploração de interfaces desktop e
                mobile para um sistema corporativo de vendas.
              </Text>
              <div className="case-role">
                <Text as="strong">Recorte de atuação</Text>
                <ul>
                  <li>Pesquisa, workshops, personas e jornadas</li>
                  <li>Definição de fluxos e prototipação</li>
                  <li>Interfaces desktop e mobile</li>
                  <li>Dados do cliente, oferta e confirmação</li>
                </ul>
              </div>
            </div>

            <div
              className="case-evidence"
              role="group"
              aria-label="Escala declarada do discovery"
            >
              <Text as="span">Escala declarada</Text>
              <div className="evidence-grid">
                <div>
                  <Text as="strong">20</Text>
                  <Text>entrevistas</Text>
                </div>
                <div>
                  <Text as="strong">10</Text>
                  <Text>personas</Text>
                </div>
                <div>
                  <Text as="strong">22</Text>
                  <Text>jornadas mapeadas</Text>
                </div>
                <div>
                  <Text as="strong">70</Text>
                  <Text>oportunidades identificadas</Text>
                </div>
              </div>
              <Text className="evidence-note">
                Escopo relatado no case original. Essas quantidades descrevem o
                discovery e não equivalem a resultados operacionais.
              </Text>
            </div>
          </article>

          <div className="case-summary-cta">
            <Text>
              Contexto, discovery, decisões, limites de evidência e próximos
              passos organizados para uma leitura responsável.
            </Text>
            <Link
              className="button button--primary"
              href="/cases/claro-ativacao-simplificada"
              ariaLabel="Ler case completo: Claro · Ativação simplificada"
              tabIndex={-1}
            >
              Ler case completo <ArrowIcon />
            </Link>
          </div>

          <section className="case-roadmap" aria-labelledby="itau-cases-title">
            <div className="roadmap-heading">
              <div>
                <Pill>Fintech · Itaú Unibanco</Pill>
                <Text as="h3" id="itau-cases-title">
                  Cinco recortes de produto para operações complexas.
                </Text>
              </div>
              <div className="roadmap-intro">
                <Text>
                  Problemas, decisões e aprendizados organizados em páginas
                  próprias. Os relatos distinguem propostas de resultados
                  demonstrados.
                </Text>
                <Text>
                  Cada case mostra telas reais, as decisões tomadas e o que
                  ficou como proposta.
                </Text>
              </div>
            </div>
            <div className="roadmap-grid">
              {additionalCases.map((project, index) => (
                <article className="roadmap-card" key={project.slug}>
                  <div className="roadmap-card-top">
                    <span>{String(index + 1).padStart(2, "0")}</span>
                    <span>{project.theme}</span>
                  </div>
                  <div className="roadmap-card-title">
                    <Text as="h4">{project.title}</Text>
                  </div>
                  <Text className="roadmap-reason">{project.description}</Text>
                  <div className="roadmap-facts">
                    <div>
                      <Text as="span">Recorte de design</Text>
                      <Text>{project.focus}</Text>
                    </div>
                  </div>
                  <Link
                    className="roadmap-link"
                    href={`/cases/itau/${project.slug}`}
                  >
                    Ler case: {project.title} <ArrowIcon />
                  </Link>
                </article>
              ))}
            </div>
          </section>
        </section>

        <section className="section experience" aria-labelledby="experiencia">
          <SectionHeading
            index="03"
            eyebrow="Experiência"
            id="experiencia"
            title="Uma carreira construída entre acabamento de interface e visão de sistema."
          />

          <div className="timeline">
            {experience.map((item) => (
              <article className="timeline-item" key={item.company}>
                <Text as="span" className="timeline-period">
                  {item.period}
                </Text>
                <div className="timeline-main">
                  <Text as="h3">{item.company}</Text>
                  <Text as="strong">{item.role}</Text>
                  <Text>{item.description}</Text>
                </div>
                <ul className="timeline-tags" aria-label="Competências">
                  {item.tags.map((tag) => (
                    <li key={tag}>{tag}</li>
                  ))}
                </ul>
              </article>
            ))}
          </div>

          <div className="credentials">
            <div>
              <Text as="span">Formação</Text>
              <Text as="strong">Ciência da Computação</Text>
              <Text>Universidade do Vale do Itajaí · UNIVALI</Text>
            </div>
            <div>
              <Text as="span">Temas de estudo contínuo</Text>
              <Text as="strong">Produto · Experiência · Dados</Text>
              <Text>
                Aprendizado contínuo em produto, experiência e tecnologia.
              </Text>
            </div>
          </div>
        </section>

        <section
          className="contact"
          id="contato"
          aria-labelledby="contact-title"
        >
          <div>
            <SectionLabel index="04">Contato</SectionLabel>
            <Text as="h2" id="contact-title">
              Vamos transformar um problema complexo em uma direção clara.
            </Text>
          </div>
          <div className="contact-side">
            <Text>
              Disponível para conversar sobre posições seniores, consultoria e
              desafios de produto.
            </Text>
            <Link
              className="button button--light"
              href="mailto:irozar@yahoo.com.br"
            >
              Enviar um e-mail <ArrowIcon />
            </Link>
            <div className="contact-links">
              <Link href="/documents/israel-rozar-curriculo.pdf">
                Baixar currículo
              </Link>
              <Link href="https://www.linkedin.com/in/israelrozar/">
                LinkedIn
              </Link>
              <Link href="https://uxfol.io/israelrozar">UXfolio</Link>
            </div>
          </div>
        </section>
      </main>

      <SiteFooter />
    </>
  )
}
