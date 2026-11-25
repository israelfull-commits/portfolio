# Auditoria Visual e Estrutural Completa: Case Einstein (/cases/einstein-laudos)

**Projeto:** Portfólio Israel Rozar · Case Flagship: Hospital Israelita Albert Einstein  
**Data:** 14 de Novembro de 2026  
**Status:** Inspeção via Playwright em Desktop (1440×900 Retina 2×) e Mobile (375×812 Retina 2×)  
**Referência de Design:** Template Figma Portfólio / Case / Desktop · 1280 (Nó 370:17047)

---

## 1. Resumo Executivo da Auditoria

A página do case do Einstein possui uma base sólida, com excelente densidade narrativa, separação clara entre métodos de pesquisa clínica, arquitetura de informação e governança de Design System. 

No entanto, a auditoria identificou oportunidades cruciais de **refinamento de grid, proporção de galerias e hierarquia**, especialmente no **Capítulo 05**, que concentrava 6 figuras empilhadas verticalmente em uma coluna de 4.444px de altura.

---

## 2. Diagnóstico Seção por Seção

### A. Hero & Metadata (Figma Nó 370:17047)
* **Breadcrumb:** `← Voltar aos cases` perfeitamente acessível com `min-height: 2.5rem` (40px) e link ativo para a Home (`/`).
* **Kicker:** Tag `Saúde · UX Lead` com tracking equilibrado (`0.05em`).
* **H1 Principal:** `Einstein · Laudos médicos` renderizado em 56px / 700 com cor Pine (`#1A201C`), transmitindo sobriedade institucional.
* **Headline & Subtitle:**
  * *Headline:* `Clareza não é o mesmo que compreensão.` (provocação intelectual sênior).
  * *Subtitle:* `Uma linguagem visual modular para laudos em diferentes canais.`
* **Grid de Metadados (4 Colunas):**
  * `MEU PAPEL`: UX Lead
  * `EQUIPE`: Foursys × Hospital Israelita Albert Einstein
  * `ESCOPO`: Pesquisa, modelagem da informação e prototipagem
  * `RESULTADO-CHAVE`: 14 famílias de laudos padronizadas
  * *Status:* 100% aderente ao chassi de 4 colunas com padding de 24px (`1.5rem`) e fundo Surface (`#F6F3EC`).
* **Capa Visual do Hero (`.cp-hero-visual`):**
  * Utiliza a Capa Editorial do Design System (`hiae-capa-editorial-1600.webp` em 1110×689px) com moldura de raio 24px e sutil aura lime (`rgba(206, 255, 26, 0.08)`).

---

### B. Arquitetura de Leitura: Sidebar vs Artigo (2 Colunas Desktop)
* **Sidebar Esquerda (`.cp-sidebar`, 240px):**
  * Índice dinâmico de 7 capítulos com numeração sequencial (01 a 07).
  * Fixação inteligente (*sticky*) que acompanha o leitor durante a descida da página.
  * *Status:* Excelente usabilidade para recrutadores que desejam saltar direto para a seção de pesquisa ou solução.
* **Coluna de Conteúdo (`.cp-article`, 848px):**
  * Largura calculada dentro da métrica de leitura ideal (65–85 caracteres por linha para parágrafos).
  * Tipografia: 18px com `line-height: 1.65` (28px).

---

### C. Mapeamento dos 7 Capítulos Narrativos

