# Guia Consolidado · Regras, Códigos Congelados & Banca (2026)

**Fonte Canônica:** *Guia consolidado · Portfólio e cases para Senior Product / UX-UI Designer* (26/11/2026 · Israel Laudelino Rozar)  
**Nota editorial:** *A recomendação sintetiza pesquisa sobre portfólios e critérios de acessibilidade. A aplicação ao contexto sênior e o modelo híbrido SCQA + STAR são uma interpretação editorial.*  
**Skills acopladas:** `portfolio-writing` · `portfolio-design-qa` · `portfolio-banca`

---

## 1. Ordem de Prioridade & Níveis de Confiabilidade

### Ordem de prioridade quando regras competem
1. **Pedido explícito de Israel na conversa** (dados reais confirmados, sem linguagem publicitária).
2. **Norma W3C WCAG 2.2 AA (`A-01..28`)**.
3. **Estrutura do case (`CS-01..15`) e Tom Sênior (`TX-01..09`, `IA-01..04`)**.
4. **Home, Mobile, Apresentação, Higiene Técnica e Figma (`HP-`, `MB-`, `AP-`, `TH-`, `FG-`)**.
5. **Sugestões sem código** (ficam em seção separada e nunca reprovam nada).

### Níveis de confiabilidade das fontes
- **N1 · Norma:** W3C WCAG 2.2 (Recomendação 12/12/2024, What's New, Quick Reference, Understanding).
- **N2 · Pesquisa institucional:** Nielsen Norman Group (Krause 2019, Sunwall 2023, Azarova 2022, Moran 2020/2021, Budiu 2015, Establishing Baselines & Reporting UX Business Outcomes 2026).
- **N3 · Guia editorial de praticantes:** UX Companion (POW XD Ltd — Checklist 35 pontos, Template Pack 9 blocos, Before/After, Senior Examples, What AI Should Not Replace, Interview Worksheet).
- **N4 · Interpretação editorial:** Modelo híbrido SCQA + STAR, rubrica ponderada da banca (`/10`) e adaptação ao contexto sênior de Israel.

---

## 2. Lista Congelada de Códigos (90 Códigos Oficiais)

> **Regra de uso:** Toda auditoria usa **somente estes códigos**. Cada item é `Passa`, `Falha` ou `N/A`.  
> **Critério de Prontidão Sênior:** `0` falhas em `HP`, `CS`, `TX`, `IA` e `A`; até `2` falhas em `AP`/`MB`/`TH` com prazo (exceção formal registrada em ADR: `TH-01` domínio próprio em favor de `github.io`).

### HP · Home (7 códigos)
- `HP-01` Nome, cargo e local acima da dobra
- `HP-02` Posicionamento em uma linha (tipo de problema, para quem, em que setor)
- `HP-03` 3–5 cards com títulos específicos
- `HP-04` Empresa ou setor em cada card
- `HP-05` Contato sem rolar
- `HP-06` Bio e LinkedIn coerentes (cargo, anos, foco)
- `HP-07` Navegação com 4–6 itens, links funcionando, contato em todas as páginas

### CS · Case (15 códigos — 9 Blocos SCQA + STAR)
- `CS-01` Resumo (hero): empresa, papel, problema e resultado em 3–4 frases + 1 tela forte com legenda factual
- `CS-02` Contexto com objetivo de negócio (linguagem de não-designer) e tensão central nomeada
- `CS-03` Papel: o que conduziu × onde contribuiu × composição do time
- `CS-04` Pesquisa abrindo pelo insight (ou declaração explícita de que não houve + o que foi usado)
- `CS-05` Enquadramento em 1–2 frases (pergunta central sem resposta embutida)
- `CS-06` 2–3 decisões no micro-template (`Pergunta → Opções nomeadas → Trade-offs → Decisão/custo aceito → Evidência`)
- `CS-07` 3–6 telas com anotação de **porquê** (justificativa), não de o quê
- `CS-08` Resultado: métrica, linha de base, variação (`p.p.` e relativo identificado), período, confiança/fatores externos (ou evidência qualitativa declarada)
- `CS-09` Reflexão (3–4 frases) com 1 decisão específica a reverter e por quê
- `CS-10` Cases não são templates idênticos
- `CS-11` Leitura em 5–8 min (1.200–1.800 palavras)
- `CS-12` Sinais sênior: reenquadramento, quem concordou, discordância, o que não fazer, resultado no negócio e no time
- `CS-13` Conjunto: case principal + sistema/influência + projeto difícil/falho
- `CS-14` Projeto não lançado declarado diretamente como tal
- `CS-15` NDA tratado por generalização, reconstrução de UI ou faixas numéricas

### TX · Texto e Tom Sênior (9 códigos)
- `TX-01` Primeira pessoa precisa (`Conduzi`, `propus`, `cedi em`; `nós` só quando coletivo)
- `TX-02` Verbos de decisão (`decidi`, `priorizei`, `descartei`, `negociei`; evitar `participei`, `ajudei`, `fui responsável por`)
- `TX-03` Fato antes de adjetivo (sem `incrível`, `inovador`, `disruptivo`, `desafiador`, `rigorosa`, `alta criticidade`, `expertise`)
- `TX-04` Sem linguagem publicitária (frases declarativas, zero superlativos/promessas/clichês)
- `TX-05` Trade-off explícito (`a custo de…`, `aceitamos…`)
- `TX-06` Honestidade de escopo (`não foi lançado`, `não medimos`)
- `TX-07` Frases curtas (uma ideia por frase)
- `TX-08` Termos consistentes (mesmo termo para o mesmo conceito no case inteiro; **Glossário Itaú IFA:** *Especialista de investimentos* e *Assessor* são cargos distintos — o **Assessor auxilia os Especialistas** na operação e no acompanhamento das carteiras; nunca usar como sinônimos)
- `TX-09` Sem dados inventados (somente fatos confirmados por Israel)

### IA · Transparência de IA (4 códigos)
- `IA-01` Se IA foi usada no processo, nomear ferramenta, finalidade e onde ficou o julgamento humano
- `IA-02` Nenhum dado, citação ou resultado gerado por IA entra como real
- `IA-03` Texto revisado com IA segue `TX-01..09`; conteúdo factual vem de Israel
- `IA-04` Imagens geradas por IA não substituem telas reais; quando ilustrativas, ficam identificadas

### AP · Apresentação (7 códigos)
- `AP-01` Corpo 16–18px; altura de linha 1,5–1,75
- `AP-02` 65–75 caracteres por linha em prosa
- `AP-03` Uma família tipográfica, até dois pesos dominantes
- `AP-04` Imagens WebP/AVIF no tamanho de exibição
- `AP-05` LCP < 2,5 s
- `AP-06` Sem parallax ou animação pesada
- `AP-07` Contraste AA (`= A-04, A-07`)

### MB · Mobile (6 códigos)
- `MB-01` Coluna única abaixo de 720px
- `MB-02` Corpo `>= 16px` no mobile
- `MB-03` Hero sem estouro horizontal
- `MB-04` Menu hambúrguer ou compacto
- `MB-05` Legível do início ao fim
- `MB-06` Alvos `>= 24×24px` (`= A-20`; padrão do projeto `44–48px`)

### TH · Higiene Técnica (8 códigos)
- `TH-01` Domínio próprio *(ADR formal: exceção aceita para `github.io`)*
- `TH-02` SSL válido
- `TH-03` Nenhum 404
- `TH-04` Títulos de página específicos (`= A-13`)
- `TH-05` Meta descriptions e Open Graph apontando para produção
- `TH-06` CV em PDF com nome legível e link funcional
- `TH-07` Nenhuma ferramenta de edição exposta
- `TH-08` Revisão ortográfica integral

### A · Acessibilidade W3C WCAG 2.2 AA (28 códigos)
`A-01` (1.1.1) · `A-02` (1.3.1) · `A-03` (1.4.1) · `A-04` (1.4.3) · `A-05` (1.4.4) · `A-06` (1.4.10) · `A-07` (1.4.11) · `A-08` (1.4.12) · `A-09` (1.4.13) · `A-10` (2.1.1) · `A-11` (2.2.2) · `A-12` (2.4.1) · `A-13` (2.4.2) · `A-14` (2.4.3) · `A-15` (2.4.4) · `A-16` (2.4.6) · `A-17` (2.4.7) · `A-18` (2.4.11) · `A-19` (2.5.3) · `A-20` (2.5.8) · `A-21` (3.1.1) · `A-22` (3.2.3) · `A-23` (3.2.4) · `A-24` (3.2.6) · `A-25` (3.3.1/3.3.2) · `A-26` (3.3.7) · `A-27` (3.3.8) · `A-28` (4.1.2). Referência extra AAA: `2.4.13` (aparência do foco >= 2px, contraste >= 3:1).

### FG · Figma Estrutural (6 códigos)
- `FG-01` Auto layout em todos os nós filhos (`fills = []` em wrappers)
- `FG-02` Sem hug/fill incorreto, sem corte, sem overlay indevido
- `FG-03` Sem quebra de texto indevida (inclui "uma palavra por linha")
- `FG-04` Tokens e estilos de texto vinculados (sem valores soltos)
- `FG-05` Responsivo em `1280 / 768 / 390`
- `FG-06` Escala tipográfica do projeto: menor texto `12px` (Caption)

---

## 3. Resolução de Conflitos entre Fontes (Referência Permanente)
- **Quantidade de cases:** mínimo 3 (principal + sistema/influência + difícil), até 5.
- **Escalas de prontidão:** substituídas pela lista congelada (`Passa`/`Falha`/`N/A`); `/30` e `35 pontos` servem como referência.
- **Alvos de toque:** WCAG `24×24px` é o mínimo legal; o projeto adota **`44–48px`** como padrão.
- **Variação percentual:** informar valores de origem, `p.p.` e, se usar escore relativo (`novo/antigo − 1`), identificar explicitamente e preferir a forma conservadora em métricas "ruins".
- **Atribuição de negócio:** separar efeito direto de UX (a montante) de efeito de negócio (a jusante) e nomear fatores externos.
- **Amostras pequenas (ex.: 4–5 usuários):** relatar como sinal qualitativo, nunca como taxa percentual.

