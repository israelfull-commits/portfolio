import re

with open('site/src/pages/CasePages.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

claro_pattern = r"(export const claroPresentation: CasePresentationData = \{.*?\n  chapters:\[)(.*?)(\n  \],\n\})"

new_claro_chapters = """
    {
      title: 'Redesenho da operação comercial e redução de atrito na venda multicanal.',
      content: (
        <>
          <div className="cp-summary">
            <p>
              Organizar uma operação comercial complexa para que o atendente consiga consultar o cliente,
              configurar planos e aparelhos e acompanhar a jornada de ponta a ponta sem rupturas de contexto.
            </p>
            <p>
              O projeto integrou discovery de campo em lojas físicas e canais remotos, decomposição de jornadas
              críticas de telecom e propostas estruturadas de interface para desktop e mobile, organizando regras
              de negócio e resumo financeiro em tempo real.
            </p>
          </div>
          <CaseMetrics
            items={[
              ['20', 'entrevistas em profundidade'],
              ['22', 'jornadas de atendimento mapeadas'],
              ['70', 'oportunidades de melhoria levantadas'],
            ]}
          />
          <p>
            Esses números descrevem o escopo auditado de discovery com a operação, não resultados causais de negócio.
            As evidências visuais selecionadas estão apresentadas nas etapas correspondentes.
          </p>
        </>
      ),
    },
    {
      title: 'Uma operação de alta densidade dividida entre balcão físico e mobilidade.',
      content: (
        <>
          <div className="cp-columns">
            <div>
              <h3>O cenário</h3>
              <p>
                A rotina comercial precisava conciliar necessidades de atendentes de loja, consultores em trânsito
                e as regras de negócio de telecom, com grande volume de dados por transação.
              </p>
            </div>
            <div>
              <h3>O desafio</h3>
              <p>
                Como apoiar a continuidade do atendimento e tornar os dados cadastrais, técnicos e financeiros
                compreensíveis em telas de desktop e dispositivos móveis?
              </p>
            </div>
          </div>
          <div className="cp-note">
            <h3>Minha contribuição documentada</h3>
            <p>
              Atuação em UX/UI, da imersão inicial e síntese de pesquisa à definição de fluxos de navegação,
              prototipação de alta fidelidade e entrega visual para engenharia.
            </p>
          </div>
        </>
      ),
    },
    {
      title: 'Compreender a rotina real dos atendentes antes de desenhar interfaces.',
      content: (
        <>
          <p>
            O discovery reuniu benchmarking competitivo, 20 entrevistas com profissionais e lideranças executivas,
            três dias de workshops imersivos e a formulação de dez personas operacionais. Os materiais selecionados
            demonstram o processo colaborativo e o mapeamento detalhado da jornada de troca de chip.
          </p>
          <div className="cp-gallery">
            {claroImages.slice(1, 3).map((image) => (
              <CaseFigure key={image.src} image={image} />
            ))}
          </div>
        </>
      ),
    },
    {
      title: 'Navegação progressiva, resumo financeiro visível e preservação do contexto do cliente.',
      content: (
        <ol className="cp-decisions">
          {[
            [
              'Navegação progressiva por etapas',
              'Grupos expansíveis e etapas numeradas orientam o operador em fluxos extensos sem poluição visual.',
            ],
            [
              'Preservação do contexto do cliente',
              'Cabeçalho fixo com dados da linha, status cadastral e atalhos para jornadas frequentes apoiam a continuidade da conversa.',
            ],
            [
              'Composição financeira em tempo real',
              'O resumo lateral aproxima produtos, descontos aplicados e valores finais durante toda a configuração do plano.',
            ],
          ].map(([title, text]) => (
            <li key={title}>
              <h3>{title}</h3>
              <p>{text}</p>
            </li>
          ))}
        </ol>
      ),
    },
    {
      title: 'Da jornada do chip às interfaces desktop e mobile padronizadas.',
      content: (
        <>
          <p>
            As propostas apresentam ativação, detalhe da linha e confirmação, com adaptações responsivas entre desktop
            e mobile. A sequência evidencia consistência de padrões, legibilidade de dados e clareza nos estados operacionais.
          </p>
          <div className="cp-gallery">
            {[claroImages[3], claroImages[4], claroImages[5]].map((image) => (
              <CaseFigure key={image.src} image={image} />
            ))}
          </div>
        </>
      ),
    },
    {
      title: 'Decomposição de 22 jornadas de atendimento e aprendizados operacionais.',
      content: (
        <>
          <p>
            O acervo documenta a decomposição de 22 jornadas e propostas para consultar clientes, configurar ofertas e
            confirmar operações. Ele permite discutir arquitetura de informação e continuidade omnicanal em escala.
          </p>
          <p>
            Avaliar o efeito operacional exigiria comparar conclusões de tarefas e taxas de erro em testes pareados.
            O material histórico comprova a especificação e entrega das telas, delimitando com rigor o que foi executado.
          </p>
          <div className="cp-note">
            <h3>Aprendizado de design</h3>
            <p>
              Uma interface de atendimento comercial precisa manter o contexto do cliente e da oferta sempre visíveis.
              O design deve reduzir a carga cognitiva do operador e, ao mesmo tempo, garantir transparência absoluta para o consumidor final.
            </p>
          </div>
        </>
      ),
    },
    {
      title: 'Acervo histórico de discovery, colaboração e limites de evidência.',
      content: (
        <div className="cp-appendix">
          <details open>
            <summary>Arquivos e versões auditadas</summary>
            <div>
              <p>
                Acervo Claro fornecido pelo autor: registros de workshops, mapa de jornada de troca de chip, telas de ativação,
                detalhe da linha e confirmação mobile.
              </p>
              <p>
                O documento de migração desktop identifica V.2 de 10/05/2018; o PDF mobile foi atualizado em 11/06/2018.
              </p>
              <Sources project="claro" />
            </div>
          </details>
          <details>
            <summary>Colaboração e alcance das evidências</summary>
            <div>
              <p>
                Israel Rozar — UX/UI Designer, em colaboração com stakeholders e operadores de loja. As quantidades de discovery
                provêm do relatório primário da iniciativa; os materiais visuais comprovam os artefatos projetados.
              </p>
            </div>
          </details>
        </div>
      ),
    }"""

match = re.search(claro_pattern, content, flags=re.DOTALL)
if match:
    new_content = content[:match.start(2)] + new_claro_chapters + content[match.end(2):]
    with open('site/src/pages/CasePages.tsx', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("SUCCESS: Updated claroPresentation!")
else:
    print("ERROR: Could not find claroPresentation pattern!")

