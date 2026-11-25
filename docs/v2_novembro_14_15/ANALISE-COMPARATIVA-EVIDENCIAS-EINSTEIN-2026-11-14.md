# Análise Comparativa Visual: Calibração de Evidências no Case em Destaque

**Projeto:** Portfólio Israel Rozar · Case Flagship: Hospital Israelita Albert Einstein  
**Data:** 14 de Novembro de 2026  
**Objetivo:** Comparar visualmente e estruturalmente as duas alternativas de exibição de evidências no card em destaque para determinar a densidade de informação ideal.

---

## 1. Visão Geral das Duas Alternativas Testadas

| Atributo | Alternativa A (Calibração Essencial: 2 Evidências) | Alternativa B (Pura Elegância Editorial: Zero Evidências) |
| :--- | :--- | :--- |
| **Composição da Coluna Direita** | Mockup MacBook Pro + Legenda + **2 caixas de métricas** (`14` Famílias sistematizadas e `121` Pacientes em discovery) + Assinatura de parceiros. | Mockup MacBook Pro + Legenda + **Espaço de respiro editorial** + Assinatura de parceiros. |
| **Evidências Exibidas** | Apenas as 2 métricas de maior impacto e rigor metodológico. | Nenhuma caixa numérica na capa da Home (dados 100% no case interno). |
| **Objetivo Perceptual** | Equilibrar prova visual de UI com prova quantitativa de liderança de UX Lead. | Foco monocelular na excelência visual do produto e no clique para o case. |

---

## 2. Inspeção Métrica e Estrutural do DOM

Ambas as alternativas foram renderizadas ao vivo no servidor local em resolução Retina 2× (1440×900px Desktop e 375×812px Mobile) e medidas via Playwright:

```
+-----------------------------------+--------------------+--------------------+
| Métrica no DOM                    | Alternativa A (2)  | Alternativa B (0)  |
+-----------------------------------+--------------------+--------------------+
| Altura total do card (.pf-featured)| 584 px             | 581 px             |
| Altura Coluna Esquerda (Texto/CTA)| 584 px             | 581 px             |
| Altura Coluna Direita (Mídia/Evid)| 584 px             | 412 px (conteúdo)  |
| Vazio vertical na coluna direita  | 0 px (Preenchido)  | ~169 px (Espaço)   |
| Altura Mobile (.pf-featured)      | 2450 px            | 2118 px (-332 px)  |
+-----------------------------------+--------------------+--------------------+
```

### O fenômeno da "assimetria vertical" na Alternativa B:
A coluna da esquerda possui um volume textual substancial (Badge de Saúde + Título em H3 de 3 linhas + Parágrafo explicativo de 3 linhas + Callout de Atuação como UX Lead de 4 linhas + Botão de Ação CTA Lime).  
* Na **Alternativa A**, as duas caixas de métricas preenchem exatamente a altura necessária para que a base da coluna direita termine no mesmo alinhamento horizontal do botão CTA da esquerda.
* Na **Alternativa B**, sem as caixas de evidências, a coluna direita fica consideravelmente mais curta que a esquerda, gerando um vazio residual sob o mockup antes do rodapé de parceiros.

---

## 3. Análise Perceptual e Cognitiva (Olhar de Recrutadores e CPOs)

### Por que a versão original de 4 evidências pecava por excesso?
* **"04 entrevistas médicas"**: Soava como uma amostra pequena para pesquisa qualitativa de um grande hospital.
* **"44 participantes em testes"**: Repetia o conceito de validação sem acrescentar autoridade nova.
* **4 caixas lado a lado**: Dividiam o olhar do recrutador em 4 pontos de atenção concorrentes, roubando o protagonismo do Mockup do MacBook Pro.

### Comparativo: Alternativa A vs Alternativa B

1. **Gatilho de Credibilidade Instantânea:**
   * **Alternativa A:** Quem passa 5 segundos pela Home absorve a equação executiva completa: **Marca hospitalar de prestígio** + **Hardware Pro de alta fidelidade** + **Escala de Design System (14 famílias)** + **Validação clínica com usuários reais (121 pacientes)**.
   * **Alternativa B:** Apresenta apenas o visual do computador. Para um leitor apressado, pode parecer um trabalho puramente cosmético de UI design (mockup estético), escondendo o esforço massivo de UX Architecture e liderança clínica.

2. **Diferenciação do Case Flagship vs Cards Secundários:**
   * Os 3 cards do Itaú logo abaixo **não possuem caixas de métricas**; eles são mais compactos e focados na imagem de capa.
   * O Case do Einstein **precisa** se destacar como o projeto de maior peso e autoridade do portfólio. As 2 evidências-âncora da Alternativa A conferem a este card o peso de "case master", justificando a largura total (full-width span).

---

## 4. O Veredito Técnico

> ### 🏆 Alternativa Vencedora: **Alternativa A (Calibração Essencial com 2 Evidências)**
> 
> **Justificativa Definitiva:**
> 1. **Equilíbrio de Layout Impecável:** Resolve a assimetria vertical entre a narrativa densa de UX Lead da esquerda e a coluna visual da direita, fechando a linha de base com precisão milimétrica.
> 2. **Eliminação de 100% do Ruído:** Corta as métricas fracas ("04 entrevistas" e "44 testes"), mantendo apenas as **2 evidências inquestionáveis** (`14 famílias de laudos` e `121 pacientes ouvidos`).
> 3. **Posicionamento de Liderança (UX Lead vs UI Designer):** Demonstra que por trás do belo produto no MacBook Pro existe rigor científico, método de discovery e governança de sistemas complexos.

---

## 5. Capturas de Verificação Real

* 🖼️ [comparativo_visual_alt_a_vs_alt_b.png](file:///C:/Users/Israel%20Rozar/.gemini/antigravity/brain/ec9956e5-078d-4d87-9a8e-74481434c7dc/comparativo_visual_alt_a_vs_alt_b.png) — Comparativo direto lado a lado.
* 💻 [compare_alt_a_desktop.png](file:///C:/Users/Israel%20Rozar/.gemini/antigravity/brain/ec9956e5-078d-4d87-9a8e-74481434c7dc/compare_alt_a_desktop.png) — Alternativa A no Desktop.
* 💻 [compare_alt_b_desktop.png](file:///C:/Users/Israel%20Rozar/.gemini/antigravity/brain/ec9956e5-078d-4d87-9a8e-74481434c7dc/compare_alt_b_desktop.png) — Alternativa B no Desktop.
* 📱 [compare_alt_a_mobile.png](file:///C:/Users/Israel%20Rozar/.gemini/antigravity/brain/ec9956e5-078d-4d87-9a8e-74481434c7dc/compare_alt_a_mobile.png) — Alternativa A no Mobile.
* 📱 [compare_alt_b_mobile.png](file:///C:/Users/Israel%20Rozar/.gemini/antigravity/brain/ec9956e5-078d-4d87-9a8e-74481434c7dc/compare_alt_b_mobile.png) — Alternativa B no Mobile.
