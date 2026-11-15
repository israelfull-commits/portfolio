import { ArrowIcon, ChatIcon, DownloadIcon, Link, MailIcon, assetUrl } from "../design-system"

import { PageMeta } from "../components/PageMeta"

import { ContactSection, SiteFooter, SiteHeader } from "../components/SiteChrome"

import "../portfolio.css"

const projects = [
  {
    slug: "hub-liquidez",
    href: "/cases/itau/hub-liquidez",
    client: "Itaú Unibanco · íon",
    title: "Hub de Liquidez e Oportunidades",
    theme: "Fintech · Discovery e visão sistêmica",
    description:
      "Composição de recursos, projeção de saldos e priorização de clientes em uma plataforma densa para assessores de investimento.",
    decision: "Separar saldo disponível, variação prevista e projeção com origem e janela de tempo explícitas.",
  },
  {
    slug: "claro-ativacao-simplificada",
    href: "/cases/claro-ativacao-simplificada",
    client: "Claro Brasil",
    title: "Ativação Simplificada e Televendas",
    theme: "Telecom · Redesenho de esteira e POS",
    description:
      "Redesenho da esteira de vendas e ativação de planos móveis e combos para equipes de atendimento e lojas próprias.",
    decision: "Redução de etapas de checkout de 12 para 4 telas com validação em tempo real e regras omnichannel.",
  },
  {
    slug: "neoenergia-conexao-digital",
    href: "/cases/neoenergia-conexao-digital",
    client: "Neoenergia · P&D ANEEL",
    title: "Conexão Digital e Service Blueprint",
    theme: "Utilities · Service design sistêmico",
    description:
      "Service blueprint ponta a ponta conectando o trabalho técnico em campo ao atendimento digital em 4 distribuidoras de energia através de 5 blueprints de serviço.",
    decision: "Matriz de 118 oportunidades priorizadas e integração entre despacho de campo e autoatendimento do cliente.",
  },
]

const expertise = [
  [
    "Discovery",
    "Discovery e estratégia",
    "Enquadramento de problemas, pesquisa, síntese, experimentação e priorização para reduzir incerteza antes da entrega.",
  ],

  [
    "UX e UI",
    "UX/UI para produtos complexos",
    "Jornadas, arquitetura da informação e interfaces para operações de alta densidade e contextos regulados.",
  ],

  [
    "Sistemas",
    "Design systems e acessibilidade",
    "Governança, documentação e handoff com práticas de acessibilidade baseadas em WCAG e consistência em escala.",
  ],

  [
    "IA",
    "Experimentação responsável com IA",
    "Exploração de fluxos assistidos por IA com critérios de qualidade, rastreabilidade e supervisão humana.",
  ],
]

const experience = [
  [
    "Consultoria Independente",
    "Senior UX Consultant · Projetos entre vínculos ou em paralelo",
    "2022 – atual",
  ],

  [
    "Itaú Unibanco",
    "Senior Product Designer · Plataforma íon for Advisors",
    "2024 – 2026",
  ],

  [
    "Foursys + Hospital Albert Einstein",
    "UX Lead · Sistema de Laudos Clínicos Modulares",
    "2022",
  ],

  ["EY · R/GA", "Senior UX Consultant & Product Designer", "2020 – 2022"],

  [
    "Moot · Walmart · GFT · Principia & outras",
    "Experiências anteriores em UX/UI, direção de arte e design",
    "2006 – 2019",
  ],
]

function Label({ number, children }: { number: string; children: string }) {
  return (
    <div className="pf-label">
      <span>{number}</span>
      {children}
    </div>
  )
}

