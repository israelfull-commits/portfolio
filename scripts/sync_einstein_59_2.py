with open('site/src/pages/CasePages.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Target einsteinPresentation block
start_marker = 'export const einsteinPresentation: CasePresentationData = {'
end_marker = 'export const claroPresentation: CasePresentationData = {'

pos_start = content.find(start_marker)
pos_end = content.find(end_marker)

if pos_start == -1 or pos_end == -1:
    print("Could not locate start or end marker!")
    exit(1)

new_einstein_presentation = '''export const einsteinPresentation: CasePresentationData = {
  title: "Einstein — Consumo de Resultados",

  context: "Saúde · HIAE × Foursys · 2022",

  headline: "Clareza não é o mesmo que compreensão.",

  subtitle: "Uma linguagem visual modular para laudos em diferentes canais.",

  role: "UX Lead",

  team: "Foursys × Hospital Israelita Albert Einstein",

  scope: "Pesquisa, modelagem da informação e prototipagem",

  kicker: "Saúde · Laudos Médicos",

  hero: einsteinHero,

  nextCase: {
    title: "Strategic Discovery e Service Design: Ecossistema Neoenergia",

    href: "/cases/neoenergia-conexao-digital",

    context: "Utilities · P&D ANEEL · 34M de pessoas",
  },

  prevCase: {
    title: "Claro — Ativação Simplificada",

    href: "/cases/claro-ativacao-simplificada",

    context: "Telecom · Enterprise UX",
  },

  chapters: [
    {
      title: "Organizar resultados sem perder o contexto clínico.",

      content: (
        <>
          <div className="cp-summary">
            <p>
              Pesquisa e proposta de uma linguagem visual modular para laudos,
              com hierarquia estável entre nome do exame, resultado, referência
              e contexto.
            </p>
            <p>
              Laudos heterogêneos reuniam informações importantes em hierarquias
              variáveis. Pacientes precisavam localizar informações e levá-las à
              consulta; médicos precisavam cruzar resultados, referências,
              observações e contexto clínico.
            </p>
          </div>
          <CaseMetrics
            items={[
              ["4 médicos", "entrevistas semiestruturadas"],

              ["Questionário", "pesquisa exploratória com pacientes"],

              ["14", "categorias de exames no escopo"],
            ]}
          />
          <p>
            Amostras de métodos diferentes não se somam. O total do questionário
            diverge entre recortes de 117 e 121 respostas.
          </p>
        </>
      ),
    },

    {
      title: "Uma hierarquia que funcione na tela e no papel.",

      content: (
        <>
          <div className="cp-columns">
            <div>
              <h3>O cenário</h3>
              <p>
                A experiência precisava funcionar no digital e no papel, em
                sistemas de fornecedores distintos e com recursos limitados para
                configurar templates. Em alguns cenários, o conteúdo era
                estruturado no Microsoft Word.
              </p>
            </div>
            <div>
              <h3>O mandato</h3>
              <List
                items={[
                  "Dar hierarquia estável ao nome do exame, material, resultado e referência.",

                  "Manter comentários, método e contexto clínico próximos.",

                  "Respeitar variações de dados e restrições dos sistemas laudadores.",
                ]}
              />
            </div>
          </div>
          <div className="cp-note">
            <h3>Minha contribuição</h3>
            <p>
              Atuação como UX Lead no projeto HIAE × Foursys, articulando
              pesquisa, estrutura da informação e decisões de experiência com a
              equipe multidisciplinar.
            </p>
          </div>
        </>
      ),
    },

    {
      title: "Do documento ao dado.",

      content: (
        <>
          <p>
            A descoberta reuniu quatro entrevistas médicas, questionário
            exploratório e análise documental. A base registra 189 exames
            analisados, 150 priorizados e 14 categorias; recortes menores
            representam subconjuntos do acervo.
          </p>
          <List
            items={[
              "Entrevistas com especialidades e contextos de atendimento distintos.",

              "Análise de comportamentos e canais preferidos dos pacientes.",

              "Inventário de conteúdos de áreas internas e fornecedores, além de benchmark de serviços de saúde.",
            ]}
          />
          <CaseFigure image={einsteinImages[1]} />
          <div className="cp-note">
            <h3>Como evitar uma interpretação clínica isolada?</h3>
            <p>
              Paciente e médico precisam de relações claras entre os dados,
              preservando referência, observações e contexto.
            </p>
          </div>
        </>
      ),
    },

    {
      title: "Preservar relações entre resultado, referência e contexto.",

      content: (
        <>
          <ol className="cp-decisions">
            {[
              [
                "Âncora de leitura estável",

                "Nome, material, resultado e referência formam o primeiro nível de leitura.",
              ],

              [
                "Componentes para variação real",

                "DataField e ExamTitle organizam variações numéricas, textuais e de extensão sem criar um template por exame.",
              ],

              [
                "Sinais redundantes",

                "Texto, posição e tratamento visual trabalham juntos; a cor não comunica o estado sozinha.",
              ],

              [
                "Compatibilidade antes de sofisticação",

                "Formatação simples, cabeçalho e rodapé comuns apoiam o uso nos sistemas laudadores existentes.",
              ],
            ].map(([title, copy]) => (
              <li key={title}>
                <h3>{title}</h3>
                <p>{copy}</p>
              </li>
            ))}
          </ol>
          <CaseFigure
            image={{
              src: "/images/hiae-ds-componentes-crop-1600.webp",
              width: 1600,
              height: 900,
              alt: "Documentação dos componentes DataField e ExamTitle com tokens e anatomia modular",
              caption:
                "Documentação dos componentes estruturais: DataField e ExamTitle com tokens de espaçamento e regras de anatomia modular.",
            }}
          />
        </>
      ),
    },

    {
      title: "Uma estrutura comum para conteúdos diferentes.",

      content: (
        <>
          <p>
            A proposta organiza o conteúdo para reduzir competição visual e
            aproximar resultado, unidade e referência. Os artefatos documentam
            pesquisa, modelagem e entrega.
          </p>
          <div className="cp-gallery">
            <CaseFigure
              image={{
                src: "/images/hiae-laudo-original-recorte.webp",

                width: 1120,

                height: 640,

                alt: "Documento original — recorte de análise",

                caption:
                  "Documento original — recorte de análise da composição textual densa.",
              }}
            />
            <CaseFigure
              image={{
                src: "/images/hiae-laudo-proposta-demonstrativa-1600.webp",

                width: 1600,

                height: 1199,

                alt: "Reconstrução demonstrativa da estrutura proposta",

                caption:
                  "Reconstrução demonstrativa da estrutura proposta. Conteúdo fictício.",
              }}
            />
          </div>
          <CaseFigure
            image={{
              ...einsteinImages[0],

              previewCrop: { x: 216, y: 188, width: 718, height: 931 },

              caption:
                "Artefato original de proposta: template no Word para organizar informações do exame. Demonstra a estrutura de conteúdo; não comprova implantação.",
            }}
          />
        </>
      ),
    },

    {
      title: "Clareza percebida e interpretação exigem avaliações distintas.",

      content: (
        <>
          <p>
            Os registros reportam 44 participantes em testes, sem bases
            completas por modalidade e pergunta. Clareza percebida e
            interpretação foram medidas em tarefas distintas; os percentuais
            não demonstram melhoria antes/depois nem impacto clínico.
          </p>
          <div className="cp-note">
            <h3>Aprendizado</h3>
            <p>
              Medir separadamente localização, associação entre valor e
              referência, interpretação e erros críticos — com revisão clínica
              e tecnologias assistivas.
            </p>
          </div>
        </>
      ),
    },

    {
      title: "Pesquisa, entregáveis e colaboração.",

      content: (
        <div className="cp-appendix">
          <details open>
            <summary>Fontes e recorte histórico</summary>
            <div>
              <p>
                Projeto de 2022. O estudo do Notion foi atualizado em
                29/12/2024; essa data editorial não representa uma nova versão
                de interface. Protótipos e reconstruções estão identificados nas
                legendas.
              </p>
              <Sources project="einstein" />
            </div>
          </details>
          <details>
            <summary>Autoria e colaboração</summary>
            <div>
              <p>
                Israel Rozar — UX Lead. Trabalho realizado com Foursys, Hospital
                Israelita Albert Einstein e equipe multidisciplinar, com atuação
                em pesquisa, síntese e coordenação das decisões de experiência.
              </p>
            </div>
          </details>
          <details>
            <summary>Limites das evidências</summary>
            <div>
              <p>
                As 121 respostas referem-se à seção de questionário do estudo
                original. O resumo final menciona 117 pacientes e outros
                percentuais, sem reconciliação dos recortes. Amostras e etapas
                diferentes não são somadas nem tratadas como resultado de
                negócio.
              </p>
            </div>
          </details>
        </div>
      ),
    },
  ],
}

'''

content = content[:pos_start] + new_einstein_presentation + content[pos_end:]

with open('site/src/pages/CasePages.tsx', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated einsteinPresentation with 100% parity to Figma node 59:2")

