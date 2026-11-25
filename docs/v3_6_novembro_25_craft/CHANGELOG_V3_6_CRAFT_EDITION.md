# Changelog Detalhado — Versão V3.6 (Craft Edition & Documentação Figma)

**Data:** 25 de Novembro de 2026  
**Conversa de Origem:** `b9eff66e-96f2-48ed-af7d-28e8cea0dfad`  
**Base Anterior:** Versão V3.5 (`e8fecf8`)

---

## 1. Melhorias de Craft Visual & Experiência de Interface

Implementados os 4 refinamentos funcionais de alto impacto (evitando intencionalmente *Scroll Reveal* que oculta conteúdo na triagem rápida de recrutadores):

1. **Barra de Progresso de Leitura nos Cases (`Site / CasePresentation.tsx` & `case-presentation.css`):**
   * Linha fixa de `3px` no topo da viewport (`.cp-reading-progress`) em gradiente `var(--cp-pine)` ➔ `#1b6b45` ➔ `var(--cp-lime)`.
   * Atualizada de forma passiva via `requestAnimationFrame`, sem impacto em performance ou layout shift.
2. **Microinterações Táteis nos Cards e CTAs (`portfolio.css`):**
   * Elevação física suave nos cards da Home (`translateY(-4px)` + sombra multi-camada difusa em tom pine).
   * Zoom sutil (`scale(1.015)`) no preview do tablet do Einstein ao passar o mouse no card destaque.
   * Micro-deslocamento da seta (`translateX(3px)`) nos botões e CTAs.
   * Realce suave nos links de submódulos do Itaú.
3. **Header Inteligente com Profundidade no Scroll (`SiteChrome.tsx` & `index.css`):**
   * Classe dinâmica `.is-scrolled` ativada acima de `12px` de scroll, aplicando `backdrop-filter: blur(12px)` e sombra difusa sutil.
4. **Lightbox com Zoom Direto na Imagem (`CasePresentation.tsx` & `case-presentation.css`):**
   * Clique direto na imagem ampliada alterna entre *Ajustar à tela* e *Tamanho original 1:1* com cursor contextual (`zoom-in` / `zoom-out`) e animação suave de entrada (`180ms cubic-bezier`).
5. **Proteção Vestibular Integral:**
   * 100% das novas transições e animações respeitam `@media (prefers-reduced-motion: reduce)`.

---

## 2. Sincronização de Design & Documentação no Figma Desktop

* **Gerador Atualizado ([build_portfolio_figma_screens.py](../../scripts/build_portfolio_figma_screens.py)):**
  * Adicionada a prancha canônica **`buildDesignSystemDocsFrame`** (`create_ds_docs`) contendo: Paleta Semântica & Matriz WCAG 2.2 AAA, Tipografia & Grid 8px, Especificação de Microinterações V3.6 e Histórico Completo de Versões (V1 ➔ V3.6).
  * Integrada tanto no botão dedicado da UI do plugin quanto na geração completa (`create_all_screens`).
  * Bundle `code.js` e `ui.html` recompilados e sincronizados em `figma-refine-plugin` e `gemini-figma-plugin` (sintaxe ES5/ES6 clássica compatível com Figma Desktop no Windows).


---

## 3. Atualização Incremental (V3.6.1)
* **Home (`Home.tsx` & `portfolio.css`):** Links da barra *"Outros recortes no Itaú (IFA)"* (`Gestão de Vencimentos`, `Movimentações`, `Gestão de Campanhas`) desativados e convertidos em tags informativas estáticas (`.pf-home-submodules-item`, `<div>` semântico), preservando os `href` no array `itauSubmodules` para reativação rápida quando desejado.
* **Hero (`Home.tsx`):** Removido o link de e-mail em texto aberto abaixo dos botões do Hero para proteger contra scrapers/bots de spam e manter a dobra inicial limpa com `Ver projetos` + `Currículo (PDF)`.
* **Contato Anti-Spam (`SiteChrome.tsx`):** Padronizado o CTA do rodapé da Home e dos Cases para `Enviar um e-mail` com montagem dinâmica do `mailto:` apenas no evento de clique (`openProtectedEmail`), eliminando 100% de endereços de e-mail em texto aberto no HTML/bundle contra robôs de scraping.
* **Auditoria Integral de Imagens & 100% WebP (`ItauPreparationCase.tsx`):** Auditadas todas as 42 declarações de imagens do portfólio (0 distorções de proporção, 0 imagens quebradas). Convertidos os últimos 4 `.png` legados do Itaú (`itau-vencimentos-canonico`, `itau-vencimentos-eventos`, `itau-vencimentos-empty`, `itau-hub-liquidez-solucao`) para WebP de alta fidelidade (`q=92`, economia de 28% mantendo nitidez 1:1 de tipografia UI).
