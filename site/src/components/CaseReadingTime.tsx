/** Estimated from rendered case chapters at 200 words/minute, reviewed 25/11/2026. */
export const caseReadingMinutes: Record<string, number> = {
  "/cases/einstein-laudos": 8,
  "/cases/itau/hub-liquidez": 4,
  "/cases/claro-ativacao-simplificada": 6,
  "/cases/neoenergia-conexao-digital": 7,
  "/cases/itau/movimentacoes": 4,
  "/cases/itau/campanhas": 5,
  "/cases/itau/registros-atendimento": 4,
}

export function CaseReadingTime({ href }: { href: string }) {
  const minutes = caseReadingMinutes[href]
  if (!minutes) return null
  return (
    <span className="case-reading-time" aria-label={`Leitura estimada: ${minutes} minutos`}>
      <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round" aria-hidden="true" focusable="false">
        <circle cx="12" cy="12" r="9" />
        <path d="M12 7v5l3 2" />
      </svg>
      <span>{minutes} min de leitura</span>
    </span>
  )
}
