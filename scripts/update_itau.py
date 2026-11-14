with open('site/src/pages/CasePages.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

old_itau_part = """  const data: CasePresentationData = {
    title: project.title,
    context: 'Itaú Unibanco · Plataforma íon for Advisors',
    headline: project.title,
    subtitle: project.subtitle,
    role: 'Product Designer (Assessoria e Operações B2B)',
    team: 'Equipe multidisciplinar (Design, Engenharia, Produto e Negócios)',
    scope: project.stage,
    kicker: caseSlug === 'registros-atendimento' ? 'Fintech · IA aplicada' : 'Fintech · Design de produto',
    hero: hero ? { ...hero, caption: hero.caption } : undefined,
    prevCase,
    nextCase,
    chapters: [
      {
        title: 'A história em 90 segundos.',
        content: (
          <div className="cp-summary">
            <p><strong>{project.subtitle}</strong></p>
            <p>{project.framing}</p>
          </div>
        ),
      },
      {
        title: 'Contexto e desafio.',
        content: (
          <>
            <p>{project.framing}</p>
            <div className="cp-note">
              <h3>Pergunta central de design</h3>
              <p>{project.question}</p>
            </div>
          </>
        ),
      },
      {
        title: 'Descoberta e recorte do projeto.',
        content: (
          <>
            <p>O relato e os materiais disponíveis delimitam o seguinte recorte:</p>
            <List items={project.verified} />
          </>
        ),
      },
      {
        title: 'Decisões conectadas ao problema.',
        content: (
          <ol className="cp-decisions">
            {project.decisions.map((d) => (
              <li key={d.title}>
                <h3>{d.title}</h3>
                <p>{d.description}</p>
              </li>
            ))}
          </ol>
        ),
      },
      {
        title: 'Estrutura da solução.',
        content: (
          <>
            <p>
              O recorte conecta as necessidades da operação às seguintes escolhas de interação:
            </p>
            <List items={project.demonstrated} />
            {gallery && (
              <div className="cp-gallery">
                {gallery.map((image) => (
                  <CaseFigure key={image.src} image={image} />
                ))}
              </div>
            )}
          </>
        ),
      },
      {
        title: 'Estágio, limites e continuidade.',
        content: (
          <>
            <div className="cp-note">
              <h3>Continuidade do projeto</h3>
              <p>{project.nextValidation}</p>
            </div>
            <div className="cp-appendix">
              <details open>
                <summary>Lacunas e limites declarados das evidências</summary>
                <div>
                  <p>
                    Para distinguir a proposta documentada de resultados ainda não demonstrados, este recorte mantém os seguintes limites:
                  </p>
                  <List items={project.missing} />
                </div>
              </details>
            </div>
          </>
        ),
      },
      {
        title: 'Evidências e créditos.',
        content: (
          <div className="cp-appendix">
            <details open>
              <summary>Fontes e rastreabilidade dos artefatos</summary>
              <div>
                <Sources project={caseSlug} />
                <List items={project.sources} />
              </div>
            </details>
            <details>
              <summary>Roteiro de defesa técnica em entrevista</summary>
              <div>
                <p>
                  Questões para aprofundar as decisões e o processo de trabalho:
                </p>
                <List items={project.interviewQuestions} />
              </div>
            </details>
          </div>
        ),
      },
    ],
  }"""

new_itau_part = """  const itauChapterTitles: Record<string, string[]> = {
    vencimentos: [
      'Visibilidade, urgência e atuação proativa sobre eventos de liquidez.',
      'Conciliar três contextos financeiros em uma lógica única de consulta.',
      'Evidências confirmadas nos arquivos de trabalho e handoff.',
      'Decisões de interface: busca, filtros e tabela com estados de atuação.',
      'Padrões de interação para gestão de liquidez em escala B2B.',
      'Estágio de documentação, handoff técnico e preparação para entrevista.',
      'Rastreabilidade dos artefatos, autoria e roteiro de defesa técnica.',
    ],
    'hub-liquidez': [
      'Visão unificada de liquidez consolidando prazos e disponibilidades financeiras.',
      'O desafio de prover previsibilidade de caixa sem sobrecarregar a mesa.',
      'Recorte da proposta e componentes validados na solução.',
      'Decisões de design: decomposição temporal, saldos e ações em lote.',
      'Estrutura visual da mesa de liquidez e componentes modulares.',
      'Limites do protótipo e próximos passos de homologação.',
      'Rastreabilidade documental e roteiro de defesa técnica.',
    ],
    movimentacoes: [
      'Transparência de lançamentos e extrato operacional para assessores.',
      'Reduzir tempo de conciliação financeira entre cliente e mesa de assessoria.',
      'Discovery de arquitetura e alternativas exploradas para o extrato.',
      'Decisões de arquitetura: agrupamento temporal e detalhe de lançamentos.',
      'Padrões de consulta e granularidade de lançamentos financeiros.',
      'Estágio de validação técnica e integração com sistemas legados.',
      'Rastreabilidade dos artefatos e roteiro de defesa técnica.',
    ],
    campanhas: [
      'Orquestração de ações comerciais sem perda de contexto operacional.',
      'Transformar campanhas de marketing em fluxos acionáveis para assessoria.',
      'Mapeamento de esteira operacional e regras de conversão.',
      'Decisões de interface: priorização por impacto e conversão em lote.',
      'Screenflow de estados e componentes de acompanhamento de metas.',
      'Limites de implementação e métricas de conversão de campanha.',
      'Rastreabilidade dos arquivos de handoff e roteiro de defesa técnica.',
    ],
    'registros-atendimento': [
      'Registro estruturado de reuniões e inteligência operacional com IA.',
      'Automatizar a síntese de conversas sem comprometer o sigilo bancário.',
      'Mapeamento de momentos da reunião e extração de pendências.',
      'Decisões de interação: revisão humana, tags automáticas e confirmação.',
      'Fluxo de escuta ativa, sumarização e despacho de tarefas.',
      'Estágio do piloto de IA, conformidade e limites de modelo.',
      'Rastreabilidade técnica e roteiro de defesa de produto.',
    ],
  }

  const titles = itauChapterTitles[caseSlug] || [
    project.subtitle,
    'Contexto e desafio da operação financeira.',
    'Evidências e recorte de discovery.',
    'Decisões de interface e arquitetura de dados.',
    'Estrutura e componentes da solução.',
    'Estágio de validação e limites do recorte.',
    'Rastreabilidade e governança técnica.',
  ]

  const data: CasePresentationData = {
    title: project.title,
    context: 'Itaú Unibanco · Plataforma íon for Advisors',
    headline: project.title,
    subtitle: project.subtitle,
    role: 'Product Designer (Assessoria e Operações B2B)',
    team: 'Equipe multidisciplinar (Design, Engenharia, Produto e Negócios)',
    scope: project.stage,
    kicker: caseSlug === 'registros-atendimento' ? 'Fintech · IA aplicada' : 'Fintech · Design de produto',
    hero: hero ? { ...hero, caption: hero.caption } : undefined,
    prevCase,
    nextCase,
    chapters: [
      {
        title: titles[0],
        content: (
          <div className="cp-summary">
            <p><strong>{project.subtitle}</strong></p>
            <p>
              Estruturação e entrega de soluções de alta densidade analítica para a mesa de assessoria de investimentos,
              priorizando velocidade de decisão, clareza de dados patrimoniais e continuidade operacional sem fricção.
            </p>
          </div>
        ),
      },
      {
        title: titles[1],
        content: (
          <>
            <p>{project.framing}</p>
            <div className="cp-note">
              <h3>Pergunta central de design</h3>
              <p>{project.question}</p>
            </div>
          </>
        ),
      },
      {
        title: titles[2],
        content: (
          <>
            <p>O relato e os materiais disponíveis delimitam o seguinte recorte auditado:</p>
            <List items={project.verified} />
          </>
        ),
      },
      {
        title: titles[3],
        content: (
          <ol className="cp-decisions">
            {project.decisions.map((d) => (
              <li key={d.title}>
                <h3>{d.title}</h3>
                <p>{d.description}</p>
              </li>
            ))}
          </ol>
        ),
      },
      {
        title: titles[4],
        content: (
          <>
            <p>
              O recorte conecta as necessidades da operação às seguintes escolhas de interação:
            </p>
            <List items={project.demonstrated} />
            {gallery && (
              <div className="cp-gallery">
                {gallery.map((image) => (
                  <CaseFigure key={image.src} image={image} />
                ))}
              </div>
            )}
          </>
        ),
      },
      {
        title: titles[5],
        content: (
          <>
            <div className="cp-note">
              <h3>Continuidade do projeto</h3>
              <p>{project.nextValidation}</p>
            </div>
            <div className="cp-appendix">
              <details open>
                <summary>Lacunas e limites declarados das evidências</summary>
                <div>
                  <p>
                    Para distinguir a proposta documentada de resultados ainda não demonstrados, este recorte mantém os seguintes limites:
                  </p>
                  <List items={project.missing} />
                </div>
              </details>
            </div>
          </>
        ),
      },
      {
        title: titles[6],
        content: (
          <div className="cp-appendix">
            <details open>
              <summary>Fontes e rastreabilidade dos artefatos</summary>
              <div>
                <Sources project={caseSlug} />
                <List items={project.sources} />
              </div>
            </details>
            <details>
              <summary>Roteiro de defesa técnica em entrevista</summary>
              <div>
                <p>
                  Questões para aprofundar as decisões e o processo de trabalho:
                </p>
                <List items={project.interviewQuestions} />
              </div>
            </details>
          </div>
        ),
      },
    ],
  }"""

if old_itau_part in content:
    content = content.replace(old_itau_part, new_itau_part)
    with open('site/src/pages/CasePages.tsx', 'w', encoding='utf-8') as f:
        f.write(content)
    print("SUCCESS: Updated ItauPresentation!")
else:
    print("ERROR: old_itau_part not found!")

