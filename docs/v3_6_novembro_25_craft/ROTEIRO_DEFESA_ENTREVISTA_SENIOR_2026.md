# Roteiro de Defesa Oral de Portfólio & Entrevista Sênior/Lead (V4.4.0)

> **Proveniência & Rastreabilidade**
> - **IA / Plataforma:** Antigravity — Google DeepMind
> - **Data de criação:** 2026-11-27
> - **Última atualização:** 2026-11-27
> - **Conversa de origem:** [66417f41-f841-4d50-a701-e678302e3ec2](conversation://66417f41-f841-4d50-a701-e678302e3ec2)
> - **Base normativa:** [UX_INTERVIEW_AND_CHALLENGE_PLAYBOOK_2026.md](UX_INTERVIEW_AND_CHALLENGE_PLAYBOOK_2026.md) + `portfolio-banca` (Papel 7 · Entrevistador) + fatos verificados `V4.4.0` (`TX-09`).

---

## 1. Mapa de Tempo — Entrevista de 45 min (ou 60 min)

> **Regra de ouro:** fale por **75% do tempo** de cada bloco para abrir espaço natural para perguntas da banca (*Story Triangle*) sem correr no final.

| Bloco | Slot 45 min | Slot 60 min | Objetivo |
| :--- | :---: | :---: | :--- |
| **Abertura** | `0–3 min` | `0–3 min` | Posicionamento em 3 frases + por que escolheu estes 2 cases. |
| **Case 1 · Hospital Albert Einstein** | `3–18 min` | `3–23 min` | Âncora de **pesquisa + sistema modular + entrega em produção + rigor de dados**. |
| **Case 2 · Itaú IFA (Hub de Liquidez + IA)** | `18–31 min` | `23–38 min` | Âncora de **arquitetura financeira densa + contratos de dados + governança de IA (HITL)**. |
| **Perguntas da Banca (Q&A)** | `31–40 min` | `38–52 min` | Defesa de trade-offs, desacordo construtivo e colaboração com PM/Engenharia. |
| **Suas Perguntas Estratégicas** | `40–45 min` | `52–60 min` | 2–3 perguntas que mostram leitura de negócio e maturidade de Senior/Lead. |

---

## 2. Abertura de 90 Segundos (3 Frases)

> *"Sou Senior Product Designer com mais de 15 anos de experiência em produtos digitais para saúde, finanças, telecom e energia, atuando de ponta a ponta em discovery, arquitetura da informação e design systems junto a Produto e Engenharia.*
> *No meu ciclo mais recente no Itaú Unibanco, atuei na plataforma íon for Advisors estruturando fluxos operacionais e contratos de dados para especialistas de investimentos e os assessores que os auxiliam.*
> *Para hoje, escolhi dois recortes complementares: o **padrão modular de laudos do Hospital Albert Einstein**, onde liderei pesquisa e sistemas até a implantação em produção, e o **Hub de Liquidez no Itaú IFA**, focado em hierarquia financeira densa e decisões de arquitetura."*

*(Dica: pergunte antes de abrir o Case 1 — **"Vocês preferem que eu aprofunde mais em pesquisa e governança ou em decisões de interface e Design System?"** — isso sinaliza senioridade imediata.)*

---

## 3. Roteiro Oral — Case 1: Hospital Israelita Albert Einstein (12–15 min)

### 1) Contexto e por que era difícil (`2 min`)
- **Tela aberta:** Hero Bento `v17` + Cap. 1 (*Tese Clínica*).
- **Fala:** *"Em 2022, atuei como UX Lead pela Foursys no projeto de Consumo de Resultados do Einstein. Laboratórios e hospitais parceiros emitiam exames em layouts diferentes — tabelas densas, textos corridos e rodapés misturados com o resultado. O maior desafio não era visual: o mesmo laudo precisava funcionar no portal web, no celular e em **impressão preto e branco em consultório**, além de conviver com sistemas laudadores legados e templates em Microsoft Word."*

### 2) Pesquisa e achado que redirecionou o projeto (`2 min`)
- **Tela aberta:** Cap. 1 métricas (`121` pacientes · `4` médicos · `14` entregáveis) + Cap. 2 Antes/Depois `v03`.
- **Fala:** *"Triangulamos 4 frentes: questionário anonimizado com 121 pacientes (LGPD), 4 entrevistas semiestruturadas com médicos especialistas, análise documental de mais de 80 exames reais e restrições técnicas dos sistemas laudadores. O achado central foi uma tensão direta: **pacientes buscavam saber rapidamente se estavam bem**, enquanto **médicos exigiam que o resultado não induzisse autodiagnóstico fora da consulta**."*

### 3) As 3 decisões de design + trade-offs (`5 min`)
- **Decisão 1 — Sinalização sem autodiagnóstico (Cap. 2):**
  - *Opções:* selos coloridos de *"normal/alterado"* vs. cor neutra + ícone geométrico (`✓`, `▲`, `▼`) + referência ao lado do valor.
  - *Escolha & custo aceito:* com os 4 médicos, descartamos selos interpretativos. **Aceitamos sacrificar uma leitura binária instantânea** para reduzir risco clínico e manter a sinalização legível em impressão P&B e daltonismo.
- **Decisão 2 — Taxonomia de 3 macroáreas vs. template por exame (Cap. 3):**
  - *Escolha & custo aceito:* em vez de manter dezenas de layouts por especialidade, padronizamos **3 macroáreas fixas** (cabeçalho, resultado/referência e metadados) nos componentes `examTitle` e `dataField` do Design System Zera 1.0 (mostrar Bento Zera 1.0). **Custo aceito:** menor liberdade de diagramação sob medida em exames de exceção para viabilizar escala em `80+` exames.
- **Decisão 3 — Compatibilidade com Word/legado vs. redesenho do portal (Cap. 4):**
  - *Escolha & custo aceito:* com a engenharia, priorizamos compatibilidade com cabeçalho/rodapé comuns e geração de PDF/Word, **adiando o redesenho completo do portal** para viabilizar adoção multicanal real (mostrar prancha 3 Canais `v13`).

### 4) Validação honesta, produção e o que eu reverteria (`3 min`)
- **Tela aberta:** Cap. 6 métricas (`81,6%`, `77,8%`, `58,8%`, `56,2%`).
- **Fala:** *"Nos testes da proposta v3, **81,6%** reconheceram o laudo de imediato e **77,8%** focaram primeiro em exame, resultado e referência — mas só **56,2%** interpretaram a condição clínica sozinhos. Essa diferença de **21,6 pontos percentuais** provou algo valioso: clareza de interface melhora localização de dados, mas não substitui o médico — validando nossa recusa aos selos automáticos.*
  *A proposta v3 (EN-1 a EN-14) chegou a ser implantada em produção; como encerrei minha atuação após a implantação, não tenho linha de base do legado nem telemetria pós-lançamento.*
  *O que eu reverteria hoje? Eu não consolidaria os componentes digitais antes de testar quebras de página na geração de PDF — trazer a engenharia de PDF desde a primeira semana teria evitado ajustes concentrados na reta final."*

---

## 4. Roteiro Oral — Case 2: Itaú Unibanco · Hub de Liquidez & Ecossistema IFA (10–12 min)

### 1) Contexto e papel (`2 min`)
- **Tela aberta:** Hero Bento `v16` + Cap. 1 (*Gargalo Operacional*).
- **Fala:** *"Entre 2024 e 2026, atuei como Senior Product Designer no Itaú Unibanco, na plataforma íon for Advisors (IFA), usada por **especialistas de investimentos e pelos assessores que os auxiliam** no acompanhamento de carteiras. Trabalhei em 5 módulos — hoje aprofundo o **Hub de Liquidez e Oportunidades**.*
  *O problema operacional era concreto: antes de abordar um cliente, especialistas e assessores precisavam cruzar múltiplas abas para conciliar dinheiro já disponível em conta, recursos de Open Finance e liquidez projetada."*

### 2) As 3 decisões de arquitetura (`5 min`)
- **Tela aberta:** Cap. 2 (*3 Decisões de Arquitetura*) + Cap. 3 (`itau-hub-liquidez-solucao.webp`).
- **Decisão 1 — Separar posição atual, variação prevista e projeção:**
  - *Trade-off:* um totalizador único economizava espaço no cabeçalho, mas misturava dinheiro real com projeção futura. **Aceitamos ocupar mais espaço no resumo** para impedir que recursos futuros fossem lidos como disponibilidade imediata antes de ligar para o cliente.
- **Decisão 2 — Acoplar a janela temporal (`Fim do dia`, `7 dias`, `30 dias`) ao indicador projetado:**
  - *Trade-off:* **limitamos a comparação simultânea de múltiplas janelas** na mesma tela para impedir que o usuário lesse um valor fora do horizonte filtrado.
- **Decisão 3 — Manter origem (`Itaú` vs. `Open Finance`) explícita na tabela:**
  - *Trade-off:* **aceitamos maior densidade de colunas** para que a equipe conseguisse filtrar por instituição e justificar a abordagem ao cliente sem sair da tela.

### 3) Escopo, transparência e gancho para IA (`3 min`)
- **Tela aberta:** Cap. 4 (*Salvaguardas & Aprendizado*) + menção rápida a *Registros de Atendimento* (abrir só se perguntarem sobre IA).
- **Fala:** *"Deixamos fora da primeira camada fórmulas internas de reconciliação que dependiam de homologação do domínio. Entregamos a interface documentada da solução no Design System (iDS), sem métricas de produção publicadas neste recorte.*
  *O que eu reverteria hoje? Eu explicitaria na própria linha da tabela o critério que colocou aquele cliente no topo da fila — ocultar essa regra aumenta a dependência de interpretação antes do contato.*
  *(Gancho opcional de IA): No mesmo ecossistema, também desenhei **Registros de Atendimento com IA**, aproximando os 5 últimos resumos e impondo confirmação humana obrigatória (**Human-in-the-Loop**) antes de gravar qualquer nota no prontuário bancário."*

---

## 5. Cartões de Pivô Rápido (se a banca pedir outro recorte)

- **Se pedirem Mobile / E-commerce / Desacordo com Comercial ➔ Claro Brasil (`/cases/claro-ativacao-simplificada`):**
  - *Gancho em 20s:* 22 jornadas (NET, Claro, Embratel) unificadas em 5 etapas desktop + mobile; desacordo construtivo com lideranças comerciais (queriam tela única com menos cliques vs. etapas progressivas + resumo financeiro lateral para evitar erro contratual), validado em sessões práticas com operadores.
- **Se pedirem Service Design / Alinhamento Executivo ➔ Neoenergia (`/cases/neoenergia-conexao-digital`):**
  - *Gancho em 20s:* P&D ANEEL pela EY em consórcio com a Livework; 4 distribuidoras (34M habitantes, 13,9M clientes), 11 canais, 5 Service Blueprints e 118 ideias aprovadas como baseline; desacordo com diretorias regionais resolvido com arquitetura multi-tenant em vez de 4 portais isolados.

---

## 6. Respostas Calibradas às 6 Perguntas Mais Difíceis da Banca

1. ***"Por que você não tem métricas pós-lançamento no Einstein ou no Itaú?"***
   - *Resposta direta (sem postura defensiva):* *"No Einstein, a proposta v3 foi implantada em produção, mas meu ciclo pela Foursys encerrou após a entrega e não tive acesso à telemetria pós-lançamento nem houve baseline do legado. Por isso, mostro exatamente o que medimos — a pesquisa com 121 pacientes e os testes v3 que revelaram o gap de 21,6 p.p. entre foco visual e interpretação — e explico que protocolo eu exigiria hoje. No Itaú, por sigilo bancário e recorte do ciclo, apresento a arquitetura, contratos de dados e decisões validados com o time sem inventar números."*
2. ***"Me dê um exemplo de desacordo forte com negócio ou engenharia."***
   - *3 opções prontas:* (a) **Claro:** comercial pediu tela única para reduzir cliques ➔ levei operadores em sessão prática e fechei etapas progressivas com resumo financeiro lateral; (b) **Neoenergia:** diretorias regionais pediram 4 portais independentes ➔ cruzei os 5 Service Blueprints com custo de manutenção e defendi base multi-tenant com temas; (c) **Einstein:** pressão por selo visual simples *"normal/alterado"* ➔ alinhei com os 4 médicos o risco clínico e adotamos redundância ícone + referência.
3. ***"Qual foi a decisão mais errada ou que você mudaria hoje?"***
   - *Einstein:* definir componentes digitais antes de testar quebras de página em PDF com a engenharia. *Claro:* fechar V.2 sem linha de base de tempo/erro em loja. *Itaú Hub:* não explicitar na linha da tabela o critério de ranqueamento da fila.
4. ***"Como você usa IA no seu fluxo de trabalho sem perder rigor?"***
   - *"Uso IA para acelerar síntese de notas, exploração de variações e prototipagem rápida, mas mantenho julgamento de produto, validação de evidências e revisão técnica 100% humanos — o mesmo princípio de Human-in-the-Loop que apliquei nos Registros de Atendimento do Itaú."*
5. ***"Qual foi exatamente a sua autoria individual vs. trabalho da equipe?"***
   - Sempre responder no padrão **Conduzi × Contribuí** já gravado nos 4 cases (ex.: Einstein: conduzi pesquisa, taxonomia, componentes e critique; validei terminologia com 4 médicos e limites técnicos com engenharia).
6. ***"Como você lida com Design Systems e acessibilidade sob prazo curto?"***
   - *"Trato acessibilidade e tokens como restrição de arquitetura desde o dia 1, não como checklist de fim de sprint — como no Zera 1.0 (base 8px + ícones redundantes à cor para P&B) e no iDS do Itaú (estados vazios, erro e carregamento especificados junto da tela principal)."*

---

## 7. Suas 4 Perguntas Estratégicas para Fazer à Banca (escolha 2–3)

1. *"Qual é hoje o maior gargalo entre descoberta, decisão de produto e entrega em engenharia no time em que essa vaga vai atuar?"*
2. *"Nos primeiros 90 dias, qual resultado concreto faria vocês olharem para trás e dizerem que essa contratação deu certo?"*
3. *"Como o time decide hoje quando criar um padrão novo no Design System versus adaptar um fluxo local por prazo de negócio?"*
4. *"Se vocês estão incorporando IA no produto, onde hoje fica a fronteira entre automação e revisão humana nos fluxos críticos?"*
