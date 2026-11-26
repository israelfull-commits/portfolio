import { useEffect, useState, type FormEvent, type ReactNode } from "react"
import { ArrowIcon, Link, MailIcon } from "../design-system"
import { SiteHeader } from "./SiteChrome"
import "./case-presentation.css"

const EXPECTED_HASH =
  "acf75c0284697d295e0c00fac86fb34b111ad26cb58e3871424d2a1294a89cb8"
const SESSION_KEY = "pf_case_access_v1"

async function sha256Hex(input: string): Promise<string> {
  const bytes = new TextEncoder().encode(input)
  if (typeof crypto !== "undefined" && crypto.subtle) {
    const digest = await crypto.subtle.digest("SHA-256", bytes)
    return Array.from(new Uint8Array(digest))
      .map((b) => b.toString(16).padStart(2, "0"))
      .join("")
  }
  // Pure JS SHA-256 fallback for non-secure HTTP contexts
  const K = [
    0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1,
    0x923f82a4, 0xab1c5ed5, 0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3,
    0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174, 0xe49b69c1, 0xefbe4786,
    0x0fc19dc6, 0x240ca1cc, 0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
    0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7, 0xc6e00bf3, 0xd5a79147,
    0x06ca6351, 0x14292967, 0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13,
    0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85, 0xa2bfe8a1, 0xa81a664b,
    0xc24b8b70, 0xc76c51a3, 0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
    0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a,
    0x5b9cca4f, 0x682e6ff3, 0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208,
    0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2,
  ]
  const H = [
    0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a, 0x510e527f, 0x9b05688c,
    0x1f83d9ab, 0x5be0cd19,
  ]
  const bitLen = bytes.length * 8
  const paddedLen = Math.ceil((bytes.length + 9) / 64) * 64
  const padded = new Uint8Array(paddedLen)
  padded.set(bytes)
  padded[bytes.length] = 0x80
  const view = new DataView(padded.buffer)
  view.setUint32(paddedLen - 4, bitLen >>> 0, false)
  view.setUint32(paddedLen - 8, Math.floor(bitLen / 0x100000000), false)
  const w = new Uint32Array(64)
  const rotr = (x: number, n: number) => (x >>> n) | (x << (32 - n))
  for (let i = 0; i < paddedLen; i += 64) {
    for (let j = 0; j < 16; j++) w[j] = view.getUint32(i + j * 4, false)
    for (let j = 16; j < 64; j++) {
      const s0 = rotr(w[j - 15], 7) ^ rotr(w[j - 15], 18) ^ (w[j - 15] >>> 3)
      const s1 = rotr(w[j - 2], 17) ^ rotr(w[j - 2], 19) ^ (w[j - 2] >>> 10)
      w[j] = (w[j - 16] + s0 + w[j - 7] + s1) >>> 0
    }
    let [a, b, c, d, e, f, g, h] = H
    for (let j = 0; j < 64; j++) {
      const S1 = rotr(e, 6) ^ rotr(e, 11) ^ rotr(e, 25)
      const ch = (e & f) ^ (~e & g)
      const t1 = (h + S1 + ch + K[j] + w[j]) >>> 0
      const S0 = rotr(a, 2) ^ rotr(a, 13) ^ rotr(a, 22)
      const maj = (a & b) ^ (a & c) ^ (b & c)
      const t2 = (S0 + maj) >>> 0
      h = g
      g = f
      f = e
      e = (d + t1) >>> 0
      d = c
      c = b
      b = a
      a = (t1 + t2) >>> 0
    }
    H[0] = (H[0] + a) >>> 0
    H[1] = (H[1] + b) >>> 0
    H[2] = (H[2] + c) >>> 0
    H[3] = (H[3] + d) >>> 0
    H[4] = (H[4] + e) >>> 0
    H[5] = (H[5] + f) >>> 0
    H[6] = (H[6] + g) >>> 0
    H[7] = (H[7] + h) >>> 0
  }
  return H.map((x) => x.toString(16).padStart(8, "0")).join("")
}

function requestAccessEmail() {
  const user = ["i", "r", "o", "z", "a", "r"].join("")
  const domain = ["y", "a", "h", "o", "o", ".", "c", "o", "m", ".", "b", "r"].join("")
  const subject = encodeURIComponent("Solicitação de acesso aos estudos de caso · Portfólio")
  window.location.href = `mailto:${user}@${domain}?subject=${subject}`
}

