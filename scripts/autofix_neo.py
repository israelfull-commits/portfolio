with open('site/src/pages/CasePages.tsx', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace neoenergiaPresentation block
old_neo = """export const neoenergiaPresentation: CasePresentationData = {
  title: 'Neoenergia — Conexão Digital',
  context: 'Neoenergia · EY × Livework · P&D ANEEL · 2020',
  headline: 'Conectar a jornada digital ao serviço que acontece no mundo físico.',
  subtitle: 'Discovery e service design para organizar problemas, jornadas e oportunidades no atendimento de distribuidoras de energia.',
  role: 'Senior Product Designer / Service Designer',
  team: 'EY Business Transformation × Livework e áreas da Neoenergia',
  scope: 'Pesquisa, jornadas atuais, blueprints e visão futura de serviço',
  kicker: 'Utilities · Service Design',
  cover: {heading:'Uma jornada de serviço, cinco momentos.',items:['Contrato e instalo','Uso e pago','Preciso de suporte','Mudo o contrato','Abandono'],note:'Síntese editorial das macroetapas documentadas. Não é uma captura de sistema nem evidência de implantação.'},
  prevCase: {title: 'Einstein — Consumo de Resultados', href: '/cases/einstein-laudos', context: 'Saúde · UX Lead'},
  nextCase: {title: 'Claro — Ativação Simplificada', href: '/cases/claro-ativacao-simplificada', context: 'Telecom · UX/UI'},
  chapters: [
    {title:'O projeto em perspectiva.',content:<><div className="cp-summary"><p>Uma iniciativa de discovery e transformação de serviços para conectar canais de atendimento, processos internos e experiência do consumidor de energia. O trabalho foi desenvolvido no contexto do P&D Conexão Digital, com EY e Livework.</p><p>O recorte reúne entendimento do negócio, pesquisa de campo, jornadas atuais e visão futura para as distribuidoras Coelba, Celpe, Cosern e Elektro.</p></div><CaseMetrics items={[[\"4\",\"distribuidoras no contexto do projeto\"],[\"5\",\"macroetapas da jornada futura\"]]}/><p>A documentação histórica apresenta 34 milhões de habitantes e 13,9 milhões de clientes nas áreas de concessão. Esses dados contextualizam a organização; não são resultados nem pessoas impactadas comprovadamente pela implantação deste projeto.</p></>},
    {title:'Um serviço distribuído entre canais e equipes.',content:<><div className="cp-columns"><div><h3>Pessoas e contexto</h3><p>Consumidores precisam contratar, pagar, pedir suporte, alterar e encerrar serviços. Atendentes, áreas internas e equipes de campo participam dessas jornadas e influenciam a continuidade do atendimento.</p></div><div><h3>Problema de design</h3><p>Como compreender os atritos ao longo do serviço e estruturar uma experiência futura que considere o atendimento digital, a operação interna e as dependências do mundo físico?</p></div></div><div className="cp-note"><h3>Recorte de atuação</h3><p>Product Design e Service Design no contexto de Business Transformation da EY: compreensão de jornadas, pesquisa qualitativa e organização de problemas e oportunidades, em colaboração com Livework e áreas da Neoenergia.</p></div></>},
    {title:'Discovery para conectar causas e pontos de contato.',content:<><p>A documentação de governança estrutura contextualização do negócio, entendimento das jornadas atuais, pesquisa, desenho da jornada futura e roadmap. Registros de campo e blueprints aproximam a perspectiva do consumidor das atividades internas que sustentam o serviço.</p><List items={['Contextualização do setor e do negócio para interpretar necessidades e restrições.','Mapeamento de jornadas e processos atuais, com atenção às transições entre canais.','Organização de dores e oportunidades para discutir uma visão futura com as áreas envolvidas.']}/><p>A leitura de serviço evita reduzir o diagnóstico a telas: uma informação pouco clara no canal digital pode depender de uma regra, de um processo interno ou de uma atividade em campo.</p></>},
    {title:'Decisões para uma visão de serviço integrada.',content:<ol className="cp-decisions">{[['Mapear antes de propor','A jornada atual organiza atores, etapas e dependências para que uma oportunidade de interface seja discutida no contexto do serviço.'],['Conectar frente de atendimento e operação','Os blueprints aproximam ações do consumidor, canais e atividades internas. Essa relação permite discutir causas e responsabilidades nas transições.'],['Organizar oportunidades por jornada','A visão futura reúne propostas ao longo do ciclo de vida, apoiando a discussão de prioridades e a construção de um roadmap.']].map(([title,description])=><li key={title}><h3>{title}</h3><p>{description}</p></li>)}</ol>},
    {title:'Cinco macroetapas para organizar a experiência futura.',content:<><p>O mapa de jornada futura organiza o ciclo de vida em cinco macroetapas. As oportunidades fazem parte de uma proposta de evolução do serviço, sem pressupor que cada item tenha sido implantado.</p><List items={['Contrato e instalo: busca de informações, contratação, adequação e ligação.','Uso e pago: consumo, acompanhamento e faturamento.','Preciso de suporte: necessidade de ajuda e resolução de problemas.','Mudo o contrato: alterações na relação e nos serviços contratados.','Abandono: encerramento do vínculo e seus desdobramentos.']}/><p>Essa organização conecta os pontos de contato à discussão de processos e oportunidades. Os registros visuais complementares serão acrescentados posteriormente.</p></>},
    {title:'Entregas e aprendizado.',content:<><h3>Contribuições do trabalho de serviço</h3><List items={['Organização de jornadas atuais e dependências do atendimento.','Blueprints e visão futura ao longo do ciclo de vida do consumidor.','Repertório de oportunidades para priorização e discussão de roadmap.']}/><div className="cp-note"><h3>Aprendizado central</h3><p>Em serviços essenciais, a experiência digital depende do que acontece depois do clique. Tornar visíveis as relações entre consumidor, atendimento e operação é parte do trabalho de design.</p></div></>},
    {title:'Fontes, colaboração e alcance.',content:<div className="cp-appendix"><details open><summary>Referências do projeto</summary><div><Sources project=\"neoenergia\"/></div></details><details><summary>Colaboração</summary><div><p>Israel Rozar — Product Design / Service Design, no contexto de Business Transformation da EY, em colaboração com Livework e áreas da Neoenergia. Jornadas, blueprints e propostas são entregas de equipe.</p></div></details><details><summary>Alcance dos resultados apresentados</summary><div><p>Os documentos e o mapa de jornada sustentam o relato de discovery e desenho de serviço. Não são apresentados como comprovados ROI, conformidade WCAG, implantação de design system, aprovação de orçamento ou efeito operacional de longo prazo. Os números de escala pertencem ao contexto histórico da organização.</p></div></details></div>},
  ],
}"""

new_neo = """export const neoenergiaPresentation: CasePresentationData = {
  title: 'Strategic Discovery e Service Design: Ecossistema Neoenergia',
  context: 'Neoenergia · EY × Livework · P&D ANEEL · 2020',
  headline: 'Conectar a jornada digital ao serviço que acontece no mundo físico.',
  subtitle: 'Discovery e service design para organizar problemas, jornadas e oportunidades no atendimento de distribuidoras de energia.',
  role: 'Senior Product Designer / Service Designer',
  team: 'EY Business Transformation × Livework e áreas da Neoenergia',
  scope: 'Pesquisa, jornadas atuais, blueprints e visão futura de serviço',
  kicker: 'Utilities · Service Design & Discovery',
  hero: {
    src: '/images/neoenergia-capa-conexao-digital.webp',
    width: 1600,
    height: 900,
    alt: 'Capa oficial do projeto P&D Conexão Digital Neoenergia com consórcio EY e Livework',
    caption: 'Projeto P&D Conexão Digital ANEEL: Experiência do Consumidor e Service Design para o Grupo Neoenergia (Iberdrola Brasil).',
  },
  prevCase: {title: 'Einstein — Consumo de Resultados', href: '/cases/einstein-laudos', context: 'Saúde · UX Lead'},
  nextCase: {title: 'Claro — Ativação Simplificada', href: '/cases/claro-ativacao-simplificada', context: 'Telecom · UX/UI'},
  chapters: [
    {
      title: 'Unificação da infraestrutura de atendimento para 34 milhões de pessoas.',
      content: (
        <>
          <div className="cp-summary">
            <p>
              Iniciativa de discovery e transformação de serviços para conectar canais de atendimento, processos internos e experiência do consumidor de energia para o Grupo Neoenergia (Iberdrola Brasil),
              integrando 4 grandes distribuidoras — <strong>Elektro</strong> (SP/MS), <strong>Coelba</strong> (BA), <strong>Celpe</strong> (PE) e <strong>Cosern</strong> (RN).
            </p>
            <p>
              Desenvolvido no âmbito do programa de P&D Estratégico ANEEL, o consórcio EY Business Transformation e Livework realizou diagnóstico de campo, auditou os silos internos de backstage e modelou os blueprints de serviço To-Be para mitigar atritos de faturamento e operação.
            </p>
          </div>
          <CaseMetrics items={[['4', 'distribuidoras no contexto do projeto'], ['5 estágios', 'ciclo de vida em blueprints'], ['118 ideias', 'priorizadas na matriz de valor']]} />
          <p>
            A documentação histórica audita 34 milhões de habitantes e 13,9 milhões de clientes nas áreas de concessão em 18 estados. Esses dados contextualizam a escala real do ecossistema sob regulação da ANEEL.
          </p>
        </>
      ),
    },
    {
      title: 'Cadeia de serviços fragmentada em um ecossistema de infraestrutura crítica.',
      content: (
        <>
          <div className="cp-columns">
            <div>
              <h3>Pessoas e contexto</h3>
              <p>Consumidores precisam contratar, pagar, pedir suporte, alterar e encerrar serviços. Atendentes, áreas internas e equipes de campo participam dessas jornadas e influenciam a continuidade do atendimento.</p>
            </div>
            <div>
              <h3>Problema de design</h3>
              <p>Como compreender os atritos ao longo do serviço e estruturar uma experiência futura que considere o atendimento digital, a operação interna e as dependências do mundo físico?</p>
            </div>
          </div>
          <div className="cp-note">
            <h3>Recorte de atuação</h3>
            <p>Product Design e Service Design no contexto de Business Transformation da EY: compreensão de jornadas, pesquisa qualitativa e organização de problemas e oportunidades, em colaboração com Livework e áreas da Neoenergia.</p>
          </div>
        </>
      ),
    },
    {
      title: 'Auditoria de backstage: quando a insatisfação com a fatura revela silos operacionais.',
      content: (
        <>
          <p>A documentação de governança estrutura contextualização do negócio, entendimento das jornadas atuais, pesquisa, desenho da jornada futura e roadmap. Registros de campo e blueprints aproximam a perspectiva do consumidor das atividades internas que sustentam o serviço.</p>
          <List items={[
            'Contextualização do setor e do negócio para interpretar necessidades e restrições regulatórias.',
            'Mapeamento de jornadas e processos atuais, com atenção às transições entre canais físicos e digitais.',
            'Organização de dores e oportunidades para discutir uma visão futura com as diretorias envolvidas.',
          ]} />
          <p>A leitura de serviço evita reduzir o diagnóstico a telas: uma informação pouco clara no canal digital pode depender de uma regra, de um processo interno ou de uma atividade em campo.</p>
        </>
      ),
    },
    {
      title: 'Desburocratização de backoffice antes de redesenho de portal e Design System multi-tenant.',
      content: (
        <ol className="cp-decisions">{[
          ['Mapear antes de propor', 'A jornada atual organiza atores, etapas e dependências para que uma oportunidade de interface seja discutida no contexto do serviço.'],
          ['Conectar frente de atendimento e operação', 'Os blueprints aproximam ações do consumidor, canais e atividades internas. Essa relação permite discutir causas e responsabilidades nas transições.'],
          ['Organizar oportunidades por jornada', 'A visão futura reúne propostas ao longo do ciclo de vida, apoiando a discussão de prioridades e a construção de um roadmap.'],
        ].map(([title, description]) => (
          <li key={title}>
            <h3>{title}</h3>
            <p>{description}</p>
          </li>
        ))}</ol>
      ),
    },
    {
      title: 'Os 5 estágios do ciclo de vida do cliente mapeados em Service Blueprints.',
      content: (
        <>
          <p>O mapa de jornada futura organiza o ciclo de vida em cinco macroetapas estruturadas em pranchas detalhadas de Service Blueprint:</p>
          <List items={[
            '1. Contrato e instalo: busca de informações, contratação, adequação e ligação nova.',
            '2. Uso e pago: consumo, acompanhamento, autoleitura e faturamento.',
            '3. Preciso de suporte: necessidade de ajuda, interrupção e resolução de problemas.',
            '4. Mudo o contrato: alterações cadastrais, portabilidade ao Mercado Livre e geração solar.',
            '5. Abandono: encerramento do vínculo, prevenção de inadimplência e desdobramentos.',
          ]} />
          <div className="cp-gallery">
            <CaseFigure image={{
              src: '/images/neoenergia-blueprint-2-uso-pago.webp',
              width: 1414,
              height: 4480,
              alt: 'Service Blueprint detalhado da etapa 2: Uso e Pago — Consumo, faturamento e autoleitura',
              caption: 'Artefato original de Service Blueprint: Macro-etapa 2. Uso e Pago (ações, criticidade, highlights por 3 perfis de clientes, análise interna de processos e oportunidades).',
            }} />
            <CaseFigure image={{
              src: '/images/neoenergia-blueprint-1-contrato-instalo.webp',
              width: 2000,
              height: 5200,
              alt: 'Service Blueprint da etapa 1: Contrato e Instalo',
              caption: 'Artefato original de Service Blueprint: Macro-etapa 1. Contrato e Instalo (pesquisa de informações, adequação e ligação nova).',
            }} />
            <CaseFigure image={{
              src: '/images/neoenergia-jornada-futuro-tobe.webp',
              width: 2000,
              height: 1200,
              alt: 'Service Blueprint da Jornada do Futuro To-Be',
              caption: 'Artefato original da Jornada do Futuro (To-Be): blueprint de serviço integrado omnicanal e visão consolidada de ganhos.',
            }} />
          </div>
        </>
      ),
    },
    {
      title: 'Matriz de 118 ideias priorizadas e baseline para o plano diretor de inovação.',
      content: (
        <>
          <h3>Contribuições do trabalho de serviço</h3>
          <List items={[
            'Organização de jornadas atuais e dependências do atendimento em 11 canais.',
            'Blueprints e visão futura ao longo do ciclo de vida do consumidor.',
            'Matriz de 118 ideias estruturadas para priorização executiva e discussão de roadmap.',
          ]} />
          <CaseFigure image={{
            src: '/images/neoenergia-matriz-118-ideias.webp',
            width: 2000,
            height: 1195,
            alt: 'Matriz de Priorização com 118 Ideias de Inovação',
            caption: 'Matriz de Priorização: 118 ideias estruturadas e classificadas por impacto no negócio versus valor percebido pelo consumidor.',
          }} />
          <div className="cp-note">
            <h3>Aprendizado central</h3>
            <p>Em serviços essenciais, a experiência digital depende do que acontece depois do clique. Tornar visíveis as relações entre consumidor, atendimento e operação é parte do trabalho de design.</p>
          </div>
        </>
      ),
    },
    {
      title: 'Fontes oficiais de P&D ANEEL, governança executiva e equipe EY × Livework.',
      content: (
        <div className="cp-appendix">
          <details open>
            <summary>Referências do projeto</summary>
            <div>
              <Sources project=\"neoenergia\" />
            </div>
          </details>
          <details>
            <summary>Colaboração</summary>
            <div>
              <p>Israel Rozar — Senior Product Designer / Service Designer, no contexto de Business Transformation da EY, em colaboração com Livework e áreas da Neoenergia. Jornadas, blueprints e propostas são entregas de equipe multidisciplinar.</p>
            </div>
          </details>
          <details>
            <summary>Alcance dos resultados apresentados</summary>
            <div>
              <p>Os documentos e os blueprints sustentam o relato de discovery e desenho de serviço. Não são apresentados como comprovados ROI, conformidade WCAG, implantação de design system, aprovação de orçamento ou efeito operacional de longo prazo. Os números de escala pertencem ao contexto histórico da organização.</p>
            </div>
          </details>
        </div>
      ),
    },
  ],
}"""

if old_neo in text:
    text = text.replace(old_neo, new_neo)
    with open('site/src/pages/CasePages.tsx', 'w', encoding='utf-8') as f:
        f.write(text)
    print("SUCCESS: AutoFixed neoenergiaPresentation with real blueprints and no placeholders!")
else:
    print("ERROR: old_neo block not found!")

