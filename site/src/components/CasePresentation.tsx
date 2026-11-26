import {
  useState,
  useRef,
  useEffect,
  type CSSProperties,
  type MouseEvent,
  type ReactNode,
} from "react"

import { ArrowIcon, Link, Pill, assetUrl } from "../design-system"

import { PageMeta } from "./PageMeta"
import { CaseReadingTime } from "./CaseReadingTime"
import { CaseAccessGate } from "./CaseAccessGate"
import { useLocation } from "react-router"

import { ContactSection, SiteFooter, SiteHeader } from "./SiteChrome"

import "./case-presentation.css"
import "../portfolio.css"

export const caseChapters = [
  ["resumo", "Resumo executivo"],

  ["contexto", "Contexto e desafio"],

  ["descoberta", "Descoberta e recorte"],

  ["decisoes", "Estratégia e decisões"],

  ["solucao", "Solução e validação"],

  ["impacto", "Impacto e reflexão"],

  ["evidencias", "Evidências e créditos"],
] as const

export type CropRect = {
  x: number;
  y: number;
  width: number;
  height: number;
};

export type CaseImage = {
  src: string;
  width: number;
  height: number;
  alt: string;
  caption: string;
  previewCrop?: CropRect;
};

export type CaseNavTarget = {
  title: string;
  href: string;
  context: string;
  kicker?: string;
};

export type CaseCover = {
  heading: string;
  items: string[];
  note: string;
};

export type CaseChapter = {
  id?: string;
  tag?: string;
  title: string;
  content: ReactNode;
};

export type CasePresentationData = {
  title: string;
  context: string;
  headline: string;
  subtitle: string;
  role: string;
  team: string;
  scope: string;
  keyMetric?: string;
  kicker?: string;
  noIndex?: boolean;
  hero?: CaseImage;
  cover?: CaseCover;
  prevCase?: CaseNavTarget;
  nextCase?: CaseNavTarget;
  chapters: CaseChapter[];
};

