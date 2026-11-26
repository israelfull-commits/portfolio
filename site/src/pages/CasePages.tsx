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
  vencimentos: [
    [
      "Interface canônica · Gestão de liquidez",

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
  src: "/images/v17-einstein-bento-light-aeroload.webp",
  width: 2400,
  height: 1350,
  alt: "Visão modular do sistema de laudos do Hospital Israelita Albert Einstein: arquitetura multicanal, componente canônico de Protrombina e tokens clínicos",
  caption:
    "Sistema modular de laudos em produção: arquitetura multicanal, componente canônico de resultado + referência e tokens tipográficos aplicados em mais de 80 tipos de exames.",
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

    width: 1800,

    height: 1052,

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
    "Liderança de UX em pesquisa, Arquitetura da Informação e componentes escaláveis para estruturar mais de 80 tipos de laudos clínicos em tela e impressão monocromática, preservando o contexto diagnóstico.",

  role: "UX Lead",

  team: "Foursys × Hospital Israelita Albert Einstein",

  scope: "Pesquisa, modelagem da informação e prototipagem",

  keyMetric: "14 entregáveis documentados",

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
      id: "tese-clinica",
      tag: "Tese Clínica",
      title: "Organizar resultados sem perder o contexto clínico.",

      content: (
        <>
          <div className="cp-lead-editorial">
            <p className="cp-lead-text">
              Laudos de diferentes laboratórios e hospitais parceiros reuniam informações críticas em estruturas variáveis. O projeto desenhou uma linguagem modular previsível para mais de 80 tipos de exames, permitindo que médicos cruzem resultados, métodos e referências com agilidade, e que pacientes localizem seus dados com facilidade para levar à conversa médica.
            </p>
            <div className="cp-tradeoff-box">
              <span className="cp-tradeoff-eyebrow">
                Pergunta Norteadora & Desafio Central
              </span>
              <p className="cp-tradeoff-question">
                Como facilitar a localização e a leitura do laudo sem induzir uma interpretação clínica isolada?
              </p>
            </div>
          </div>
          <CaseMetrics
            items={[
              ["121", "pacientes responderam ao questionário de hábitos de leitura"],

              ["4", "médicos especialistas entrevistados em profundidade"],

              ["14", "entregáveis documentados no inventário EN-1 a EN-14"],
            ]}
          />
          <p className="cp-metrics-footnote">
            A pesquisa quantitativa com 121 pacientes mapeou hábitos de leitura e compreensão de termos médicos, triangulada com entrevistas em profundidade com médicos especialistas para assegurar rigor clínico, conformidade com a LGPD e sigilo médico.
          </p>
        </>
      ),
    },

    {
      id: "tela-e-papel",
      tag: "Tela & Papel (Antes/Depois)",
      title: "Uma hierarquia que funcione na tela e no papel.",

      content: (
        <>
          <div className="cp-cards-grid">
            <div className="cp-feature-card">
              <span className="cp-feature-tag">Cenário e Restrições</span>
              <h3>O desafio prático</h3>
              <p>
                O mesmo laudo precisava funcionar no aplicativo do celular, na tela do consultório e impresso em preto e branco nas impressoras dos hospitais parceiros. A especificação precisava operar dentro das limitações dos sistemas laudadores legados e manter legibilidade integral em impressão monocromática (contraste WCAG 2.2 AAA).
              </p>
            </div>
            <div className="cp-feature-card">
              <span className="cp-feature-tag">Diretrizes de Interface</span>
              <h3>As regras centrais do projeto</h3>
              <ul className="cp-card-list">
                <li>
                  <strong>Resultado e referência lado a lado:</strong> o valor do exame e o intervalo normal aparecem sempre juntos, na mesma linha visual.
                </li>
                <li>
                  <strong>Separação por região comum (Gestalt):</strong> metadados administrativos isolados no cabeçalho com borda estrutural, mantendo o bloco clínico livre de ruído.
                </li>
                <li>
                  <strong>Estrutura flexível:</strong> modelo modular que atende desde testes rápidos de uma linha até laudos descritivos extensos.
                </li>
              </ul>
            </div>
          </div>
          <CaseFigure
            image={{
              src: "/images/v03-einstein-antes-depois-layers.webp",
              width: 2400,
              height: 1350,
              alt: "Comparativo Antes vs. Depois do laudo Einstein: documento legado fragmentado à esquerda versus arquitetura modular com resultado e referência agrupados à direita",
              caption:
                "Antes vs. Depois: transição do laudo legado com dados espalhados para a arquitetura modular aprovada, agrupando resultado, unidade e valor de referência no mesmo bloco visual.",
            }}
          />
          <div className="cp-note">
            <h3>Meu papel como UX Lead, tensão técnica e mentoria</h3>
            <p>
              Liderei a arquitetura de informação, os rituais de critique com o time de design da Foursys e o alinhamento direto entre o corpo clínico do Albert Einstein e a engenharia dos sistemas laudadores. O principal desacordo ocorreu quando parte do negócio pediu alertas visuais interpretativos por cor: em conjunto com os médicos entrevistados, defendemos e provamos que o laudo precisava funcionar em impressão preto e branco sem induzir autodiagnóstico isolado.
            </p>
          </div>
        </>
      ),
    },

    {
      id: "taxonomia",
      tag: "Taxonomia de Dados",
      title: "Do documento ao dado.",

      content: (
        <>
          <p>
            Para construir esse padrão, analisamos mais de 80 exames reais de diversas especialidades — de análises laboratoriais a exames de imagem complexos. Descobrimos que, apesar das diferenças de formato, todos os laudos convergem para três macroáreas funcionais previsíveis.
          </p>
          <div className="cp-split">
            <div className="cp-split-content">
              <span className="cp-split-tag">Taxonomia de Dados Clínicos</span>
              <h3>As 3 Macroáreas do Exame</h3>
              <p>
                O modelo organiza metodologia, resultados e contexto clínico em três macroáreas, para orientar a localização das informações e preservar o contexto de leitura:
              </p>
              <ul className="cp-card-list">
                <li>
                  <strong>1. Metodologia:</strong> reúne prescrição, material biológico e parâmetros do equipamento, garantindo validade jurídica e técnica.
                </li>
                <li>
                  <strong>2. Resultado:</strong> núcleo objetivo do laudo com achados estruturados e intervalos de referência alinhados na mesma linha de leitura.
                </li>
                <li>
                  <strong>3. Conclusão diagnóstica:</strong> síntese conclusiva e parecer interpretativo assinado pelo especialista médico.
                </li>
              </ul>
            </div>
            <div className="cp-split-media">
              <CaseFigure
                image={{
                  src: "/images/hiae-taxonomia-laudo-2000.webp",
                  width: 2560,
                  height: 1302,
                  alt: "Prancha real de taxonomia clínica do projeto Einstein: decomposição de laudo de enterotomografia nas três macroáreas (Metodologia, Resultado e Conclusão Diagnóstica)",
                  caption:
                    "Taxonomia real do projeto: decomposição de exames em três macroáreas canônicas (Metodologia, Resultado e Conclusão Diagnóstica) com dados anonimizados sob LGPD.",
                }}
              />
            </div>
          </div>
          <List
            items={[
              "Fluxo de leitura médica: em consultas curtas e pronto-socorro, o profissional precisa localizar desvios de referência na primeira varredura visual, sem depender de interpretação por cor isolada.",

              "Como o paciente lê: busca o próprio resultado e precisa localizar o que importa para levar à conversa médica, sem se perder em termos técnicos ou fazer interpretações clínicas isoladas.",

              "Limitações dos sistemas: mapeamos o tamanho dos textos e tabelas para garantir que nenhuma palavra ou número ficasse cortado em qualquer impressora dos laboratórios parceiros.",
            ]}
          />
          <div className="cp-note">
            <h3>Evitando erros de leitura</h3>
            <p>
              Em saúde, um alinhamento confuso pode induzir a um diagnóstico errado. Resultado, unidade e intervalo de referência formam uma única unidade visual por proximidade (Gestalt), mitigando erros de associação linha a linha em cenários clínicos de alta carga cognitiva.
            </p>
          </div>
        </>
      ),
    },

    {
      id: "anatomia",
      tag: "Anatomia do Componente",
      title: "Preservar relações entre resultado, referência e contexto.",

      content: (
        <>
          <blockquote className="cp-quote">
            <p>
              Modular não é simplificar. É manter o contexto clínico no lugar
              onde a pessoa o espera.
            </p>
          </blockquote>
          <div className="cp-split">
            <div className="cp-split-content">
              <span className="cp-split-tag">Anatomia do Componente (v3.0)</span>
              <h3>Tempo de Protrombina (RNI)</h3>
              <ol className="cp-callout-list">
                <li className="cp-callout-item">
                  <span className="cp-callout-badge">1</span>
                  <div>
                    <strong>examTitle:</strong> Nome do exame e material biológico no topo.
                  </div>
                </li>
                <li className="cp-callout-item">
                  <span className="cp-callout-badge">2</span>
                  <div>
                    <strong>Uma linha por parâmetro:</strong> Cada teste clínico com linha horizontal dedicada.
                  </div>
                </li>
                <li className="cp-callout-item">
                  <span className="cp-callout-badge">3</span>
                  <div>
                    <strong>Acessibilidade visual:</strong> Ícones de conformidade que não dependem apenas da cor.
                  </div>
                </li>
                <li className="cp-callout-item">
                  <span className="cp-callout-badge">4</span>
                  <div>
                    <strong>Resultado e referência:</strong> Valor medido e limites normais alinhados lado a lado.
                  </div>
                </li>
              </ol>
            </div>
            <div className="cp-split-media">
              <CaseFigure
                image={{
                  src: "/images/hiae-componente-protrombina-crop.webp",
                  width: 2400,
                  height: 880,
                  alt: "Recorte real do protótipo v3 do projeto Einstein: componente Tempo de Protrombina (RNI) com examTitle, linha por parâmetro, ícone de conformidade redundante à cor e referência alinhada lado a lado",
                  caption:
                    "Protótipo real (v3): anatomia do componente Tempo de Protrombina (RNI) com título do exame, ícone de conformidade redundante à cor e intervalo de referência alinhado lado a lado.",
                }}
              />
            </div>
          </div>
          <div className="cp-split">
            <div className="cp-split-content">
              <span className="cp-split-tag">Design System Zera 1.0</span>
              <h3>Tokens e Anatomia Modular</h3>
              <p>
                Mapeamento dos tokens de cor semântica, tipografia proporcional e espaçamento (grid base 8px) integrados aos componentes modulares <code>dataField</code> e <code>examTitle</code>. O contrato garante previsibilidade e alinhamento estrito entre o protótipo no Figma e a implementação nos sistemas laudadores legados.
              </p>
            </div>
            <div className="cp-split-media">
              <CaseFigure
                image={{
                  src: "/images/hiae-ds-tokens-clean-1280.webp",
                  width: 2000,
                  height: 1250,
                  alt: "Documentação no Design System Zera 1.0: especificações de tokens de cores, tipografia e espaçamento para componentes de laudo",
                  caption:
                    "Design System Zera 1.0: especificações dos componentes dataField e examTitle com tokens de espaçamento e regras de anatomia modular para a engenharia.",
                }}
              />
            </div>
          </div>
        </>
      ),
    },

    {
      id: "escala",
      tag: "Escala em 80+ Exames",
      title: "Uma estrutura única para qualquer tipo de exame.",

      content: (
        <>
          <p>
            Um dos maiores desafios foi garantir que o mesmo padrão visual funcionasse tanto para laudos descritivos com muito texto (como mamografia e biópsias) quanto para tabelas densas cheias de números (como ressonâncias e hemogramas). A nova anatomia organiza a leitura para que o olhar encontre primeiro o resultado principal e, em seguida, os detalhes de técnica e observações.
          </p>
          <CaseFigure
            image={{
              src: "/images/v13-einstein-3-canais-mesa-concreto.webp",
              width: 2400,
              height: 1350,
              alt: "Paridade omnicanal do laudo Einstein em 3 suportes reais: folha A4 impressa de mamografia, portal web em MacBook e aplicativo mobile",
              caption:
                "Paridade real em 3 canais: mesma hierarquia clínica preservada na versão impressa A4, no prontuário web e no aplicativo mobile do paciente.",
            }}
          />
          <div className="cp-gallery">
            <CaseFigure
              image={{
                src: "/images/hiae-visao-futura-mamografia.webp",
                width: 2000,
                height: 1336,
                alt: "Laudo descritivo de mamografia estruturado para tablet e celular",
                caption:
                  "Laudo descritivo (Mamografia): cabeçalho padronizado e seções estruturadas para técnica, indicação clínica e conclusão diagnóstica.",
              }}
            />
            <CaseFigure
              image={{
                src: "/images/hiae-visao-futura-ressonancia.webp",
                width: 2000,
                height: 1336,
                alt: "Laudo tabular de ressonância cardiovascular com resultados em tabela no tablet e celular",
                caption:
                  "Laudo tabular (Ressonância): resultados organizados em grade tabular com alinhamento numérico fixo, reduzindo erros de comparação entre medidas no celular e no tablet.",
              }}
            />
          </div>
          <div className="cp-note">
            <h3>Estrutura Canônica no Prontuário Digital</h3>
            <p>
              O modelo unificado organiza a leitura para que o corpo clínico e o paciente visualizem primeiro o resultado principal e, em seguida, os parâmetros técnicos e observações diagnósticas, eliminando inconsistências entre diferentes unidades da rede.
            </p>
          </div>
        </>
      ),
    },

    {
      id: "validacao-escopo",
      tag: "Compreensão, Escopo & NDA",
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
              81,6% reconheceram o documento como um laudo médico; 77,8% concentraram a atenção no nome do exame, resultado e referência. Os indicadores de compreensão reforçam a importância da conversa com o médico. O laudo apresenta os dados para apoiar essa conversa e preservar o contexto clínico.
            </p>
          </div>
          <div className="cp-cards-grid">
            <div className="cp-feature-card">
              <span className="cp-feature-tag">Disciplina de Escopo</span>
              <h3>O que ficou fora do recorte</h3>
              <p>
                Optamos por não incluir selos interpretativos automáticos isolados do texto clínico nem redesenhar o portal inteiro de exames. O foco na arquitetura modular do laudo garantiu compatibilidade com impressão em preto e branco e sistemas legados sem induzir autodiagnóstico.
              </p>
            </div>
            <div className="cp-feature-card">
              <span className="cp-feature-tag">Reflexão Crítica</span>
              <h3>O que eu faria diferente hoje</h3>
              <p>
                Integraria a engenharia de geração de PDF e representantes de mais especialidades médicas desde a primeira semana de descoberta, validando quebras de página em exames extensos antes de consolidar os primeiros componentes.
              </p>
            </div>
          </div>
          <div className="cp-appendix">
            <details open>
              <summary>Contexto e documentação do projeto</summary>
              <div>
                <p>
                  Projeto desenvolvido em parceria institucional com o Hospital Israelita Albert Einstein. Em conformidade com as diretrizes de confidencialidade (NDA), governança hospitalar e sigilo médico, as especificações integrais de componentes, fluxos proprietários e arquivos de trabalho são de custódia restrita e documentação interna da instituição.
                </p>
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
        </>
      ),
    },
  ],
}

