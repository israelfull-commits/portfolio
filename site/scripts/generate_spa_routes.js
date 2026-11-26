import fs from "node:fs"
import path from "node:path"

const SITE_BASE = "https://israelfull-commits.github.io/portfolio"

const routes = [
  {
    path: "cases/einstein-laudos",
    title: "Albert Einstein · Consumo de Resultados — Israel Rozar",
    description:
      "UX Lead no Einstein (2022): arquitetura modular para 80+ tipos de laudos em tela e impressão P&B. Nos testes, 81,6% reconheceram o laudo e 77,8% focaram nos dados.",
  },
  {
    path: "cases/claro-ativacao-simplificada",
    title: "Claro · Ativação simplificada — Israel Rozar",
    description:
      "UX/UI Designer na Claro Brasil (2017–2018): 22 jornadas comerciais unificadas em esteira desktop e mobile de 5 etapas, com 70 oportunidades e especificações V.2.",
  },
  {
    path: "cases/neoenergia-conexao-digital",
    title: "Neoenergia · Service Design — Israel Rozar",
    description:
      "Service Design no P&D ANEEL da Neoenergia (EY × Livework, 2020): 4 distribuidoras, 5 Service Blueprints e 118 ideias priorizadas como baseline estratégico.",
  },
  {
    path: "cases/itau/hub-liquidez",
    title: "Itaú · Hub de Liquidez e Oportunidades — Israel Rozar",
    description:
      "Senior Product Designer no Itaú íon for Advisors (2024–2026): hierarquia de saldo disponível, projeção temporal (dia, 7d, 30d) e fila de clientes no Hub de Liquidez.",
  },
  {
    path: "cases/itau/vencimentos",
    title: "Itaú · Gestão de Vencimentos — Israel Rozar",
    description:
      "Senior Product Designer no Itaú íon for Advisors (2024–2026): consulta unificada de vencimentos, eventos futuros e Open Finance com filtros combináveis e estados.",
  },
  {
    path: "cases/itau/movimentacoes",
    title: "Itaú · Movimentações — Israel Rozar",
    description:
      "Senior Product Designer no Itaú íon for Advisors (2024–2026): transição do Extrato EA para o IFA com saldo provisionado no cabeçalho e limites em Movimentações.",
  },
  {
    path: "cases/itau/campanhas",
    title: "Itaú · Gestão de Campanhas — Israel Rozar",
    description:
      "Senior Product Designer no Itaú íon for Advisors (2024–2026): fluxos de configuração, importação de base, estados de processamento e manutenção em lote.",
  },
  {
    path: "cases/itau/registros-atendimento",
    title: "Itaú · Registros de Atendimento — Israel Rozar",
    description:
      "Senior Product Designer no Itaú íon for Advisors (2024–2026): histórico dos 5 últimos resumos e minuta assistida por IA com revisão humana obrigatória.",
  },
]

function escapeAttr(str) {
  return str.replace(/&/g, "&amp;").replace(/"/g, "&quot;").replace(/</g, "&lt;").replace(/>/g, "&gt;")
}

function injectRouteMeta(html, route) {
  const url = `${SITE_BASE}/${route.path}/`
  const title = escapeAttr(route.title)
  const desc = escapeAttr(route.description)
  return html
    .replace(/<title>[\s\S]*?<\/title>/, `<title>${title}</title>`)
    .replace(/<meta name="description" content="[^"]*"\s*\/>/, `<meta name="description" content="${desc}" />`)
    .replace(/<meta property="og:title" content="[^"]*"\s*\/>/, `<meta property="og:title" content="${title}" />`)
    .replace(/<meta property="og:description" content="[^"]*"\s*\/>/, `<meta property="og:description" content="${desc}" />`)
    .replace(/<meta property="og:url" content="[^"]*"\s*\/>/, `<meta property="og:url" content="${url}" />`)
    .replace(/<meta name="twitter:title" content="[^"]*"\s*\/>/, `<meta name="twitter:title" content="${title}" />`)
    .replace(/<meta name="twitter:description" content="[^"]*"\s*\/>/, `<meta name="twitter:description" content="${desc}" />`)
    .replace(/<link rel="canonical" href="[^"]*"\s*\/>/, `<link rel="canonical" href="${url}" />`)
}

const distDir = path.resolve("dist")
const indexPath = path.join(distDir, "index.html")

if (fs.existsSync(indexPath)) {
  const indexHtml = fs.readFileSync(indexPath, "utf8")

  for (const route of routes) {
    const targetDir = path.join(distDir, route.path)
    fs.mkdirSync(targetDir, { recursive: true })
    fs.writeFileSync(path.join(targetDir, "index.html"), injectRouteMeta(indexHtml, route))
  }

  fs.writeFileSync(path.join(distDir, "404.html"), indexHtml)
  console.log(`Generated static index.html entrypoints for ${routes.length} SPA routes + 404.html`)
} else {
  console.error("dist/index.html not found!")
}
