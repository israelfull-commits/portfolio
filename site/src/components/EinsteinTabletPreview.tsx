import { useState, useEffect, useRef } from "react"
import { ArrowIcon, Link } from "../design-system"

interface ProgressiveStep {
  step: number
  label: string
  pill: string
  description: string
  visibleCount: number
}

const STEPS: ProgressiveStep[] = [
  {
    step: 0,
    label: "01 Metodologia",
    pill: "Passo 1 de 3 · Metodologia do Exame",
    description:
      "Apresentação da primeira macroárea: definição de técnica de aquisição de imagens e contextualização clínica.",
    visibleCount: 1,
  },
  {
    step: 1,
    label: "02 + Resultados",
    pill: "Passo 2 de 3 · Tabela Estruturada",
    description:
      "Acoplamento da segunda macroárea: dados quantitativos, unidades de medida e intervalos de referência alinhados.",
    visibleCount: 2,
  },
  {
    step: 2,
    label: "03 + Conclusão",
    pill: "Passo 3 de 3 · Conclusão & QR Code",
    description:
      "Acoplamento da terceira macroárea: síntese diagnóstica executiva, assinatura médica e validação criptográfica.",
    visibleCount: 3,
  },
  {
    step: 3,
    label: "Laudo Completo",
    pill: "Laudo Unificado · 3 Macroáreas Ativas",
    description:
      "Todas as macroáreas consolidadas: arquitetura unificada de informação que padronizou mais de 80 exames distintos.",
    visibleCount: 3,
  },
]

