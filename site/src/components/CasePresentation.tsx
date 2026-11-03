import {
  useState,
  useRef,
  useEffect,
  type CSSProperties,
  type MouseEvent,
  type ReactNode,
} from "react"

import { ArrowIcon, Link, Pill } from "../design-system"

import { PageMeta } from "./PageMeta"

import { SiteFooter, SiteHeader } from "./SiteChrome"

import "./case-presentation.css"

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
                href={image.src}
                width={image.width}
                height={image.height}
              />
            </svg>
          ) : (
            <img
              src={image.src}
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
        <figcaption>
          {image.caption}
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
        <div className="cp-lightbox-content">
          <div className="cp-lightbox-header">
            <p className="cp-lightbox-caption">{image.caption}</p>
            <button
              type="button"
              className="cp-lightbox-close"
              onClick={closeLightbox}
              aria-label="Fechar visualização ampliada"
            >
              ✕
            </button>
          </div>
          <div
            className={`cp-lightbox-media${
              actualSize ? " cp-lightbox-media--actual" : ""
            }`}
          >
            {lightboxOpen && (
              <img
                src={image.src}
                width={image.width}
                height={image.height}
                alt={image.alt}
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
            <a href={image.src} target="_blank" rel="noopener noreferrer">
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
  const [activeChapter, setActiveChapter] = useState<string>(caseChapters[0][0])

  useEffect(() => {
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
  }, [])

  return (
    <>
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
        className="case-presentation"
        data-template="figma-YIHybVXPe0Hfmja1hAyzQZ-31-10884"
      >
        <section className="cp-hero" id="topo" aria-labelledby="case-title">
          <nav aria-label="Trilha de navegação" className="cp-breadcrumb">
            <Link href="/#trabalho">
              <ArrowIcon direction="left" /> Voltar aos cases
            </Link>
          </nav>
          <div className="cp-kicker">
            <Pill tone="accent">{data.kicker || "Design de produto"}</Pill>
            <p>{data.context}</p>
          </div>
          <h1 id="case-title">{data.headline}</h1>
          <p className="cp-subtitle">{data.subtitle}</p>
          <div className="cp-meta">
            <div>
              <span>Meu papel</span>
              <strong>{data.role}</strong>
            </div>
            <div>
              <span>Equipe</span>
              <strong>{data.team}</strong>
            </div>
            <div>
              <span>Escopo</span>
              <strong>{data.scope}</strong>
            </div>
            <a href="#resumo">
              Ler o case <ArrowIcon direction="down" />
            </a>
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
              <div className="cp-hero-visual">
                <CaseFigure image={data.hero} />
              </div>
            )
          )}
        </section>
        <div className="cp-body">
          <aside className="cp-sidebar">
            <nav aria-label="Neste case">
              <strong>Neste case</strong>
              <ol>
                {caseChapters.map(([id, label], i) => {
                  const isActive = activeChapter === id

                  return (
                    <li key={id}>
                      <a
                        href={`#${id}`}
                        className={isActive ? "is-active" : undefined}
                        aria-current={isActive ? "location" : undefined}
                      >
                        <span>{String(i + 1).padStart(2, "0")}</span>
                        {label}
                      </a>
                    </li>
                  )
                })}
              </ol>
              <a className="cp-back" href="/#trabalho">
                <ArrowIcon direction="left" /> Voltar aos cases
              </a>
            </nav>
          </aside>
          <article className="cp-article">
            {data.chapters.map((chapter, i) => (
              <section
                className="cp-chapter"
                id={caseChapters[i][0]}
                key={caseChapters[i][0]}
                aria-labelledby={`chapter-${i}`}
              >
                <div className="cp-chapter-label">
                  <span>{String(i + 1).padStart(2, "0")}</span>
                  <p>{caseChapters[i][1]}</p>
                </div>
                <h2 id={`chapter-${i}`}>{chapter.title}</h2>
                <div className="cp-chapter-content">{chapter.content}</div>
              </section>
            ))}

            {(data.prevCase || data.nextCase) && (
              <nav className="cp-case-nav" aria-label="Navegação entre cases">
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
                  <div className="cp-case-nav-placeholder" aria-hidden="true" />
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
                  <div className="cp-case-nav-placeholder" aria-hidden="true" />
                )}
              </nav>
            )}
          </article>
        </div>
      </main>
      <SiteFooter />
    </>
  )
}