| Capítulo | Título | Altura | Conteúdo e Figuras | Diagnóstico |
| :---: | :--- | :---: | :--- | :--- |
| **01** | *Organizar resultados sem perder o contexto clínico.* | 647 px | Texto de abertura + 3 cards de métricas (`4 médicos`, `Questionário`, `14 categorias`). | **Perfeito.** Leve e contextualizador. |
| **02** | *Do documento ao dado.* | 1706 px | Diagnóstico legado + 2 Figuras: Estado atual anotado + Diagrama de triangulação. | **Consistente.** Boa prova metodológica. |
| **03** | *Uma hierarquia que funcione na tela e no papel.* | 1212 px | Decisão modular + 1 Figura: Proposta anotada. | **Claro e direto.** |
| **04** | *Preservar relações entre resultado, referência e contexto.* | 1274 px | Taxonomias + 1 Figura: Documentação de tokens e componentes (`DataField`, `ExamTitle`). | **Forte.** Prova direta de Design System. |
| **05** | *Uma estrutura comum para conteúdos diferentes.* | **4444 px** | **6 Figuras empilhadas**: Original, Proposta demonstrativa, Template Word (SVG crop), Mamografia, Ressonância, Multicanal. | ⚠️ **Gargalo de Grid.** As imagens estavam em coluna única vertical, forçando um scroll longo desnecessário. |
| **06** | *Clareza percebida e interpretação exigem avaliações distintas.* | 503 px | Separação entre clareza subjetiva (84,3%) e interpretação clínica real (56,25%). | **Crucial.** Mostra maturidade científica. |
| **07** | *Pesquisa, entregáveis e colaboração.* | 506 px | Síntese de governança e transferência para engenharia. | **Conclusão sólida.** |

---

## 3. Análise Detalhada de Grid, Margens, Paddings e Estilos

### Grid e Espaçamentos (Tokens Oficiais)
* **Largura Máxima do Container:** `width: min(100% - 3rem, 1152px)` — perfeitamente harmonizado com o grid de 12 colunas da Home.
* **Respiro entre Capítulos:** `--cp-chapter-gap: clamp(4rem, 6vw, 5.5rem)` (64px a 88px) — hierarquia Gestalt forte, separando claramente cada etapa do processo.
* **Respiro entre Parágrafos:** `margin-bottom: 1.25rem` (20px).
* **Grid de Galerias (`.cp-gallery`):**
  * *Problema Atual:* O CSS definia apenas `display: grid; gap: 2.5rem;` sem `grid-template-columns`.
  * *Ação de Correção:* Aplicar `grid-template-columns: repeat(2, minmax(0, 1fr))` para telas desktop (`>= 768px`), permitindo que pares comparativos (como *Antes × Depois* e *Mamografia × Ressonância*) fiquem lado a lado, reduzindo a altura do Capítulo 05 de 4.444px para ~2.200px.

### Bordas, Sombras e Elevação
* **Bordas dos Cards de Figura (`.cp-figure`):**
  * `border: 1px solid var(--cp-border)` (`#EDE9DE`)
  * `border-radius: 1rem` (16px)
  * `background-color: var(--cp-surface)` (`#F6F3EC`)
  * `padding: 1.5rem` (24px)
  * *Avaliação:* Consistência total com o design system, conferindo "respiro de museu/galeria" a cada laudo clínico.
* **Elevação e Sombras:**
  * Uso de sombra suave de oclusão de ambiente (`box-shadow: 0 4px 20px -2px rgba(10, 54, 34, 0.05)`).
  * Sem sombras duras ou artificiais, mantendo o padrão visual editorial clean.

### Lightbox Modal (Inspeção em Tamanho Real)
* Cada figura possui o botão integrado `Ver ampliado →`.
* Ao clicar, abre um `<dialog className="cp-lightbox">` nativo com `backdrop-filter: blur(8px)`, permitindo inspecionar o exame em escala 1:1 com botão para alternar entre "Ajustar à tela" e "Ver em tamanho original".
* *Avaliação:* Excelente recurso de acessibilidade e transparência para recrutadores técnicos.

---

## 4. Oportunidades de Otimização Imediata

1. **Ativar o Grid de 2 Colunas no `.cp-gallery`:**  
   Fazer com que as figuras do Capítulo 05 fiquem agrupadas em pares lado a lado (Original vs Proposta, e Mamografia vs Ressonância), valorizando a comparação direta e reduzindo o scroll.
2. **Harmonização do Ativo Multicanal:**  
   Garantir que a figura de fechamento do Capítulo 05 utilize o novo ativo em alta definição (`hiae-multicanal-web-celular.webp`, 2000px).
3. **Equilíbrio no Mobile (375px):**  
   Garantir que a sidebar recolhida no mobile se torne um seletor de capítulos compacto no topo do artigo.
