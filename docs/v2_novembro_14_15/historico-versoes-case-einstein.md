# Histórico Consolidado de Versões: Case Albert Einstein

Este documento documenta lado a lado a evolução editorial do case Albert Einstein para fácil consulta e rastreabilidade.

---

## 1. Hero do Case (Abertura)

### Versão 1 (Original)
- **Título:** *Einstein · Laudos médicos*
- **Subtítulo:** *"Uma linguagem visual modular para laudos em diferentes canais."*
- **Leitura:** Muito resumida e genérica, não expressava o volume de exames nem o valor gerado para médico e paciente.

### Versão 2 (Intermediária — Jargão Teórico)
- **Título:** *Albert Einstein · Laudos de Medicina Diagnóstica*
- **Subtítulo:** *"Design system modular e arquitetura da informação para laudos clínicos e de imagem, unificando a leitura médica especializada e o autosserviço do paciente no digital e no papel."*
- **Leitura:** Excessivamente formal e acadêmica, soava como manual técnico.

### Versão 3 (Atual Definitiva — Aprovada) 🏆
- **Título:** *Albert Einstein · Laudos de Medicina Diagnóstica*
- **Headline:** *Clareza não é o mesmo que compreensão.*
- **Subtítulo:** **"Pesquisa e arquitetura de informação para estruturar mais de 80 exames distintos em uma linguagem modular previsível, facilitando a tomada de decisão médica e reduzindo a ansiedade de pacientes."**
- **Por que funciona:** Comunica escopo real (80+ exames), a metodologia (arquitetura modular previsível) e o impacto humano duplo (decisão médica rápida + redução de ansiedade do paciente).

---

## 2. Capítulo 1: O Desafio Inicial

### Versão 1 (Original)
> *"Pesquisa e proposta de uma linguagem visual modular para laudos, com hierarquia estável entre nome do exame, resultado, referência e contexto.*  
> *Laudos heterogêneos reuniam informações importantes em hierarquias variáveis. Pacientes precisavam localizar informações e levá-las à consulta; médicos precisavam cruzar resultados, referências, observações e contexto clínico."*  
> Métricas: `[4 médicos]` `[Questionário]` `[14]`

### Versão 2 (Intermediária — Jargão Teórico)
> *"Como transformar resultados analíticos densos em uma interface modular estável, compreensível para o paciente e clinicamente rigorosa para o médico?*  
> *Laudos hospitalares operam sob restrições severas: sistemas emissores legados, disparidade de dados entre especialidades e a necessidade de preservar o contexto diagnóstico. O projeto estabeleceu uma taxonomia visual padronizada que separa dados administrativos, parâmetros analíticos e notas clínicas em componentes reutilizáveis."*  
> Métricas: `[121 pacientes]` `[4 médicos]` `[14 famílias]`

### Versão 3 (Atual Definitiva — Aprovada) 🏆
> **"O objetivo central é clareza, compreensão e facilidade para interpretar resultados: apoiar a tomada de decisão médica com agilidade e permitir que o paciente entenda sua própria saúde sem ansiedade.**  
> *Em hospitais e laboratórios, cada exame costumava ter um formato diferente. Informações críticas ficavam dispersas: o paciente sentia insegurança ao não entender os valores de referência, e o médico perdia tempo buscando métodos e observações em partes separadas da folha."*  
> **Métricas Sincronizadas:**
> - **121:** pacientes responderam à pesquisa de hábitos de leitura
> - **4:** médicos especialistas entrevistados em profundidade
> - **14:** modelos padronizados cobrindo todo o acervo de exames

---

## 3. Capítulo 2: Cenário & Mandato vs. Desafio Prático & Regras

### Versão 1 (Original)
- **O cenário:** *"A experiência precisava funcionar no digital e no papel, em sistemas de fornecedores distintos e com recursos limitados para configurar templates. Em alguns cenários, o conteúdo era estruturado no Microsoft Word."*
- **O mandato:**
  - *"Dar hierarquia estável ao nome do exame, material, resultado e referência."*
  - *"Manter comentários, método e contexto clínico próximos."*
  - *"Respeitar variações de dados e restrições dos sistemas laudadores."*

### Versão 2 (Intermediária — Jargão Teórico)
- **Restrições técnicas e interoperabilidade:** *"O projeto demandava paridade estrutural entre a impressão física A4 e os canais digitais responsivos, operando sobre sistemas legados de emissão diagnóstica (LIS/PACS) com capacidade limitada de estilização..."*
- **Requisitos de arquitetura da informação:**
  - *"Ancoragem determinística: nome do exame, material biológico, resultado analítico..."*
  - *"Desacoplamento de metadados: isolamento de identificadores de amostra..."*
  - *"Tolerância dimensional: grid e tipografia dimensionados..."*

### Versão 3 (Atual Definitiva — Aprovada) 🏆
- **O desafio prático:** *"O mesmo laudo precisava funcionar no aplicativo do celular, na tela do consultório e impresso em preto e branco nas impressoras dos hospitais parceiros. Não adiantava criar um visual bonito que travasse os sistemas mais antigos ou ficasse ilegível no papel comum."*
- **As regras centrais do projeto:**
  - **Resultado e referência lado a lado:** o valor do exame e o intervalo considerado normal aparecem sempre juntos, na mesma linha visual.
  - **Cabeçalho limpo:** dados administrativos (como convênio, número da guia e carimbos) foram separados, deixando o foco total no resultado médico.
  - **Estrutura flexível:** o modelo aceita desde exames de sangue curtos de uma linha até relatórios longos de ressonância com laudo descritivo.

---

## 4. Capítulo 3: Pesquisa e Descoberta

### Versão 1 (Original)
> *"A descoberta reuniu quatro entrevistas médicas, questionário exploratório e análise documental. A análise cobriu mais de 80 exames distintos e 14 categorias de laudos; recortes menores representam subconjuntos do acervo."*

### Versão 2 (Intermediária — Jargão Teórico)
> *"A fase de Product Discovery integrou auditoria de inventário sobre mais de 80 exames clínicos e laboratoriais a entrevistas semiestruturadas com 4 médicos especialistas e pesquisa quantitativa com 121 pacientes..."*  
> - *"Mapeamento de protocolos de leitura sob fadiga cognitiva médica..."*  
> - *"Avaliação de compreensão e autonomia..."*  
> - *"Auditoria e contratos de dados..."*

### Versão 3 (Atual Definitiva — Aprovada) 🏆
> *"Para construir esse padrão, analisamos mais de 80 exames reais de diversas especialidades — de análises laboratoriais a exames de imagem. Descobrimos que, apesar de parecerem muito diferentes, todos podiam ser agrupados em apenas 14 tipos de modelos previsíveis."*
> - **Como o médico trabalha:** em uma consulta rápida ou no pronto-socorro, ele precisa bater o olho e identificar em 3 segundos se algum número está fora do padrão.
> - **Como o paciente lê:** termos técnicos e tabelas densas causam ansiedade. O paciente quer entender com clareza o que aquele resultado significa antes mesmo da consulta.
> - **Limitações dos sistemas:** mapeamos o tamanho dos textos e tabelas para garantir que nenhuma palavra ou número ficasse cortado em qualquer impressora.
> - **Callout:** *"Em saúde, um alinhamento confuso pode induzir a um diagnóstico errado. O resultado, a unidade e o intervalo de referência devem formar um bloco único e inconfundível, fácil de ler até no fim de um plantão cansativo."*