export function EinsteinTabletPreview() {
  const [activeStep, setActiveStep] = useState(0)
  const [isPaused, setIsPaused] = useState(false)
  const timerRef = useRef<number | null>(null)

  useEffect(() => {
    if (isPaused) return
    const interval = window.setInterval(() => {
      setActiveStep((prev) => (prev + 1) % STEPS.length)
    }, 3800)
    timerRef.current = interval
    return () => window.clearInterval(interval)
  }, [isPaused])

  const current = STEPS[activeStep]
  const isAllVisible = activeStep === 3

  return (
    <div
      className="pf-tablet-showcase"
      onMouseEnter={() => setIsPaused(true)}
      onMouseLeave={() => setIsPaused(false)}
      role="region"
      aria-label="Demonstração sequencial da anatomia progressiva do laudo clínico em tablet"
    >
      {/* Tablet Device Frame (Static Container) */}
      <Link
        href="/cases/einstein-laudos"
        className={`pf-tablet-device ${isAllVisible ? "is-complete" : ""}`}
        ariaLabel="Explorar estudo de caso completo do Hospital Albert Einstein"
      >
        {/* Tablet Bezel & Camera */}
        <div className="pf-tablet-bezel">
          <span className="pf-tablet-camera" aria-hidden="true" />

          {/* Inner Screen Surface */}
          <div className="pf-tablet-screen">
            {/* Clinical Report Header Bar */}
            <header className="pf-screen-header">
              <div className="pf-screen-brand">
                <span className="pf-brand-badge">HIAE</span>
                <div>
                  <strong>HOSPITAL ISRAELITA ALBERT EINSTEIN</strong>
                  <span>Consumo de Resultados Clínicos · Medicina Diagnóstica</span>
                </div>
              </div>
              <div className="pf-screen-meta">
                <span className="pf-qr-placeholder">QR</span>
                <span>Protocolo #2022-8419</span>
              </div>
            </header>

            {/* Exam Title */}
            <div className="pf-exam-title">
              <h2>Ressonância Magnética Cardiovascular</h2>
              <span className="pf-exam-tag">Protocolo Padrão de Miocardiopatia</span>
            </div>

            {/* Area de Conteudo Estatica: todas as secoes tem espaco reservado */}
            <div className="pf-screen-canvas">
              {/* Macroárea 1: Metodologia e Indicação (visível a partir do passo 0) */}
              <section
                className={`pf-macro-block pf-macro-1 ${
                  activeStep === 0
                    ? "is-focus"
                    : isAllVisible
                    ? "is-unified"
                    : "is-preserved"
                }`}
              >
                <div className="pf-macro-badge">
                  <span>01</span> Metodologia &amp; Indicação
                </div>
                <div className="pf-macro-body">
                  <p>
                    <strong>Técnica:</strong> Cortes volumétricos ponderados em T1 e T2 com sequências cine-SSFP e mapeamento de realce tardio miocárdico.
                  </p>
                  <p>
                    <strong>Indicação:</strong> Avaliação anatômica e funcional de volumes biventriculares e viabilidade tecidual.
                  </p>
                </div>
              </section>

              {/* Macroárea 2: Tabela Modular de Resultados (revelada a partir do passo 1) */}
              {current.visibleCount >= 2 ? (
                <section
                  className={`pf-macro-block pf-macro-2 pf-slide-reveal ${
                    activeStep === 1
                      ? "is-focus"
                      : isAllVisible
                      ? "is-unified"
                      : "is-preserved"
                  }`}
                >
                  <div className="pf-macro-badge">
                    <span>02</span> Resultado Estruturado
                  </div>
                  <div className="pf-results-table">
                    <div className="pf-table-head">
                      <span>Parâmetro Analisado</span>
                      <span>Valor</span>
                      <span>Referência</span>
                      <span>Status</span>
                    </div>
                    <div className="pf-table-row">
                      <span className="pf-col-param">Diâmetro Diastólico VE</span>
                      <span className="pf-col-val">48 mm</span>
                      <span className="pf-col-ref">37 a 55 mm</span>
                      <span className="pf-col-status status-normal">Normal</span>
                    </div>
                    <div className="pf-table-row">
                      <span className="pf-col-param">Espessura Septo Interventricular</span>
                      <span className="pf-col-val">9 mm</span>
                      <span className="pf-col-ref">6 a 10 mm</span>
                      <span className="pf-col-status status-normal">Normal</span>
                    </div>
                    <div className="pf-table-row">
                      <span className="pf-col-param">Fração de Ejeção Estimada (VE)</span>
                      <span className="pf-col-val">64 %</span>
                      <span className="pf-col-ref">≥ 55 %</span>
                      <span className="pf-col-status status-preservada">Preservada</span>
                    </div>
                  </div>
                </section>
              ) : (
                <div className="pf-macro-skeleton pf-skeleton-2" aria-hidden="true">
                  <div className="pf-skeleton-header">
                    <span className="pf-skeleton-pill">02</span>
                    <span>Espaço reservado · Macroárea 02 (Tabela Estruturada)</span>
                  </div>
                  <div className="pf-skeleton-lines">
                    <div className="pf-sk-line sk-w80" />
                    <div className="pf-sk-line sk-w60" />
                  </div>
                </div>
              )}

              {/* Macroárea 3: Conclusão Diagnóstica (revelada a partir do passo 2) */}
              {current.visibleCount >= 3 ? (
                <section
                  className={`pf-macro-block pf-macro-3 pf-slide-reveal ${
                    activeStep === 2
                      ? "is-focus"
                      : isAllVisible
                      ? "is-unified"
                      : "is-preserved"
                  }`}
                >
                  <div className="pf-macro-badge">
                    <span>03</span> Conclusão &amp; Assinatura
                  </div>
                  <div className="pf-macro-body pf-conclusion-body">
                    <p>
                      <strong>Conclusão Diagnóstica:</strong> Dimensões cavitárias e função sistólica biventricular preservadas. Ausência de áreas focais de fibrose ou realce tardio patológico.
                    </p>
                    <div className="pf-doc-signature">
                      <span>Dr. M. S. Albuquerque · CRM-SP 148.902</span>
                      <span className="pf-auth-pill">Autenticação Criptográfica Ativa</span>
                    </div>
                  </div>
                </section>
              ) : (
                <div className="pf-macro-skeleton pf-skeleton-3" aria-hidden="true">
                  <div className="pf-skeleton-header">
                    <span className="pf-skeleton-pill">03</span>
                    <span>Espaço reservado · Macroárea 03 (Conclusão &amp; Assinatura)</span>
                  </div>
                  <div className="pf-skeleton-lines">
                    <div className="pf-sk-line sk-w90" />
                  </div>
                </div>
              )}
            </div>
          </div>
        </div>

        {/* Floating Active Pill Badge */}
        <div className={`pf-spotlight-pill ${isAllVisible ? "pill-complete" : ""}`}>
          <span className="pf-pill-dot" />
          <span>{current.pill}</span>
          <ArrowIcon />
        </div>
      </Link>

      {/* Stepper Navigation: 4 Steps */}
      <div className="pf-tablet-stepper">
        {STEPS.map((s, idx) => (
          <button
            key={s.step}
            type="button"
            className={`pf-step-btn ${activeStep === idx ? "is-current" : ""}`}
            onClick={() => setActiveStep(idx)}
            aria-pressed={activeStep === idx}
          >
            <span className="pf-step-num">
              {idx === 3 ? "✓" : `0${idx + 1}`}
            </span>
            <span className="pf-step-name">{s.label}</span>
            {activeStep === idx && !isPaused && <span className="pf-step-progress" />}
          </button>
        ))}
      </div>

      {/* Dynamic Subtitle explaining current assembly stage */}
      <figcaption className="pf-tablet-caption">
        <strong>{current.label}:</strong> {current.description}
      </figcaption>
    </div>
  )
}
