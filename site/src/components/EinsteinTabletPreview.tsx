import { useState, useEffect, useRef } from "react"
import { ArrowIcon, Link } from "../design-system"

interface MacroArea {
  id: number
  label: string
  pill: string
  description: string
}

const MACRO_AREAS: MacroArea[] = [
  {
    id: 1,
    label: "Metodologia",
    pill: "01 · Metodologia do Exame",
    description: "Técnica empregada, parâmetros de aquisição e indicação clínica estruturados para leitura médica ágil.",
  },
  {
    id: 2,
    label: "Resultado",
    pill: "02 · Tabela Estruturada de Resultados",
    description: "Alinhamento visual estrito entre valor, unidade de medida, intervalo de referência e status diagnóstico.",
  },
  {
    id: 3,
    label: "Conclusão",
    pill: "03 · Conclusão & Autenticação",
    description: "Síntese diagnóstica executiva sem jargões desnecessários, com assinatura médica e token QR code.",
  },
]

export function EinsteinTabletPreview() {
  const [activeStep, setActiveStep] = useState(0)
  const [isPaused, setIsPaused] = useState(false)
  const timerRef = useRef<number | null>(null)

  useEffect(() => {
    if (isPaused) return
    const interval = window.setInterval(() => {
      setActiveStep((prev) => (prev + 1) % MACRO_AREAS.length)
    }, 3800)
    timerRef.current = interval
    return () => window.clearInterval(interval)
  }, [isPaused])

  const current = MACRO_AREAS[activeStep]

  return (
    <div
      className="pf-tablet-showcase"
      onMouseEnter={() => setIsPaused(true)}
      onMouseLeave={() => setIsPaused(false)}
      role="region"
      aria-label="Demonstração interativa da anatomia do laudo clínico em tablet"
    >
      {/* Tablet Device Frame */}
      <Link
        href="/cases/einstein-laudos"
        className="pf-tablet-device"
        ariaLabel="Explorar estudo de caso completo do Hospital Albert Einstein"
      >
        {/* Tablet Bezel & Sensors */}
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
                <span>Laudo #2022-8419</span>
              </div>
            </header>

            {/* Exam Title */}
            <div className="pf-exam-title">
              <h2>Ressonância Magnética Cardiovascular</h2>
              <span className="pf-exam-tag">Protocolo Padrão de Miocardiopatia</span>
            </div>

            {/* Macro-area 1: Metodologia e Indicação */}
            <section
              className={`pf-macro-block pf-macro-1 ${activeStep === 0 ? "is-active" : "is-dimmed"}`}
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

            {/* Macro-area 2: Tabela Modular de Resultados */}
            <section
              className={`pf-macro-block pf-macro-2 ${activeStep === 1 ? "is-active" : "is-dimmed"}`}
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

            {/* Macro-area 3: Conclusão Diagnóstica */}
            <section
              className={`pf-macro-block pf-macro-3 ${activeStep === 2 ? "is-active" : "is-dimmed"}`}
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
          </div>
        </div>

        {/* Floating Active Pill Badge */}
        <div className="pf-spotlight-pill">
          <span className="pf-pill-dot" />
          <span>{current.pill}</span>
          <ArrowIcon />
        </div>
      </Link>

      {/* Step Indicators & Interactive Tabs */}
      <div className="pf-tablet-stepper">
        {MACRO_AREAS.map((area, idx) => (
          <button
            key={area.id}
            type="button"
            className={`pf-step-btn ${activeStep === idx ? "is-current" : ""}`}
            onClick={() => setActiveStep(idx)}
            aria-pressed={activeStep === idx}
          >
            <span className="pf-step-num">0{area.id}</span>
            <span className="pf-step-name">{area.label}</span>
            {activeStep === idx && !isPaused && <span className="pf-step-progress" />}
          </button>
        ))}
      </div>

      {/* Dynamic Subtitle explaining the highlighted area */}
      <figcaption className="pf-tablet-caption">
        <strong>{current.label}:</strong> {current.description}
      </figcaption>
    </div>
  )
}
