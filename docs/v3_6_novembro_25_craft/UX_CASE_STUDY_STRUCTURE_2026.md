# UX Case Study Structure & Writing Standards (2026) — Síntese Canônica

> **Fonte original:** [UX Companion — UX Case Study Examples (Atualizado 25 Nov 2026)](https://uxcompanion.co.uk/ux-case-study-examples)  
> **Premissa central:** *"Um estudo de caso é um argumento de que você tomou boas decisões, não um diário do projeto."*

---

## 1. Anatomia Canônica em 7 Seções (`1.000 – 1.800 palavras` · `< 10 min` de leitura)

| # | Seção | Orçamento | Função Obrigatória |
| :-: | :--- | :---: | :--- |
| **1** | **Resumo Executivo (Summary)** | 60–100 palavras | Produto, papel, time, período, problema em 1 frase e resultado em 1 frase. Quem ler só isso decide se continua. |
| **2** | **Contexto & Restrição** | 100–200 palavras | Por que importava para negócio e usuários, e **o que tornou difícil** (prazo, regulação, legado, desacordo, falta de dados). |
| **3** | **Meu Papel (Your Role)** | 40–80 palavras | O que **eu** conduzi/decidi vs. o que outros papéis fizeram (PM, Engenharia, Pesquisa — sem citar nomes pessoais). |
| **4** | **O Que Aprendi Primeiro** | 150–250 palavras | Pesquisa, dados ou auditoria + **o achado específico que mudou a direção**. Mostrar 1 artefato real, não um mosaico. |
| **5** | **Decisões (Coração do Case)** | 400–700 palavras | **2 ou 3 decisões:** alternativas consideradas, escolha feita, justificativa e **custo/trade-off aceito** (*"uma decisão que não custou nada não foi uma decisão"*). |
| **6** | **Resultado (Outcome)** | 100–200 palavras | O que aconteceu contra um **baseline**, com atribuição honesta (incluindo fatores externos/limites). |
| **7** | **Reflexão (Reflection)** | 60–120 palavras | **1 coisa específica** que eu faria diferente hoje e por quê (nunca *"aprendi muito"*). |

> **Regra de imagens:** 1 tela *antes*, 1 tela *depois* e 1 imagem por decisão-chave costuma ser suficiente. **Cada legenda deve declarar o ponto exato que a imagem prova.**

---

## 2. Os 5 Arquétipos de Case & Cobertura do Portfólio Atual
Um portfólio forte prova competências complementares entre seus cases:
1. **Design System / Acessibilidade** → Coberto por **Hospital Albert Einstein** *(Design System modular + WCAG 2.2 AAA)*
2. **Ambiente Regulado / NDA / Novo Fluxo** → Coberto por **Itaú Unibanco (IFA)** *(Sigilo bancário + fluxo assistido por IA com revisão humana)*
3. **Flow Improvement (Melhoria de Fluxo)** → Coberto por **Claro Brasil** *(Unificação de 22 jornadas em 5 etapas Desktop + Mobile)*
4. **Research-Led / Service Design** → Coberto por **Neoenergia** *(5 Service Blueprints + auditoria de backstage + 118 ideias)*
5. **Projeto Cortado / Falha Honesta** → Opcional para futuras expansões (já parcialmente coberto pelas seções de *Disciplina de Escopo* e *Reflexão Crítica* nos 4 cases).

---

## 3. Checklist Rápido Pré-Envio por Case (10 Pontos)
- [ ] Resumo nomeia produto, papel, problema e resultado logo no topo.
- [ ] Contexto deixa claras as **restrições reais** (técnicas, regulatórias ou de prazo).
- [ ] Separação explícita entre **"Eu decidi/conduzi"** e **"o time"** (sem *"nós"* genérico em tudo).
- [ ] 2–3 decisões com alternativa descartada e custo aceito.
- [ ] Números com baseline, período e nota honesta de atribuição.
- [ ] Toda imagem com legenda explicando o ponto que comprova.
- [ ] Reflexão com 1 mudança específica e concreta.
- [ ] Dados confidenciais protegidos/anonimizados e declarados no topo.
- [ ] Leitura abaixo de 10 minutos; apresentável em 15–20 minutos em entrevista.
- [ ] Transparência sobre uso e validação humana de IA quando aplicável.


---

## 4. Template Operacional de 9 Blocos & Micro-Template de Decisão (`ux-case-study-template`)

> **Fonte complementar:** [UX Companion — UX Case Study Template (2026)](https://uxcompanion.co.uk/ux-case-study-template)  
> **Padrão tipográfico e de escopo:** `1.200–1.800` palavras · `5–8 min` de leitura · `4–6` telas de alta qualidade (cada uma com **racional**, não descrição) · corpo `16–18px` · `line-height 1.5–1.75` · largura máxima `~65ch`.

### Os 9 Blocos Canônicos para Novos Cases
1. **01 — HERO SUMMARY:** Título + 1 parágrafo (3–4 frases: empresa, papel, problema em 1 linha, resultado em 1 linha) + **1 imagem Hero principal** (a tela mais forte, não um mosaico).
2. **02 — CONTEXT:** O que o negócio buscava? O que atrapalhava? Qual a tensão central?
3. **03 — YOUR ROLE:** O que você conduziu ponta a ponta? No que contribuiu? Quais outros papéis estavam na sala (PM, Engenharia, Pesquisa)?
4. **04 — RESEARCH:** Abra com o **insight**, não com o método (*"Seis entrevistas revelaram um achado inesperado..."*); cite o método de passagem.
5. **05 — PROBLEM FRAMING:** 1 frase afiada (*"Como podemos [objetivo específico] sem [trade-off]?"*).
6. **06 — PROCESS AND DECISIONS:** 2–3 decisões reais seguindo o **Micro-Template de Decisão** abaixo.
7. **07 — SOLUTION:** Design final anotado — **3 a 6 telas-chave**, cada uma com **racional de decisão** (por que ficou assim), nunca descrição óbvia do que se vê.
8. **08 — OUTCOME:** Números com baseline/período/atribuição quando disponíveis, ou evidência qualitativa honesta (feedback de stakeholders, adoção pelo time, continuidade do trabalho).
9. **09 — REFLECTION:** 1 ponto específico que faria diferente hoje (focado em processo/decisão, não em cosmética).

### Micro-Template de Decisão (usar 2–3× por case)
```markdown
**A QUESTÃO:** A escolha concreta que precisava ser tomada.
**AS OPÇÕES:** As 2 ou 3 alternativas reais consideradas (nunca "exploramos várias opções").
**OS TRADE-OFFS:** O custo de cada opção (esforço de engenharia, atrito do usuário, consistência de DS, risco de negócio).
**A DECISÃO:** O que foi escolhido, por quê (em linguagem simples) e qual custo foi aceito.
**A EVIDÊNCIA (opcional):** Tela, resultado de teste, dado ou fala que sustentou a escolha.
```

> **Alerta de Senioridade:** Evite deixar todos os cases mecanicamente idênticos — use os 9 blocos como espinha dorsal, mas adapte a ênfase e o ritmo visual à natureza de cada projeto (Design System, Fluxo Multicanal, Service Blueprint ou NDA/IA).

---

## 7. Protocolo Editorial Antes ➔ Depois (`ux-case-study-before-and-after`)

Referência operacional de reescrita para converter narração de processo em evidência de decisão sênior:

| Seção | Padrão Fraco (Evitar) | Padrão Forte (Aplicar) | Alavanca Editorial |
| :--- | :--- | :--- | :--- |
| **Hero Summary (15s)** | *"Trabalhei com um time multidisciplinar aplicando design thinking para um grande cliente."* | Empresa nomeada + verbo em 1ª pessoa (*"Liderei"*) + número do problema + resultado + janela temporal. | Ganha os próximos 8 minutos de leitura. |
| **Problem Framing** | *"Usuários tinham dores na jornada e o time alinhou redesenhar o fluxo."* | Contexto de negócio + restrição histórica/regulatória + hipótese nomeada + **tensão nomeada** (ex.: Compliance/Engenharia) + prazo. | Ganha os próximos 25 minutos e comprova leitura de contexto real. |
| **Decisions (Coração)** | *"Criamos wireframes, iteramos com stakeholders e fizemos UI moderna."* | **3 decisões numeradas** com escolha + alternativa descartada + trade-off aceito + evidência/validação. | Expõe julgamento sênior e prepara perguntas profundas de entrevista. |
| **Outcomes** | *"Aumentou engajamento em 320%; stakeholders adoraram."* | Números contra *baseline* + **variáveis de confusão (*confounders*) nomeadas** + atribuição honesta do mérito do design. | Constrói credibilidade de banca Senior/Staff. |
| **Reflection** | *"Foi um ótimo aprendizado; orgulho do que entregamos."* | **Um padrão concreto que você revisitaria** (ex.: envolver Compliance/Engenharia antes de otimizar demais o protótipo). | Um dos sinais mais fortes (e menos usados) de maturidade. |

### As 3 Viradas de Narrativa (*Storytelling Shifts*)
1. **Cronologia ➔ Causalidade:** organizar pelo que importou e por quê — cortar workshops/artefatos que não geraram uma decisão nomeada.
2. **"Nós" ➔ "Eu" + papéis nomeados:** usar **Eu** para escolhas individuais e **o time / PM / Engenharia / Compliance** para entregas conjuntas.
3. **Processo ➔ Produto:** metodologia fica implícita; o espaço nobre vai para a interface real entregue e o raciocínio por trás.

> **Regra 80/20 de Reescrita:** Ajustar **Hero Summary + 3 Decisões Explícitas + Outcomes honestos com atribuição** resolve ~80% das falhas de cases fracos sem precisar reescrever do zero.
