import fs from "node:fs"
import path from "node:path"

const routes = [
  "cases/einstein-laudos",
  "cases/claro-ativacao-simplificada",
  "cases/neoenergia-conexao-digital",
  "cases/itau/hub-liquidez",
  "cases/itau/vencimentos",
  "cases/itau/movimentacoes",
  "cases/itau/campanhas",
]

const distDir = path.resolve("dist")
const indexPath = path.join(distDir, "index.html")

if (fs.existsSync(indexPath)) {
  const indexHtml = fs.readFileSync(indexPath, "utf8")

  for (const route of routes) {
    const targetDir = path.join(distDir, route)
    fs.mkdirSync(targetDir, { recursive: true })
    fs.writeFileSync(path.join(targetDir, "index.html"), indexHtml)
  }

  fs.writeFileSync(path.join(distDir, "404.html"), indexHtml)
  console.log(`Generated static index.html entrypoints for ${routes.length} SPA routes + 404.html`)
} else {
  console.error("dist/index.html not found!")
}

