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
      "Governança, documentação e handoff com aplicação prática de padrões WCAG e consistência em escala.",
  },
  {
    index: "04",
    title: "IA aplicada ao design",
    description:
      "Fluxos conversacionais, prompt engineering e automações com critérios de qualidade, rastreabilidade e supervisão humana.",
  },
]

const upcomingCases = [
  {
    priority: "01",
    title: "Movimentações",
    subtitle: "Transição do Extrato EA para o IFA",
    theme: "Operação financeira · Arquitetura",
    status: "Prioridade editorial 1 · Discovery e prototipagem",
    reason:
      "Recompor uma capacidade essencial de consulta sem redesenhar toda a plataforma.",
    decision:
      "Equilibrar contexto local e visibilidade transversal: preservar a arquitetura global, separar recursos de crédito e aprofundar composição e eventos sem perder a consulta de origem.",
    evidence:
      "Alternativas, protótipos e QA local documentados. A hipótese B foi priorizada para validação, mas não equivale a uma decisão de produção.",
    nextStep:
      "Recuperar a referência equivalente da EA, confirmar a escolha final e comparar tarefas de continuidade operacional.",
    href: "/cases/movimentacoes",
  },
  {
    priority: "02",
    title: "Hub de Liquidez e Oportunidades",
    subtitle: "Dados, priorização e próxima ação",
    theme: "Discovery · Pensamento sistêmico",
    status: "Prioridade editorial 2 · Discovery e protótipo",
    reason:
      "Transformar sinais financeiros dispersos em uma próxima ação explicável.",
    decision:
      "Articular lista de trabalho, composição da liquidez e definição de ação, distinguindo atualização do dado de disponibilidade financeira.",
    evidence:
      "Frames de lista, composição e próxima ação, além do registro de prontidão V55. Score, contratos e validação formal permaneciam pendentes.",
    nextStep:
      "Validar regras e denominadores com o domínio e testar se o especialista explica a origem e justifica a ação.",
    href: "/cases/hub-liquidez",
  },
  {
    priority: "03",
    title: "Gestão de Campanhas",
    subtitle: "Configuração, dados, estados e manutenção",
    theme: "Interaction design · Operação em lote",
    status: "Prioridade editorial 3 · Fluxos documentados",
    reason:
      "Conectar configuração, processamento de base e manutenção em uma jornada administrativa coerente.",
    decision:
      "Separar informações da campanha e envio da base; fazer carregamento, vazio, edição, exclusão e feedback orientarem a próxima ação.",
    evidence:
      "AS IS, ideação, screenflows, especificações e estados visuais localizados. Placeholders e transições entre etapas ainda exigem curadoria.",
    nextStep:
      "Selecionar versões sem placeholders e verificar preservação de dados, erros, publicação, foco e retorno após exclusão.",
    href: "/cases/campanhas",
  },
  {
    priority: "04",
    title: "Registros de Atendimento",
    subtitle: "Resumos inteligentes com IA",
    theme: "IA aplicada · Eficiência operacional",
    status: "Prioridade editorial 4 · Validação reportada",
    metric: "150 → 27s",
    metricLabel: "−82% no tempo da tarefa · resultado reportado",
    reason:
      "Recuperar o contexto recente e reduzir o esforço de documentar um atendimento.",
    decision:
      "Aproximar os cinco resumos recentes do momento da ação e usar IA como apoio ao registro, sem atribuir correção automática ao conteúdo.",
    evidence:
      "A redução estimada representa 123 segundos por registro no cenário reportado. Protocolo, amostra, dispersão e telas equivalentes não foram recuperados.",
    nextStep:
      "Recuperar a fonte primária e avaliar fidelidade, omissões, correções, confiança e consulta ao registro original.",
  },
]

const experience = [
  {
    period: "2024 — 2026",
    company: "Itaú Unibanco",
    role: "Senior Product Designer",
    description:
      "Product Discovery e design para a plataforma íon for Advisors e ferramentas operacionais de assessoria de investimentos.",
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
    tags: ["UX/UI", "E-commerce", "Craft"],
  },
]