export function CaseFigure({ image }: { image: CaseImage }) {
  const dialogRef = useRef<HTMLDialogElement>(null)

  const [actualSize, setActualSize] = useState(false)

  const [lightboxOpen, setLightboxOpen] = useState(false)

  const openLightbox = (e: MouseEvent) => {
    e.preventDefault()

    setLightboxOpen(true)
    dialogRef.current?.showModal()
  }

  const closeLightbox = () => {
    dialogRef.current?.close()

    setActualSize(false)
  }

  return (
    <>
      <figure className="cp-figure">
        <button
          type="button"
          className="cp-figure-btn"
          onClick={openLightbox}
          aria-label={`Ampliar imagem: ${image.alt}`}
        >
          {image.previewCrop ? (
            <svg
              className="cp-figure-crop"
              width={image.previewCrop.width}
              height={image.previewCrop.height}
              viewBox={`${image.previewCrop.x} ${image.previewCrop.y} ${image.previewCrop.width} ${image.previewCrop.height}`}
              role="img"
              aria-label={image.alt}
              style={
                {
                  "--case-image-width": `${image.previewCrop.width}px`,

                  aspectRatio: `${image.previewCrop.width} / ${image.previewCrop.height}`,
                } as CSSProperties
              }
            >
              <image
                href={assetUrl(image.src)}
                width={image.width}
                height={image.height}
              />
            </svg>
          ) : (
            <img
              src={assetUrl(image.src)}
              width={image.width}
              height={image.height}
              style={
                {
                  "--case-image-width": `${image.width}px`,

                  aspectRatio: `${image.width} / ${image.height}`,
                } as CSSProperties
              }
              alt={image.alt}
              loading={
                typeof window !== "undefined" &&
                window.location.hash.includes("figmacapture=")
                  ? "eager"
                  : "lazy"
              }
              decoding="async"
            />
          )}
        </button>
        <figcaption className="cp-figure-caption">
          <p className="cp-figure-caption-text">{image.caption}</p>
          <button
            type="button"
            className="cp-lightbox-trigger"
            onClick={openLightbox}
          >
            Ver ampliado <ArrowIcon />
          </button>
        </figcaption>
      </figure>

      <dialog
        ref={dialogRef}
        className="cp-lightbox"
        aria-label={`Visualização ampliada: ${image.alt}`}
        onClick={(e) => {
          if (e.target === dialogRef.current) closeLightbox()
        }}
        onClose={() => {
          setActualSize(false)
          setLightboxOpen(false)
        }}
      >
        <div
          className={`cp-lightbox-content${actualSize ? " is-actual-size" : ""}`}
        >
          <div className="cp-lightbox-header">
            <span className="cp-lightbox-caption">{image.caption}</span>
            <button
              type="button"
              className="cp-lightbox-close"
              onClick={closeLightbox}
              aria-label="Fechar ampliação"
            >
              <span>Fechar</span>
              <svg
                width="14"
                height="14"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                strokeWidth="2.5"
                strokeLinecap="round"
                strokeLinejoin="round"
                aria-hidden="true"
              >
                <line x1="18" y1="6" x2="6" y2="18" />
                <line x1="6" y1="6" x2="18" y2="18" />
              </svg>
            </button>
          </div>
          <div className="cp-lightbox-viewport">
            {image.previewCrop ? (
              <svg
                width={image.previewCrop.width}
                height={image.previewCrop.height}
                viewBox={`${image.previewCrop.x} ${image.previewCrop.y} ${image.previewCrop.width} ${image.previewCrop.height}`}
                role="img"
                aria-label={image.alt}
                onClick={() => setActualSize((value) => !value)}
                className="cp-lightbox-media"
              >
                <image
                  href={assetUrl(image.src)}
                  width={image.width}
                  height={image.height}
                />
              </svg>
            ) : (
              <img
                src={assetUrl(image.src)}
                width={image.width}
                height={image.height}
                alt={image.alt}
                onClick={() => setActualSize((value) => !value)}
                title={actualSize ? "Clique para ajustar à tela" : "Clique para ampliar em tamanho original"}
                className="cp-lightbox-media"
              />
            )}
          </div>
          <div className="cp-lightbox-footer">
            <span>
              Dimensões originais: {image.width} × {image.height} px
            </span>
            <button
              type="button"
              className="cp-lightbox-size"
              aria-pressed={actualSize}
              onClick={() => setActualSize((value) => !value)}
            >
              {actualSize ? "Ajustar à tela" : "Ver em tamanho original"}
            </button>
            <a href={assetUrl(image.src)} target="_blank" rel="noopener noreferrer">
              Abrir imagem original em nova aba <ArrowIcon />
            </a>
          </div>
        </div>
      </dialog>
    </>
  )
}

export function CaseMetrics({ items }: { items: Array<[string, string]> }) {
  return (
    <dl
      className="cp-metrics"
      style={{ "--metric-columns": Math.min(items.length, 3) } as CSSProperties}
    >
      {items.map(([value, label]) => (
        <div key={label}>
          <dt>{label}</dt>
          <dd>{value}</dd>
        </div>
      ))}
    </dl>
  )
}

export function CasePresentation({ data }: { data: CasePresentationData }) {
  return (
    <CaseAccessGate caseName={data.title}>
      <CasePresentationContent data={data} />
    </CaseAccessGate>
  )
}

