import { ArrowIcon, DownloadIcon, Link, assetUrl } from "../design-system"
import { CaseReadingTime } from "../components/CaseReadingTime"
import { PageMeta } from "../components/PageMeta"
import { ContactSection, SiteFooter, SiteHeader } from "../components/SiteChrome"
import "../portfolio.css"

const projects = [
  {
    slug: "hub-liquidez",
    href: "/cases/itau/hub-liquidez",
    client: "Itaú Unibanco",
    title: "Hub de Liquidez e Oportunidades",
    role: "Senior Product Designer",
    scope: "íon for Advisors · 4 módulos operacionais",
    description: "Organização de saldos, projeções e oportunidades para especialistas de investimentos e assessores.",
  },
  {
    slug: "claro-ativacao-simplificada",
    href: "/cases/claro-ativacao-simplificada",
    client: "Claro Brasil",
    title: "Ativação de planos e televendas",
    role: "UX/UI Designer",
    scope: "22 jornadas unificadas · 20 entrevistas · 70 oportunidades",
    description: "Unificação da jornada de venda e ativação de planos para equipes de lojas físicas, televendas e campo.",
  },
  {
    slug: "neoenergia-conexao-digital",
    href: "/cases/neoenergia-conexao-digital",
    client: "Neoenergia",
    title: "Atendimento e operação de campo",
    role: "Senior Product Designer · Service Design",
    scope: "4 distribuidoras · 5 blueprints · 118 ideias",
    description: "Mapeamento de jornadas e serviços para conectar o atendimento digital à operação em campo.",
  },
]

const itauSubmodules = [
  { label: "Gestão de Vencimentos", href: "/cases/itau/vencimentos" },
  { label: "Movimentações", href: "/cases/itau/movimentacoes" },
  { label: "Gestão de Campanhas", href: "/cases/itau/campanhas" },
]

const trajectory = [
  { org: "Itaú Unibanco", role: "Senior Product Designer · Plataforma IFA (íon for Advisors)", period: "2024 – 2026" },
  { org: "Consultoria Independente", role: "Senior UX Consultant · Produtos Digitais", period: "2022 – atual" },
  { org: "Foursys + Hospital Albert Einstein", role: "UX Lead · Padrão de Laudos Clínicos", period: "2022" },
  { org: "EY · R/GA", role: "Senior UX Consultant & Product Designer", period: "2020 – 2022" },
  { org: "Moot · Walmart · GFT · Principia e outras", role: "Design de produtos digitais, UX/UI e direção de arte", period: "2006 – 2019" },
]

