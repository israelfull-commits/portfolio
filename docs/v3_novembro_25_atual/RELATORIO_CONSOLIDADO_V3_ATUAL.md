# Relatório Técnico Consolidado — Versão 3 (Vigente em Produção)

**Data de Validação:** 25 de Novembro de 2026  
**Status do Deploy:** Ativo no GitHub Pages  
**URL de Produção:** [https://israelfull-commits.github.io/portfolio/](https://israelfull-commits.github.io/portfolio/)

---

## 1. Escopo das Entregas e Decisões da Versão 3

A Versão 3 representa o fechamento de ciclo do portfólio de Israel Rozar, consolidando a experiência completa para recrutadores e lideranças executivas de Product Design:

### A. Qualidade Visual e Craft de Estúdio
* **Albert Einstein:** Capa master de estúdio em **2560 × 1440 px (16:9)** (`hiae-capa-editorial-1600.webp`), eliminando definitivamente o antigo arquivo com linhas de redline e bounding boxes do Figma.
* **Claro:** Calibração exata de dimensões para 1600 × 900 px e atualização da imagem de ativação para alta resolução (1440 px).
* **Neoenergia & Itaú:** Padronização completa dos Heros em 16:9 de estúdio com sombras difusas e moldura de contenção.

### B. Mecanismo de Lightbox e Zoom Acessível
* **Geometria Expandida:** O modal agora preenche confortavelmente até `min(96vw, 96rem)` de largura e `min(94vh, 60rem)` de altura.
* **Resolução do Bug de Overflow:** Substituição de `place-items: center` no CSS Grid por centralização em bloco com margem automática (`display: block; margin: 0 auto;`). Isso permite rolagem horizontal suave até a margem esquerda no modo *tamanho original*, sem cortes.
* **39 Lightboxes Auditados:** 100% dos modais abrem, escalam e fecham com suporte à tecla `Escape`, botão Fechar ou clique no backdrop escuro.

### C. Acessibilidade Digital (100% WCAG AAA)
* **216 pares de cores auditados** em todas as páginas através do script automatizado `scripts/test_color_accessibility.py`.
* Taxa de aprovação WCAG AA: **100% (216/216)**.
* Taxa de aprovação WCAG AAA: **100% (216/216)**.
* Contraste do texto principal: **14.8:1** (mais que o dobro do mínimo de 7.0:1 do nível AAA).
* Contraste nos cards invertidos escuros: **11.85:1**.
* Contraste nos badges Acid Lime (`#CEFF1A` sobre `#0A3622`): **11.2:1**.
* **Zero imagens sem `alt`** e **Zero botões abaixo do tamanho mínimo de toque de 24 × 24 px**.

### D. Governança Editorial, Confidencialidade e Zero Redundância
* **Remoção de Links Confidenciais:** Links para arquivos de trabalho no Notion e no Figma do projeto Albert Einstein foram removidos em conformidade estrita com o NDA hospitalar e o sigilo médico.
* **Remoção de Canais Redundantes:** Links de "GitHub" e "UXfolio" foram completamente eliminados dos cards de contato, mantendo uma linha de ação limpa e relevante para recrutadores de Product Design: $\text{Baixar currículo (PDF)} \bullet \text{LinkedIn}$.
* **Diferenciação de Legendas:** Corrigida a duplicação textual no case de Campanhas do Itaú.
* **Enquadramento Regulatório:** Todos os protótipos de alta complexidade são categorizados sob a ótica afirmativa de dados sintetizados para conformidade com a LGPD e sigilos setoriais.

### E. Infraestrutura de Deploy Contínuo (CI/CD)
* **Workflow Desacoplado:** `.github/workflows/deploy.yml` dividido em dois jobs (`build` ➔ `deploy` com dependência explícita `needs: build`), garantindo que o upload do artefato seja concluído antes da chamada da API de deploy do GitHub Pages.
* **Geração Estática de Rotas SPA:** 7 diretórios de rotas com `index.html` estáticos e `404.html` gerados no pós-build para garantir resposta com **HTTP 200 OK** em qualquer navegação direta ou atualização de página.

