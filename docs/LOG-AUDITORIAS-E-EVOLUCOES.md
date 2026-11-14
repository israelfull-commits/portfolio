# Registro Contínuo de Auditorias, Correções e Evoluções do Portfólio

Este documento centraliza todas as auditorias formais, correções de código, evoluções de arquitetura de informação e atualizações visuais aplicadas no portfólio de Israel Rozar. Ele complementa o [CHANGELOG.md](../CHANGELOG.md) detalhando ferramentas, métodos, artefatos gerados e critérios de aprovação.

---

## Índice de Auditorias e Marcos

| Data | Tipo de Auditoria / Evolução | Escopo Principal | Critério de Aceite / Status | Artefato de Auditoria Gerado |
|---|---|---|---|---|
| **2026-11-14** | Auditoria Visual & Editorial Figma Nó 59:2 | Case Einstein: Consumo de Resultados | 100% Paridade nos 7 capítulos, pontuação e limites de amostra | [RELATORIO-INSPECAO-VISUAL-FIGMA-NODE-59-2-2026-11-03.md](file:///C:/Users/Israel%20Rozar/.gemini/antigravity/brain/ec9956e5-078d-4d87-9a8e-74481434c7dc/RELATORIO-INSPECAO-VISUAL-FIGMA-NODE-59-2-2026-11-03.md) |
| **2026-11-14** | Auditoria Geral de Alterações & Working Tree | Varredura profunda do repositório | 0 erros de build, rotas 200 OK | [VARREDURA-PROFUNDA-ULTIMAS-ALTERACOES-2026-11-14.md](file:///C:/Users/Israel%20Rozar/.gemini/antigravity/brain/ec9956e5-078d-4d87-9a8e-74481434c7dc/VARREDURA-PROFUNDA-ULTIMAS-ALTERACOES-2026-11-14.md) |
| **2026-11-14** | Auditoria de Ativos & Direção de Arte | Capas 16:9 e Evidências Reais | Reversão de mockups 3D; 8 capas 16:9 autênticas aprovadas | [RELATORIO-DIRECAO-ARTE-CAPAS-E-RECORTES-EVIDENCIAS-2026-11-02.md](file:///C:/Users/Israel%20Rozar/.gemini/antigravity/brain/ec9956e5-078d-4d87-9a8e-74481434c7dc/RELATORIO-DIRECAO-ARTE-CAPAS-E-RECORTES-EVIDENCIAS-2026-11-02.md) |
| **2026-11-13** | QA de Implementação da Nova Home | Home React (Figma 370:16614 e 375:366) | Testes Playwright (320px–1440px), a11y de menu | [site/design-qa.md](file:///c:/Users/Israel%20Rozar/Documents/ChatGPT/Portfolio/site/design-qa.md) |
| **2026-11-03** | Auditoria Editorial e Acessibilidade | Einstein, Claro, Neoenergia, Itaú | WCAG AA, WebP, sticky TOC funcional | [AUDITORIA-RECRUTADORES-UX-UI-COPY-2026-11-02.md](file:///c:/Users/Israel%20Rozar/Documents/ChatGPT/Portfolio/AUDITORIA-RECRUTADORES-UX-UI-COPY-2026-11-02.md) |
| **2026-11-02** | Auditoria Comparativa Figma Página 30 | Plataforma IFA (Vencimentos, Campanhas, etc.) | Consistência com íon Design System | [AUDITORIA-COMPARATIVA-FIGMA-PAGINA30-E-CASES-EDITORIAIS-2026-11-02.md](file:///C:/Users/Israel%20Rozar/.gemini/antigravity/brain/ec9956e5-078d-4d87-9a8e-74481434c7dc/AUDITORIA-COMPARATIVA-FIGMA-PAGINA30-E-CASES-EDITORIAIS-2026-11-02.md) |

---

## Protocolo de Registro Automático de Novas Alterações

Sempre que uma nova auditoria, correção ou evolução for concluída, o procedimento padrão exige:

1. **Executar o script de automação de log:**
   ```powershell
   python scripts/update_changelog.py
   ```
2. **Atualizar o [CHANGELOG.md](../CHANGELOG.md) e [docs/LOG-AUDITORIAS-E-EVOLUCOES.md](file:///c:/Users/Israel%20Rozar/Documents/ChatGPT/Portfolio/docs/LOG-AUDITORIAS-E-EVOLUCOES.md)** com:
   * **Tipo da alteração:** Adição (`Added`), Modificação (`Changed`), Correção (`Fixed`), Remoção (`Removed`) ou Auditoria (`Audits`).
   * **Contexto e Racional:** Justificativa da decisão e correspondência no Figma (nó/frame).
   * **Arquivos e Linhas Afetadas:** Lista explícita com links clicáveis.
   * **Evidências de Validação:** Resultado do build (`npm run build`), testes de rotas ou capturas de tela comparativas.

