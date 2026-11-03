# Portfólio Israel Rozar — réplica fiel do Figma Make

Projeto React/Vite reconstruído a partir do código-fonte e dos assets do Figma Make `wu8RFWqSsQKt4SgrBqgGEf`. A identidade visual e o comportamento responsivo foram preservados; a versão pública foi refinada para concentrar evidências verificáveis e reduzir riscos de confidencialidade, autoria e métricas sem fonte.

## Executar

```powershell
npm install
npm run dev -- --host 0.0.0.0 --port 4173 --strictPort
```

Abra `http://localhost:4173`.

## Validar

```powershell
npm run build
```

O relatório de comparação visual e funcional está em `design-qa.md`.

## Correções aplicadas sem redesign

- Metadados únicos, canonical, Open Graph, Twitter Card e JSON-LD.
- Indexação habilitada no HTML, em `.figma/make/site.json` e em `robots.txt`.
- Menu móvel com `button`, `aria-expanded`, `aria-controls`, foco inicial, fechamento por link, clique externo e `Escape`.
- Assets visuais, currículo e favicon armazenados localmente.
- Remoção da injeção duplicada de metadados do shell Figma.

Antes de publicar em outro domínio, atualize canonical, sitemap, `og:url`, JSON-LD e URLs absolutas das imagens sociais.
