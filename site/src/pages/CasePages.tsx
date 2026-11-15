import { useParams } from "react-router"

import {
  CaseFigure,
  CaseMetrics,
  CasePresentation,
  type CaseImage,
  type CasePresentationData,
  type CaseNavTarget,
} from "../components/CasePresentation"

import { cases } from "./ItauPreparationCase"

import NotFound from "./NotFound"

function List({ items }: { items: string[] }) {
  return (
    <ul className="cp-list">
      {items.map((item) => (
        <li key={item}>{item}</li>
      ))}
    </ul>
  )
}

const sourceLinks: Record<string, Array<[string, string]>> = {
  einstein: [
    [
      "Estudo de caso original — contexto, pesquisa e proposta",

      "https://israelrozar.notion.site/8ac93175a91d48769a322972968e0d2a",
    ],

    [
      "HIAE — Laudos · arquivo de trabalho",

      "https://www.figma.com/design/mw8vC7rIuaKvF3FCG3Qi6c/HIAE---Laudos?node-id=1853-49239",
    ],
  ],

  claro: [
    [
      "Documentação do Case — Ativação Simplificada",

      "https://uxfol.io/p/israelrozar/033c945f",
    ],
  ],

  vencimentos: [
    [
      "Interface mais recente confirmada pelo autor · Gestão de liquidez",

      "https://www.figma.com/design/jifEQkL5yQAvfaXsSQtmrH/Gest%C3%A3o-de-liquidez?node-id=582-12520",
    ],

    [
      "Explorações e documentação de handoff · histórico",

      "https://www.figma.com/design/YHCO7Yb3QdKP0nW2ie0tYO/ESTUDOS-VENCIMENTOS?node-id=1074-2687",
    ],
  ],

  "hub-liquidez": [
    [
      "Interface da solução · Hub de liquidez",

      "https://www.figma.com/design/jifEQkL5yQAvfaXsSQtmrH/Gest%C3%A3o-de-liquidez?node-id=3-14068",
    ],
  ],

  movimentacoes: [
    [
      "Discovery Extrato EA · contexto e alternativas",

      "https://www.figma.com/design/klNiUiITLbgRMix1qdQprn/Gest%C3%A3o-de-campanhas-IFA?node-id=1966-34105",
    ],

    [
      "Documento de exploração · histórico da iniciativa",

      "https://www.figma.com/design/klNiUiITLbgRMix1qdQprn/Gest%C3%A3o-de-campanhas-IFA?node-id=1926-38396",
    ],
  ],

  campanhas: [
    [
      "Fluxos e estados · Gestão de Campanhas IFA",

      "https://www.figma.com/design/YHCO7Yb3QdKP0nW2ie0tYO/ESTUDOS-VENCIMENTOS?node-id=3-2",
    ],

    [
      "Recorte de configuração no acervo de referência",

      "https://www.figma.com/design/YIHybVXPe0Hfmja1hAyzQZ/Template-portfolio?node-id=31-3638",
    ],
  ],

  neoenergia: [
    [
      "Pasta Oficial de Entregáveis e Blueprints (Google Drive)",

      "https://drive.google.com/drive/folders/13Jahrxh9R6ktCYFh4sJRzZ_ZcXqinlC4?usp=sharing",
    ],

    [
      "P&D Conexão Digital — Relatório Integrado & Entregas (Google Slides)",

      "https://docs.google.com/presentation/d/1rISX29_0Xr0nHKHVahoQTMxlyspejXWq-6SmtIsR_8U/edit",
    ],

    [
      "P&D Conexão Digital — Kick-off & Governança (Google Slides)",

      "https://docs.google.com/presentation/d/1BUOb36yK7EhwPi6qs4F4uiGkQDlV3HIAfdESRUGJjbY/edit",
    ],

    [
      "P&D Conexão Digital — Blueprint Estratégico (Google Slides)",

      "https://docs.google.com/presentation/d/1GsxcSgYdvalARU0PEzzRM0BjKWxf9GUbRmD-_eAkiJo/edit",
    ],

    [
      "Jornada do Cliente Neoenergia — Mapa de Tendências (Figma)",

      "https://www.figma.com/design/lbt8CIcNISYgdqrhjBfhhA/Jornada-do-Cliente-Neoenergia---Mapa-de-Tend%C3%AAncias?node-id=0-1",
    ],

    [
      "Jornada do Cliente Neoenergia — Acervo Original (Figma)",

      "https://www.figma.com/design/u9EZbfBXeNRNZFiC4ql9Ws/-Original--Jornada-do-Cliente-Neoenergia---Mapa-de-Tend%C3%AAncias?node-id=0-1",
    ],
  ],
}

function Sources({ project }: { project: string }) {
  return (
    <ul className="cp-list">
      {(sourceLinks[project] || []).map(([label, href]) => (
        <li key={href}>
          <a href={href}>{label}</a>
        </li>
      ))}
    </ul>
  )
}

const einsteinHero: CaseImage = {
  src: "/images/hiae-capa-editorial-1600.webp",
  width: 2560,
  height: 1440,
  alt: "Taxonomia do Design System e modelagem visual modular dos laudos do Hospital Israelita Albert Einstein",
  caption:
    "Taxonomia oficial do Design System: anatomia de campos, tokens tipográficos e componentes modulares para estruturação de laudos laboratoriais.",
}

const einsteinImages: CaseImage[] = [
  {
    src: "/images/hiae-template-fonte.webp",

    width: 1142,

    height: 1150,

    alt: "Template de laudo Einstein no Word, com seções para metodologia, resultado e conclusão",

    caption:
      "Template original no Microsoft Word: adaptação da linguagem visual para os sistemas laudadores legados.",
  },

  {
    src: "/images/hiae-triangulacao-pesquisa-1200.webp",

    width: 1200,

    height: 701,

    alt: "Diagrama relacionando questionário, entrevistas médicas e levantamento documental",

    caption:
      "Triangulação de pesquisa: perspectivas de pacientes e médicos combinadas à análise dos documentos e das restrições do serviço.",
  },
]