function CasePresentationContent({ data }: { data: CasePresentationData }) {
  const { pathname } = useLocation()
  const resolvedChapters = data.chapters.map((chapter, i) => ({
    ...chapter,
    resolvedId: chapter.id || caseChapters[i]?.[0] || `capitulo-${i + 1}`,
    resolvedTag: chapter.tag || caseChapters[i]?.[1] || `Seção ${i + 1}`,
  }))
  const [activeChapter, setActiveChapter] = useState<string>(
    resolvedChapters[0]?.resolvedId || "resumo",
  )

  useEffect(() => {
    setActiveChapter(resolvedChapters[0]?.resolvedId || "resumo")
    const chapters = document.querySelectorAll<HTMLElement>(".cp-chapter")

    if (!chapters.length) return

    const observer = new IntersectionObserver(
      (entries) => {
        for (const entry of entries) {
          if (entry.isIntersecting && entry.target.id) {
            setActiveChapter(entry.target.id)
          }
        }
      },

      { rootMargin: "-20% 0px -65% 0px", threshold: 0 },
    )

    chapters.forEach((c) => observer.observe(c))

    return () => observer.disconnect()
  }, [pathname])

  const [readProgress, setReadProgress] = useState(0)

  useEffect(() => {
    let rafId = 0
    const updateProgress = () => {
      const scrollable = document.documentElement.scrollHeight - window.innerHeight
      const ratio = scrollable > 0 ? Math.min(100, Math.max(0, (window.scrollY / scrollable) * 100)) : 0
      setReadProgress(ratio)
    }
    const onScroll = () => {
      if (rafId) cancelAnimationFrame(rafId)
      rafId = requestAnimationFrame(updateProgress)
    }
    updateProgress()
    window.addEventListener("scroll", onScroll, { passive: true })
    return () => {
      if (rafId) cancelAnimationFrame(rafId)
      window.removeEventListener("scroll", onScroll)
    }
  }, [])

  return (
    <div className="case-page-wrapper">
      <div
        className="cp-reading-progress"
        aria-hidden="true"
        style={{ width: `${readProgress}%` }}
      />
      <PageMeta
        title={`${data.title} — Israel Rozar`}
        description={data.subtitle}
        noIndex={data.noIndex}
      />
      <Link className="skip-link" href="#conteudo">
        Pular para o conteúdo
      </Link>
      <SiteHeader casePage />
      <main
        id="conteudo"
        tabIndex={-1}
        className="case-presentation"
        data-template="figma-YIHybVXPe0Hfmja1hAyzQZ-370-17047"
      >
        <section
          className="cp-hero"
          id="topo"
          aria-labelledby="case-title"
          data-name="MasterCaseStudySection"
        >
          <nav aria-label="Trilha de navegação" className="cp-breadcrumb">
            <Link href="/#trabalho">
              <ArrowIcon direction="left" /> Voltar aos cases
            </Link>
          </nav>
          <div className="cp-kicker" data-name="Case Header & Tag">
            <span className="cp-tag-pill">
              {data.kicker || "Design de produto"}
            </span>
            <p className="cp-context">{data.context}</p>
          </div>
          <h1 id="case-title" className="cp-title">{data.headline}</h1>
          <p className="cp-subtitle">{data.subtitle}</p>
          <div className="cp-reading-meta"><CaseReadingTime href={pathname.replace(/\/$/, "")} /></div>

          <div
            className="cp-meta-grid"
            data-name="Metadata Specs Grid (4 Cols)"
          >
            <div className="cp-meta-col">
              <span className="cp-meta-label">MEU PAPEL</span>
              <strong className="cp-meta-value">{data.role}</strong>
            </div>
            <div className="cp-meta-col">
              <span className="cp-meta-label">EQUIPE</span>
              <strong className="cp-meta-value">{data.team}</strong>
            </div>
            <div className="cp-meta-col">
              <span className="cp-meta-label">ESCOPO</span>
              <strong className="cp-meta-value">{data.scope}</strong>
            </div>
            <div className="cp-meta-col">
              <span className="cp-meta-label">RESULTADO-CHAVE</span>
              <strong className="cp-meta-value cp-meta-value--accent">
                {data.keyMetric || "Operação financeira"}
              </strong>
            </div>
          </div>

          {data.cover ? (
            <figure className="cp-concept-cover">
              <span className="cp-cover-eyebrow">
                Síntese visual do projeto
              </span>
              <p className="cp-cover-heading">{data.cover.heading}</p>
              <ol
                className="cp-cover-flow"
                style={
                  {
                    "--cover-columns": Math.min(data.cover.items.length, 3),
                  } as CSSProperties
                }
              >
                {data.cover.items.map((item, index) => (
                  <li key={item}>
                    <span>{String(index + 1).padStart(2, "0")}</span>
                    <strong>{item}</strong>
                  </li>
                ))}
              </ol>
              <figcaption>{data.cover.note}</figcaption>
            </figure>
          ) : (
            data.hero && (
              <div
                className="cp-hero-visual"
                data-name="Master Interface Mockup"
              >
                <CaseFigure image={data.hero} />
              </div>
            )
          )}
        </section>

        <div
          className="cp-body"
          data-name="Deep Dive Narrative: Sticky Sub-navigation + Content"
        >
          <aside
            className="cp-sidebar"
            data-name="Aside - Sticky Sidebar Case Index"
          >
            <div className="cp-sidebar-card">
              <span className="cp-sidebar-header">NESTE CASE</span>
              <nav aria-label="Neste case" className="cp-sidebar-nav">
                <ol>
                  {resolvedChapters.map((chapter, i) => {
                    const isActive = activeChapter === chapter.resolvedId

                    return (
                      <li key={chapter.resolvedId}>
                        <a
                          href={`#${chapter.resolvedId}`}
                          className={isActive ? "is-active" : undefined}
                          aria-current={isActive ? "location" : undefined}
                        >
                          <span className="cp-sidebar-num">
                            {String(i + 1).padStart(2, "0")}
                          </span>
                          <span className="cp-sidebar-text">{chapter.resolvedTag}</span>
                        </a>
                      </li>
                    )
                  })}
                </ol>
              </nav>
              <Link className="cp-back" href="/#trabalho">
                <ArrowIcon direction="left" /> Voltar aos cases
              </Link>
            </div>
          </aside>

          <article
            className="cp-article"
            data-name="Main Case Content Columns"
          >
            {resolvedChapters.map((chapter, i) => (
              <section
                className="cp-chapter"
                id={chapter.resolvedId}
                key={chapter.resolvedId}
                aria-labelledby={`chapter-${i}`}
                data-name={`Section - ${String(i + 1).padStart(2, "0")} ${chapter.resolvedTag.toUpperCase()}`}
              >
                <div className="cp-chapter-badge">
                  <div className="cp-chapter-num-box">
                    {String(i + 1).padStart(2, "0")}
                  </div>
                  <span className="cp-chapter-tag">
                    {chapter.resolvedTag}
                  </span>
                </div>
                <h2 id={`chapter-${i}`} className="cp-chapter-title">
                  {chapter.title}
                </h2>
                <div className="cp-chapter-content">{chapter.content}</div>
              </section>
            ))}
          </article>
        </div>

        <section
          className="cp-explore-section"
          data-name="Navegação / Outros projetos"
        >
          <div className="cp-explore-header">
            <h3 className="cp-explore-title">
              Continue explorando os projetos
            </h3>
            <Link className="cp-explore-all" href="/#trabalho">
              Ver todos os projetos ↗
            </Link>
          </div>

          {(data.prevCase || data.nextCase) && (
            <nav
              className="cp-case-nav"
              aria-label="Navegação entre cases"
            >
              {data.prevCase ? (
                <Link
                  className="cp-case-nav-card cp-case-nav-card--prev"
                  href={data.prevCase.href}
                >
                  <span className="cp-case-nav-label">
                    <ArrowIcon direction="left" /> Case anterior
                  </span>
                  <strong className="cp-case-nav-title">
                    {data.prevCase.title}
                  </strong>
                  <span className="cp-case-nav-context">
                    {data.prevCase.context}
                  </span>
                </Link>
              ) : (
                <div
                  className="cp-case-nav-placeholder"
                  aria-hidden="true"
                />
              )}

              {data.nextCase ? (
                <Link
                  className="cp-case-nav-card cp-case-nav-card--next"
                  href={data.nextCase.href}
                >
                  <span className="cp-case-nav-label">
                    Próximo case <ArrowIcon />
                  </span>
                  <strong className="cp-case-nav-title">
                    {data.nextCase.title}
                  </strong>
                  <span className="cp-case-nav-context">
                    {data.nextCase.context}
                  </span>
                </Link>
              ) : (
                <div
                  className="cp-case-nav-placeholder"
                  aria-hidden="true"
                />
              )}
            </nav>
          )}
        </section>
      </main>

      <ContactSection />

      <SiteFooter />
    </div>
  )
}
