import re

with open('site/src/pages/CasePages.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Let's replace chapter titles and content in neoenergiaPresentation
neo_pattern = r"(export const neoenergiaPresentation: CasePresentationData = \{.*?\n  chapters: \[)(.*?)(\n  \],\n\})"

new_neo_chapters = """
    {
      title: 'Unificação da infraestrutura de atendimento para 34 milhões de pessoas.',
      content: (
        <>
          <div className="cp-summary">
            <p>
              Mapeamento integral e redesenho de processos omnicanal no setor elétrico para o Grupo Neoenergia (Iberdrola Brasil),
              integrando 4 grandes distribuidoras de energia — <strong>Elektro</strong> (SP/MS), <strong>Coelba</strong> (BA),
              {' '}<strong>Celpe</strong> (PE) e <strong>Cosern</strong> (RN).
            </p>
            <p>
              Em iniciativa desenvolvida sob o programa de P&D Tecnológico regulado pela ANEEL, o consórcio estratégico
              EY Business Transformation e Livework realizou um diagnóstico profundo de campo, auditou os silos internos de backstage,
              mapeou as 5 macro-etapas do ciclo de vida em blueprints detalhados e priorizou 118 ideias de inovação sistêmica
              para reduzir gargalos operacionais e atritos de faturamento.
            </p>
          </div>
          <CaseMetrics
            items={[
              ['34M', 'habitantes nas áreas de concessão'],
              ['13,9M', 'unidades consumidoras faturadas'],
              ['5 estágios', 'ciclo de vida em blueprints'],
              ['118 ideias', 'priorizadas na matriz de valor'],
            ]}
          />
          <p>
            Os 34 milhões de habitantes (17% da população do Brasil) e 13,9 milhões de clientes representam a escala real auditada das áreas de concessão do Grupo Neoenergia em 18 estados. O projeto foi executado sob as diretrizes do Programa de P&D ANEEL.
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
              <h3>O cenário base</h3>
              <p>
                Como uma das maiores distribuidoras de energia do país, a Neoenergia lidava com uma cadeia de serviços altamente fragmentada.
                O ecossistema envolvia desde pequenos consumidores residenciais (PF) até grandes indústrias no Mercado Livre,
                operando em canais físicos e digitais que não se comunicavam de forma coesa.
              </p>
            </div>
            <div>
              <h3>O desafio estratégico</h3>
              <List
                items={[
                  'Reduzir custos operacionais severos decorrentes de deslocamentos técnicos improdutivos e processos manuais de backoffice.',
                  'Eliminar atritos críticos de confiança na ponta causados por insegurança nas faturas e demora em novas ligações.',
                  'Diagnosticar falhas estruturais de backstage e desenhar a jornada futura To-Be integrada para 4 concessionárias.',
                ]}
              />
            </div>
          </div>
          <div className="cp-note">
            <h3>Minha contribuição documentada</h3>
            <p>
              Atuação como Senior Product Designer / Service Designer na squad de Business Transformation da EY,
              em parceria estreita com a Livework, conduzindo diagnósticos de campo, entrevistas com lideranças e especialistas,
              shadowing de atendentes em agências físicas, facilitação de workshops de co-criação e modelagem dos blueprints de serviço.
            </p>
          </div>
        </>
      ),
    },
    {
      title: 'Auditoria de backstage: quando a insatisfação com a fatura revela silos operacionais.',
      content: (
        <>
          <p>
            <strong>Diagnóstico orientado a dados:</strong> Ao invés de atuar apenas na camada de interface (UI) de um aplicativo,
            a abordagem focou na raiz do serviço estrutural. A pesquisa qualitativa e as dinâmicas de Discovery revelaram que grande parte
            da insatisfação do cliente era um sintoma direto de processos de backstage ineficientes e dissociados.
          </p>
          <List
            items={[
              'Silos operacionais: as automações internas existiam apenas de forma isolada em cada departamento. Essa quebra de integração forçava o trabalho manual e reativo dos atendentes na geração de faturas e análises de viabilidade.',
              'O gargalo das três notas: para atender a um simples protocolo de ligação nova, o sistema gerava de forma desintegrada três Ordens de Serviço (nota de solicitação, nota de obra e nota de ligação), multiplicando deslocamentos improdutivos de equipes de campo.',
              'A fatura como ponto de tensão: termos técnicos complexos e cálculos por média de consumo retroalimentavam a desconfiança nas equipes técnicas e o sobrecarregamento das centrais de atendimento.',
            ]}
          />
          <div className="cp-note">
            <h3>Triangulação em 11 canais de atendimento</h3>
            <p>
              A análise cobriu 11 canais de atendimento: Aplicativo Mobile, Agência Virtual Web, Totens de Autoatendimento,
              Agências Presenciais, Call Center 0800, SMS, E-mail, Chatbot/WhatsApp, Redes Sociais, Canal Regulado de Acessibilidade Auditiva/Fala (0800 701 01 55 com tecnologia TDD) e Canal de Ética e Denúncia.
            </p>
          </div>
        </>
      ),
    },
    {
      title: 'Desburocratização de backoffice antes de redesenho de portal e Design System multi-tenant.',
      content: (
        <ol className="cp-decisions">
          {[
            [
              'Desburocratização de Backoffice antes de Redesenho de Portal',
              'Em vez de focar recursos em redesenhar completamente o portal web no curto prazo, a priorização estratégica indicou que o maior retorno de investimento (ROI) viria da desburocratização de backoffice e da capacitação técnica das equipes de campo para atuar de forma resolutiva.',
            ],
            [
              'Automação e Escalabilidade de Ordens de Serviço',
              'Foram mapeados requisitos para que integrações sistêmicas substituíssem processos de validação estritamente manuais (como as três notas de serviço distintas geradas em um simples pedido de ligação), propondo um fluxo unificado e automatizado com rastreamento em tempo real.',
            ],
            [
              'Desacoplamento da Cobrança de Terceiros',
              'Separação definitiva da dívida do indivíduo (CPF) da unidade consumidora (UC), eliminando penalizações indevidas a novos inquilinos e proprietários de imóveis alugados.',
            ],
            [
              'Arquitetura Multi-Tenant de Design System',
              'Desacoplamento entre lógica de interação e identidade visual: uma única base de código e componentes com tokens semânticos capazes de renderizar as marcas Elektro, Coelba, Celpe e Cosern sob diretrizes rigorosas de acessibilidade WCAG 2.1 AA.',
            ],
          ].map(([title, desc]) => (
            <li key={title}>
              <h3>{title}</h3>
              <p>{desc}</p>
            </li>
          ))}
        </ol>
      ),
    },
    {
      title: 'Os 5 estágios do ciclo de vida do cliente mapeados em Service Blueprints.',
      content: (
        <>
          <p>
            Para garantir escaneabilidade e acionamento por parte das diretorias de negócio, o serviço foi documentado
            e arquitetado em 5 grandes estágios do ciclo de vida do cliente:
          </p>
          <List
            items={[
              '1. Contrato e Instalo: Redesenho das regras de entrada, focando em antecipar exigências técnicas para os clientes e mitigar deslocamentos frustrados.',
              '2. Uso e Pago: Estruturação de novos serviços digitais (Simulador e Autoleitura) focados em devolver a autonomia ao usuário e reduzir disputas de faturamento.',
              '3. Preciso de Suporte: Padronização do atendimento reativo, notificações preditivas de apagões e canal 100% digital de ressarcimento de danos elétricos (RDE).',
              '4. Mudo o Contrato: Facilitadores para portabilidade ao Mercado Livre, troca de titularidade instantânea por biometria e transparência em Geração Distribuída Solar.',
              '5. Abandono: Estratégias preventivas contra ligações irregulares e automação do encerramento de vínculo.',
            ]}
          />
          <div className="cp-gallery">
            <CaseFigure
              image={{
                src: '/images/neoenergia-blueprint-2-uso-pago.webp',
                width: 1414,
                height: 4480,
                alt: 'Service Blueprint detalhado da etapa 2: Uso e Pago — Consumo, faturamento e autoleitura',
                caption: 'Service Blueprint original: Macro-etapa 2. Uso e Pago (ações, criticidade, highlights por perfil, análise interna de processos e oportunidades).',
              }}
            />
            <CaseFigure
              image={{
                src: '/images/neoenergia-blueprint-1-contrato-instalo.webp',
                width: 2000,
                height: 5200,
                alt: 'Service Blueprint da etapa 1: Contrato e Instalo',
                caption: 'Service Blueprint original: Macro-etapa 1. Contrato e Instalo (pesquisa de informações, adequação e ligação nova).',
              }}
            />
            <CaseFigure
              image={{
                src: '/images/neoenergia-jornada-futuro-tobe.webp',
                width: 2000,
                height: 1200,
                alt: 'Service Blueprint da Jornada do Futuro To-Be',
                caption: 'Jornada do Futuro (To-Be): blueprint de serviço integrado omnicanal e visão consolidada de ganhos.',
              }}
            />
          </div>
        </>
      ),
    },
    {
      title: 'Matriz de 118 ideias priorizadas e baseline para o plano diretor de inovação.',
      content: (
        <>
          <p>
            O mapeamento serviu como o artefato fundamental (baseline) para o plano diretor de inovação e digitalização da companhia:
          </p>
          <List
            items={[
              'Alinhamento Executivo: Construção de uma matriz clara de dores vs. oportunidades financeiras (118 ideias priorizadas), justificando o orçamento técnico para modernização de infraestrutura (sistemas de detecção de fraudes e gestão de medidores).',
              'Visão de Futuro: O projeto entregou não apenas relatórios passivos, mas um Service Blueprint estruturado e priorizado que embasou as Sprints de desenvolvimento de produtos digitais subsequentes.',
            ]}
          />
          <CaseFigure
            image={{
              src: '/images/neoenergia-matriz-118-ideias.webp',
              width: 2000,
              height: 1195,
              alt: 'Matriz de Priorização com 118 Ideias de Inovação',
              caption: 'Matriz de Priorização: 118 ideias estruturadas e classificadas por impacto no negócio versus valor percebido pelo consumidor.',
            }}
          />
          <div className="cp-note">
            <h3>Aprendizado central</h3>
            <p>
              Em serviços essenciais de infraestrutura pública, a experiência digital não pode ser desenhada de forma isolada do mundo físico.
              A transparência de dados operacionais e a consistência entre o aplicativo, o atendente da agência e a equipe de campo são os fatores determinantes para construir a confiança da população.
            </p>
          </div>
          <div className="cp-appendix">
            <details open>
              <summary>Limites declarados das evidências</summary>
              <div>
                <p>
                  Para preservar o rigor técnico e a transparência profissional, os seguintes limites metodológicos são declarados:
                </p>
                <List
                  items={[
                    'Os números de 34 milhões de habitantes, 13,9 milhões de clientes e 1.028 cidades correspondem aos dados cadastrais e demográficos oficiais das concessões do Grupo Neoenergia.',
                    'Os artefatos auditados comprovam as etapas de diagnóstico, pesquisa de campo, mapeamento de jornadas, blueprints To-Be, especificações de UI e roteiros de teste.',
                    'A implantação gradual em sistemas corporativos (SAP, Salesforce, smart grids) e eventuais indicadores operacionais de longo prazo pertencem aos ciclos plurianuais da Neoenergia e não são atribuídos como impacto individual de design.',
                  ]}
                />
              </div>
            </details>
          </div>
        </>
      ),
    },
    {
      title: 'Fontes oficiais de P&D ANEEL, governança executiva e equipe EY × Livework.',
      content: (
        <div className="cp-appendix">
          <details open>
            <summary>Fontes e rastreabilidade dos artefatos</summary>
            <div>
              <p>
                Projeto desenvolvido em 2020 no âmbito do Programa de P&D Estratégico ANEEL Conexão Digital. O acervo auditado inclui pranchas de service blueprints em altíssima resolução, apresentações de governança e documentação metodológica. Fontes de consulta:
              </p>
              <Sources project="neoenergia" />
            </div>
          </details>
          <details>
            <summary>Autoria e equipe documentada</summary>
            <div>
              <p>
                <strong>Israel Rozar</strong> — Senior Product Designer / Service Designer, integrante da equipe de Business Transformation da EY.
              </p>
              <p>
                Equipe EY Business Transformation registrada nos documentos oficiais (slides 63-64): João Pissutto, Maria Eugênia Rocha (Marô), Gustavo Risonho, Caio Neves, Piera Casale, Ana Augusto, Guilherme Homma, Rafael Nakamoto, Karen Ferrari, Cinthia Trevisoli e Marina Bauer, em consórcio com os especialistas da Livework Brasil.
              </p>
            </div>
          </details>
          <details>
            <summary>Roteiro de defesa técnica em entrevista</summary>
            <div>
              <p>Perguntas-chave que este case capacita a responder com profundidade:</p>
              <List
                items={[
                  'Como diagnosticar que a insatisfação do cliente com uma fatura é sintoma de silos operacionais de backstage e não apenas um problema visual de layout?',
                  'Como conduzir pesquisa qualitativa e cliente oculto (Mystery Shopper) respeitando as particularidades socioeconômicas e de conectividade entre o Sudeste e o Nordeste?',
                  'Como priorizar 118 ideias de inovação através de uma Matriz de Impacto no Negócio vs. Valor Percebido pelo Consumidor?',
                  'Como arquitetar um Design System multi-tenant que unifique a experiência de 4 distribuidoras reguladas preservando identidades de marca distintas sob conformidade WCAG 2.1 AA?',
                ]}
              />
            </div>
          </details>
        </div>
      ),
    }"""

match = re.search(neo_pattern, content, flags=re.DOTALL)
if match:
    new_content = content[:match.start(2)] + new_neo_chapters + content[match.end(2):]
    with open('site/src/pages/CasePages.tsx', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("SUCCESS: Updated neoenergiaPresentation!")
else:
    print("ERROR: Could not find neoenergiaPresentation pattern!")

