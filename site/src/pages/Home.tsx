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
    description: "Organização de saldos, projeções e oportunidades para assessores de investimentos.",
  },
  {
    slug: "claro-ativacao-simplificada",
    href: "/cases/claro-ativacao-simplificada",
    client: "Claro Brasil",
    title: "Ativação de planos e televendas",
    role: "UX/UI Designer",
    scope: "22 jornadas mapeadas · 70+ validações",
    description: "Redesenho da jornada de venda e ativação de planos para equipes de atendimento e lojas.",
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
  { org: "Itaú Unibanco", role: "Senior Product Designer · Plataforma IFA", period: "2024 – 2026" },
  { org: "Consultoria Independente", role: "Senior UX Consultant · Produtos Digitais", period: "2022 – atual" },
  { org: "Foursys + Hospital Albert Einstein", role: "UX Lead · Padrão de Laudos Clínicos", period: "2022" },
  { org: "EY · R/GA", role: "Senior UX Consultant & Product Designer", period: "2020 – 2022" },
  { org: "Formação & Base", role: "Ciência da Computação (Univali) · Design Digital", period: "2006 – 2019" },
]

export default function Home() {
  return (
    <div className="portfolio-site pf-home-compact">
      <PageMeta
        title="Israel Rozar — Senior Product Designer"
        description="Senior Product Designer com atuação desde 2006. Projetos de saúde, finanças, telecom e energia: conheça o contexto, as decisões e as entregas."
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
            <p className="pf-lead">Desde 2006, atuo em pesquisa e design de produtos digitais. No Itaú, liderei frentes de design para especialistas de investimentos.</p>
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
            <figcaption>Israel Rozar</figcaption>
          </figure>
        </section>
        <section className="pf-work pf-section" id="trabalho" aria-labelledby="work-title">
          <div className="pf-container">
            <h2 id="work-title">Projetos selecionados</h2>
            <p className="pf-work-intro">Contexto, decisões de design e entregas em saúde, serviços financeiros, telecom e energia. Estudos de caso protegidos por senha.</p>
            <article className="pf-featured" id="project-einstein-laudos">
              <div className="pf-featured-story">
                <p className="pf-home-project-client">Hospital Albert Einstein · UX Lead</p>
                <h3>Estrutura modular para laudos clínicos.</h3>
                <p className="pf-home-scope">14 entregáveis · 121 pacientes · 4 médicos especialistas</p>
                <p>Pesquisa e arquitetura da informação para organizar laudos de diferentes exames em uma estrutura comum.</p>
                <div className="pf-featured-actions">
                  <Link className="pf-button pf-button-lime" href="/cases/einstein-laudos">Ver estudo de caso <ArrowIcon /><span className="pf-sr-only">: Hospital Albert Einstein</span></Link>
                  <CaseReadingTime href="/cases/einstein-laudos" />
                </div>
              </div>
              <figure className="pf-case-preview">
                <img src={assetUrl("/images/hiae-proposta-v3-tablet-1600.webp")} width="1200" height="675" loading="eager" decoding="async" alt="Proposta de laudo clínico com seções de exame, resultados e referências organizadas em uma estrutura modular." />
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
                    <Link className="pf-project-link" href={project.href}>Ver case <ArrowIcon /><span className="pf-sr-only">: {project.title}</span></Link>
                  </div>
                </article>
              ))}
            </div>
            <div className="pf-home-submodules" aria-label="Outros módulos do ecossistema Itaú IFA">
              <span className="pf-home-submodules-label">Outros recortes no Itaú (IFA):</span>
              {itauSubmodules.map(item => (
                <span key={item.href} className="pf-home-submodules-item">{item.label}</span>
              ))}
            </div>
          </div>
        </section>
        <section className="pf-about pf-section" id="sobre" aria-labelledby="about-title">
          <div className="pf-container pf-home-about">
            <h2 id="about-title">Sobre minha atuação</h2>
            <div>
              <p id="experiencia">Experiência em saúde, serviços financeiros, telecom e energia. Trabalho com pesquisa, arquitetura da informação e design de interfaces em colaboração com Produto e Engenharia.</p>
              <p>Exploro recursos de IA com revisão humana e foco em acessibilidade digital (WCAG 2.2).</p>
              <ul className="pf-home-trajectory" aria-label="Trajetória profissional resumida">
                {trajectory.map(item => (
                  <li key={item.org}>
                    <div><strong>{item.org}</strong> · {item.role}</div>
                    <span>{item.period}</span>
                  </li>
                ))}
              </ul>
              <Link className="pf-home-cv" href={assetUrl("/documents/israel-rozar-curriculo.pdf")} download="Israel-Rozar-Curriculo.pdf">Ver trajetória completa no currículo (PDF)</Link>
            </div>
          </div>
        </section>
        <ContactSection compact />
      </main>
      <SiteFooter />
    </div>
  )
}
