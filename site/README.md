# Portfólio de Israel Rozar

Implementação React 19 + Vite da home aprovada no Figma (`370:16614`), com adaptação móvel baseada em `375:366`. Estudos de caso existentes foram preservados e conectados à home.

## Executar e validar

```powershell
npm ci
npm run dev -- --port 8443
node node_modules/typescript/bin/tsc --noEmit
npm run build
npm run preview -- --port 8443
```

## Conteúdo e manutenção

- Home, projetos, posicionamento, trajetória e contato: `src/pages/Home.tsx`.
- Layout responsivo da home: `src/portfolio.css`.
- Tokens compartilhados e cabeçalho: bloco final de `src/index.css`.
- Menu acessível: `src/components/SiteChrome.tsx`.
- Estudos de caso: `src/pages/CasePages.tsx` e `src/components/CasePresentation.tsx`.
- Currículo: `public/documents/israel-rozar-curriculo.pdf`.
- Retrato tratado: `public/images/israel-rozar-treated-800.webp`, variante480 para telas menores. Original mantido.
- Plus Jakarta Sans400/600/700 hospedada localmente, licença OFL em `public/fonts/OFL.txt`.
- Identidade da hospedagem: `.openai/hosting.json`. Reutilizar o project_id nas atualizações.

Paleta: canvas#FCF9F2, subtle#F6F3EC, texto#1A201C/#4A554E, pine#0A3622, lime#CEFF1A, borda#EDE9DE. Container1152px; margens desktop64px, tablet32px e mobile24px. Seções64px/48px; grids24px; cards16px; destaque/contato24px. Não introduzir modo escuro automático.

A home inclui um case de destaque e quatro projetos do Itaú. Registros de Atendimento é apresentado como recorte, com limites documentados no estudo. As amostras de pesquisa do Einstein não devem ser somadas nem transformadas em resultados de negócio.

Não há formulário nem coleta de dados. Contato abre o cliente de e-mail; LinkedIn e UXfolio apontam aos perfis fornecidos no projeto. Ao mudar o domínio, atualizar URLs absolutas de index.html, robots.txt e sitemap.xml. PageMeta usa o domínio atual para os metadados das rotas.

## Verificação e Registro de Mudanças

- Consulte `CHANGELOG.md` e `docs/LOG-AUDITORIAS-E-EVOLUCOES.md` para o histórico completo e rastreável de todas as auditorias, correções e evoluções aplicadas.
- Execute `python scripts/update_changelog.py` para registrar novas alterações automaticamente no histórico.
- Consulte `design-qa.md` para evidências e desvios intencionais. Capturas locais ficam em `qa/` e não são publicadas. Os assets distribuídos ficam em `public/`; build em `dist/`.