const claroHero: CaseImage = {
  src: "/images/v08-claro-multicanal-desktop-iphone.webp",
  width: 2400,
  height: 1350,
  alt: "Ativação Simplificada Claro Brasil em Desktop e Mobile: detalhe da linha com cabeçalho fixo ao lado da experiência móvel padronizada",
  caption:
    "Ativação Simplificada Claro Brasil: 22 jornadas comerciais (NET, Claro e Embratel) unificadas em uma única arquitetura Desktop e Mobile.",
}

const claroImages: CaseImage[] = [
  {
    src: "/images/claro-busca-cliente.webp",
    width: 1550,
    height: 972,
    alt: "Tela de busca de cliente do sistema de ativação, com campo de CPF e validação cadastral",
    caption:
      "Ponto de entrada da ativação: consulta de cliente por CPF com validação instantânea e dados sintetizados para conformidade com a LGPD.",
  },
  {
    src: "/images/claro-jornadas.webp",
    width: 1440,
    height: 1440,
    alt: "Mapa da jornada de troca de chip no Miro com user stories e validações",
    caption:
      "Decomposição operacional: validações, etapas da troca de chip, resumo financeiro e regras de oferta organizados na jornada.",
  },
  {
    src: "/images/claro-detalhe-linha.webp",
    width: 1550,
    height: 972,
    alt: "Detalhe da linha com dados do cliente, cabeçalho fixo e grupos expansíveis",
    caption:
      "Preservação de contexto: dados do cliente, linha, plano e fatura agrupados em blocos expansíveis com acesso direto às jornadas relacionadas.",
  },
  {
    src: "/images/claro-multicanal.webp",
    width: 1376,
    height: 932,
    alt: "Composição de interfaces desktop e mobile da ativação simplificada Claro",
    caption:
      "Paridade multicanal: mesma taxonomia de planos, resumo financeiro e etapas de confirmação entre o balcão desktop e o aplicativo mobile.",
  },
]

