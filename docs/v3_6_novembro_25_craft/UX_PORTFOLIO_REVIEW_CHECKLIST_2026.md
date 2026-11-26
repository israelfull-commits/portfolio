# UX Portfolio Review Checklist (2026) — Framework Canônico de Revisão & Scorecard

> **Fonte original:** [UX Companion — UX Portfolio Review Checklist (2026)](https://uxcompanion.co.uk/ux-portfolio-review-checklist)  
> **Propósito:** Framework operacional de **efetividade** (*"está funcionando?"*) em 6 seções × 5 pontos (**total `/30`**), complementar ao checklist de completude (*"está lá?"*).  
> **Uso recomendado:** Regra permanente de revisão pré-submissão para vagas Sênior/Staff, combinada ao [portfolio_qa_sentinel.py](../../scripts/portfolio_qa_sentinel.py) e a revisões externas por pares.

---

## 1. Estrutura de Pontuação (Total: `/30`)

| Faixa de Pontuação | Diagnóstico Operacional | Ação Recomendada |
| :--- | :--- | :--- |
| **27 – 30** | **Pronto para vagas Sênior** | Portfólio operando no nível exigido. Submeter com confiança. |
| **22 – 26** | **Pronto para Pleno; precisa de ajustes para Sênior** | Identificar as seções com menor nota e resolver em um ciclo focado. |
| **17 – 21** | **Necessita trabalho estrutural** | Possui boas peças, mas ao menos duas seções jogam contra. Não submeter ainda. |
| **Abaixo de 17** | **Reconstrução** | Exige mais que ajustes incrementais; começar pela reestruturação dos cases. |

---

## 2. As 6 Seções Diagnósticas & Rubrica Detalhada (1 a 5)

### Seção 1 · Homepage Review (`/5`)
**Teste diagnóstico (30 segundos):** Um recrutador com 30 segundos de atenção consegue ver nome, sinalização de senioridade, empresas nomeadas e ao menos um card de estudo de caso?

| Nota | Critério |
| :---: | :--- |
| **5** | Acima da dobra contém nome, cargo, sinalização de senioridade, 3–5 cards de cases com empresas nomeadas e contato visível. Sem texto genérico de missão (*mission statement filler*) e sem intro animada. Recrutador conclui a triagem sem precisar rolar. |
| **4** | Maioria dos itens acima; 1 elemento ausente ou fraco (ex.: contato apenas no rodapé). |
| **3** | Cases presentes, mas empresas não nomeadas na Home; recrutador precisa clicar para ver sinal. |
| **2** | Hero dominado por frase de efeito ou animação; cases exigem rolagem longa. |
| **1** | Sem sinalização de senioridade, sem empresas nomeadas e sem cards visíveis. |

---

### Seção 2 · Navigation Review (`/5`)
**Teste diagnóstico:** Todos os links funcionam, os destinos fazem sentido e o leitor sabe sempre onde está?

| Nota | Critério |
| :---: | :--- |
| **5** | Máximo de **4–6 itens** com rótulos claros e 100% funcionais. Breadcrumbs ou hierarquia visual deixam a página atual óbvia. Logo retorna para a Home. Contato acessível a partir de qualquer página. |
| **4** | Maioria dos itens acima; 1 ponto menor de fricção (ex.: rótulo ligeiramente ambíguo, mas funcional). |
| **3** | Navegação funciona, mas tem 8+ itens ou rótulos pouco claros. |
| **2** | Links quebrados, rótulos ausentes ou inconsistências visíveis. |
| **1** | Navegação atrapalha ativamente a leitura. |

---

### Seção 3 · Case Study Review (`/5`)
**Teste diagnóstico:** Avaliar os cases **como um conjunto** (consistência importa tanto quanto o melhor case individual).

| Nota | Critério |
| :---: | :--- |
| **5** | **3–5 estudos de caso** de profundidade comparável (**5–8 minutos** de leitura cada). Cada case abre com resumo executivo nomeando empresa, papel, problema e resultado. Cada um tem seção de **decisões** com **2–3 decisões explícitas**, alternativas consideradas e trade-offs aceitos. Resultados honestos. Encerra com reflexão específica. |
| **4** | Maioria dos itens acima; 1 case mais fraco que os demais ou 1 elemento estrutural raso no conjunto. |
| **3** | Cases desiguais; alguns sem seção de decisões, resumos genéricos ou resultados inflados. |
| **2** | Dominado por narração genérica de processo; poucas decisões visíveis; cara de template de bootcamp. |
| **1** | Cases ausentes ou superficiais; avaliador não consegue identificar o que o candidato decidiu. |

---

### Seção 4 · Presentation Review (`/5`)
**Teste diagnóstico:** A apresentação visual **sustenta** o conteúdo ou **compete** com ele?

| Nota | Critério |
| :---: | :--- |
| **5** | Tipografia limpa (família consistente, escala contida, corpo legível **16px+**). Hierarquia visual forte. **Screenshots reais de produto priorizados sobre mockups decorativos.** Mínimo de elementos decorativos. Espaço em branco generoso. Acessibilidade básica garantida (**contraste mínimo WCAG 2.2 AA**). |
| **4** | Maioria dos itens acima; 1 problema visual menor (ex.: 1 imagem em baixa resolução). |
| **3** | Aceitável, mas sem destaque; algumas inconsistências de tipografia ou espaçamento. |
| **2** | Problemas visíveis: baixo contraste, texto pequeno/ilegível, tipografia inconsistente, imagens fracas. |
| **1** | Apresentação prejudica ativamente a credibilidade. |

---

### Seção 5 · Mobile Review (`/5`)
**Teste diagnóstico:** Abrir o portfólio em um celular (**375px**) e realizar a triagem completa de um recrutador.

| Nota | Critério |
| :---: | :--- |
| **5** | Renderização limpa no mobile. Dobra inicial da Home faz sentido em `375px`. Imagens dos cases amigáveis a zoom. Texto legível sem scroll horizontal. Navegação colapsa em menu mobile usável. Contato/ações funcionam bem no toque. |
| **4** | Maioria dos itens acima; 1 fricção menor no mobile. |
| **3** | Funciona com concessões visíveis (texto pequeno, imagens cortadas). |
| **2** | Problemas funcionais (scroll horizontal, navegação quebrada, texto ilegível). |
| **1** | Renderização mobile quebrada. |

---

### Seção 6 · Credibility Review (`/5`)
**Teste diagnóstico:** Um avaliador cético consegue verificar e confiar nas afirmações do candidato?

| Nota | Critério |
| :---: | :--- |
| **5** | Empresas nomeadas e verificáveis. Resultados honestos (zero métricas infladas). Seções de reflexão que reconhecem o que não funcionou ou o que faria diferente. Clareza visível de **"o que eu fiz vs. o que o time fez"**. Seção "Sobre" específica e crível. **Domínio pessoal próprio** (ex.: `israelrozar.com.br`) em vez de subdomínio gratuito. Hospedagem estável (zero imagens quebradas, SSL válido). |
| **4** | Maioria dos itens acima; 1 fricção menor de credibilidade (ex.: case anonimizado ou subdomínio gratuito). |
| **3** | Maioria crível, mas ao menos 1 case com métrica inflada ou linguagem promocional (*PR-speak*). |
| **2** | Problemas de credibilidade visíveis em múltiplos cases. |
| **1** | Credibilidade comprometida por afirmações infladas, jargão publicitário ou dados inverificáveis. |

---

## 3. Revisão Externa (Regra de Triangulação)

O framework alerta que **autoavaliação é necessária, mas insuficiente** (*"o candidato não consegue ver o que não consegue ver"*). A rotina recomendada antes de submissões para vagas Sênior/Staff combina:
1. **Autoavaliação estruturada** usando os 6 pilares (`/30`) + automação técnica (`portfolio_qa_sentinel.py`).
2. **Revisão por par (Peer Review):** pedir 30 minutos a um designer sênior de confiança na rede.
3. **Segunda opinião independente (opcional):** revisão escrita externa focada em pontos cegos antes de aplicar para vagas-alvo.

---

## 4. Scorecard Atual do Portfólio — Israel Rozar (`28 / 30`)

| Seção | Nota Atual | Evidências Atendidas | Oportunidade de Elevação para `5/5` |
| :--- | :---: | :--- | :--- |
| **1. Homepage** | **4.5 / 5** | Nome, cargo (`Senior Product Designer`), 20 anos de atuação, 4 empresas nomeadas, CTA de contato e currículo no topo, 0 filler/animação. | Manter o topo compacto para que o 1º card (Einstein) apareça ainda mais alto em telas `1366×768`. |
| **2. Navigation** | **5.0 / 5** | 4 itens no header, logo → Home, breadcrumb + TOC lateral nos cases, navegação circular, contato em todas as páginas. | Critério 100% atendido. |
| **3. Case Studies** | **4.5 / 5** | 4 cases com resumo executivo, decisões com alternativas/trade-offs, *"O que ficou fora do recorte"* e *"O que eu faria diferente hoje"*. | Igualar a densidade visual do case Itaú (sigilo bancário) com mais diagramas de arquitetura/decisão. |
| **4. Presentation** | **4.5 / 5** | `Plus Jakarta Sans` unificada, corpo `16px`, WCAG 2.2 AA/AAA, 0 estilos inline, 0 duplicatas, espaço em branco *outside-in*. | Aplicar as variações selecionadas de estúdio (`V01`–`V19`) preservando 100% dos screenshots reais legíveis. |
| **5. Mobile** | **5.0 / 5** | `0px` overflow em `390px`, menu mobile acessível, Lightbox com zoom nativo, cards equalizados, alvos `>= 24px`. | Critério 100% atendido. |
| **6. Credibility** | **4.5 / 5** | Empresas reais (Einstein, Itaú, Claro, Neoenergia), métricas auditadas sem PR-speak, autoria individual explícita, `0` imagens quebradas, SSL ativo. | Configurar **domínio pessoal próprio** (ex.: `israelrozar.com.br`) apontando para o GitHub Pages em vez de `israelfull-commits.github.io/portfolio/`. |
| **TOTAL** | **28.0 / 30** | **Faixa 27–30: Pronto para submissão em vagas Sênior/Staff.** | Com domínio próprio + polimento visual dos cases: **`29.5–30 / 30`**. |

---

## 5. Como Integrar como Regra Permanente Automática

- **Automação técnica (já coberta pelo `portfolio_qa_sentinel.py` v2):**
  - Seções **2 (Navigation)**, **4 (Presentation / WCAG / Tipografia / Gestalt)**, **5 (Mobile 390px)** e parte da **6 (Credibility / zero PR-speak / zero imagens quebradas)** já são verificadas automaticamente em código e Chromium.
- **Governança editorial permanente (`AGENTS.md`):**
  - Incorporar o **Scorecard `/30` (Meta mínima `>= 27/30`)** como gate obrigatório de fechamento em qualquer evolução relevante do portfólio (especialmente ao adicionar um novo case ou reformular a Home).