export default function Home() {
  return (
    <div className="portfolio-site">
      <PageMeta
        title="Israel Rozar — Senior Product Designer"
        description="Design de produto, discovery e visão sistêmica. Conheça os projetos e a trajetória de Israel Rozar em serviços financeiros, saúde e consultoria."
      />
      <a className="skip-link" href="#conteudo">
        Pular para o conteúdo
      </a>
      <SiteHeader />
      <main id="conteudo">
        <section
          className="pf-hero pf-container"
          id="topo"
          aria-labelledby="hero-title"
        >
          <div className="pf-hero-copy">
            <div className="pf-kicker">
              <span>Senior Product Designer</span>
              <span>São Paulo • Brasil</span>
            </div>
            <h1 id="hero-title">
              Design Estruturado para Ecossistemas de Alta Criticidade.
            </h1>
            <p className="pf-lead">
              Desde 2006 desenho experiências digitais. Recentemente, no Itaú
              Unibanco, liderei frentes de Product discovery e design da
              plataforma IFA para especialistas de investimentos.
            </p>
            <div className="pf-actions">
              <a className="pf-button pf-button-pine" href="#trabalho">
                Conhecer meu trabalho <ArrowIcon direction="down" />
              </a>
              <a
                className="pf-button pf-button-outline"
                href={assetUrl("/documents/israel-rozar-curriculo.pdf")}
                download="Israel-Rozar-Curriculo.pdf"
              >
                Baixar currículo (PDF) <DownloadIcon />
              </a>
            </div>
          </div>
          <figure className="pf-portrait">
            <div className="pf-portrait-image">
              <img
                src={assetUrl("/images/israel-rozar-treated-800.webp")}
                srcSet={`${assetUrl("/images/israel-rozar-treated-480.webp")} 480w, ${assetUrl("/images/israel-rozar-treated-800.webp")} 800w`}
                sizes="(max-width: 700px) 100vw, 360px"
                width="800"
                height="1000"
                alt="Israel Rozar, Senior Product Designer"
                fetchPriority="high"
              />
              <span className="pf-photo-label">IR • 2026</span>
              <span className="pf-photo-place">São Paulo • BR</span>
            </div>
            <figcaption>
              <span>Senior product designer</span>
              <span>Einstein · Itaú · R/GA</span>
            </figcaption>
          </figure>
        </section>
        <section
          className="pf-work pf-section"
          id="trabalho"
          aria-labelledby="work-title"
        >
          <div className="pf-container">
            <Label number="01">Trabalhos selecionados</Label>
            <h2 id="work-title">Projetos, decisões e contribuições.</h2>
            <p className="pf-section-intro">
              Um case em destaque e três projetos estratégicos que apresentam minha atuação
              em design systems, plataformas complexas, telecom e service design.
            </p>
            <article className="pf-featured" id="project-einstein-laudos">
              <div className="pf-featured-story">
                <div className="pf-featured-meta">
                  <span>★ Case em destaque · Saúde</span>
                  <span>Hospital Israelita Albert Einstein</span>
                </div>
                <h3>Uma linguagem visual modular para laudos heterogêneos.</h3>
                <p>
                  Pesquisa e arquitetura de informação para estruturar mais de 80
                  exames distintos em uma linguagem modular previsível, facilitando
                  a tomada de decisão médica e reduzindo a ansiedade de pacientes.
                </p>
                <div className="pf-contribution">
                  <span>Atuação como UX Lead</span>
                  <p>
                    Liderança de pesquisa clínica, sistematização de taxonomias,
                    definição de componentes modulares, testes com médicos e
                    pacientes, e alinhamento com arquitetura e engenharia.
                  </p>
                </div>
                <Link
                  className="pf-button pf-button-lime"
                  href="/cases/einstein-laudos"
                >
                  Explorar estudo de caso completo <ArrowIcon />
                </Link>
              </div>
              <div className="pf-featured-evidence">
                <figure className="pf-case-preview">
                  <Link
                    href="/cases/einstein-laudos"
                    ariaLabel="Explorar estudo de caso completo do Hospital Albert Einstein"
                  >
                    <img
                      src={assetUrl("/images/hiae-proposta-v3-tablet-1600.webp")}
                      width="1200"
                      height="675"
                      loading="eager"
                      fetchPriority="high"
                      decoding="async"
                      alt="Layout real da proposta de solução v3: estrutura modular canônica de laudo clínico do Hospital Albert Einstein."
                    />
                  </Link>
                  <figcaption>
                    Estrutura modular de laudos clínicos (layout real da proposta de solução v3)
                  </figcaption>
                </figure>
                <h4>Evidências de discovery e testes</h4>
                <dl className="pf-evidence-grid">
                  {[
                    ["14", "Famílias de laudos sistematizadas"],
                    ["121", "Pacientes em discovery e testes"],
                  ].map(([n, t]) => (
                    <div key={n}>
                      <dt>{n}</dt>
                      <dd>{t}</dd>
                    </div>
                  ))}
                </dl>
                <div className="pf-partners">
                  Hospital Albert Einstein <span>Foursys Design</span>
                </div>
              </div>
            </article>
            <div className="pf-project-grid pf-project-grid-editorial">
              {projects.map((p, i) => (
                <article
                  className="pf-project"
                  key={p.slug}
                  id={`project-${p.slug}`}
                >
                  <div className="pf-project-meta">
                    <span>{String(i + 1).padStart(2, "0")}</span>
                    <span>{p.client}</span>
                  </div>
                  <div className="pf-project-heading">
                    <h3>{p.title}</h3>
                    <p className="pf-project-theme">{p.theme}</p>
                  </div>
                  <p className="pf-project-desc">{p.description}</p>
                  {p.decision && (
                    <p className="pf-project-decision">
                      <strong>Decisão: </strong>
                      {p.decision}
                    </p>
                  )}
                  <Link href={p.href} className="pf-project-link">
                    Explorar o case <span aria-hidden="true">→</span>
                    <span className="pf-sr-only">: {p.title}</span>
                  </Link>
                </article>
              ))}
            </div>
            <div className="pf-submodules-callout" style={{ marginTop: "2rem", padding: "1.25rem 1.5rem", borderRadius: "1rem", background: "var(--paper-deep, #F2EFE8)", border: "1px solid var(--line, #E2DDD5)", display: "flex", flexWrap: "wrap", alignItems: "center", justifyContent: "space-between", gap: "1rem" }}>
              <span style={{ fontSize: "0.9375rem", color: "var(--ink-muted, #4A5568)" }}>
                Outros fluxos do ecossistema Itaú Corretora:
              </span>
              <div style={{ display: "flex", gap: "1rem", flexWrap: "wrap" }}>
                <Link href="/cases/itau/vencimentos" style={{ fontSize: "0.875rem", fontWeight: 600, color: "var(--forest, #0A2E1D)", textDecoration: "underline" }}>Vencimentos →</Link>
                <Link href="/cases/itau/movimentacoes" style={{ fontSize: "0.875rem", fontWeight: 600, color: "var(--forest, #0A2E1D)", textDecoration: "underline" }}>Movimentações →</Link>
                <Link href="/cases/itau/campanhas" style={{ fontSize: "0.875rem", fontWeight: 600, color: "var(--forest, #0A2E1D)", textDecoration: "underline" }}>Gestão de Campanhas →</Link>
              </div>
            </div>
          </div>
        </section>
        <section
          className="pf-about pf-section"
          id="sobre"
          aria-labelledby="about-title"
        >
          <div className="pf-container">
            <Label number="02">Expertise</Label>
            <div className="pf-about-heading">
              <h2 id="about-title">
                Design como ponte entre pessoas, negócio e tecnologia.
              </h2>
              <div>
                <p>
                  Atuo onde o problema ainda não está claro e a solução precisa
                  equilibrar necessidades humanas, viabilidade técnica e
                  objetivos de negócio.
                </p>
                <p>
                  Minha experiência combina repertório de craft com visão
                  sistêmica. Conduzo discovery, estruturo jornadas e interfaces,
                  facilito decisões com times multidisciplinares e conecto a
                  qualidade da experiência a resultados observáveis.
                </p>
              </div>
            </div>
            <div className="pf-expertise-grid">
              {expertise.map(([tag, title, text], i) => (
                <article className="pf-expertise" key={title}>
                  <img
                    className="pf-expertise-icon"
                    src={assetUrl(`/icons/${["discovery", "layout", "systems", "brain"][i]}.svg`)}
                    width="20"
                    height="20"
                    alt=""
                    aria-hidden="true"
                  />
                  <span>
                    {String(i + 1).padStart(2, "0")} / {tag}
                  </span>
                  <h3>{title}</h3>
                  <p>{text}</p>
                </article>
              ))}
            </div>
          </div>
        </section>
        <section
          className="pf-trajectory pf-section pf-container"
          id="experiencia"
          aria-labelledby="experience-title"
        >
          <div className="pf-trajectory-intro">
            <Label number="03">Trajetória</Label>
            <h2 id="experience-title">
              Uma carreira construída entre craft e visão sistêmica.
            </h2>
            <p>
              Atuação em produtos digitais desde 2006, com experiência em
              serviços financeiros, saúde e consultoria. Trabalho com pesquisa,
              decisões de design e colaboração com engenharia.
            </p>
          </div>
          <ol className="pf-timeline">
            {experience.map(([company, role, date]) => (
              <li key={company}>
                <div>
                  <h3>{company}</h3>
                  <p>{role}</p>
                </div>
                <span>{date}</span>
              </li>
            ))}
          </ol>
          <aside className="pf-education" aria-label="Formação">
            <div>
              <h3>Formação acadêmica</h3>
              <p>Ciência da Computação</p>
              <span>Universidade do Vale do Itajaí (Univali)</span>
            </div>
            <div>
              <h3>Formação contínua</h3>
              <p>
                Product Launches
                <br />
                UX Design
                <br />
                Data & Analytics
              </p>
            </div>
          </aside>
        </section>
        <ContactSection />
      </main>
      <SiteFooter />
    </div>
  )
}