function SectionHeading({
  index,
  eyebrow,
  title,
  id,
}: {
  index: string
  eyebrow: string
  title: string
  id: string
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
            <Text as="h1" className="display-xl" id="hero-title">
              Transformo complexidade em produtos claros, inclusivos e
              escaláveis.
            </Text>
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
              <figcaption>
                <span aria-hidden="true" />
                Design com clareza e intenção
              </figcaption>
            </figure>
          </div>

          <div className="hero-intro">
            <Text className="hero-deck">
              Desde 2006 desenho experiências digitais. Nos últimos 11 anos,
              atuo entre discovery, UX/UI e estratégia de produto em desafios de
              fintech, saúde e operações complexas.
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

          <div className="signal-bar" aria-label="Resumo profissional">
            <div>
              <Text as="strong">Desde 2006</Text>
              <Text>em projetos digitais</Text>
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
              <Text>acessibilidade e experimentação responsável</Text>
            </div>
          </div>
        </section>

        <section className="marquee" aria-label="Áreas de especialidade">
          <div>
            <span>Product Discovery</span>
            <span aria-hidden="true">•</span>
            <span>UX Strategy</span>
            <span aria-hidden="true">•</span>
            <span>Design Systems</span>
            <span aria-hidden="true">•</span>
            <span>Acessibilidade</span>
            <span aria-hidden="true">•</span>
            <span>Fluxos com IA</span>
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
                Minha experiência combina repertório de craft com visão
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
            eyebrow="Trabalho selecionado"
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
                Uma linguagem visual modular para laudos heterogêneos.
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

            <div className="case-evidence" aria-label="Escopo da pesquisa">
              <Text as="span">Universos de evidência</Text>
              <div className="evidence-grid">
                <div>
                  <Text as="strong">04</Text>
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
                  <Text as="strong">44</Text>
                  <Text>participantes reportados nos testes</Text>
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
            >
              Ler case completo <ArrowIcon />
            </Link>
          </div>

          <section className="case-roadmap" aria-labelledby="roadmap-title">
            <div className="roadmap-heading">
              <div>
                <Pill tone="accent">Dossiês em preparação · Itaú Unibanco</Pill>
                <Text as="h3" id="roadmap-title">
                  Quatro recortes para discutir diferentes dimensões de
                  senioridade.
                </Text>
              </div>
              <div className="roadmap-intro">
                <Text>
                  Projetos para a plataforma íon for Advisors e ferramentas
                  operacionais de assessoria de investimentos.
                </Text>
                <Text>
                  Movimentações, Hub e Campanhas têm a base visual mais
                  rastreável. Registros com IA complementa o conjunto com um
                  resultado de tempo reportado. Todos permanecem como cases em
                  preparação.
                </Text>
              </div>
            </div>

            <div className="roadmap-grid">
              {upcomingCases.map((project) => (
                <article className="roadmap-card" key={project.priority}>
                  <div className="roadmap-card-top">
                    <Text as="span">{project.priority}</Text>
                    <Text as="span">{project.theme}</Text>
                  </div>
                  <div className="roadmap-card-title">
                    <Text as="h4">{project.title}</Text>
                    <Text>{project.subtitle}</Text>
                  </div>
                  {project.metric && (
                    <div className="roadmap-metric">
                      <Text as="strong">{project.metric}</Text>
                      <Text>{project.metricLabel}</Text>
                    </div>
                  )}
                  <Text className="roadmap-reason">{project.reason}</Text>
                  <div className="roadmap-facts">
                    <div>
                      <Text as="span">Decisão de design</Text>
                      <Text>{project.decision}</Text>
                    </div>
                    <div>
                      <Text as="span">Base atual</Text>
                      <Text>{project.evidence}</Text>
                    </div>
                  </div>
                  <div className="roadmap-status">
                    <Text as="strong">{project.status}</Text>
                    <Text>{project.nextStep}</Text>
                  </div>
                  {project.href && (
                    <Link className="roadmap-link" href={project.href}>
                      Abrir dossiê em preparação <ArrowIcon />
                    </Link>
                  )}
                </article>
              ))}
            </div>

            <aside className="roadmap-note">
              <Text as="strong">Critério editorial</Text>
              <Text>
                Telas, métricas e decisões só serão promovidas no portfólio
                quando houver fonte, contexto, autorização e contribuição
                individual verificáveis. O dado “150 → 27s” equivale a 82% de
                redução na tarefa reportada, não a 82% de produtividade ou
                impacto operacional confirmado.
              </Text>
            </aside>
          </section>
        </section>

        <section className="section experience" aria-labelledby="experiencia">
          <SectionHeading
            index="03"
            eyebrow="Trajetória"
            id="experiencia"
            title="Uma carreira construída entre craft e visão sistêmica."
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
              <Text as="span">Certificações e formação contínua</Text>
              <Text as="strong">
                Product Launches · UX Design · Data & Analytics
              </Text>
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

