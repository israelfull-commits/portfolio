# Extração de referência — Figma Make

- Make: `wu8RFWqSsQKt4SgrBqgGEf`
- Publicação correlacionada: `https://amity-cast-92973331.figma.site/`
- Data da extração: 2026-11-01 (America/Sao_Paulo)
- Destino isolado: `figma-make-reference/wu8RFWqSsQKt4SgrBqgGEf`
- A pasta `site/` não foi modificada.

## Resultado

Foi recuperado o grafo completo de código alcançável a partir de `src/main.tsx`, incluindo configuração Vite/Figma, rotas, páginas, componentes, design system e folha de estilos. Os sete arquivos públicos referenciados pelo código também foram recuperados. O projeto compila com sucesso usando Vite 8.3.5.

## Arquivos-fonte recuperados pelo recurso oficial `file://figma/make/source`

- `.figma/make/site.json`
- `index.html`
- `package.json`
- `public/favicon.svg`
- `src/main.tsx`
- `src/index.css`
- `src/app/App.tsx`
- `src/app/routes.tsx`
- `src/components/PageMeta.tsx`
- `src/components/SiteChrome.tsx`
- `src/design-system.tsx`
- `src/pages/Home.tsx`
- `src/pages/EinsteinCase.tsx`
- `src/pages/ItauPreparationCase.tsx`
- `src/pages/NotFound.tsx`
- `tsconfig.json`
- `vite.config.ts`

## Assets recuperados

Os recursos binários do Make são retornados pelo MCP em base64. Como respostas grandes são truncadas pelo cliente, os binários completos foram baixados das mesmas rotas públicas da publicação correlacionada e conferidos por tamanho, tipo e SHA-256.

| Asset | Bytes | SHA-256 |
|---|---:|---|
| `public/documents/israel-rozar-curriculo.pdf` | 58.669 | `c4fcc4dbc6b11ac770f2e699b662938223997ceca5980f5443c77b6819d3d639` |
| `public/favicon.svg` | 3.236 | `6c606f36cdb90a709f192b573dd3fe00e484549231303204fefc7a2ef40a3dff` |
| `public/images/hiae-laudo-original-recorte.webp` | 113.090 | `08559dd07329a15c0786a3f8f558c432bd829db9f25cfcd0fd0077239cbd5384` |
| `public/images/hiae-laudo-proposta-completa.webp` | 82.662 | `d5d9e6ced03f522b8079565f047e73e26c030bdc68e4190cc8e682d1fdfe2d72` |
| `public/images/israel-rozar-portrait-480.webp` | 37.714 | `15a4dc879e43f01c0168e036d47128740988257cf3885bfe64fd354223db538e` |
| `public/images/israel-rozar-portrait-800.webp` | 97.564 | `12374be5dd19717a293e8e75a2a88075f5726f916712405b6969c73c3a1f494d` |
| `public/images/israel-rozar-social.jpg` | 72.944 | `b1c8472cc6fefc86a482ed4be78e50e06298823cafdfe6c396539452df4b7556` |

## Mapeamento para o site publicado

| Rota publicada | Implementação |
|---|---|
| `/` | `src/pages/Home.tsx` |
| `/cases/einstein-laudos` | `src/pages/EinsteinCase.tsx` |
| `/cases/movimentacoes` | `src/pages/ItauPreparationCase.tsx`, dataset `movimentacoes` |
| `/cases/hub-liquidez` | `src/pages/ItauPreparationCase.tsx`, dataset `hub-liquidez` |
| `/cases/campanhas` | `src/pages/ItauPreparationCase.tsx`, dataset `campanhas` |
| demais rotas | `src/pages/NotFound.tsx` |
| shell, navegação e rodapé | `src/components/SiteChrome.tsx` |
| metadados por rota | `src/components/PageMeta.tsx` |
| tokens e componentes básicos | `src/design-system.tsx` + `src/index.css` |
| metadados base, JSON-LD e bootstrap | `index.html` |
| política de publicação Figma | `.figma/make/site.json` |

## Validação executada

- `npm install`: concluído, 47 pacotes instalados.
- `npm run build`: concluído, 30 módulos transformados.
- Saída principal: CSS 37,48 kB; JavaScript principal 313,22 kB; chunks separados para Home e cases.
- Todos os sete caminhos públicos referenciados retornaram HTTP 200 na publicação.
- O build reproduz `robots.txt` bloqueando indexação porque `.figma/make/site.json` contém `robots.index: false`.

## Lacunas e ressalvas

1. O servidor MCP não fornece um manifesto/diretório enumerável do Make; os arquivos foram descobertos pelo entrypoint, imports e referências públicas. O grafo executável está completo, mas não é possível provar a ausência de arquivos órfãos e não importados.
2. O MCP limita respostas binárias grandes; por isso seis binários foram recuperados integralmente pela publicação correlacionada, nos caminhos declarados pelo próprio código. O SVG foi obtido diretamente pelo recurso MCP.
3. `package-lock.json`, `node_modules/` e `dist/` são artefatos gerados localmente para validação, não fontes originais do Make.
4. O build emite dois avisos prospectivos do Vite sobre `__dirname` e importação JSON sem `with { type: 'json' }`; não impedem a compilação atual.
5. A configuração atual duplica parte dos metadados entre `index.html` e o plugin de site e mantém `noindex`; são achados a corrigir na implementação derivada, não nesta cópia de referência.

