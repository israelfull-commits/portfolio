# Regras Permanentes de Design, Auditoria & Prevenção de Erros no Figma (V3.8.0+)

**Proveniência:** Criado no **Antigravity (Google DeepMind)** · **Data de criação:** `2026-11-26` · **Conversa ID:** `b9eff66e-96f2-48ed-af7d-28e8cea0dfad`  
**Objetivo:** Impedir a recorrência dos erros reais detectados na auditoria profunda de 494 nós da página `🚀 V3.8.0` no Figma (`Template-portfolio` · `YIHybVXPe0Hfmja1hAyzQZ`).

---

## 1. Catálogo de Erros Conhecidos & Regras Preventivas Obrigatórias

| # | Erro Real Detectado | Causa Raiz Técnica | Regra Preventiva Permanente |
| :-: | :--- | :--- | :--- |
| **1** | **80 fundos brancos fantasma (`#FFFFFF`)** sobre superfícies `#F4F2E9` / `#FFFDF7` | `figma.createAutoLayout()` cria frames com `fills: [{ type: 'SOLID', color: white }]` por padrão. | **SEMPRE** executar `frame.fills = []` imediatamente após criar qualquer container estrutural/wrapper (header brand, nav, grids, colunas de metadata, linhas de sidebar). Só aplicar `fills` em superfícies explícitas (cards, botões, inputs). |
| **2** | **Frames colapsando para `height: 100px`** (`1280×114`) | `node.resize(w, h)` redefine `primaryAxisSizingMode` e `counterAxisSizingMode` para `'FIXED'`. | **Ordem obrigatória:** `createAutoLayout()` ➔ `resize(w, 100)` ➔ `counterAxisSizingMode = 'FIXED'` ➔ `primaryAxisSizingMode = 'AUTO'` (sempre **depois** do `resize()`). |
| **3** | **Cards irmãos com alturas desiguais** em linhas horizontais (`Home 3-grid`, `Escopo & Reflexão`, `2×2 Cases`) | Containers horizontais sem stretch vertical deixam cada card abraçar apenas seu próprio texto. | Em toda linha de cards irmãos, equalizar alturas com `layoutSizingVertical = 'FILL'` (em linhas de 1 linha) ou calcular `maxH` por linha em grids com `layoutWrap = 'WRAP'`. |
| **4** | **Inconsistência de componentes entre telas** (`SiteHeader` com avatar circular verde `IR` na Home/Gate vs. texto puro nos 4 Cases) | Reconstrução manual divergente de um mesmo padrão estrutural em scripts diferentes. | Extrair padrões recorrentes (`SiteHeader`, `Provenance / Antigravity Banner`, `Button`, `Feature Card`, `Dark Pine Note`) como `COMPONENT`s nativos e usar `.createInstance()` em todas as telas. |
| **5** | **Vazios verticais em blocos de Hero/Spec** (`height: 240` fixo com apenas 3 linhas de texto) | Altura fixa artificial desproporcional ao conteúdo interno. | Usar `primaryAxisSizingMode = 'AUTO'` com padding generoso (`32px`) em blocos de especificação, reservando altura fixa `16:9` apenas quando houver arte raster/vetorial preenchendo 100% da área. |
| **6** | **Fontes não carregadas / estilos errados** | Supor `"Semi Bold"` vs. `"SemiBold"` sem consultar `listAvailableFontsAsync()`. | Sempre rodar `await figma.listAvailableFontsAsync()` na descoberta e carregar explicitamente `Plus Jakarta Sans` (`Regular`, `Medium`, `SemiBold`, `Bold`) antes de qualquer escrita em texto. |
| **7** | **Falta de rastreabilidade nas pranchas** | Pranchas criadas sem indicar versão, IA responsável, datas ou link da sessão. | Instanciar obrigatoriamente `Provenance / Antigravity Banner` em **100% das pranchas** (Home, Cases, Design System, Specs e Handoff), atualizando a data de última modificação no componente mestre a cada rodada. |

---

## 2. Protocolo Obrigatório de Auditoria Pós-Criação no Figma

Antes de considerar qualquer prancha do Figma concluída, executar automaticamente:
1. **Varredura programática (`use_figma`):**
   - `whiteGhostFills === 0` (nenhum wrapper sem borda com `#FFFFFF` acidental);
   - `nonJakartaFonts === 0` (100% `Plus Jakarta Sans`);
   - `zeroWidthTexts === 0` (nenhum texto colapsado);
   - `equalHeightGrids === PASS` (todos os cards irmãos da mesma linha com altura idêntica);
   - `provenancePresent === 100%` (instância do banner em cada artboard).
2. **Inspeção visual real (`get_screenshot` + `read_file`):**
   - Baixar e abrir visualmente os prints de cada artboard alterado; corrigir qualquer anomalia óptica antes de reportar conclusão ao usuário.