export const claroPresentation: CasePresentationData = {
  title: "Claro · Ativação simplificada",

  context: "Telecom · Claro Brasil · 2017–2018",

  headline: "22 jornadas comerciais unificadas em uma esteira desktop e mobile.",

  subtitle:
    "Product Discovery, Arquitetura da Informação e interface padronizada para lojas físicas, televendas e consultores em campo (NET, Claro e Embratel).",

  role: "UX/UI Designer",

  team: "Design, stakeholders e profissionais da operação",

  scope: "Discovery, fluxos e interfaces desktop e mobile",

  keyMetric: "22 jornadas unificadas · 70 oportunidades",

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
      id: "operacao",
      tag: "Operação Fragmentada",
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
          <div className="cp-cards-grid">
            <div className="cp-feature-card">
              <span className="cp-feature-tag">Contexto Operacional</span>
              <h3>O cenário</h3>
              <p>
                A rotina comercial precisava conciliar necessidades de
                atendentes de loja, consultores em trânsito e as regras de
                negócio de telecom, com grande volume de dados por transação.
              </p>
            </div>
            <div className="cp-feature-card">
              <span className="cp-feature-tag">Pergunta de Pesquisa</span>
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
      id: "esteira",
      tag: "22 Jornadas ➔ 5 Etapas",
      title:
        "Decomposição de 22 jornadas de atendimento em uma esteira unificada.",

      content: (
        <>
          <div className="cp-split">
            <div className="cp-split-content">
              <span className="cp-split-tag">Discovery & Pesquisa Operacional</span>
              <h3>Imersão em Lojas Físicas e Televendas</h3>
              <p>
                O discovery reuniu benchmarking competitivo, 20 entrevistas em profundidade com profissionais e lideranças executivas, três dias de workshops imersivos e a formulação de 10 personas operacionais. O shadowing em lojas físicas e televendas evidenciou que até 40% do tempo observado em atendimento era consumido na alternância manual entre sistemas legados desconectados para consultar uma única linha.
              </p>
              <ul className="cp-card-list">
                <li>
                  <strong>Ruptura de contexto:</strong> alternância constante entre sistemas desconectados durante o atendimento presencial ou telefônico.
                </li>
                <li>
                  <strong>Insegurança tarifária:</strong> dificuldade operacional em calcular descontos, combos e regras de fidelização em tempo real.
                </li>
                <li>
                  <strong>Carga cognitiva:</strong> necessidade de memorizar códigos promocionais e regras de negócio para evitar erros de contratação.
                </li>
              </ul>
            </div>
            <div className="cp-split-media">
              <CaseFigure image={claroImages[0]} />
            </div>
          </div>
          <div className="cp-split">
            <div className="cp-split-content">
              <span className="cp-split-tag">Arquitetura da Informação & Fluxos</span>
              <h3>Matriz Unificada de 22 Jornadas Comerciais</h3>
              <p>
                A padronização das 22 jornadas operacionais eliminou redundâncias entre a consulta cadastral, a configuração do plano e a formalização do contrato. Em vez de fluxos isolados para cada transação (troca de chip, ativação, upgrade de plano e portabilidade), estruturamos uma esteira unificada de atendimento:
              </p>
              <ul className="cp-card-list">
                <li>
                  <strong>Esteira unificada:</strong> mesma ordem mental de leitura e decisão no balcão de loja e na mobilidade.
                </li>
                <li>
                  <strong>Validação progressiva:</strong> checagem automática de elegibilidade cadastral e antifraude antes da oferta.
                </li>
                <li>
                  <strong>Mitigação de atrito:</strong> redução de etapas intermediárias e visualização clara de pré-requisitos técnicos do chip.
                </li>
              </ul>
            </div>
            <div className="cp-split-media">
              <CaseFigure image={claroImages[1]} />
            </div>
          </div>
          <CaseFigure
            image={{
              src: "/images/v10-claro-jornada-editorial.webp",
              width: 2400,
              height: 1350,
              alt: "Diagrama da esteira unificada de atendimento Claro Brasil em 5 etapas com camada persistente de contexto e paridade entre Desktop e Mobile",
              caption:
                "Esteira unificada em 5 etapas: da identificação por CPF à confirmação contratual, mantendo cabeçalho fixo do cliente e resumo financeiro persistente em Desktop e Mobile.",
            }}
          />
          <div className="cp-note">
            <h3>Desacordo construtivo & decisão validada com a operação</h3>
            <p>
              Lideranças comerciais inicialmente defenderam exibir todos os parâmetros de oferta em tela única para evitar cliques extras. Em sessões práticas com operadores de loja e televendas, demonstrei que a densidade sem hierarquia elevava erros de preenchimento — o acordo foi adotar etapas progressivas com resumo financeiro lateral sempre visível.
            </p>
          </div>
        </>
      ),
    },

    {
      id: "contexto-fixo",
      tag: "Contexto Fixo & Resumo Lateral",
      title:
        "Navegação progressiva, resumo financeiro visível e preservação do contexto do cliente.",

      content: (
        <>
          <div className="cp-split">
            <div className="cp-split-content">
              <span className="cp-split-tag">Diretrizes de Interface & Usabilidade</span>
              <h3>Resumo Financeiro Lateral & Contexto Fixo</h3>
              <p>
                Para mitigar erros de contratação e dar previsibilidade ao atendente, definimos três regras centrais de arquitetura de informação:
              </p>
              <ul className="cp-card-list">
                <li>
                  <strong>1. Navegação progressiva por etapas:</strong> grupos expansíveis com revelação progressiva (progressive disclosure) e etapas numeradas aplicam a heurística de visibilidade do status do sistema (Nielsen) para reduzir carga cognitiva em fluxos extensos.
                </li>
                <li>
                  <strong>2. Preservação do contexto do cliente:</strong> cabeçalho fixo com dados da linha, status cadastral e atalhos rápidos apoiam a continuidade da conversa.
                </li>
                <li>
                  <strong>3. Composição financeira em tempo real:</strong> o resumo lateral aproxima produtos, descontos aplicados e valores finais durante toda a configuração da oferta.
                </li>
              </ul>
            </div>
            <div className="cp-split-media">
              <CaseFigure image={claroImages[2]} />
            </div>
          </div>
        </>
      ),
    },

    {
      id: "multicanal",
      tag: "Paridade Desktop & Mobile",
      title: "Da jornada do chip às interfaces desktop e mobile padronizadas.",

      content: (
        <>
          <div className="cp-split">
            <div className="cp-split-content">
              <span className="cp-split-tag">Consistência Multicanal</span>
              <h3>Paridade entre Desktop e Aplicativo Móvel</h3>
              <p>
                O atendente de balcão utiliza a interface desktop com maior densidade de dados; o consultor externo utiliza o aplicativo mobile. A taxonomia de planos e as etapas de confirmação são preservadas entre desktop e mobile, apoiando a continuidade entre canais.
              </p>
            </div>
            <div className="cp-split-media">
              <CaseFigure image={claroImages[3]} />
            </div>
          </div>
          <div className="cp-cards-grid">
            <div className="cp-feature-card">
              <span className="cp-feature-tag">Disciplina de Escopo</span>
              <h3>O que ficou fora do recorte</h3>
              <p>
                Não redesenhamos os sistemas legados de faturamento nem alteramos as regras de validação de crédito de backoffice. O recorte concentrou-se em unificar a camada de atendimento e vendas (desktop e mobile) para dar clareza ao resumo financeiro durante a oferta.
              </p>
            </div>
            <div className="cp-feature-card">
              <span className="cp-feature-tag">Reflexão Crítica</span>
              <h3>O que eu faria diferente hoje</h3>
              <p>
                Estruturaria desde o início um protocolo de telemetria comparativa entre lojas próprias e televendas, medindo o tempo por etapa de ativação antes e depois da implantação para quantificar o ganho operacional por canal.
              </p>
            </div>
          </div>
        </>
      ),
    },

    {
      id: "escopo-equipe",
      tag: "Escopo, Reflexão & Equipe",
      title:
        "Governança do projeto, colaboração multidisciplinar e impacto.",

      content: (
        <div className="cp-appendix">
          <details open>
            <summary>Arquivos e versões</summary>
            <div>
              <p>
                Documentação técnica do projeto Claro: registros de workshops, mapa
                de jornada de troca de chip, telas de ativação, detalhe da linha
                e confirmação mobile.
              </p>
              <p>
                O documento de migração desktop identifica V.2 de 10/05/2018; o
                PDF mobile foi atualizado em 11/06/2018, integrando o acervo técnico documentado da iniciativa.
              </p>
            </div>
          </details>
          <details>
            <summary>Colaboração e equipe</summary>
            <div>
              <p>
                Israel Rozar — UX/UI Designer, atuando junto a lideranças
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
    src: "/images/v12-neoenergia-bento-service-design.webp",

    width: 2400,

    height: 1350,

    alt: "Visão executiva P&D ANEEL Neoenergia: Service Blueprint de Uso e Pago, escala das 4 distribuidoras e Matriz de 118 Ideias Priorizadas",

    caption:
      "Projeto P&D Conexão Digital ANEEL: Service Design integrando 4 distribuidoras (34M de pessoas), 5 Service Blueprints e 118 oportunidades priorizadas.",
  },

  prevCase: {
    title: "Claro · Ativação simplificada",

    href: "/cases/claro-ativacao-simplificada",

    context: "Telecom · Claro Brasil · 22 jornadas unificadas",
  },

  nextCase: {
    title: "Einstein · Laudos médicos",

    href: "/cases/einstein-laudos",

    context: "Saúde · HIAE × Foursys · 2022",
  },

  chapters: [
    {
      id: "escala-nacional",
      tag: "Escala Nacional (34M)",
      title:
        "Unificação da infraestrutura de atendimento para 34 milhões de pessoas.",

      content: (
        <>
          <div className="cp-summary">
            <p>
              Iniciativa de Product Discovery e Service Design (Human-Centered
              Design) para conectar 11 canais de atendimento, backoffice e
              equipes de campo do Grupo Neoenergia (Iberdrola Brasil),
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
              ["4", "distribuidoras integradas na mesma esteira"],

              ["5 estágios", "ciclo de vida em blueprints To-Be"],

              ["118 ideias", "priorizadas na matriz de valor"],
            ]}
          />
          <div className="cp-split">
            <div className="cp-split-content">
              <span className="cp-split-tag">Ecossistema & Multicanalidade</span>
              <h3>Mapeamento de 11 Canais de Atendimento</h3>
              <p>
                O diagnóstico mapeou a jornada do consumidor através de 11 pontos de contato — desde o atendimento presencial em agências e postos credenciados até canais digitais (portal web, aplicativo móvel, SMS, WhatsApp e call center) e equipes de campo.
              </p>
              <ul className="cp-card-list">
                <li>
                  <strong>Ruptura de continuidade:</strong> solicitações iniciadas nos canais digitais exigiam deslocamento físico até a agência para validação documental presencial.
                </li>
                <li>
                  <strong>Silos operacionais:</strong> o atendente do call center não visualizava as ordens de serviço pendentes das equipes de campo, gerando reiterações e frustração.
                </li>
                <li>
                  <strong>Assimetria de dados:</strong> ausência de transparência em faturamentos estimados e histórico de consumo, provocando alto volume de contestações.
                </li>
              </ul>
            </div>
            <div className="cp-split-media">
              <CaseFigure
                image={{
                  src: "/images/neoenergia-grandes-numeros.webp",
                  width: 1600,
                  height: 900,
                  alt: "Escala nacional da Neoenergia: 4 distribuidoras (Coelba, Celpe, Cosern e Elektro), 18 estados, 34 milhões de habitantes e 13,9 milhões de clientes",
                  caption:
                    "Escala da operação: 4 distribuidoras (Coelba, Celpe, Cosern e Elektro) atendendo 13,9 milhões de clientes em 18 estados brasileiros.",
                }}
              />
            </div>
          </div>
        </>
      ),
    },

    {
      id: "backstage",
      tag: "Auditoria de Backstage",
      title:
        "Auditoria de backstage: quando a insatisfação com a fatura revela silos operacionais.",

      content: (
        <>
          <div className="cp-feature-card">
            <span className="cp-feature-tag">Diagnóstico & Auditoria Operacional</span>
            <h3>Linhas de Visibilidade e Silos de Backstage</h3>
            <p>
              A leitura de Service Design evita reduzir o diagnóstico a interfaces de tela: a insatisfação com a fatura raramente é um problema visual, decorrendo de regras de negócio obscuras, leituras por estimativa ou falta de sincronização entre o despacho técnico e o faturamento.
            </p>
            <ul className="cp-card-list">
              <li>
                <strong>Linha de interação:</strong> pontos de contato diretos onde o consumidor registra a solicitação ou autoleitura.
              </li>
              <li>
                <strong>Linha de visibilidade:</strong> fronteira que separa o que o cliente enxerga das validações internas de crédito e engenharia.
              </li>
              <li>
                <strong>Linha de suporte interno:</strong> integração de sistemas legados de despacho de equipes técnicas e baixa bancária.
              </li>
            </ul>
          </div>
          <CaseFigure
            image={{
              src: "/images/v11-neoenergia-blueprint-studio-desk.webp",
              width: 2400,
              height: 1350,
              alt: "Service Blueprints 1 e 2 da Neoenergia apresentados em prancha editorial conectando frontstage, backstage e sistemas de campo",
              caption:
                "Auditoria de backstage: pranchas dos Service Blueprints conectando a experiência do consumidor aos sistemas legados e equipes de campo das 4 distribuidoras.",
            }}
          />
        </>
      ),
    },

    {
      id: "blueprints",
      tag: "5 Service Blueprints",
      title:
        "Os 5 estágios do ciclo de vida do cliente mapeados em Service Blueprints.",

      content: (
        <>
          <div className="cp-split">
            <div className="cp-split-content">
              <span className="cp-split-tag">Arquitetura de Serviços & Visão To-Be</span>
              <h3>Ciclo de Vida Estruturado em 5 Macroetapas</h3>
              <p>
                Para superar a fragmentação entre as 4 distribuidoras, consolidamos a jornada completa do consumidor em 5 estágios canônicos com especificações de frontstage e backstage:
              </p>
              <ol className="cp-card-list cp-card-list--numbered">
                <li>
                  <strong>1. Contrato e instalo:</strong> busca de requisitos, adequação técnica do padrão e ligação nova de energia.
                </li>
                <li>
                  <strong>2. Uso e pago:</strong> consumo em kWh, autoleitura em áreas remotas, contestação e parcelamento de débitos.
                </li>
                <li>
                  <strong>3. Preciso de suporte:</strong> comunicação de falta de energia, previsão de restabelecimento e emergências.
                </li>
                <li>
                  <strong>4. Mudo o contrato:</strong> alteração de titularidade, mudança de carga e adesão à geração solar distribuída.
                </li>
                <li>
                  <strong>5. Encerramento:</strong> desligamento definitivo, mitigação de inadimplência e quitação de débitos.
                </li>
              </ol>
            </div>
            <div className="cp-split-media">
              <CaseFigure
                image={{
                  src: "/images/neoenergia-blueprint-crop-uso-pago-1600.webp",
                  width: 1600,
                  height: 900,
                  alt: "Recorte em alta resolução do Service Blueprint 2 (Uso e Pago): storyboard, ações do consumidor e curva de criticidade",
                  caption:
                    "Service Blueprint 2 (Uso e Pago): recorte em alta resolução conectando consumo, autoleitura, análise de cobrança e curva de criticidade.",
                }}
              />
            </div>
          </div>
        </>
      ),
    },

    {
      id: "multi-tenant",
      tag: "Design System Multi-Tenant",
      title:
        "Desburocratização de backoffice antes de redesenho de portal e Design System multi-tenant.",

      content: (
        <>
          <div className="cp-split">
            <div className="cp-split-content">
              <span className="cp-split-tag">Design System Multi-Tenant & Governança</span>
              <h3>Padronização de Interfaces para 4 Distribuidoras</h3>
              <p>
                Em vez de manter quatro portais independentes, estruturamos um Design System multi-tenant baseado em componentes escaláveis e tokens semânticos por distribuidora, garantindo consistência de arquitetura, contraste acessível (WCAG) e redução do custo de manutenção em código:
              </p>
              <ul className="cp-card-list">
                <li>
                  <strong>1. Mapear antes de propor:</strong> a jornada de serviço orienta a interface para que as telas resolvam os atritos reais da operação física.
                </li>
                <li>
                  <strong>2. Conectar atendimento e operação:</strong> componentes que refletem o status real dos sistemas de campo em tempo real.
                </li>
                <li>
                  <strong>3. Governança multi-tenant:</strong> um único chassi de componentes alimentando Elektro, Coelba, Celpe e Cosern com temas dedicados.
                </li>
              </ul>
            </div>
            <div className="cp-split-media">
              <CaseFigure
                image={{
                  src: "/images/neoenergia-entregaveis-ui-design-system.webp",
                  width: 1600,
                  height: 900,
                  alt: "Entregáveis de interface, portal unificado e Design System multi-tenant para as 4 distribuidoras",
                  caption:
                    "Design System Multi-tenant: componentes modulares e esteira de autosserviço padronizada para as 4 distribuidoras do grupo.",
                }}
              />
            </div>
          </div>
        </>
      ),
    },

    {
      id: "matriz-118",
      tag: "Matriz de 118 Ideias",
      title:
        "Matriz de 118 oportunidades priorizadas como baseline para o roadmap de evolução de serviços.",

      content: (
        <>
          <div className="cp-split">
            <div className="cp-split-content">
              <span className="cp-split-tag">Priorização & Roadmap Estratégico</span>
              <h3>118 Oportunidades Estruturadas por Impacto e Esforço</h3>
              <p>
                As oportunidades mapeadas durante a pesquisa de campo e a auditoria de processos foram organizadas em uma matriz analítica, cruzando o valor percebido pelo consumidor com o esforço operacional de implementação:
              </p>
              <ul className="cp-card-list">
                <li>
                  <strong>Quick Wins (Ações Imediatas):</strong> correções de comunicação na fatura e desburocratização da autoleitura via aplicativo móvel.
                </li>
                <li>
                  <strong>Programas Estruturantes:</strong> unificação do portal de serviços e integração direta dos sistemas de despacho de campo.
                </li>
                <li>
                  <strong>Iniciativas Estruturais de Longo Prazo:</strong> telemedição automatizada, canais conversacionais com supervisão humana e autoatendimento para geração solar distribuída.
                </li>
              </ul>
            </div>
            <div className="cp-split-media">
              <CaseFigure
                image={{
                  src: "/images/neoenergia-matriz-118-ideias.webp",
                  width: 2000,
                  height: 1195,
                  alt: "Matriz de Priorização com 118 Oportunidades de Serviço (Impacto vs. Esforço)",
                  caption:
                    "Matriz de Priorização: 118 oportunidades estruturadas e classificadas por impacto no negócio versus valor percebido pelo consumidor.",
                }}
              />
            </div>
          </div>
          <div className="cp-note">
            <h3>Desacordo estratégico & aprendizado central</h3>
            <p>
              Durante a priorização, diretorias regionais inicialmente pediram quatro portais independentes para preservar particularidades locais. Ao cruzar os 5 Service Blueprints com o custo de manutenção de backoffice, defendemos a arquitetura multi-tenant com tokens de marca — mantendo identidade regional sem multiplicar quatro vezes o débito técnico.
            </p>
          </div>
          <div className="cp-cards-grid">
            <div className="cp-feature-card">
              <span className="cp-feature-tag">Disciplina de Escopo</span>
              <h3>O que ficou fora do recorte</h3>
              <p>
                A etapa de P&D não incluiu o desenvolvimento em código do portal final nem a substituição imediata dos ERPs legados das 4 distribuidoras. Priorizamos o diagnóstico de backstage, os 5 Service Blueprints e a matriz de 118 ideias para atacar primeiro os gargalos que geravam retrabalho em campo.
              </p>
            </div>
            <div className="cp-feature-card">
              <span className="cp-feature-tag">Reflexão Crítica</span>
              <h3>O que eu faria diferente hoje</h3>
              <p>
                Incluiria protótipos navegáveis de alta fidelidade para dois fluxos críticos de campo já durante os workshops de priorização, acelerando o alinhamento entre as diretorias regionais sobre o esforço técnico da esteira multi-tenant.
              </p>
            </div>
          </div>
        </>
      ),
    },

    {
      id: "governanca-aneel",
      tag: "Governança P&D ANEEL",
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
      "A etapa de discovery e o handoff mapearam a evolução da consulta, os estados operacionais, o registro de ações, os pontos de entrada e a visão gerencial. A interface consolidada de Gestão de Liquidez centraliza esses fluxos em uma experiência única de acompanhamento da carteira.",

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
      "Na plataforma íon for Advisors (IFA), especialistas precisavam cruzar múltiplas abas para conciliar saldo em conta, recursos de Open Finance e liquidez projetada antes de abordar clientes. O objetivo foi estruturar uma visão única capaz de separar disponibilidade imediata de projeção temporal sem perder a rastreabilidade da origem.",

    users:
      "Especialistas de investimentos que acompanham recursos disponíveis e oportunidades de atuação em suas carteiras.",

    contribution:
      "Hierarquia dos dados financeiros, distinção temporal dos valores e conexão entre visão de carteira, lista de clientes, filtros e estado da atuação.",

    research:
      "A arquitetura do Hub de Liquidez conecta a posição atual, a projeção de recursos e a fila prioritária de clientes para atuação. A solução integra os valores de liquidez imediata identificados pelo Cofrinho IFA ao acompanhamento dos recursos que permanecem em conta.",

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
      "Os dados e valores numéricos apresentados na interface foram sintetizados para preservação do sigilo bancário, mantendo a hierarquia de saldos, filtros, status operacionais e regras de visualização apresentadas no artefato.",

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
      "A etapa de discovery comparou alternativas para acomodar o Extrato EA no IFA, distinguindo conta corrente, investimentos e conta gráfica. A arquitetura adotada manteve o saldo provisionado persistente no cabeçalho, com CEP, CEP Plus e limite contextualizados em Movimentações.",

    constraints: [
      "O saldo provisionado é necessário em diferentes jornadas e não pode depender de troca de aba.",

      "Conta corrente, investimentos e conta gráfica têm informações próprias e precisam permanecer distinguíveis.",

      "Consulta por período, busca e ordenação devem manter contexto suficiente para interpretar os lançamentos.",
    ],

    decisions: [
      [
        "Manter o provisionado no cabeçalho",

        "O acesso transversal evita exigir navegação até Movimentações para consultar um saldo necessário em outras tarefas operacionais.",
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
      "Em operações financeiras reguladas, a automação de processos por IA reduz o tempo de transcrição apenas quando mantém rastreabilidade auditável: o especialista valida, edita e aprova cada registro antes da persistência bancária (Human-in-the-Loop).",

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

        note: "Síntese de arquitetura da informação e modelos de fluxo para conformidade com sigilo bancário e padrões do íon for Advisors.",
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
          context: "Telecom · Claro Brasil · 22 jornadas unificadas",
        }
        : target(order[(index + 1) % order.length]),

    chapters: [
      {
        id: "gargalo",
        tag: "Gargalo Operacional",
        title: project.question,

        content: (
          <>
            <div className="cp-summary">
              <p>{story.summary}</p>
              <p>{project.framing}</p>
            </div>
            <div className="cp-cards-grid">
              <div className="cp-feature-card">
                <span className="cp-feature-tag">Público-Alvo</span>
                <h3>Para quem</h3>
                <p>{story.users}</p>
              </div>
              <div className="cp-feature-card">
                <span className="cp-feature-tag">Escopo de Design</span>
                <h3>Recorte de atuação</h3>
                <p>{story.contribution}</p>
              </div>
            </div>
            <h3>Restrições que moldaram a solução</h3>
            <List items={story.constraints} />
          </>
        ),
      },

      {
        id: "decisoes",
        tag: "3 Decisões de Arquitetura",
        title: `Decisões estruturais em ${project.title}.`,

        content: (
          <>
            <p>{story.research}</p>
            <ol className="cp-decisions">
              {story.decisions.map(([title, description]) => (
                <li key={title}>
                  <h3>{title}</h3>
                  <p>{description}</p>
                </li>
              ))}
            </ol>
          </>
        ),
      },

      {
        id: "interface",
        tag: "Fluxo & Interface Canônica",
        title: `Como o assessor opera ${project.title} ponta a ponta.`,

        content: (
          <>
            <ol className="cp-list">
              {story.flow.map((step) => (
                <li key={step}>{step}</li>
              ))}
            </ol>
            {visuals.length === 2 ? (
              <CaseFigure image={visuals[1]} />
            ) : visuals.length > 2 ? (
              <div className="cp-gallery">
                {visuals.slice(1).map((image) => (
                  <CaseFigure key={image.src} image={image} />
                ))}
              </div>
            ) : null}
          </>
        ),
      },

      {
        id: "salvaguardas",
        tag: "Salvaguardas & Aprendizado",
        title: "O que fica dentro, o que fica fora e o que evoluir.",

        content: (
          <>
            <h3>O que este recorte apresenta</h3>
            <List items={story.delivery} />
            <div className="cp-note">
              <h3>Aprendizado de design</h3>
              <p>{story.learning}</p>
            </div>
            <div className="cp-cards-grid">
              <div className="cp-feature-card">
                <span className="cp-feature-tag">Disciplina de Escopo</span>
                <h3>O que ficou fora do recorte</h3>
                <p>
                  Mantivemos fora da primeira camada visual configurações avançadas de baixa recorrência e automações sem revisão do especialista. Em operações financeiras densas, o trade-off foi priorizar visibilidade de contexto, filtros previsíveis e rastreabilidade da decisão humana.
                </p>
              </div>
              <div className="cp-feature-card">
                <span className="cp-feature-tag">Reflexão Crítica</span>
                <h3>O que eu faria diferente hoje</h3>
                <p>
                  Ampliaria o acompanhamento longitudinal após o handoff com indicadores de uso por perfil de carteira, cruzando o tempo de consulta de dados com a taxa de registro de ações concluídas pelos assessores.
                </p>
              </div>
            </div>
          </>
        ),
      },

      {
        id: "conformidade",
        tag: "Escopo & Conformidade",
        title: "Governança, autoria e sigilo bancário (LGPD).",

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
              <summary>Colaboração e liderança de design</summary>
              <div>
                <p>
                  Israel Rozar — Senior Product Designer no contexto de assessoria e
                  operações da plataforma íon for Advisors do Itaú Unibanco (2024–2026).
                  Atuação em squads multidisciplinares integrando Design, Gestão de Produto,
                  Engenharia e lideranças de negócio na definição de arquitetura da informação,
                  contratos de dados e fluxos de alta complexidade.
                </p>
              </div>
            </details>
            <details>
              <summary>Conformidade e sigilo bancário</summary>
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
