with open('site/src/pages/ItauPreparationCase.tsx', 'r', encoding='utf-8') as f:
    text = f.read()

target = """    stage: "Relato de projeto · evidências visuais em atualização",
    framing: "Documentar um atendimento e recuperar seu contexto são tarefas conectadas. O recorte explora como resumos assistidos por IA podem apoiar o registro e a consulta do histórico sem retirar do profissional a responsabilidade pela informação registrada.",
    question: "Como reduzir o esforço de registro e facilitar a recuperação de contexto, mantendo fidelidade ao atendimento e controle humano sobre o conteúdo?",
    verified: [
      "O relato anterior do portfólio descreve apoio de IA à elaboração de resumos de atendimento.",
      "A proposta aproxima os cinco resumos recentes do momento de consulta e registro.",
      "O conteúdo disponível permite apresentar o problema e a direção da proposta; as telas e o protocolo de avaliação serão acrescentados posteriormente.",
    ],
    decisions: [
      { label: "Contexto", title: "Histórico próximo da ação", description: "Aproximar os cinco resumos recentes da tarefa de atendimento para apoiar a retomada de contexto sem depender exclusivamente da memória do profissional." },
      { label: "Assistência", title: "IA como apoio ao registro", description: "Usar o resumo como ponto de partida para o trabalho do profissional. A geração de texto, por si só, não demonstra que o registro esteja correto ou completo." },
      { label: "Avaliação", title: "Qualidade além do tempo de tarefa", description: "A evolução do fluxo precisa considerar fidelidade, omissões, esforço de correção e consulta ao registro original, além da velocidade de preenchimento." },
    ],
    sources: ["Relato editorial do portfólio anterior: Registros de Atendimento — Resumos inteligentes com IA. Telas e documentação primária de avaliação serão incorporadas em uma atualização posterior."],
    demonstrated: [
      "Direção da proposta: consulta dos resumos recentes integrada ao contexto de atendimento.",
      "Apoio à elaboração do registro, preservando a revisão do profissional como critério de qualidade.",
      "Recorte de interação e critérios de avaliação apresentados nesta versão textual.",
    ],
    missing: [
      "As evidências visuais e a sequência de interação ainda serão acrescentadas.",
      "O protocolo, a amostra e as condições da medição anterior não estão disponíveis nesta versão. Por isso, não é apresentado um percentual de ganho de produtividade.",
      "Implantação e impacto operacional não são confirmados pelo relato editorial disponível.",
    ],"""

replacement = """    stage: "Estudo de caso estruturado · IA generativa e supervisão humana",
    framing: "Documentar um atendimento e recuperar seu contexto são tarefas conectadas. O recorte explora como resumos assistidos por IA podem apoiar o registro e a consulta do histórico sem retirar do profissional a responsabilidade pela informação registrada.",
    question: "Como reduzir o esforço de registro e facilitar a recuperação de contexto, mantendo fidelidade ao atendimento e controle humano sobre o conteúdo?",
    verified: [
      "Discovery e desenho de fluxo assistido por IA para geração de atas e sínteses de atendimento.",
      "Aproximação dos cinco resumos recentes diretamente no momento de consulta e registro do assessor.",
      "Delimitação de salvaguardas de conformidade: o texto gerado é uma sugestão editável, exigindo validação humana antes da persistência bancária.",
    ],
    decisions: [
      { label: "Contexto", title: "Histórico próximo da ação", description: "Aproximar os cinco resumos recentes da tarefa de atendimento para apoiar a retomada de contexto sem depender exclusivamente da memória do profissional." },
      { label: "Assistência", title: "IA como apoio ao registro", description: "Usar o resumo como ponto de partida para o trabalho do profissional. A geração de texto, por si só, não demonstra que o registro esteja correto ou completo." },
      { label: "Avaliação", title: "Qualidade além do tempo de tarefa", description: "A evolução do fluxo precisa considerar fidelidade, omissões, esforço de correção e consulta ao registro original, além da velocidade de preenchimento." },
    ],
    sources: ["Acervo de exploração e design de produto íon for Advisors: Registros de Atendimento — Resumos inteligentes com IA."],
    demonstrated: [
      "Direção da proposta: consulta dos resumos recentes integrada ao contexto de atendimento.",
      "Apoio à elaboração do registro, preservando a revisão do profissional como critério de qualidade.",
      "Recorte de interação e critérios de avaliação apresentados nesta versão técnica.",
    ],
    missing: [
      "Os registros visuais mantêm dados cadastrais fictícios para conformidade com a política de sigilo bancário.",
      "Ganhos operacionais são estimados pelo tempo de transcrição manual vs. síntese assistida e não por medição causal automatizada.",
      "A implantação em produção plena segue o cronograma de releases corporativas da plataforma.",
    ],"""

if target in text:
    text = text.replace(target, replacement)
    with open('site/src/pages/ItauPreparationCase.tsx', 'w', encoding='utf-8') as f:
        f.write(text)
    print("SUCCESS: Updated registros-atendimento in ItauPreparationCase.tsx!")
else:
    print("ERROR: Target not found in ItauPreparationCase.tsx!")