export function CaseAccessGate({
  caseName,
  children,
}: {
  caseName: string
  children: ReactNode
}) {
  const [unlocked, setUnlocked] = useState<boolean>(() => {
    try {
      return sessionStorage.getItem(SESSION_KEY) === EXPECTED_HASH
    } catch {
      return false
    }
  })
  const [password, setPassword] = useState("")
  const [showPassword, setShowPassword] = useState(false)
  const [error, setError] = useState("")
  const [submitting, setSubmitting] = useState(false)

  useEffect(() => {
    if (unlocked) return
    const prevTitle = document.title
    document.title = `Acesso protegido · ${caseName} — Israel Rozar`
    return () => {
      document.title = prevTitle
    }
  }, [unlocked, caseName])

  if (unlocked) {
    return <>{children}</>
  }

  async function handleSubmit(event: FormEvent) {
    event.preventDefault()
    setError("")
    const normalized = password.trim().toLowerCase()
    if (!normalized) {
      setError("Informe a senha de acesso para continuar.")
      return
    }
    setSubmitting(true)
    try {
      const digest = await sha256Hex(normalized)
      if (digest === EXPECTED_HASH) {
        try {
          sessionStorage.setItem(SESSION_KEY, EXPECTED_HASH)
        } catch {
          // Ignore storage restrictions in private browsing
        }
        setUnlocked(true)
      } else {
        setError("Senha incorreta. Verifique o código informado ou solicite acesso por e-mail.")
      }
    } finally {
      setSubmitting(false)
    }
  }

  return (
    <div className="pf-page">
      <SiteHeader casePage />
      <main className="cp-gate-main" id="conteudo">
        <section className="cp-gate-card" aria-labelledby="gate-title">
          <div className="cp-gate-badge">
            <span className="cp-gate-lock" aria-hidden="true">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.2" strokeLinecap="round" strokeLinejoin="round">
                <rect x="3" y="11" width="18" height="11" rx="2" ry="2" />
                <path d="M7 11V7a5 5 0 0 1 10 0v4" />
              </svg>
            </span>
            Acesso protegido · Estudos de caso
          </div>

          <h1 id="gate-title" className="cp-gate-title">
            {caseName}
          </h1>

          <p className="cp-gate-lead">
            Este estudo de caso reúne decisões de arquitetura, fluxos e artefatos de projetos sob confidencialidade (NDA) em domínios regulados. Digite a senha fornecida para liberar a leitura de todos os cases nesta sessão.
          </p>

          <form className="cp-gate-form" onSubmit={handleSubmit} noValidate>
            <label htmlFor="case-access-password" className="cp-gate-label">
              Senha de acesso
            </label>
            <div className="cp-gate-input-wrap">
              <input
                id="case-access-password"
                type={showPassword ? "text" : "password"}
                className="cp-gate-input"
                value={password}
                onChange={(e) => {
                  setPassword(e.target.value)
                  if (error) setError("")
                }}
                autoComplete="current-password"
                placeholder="Digite a senha"
                aria-invalid={error ? "true" : "false"}
                aria-describedby={error ? "case-access-error" : undefined}
                autoFocus
              />
              <button
                type="button"
                className="cp-gate-toggle"
                onClick={() => setShowPassword((prev) => !prev)}
                aria-pressed={showPassword}
              >
                {showPassword ? "Ocultar" : "Mostrar"}
              </button>
            </div>

            {error ? (
              <p id="case-access-error" className="cp-gate-error" role="alert">
                {error}
              </p>
            ) : null}

            <button
              type="submit"
              className="pf-button pf-button-primary cp-gate-submit"
              disabled={submitting}
            >
              {submitting ? "Verificando…" : "Acessar estudo de caso"} <ArrowIcon />
            </button>
          </form>

          <div className="cp-gate-footer">
            <button
              type="button"
              className="cp-gate-request"
              onClick={requestAccessEmail}
            >
              <MailIcon /> Solicitar senha por e-mail
            </button>
            <Link className="cp-gate-back" href="/#trabalho">
              ← Voltar para a visão geral
            </Link>
          </div>
        </section>
      </main>
    </div>
  )
}