export default function Home() {
  return (
    <div className="portfolio-site pf-home-compact">
      <PageMeta
        title="Israel Rozar — Senior Product Designer"
        description="Senior Product Designer com mais de 15 anos de experiência. Projetos em saúde, finanças, telecom e energia: contexto, decisões e entregas."
      />
      <a className="skip-link" href="#conteudo">Pular para o conteúdo</a>
      <SiteHeader />
      <main id="conteudo" tabIndex={-1}>
        <section className="pf-hero pf-container" id="topo" aria-labelledby="hero-title">
          <div className="pf-hero-copy">
            <div className="pf-kicker">
              <span>Senior Product Designer</span>
              <span>São Paulo · Brasil</span>
            </div>
            <h1 id="hero-title">Design de produtos para saúde, finanças e serviços essenciais.</h1>
            <p className="pf-lead">Com mais de 15 anos de experiência, estruturo fluxos operacionais e sistemas de interface com Produto e Engenharia. No Itaú Unibanco, conduzi pesquisa e design no íon for Advisors para especialistas de investimentos e assessores.</p>
            <div className="pf-actions">
              <a className="pf-button pf-button-pine" href="#trabalho">Ver projetos</a>
              <a className="pf-button pf-button-outline" href={assetUrl("/documents/israel-rozar-curriculo.pdf")} download="Israel-Rozar-Curriculo.pdf">Currículo (PDF) <DownloadIcon /></a>
            </div>
          </div>
          <figure className="pf-portrait">
            <div className="pf-portrait-image">
              <img
                src={assetUrl("/images/israel-rozar-treated-800.webp")}
                srcSet={`${assetUrl("/images/israel-rozar-treated-480.webp")} 480w, ${assetUrl("/images/israel-rozar-treated-800.webp")} 800w`}
                sizes="(max-width: 700px) 96px, 320px"
                width="800" height="1000" alt="Israel Rozar, Senior Product Designer" fetchPriority="high"
              />
            </div>
            <figcaption>
              <span>Israel Rozar</span>
              <span className="pf-portrait-brands">Itaú · Einstein · R/GA · EY</span>
            </figcaption>
          </figure>
        </section>
        <section className="pf-work pf-section" id="trabalho" aria-labelledby="work-title">
          <div className="pf-container">
            <h2 id="work-title">Projetos selecionados</h2>
            <p className="pf-work-intro">Contexto, decisões de design e entregas em saúde, finanças, telecom e energia. Estudos de caso protegidos por senha.</p>
            <article className="pf-featured" id="project-einstein-laudos">
              <div className="pf-featured-story">
                <p className="pf-home-project-client">Hospital Albert Einstein · UX Lead</p>
                <h3>Estrutura modular para laudos clínicos</h3>
                <p className="pf-home-scope">14 entregáveis · 121 pacientes · 4 médicos especialistas</p>
                <p>Pesquisa e arquitetura da informação para organizar laudos de diferentes exames em uma estrutura comum.</p>
                <div className="pf-featured-actions">
                  <Link className="pf-button pf-button-lime" href="/cases/einstein-laudos">Ver estudo de caso <ArrowIcon /><span className="pf-sr-only">: Estrutura modular para laudos clínicos — Hospital Albert Einstein</span></Link>
                  <CaseReadingTime href="/cases/einstein-laudos" />
                </div>
              </div>
              <figure className="pf-case-preview">
                <img src={assetUrl("/images/hiae-proposta-v3-tablet-v2.webp")} width="1600" height="900" loading="eager" decoding="sync" fetchPriority="high" alt="Proposta de laudo clínico com seções de exame, resultados e referências organizadas em uma estrutura modular." />
              </figure>
            </article>
            <div className="pf-project-grid pf-project-grid-editorial">
              {projects.map(project => (
                <article className="pf-project" id={`project-${project.slug}`} key={project.slug}>
                  <p className="pf-home-project-client">{project.client}</p>
                  <h3>{project.title}</h3>
                  <p className="pf-home-project-role">{project.role}</p>
                  <p className="pf-home-scope">{project.scope}</p>
                  <p className="pf-project-desc">{project.description}</p>
                  <div className="pf-project-footer">
                    <CaseReadingTime href={project.href} />
                    <Link className="pf-project-link" href={project.href}>Ver estudo de caso <ArrowIcon /><span className="pf-sr-only">: {project.title} — {project.client}</span></Link>
                  </div>
                </article>
              ))}
            </div>
            <div className="pf-home-submodules" role="group" aria-labelledby="itau-submodules-label">
              <span id="itau-submodules-label" className="pf-home-submodules-label">Outros módulos no Itaú · íon for Advisors (IFA):</span>
              {itauSubmodules.map(item => (
                <span key={item.href} className="pf-home-submodules-item">{item.label}</span>
              ))}
            </div>
          </div>
        </section>
        <section className="pf-about pf-section" id="sobre" aria-labelledby="about-title">
          <div className="pf-container pf-trajectory">
            <div className="pf-trajectory-intro">
              <h2 id="about-title">Sobre minha atuação</h2>
              <div className="pf-home-about-role">
                <strong>Senior Product Designer</strong>
                <span>São Paulo, Brasil · Remoto ou híbrido</span>
              </div>
              <p id="experiencia">Atuo em produtos digitais para saúde, finanças, telecom e energia há mais de 15 anos. Conduzo pesquisa com usuários, organização de fluxos operacionais e sistemas de componentes com Produto e Engenharia.</p>
              <p>Documento decisões de interface e critérios de acessibilidade (WCAG 2.2) desde a concepção. Uso IA como apoio em descoberta e prototipagem, mantendo decisões de produto, validação de evidências e revisão técnica sob julgamento humano.</p>
            </div>
            <ul className="pf-timeline" aria-label="Trajetória profissional">
              {trajectory.map(item => (
                <li key={item.org}>
                  <div>
                    <h3>{item.org}</h3>
                    <p>{item.role}</p>
                  </div>
                  <span>{item.period}</span>
                </li>
              ))}
            </ul>
            <aside className="pf-education" aria-label="Formação acadêmica e contínua">
              <div>
                <span className="pf-education-label">Formação acadêmica</span>
                <p><strong>Ciência da Computação</strong></p>
                <span>Universidade do Vale do Itajaí (Univali)</span>
              </div>
              <div>
                <span className="pf-education-label">Estudos complementares</span>
                <p><strong>Design Digital · UX Design · Dados e Análise</strong></p>
                <span>Frentes aplicadas em produto, pesquisa e análise de dados</span>
              </div>
            </aside>
          </div>
        </section>
        <ContactSection />
      </main>
      <SiteFooter />
    </div>
  )
}