export const einsteinPresentation: CasePresentationData = {
  title: "Albert Einstein · Consumo de Resultados",

  context: "Saúde · HIAE × Foursys · 2022",

  headline: "Uma linguagem visual modular para laudos heterogêneos.",

  subtitle:
    "Um trabalho coletivo entre pesquisa, conteúdo, interface e viabilidade técnica para facilitar a criação dos laudos e a localização de informações sem simplificar indevidamente o contexto clínico.",

  role: "UX Lead",

  team: "Foursys × Hospital Israelita Albert Einstein",

  scope: "Pesquisa, modelagem da informação e prototipagem",

  keyMetric: "14 famílias de laudos padronizadas",

  kicker: "Saúde · UX Lead",

  hero: einsteinHero,

  nextCase: {
    title: "Itaú Corretora · Hub de Liquidez",

    href: "/cases/itau/hub-liquidez",

    context: "Fintech · Itaú Unibanco · íon for Advisors",
  },

  prevCase: {
    title: "Neoenergia · Service design",

    href: "/cases/neoenergia-conexao-digital",

    context: "Utilities · P&D ANEEL · 34M de pessoas",
  },

  chapters: [
    {
      title: "Organizar resultados sem perder o contexto clínico.",

      content: (
        <>
          <div className="cp-summary">
            <p className="cp-lead">
              Como facilitar a localização e a leitura do laudo sem induzir uma interpretação clínica isolada?
            </p>
            <p>
              Laudos de diferentes laboratórios e hospitais parceiros reuniam informações críticas em estruturas variáveis. O projeto desenhou uma linguagem modular previsível para mais de 80 tipos de exames, permitindo que médicos cruzem resultados, métodos e referências com agilidade, e que pacientes localizem seus dados com facilidade para levar à conversa médica.
            </p>
          </div>
          <CaseMetrics
            items={[
              ["121", "pacientes responderam ao questionário de hábitos de leitura"],

              ["4", "médicos especialistas entrevistados em profundidade"],

              ["14", "entregáveis canônicos e famílias de laudos estruturadas"],
            ]}
          />
          <p>
            A pesquisa quantitativa com 121 pacientes mapeou hábitos de leitura e compreensão de termos médicos, triangulada com entrevistas em profundidade com médicos especialistas para assegurar rigor clínico, conformidade com a LGPD e sigilo médico.
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
              <h3>O desafio prático</h3>
              <p>
                O mesmo laudo precisava funcionar no aplicativo do celular, na tela do consultório e impresso em preto e branco nas impressoras dos hospitais parceiros. Não adiantava criar um visual bonito que travasse os sistemas mais antigos ou ficasse ilegível no papel comum.
              </p>
            </div>
            <div>
              <h3>As regras centrais do projeto</h3>
              <List
                items={[
                  "Resultado e referência lado a lado: o valor do exame e o intervalo considerado normal aparecem sempre juntos, na mesma linha visual.",

                  "Cabeçalho limpo: dados administrativos (como convênio, número da guia e carimbos) foram separados, deixando o foco total no resultado médico.",

                  "Estrutura flexível: o modelo aceita desde exames de sangue curtos de uma linha até relatórios longos de ressonância com laudo descritivo.",
                ]}
              />
            </div>
          </div>
          <CaseFigure
            image={{
              src: "/images/hiae-estado-proposto-anotado.webp",
              width: 2000,
              height: 1076,
              alt: "Laudo proposto anotado demonstrando resultado e valores normais agrupados, e dados administrativos no topo",
              caption:
                "Proposta aprovada: resultado do exame, unidade de medida e valores normais agrupados no mesmo bloco visual; informações administrativas separadas no topo. Dados anonimizados para proteção de privacidade.",
            }}
          />
          <div className="cp-note">
            <h3>Meu papel como UX Lead</h3>
            <p>
              Liderei o alinhamento entre as equipes de design, tecnologia dos hospitais e o corpo clínico do Albert Einstein, garantindo que o novo padrão atendesse tanto aos médicos quanto à realidade prática dos sistemas parceiros.
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
            Para construir esse padrão, analisamos mais de 80 exames reais de diversas especialidades — de análises laboratoriais a exames de imagem. Descobrimos que, apesar de parecerem muito diferentes, todos podiam ser agrupados em apenas 14 tipos de modelos previsíveis.
          </p>
          <List
            items={[
              "Como o médico trabalha: em uma consulta rápida ou no pronto-socorro, ele precisa bater o olho e identificar em 3 segundos se algum número está fora do padrão.",

              "Como o paciente lê: busca o próprio resultado e precisa localizar o que importa para levar à conversa médica, sem se perder em termos técnicos ou fazer interpretações clínicas isoladas.",

              "Limitações dos sistemas: mapeamos o tamanho dos textos e tabelas para garantir que nenhuma palavra ou número ficasse cortado em qualquer impressora.",
            ]}
          />
          <CaseFigure
            image={{
              src: "/images/hiae-estado-atual-anotado.webp",
              width: 2000,
              height: 1076,
              alt: "Laudo anterior anotado mostrando dados espalhados e valores normais longe do resultado",
              caption:
                "Como era antes: informações espalhadas pela página, com o resultado distante dos valores normais e dados administrativos misturados ao texto médico.",
            }}
          />
          <CaseFigure image={einsteinImages[1]} />
          <div className="cp-note">
            <h3>Evitando erros de leitura</h3>
            <p>
              Em saúde, um alinhamento confuso pode induzir a um diagnóstico errado. O resultado, a unidade e o intervalo de referência devem formar um bloco único e inconfundível, fácil de ler até no fim de um plantão cansativo.
            </p>
          </div>
        </>
      ),
    },

    {
      title: "Preservar relações entre resultado, referência e contexto.",

      content: (
        <>
          <blockquote className="cp-quote">
            <p>
              Modular não é simplificar. É manter o contexto clínico no lugar
              onde a pessoa o espera.
            </p>
          </blockquote>
          <CaseFigure
            image={{
              src: "/images/hiae-componente-protrombina-crop.webp",
              width: 1800,
              height: 640,
              alt: "Recorte detalhado do protótipo documentado (v3.0) exibindo os campos de Tempo de Protrombina (RNI) e parâmetros de referência",
              caption:
                "Anatomia do componente no protótipo final (v3.0): exame de Tempo de Protrombina (RNI) com cada parâmetro em sua linha, resultado e valor de referência lado a lado, e ícones que não dependem apenas da cor para indicar normalidade.",
            }}
          />
          <ol className="cp-callout-list">
            <li className="cp-callout-item">
              <span className="cp-callout-badge">1</span>
              <div>
                <strong>examTitle:</strong> Nome do exame e material biológico no topo (ex.: Tempo de Protrombina em plasma).
              </div>
            </li>
            <li className="cp-callout-item">
              <span className="cp-callout-badge">2</span>
              <div>
                <strong>Uma linha por parâmetro:</strong> Cada teste clínico ganha sua própria linha horizontal, evitando que números se misturem.
              </div>
            </li>
            <li className="cp-callout-item">
              <span className="cp-callout-badge">3</span>
              <div>
                <strong>Acessibilidade visual:</strong> Ícones de verificação e alerta acompanham a cor, garantindo leitura segura para daltônicos e na impressão em preto e branco.
              </div>
            </li>
            <li className="cp-callout-item">
              <span className="cp-callout-badge">4</span>
              <div>
                <strong>Resultado e referência alinhados:</strong> O valor medido e o intervalo normal ficam lado a lado, com a unidade de medida sempre visível.
              </div>
            </li>
          </ol>
          <p style={{ fontSize: "0.875rem", color: "var(--cp-muted)", marginBottom: "2rem", lineHeight: 1.5 }}>
            A evolução para a versão 3.0 refinou o espaçamento e a largura de leitura, removeu negritos excessivos que poluíam a página e organizou os dados de identificação em colunas discretas.
          </p>
          <ol className="cp-decisions">
            {[
              [
                "Âncora de leitura imediata",
                "Nome do exame, material, resultado e referência formam o primeiro ponto de contato visual.",
              ],
              [
                "Componentes flexíveis (dataField e examTitle)",
                "Em vez de desenhar uma tela para cada um dos 80+ exames, criamos blocos modulares que acomodam números simples, tabelas ou textos longos.",
              ],
              [
                "Sinais claros e acessíveis",
                "Texto, posição e símbolos trabalham juntos; a cor nunca comunica o status de um exame sozinha.",
              ],
              [
                "Compatibilidade com os sistemas do hospital",
                "Estrutura integrada ao Design System Zera 1.0, com cabeçalhos e rodapés que funcionam tanto nas impressoras dos laboratórios quanto nas telas modernas.",
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
                "Documentação no Design System Zera 1.0: especificações dos componentes dataField e examTitle com tokens de espaçamento e regras de anatomia modular para a engenharia.",
            }}
          />
        </>
      ),
    },

    {
      title: "Uma estrutura única para qualquer tipo de exame.",

      content: (
        <>
          <p>
            Um dos maiores desafios foi garantir que o mesmo padrão visual funcionasse tanto para laudos descritivos com muito texto (como mamografia e biópsias) quanto para tabelas densas cheias de números (como ressonâncias e hemogramas). A nova anatomia organiza a leitura para que o olhar encontre primeiro o resultado principal e, em seguida, os detalhes de técnica e observações.
          </p>
          <div className="cp-gallery">
            <CaseFigure
              image={{
                src: "/images/hiae-laudo-original-recorte.webp",
                width: 1120,
                height: 640,
                alt: "Recorte do laudo original demonstrando texto denso e sem hierarquia visual",
                caption:
                  "Laudo original: texto corrido e denso, onde valores de referência e resultados se misturavam sem hierarquia visual clara.",
              }}
            />
            <CaseFigure
              image={{
                src: "/images/hiae-laudo-proposta-demonstrativa-1600.webp",
                width: 1600,
                height: 1199,
                alt: "Estrutura modular de laudo proposta com áreas bem delimitadas",
                caption:
                  "Proposta modular: anatomia padronizada com áreas bem delimitadas para resultado, valores de referência e contexto clínico.",
              }}
            />
          </div>
          <CaseFigure
            image={{
              ...einsteinImages[0],
              previewCrop: { x: 216, y: 188, width: 718, height: 931 },
              caption:
                "Adaptação para sistemas legados: estrutura compatível com geradores de texto hospitalares e pronta para impressão em preto e branco em folha A4.",
            }}
          />
          <div className="cp-gallery">
            <CaseFigure
              image={{
                src: "/images/hiae-visao-futura-mamografia.webp",
                width: 1340,
                height: 895,
                alt: "Laudo descritivo de mamografia estruturado para tablet e celular",
                caption:
                  "Laudo descritivo (Mamografia): cabeçalho padronizado e seções estruturadas para técnica, indicação clínica e conclusão diagnóstica.",
              }}
            />
            <CaseFigure
              image={{
                src: "/images/hiae-visao-futura-ressonancia.webp",
                width: 1340,
                height: 895,
                alt: "Laudo tabular de ressonância cardiovascular com resultados em tabela no tablet e celular",
                caption:
                  "Laudo tabular (Ressonância): resultados estruturados em colunas limpas, facilitando a comparação de medidas no celular e no tablet.",
              }}
            />
          </div>
          <CaseFigure
            image={{
              src: "/images/hiae-multicanal-web-celular.webp",
              width: 1466,
              height: 900,
              alt: "Mesmo exame exibido na web e no celular, com a mesma ordem mental de leitura",
              caption:
                "Consistência multicanal: o paciente e o médico encontram a mesma hierarquia de leitura no portal web e no aplicativo móvel.",
            }}
          />
        </>
      ),
    },

    {
      title: "Clareza de leitura e diagnóstico clínico: papéis complementares.",

      content: (
        <>
          <p>
            Durante os testes de usabilidade com a nova interface, avaliamos como as pessoas interagiam com o documento em quatro etapas: desde o reconhecimento visual até a interpretação do conteúdo. Os resultados confirmaram que uma boa organização visual facilita a localização dos dados, mas não substitui a conversa com o médico.
          </p>
          <dl className="cp-metrics" style={{ "--metric-columns": 4 } as React.CSSProperties}>
            <div>
              <dt>Identificaram de imediato que se tratava de um laudo médico</dt>
              <dd>81,6%</dd>
            </div>
            <div>
              <dt>Focaram primeiro no nome do exame, resultado e referência</dt>
              <dd>77,8%</dd>
            </div>
            <div>
              <dt>Compreenderam com clareza o objetivo daquele exame</dt>
              <dd>58,8%</dd>
            </div>
            <div>
              <dt>Interpretaram a condição clínica sem apoio de um profissional</dt>
              <dd>56,2%</dd>
            </div>
          </dl>
          <div className="cp-note">
            <h3>Conclusão do teste</h3>
            <p>
              A interface cumpre o seu papel ao eliminar o ruído visual e destacar o que é prioritário: mais de 80% das pessoas encontram as informações sem esforço. Ao mesmo tempo, o resultado reforça a premissa ética do projeto: o laudo deve apresentar os dados com clareza para que o paciente converse melhor com seu médico, e não induzir um autodiagnóstico isolado.
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
            <summary>Contexto e documentação do projeto</summary>
            <div>
              <p>
                Projeto desenvolvido em 2022 pelo time de design e produto em parceria com o Hospital Israelita Albert Einstein. As especificações de componentes, fluxos e registros de pesquisa estão documentados nas fontes oficiais do projeto.
              </p>
              <Sources project="einstein" />
            </div>
          </details>
          <details>
            <summary>Autoria e time multidisciplinar</summary>
            <div>
              <p>
                Israel Rozar — UX Lead. Atuação em pesquisa qualitativa e quantitativa, arquitetura da informação, estruturação dos componentes no Design System e alinhamento com equipes médicas e de tecnologia da Foursys e do Einstein.
              </p>
            </div>
          </details>
          <details>
            <summary>Ética e conformidade na pesquisa</summary>
            <div>
              <p>
                A pesquisa com pacientes seguiu diretrizes de proteção de dados (LGPD) e anonimização de informações. A etapa quantitativa com 121 participantes foi combinada com entrevistas em profundidade com médicos laudadores de diferentes especialidades (cardiologia, radiologia e hematologia), garantindo conformidade com as rotinas hospitalares e as normas sanitárias vigentes.
              </p>
            </div>
          </details>
        </div>
      ),
    },
  ],
}

const claroHero: CaseImage = {
  src: "/images/claro-capa-editorial-1600.webp",
  width: 2400,
  height: 1327,
  alt: "Visão editorial multicanal da Ativação Simplificada Claro: interfaces desktop e mobile com resumo financeiro integrado",
  caption:
    "Ecossistema multicanal: composição de interfaces desktop e mobile com carrinho de contratação em tempo real e detalhamento transparente de planos.",
}

const claroImages: CaseImage[] = [
  {
    src: "/images/claro-ativacao-desktop.webp",
    width: 775,
    height: 486,
    alt: "Ativação desktop com resumo financeiro lateral",
    caption:
      "Ativação e resumo da oferta: composição financeira visível durante a escolha do produto.",
  },
  {
    src: "/images/claro-workshop.webp",
    width: 720,
    height: 720,
    alt: "Workshop do projeto com post-its na parede",
    caption: "Registro de workshop colaborativo do acervo original.",
  },
  {
    src: "/images/claro-jornadas.webp",
    width: 720,
    height: 720,
    alt: "Mapa da jornada de troca de chip no Miro",
    caption:
      "Validações, etapas da troca de chip, resumo e oferta organizados na jornada.",
  },
  {
    src: "/images/claro-multicanal.webp",
    width: 1376,
    height: 932,
    alt: "Composição de interfaces desktop e mobile",
    caption:
      "Propostas históricas para desktop e mobile, com agrupamentos de oferta e serviços.",
  },
  {
    src: "/images/claro-detalhe-linha.webp",
    width: 775,
    height: 486,
    alt: "Detalhe da linha com dados do cliente e grupos expansíveis",
    caption:
      "Cliente, linha, plano e fatura agrupados, com acesso às jornadas relacionadas.",
  },
  {
    src: "/images/claro-confirmacao-mobile.webp",
    width: 280,
    height: 606,
    alt: "Confirmação mobile da troca de chip",
    caption:
      "Confirmação mobile reúne cliente, linha, chip e promoção. Exportação original de 280 px.",
  },
]

export const claroPresentation: CasePresentationData = {
  title: "Claro · Ativação simplificada",

  context: "Telecom · Claro Brasil · acervo de 2017–2018",

  headline: "Simplificando o atendimento em múltiplos canais.",

  subtitle:
    "Redesenho da experiência de vendas para profissionais da operação comercial.",

  role: "UX/UI Designer",

  team: "Design, stakeholders e profissionais da operação",

  scope: "Discovery, fluxos e interfaces desktop e mobile",

  keyMetric: "Atendimento unificado multicanal",

  kicker: "Telecom · UX corporativo",

  hero: claroHero,

  nextCase: {
    title: "Neoenergia · Service design",

    href: "/cases/neoenergia-conexao-digital",

    context: "Utilities · P&D ANEEL · 34M de pessoas",
  },

  prevCase: {
    title: "Itaú Corretora · Hub de Liquidez",

    href: "/cases/itau/hub-liquidez",

    context: "Fintech · Itaú Unibanco · íon for Advisors",
  },

  chapters: [
    {
      title:
        "Redesenho da operação comercial e redução de atrito na venda multicanal.",

      content: (
        <>
          <div className="cp-summary">
            <p>
              Organizar uma operação comercial complexa para que o atendente
              consiga consultar o cliente, configurar planos e aparelhos e
              acompanhar a jornada de ponta a ponta sem rupturas de contexto.
            </p>
            <p>
              O projeto integrou discovery de campo em lojas físicas e canais
              remotos, decomposição de jornadas críticas de telecom e propostas
              estruturadas de interface para desktop e mobile, organizando
              regras de negócio e resumo da composição financeira.
            </p>
          </div>
          <CaseMetrics
            items={[
              ["20", "entrevistas em profundidade"],

              ["22", "jornadas de atendimento mapeadas"],

              ["70", "oportunidades de melhoria levantadas"],
            ]}
          />
          <p>
            Essas métricas refletem a profundidade da fase de discovery e imersão operacional em lojas e centrais de televendas, fundamentando as decisões de arquitetura de informação e simplificação das esteiras de venda.
          </p>
        </>
      ),
    },

    {
      title:
        "Uma operação de alta densidade dividida entre balcão físico e mobilidade.",

      content: (
        <>
          <div className="cp-columns">
            <div>
              <h3>O cenário</h3>
              <p>
                A rotina comercial precisava conciliar necessidades de
                atendentes de loja, consultores em trânsito e as regras de
                negócio de telecom, com grande volume de dados por transação.
              </p>
            </div>
            <div>
              <h3>O desafio</h3>
              <p>
                Como apoiar a continuidade do atendimento e tornar os dados
                cadastrais, técnicos e financeiros compreensíveis em telas de
                desktop e dispositivos móveis?
              </p>
            </div>
          </div>
          <div className="cp-note">
            <h3>Minha contribuição documentada</h3>
            <p>
              Atuação em UX/UI, da imersão inicial e síntese de pesquisa à
              definição de fluxos de navegação, prototipação de alta fidelidade
              e entrega visual para engenharia.
            </p>
          </div>
        </>
      ),
    },

    {
      title:
        "Compreender a rotina real dos atendentes antes de desenhar interfaces.",

      content: (
        <>
          <p>
            O discovery reuniu benchmarking competitivo, 20 entrevistas com
            profissionais e lideranças executivas, três dias de workshops
            imersivos e a formulação de dez personas operacionais. Os materiais
            selecionados demonstram o processo colaborativo e o mapeamento
            detalhado da jornada de troca de chip.
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
      title:
        "Decomposição de 22 jornadas de atendimento e aprendizados operacionais.",

      content: (
        <>
          <p>
            O acervo documenta a decomposição de 22 jornadas e propostas para
            consultar clientes, configurar ofertas e confirmar operações. Ele
            permite discutir arquitetura de informação e continuidade omnicanal
            em escala.
          </p>
          <p>
            A padronização das 22 jornadas eliminou redundâncias entre a consulta cadastral, a configuração do plano e a formalização do contrato. A interface unificada garantiu que tanto o atendente de loja física quanto o operador de televendas trabalhassem com a mesma clareza de regras e velocidade de confirmação.
          </p>
          <div className="cp-note">
            <h3>Aprendizado de design</h3>
            <p>
              Uma interface de atendimento comercial precisa manter o contexto
              do cliente e da oferta sempre visíveis. O design deve reduzir a
              carga cognitiva do operador e, ao mesmo tempo, garantir
              transparência absoluta para o consumidor final.
            </p>
          </div>
        </>
      ),
    },

    {
      title:
        "Navegação progressiva, resumo financeiro visível e preservação do contexto do cliente.",

      content: (
        <>
          <CaseFigure
            image={{
              src: "/images/claro-busca-cliente.webp",
              width: 775,
              height: 486,
              alt: "Tela de busca de cliente do sistema de ativação, com campo de CPF e botão de busca",
              caption:
                "Ponto de entrada da ativação: a busca por CPF inicia o atendimento com dados sintetizados para conformidade com a LGPD.",
            }}
          />
          <ol className="cp-decisions">
            {[
              [
                "Navegação progressiva por etapas",

                "Grupos expansíveis e etapas numeradas orientam o operador em fluxos extensos sem poluição visual.",
              ],

              [
                "Preservação do contexto do cliente",

                "Cabeçalho fixo com dados da linha, status cadastral e atalhos para jornadas frequentes apoiam a continuidade da conversa.",
              ],

              [
                "Composição financeira em tempo real",

                "O resumo lateral aproxima produtos, descontos aplicados e valores finais durante toda a configuração do plano.",
              ],
            ].map(([title, text]) => (
              <li key={title}>
                <h3>{title}</h3>
                <p>{text}</p>
              </li>
            ))}
          </ol>
        </>
      ),
    },

    {
      title: "Da jornada do chip às interfaces desktop e mobile padronizadas.",

      content: (
        <>
          <p>
            As propostas apresentam ativação, detalhe da linha e confirmação,
            com adaptações responsivas entre desktop e mobile. A sequência
            evidencia consistência de padrões, legibilidade de dados e clareza
            nos estados operacionais.
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
      title:
        "Governança do projeto, colaboração multidisciplinar e impacto.",

      content: (
        <div className="cp-appendix">
          <details open>
            <summary>Arquivos e versões</summary>
            <div>
              <p>
                Acervo Claro documentado pelo autor: registros de workshops, mapa
                de jornada de troca de chip, telas de ativação, detalhe da linha
                e confirmação mobile.
              </p>
              <p>
                O documento de migração desktop identifica V.2 de 10/05/2018; o
                PDF mobile foi atualizado em 11/06/2018.
              </p>
              <Sources project="claro" />
            </div>
          </details>
          <details>
            <summary>Colaboração e equipe</summary>
            <div>
              <p>
                Israel Rozar — UX/UI Designer, em estreita colaboração com lideranças
                de produto, engenharia de sistemas e operadores comerciais de loja
                e televendas da Claro Brasil.
              </p>
            </div>
          </details>
        </div>
      ),
    },
  ],
}

export function EinsteinPresentation() {
  return <CasePresentation data={einsteinPresentation} />
}

export function ClaroPresentation() {
  return <CasePresentation data={claroPresentation} />
}

export const neoenergiaPresentation: CasePresentationData = {
  title: "Neoenergia · Service design",

  context: "Neoenergia · EY × Livework · P&D ANEEL · 2020",

  headline:
    "Conectar a jornada digital ao serviço que acontece no mundo físico.",

  subtitle:
    "Discovery e service design para organizar problemas, jornadas e oportunidades no atendimento de distribuidoras de energia.",

  role: "Senior Product Designer / Service Designer",

  team: "EY Business Transformation × Livework e áreas da Neoenergia",

  scope: "Pesquisa, jornadas atuais, blueprints e visão futura de serviço",

  keyMetric: "5 Blueprints de Serviço P&D ANEEL",

  kicker: "Energia · Service design",

  hero: {
    src: "/images/neoenergia-capa-conexao-digital.webp",

    width: 1600,

    height: 900,

    alt: "Capa oficial do projeto P&D Conexão Digital Neoenergia com consórcio EY e Livework",

    caption:
      "Projeto P&D Conexão Digital ANEEL: Experiência do Consumidor e Service Design para o Grupo Neoenergia (Iberdrola Brasil).",
  },

  prevCase: {
    title: "Claro · Ativação simplificada",

    href: "/cases/claro-ativacao-simplificada",

    context: "Telecom · Claro Brasil · 34M de clientes",
  },

  nextCase: {
    title: "Einstein · Laudos médicos",

    href: "/cases/einstein-laudos",

    context: "Saúde · HIAE × Foursys · 2022",
  },

  chapters: [
    {
      title:
        "Unificação da infraestrutura de atendimento para 34 milhões de pessoas.",

      content: (
        <>
          <div className="cp-summary">
            <p>
              Iniciativa de discovery e transformação de serviços para conectar
              canais de atendimento, processos internos e experiência do
              consumidor de energia para o Grupo Neoenergia (Iberdrola Brasil),
              integrando 4 grandes distribuidoras — <strong>Elektro</strong>{" "}
              (SP/MS), <strong>Coelba</strong> (BA), <strong>Celpe</strong> (PE)
              e <strong>Cosern</strong> (RN).
            </p>
            <p>
              Desenvolvido no âmbito do programa de P&D Estratégico ANEEL, o
              consórcio EY Business Transformation e Livework realizou
              diagnóstico de campo, auditou os silos internos de backstage e
              modelou os blueprints de serviço To-Be para mitigar atritos de
              faturamento e operação.
            </p>
          </div>
          <CaseMetrics
            items={[
              ["4", "distribuidoras no contexto do projeto"],

              ["5 estágios", "ciclo de vida em blueprints"],

              ["118 ideias", "priorizadas na matriz de valor"],
            ]}
          />
          <p>
            A documentação histórica audita 34 milhões de habitantes e 13,9
            milhões de clientes nas áreas de concessão em 18 estados. Esses
            dados contextualizam a escala real do ecossistema sob regulação da
            ANEEL.
          </p>
        </>
      ),
    },

    {
      title:
        "Cadeia de serviços fragmentada em um ecossistema de infraestrutura crítica.",

      content: (
        <>
          <div className="cp-columns">
            <div>
              <h3>Pessoas e contexto</h3>
              <p>
                Consumidores precisam contratar, pagar, pedir suporte, alterar e
                encerrar serviços. Atendentes, áreas internas e equipes de campo
                participam dessas jornadas e influenciam a continuidade do
                atendimento.
              </p>
            </div>
            <div>
              <h3>Problema de design</h3>
              <p>
                Como compreender os atritos ao longo do serviço e estruturar uma
                experiência futura que considere o atendimento digital, a
                operação interna e as dependências do mundo físico?
              </p>
            </div>
          </div>
          <div className="cp-note">
            <h3>Recorte de atuação</h3>
            <p>
              Product Design e Service Design no contexto de Business
              Transformation da EY: compreensão de jornadas, pesquisa
              qualitativa e organização de problemas e oportunidades, em
              colaboração com Livework e áreas da Neoenergia.
            </p>
          </div>
        </>
      ),
    },

    {
      title:
        "Auditoria de backstage: quando a insatisfação com a fatura revela silos operacionais.",

      content: (
        <>
          <p>
            A documentação de governança estrutura contextualização do negócio,
            entendimento das jornadas atuais, pesquisa, desenho da jornada
            futura e roadmap. Registros de campo e blueprints aproximam a
            perspectiva do consumidor das atividades internas que sustentam o
            serviço.
          </p>
          <List
            items={[
              "Contextualização do setor e do negócio para interpretar necessidades e restrições regulatórias.",

              "Mapeamento de jornadas e processos atuais, com atenção às transições entre canais físicos e digitais.",

              "Organização de dores e oportunidades para discutir uma visão futura com as diretorias envolvidas.",
            ]}
          />
          <p>
            A leitura de serviço evita reduzir o diagnóstico a telas: uma
            informação pouco clara no canal digital pode depender de uma regra,
            de um processo interno ou de uma atividade em campo.
          </p>
        </>
      ),
    },

    {
      title:
        "Os 5 estágios do ciclo de vida do cliente mapeados em Service Blueprints.",

      content: (
        <>
          <p>
            O mapa de jornada futura organiza o ciclo de vida em cinco
            macroetapas estruturadas em pranchas detalhadas de Service
            Blueprint:
          </p>
          <List
            items={[
              "1. Contrato e instalo: busca de informações, contratação, adequação e ligação nova.",

              "2. Uso e pago: consumo, acompanhamento, autoleitura e faturamento.",

              "3. Preciso de suporte: necessidade de ajuda, interrupção e resolução de problemas.",

              "4. Mudo o contrato: alterações cadastrais, portabilidade ao Mercado Livre e geração solar.",

              "5. Abandono: encerramento do vínculo, prevenção de inadimplência e desdobramentos.",
            ]}
          />
          <div className="cp-gallery">
            <CaseFigure
              image={{
                src: "/images/neoenergia-blueprint-crop-contrato-1600.webp",
                width: 1600,
                height: 900,
                alt: "Recorte editorial em alta resolução do Blueprint 1: Contrato e Instalação com jornada do cliente e pontos de contato da operação",
                caption:
                  "Recorte editorial do Blueprint 1 (Contrato e Instalação): visão de alta densidade da jornada do cliente, evidências físicas e pontos de contato da linha de frente.",
              }}
            />
            <CaseFigure
              image={{
                src: "/images/neoenergia-blueprint-2-uso-pago.webp",

                width: 1414,

                height: 4480,

                alt: "Service Blueprint detalhado da etapa 2: Uso e Pago — Consumo, faturamento e autoleitura",

                caption:
                  "Artefato original de Service Blueprint: Macro-etapa 2. Uso e Pago (ações, criticidade, highlights por 3 perfis de clientes, análise interna de processos e oportunidades).",
              }}
            />
            <CaseFigure
              image={{
                src: "/images/neoenergia-blueprint-1-contrato-instalo.webp",

                width: 2000,

                height: 5200,

                alt: "Service Blueprint da etapa 1: Contrato e Instalo",

                caption:
                  "Artefato original de Service Blueprint: Macro-etapa 1. Contrato e Instalo (pesquisa de informações, adequação e ligação nova).",
              }}
            />
            <CaseFigure
              image={{
                src: "/images/neoenergia-jornada-futuro-tobe.webp",

                width: 2000,

                height: 1200,

                alt: "Service Blueprint da Jornada do Futuro To-Be",

                caption:
                  "Artefato original da Jornada do Futuro (To-Be): blueprint de serviço integrado omnicanal e visão consolidada de ganhos.",
              }}
            />
          </div>
        </>
      ),
    },

    {
      title:
        "Desburocratização de backoffice antes de redesenho de portal e Design System multi-tenant.",

      content: (
        <ol className="cp-decisions">
          {[
            [
              "Mapear antes de propor",

              "A jornada atual organiza atores, etapas e dependências para que uma oportunidade de interface seja discutida no contexto do serviço.",
            ],

            [
              "Conectar frente de atendimento e operação",

              "Os blueprints aproximam ações do consumidor, canais e atividades internas. Essa relação permite discutir causas e responsabilidades nas transições.",
            ],

            [
              "Organizar oportunidades por jornada",

              "A visão futura reúne propostas ao longo do ciclo de vida, apoiando a discussão de prioridades e a construção de um roadmap.",
            ],
          ].map(([title, description]) => (
            <li key={title}>
              <h3>{title}</h3>
              <p>{description}</p>
            </li>
          ))}
        </ol>
      ),
    },

    {
      title:
        "Matriz de 118 ideias priorizadas e baseline para o plano diretor de inovação.",

      content: (
        <>
          <h3>Contribuições do trabalho de serviço</h3>
          <List
            items={[
              "Organização de jornadas atuais e dependências do atendimento em 11 canais.",

              "Blueprints e visão futura ao longo do ciclo de vida do consumidor.",

              "Matriz de 118 ideias estruturadas para priorização executiva e discussão de roadmap.",
            ]}
          />
          <CaseFigure
            image={{
              src: "/images/neoenergia-matriz-118-ideias.webp",

              width: 2000,

              height: 1195,

              alt: "Matriz de Priorização com 118 Ideias de Inovação",

              caption:
                "Matriz de Priorização: 118 ideias estruturadas e classificadas por impacto no negócio versus valor percebido pelo consumidor.",
            }}
          />
          <div className="cp-note">
            <h3>Aprendizado central</h3>
            <p>
              Em serviços essenciais, a experiência digital depende do que
              acontece depois do clique. Tornar visíveis as relações entre
              consumidor, atendimento e operação é parte do trabalho de design.
            </p>
          </div>
        </>
      ),
    },

    {
      title:
        "Fontes oficiais de P&D ANEEL, governança executiva e equipe EY × Livework.",

      content: (
        <div className="cp-appendix">
          <details open>
            <summary>Referências do projeto</summary>
            <div>
              <Sources project="neoenergia" />
            </div>
          </details>
          <details>
            <summary>Colaboração</summary>
            <div>
              <p>
                Israel Rozar — Senior Product Designer / Service Designer, no
                contexto de Business Transformation da EY, em colaboração com
                Livework e áreas da Neoenergia. Jornadas, blueprints e propostas
                são entregas de equipe multidisciplinar.
              </p>
            </div>
          </details>
          <details>
            <summary>Governança e impacto estratégico</summary>
            <div>
              <p>
                Os blueprints de serviço e a matriz de 118 oportunidades serviram
                como baseline estratégico aprovado pelas diretorias de operação e
                atendimento do Grupo Neoenergia no âmbito do programa de P&D
                Estratégico ANEEL, orientando as esteiras de inovação e unificação
                de canais das 4 distribuidoras.
              </p>
            </div>
          </details>
        </div>
      ),
    },
  ],
}

export function NeoenergiaPresentation() {
  return <CasePresentation data={neoenergiaPresentation} />
}

const itauNarratives = {
  vencimentos: {
    summary:
      "Conectar a identificação de vencimentos à atuação do especialista. A experiência organiza eventos financeiros, contexto do cliente e registro de ações para apoiar o acompanhamento da carteira.",

    users:
      "Especialistas de investimentos que acompanham clientes encarteirados e gestores que precisam compreender a atuação das equipes.",

    contribution:
      "Arquitetura de consulta, organização de filtros e tabelas, estados da interface e continuidade entre identificação do evento e atuação. O recorte de design é apresentado junto às funcionalidades descritas na base de conhecimento do produto.",

    research:
      "Os arquivos de exploração e handoff mostram a evolução da consulta e dos estados. A base de conhecimento explica o registro de ações, os pontos de entrada e a visão gerencial. A interface de Gestão de liquidez, nó 582:12520, é a versão mais recente confirmada pelo autor; os demais frames são tratados como histórico.",

    constraints: [
      "Distinguir vencimentos, eventos futuros e Open Finance sem fragmentar a lógica de consulta.",

      "Preservar a relação entre data, produto, valor, cliente e situação da atuação em uma tabela densa.",

      "Acomodar diferentes pontos de entrada: panorama, operações, contexto do cliente e acesso direto.",
    ],

    decisions: [
      [
        "Reutilizar a lógica de consulta",

        "Abas distinguem contextos financeiros enquanto busca, filtros e tabela mantêm um padrão comum. Isso preserva as diferenças entre os eventos sem exigir reaprendizado de toda a navegação.",
      ],

      [
        "Tornar o recorte da lista explícito",

        "Período, produto, carteira, status e identificação do cliente ajudam a delimitar a consulta. A leitura dos filtros precisa acompanhar a interpretação de totais e estados.",
      ],

      [
        "Conectar consulta e atuação",

        "A base de conhecimento descreve registro de valor, comentários e informações de contato. O evento deve permanecer relacionado ao cliente durante a ação e no acompanhamento posterior.",
      ],
    ],

    flow: [
      "Localizar vencimentos da carteira a partir de um ponto de entrada do IFA.",

      "Delimitar período e universo de clientes, produtos e status.",

      "Interpretar data, valor e contexto do evento antes de atuar.",

      "Registrar a ação e acompanhar a situação do vencimento; a visão gerencial agrega a atuação das equipes.",
    ],

    delivery: [
      "Interface mais recente de consulta identificada e distinguida das explorações anteriores.",

      "Estrutura compartilhada de busca, filtros, dados do cliente e estados da atuação.",

      "Documentação de componentes, estados vazios e preparação para handoff.",
    ],

    learning:
      "A utilidade de uma tabela financeira depende de ligar o sinal à ação. Mostrar um vencimento é apenas parte da tarefa: o especialista também precisa interpretar o contexto e reconhecer o que já foi tratado.",

    boundary:
      "Os dados cadastrais e valores financeiros apresentados na interface foram sintetizados para preservação do sigilo bancário e conformidade com a LGPD, mantendo fidelidade estrita às regras de ordenação de vencimentos, filtros operacionais e contratos de dados acordados com os assessores.",

    scope: "Consulta, filtros, estados e registro de atuação",
  },

  "hub-liquidez": {
    summary:
      "Reunir posição atual, variação prevista e liquidez projetada em uma visão que ajude o especialista a decidir sobre quais clientes atuar, mantendo a origem e o horizonte dos valores compreensíveis.",

    users:
      "Especialistas de investimentos que acompanham recursos disponíveis e oportunidades de atuação em suas carteiras.",

    contribution:
      "Hierarquia dos dados financeiros, distinção temporal dos valores e conexão entre visão de carteira, lista de clientes, filtros e estado da atuação.",

    research:
      "A leitura da interface confirmada, nó 3:14068 de Gestão de liquidez, mostra a relação entre posição atual, projeção e clientes para atuação. O texto da própria solução conecta o Hub aos valores de liquidez imediata identificados pelo Cofrinho IFA e ao acompanhamento de recursos que permanecem em conta.",

    constraints: [
      "Diferenciar dinheiro disponível agora de uma projeção para outra janela.",

      "Manter a origem Itaú e Open Finance explícita durante a leitura.",

      "Apresentar atualização do dado e status de atuação sem confundi-los com disponibilidade financeira.",
    ],

    decisions: [
      [
        "Separar posição, variação e projeção",

        "O resumo apresenta total disponível agora, variação prevista e liquidez projetada. A relação visual entre os três valores explicita que representam conceitos e momentos diferentes.",
      ],

      [
        "Dar contexto à janela de tempo",

        "Fim do dia, 7 dias e 30 dias delimitam a projeção. A janela selecionada acompanha o título do valor projetado para reduzir interpretações fora do período.",
      ],

      [
        "Ligar o resumo à fila de trabalho",

        "A tabela aproxima cliente, carteira, agência/conta, disponível agora, total projetado e status. Busca, origem e faixas de valor permitem delimitar o universo antes da ação.",
      ],
    ],

    flow: [
      "Consultar a posição da carteira e a informação de atualização.",

      "Selecionar a janela da projeção e comparar disponível, variação e total projetado.",

      "Filtrar por origem e faixa de valor ou localizar um cliente.",

      "Aprofundar o cliente preservando a leitura do valor e do estado de atuação.",
    ],

    delivery: [
      "Interface que conecta resumo de liquidez e clientes para atuação.",

      "Distinção visual de origem, janela temporal e situação do atendimento.",

      "Busca e filtros posicionados junto à tabela operacional.",
    ],

    learning:
      "Priorizar uma oportunidade exige explicar o dado. A hierarquia deve permitir distinguir valor observado, variação conhecida e projeção antes de sugerir uma ação ao especialista.",

    boundary:
      "Os dados e valores numéricos apresentados na interface foram sintetizados para preservação do sigilo bancário, mantendo fidelidade estrita à hierarquia de saldos, filtros, status operacionais e regras de visualização validadas com os especialistas.",

    scope: "Hierarquia financeira, projeção e clientes para atuação",
  },

  movimentacoes: {
    summary:
      "Preservar a continuidade operacional na transição do Extrato EA para o IFA. A solução mantém o saldo provisionado visível no cabeçalho entre jornadas; Movimentações concentra a consulta detalhada e o contexto de CEP, CEP Plus e limite.",

    users:
      "Assessores e especialistas que precisam consultar lançamentos, compreender saldos e explicar movimentações de seus clientes.",

    contribution:
      "Arquitetura da informação, comparação de alternativas de visibilidade do saldo e definição da relação entre contexto financeiro persistente e consulta detalhada.",

    research:
      "A documentação de discovery registra alternativas para acomodar o Extrato EA no IFA. A base de conhecimento detalha conta corrente, investimentos e conta gráfica. A solução final de arquitetura adotada neste relato segue a confirmação explícita do autor: provisionado persistente, com CEP, CEP Plus e limite contextualizados em Movimentações.",

    constraints: [
      "O saldo provisionado é necessário em diferentes jornadas e não pode depender de troca de aba.",

      "Conta corrente, investimentos e conta gráfica têm informações próprias e precisam permanecer distinguíveis.",

      "Consulta por período, busca e ordenação devem manter contexto suficiente para interpretar os lançamentos.",
    ],

    decisions: [
      [
        "Manter o provisionado no cabeçalho",

        "O acesso transversal evita exigir navegação até Movimentações para consultar um saldo necessário em outras tarefas. Esta é a solução confirmada pelo autor.",
      ],

      [
        "Contextualizar os limites em Movimentações",

        "CEP, CEP Plus e limite permanecem junto ao aprofundamento financeiro. A distinção preserva a função do cabeçalho sem transportar todo o extrato para a navegação global.",
      ],

      [
        "Separar domínios com consulta consistente",

        "A base de conhecimento distingue lançamentos de conta corrente, movimentos de investimentos e conta gráfica. Período, busca e ordenação apoiam a consulta, respeitando os dados específicos de cada domínio.",
      ],
    ],

    flow: [
      "Consultar o saldo provisionado no cabeçalho durante diferentes jornadas.",

      "Acessar Movimentações para aprofundar conta corrente, investimentos ou conta gráfica.",

      "Delimitar período e localizar lançamentos pela descrição e demais opções disponíveis no módulo.",

      "Interpretar datas, valores e detalhes da operação com os limites no contexto de Movimentações.",
    ],

    delivery: [
      "Definição da relação entre informação persistente e informação contextual.",

      "Registro das alternativas de arquitetura e distinção da solução escolhida.",

      "Organização da consulta financeira em domínios com diferentes níveis de detalhe.",
    ],

    learning:
      "A informação usada entre jornadas deve acompanhar o trabalho. Concentrar tudo em uma página especializada pode preservar a organização interna e, ainda assim, dificultar uma tarefa transversal.",

    boundary:
      "Os lançamentos de extrato e valores apresentados foram sintetizados para conformidade com o sigilo bancário, preservando com rigor a hierarquia da informação entre o saldo provisionado no cabeçalho e os módulos detalhados de conta corrente e investimentos.",

    scope: "Arquitetura do extrato e contexto financeiro transversal",
  },

  campanhas: {
    summary:
      "Conectar configuração, execução comercial e acompanhamento gerencial. O sistema de campanhas permite direcionar ações a especialistas e clientes específicos, tornando público, vigência e situação da atuação parte da experiência.",

    users:
      "Administradores de backoffice que configuram campanhas; especialistas que atuam com os clientes; gestores que acompanham a execução das equipes.",

    contribution:
      "Organização dos fluxos de configuração, consulta e manutenção, hierarquia dos dados e cobertura de estados. O relato também conecta esse recorte de interface aos três perfis descritos na base de conhecimento.",

    research:
      "Os screenflows e a exploração de configuração explicam informações gerais, público, campos personalizados e estados de processamento. A base de conhecimento amplia o contexto: administração, execução pelo especialista e acompanhamento por hierarquia gerencial são partes do mesmo serviço.",

    constraints: [
      "Combinar público, vigência e ativação para controlar a visibilidade da campanha.",

      "Acomodar importação de base, processamento e estados de erro sem confundir configuração com execução.",

      "Distinguir permissões e tarefas de administradores, especialistas e gestores.",
    ],

    decisions: [
      [
        "Configurar antes de disponibilizar",

        "Nome, descrição, tipo, categoria, público e vigência definem o contexto da campanha. A ativação determina sua visibilidade para o público de especialistas.",
      ],

      [
        "Explicitar estado e consequência",

        "Carregamento, vazio, processamento e erro orientam a leitura da base e as ações de manutenção. A experiência precisa tornar reconhecível quando uma campanha pode ser disponibilizada ou retirada.",
      ],

      [
        "Conectar atuação e acompanhamento",

        "A documentação descreve evolução de Pendente para Em andamento e Atuado, com valor e comentários. Gestores acompanham atuações consolidadas conforme a hierarquia organizacional; atuação registrada não equivale automaticamente a conversão de vendas.",
      ],
    ],

    flow: [
      "O administrador define campanha, público, vigência e informações da base.",

      "A base é importada e seu processamento é acompanhado; a campanha é ativada para o público definido.",

      "O especialista consulta campanhas e clientes e registra a atuação.",

      "O gestor acompanha a execução por campanha e período dentro de sua hierarquia.",
    ],

    delivery: [
      "Fluxos de configuração, consulta e manutenção organizados em screenflows.",

      "Exploração de informações gerais, público e campos personalizados.",

      "Cobertura de estados que orientam leitura e ação na administração da campanha.",
    ],

    learning:
      "Uma operação em lote depende da continuidade entre quem prepara a base, quem executa a ação e quem acompanha o trabalho. O estado da campanha precisa fazer sentido nos três contextos.",

    boundary:
      "As parametrizações e bases de clientes exibidas foram anonimizadas para conformidade com a LGPD, mantendo fidelidade estrita à taxonomia de campanhas, regras de elegibilidade por carteira e estados de processamento validados com a equipe de operações.",

    scope: "Configuração, consulta, estados e acompanhamento de atuação",
  },

  "registros-atendimento": {
    summary:
      "Apoiar a documentação de atendimentos e a recuperação de contexto por meio de resumos assistidos por inteligência artificial. A solução posiciona os resumos dos atendimentos recentes no fluxo de trabalho do assessor, acelerando a contextualização sem abrir mão da revisão humana.",

    users:
      "Assessores e especialistas de investimento que precisam retomar o histórico do cliente com agilidade e documentar os pontos acordados em cada contato.",

    contribution:
      "Arquitetura de interação entre a consulta ao histórico recente e o apoio à redação do registro. Definição do modelo de supervisão humana para garantir integridade e conformidade das notas de atendimento.",

    research:
      "O mapeamento da rotina dos assessores identificou que a transição entre atendimentos gerava perda de contexto e sobrecarga de digitação. A solução estruturou resumos em tópicos objetivos dos últimos 5 atendimentos e sugestões automáticas de ata para validação do profissional.",

    constraints: [
      "Garantir que o conteúdo sugerido pela IA seja sempre revisado e confirmado pelo especialista antes de ser gravado no prontuário do cliente.",

      "Preservar a fidelidade técnica de termos financeiros, evitando alucinações ou omissão de direcionamentos de carteira.",

      "Manter o tempo de recuperação de histórico compatível com o ritmo ágil das interações de assessoria.",
    ],

    decisions: [
      [
        "Contextualização imediata via histórico recente",
        "Acesso direto aos 5 resumos anteriores no painel lateral do cliente, permitindo retomar assuntos pendentes sem abrir múltiplos registros manuais.",
      ],

      [
        "Supervisão e validação humana obrigatória",
        "O texto sugerido funciona como minuta preliminar estruturada; a interface exige a confirmação ativa do especialista antes de salvar a nota de atendimento.",
      ],

      [
        "Critérios de qualidade focados em precisão e conformidade",
        "A avaliação da ferramenta prioriza a precisão das orientações registradas e a mitigação de erros, e não apenas o tempo economizado na digitação.",
      ],
    ],

    flow: [
      "Consultar os resumos dos atendimentos anteriores antes de iniciar o contato.",

      "Utilizar a sugestão automática de tópicos para estruturar o resumo da conversa.",

      "Revisar, editar e confirmar o registro no prontuário financeiro do cliente.",
    ],

    delivery: [
      "Arquitetura da informação integrando histórico recente e campo de registro.",

      "Diretrizes de interação para assistência de IA generativa com supervisão humana.",

      "Critérios de validação e governança de dados para ferramentas de produtividade.",
    ],

    learning:
      "Em ferramentas de assessoria financeira, a inteligência artificial gera valor real quando reduz a burocracia sem transferir a responsabilidade. O especialista permanece no centro da decisão, com a IA atuando como apoio de síntese.",

    boundary:
      "Os registros e notas de atendimento apresentados são anonimizados para conformidade com a LGPD e o sigilo bancário, demonstrando a arquitetura de interação assistida validada com os times de negócio.",

    scope: "Arquitetura de interação para resumos assistidos por IA e governança de notas",
  },
}

export function ItauPresentation() {
  const { caseSlug = "" } = useParams()

  const isKnownCase = (slug: string) =>
    Object.prototype.hasOwnProperty.call(cases, slug) &&
    Object.prototype.hasOwnProperty.call(itauNarratives, slug)

  if (!isKnownCase(caseSlug)) return <NotFound />

  const project = cases[caseSlug]

  const story = itauNarratives[(caseSlug as keyof typeof itauNarratives)]

  const order = [
    "vencimentos",

    "hub-liquidez",

    "movimentacoes",

    "campanhas",

    "registros-atendimento",
  ]

  const index = order.indexOf(caseSlug)

  const target = (slug: string): CaseNavTarget => ({
    title: cases[slug].title,

    href: `/cases/itau/${slug}`,

    context: "Itaú · Design de produto",
  })

  const visuals = project.visuals || []

  const kbNodes: Record<string, string> = {
    vencimentos: "593-126008",

    movimentacoes: "593-126014",

    campanhas: "593-125976",
  }

  const itauKeyMetrics: Record<string, string> = {
    vencimentos: "Visão canônica de proventos e agenda",
    "hub-liquidez": "Consolidação de composição de liquidez",
    movimentacoes: "Transição Extrato EA para IFA",
    campanhas: "Operação e parametrização em lote",
    "registros-atendimento": "Resumos assistidos por IA com supervisão",
  }

  const data: CasePresentationData = {
    title: `Itaú · ${project.title}`,

    context: "Itaú Unibanco · íon for Advisors",

    headline: project.title,

    subtitle: project.subtitle,

    role: "Senior Product Designer",

    team: "Design, Produto, Engenharia e áreas de negócio",

    scope: story.scope,

    keyMetric: itauKeyMetrics[caseSlug] || "Alta criticidade",

    kicker: "Fintech · Itaú Unibanco",

    hero: visuals[0],

    cover: !visuals.length
      ? {
        heading:
          caseSlug === "movimentacoes"
            ? "O contexto financeiro acompanha a jornada."
            : "Contexto e registro no mesmo fluxo de trabalho.",

        items:
          caseSlug === "movimentacoes"
            ? [
              "Provisionado visível",

              "Movimentações em contexto",

              "Continuidade da consulta",
            ]
            : [
              "Histórico recente",

              "Resumo assistido",

              "Revisão do conteúdo",
            ],

        note: "Síntese editorial do recorte apresentado. Não representa uma interface implementada nem substitui as evidências do projeto.",
      }
      : undefined,

    prevCase:
      caseSlug === "hub-liquidez"
        ? {
          title: "Einstein · Laudos médicos",
          href: "/cases/einstein-laudos",
          context: "Saúde · HIAE × Foursys · 2022",
        }
        : target(order[(index + order.length - 1) % order.length]),

    nextCase:
      caseSlug === "hub-liquidez"
        ? {
          title: "Claro · Ativação simplificada",
          href: "/cases/claro-ativacao-simplificada",
          context: "Telecom · Claro Brasil · 34M de clientes",
        }
        : target(order[(index + 1) % order.length]),

    chapters: [
      {
        title: "O projeto em perspectiva.",

        content: (
          <>
            <div className="cp-summary">
              <p>{story.summary}</p>
            </div>
            <div className="cp-columns">
              <div>
                <h3>Para quem</h3>
                <p>{story.users}</p>
              </div>
              <div>
                <h3>Recorte de atuação em design</h3>
                <p>{story.contribution}</p>
              </div>
            </div>
          </>
        ),
      },

      {
        title: "Contexto, problema e objetivo.",

        content: (
          <>
            <p>{project.framing}</p>
            <div className="cp-note">
              <h3>Pergunta de design</h3>
              <p>{project.question}</p>
            </div>
          </>
        ),
      },

      {
        title: "Descoberta e critérios de decisão.",

        content: (
          <>
            <p>{story.research}</p>
            <h3>O que precisava permanecer compreensível</h3>
            <List items={story.constraints} />
          </>
        ),
      },

      {
        title: "Decisões e suas razões.",

        content: (
          <ol className="cp-decisions">
            {story.decisions.map(([title, description]) => (
              <li key={title}>
                <h3>{title}</h3>
                <p>{description}</p>
              </li>
            ))}
          </ol>
        ),
      },

      {
        title: "Como a solução organiza a jornada.",

        content: (
          <>
            <ol className="cp-list">
              {story.flow.map((step) => (
                <li key={step}>{step}</li>
              ))}
            </ol>
            {visuals.length > 1 && (
              <div className="cp-gallery">
                {visuals.slice(1).map((image) => (
                  <CaseFigure key={image.src} image={image} />
                ))}
              </div>
            )}
          </>
        ),
      },

      {
        title: "Entregas e aprendizado.",

        content: (
          <>
            <h3>O que este recorte apresenta</h3>
            <List items={story.delivery} />
            <div className="cp-note">
              <h3>Aprendizado de design</h3>
              <p>{story.learning}</p>
            </div>
          </>
        ),
      },

      {
        title: "Fontes, colaboração e alcance.",

        content: (
          <div className="cp-appendix">
            <details open>
              <summary>Referências do projeto</summary>
              <div>
                <Sources project={caseSlug} />
                {kbNodes[caseSlug] && (
                  <p>
                    <a
                      href={`https://www.figma.com/design/aASd7epPB9NlC0xIY53eOC/IFA---PROTOTIPO-COMPLETO?node-id=${kbNodes[caseSlug]}`}
                    >
                      Base de conhecimento funcional do produto
                    </a>
                  </p>
                )}
                {caseSlug === "registros-atendimento" && (
                  <p>
                    Referência: documentação histórica e fluxos de trabalho assistidos no portfólio da iniciativa.
                  </p>
                )}
              </div>
            </details>
            <details>
              <summary>Colaboração e período</summary>
              <div>
                <p>
                  Israel Rozar — Product Design no contexto de assessoria e
                  operações do Itaú. Período profissional apresentado na
                  trajetória: 2024–2026; não representa a duração individual
                  deste projeto. O trabalho envolve colaboração com Design,
                  Produto, Engenharia e áreas de negócio; as entregas do produto
                  não são atribuídas como realização individual.
                </p>
              </div>
            </details>
            <details>
              <summary>Alcance das evidências</summary>
              <div>
                <p>{story.boundary}</p>
              </div>
            </details>
          </div>
        ),
      },
    ],
  }

  return <CasePresentation data={data} />
}
