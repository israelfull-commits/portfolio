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
          <a href={href} target="_blank" rel="noopener noreferrer">
            {label}
            <span className="pf-sr-only"> (abre em nova aba)</span>
          </a>
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
    "Proposta modular de laudos (v3) estruturada para preservar a mesma ordem de leitura em papel A4, web e mobile, sem depender de cor isolada — desenhada a partir de mais de 80 exames analisados.",
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

  context: "HIAE × Foursys · 2022",

  headline: "Uma linguagem visual modular para laudos heterogêneos.",

  subtitle:
    "Como UX Lead no projeto Consumo de Resultados (HIAE × Foursys), conduzi pesquisa, arquitetura da informação e componentização para mais de 80 tipos de laudos em tela e papel P&B. Nos testes com protótipo, 81,6% reconheceram o documento e 77,8% focaram primeiro em exame, resultado e referência.",

  role: "UX Lead",

  team: "Design (Foursys) × Corpo clínico e Engenharia (Einstein)",

  scope: "Pesquisa, arquitetura da informação e prototipagem",

  keyMetricLabel: "VALIDAÇÃO E ESCOPO",
  keyMetric: "81,6% reconhecimento · 14 entregáveis",

  kicker: "Saúde · UX Lead",

  hero: einsteinHero,

  nextCase: {
    title: "Itaú Unibanco · Hub de Liquidez",

    href: "/cases/itau/hub-liquidez",

    context: "Fintech · Itaú Unibanco · íon for Advisors",
  },

  prevCase: {
    title: "Neoenergia · Service Design",

    href: "/cases/neoenergia-conexao-digital",

    context: "Energia · P&D ANEEL · 34M de pessoas",
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
              Laboratórios e hospitais parceiros emitiam exames em layouts distintos, dificultando a leitura clínica e a padronização dos sistemas laudadores. A tensão central era tornar o laudo fácil de localizar para o paciente sem induzir autodiagnóstico fora da consulta. Conduzi a definição de uma linguagem modular para mais de 80 tipos de exames, mantendo resultado, método e referência sempre na mesma ordem de leitura.
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
            Insight central da descoberta: pacientes procuram localizar o próprio resultado para levar à consulta, mas erram a interpretação quando valores e referências ficam separados — achado triangulado entre 121 respostas anônimas (LGPD) e 4 entrevistas com médicos especialistas.
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
                O mesmo laudo precisava manter leitura legível no aplicativo, na tela do consultório e em impressão preto e branco nos hospitais parceiros. A especificação foi desenhada para respeitar as restrições dos sistemas laudadores legados (incluindo templates em Microsoft Word) e alto contraste sem depender de cor.
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
                "Antes vs. Depois: aproximamos resultado, unidade e valor de referência no mesmo bloco visual para evitar erro de associação linha a linha entre colunas afastadas no documento legado.",
            }}
          />
          <div className="cp-note">
            <h3>Meu papel como UX Lead e composição do trabalho</h3>
            <p>
              Conduzi ponta a ponta a pesquisa com médicos e pacientes, a arquitetura da informação, os rituais de critique com o time de design da Foursys e a prototipação da proposta v3. Contribuí com o corpo clínico do Einstein na revisão de terminologia e com a engenharia dos sistemas laudadores na definição de limites de tabela e impressão.
            </p>
          </div>
          <div className="cp-cards-grid">
            <div className="cp-feature-card">
              <span className="cp-feature-tag">Decisão 01 · Alertas por cor</span>
              <h3>Como sinalizar desvios sem induzir autodiagnóstico?</h3>
              <p>
                <strong>Opções:</strong> (A) selos coloridos interpretativos (&ldquo;normal/alterado&rdquo;), pedido inicial de parte do negócio; (B) resultado e faixa de referência lado a lado com ícone redundante à cor. <strong>Decisão e trade-off:</strong> com apoio dos médicos entrevistados, descartei (A) e adotei (B), a custo de não oferecer uma leitura instantânea binária ao paciente. <strong>Evidência:</strong> restrição de impressão P&amp;B nos hospitais parceiros e 4 entrevistas médicas.
              </p>
            </div>
            <div className="cp-feature-card">
              <span className="cp-feature-tag">Decisão 02 · Modelo único vs. templates por exame</span>
              <h3>Padronizar por exame ou criar uma taxonomia comum?</h3>
              <p>
                <strong>Opções:</strong> (A) manter templates independentes por especialidade; (B) decompor mais de 80 exames em 3 macroáreas fixas com componentes modulares (<code>examTitle</code> e <code>dataField</code>). <strong>Decisão e trade-off:</strong> priorizei (B) para viabilizar manutenção nos sistemas legados, a custo de menor liberdade de diagrama específico em exames atípicos. <strong>Evidência:</strong> inventário de 80+ exames e restrições dos templates em Word.
              </p>
            </div>
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
            Apesar de variarem entre tabelas laboratoriais e textos descritivos de imagem, todos os mais de 80 exames reais que auditei convergem para três macroáreas funcionais. Essa descoberta permitiu trocar layouts artesanais por uma estrutura única.
          </p>
          <div className="cp-split">
            <div className="cp-split-content">
              <span className="cp-split-tag">Taxonomia de Dados Clínicos</span>
              <h3>As 3 Macroáreas do Exame</h3>
              <p>
                O modelo separa cada exame em três blocos fixos para manter previsível onde encontrar método, achados e parecer:
              </p>
              <ul className="cp-card-list">
                <li>
                  <strong>1. Metodologia:</strong> reúne prescrição, material biológico e parâmetros do equipamento, garantindo validade jurídica e técnica.
                </li>
                <li>
                  <strong>2. Resultado:</strong> núcleo objetivo do laudo com achados estruturados e intervalos de referência alinhados na mesma linha de leitura.
                </li>
                <li>
                  <strong>3. Conclusão diagnóstica:</strong> síntese interpretativa e parecer assinado pelo médico especialista.
                </li>
              </ul>
            </div>
            <div className="cp-split-media">
              <CaseFigure
                image={{
                  src: "/images/hiae-taxonomia-laudo-2000.webp",
                  width: 2560,
                  height: 1302,
                  alt: "Prancha real de taxonomia clínica do projeto Einstein: decomposição de laudo de enterotomografia nas três macroáreas (Metodologia, Resultado e Conclusão diagnóstica)",
                  caption:
                    "Taxonomia em 3 macroáreas (Metodologia, Resultado e Conclusão diagnóstica): escolhida para reutilizar a mesma ordem de leitura em exames laboratoriais e de imagem, mesmo sob sistemas emissores distintos (dados anonimizados sob LGPD).",
                }}
              />
            </div>
          </div>
          <List
            items={[
              "Leitura médica: em consultas curtas e pronto-socorro, o profissional precisa localizar desvios de referência na primeira varredura, sem depender de cor isolada.",

              "Leitura do paciente: busca o próprio resultado para levar à consulta, sem se perder em termos técnicos nem fazer interpretações clínicas isoladas.",

              "Limitações dos sistemas: mapeei larguras de texto e tabelas para reduzir cortes de palavras e números nas impressoras dos laboratórios parceiros.",
            ]}
          />
          <div className="cp-note">
            <h3>Por que agrupar resultado, unidade e referência</h3>
            <p>
              Quando o valor e a faixa de referência ficam em extremos opostos da página, o leitor pode associar o número à linha errada. Agrupar os três elementos por proximidade (Gestalt) reduz o esforço de rastreamento visual em exames extensos.
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
                    <strong>examTitle:</strong> nome do exame e material biológico no topo.
                  </div>
                </li>
                <li className="cp-callout-item">
                  <span className="cp-callout-badge">2</span>
                  <div>
                    <strong>Uma linha por parâmetro:</strong> cada teste clínico em linha horizontal dedicada.
                  </div>
                </li>
                <li className="cp-callout-item">
                  <span className="cp-callout-badge">3</span>
                  <div>
                    <strong>Acessibilidade visual:</strong> ícones de conformidade que não dependem apenas da cor.
                  </div>
                </li>
                <li className="cp-callout-item">
                  <span className="cp-callout-badge">4</span>
                  <div>
                    <strong>Resultado e referência:</strong> valor medido e limites normais alinhados lado a lado.
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
                    "Protótipo v3 (Tempo de Protrombina / RNI): ícone redundante à cor e alinhamento fixo entre valor e referência mantêm a leitura compreensível em impressão P&B e para leitores com daltonismo.",
                }}
              />
            </div>
          </div>
          <div className="cp-split">
            <div className="cp-split-content">
              <span className="cp-split-tag">Design System Zera 1.0</span>
              <h3>Tokens e Anatomia Modular</h3>
              <p>
                Especifiquei tokens de cor semântica, escala tipográfica e espaçamento em base 8px nos componentes <code>dataField</code> e <code>examTitle</code>. Essa documentação padroniza o handoff entre o Figma e as equipes de engenharia dos sistemas laudadores.
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
                    "Design System Zera 1.0: tokens e regras dos componentes dataField e examTitle documentados para reduzir divergências de espaçamento e hierarquia entre diferentes fornecedores laudadores.",
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
            Estruturei a mesma anatomia modular para atender dois extremos do acervo: laudos descritivos longos (como mamografia e biópsias) e tabelas numéricas densas (como ressonâncias e hemogramas). Em ambos os formatos, o leitor encontra primeiro o resultado principal e, abaixo dele, técnica e observações.
          </p>
          <CaseFigure
            image={{
              src: "/images/v13-einstein-3-canais-mesa-concreto.webp",
              width: 2400,
              height: 1350,
              alt: "Paridade omnicanal do laudo Einstein em 3 suportes reais: folha A4 impressa de mamografia, portal web em MacBook e aplicativo mobile",
              caption:
                "Paridade em 3 suportes (A4, web e mobile): preservar a mesma ordem entre papel e digital evita que médico e paciente precisem reaprender onde fica cada dado ao trocar de canal.",
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
                  "Laudo descritivo (Mamografia): seções separadas para técnica, indicação e conclusão evitam blocos corridos de texto que dificultam localizar o parecer em telas menores.",
              }}
            />
            <CaseFigure
              image={{
                src: "/images/hiae-visao-futura-ressonancia.webp",
                width: 2000,
                height: 1336,
                alt: "Laudo tabular de ressonância cardiovascular com resultados em tabela no tablet e celular",
                caption:
                  "Laudo tabular (Ressonância): grade com alinhamento numérico fixo escolhida para facilitar a comparação entre medidas no celular e no tablet sem deslocamento de colunas.",
              }}
            />
          </div>
          <div className="cp-note">
            <h3>Por que manter um único padrão entre texto e tabela</h3>
            <p>
              Reaproveitar o mesmo cabeçalho, hierarquia de títulos e separação de blocos entre exames laboratoriais e de imagem reduz o número de templates que a engenharia precisa manter nos sistemas emissores.
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
            Nos testes com o protótipo (entregáveis EN-7 e EN-14, sem linha de base comparativa do laudo legado), medimos quatro etapas: reconhecimento do documento, foco inicial, entendimento do objetivo do exame e interpretação autônoma. A hierarquia visual facilitou localizar os dados, mas confirmou que a interpretação clínica continua dependendo do médico.
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
            <h3>O que a diferença entre foco e interpretação orientou</h3>
            <p>
              A distância entre foco visual (77,8%) e interpretação autônoma (56,2%) confirmou que clareza visual não equivale a compreensão clínica. Esse dado sustentou a decisão de manter o laudo descritivo e contextualizado para apoiar a consulta, sem rótulos automáticos de diagnóstico. Como não medimos linha de base do formato anterior nem acompanhamento pós-lançamento, os percentuais servem como validação do protótipo.
            </p>
          </div>
          <div className="cp-cards-grid">
            <div className="cp-feature-card">
              <span className="cp-feature-tag">Disciplina de Escopo</span>
              <h3>O que ficou fora do recorte</h3>
              <p>
                Descartei incluir selos interpretativos automáticos isolados do texto clínico e redesenhar o portal inteiro de exames. Priorizei a arquitetura modular do laudo a custo de não oferecer uma leitura rápida de &ldquo;normal/alterado&rdquo;, preservando compatibilidade com impressão P&amp;B e sistemas legados.
              </p>
            </div>
            <div className="cp-feature-card">
              <span className="cp-feature-tag">Reflexão Crítica</span>
              <h3>O que eu reverteria hoje</h3>
              <p>
                Hoje eu reverteria a decisão de consolidar os primeiros componentes digitais antes de testar quebras de página na geração de PDF. Esse sequenciamento concentrou ajustes de impressão na fase final, quando os padrões visuais já estavam estruturados. Envolver a engenharia de emissão de PDF e mais especialidades desde a primeira semana reduziria retrabalho em exames extensos.
              </p>
            </div>
          </div>
          <div className="cp-appendix">
            <details open>
              <summary>Contexto e documentação do projeto</summary>
              <div>
                <p>
                  Projeto desenvolvido em 2022 em parceria entre Foursys e Hospital Israelita Albert Einstein, entregue como proposta modular (v3) e especificação de componentes no inventário EN-1 a EN-14 — o acompanhamento de implantação em produção ficou sob gestão interna da instituição. Por confidencialidade (NDA) e sigilo médico, arquivos integrais e fluxos proprietários permanecem restritos ao hospital.
                </p>
              </div>
            </details>
            <details>
              <summary>Autoria e time multidisciplinar</summary>
              <div>
                <p>
                  Israel Rozar — UX Lead. Conduzi a pesquisa, a arquitetura da informação, os componentes de laudo e os rituais de critique com o time de design da Foursys; atuei em conjunto com médicos laudadores e engenharia do Einstein na validação clínica e técnica.
                </p>
              </div>
            </details>
            <details>
              <summary>Ética e conformidade na pesquisa</summary>
              <div>
                <p>
                  O questionário com pacientes seguiu a LGPD com respostas anonimizadas. Os relatos médicos vieram de 4 entrevistas semiestruturadas — tratados como sinal qualitativo, nunca como taxa percentual — combinados à análise documental de mais de 80 exames reais.
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
  alt: "Ativação simplificada Claro Brasil em desktop e mobile: tela de detalhe da linha com cabeçalho fixo ao lado do fluxo móvel com resumo de oferta",
  caption:
    "Unificamos 22 jornadas de NET, Claro e Embratel em uma única arquitetura desktop e mobile para evitar que o operador alternasse entre sistemas legados durante a venda.",
}

const claroImages: CaseImage[] = [
  {
    src: "/images/claro-busca-cliente.webp",
    width: 1550,
    height: 972,
    alt: "Tela de busca de cliente do sistema de ativação, com campo de CPF e validação cadastral",
    caption:
      "Por que validar o CPF na entrada: antecipar checagens cadastrais e antifraude antes da oferta evita montar um combo inelegível e refazer o atendimento. Dados sintetizados para conformidade com a LGPD.",
  },
  {
    src: "/images/claro-jornadas.webp",
    width: 1440,
    height: 1440,
    alt: "Mapa da jornada de troca de chip no Miro com user stories, validações cadastrais e regras de oferta",
    caption:
      "Por que mapear a troca de chip antes das telas: expor dependências de validação, oferta e resumo financeiro revelou etapas duplicadas entre fluxos que podiam compartilhar a mesma esteira.",
  },
  {
    src: "/images/claro-detalhe-linha.webp",
    width: 1550,
    height: 972,
    alt: "Detalhe da linha com dados do cliente, cabeçalho fixo e grupos expansíveis",
    caption:
      "Por que manter cabeçalho fixo e blocos expansíveis: o operador consulta linha, plano e fatura sem abandonar a venda em andamento nem perder os dados do cliente.",
  },
  {
    src: "/images/claro-multicanal.webp",
    width: 1376,
    height: 932,
    alt: "Telas desktop e mobile da ativação simplificada Claro exibindo seleção de plano, resumo financeiro lateral e etapa de confirmação",
    caption:
      "Por que preservar a mesma taxonomia entre desktop e mobile: manter nomes de planos, resumo financeiro e confirmação iguais reduz divergências de operação entre loja física e consultores em campo.",
  },
]

export const claroPresentation: CasePresentationData = {
  title: "Claro · Ativação simplificada",

  context: "Claro Brasil · 2017–2018",

  headline: "22 jornadas comerciais unificadas em uma esteira desktop e mobile.",

  subtitle:
    "Na Claro Brasil (NET, Claro e Embratel), atuei como UX/UI Designer para eliminar a alternância entre sistemas legados em lojas físicas, televendas e campo. Unificamos 22 jornadas comerciais em uma esteira desktop e mobile de 5 etapas, com 70 oportunidades mapeadas e especificações V.2 entregues à engenharia.",

  role: "UX/UI Designer",

  team: "Design, Produto, Engenharia de sistemas e operação comercial (lojas e televendas)",

  scope: "Discovery, 22 jornadas, protótipos e especificação desktop e mobile",

  keyMetricLabel: "ENTREGA PRINCIPAL",
  keyMetric: "22 jornadas unificadas · 70 oportunidades (handoff V.2)",

  kicker: "Telecom · UX corporativo",

  hero: claroHero,

  nextCase: {
    title: "Neoenergia · Service Design",

    href: "/cases/neoenergia-conexao-digital",

    context: "Energia · P&D ANEEL · 34M de habitantes",
  },

  prevCase: {
    title: "Itaú Unibanco · Hub de Liquidez",

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
              A Claro Brasil precisava vender e ativar planos de NET, Claro e
              Embratel com menos retrabalho e menos erros de contratação em
              lojas físicas, televendas e campo.
            </p>
            <p>
              A tensão central era conciliar a velocidade exigida no balcão com
              regras tarifárias, combos e validações cadastrais espalhadas em
              sistemas legados desconectados.
            </p>
          </div>
          <CaseMetrics
            items={[
              ["20", "entrevistas em profundidade"],

              ["22", "jornadas unificadas na esteira"],

              ["70", "oportunidades priorizadas no discovery"],
            ]}
          />
          <div className="cp-cards-grid">
            <div className="cp-feature-card">
              <span className="cp-feature-tag">Contexto Operacional</span>
              <h3>Objetivo de negócio</h3>
              <p>
                Reduzir a troca manual de telas durante a venda e dar clareza ao
                valor final da oferta para operadores de loja, televendas e
                consultores em campo.
              </p>
            </div>
            <div className="cp-feature-card">
              <span className="cp-feature-tag">Enquadramento</span>
              <h3>Pergunta central</h3>
              <p>
                Como apoiar a continuidade do atendimento e tornar dados
                cadastrais, técnicos e financeiros compreensíveis em desktop e
                mobile?
              </p>
            </div>
          </div>
          <div className="cp-note">
            <h3>Meu papel × trabalho do time</h3>
            <p>
              <strong>O que conduzi:</strong> síntese da pesquisa operacional,
              arquitetura dos fluxos de navegação, protótipos de alta fidelidade
              e especificações de interface (desktop V.2 e mobile) entregues à
              engenharia.{" "}
              <strong>Onde contribuí com o time:</strong> entrevistas em campo,
              workshops de 3 dias e alinhamento de regras de oferta com
              lideranças de produto, engenharia de sistemas e operadores de loja
              e televendas.
            </p>
          </div>
        </>
      ),
    },

    {
      id: "esteira",
      tag: "22 Jornadas em 5 Etapas",
      title:
        "Decomposição de 22 jornadas comerciais em uma esteira unificada.",

      content: (
        <>
          <div className="cp-split">
            <div className="cp-split-content">
              <span className="cp-split-tag">Discovery & Pesquisa Operacional</span>
              <h3>O principal gargalo estava na troca de sistemas, não na venda</h3>
              <p>
                A observação em lojas físicas e televendas mostrou que parte relevante do atendimento era gasta alternando manualmente entre sistemas legados desconectados para consultar uma única linha. Chegamos a esse diagnóstico com benchmarking competitivo, 20 entrevistas em profundidade com operadores e lideranças, três dias de workshops e 10 perfis operacionais.
              </p>
              <ul className="cp-card-list">
                <li>
                  <strong>Ruptura de contexto:</strong> operadores trocavam de sistema várias vezes durante o mesmo atendimento presencial ou telefônico.
                </li>
                <li>
                  <strong>Insegurança tarifária:</strong> calcular descontos, combos e fidelização dependia de conferência manual durante a negociação.
                </li>
                <li>
                  <strong>Carga cognitiva:</strong> operadores precisavam memorizar códigos promocionais e regras de negócio para evitar erros de contratação.
                </li>
              </ul>
            </div>
            <div className="cp-split-media">
              <CaseFigure image={claroImages[0]} />
            </div>
          </div>
          <div className="cp-split">
            <div className="cp-split-content">
              <span className="cp-split-tag">Decisão 1 · Arquitetura de Fluxos</span>
              <h3>Unificar 22 jornadas em uma esteira de 5 etapas</h3>
              <p>
                <strong>Pergunta:</strong> manter fluxos separados por transação (troca de chip, ativação, upgrade, portabilidade) ou unificar a sequência?
              </p>
              <p>
                <strong>Opções e trade-offs:</strong> manter 22 fluxos isolados preservaria telas familiares, mas duplicava validações cadastrais e manutenção; unificar em 5 etapas exigia renegociar regras entre áreas de negócio e aceitar mais disciplina de sequência.
              </p>
              <p>
                <strong>Decisão e custo aceito:</strong> propus e consolidamos a esteira única de 5 etapas, aceitando o custo inicial de mapear exceções por transação para eliminar validações duplicadas. <strong>Evidência:</strong> mapeamento das 22 jornadas e das 70 oportunidades nos workshops com a operação.
              </p>
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
              alt: "Diagrama da esteira unificada de atendimento Claro Brasil em 5 etapas com camada persistente de contexto e paridade entre desktop e mobile",
              caption:
                "Por que estruturar em 5 etapas com camada fixa: separar identificação, oferta e confirmação com cabeçalho e resumo persistentes impede perda de contexto e recálculo manual entre telas.",
            }}
          />
          <div className="cp-note">
            <h3>Decisão 2 · Desacordo construtivo: tela única × etapas progressivas</h3>
            <p>
              <strong>Pergunta:</strong> exibir todos os parâmetros de oferta em uma tela única ou dividir a contratação em etapas? Lideranças comerciais defenderam a tela única para reduzir cliques. Em sessões práticas com operadores de loja e televendas, demonstrei que a densidade sem hierarquia aumentava erros de preenchimento. <strong>Decisão e custo aceito:</strong> negociamos etapas progressivas com resumo financeiro lateral sempre visível, aceitando cliques adicionais de navegação em troca de menor risco de erro contratual; lideranças comerciais e operação aprovaram o formato.
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
                Para reduzir erros de contratação e dar previsibilidade ao operador, estruturei três regras de arquitetura de informação:
              </p>
              <ol className="cp-card-list cp-card-list--numbered">
                <li>
                  <strong>1. Navegação progressiva por etapas:</strong> blocos expansíveis e passos numerados mantêm visível o status da contratação (heurística de Nielsen) e diminuem a carga cognitiva.
                </li>
                <li>
                  <strong>2. Preservação do contexto do cliente:</strong> cabeçalho fixo com dados da linha, status cadastral e atalhos rápidos evita recarregar telas no meio da conversa.
                </li>
                <li>
                  <strong>3. Composição financeira visível:</strong> o resumo lateral exibe produtos, descontos aplicados e valor final durante toda a montagem da oferta.
                </li>
              </ol>
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
              <span className="cp-split-tag">Decisão 3 · Consistência Multicanal</span>
              <h3>Mesma taxonomia com densidade adaptada por dispositivo</h3>
              <p>
                <strong>Pergunta:</strong> replicar a tela densa do desktop no celular ou criar fluxos independentes para consultores em campo?
              </p>
              <p>
                <strong>Decisão e custo aceito:</strong> mantive a mesma taxonomia de planos, ordem de etapas e regras de confirmação entre desktop e mobile, mas adaptei a densidade visual para telas menores. Aceitamos mais rolagem e etapas compactas no mobile a custo de não exibir todos os blocos simultaneamente, garantindo continuidade operacional entre balcão e campo.
              </p>
            </div>
            <div className="cp-split-media">
              <CaseFigure image={claroImages[3]} />
            </div>
          </div>
          <div className="cp-note">
            <h3>Status da entrega e limite das medições</h3>
            <p>
              O escopo deste ciclo foi concluído com o mapeamento das 22 jornadas, 70 oportunidades priorizadas e entrega das especificações desktop (V.2, 10/05/2018) e mobile (11/06/2018) para engenharia. Não medimos indicadores quantitativos pós-implantação (como tempo médio de atendimento ou taxa de erro em produção) durante a minha permanência no projeto.
            </p>
          </div>
          <div className="cp-cards-grid">
            <div className="cp-feature-card">
              <span className="cp-feature-tag">Disciplina de Escopo</span>
              <h3>O que ficou fora do recorte</h3>
              <p>
                Descartamos redesenhar os sistemas legados de faturamento e alterar as regras de validação de crédito de backoffice. Concentramos o esforço na camada de vendas desktop e mobile para entregar consistência de oferta sem depender da troca imediata do legado.
              </p>
            </div>
            <div className="cp-feature-card">
              <span className="cp-feature-tag">Reflexão Crítica</span>
              <h3>O que eu reverteria hoje</h3>
              <p>
                Eu reverteria a decisão de encerrar a entrega V.2 sem acordar uma linha de base operacional antes da implantação. Na época, concentramos o esforço em fechar os fluxos das 22 jornadas e entregar as especificações desktop e mobile. Sem o tempo por etapa e a taxa de erro medidos antes em lojas e televendas, não foi possível provar o ganho quantitativo após a entrega. Hoje eu condicionaria o fechamento do discovery à definição desse protocolo com Produto e Operação.
              </p>
            </div>
          </div>
        </>
      ),
    },

    {
      id: "escopo-equipe",
      tag: "Acervo & Equipe",
      title:
        "Acervo documentado, versões entregues e colaboração multidisciplinar.",

      content: (
        <div className="cp-appendix">
          <details open>
            <summary>Arquivos e versões entregues</summary>
            <div>
              <p>
                O acervo reúne registros de workshops, mapa da jornada de troca
                de chip, telas de ativação, detalhe da linha e confirmação
                mobile.
              </p>
              <p>
                A especificação de migração desktop registra V.2 em 10/05/2018;
                a versão mobile foi atualizada em 11/06/2018.
              </p>
            </div>
          </details>
          <details>
            <summary>Colaboração e equipe</summary>
            <div>
              <p>
                Israel Rozar — UX/UI Designer. Conduzi a arquitetura de fluxos,
                protótipos e especificação visual em parceria com lideranças de
                produto, engenharia de sistemas e operadores de loja e
                televendas da Claro Brasil.
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
  title: "Neoenergia · Service Design",

  context: "Neoenergia · EY × Livework · P&D ANEEL · 2020",

  headline:
    "Conectar a jornada digital ao serviço que acontece no mundo físico.",

  subtitle:
    "No P&D ANEEL da Neoenergia (EY × Livework), atuei como Senior Product Designer e Service Designer para reduzir rupturas entre canais digitais, atendimento e campo em 4 distribuidoras. Entregamos 5 Service Blueprints e 118 ideias priorizadas como baseline estratégico aprovado pelas diretorias (etapa de P&D, sem código final neste ciclo).",

  role: "Senior Product Designer · Service Design",

  team: "EY Business Transformation × Livework e áreas de operação e atendimento da Neoenergia",

  scope: "Diagnóstico de 11 canais, 5 Service Blueprints, fundação multi-tenant e 118 ideias",

  keyMetricLabel: "ENTREGA PRINCIPAL",
  keyMetric: "4 distribuidoras · 5 Service Blueprints · 118 ideias (P&D ANEEL)",

  kicker: "Energia · Service Design",

  hero: {
    src: "/images/v12-neoenergia-bento-service-design.webp",

    width: 2400,

    height: 1350,

    alt: "Visão executiva P&D ANEEL Neoenergia: recorte do Service Blueprint 2 (Uso e Pago), escala de 4 distribuidoras (18 estados, 34 milhões de habitantes e 13,9 milhões de clientes) e jornada futura com 118 ideias",

    caption:
      "Por que cruzar blueprint, escala nacional e priorização em uma visão única: mostrar que problemas de atendimento e fatura exigiam alinhar operação e backoffice nas 4 distribuidoras antes de redesenhar portais.",
  },

  prevCase: {
    title: "Claro · Ativação simplificada",

    href: "/cases/claro-ativacao-simplificada",

    context: "Telecom · Claro Brasil · 22 jornadas unificadas",
  },

  nextCase: {
    title: "Einstein · Laudos médicos",

    href: "/cases/einstein-laudos",

    context: "HIAE × Foursys · 2022",
  },

  chapters: [
    {
      id: "escala-nacional",
      tag: "Escala Nacional (34M)",
      title:
        "Unificação do atendimento para 34 milhões de habitantes e 13,9 milhões de clientes.",

      content: (
        <>
          <div className="cp-summary">
            <p>
              O Grupo Neoenergia (Iberdrola Brasil) precisava reduzir retrabalho
              em campo, deslocamentos desnecessários a agências e contestações
              de fatura nas 4 distribuidoras — <strong>Elektro</strong> (SP/MS),{" "}
              <strong>Coelba</strong> (BA), <strong>Celpe</strong> (PE) e{" "}
              <strong>Cosern</strong> (RN).
            </p>
            <p>
              A tensão central era unificar 11 canais de atendimento e processos
              de operação em 18 estados sem apagar particularidades regionais
              nem multiplicar quatro vezes o custo de tecnologia.
            </p>
          </div>
          <CaseMetrics
            items={[
              ["4", "distribuidoras integradas na mesma esteira"],

              ["5", "Service Blueprints do ciclo de vida"],

              ["118 ideias", "priorizadas para o roadmap de P&D"],
            ]}
          />
          <div className="cp-cards-grid">
            <div className="cp-feature-card">
              <span className="cp-feature-tag">Enquadramento</span>
              <h3>Pergunta central</h3>
              <p>
                Como conectar o atendimento digital ao trabalho de backoffice e
                equipes de campo nas 4 distribuidoras sem recriar quatro
                operações independentes?
              </p>
            </div>
            <div className="cp-feature-card">
              <span className="cp-feature-tag">Papel & Time</span>
              <h3>Meu papel × consórcio EY × Livework</h3>
              <p>
                <strong>O que conduzi e co-construí:</strong> diagnóstico de
                jornadas, estruturação de Service Blueprints e propostas de
                interface multi-tenant pela equipe de Business Transformation da
                EY. <strong>Com quem trabalhei:</strong> consultores da Livework
                e áreas de operação, atendimento e negócio da Neoenergia.
              </p>
            </div>
          </div>
          <div className="cp-split">
            <div className="cp-split-content">
              <span className="cp-split-tag">Diagnóstico · 11 Canais</span>
              <h3>Canais digitais falhavam quando desconectados da operação física</h3>
              <p>
                O diagnóstico de campo e a auditoria de processos nos 11 pontos de contato — de agências presenciais e postos credenciados a portal web, aplicativo, SMS, WhatsApp, call center e equipes de campo — revelaram três rupturas recorrentes:
              </p>
              <ul className="cp-card-list">
                <li>
                  <strong>Ruptura de continuidade:</strong> solicitações iniciadas em canais digitais ainda exigiam ida à agência para validar documentos presencialmente.
                </li>
                <li>
                  <strong>Silos operacionais:</strong> o call center não via ordens de serviço pendentes das equipes de campo, gerando ligações repetidas.
                </li>
                <li>
                  <strong>Assimetria de dados:</strong> faturas estimadas e histórico pouco claros elevavam o volume de contestações no atendimento.
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
                    "Por que dimensionar a escala antes de propor interfaces: qualquer falha de processo se multiplica por 13,9 milhões de clientes e 4 operações regionais em 18 estados.",
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
              A auditoria mostrou que a insatisfação com a fatura raramente era um problema de tela. Ela vinha de leituras por estimativa, regras de cobrança pouco claras e falta de sincronização entre despacho técnico e faturamento.
            </p>
            <ul className="cp-card-list">
              <li>
                <strong>Linha de interação:</strong> pontos onde o cliente registra solicitações ou envia a autoleitura.
              </li>
              <li>
                <strong>Linha de visibilidade:</strong> fronteira entre o que o cliente acompanha e as validações internas de crédito e engenharia.
              </li>
              <li>
                <strong>Linha de suporte interno:</strong> sistemas legados de despacho de campo e baixa bancária que sustentam o serviço.
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
                "Por que mapear frontstage e backstage na mesma prancha: tornar visível onde falhas internas de sistemas legados e campo causavam retrabalho para o cliente nas 4 distribuidoras.",
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
                  <strong>5. Abandono:</strong> busca por fontes alternativas, encerramento definitivo do contrato, quitação de débitos e retorno.
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
                    "Por que destacar a curva de criticidade no estágio Uso e Pago: apontar exatamente onde a análise de cobrança e o pagamento elevam o atrito para direcionar as ações imediatas.",
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
              <span className="cp-split-tag">Decisão 1 & 2 · Backoffice & Fundação Multi-tenant</span>
              <h3>Atacar gargalos de serviço e propor base multi-tenant</h3>
              <p>
                <strong>Decisão 1 (serviço antes da tela):</strong> diante da opção de redesenhar portais isoladamente ou auditar o backstage primeiro, priorizamos os 5 Service Blueprints antes da UI, aceitando adiar o código do portal final para não digitalizar processos quebrados.
              </p>
              <p>
                <strong>Decisão 2 (base multi-tenant):</strong> para atender Elektro, Coelba, Celpe e Cosern sem manter quatro portais independentes, propusemos um Design System multi-tenant com componentes compartilhados e temas por marca — projetado para aplicar critérios de contraste (WCAG) e evitar manutenção em quadruplicidade quando levado a código.
              </p>
              <ol className="cp-card-list cp-card-list--numbered">
                <li>
                  <strong>1. Mapear antes de propor:</strong> os blueprints orientaram quais fluxos de autosserviço precisavam ser desburocratizados primeiro.
                </li>
                <li>
                  <strong>2. Conectar atendimento e operação:</strong> especificamos componentes pensados para exibir o status das ordens de serviço de campo.
                </li>
                <li>
                  <strong>3. Governança multi-tenant:</strong> um único chassi de componentes com temas dedicados para as 4 distribuidoras.
                </li>
              </ol>
            </div>
            <div className="cp-split-media">
              <CaseFigure
                image={{
                  src: "/images/neoenergia-entregaveis-ui-design-system.webp",
                  width: 1600,
                  height: 900,
                  alt: "Entregáveis de interface, portal unificado e fundação de Design System multi-tenant para as 4 distribuidoras",
                  caption:
                    "Por que estruturar um chassi multi-tenant no P&D: preservar a marca de cada distribuidora por tokens temáticos sem multiplicar quatro vezes a arquitetura de telas.",
                }}
              />
            </div>
          </div>
        </>
      ),
    },

    {
      id: "matriz-118",
      tag: "118 Ideias Priorizadas",
      title:
        "118 ideias distribuídas na jornada futura como baseline para o roadmap de serviços.",

      content: (
        <>
          <div className="cp-split">
            <div className="cp-split-content">
              <span className="cp-split-tag">Decisão 3 · Priorização & Roadmap</span>
              <h3>Sequenciamento das 118 ideias em três horizontes</h3>
              <p>
                <strong>Pergunta:</strong> iniciar o roadmap por programas de longa maturação (como telemedição) ou entregar alívio imediato em fatura e autoleitura?
              </p>
              <p>
                <strong>Decisão e custo aceito:</strong> distribuímos as 118 ideias pelos 5 estágios da jornada futura e priorizamos ações de curto prazo antes de programas de infraestrutura. Aceitamos postergar iniciativas de maior investimento para atacar primeiro os pontos de maior criticidade no atendimento:
              </p>
              <ul className="cp-card-list">
                <li>
                  <strong>Ações imediatas (Quick Wins):</strong> clareza de comunicação na fatura e simplificação da autoleitura no aplicativo móvel.
                </li>
                <li>
                  <strong>Programas estruturantes:</strong> unificação do portal de serviços e integração dos sistemas de despacho de campo.
                </li>
                <li>
                  <strong>Horizonte de longo prazo:</strong> telemedição automatizada, canais conversacionais com supervisão humana e autoatendimento para geração solar distribuída.
                </li>
              </ul>
            </div>
            <div className="cp-split-media">
              <CaseFigure
                image={{
                  src: "/images/neoenergia-matriz-118-ideias.webp",
                  width: 2000,
                  height: 1195,
                  alt: "Mapa da Jornada futura do cliente Neoenergia com os 5 estágios (Contrato e instalo, Uso e pago, Preciso de suporte, Mudo o contrato e Abandono), ações, curva de criticidade e 118 ideias distribuídas por etapa",
                  caption:
                    "Por que ancorar as 118 ideias na curva de criticidade da jornada futura: impedir que iniciativas entrassem no roadmap desconectadas dos pontos reais de maior atrito operacional.",
                }}
              />
            </div>
          </div>
          <div className="cp-note">
            <h3>Desacordo estratégico & resultado do P&D ANEEL</h3>
            <p>
              Diretorias regionais pediram inicialmente quatro portais independentes para preservar particularidades locais. Cruzando os 5 Service Blueprints com o esforço de manutenção de backoffice, defendemos a arquitetura multi-tenant com tokens de marca — aceitando maior esforço inicial de governança entre regionais a custo de menos liberdade visual local, mas sem multiplicar quatro vezes o débito técnico. Os 5 blueprints e as 118 ideias foram aprovados pelas diretorias de operação e atendimento como baseline do P&D Estratégico ANEEL; por se tratar de etapa de P&D, o portal final não foi implementado em código nem medido em produção neste ciclo.
            </p>
          </div>
          <div className="cp-cards-grid">
            <div className="cp-feature-card">
              <span className="cp-feature-tag">Disciplina de Escopo</span>
              <h3>O que ficou fora do recorte</h3>
              <p>
                Esta etapa de P&D não incluiu desenvolvimento em código do portal final nem substituição imediata dos ERPs legados das 4 distribuidoras. Priorizamos o diagnóstico de backstage, os 5 Service Blueprints e as 118 ideias para atacar primeiro os gargalos que geravam retrabalho em campo.
              </p>
            </div>
            <div className="cp-feature-card">
              <span className="cp-feature-tag">Reflexão Crítica</span>
              <h3>O que eu reverteria hoje</h3>
              <p>
                Eu reverteria a decisão de conduzir os workshops de priorização apenas com pranchas estáticas de blueprints e listas de ideias. Sem protótipos navegáveis de dois fluxos críticos de campo durante a negociação, o debate sobre o esforço da esteira multi-tenant ficou abstrato demais para parte das diretorias regionais. Levar esses fluxos simulados desde a priorização teria reduzido a resistência à arquitetura unificada mais cedo.
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
            <summary>Governança e alcance do P&D ANEEL</summary>
            <div>
              <p>
                Os 5 Service Blueprints e as 118 ideias foram aprovados pelas
                diretorias de operação e atendimento do Grupo Neoenergia no
                programa de P&D Estratégico ANEEL. O material serviu como
                baseline para orientar as esteiras de unificação de canais das 4
                distribuidoras.
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
      "Especialistas precisavam localizar vencimentos, eventos futuros e sinais de Open Finance sem perder o contexto do cliente nem o histórico do que já havia sido tratado. A interface organiza esses eventos, os filtros operacionais e o registro de ações em uma única tabela de acompanhamento da carteira.",

    users:
      "Especialistas de investimentos, os assessores que os auxiliam no acompanhamento das carteiras e gestores que monitoram a atuação das equipes.",

    contribution:
      "Conduzi a arquitetura de consulta, a definição de filtros combináveis, a estrutura da tabela densa e a especificação de estados vazios e de carregamento. Atuei com Produto e Engenharia para alinhar o handoff às regras descritas na base de conhecimento do produto.",

    research:
      "Mostrar a data de um vencimento não bastava para a atuação: o especialista precisava reconhecer o contexto do cliente e saber o que já tinha sido tratado a partir de diferentes pontos de entrada (panorama, operações, cliente e acesso direto). Com base no discovery e na base de conhecimento do produto, centralizei esses fluxos na interface consolidada de Gestão de Liquidez.",

    constraints: [
      "Distinguir vencimentos, eventos futuros e Open Finance sem fragmentar a lógica de consulta.",

      "Preservar a relação entre data, produto, valor, cliente e situação da atuação em uma tabela densa.",

      "Acomodar diferentes pontos de entrada: panorama, operações, contexto do cliente e acesso direto.",
    ],

    decisions: [
      [
        "Reutilizar a lógica de consulta em abas",

        "Entre criar telas separadas ou unificar tudo em uma lista mista, mantive Vencimentos, Eventos futuros e Open Finance em abas distintas com a mesma estrutura de busca, filtros e tabela. Aceitei exigir a troca de aba para preservar a diferença entre eventos sem forçar o usuário a reaprender a navegação.",
      ],

      [
        "Manter o recorte de filtros sempre explícito",

        "Em vez de ocultar critérios de período, produto, carteira, status e cliente em menus fechados, priorizei filtros visíveis e combináveis junto à tabela, a custo de maior densidade no topo da tela. Assim, a leitura de totais e estados acompanha diretamente o recorte ativo.",
      ],

      [
        "Ligar consulta, registro de ação e estados de exceção",

        "Descartei tratar a tabela apenas como relatório de leitura e vinculei cada linha ao registro de valor, comentários e contato previstos na base de conhecimento, além de estados explícitos de carregamento e vazio. O custo foi ampliar a especificação de estados no handoff para evitar falhas silenciosas em consultas sem retorno.",
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
      "Os dados cadastrais e valores financeiros apresentados na interface foram sintetizados para preservação do sigilo bancário e conformidade com a LGPD, mantendo fidelidade estrita às regras de ordenação de vencimentos, filtros operacionais e contratos de dados acordados com especialistas e assessores.",

    scope: "Consulta, filtros, estados e registro de atuação",
    flowTag: "Fluxo & Interface Canônica",
    flowTitle: "Como especialistas, assessores e gestores operam Gestão de Vencimentos ponta a ponta.",
    outOfScope:
      "Mantive fora deste recorte a criação de telas isoladas por tipo de evento e ações em massa sem visualização do contexto do cliente. Priorizei uma lógica única de busca, filtros e tabela compartilhada entre Vencimentos, Eventos futuros e Open Finance, a custo de exigir abas explícitas para separar naturezas financeiras distintas.",
    reflection:
      "Hoje eu revisitaria a decisão de deixar o critério de urgência implícito apenas na combinação de ordenação por data e filtros manuais. Em carteiras extensas, depender só da combinação de filtros exige esforço extra do especialista e do assessor para separar o que vence no curto prazo do que ainda pode aguardar. Em uma nova iteração, testaria um agrupamento explícito de urgência junto aos estados de atuação antes do handoff.",
  },

  "hub-liquidez": {
    summary:
      "Na plataforma íon for Advisors (IFA), especialistas precisavam cruzar múltiplas abas para conciliar saldo em conta, recursos de Open Finance e liquidez projetada antes de abordar clientes. O objetivo foi estruturar uma visão única capaz de separar disponibilidade imediata de projeção temporal sem perder a rastreabilidade da origem.",

    users:
      "Especialistas de investimentos e os assessores que os auxiliam a acompanhar recursos disponíveis e oportunidades de atuação nas carteiras.",

    contribution:
      "Conduzi a definição da hierarquia dos dados financeiros, a separação temporal dos valores e a conexão entre o resumo da carteira, os filtros operacionais e a fila de clientes. Alinhei os contratos de visualização e estados de atuação com Produto, Engenharia e áreas de negócio.",

    research:
      "Misturar dinheiro já disponível em conta com projeções futuras dificultava justificar a abordagem ao cliente. A partir do discovery e da base funcional do produto, conectei posição atual (incluindo valores de liquidez imediata do Cofrinho IFA), projeção de recursos e fila prioritária de clientes em uma única leitura.",

    constraints: [
      "Diferenciar dinheiro disponível agora de uma projeção para outra janela.",

      "Manter a origem Itaú e Open Finance explícita durante a leitura.",

      "Apresentar atualização do dado e status de atuação sem confundi-los com disponibilidade financeira.",
    ],

    decisions: [
      [
        "Separar posição, variação e projeção",

        "Descartei somar saldo atual e valores futuros em um único indicador totalizador e separei total disponível agora, variação prevista e liquidez projetada. Aceitei ocupar mais espaço no cabeçalho do resumo para evitar que recursos projetados fossem interpretados como disponibilidade imediata.",
      ],

      [
        "Vincular a janela de tempo ao valor projetado",

        "Entre manter filtros de período isolados ou acoplados ao indicador, vinculei as janelas de fim do dia, 7 dias e 30 dias diretamente ao título do valor projetado. O custo foi limitar a comparação simultânea entre múltiplas janelas na mesma tela para reduzir leituras fora do período selecionado.",
      ],

      [
        "Conectar o resumo à fila operacional por origem",

        "Mantive a origem Itaú e Open Finance explícita nos filtros e na tabela junto a cliente, carteira, agência/conta, disponível agora, total projetado e status. Aceitei maior densidade de colunas para que o especialista e o assessor filtrem por origem e faixa de valor antes de iniciar o contato.",
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
    flowTag: "Fluxo & Interface Canônica",
    flowTitle: "Como especialistas e assessores operam o Hub de Liquidez ponta a ponta.",
    outOfScope:
      "Deixei fora da primeira camada visual a exposição de fórmulas internas de reconciliação e regras automáticas de ranqueamento que dependiam de governança do domínio. Priorizei separar claramente saldo disponível agora, variação prevista e projeção por janela (fim do dia, 7 e 30 dias), a custo de não concentrar todas as variáveis de composição em uma única coluna.",
    reflection:
      "Hoje eu revisitaria a decisão de exibir a lista de clientes priorizados sem explicitar, na própria linha da tabela, o critério que levou aquele cliente ao topo da fila. O custo de ocultar essa regra foi aumentar a dependência de interpretação do especialista e do assessor antes do contato. Também definiria antes do handoff, junto a Produto e domínio, um protocolo para checar se os usuários distinguiam disponibilidade imediata de liquidez projetada sem erro.",
  },

  movimentacoes: {
    summary:
      "Na transição do Extrato EA para o IFA, concentrar todos os saldos em uma única aba obrigaria o profissional a sair da tarefa atual apenas para consultar o saldo provisionado. A arquitetura mantém o saldo provisionado visível no cabeçalho entre jornadas e concentra em Movimentações o extrato detalhado e os limites de crédito (CEP, CEP Plus e limite).",

    users:
      "Especialistas de investimentos e os assessores que os auxiliam a consultar lançamentos, compreender saldos e explicar movimentações dos clientes.",

    contribution:
      "Conduzi o discovery de arquitetura da informação, comparei alternativas de posicionamento do saldo provisionado e defini a divisão entre informação persistente no cabeçalho e consulta detalhada em Movimentações, em alinhamento com Produto e Engenharia.",

    research:
      "O saldo provisionado é consultado durante diferentes tarefas da carteira e não podia exigir troca constante de aba, enquanto conta corrente, investimentos e conta gráfica exigiam regras próprias de leitura. No discovery, comparei seis alternativas de visibilidade até definir o provisionado persistente no cabeçalho e os limites contextualizados em Movimentações.",

    constraints: [
      "O saldo provisionado é necessário em diferentes jornadas e não pode depender de troca de aba.",

      "Conta corrente, investimentos e conta gráfica têm informações próprias e precisam permanecer distinguíveis.",

      "Consulta por período, busca e ordenação devem manter contexto suficiente para interpretar os lançamentos.",
    ],

    decisions: [
      [
        "Manter o saldo provisionado no cabeçalho",

        "Comparei manter o resumo completo apenas em Movimentações ou usar faixa complementar, bloco no histórico, painel acionável, sidebar e contingência, e decidi fixar o saldo provisionado no cabeçalho. Aceitei ocupar espaço permanente na navegação superior para eliminar trocas de aba em tarefas transversais.",
      ],

      [
        "Contextualizar limites de crédito em Movimentações",

        "Descartei levar CEP, CEP Plus e limite para o cabeçalho global e mantive esses dados junto ao aprofundamento financeiro em Movimentações. O custo foi exigir um clique até o módulo para consultar limites, em troca de preservar o cabeçalho enxuto sem duplicar o extrato na navegação global.",
      ],

      [
        "Separar domínios com consulta consistente",

        "Em vez de misturar lançamentos heterogêneos em uma lista única, separei conta corrente, investimentos e conta gráfica seguindo a base de conhecimento do produto, mantendo o mesmo padrão de período, busca e ordenação. Aceitei a alternância entre domínios para preservar os campos específicos de cada operação.",
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
      "Os lançamentos de extrato e valores apresentados foram sintetizados para conformidade com o sigilo bancário, preservando a hierarquia da informação entre o saldo provisionado no cabeçalho e os módulos detalhados de conta corrente e investimentos.",

    scope: "Arquitetura do extrato e contexto financeiro transversal",
    flowTag: "Fluxo & Arquitetura de Consulta",
    flowTitle: "Como especialistas e assessores consultam saldos e Movimentações ponta a ponta.",
    outOfScope:
      "Descartei transportar limites de crédito (CEP, CEP Plus e limite) ou um extrato resumido completo para o cabeçalho global, assim como soluções de painel lateral e faixa complementar. Aceitei exigir um clique adicional até Movimentações para aprofundar limites e lançamentos, em troca de manter o saldo provisionado visível entre jornadas sem sobrecarregar a navegação global.",
    reflection:
      "Hoje eu revisitaria a decisão de encerrar o recorte de arquitetura sem uma comparação lado a lado com tarefas equivalentes do Extrato EA. Mesmo com a separação clara entre saldo provisionado no cabeçalho e limites em Movimentações, o custo dessa lacuna foi não validar antecipadamente onde ocorriam mais trocas de contexto na rotina real. Eu incluiria essa checagem comparativa antes de congelar o comportamento de conta corrente, investimentos e conta gráfica.",
  },

  campanhas: {
    summary:
      "Operações comerciais em lote falham quando configuração da base, execução pelos especialistas e acompanhamento gerencial perdem sincronia de estado. O sistema de campanhas estrutura público, vigência, processamento e registro de atuação em um fluxo contínuo entre esses três perfis.",

    users:
      "Administradores de backoffice que configuram campanhas; especialistas que atuam com os clientes; gestores que acompanham a execução das equipes.",

    contribution:
      "Conduzi a modelagem dos fluxos de configuração, consulta e manutenção, a hierarquia de dados da tabela e a especificação de estados de carregamento, vazio, processamento e erro. Alinhei esse recorte de interface às regras dos três perfis descritos na base de conhecimento do produto.",

    research:
      "Administração de backoffice, execução pelo especialista e acompanhamento por hierarquia gerencial dependem do mesmo estado da base: se o processamento falha ou a vigência muda, todos os perfis precisam reconhecer a consequência. Os fluxos de tela (screenflows) e a base de conhecimento guiaram a separação de informações gerais, público, campos personalizados e estados operacionais.",

    constraints: [
      "Combinar público, vigência e ativação para controlar a visibilidade da campanha.",

      "Acomodar importação de base, processamento e estados de erro sem confundir configuração com execução.",

      "Distinguir permissões e tarefas de administradores, especialistas e gestores.",
    ],

    decisions: [
      [
        "Separar configuração e ativação da campanha",

        "Em vez de publicar a campanha imediatamente ao fim do cadastro, dividi o fluxo entre configuração (nome, descrição, tipo, categoria, público e vigência) e ativação explícita. Aceitei um passo adicional para o administrador de backoffice para impedir que campanhas incompletas ficassem visíveis aos especialistas.",
      ],

      [
        "Explicitar estados de processamento antes da manutenção",

        "Descartei ocultar falhas de importação atrás de mensagens genéricas e mapeei estados próprios de carregamento, vazio, processamento e erro na tabela de manutenção. O custo foi aumentar a quantidade de estados a especificar e manter para tornar claro quando uma campanha pode ser publicada, editada ou retirada do ar.",
      ],

      [
        "Conectar atuação registrada e visão gerencial sem confundir conversão",

        "Mantive a evolução de Pendente para Em andamento e Atuado com valor e comentários, agregada por hierarquia gerencial conforme a documentação do produto. Evitei rotular atuação registrada como venda concluída, a custo de exigir cruzamento separado para apurar conversão comercial.",
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
    flowTag: "Fluxo & Parametrização em Lote",
    flowTitle: "Como administradores, especialistas e gestores operam Gestão de Campanhas ponta a ponta.",
    outOfScope:
      "Mantive fora da etapa inicial de criação a ativação automática da campanha logo após o upload da base e o vínculo automático entre atuação registrada e conversão comercial. Aceitei adicionar uma etapa explícita de conferência de estado (processando, carregada, vazia ou erro) antes de disponibilizar a campanha, para evitar que bases incompletas chegassem aos especialistas.",
    reflection:
      "Hoje eu revisitaria a decisão de tratar as transições de erro, edição e exclusão apenas no nível de fluxos de tela sem fechar desde o início as regras de preservação de dados entre etapas. Em fluxos administrativos em lote, perder preenchimento após uma falha de processamento gera retrabalho direto para o administrador de backoffice. Eu anteciparia a especificação de recuperação de erro e retorno seguro após exclusão junto à engenharia.",
  },

  "registros-atendimento": {
    summary:
      "Entre um contato e outro, especialistas e assessores perdiam tempo recuperando o histórico do cliente e digitando atas manualmente. A solução posiciona resumos dos últimos 5 atendimentos assistidos por IA no fluxo de trabalho e gera minutas preliminares sujeitas à revisão e confirmação humana obrigatória.",

    users:
      "Especialistas de investimentos e os assessores que os auxiliam a retomar o histórico do cliente e documentar os pontos acordados em cada contato.",

    contribution:
      "Conduzi a arquitetura de interação entre a consulta ao histórico recente e o campo de registro assistido por IA. Defini o fluxo de supervisão humana obrigatória em conjunto com áreas de negócio para preservar a integridade e a conformidade das notas bancárias.",

    research:
      "Na rotina de especialistas e assessores, a transição entre atendimentos gerava perda de contexto e sobrecarga de digitação. A partir desse mapeamento, estruturei resumos em tópicos dos últimos 5 atendimentos e sugestões de ata preliminar para validação antes da gravação.",

    constraints: [
      "Garantir que o conteúdo sugerido pela IA seja sempre revisado e confirmado pelo especialista antes de ser gravado no prontuário do cliente.",

      "Preservar a fidelidade técnica de termos financeiros, evitando alucinações ou omissão de direcionamentos de carteira.",

      "Manter a recuperação de histórico compatível com o intervalo curto entre atendimentos.",
    ],

    decisions: [
      [
        "Limitar o painel lateral aos 5 resumos mais recentes",
        "Entre exibir o histórico completo de notas brutas ou sintetizar apenas os contatos mais recentes, priorizei os 5 últimos resumos em tópicos no painel lateral do cliente. Aceitei exigir abertura do histórico completo para casos mais antigos em troca de retomada rápida de assuntos pendentes.",
      ],

      [
        "Exigir validação humana antes da gravação (Human-in-the-Loop)",
        "Descartei o salvamento automático de atas geradas por IA e defini o texto sugerido como minuta preliminar editável com confirmação ativa obrigatória do especialista. Aceitei um passo extra de revisão antes de salvar para evitar alucinações ou omissão de direcionamentos de carteira no prontuário bancário.",
      ],

      [
        "Priorizar precisão e conformidade acima de velocidade isolada",
        "Em vez de avaliar o fluxo apenas pelo tempo economizado na digitação, defini critérios de qualidade focados em fidelidade técnica dos termos financeiros, ausência de omissões e esforço de correção. O custo foi tornar a validação mais exigente para proteger a rastreabilidade regulatória.",
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
      "Em operações financeiras reguladas, a assistência por IA só sustenta ganho operacional quando mantém rastreabilidade auditável: o especialista valida, edita e aprova cada registro antes da persistência bancária (Human-in-the-Loop).",

    boundary:
      "Os registros e notas de atendimento apresentados são anonimizados para conformidade com a LGPD e o sigilo bancário, demonstrando a arquitetura de interação assistida validada com os times de negócio.",

    scope: "Arquitetura de interação para resumos assistidos por IA e governança de notas",
    flowTag: "Fluxo & Governança de IA",
    flowTitle: "Como especialistas e assessores operam Registros de Atendimento com revisão humana.",
    outOfScope:
      "Deixei fora do fluxo qualquer gravação automática de resumos gerados por IA sem confirmação ativa do especialista e métricas baseadas apenas em velocidade de preenchimento. Aceitei incluir um passo obrigatório de revisão e edição manual antes de salvar a nota, para mitigar omissões e preservar a fidelidade de termos financeiros no prontuário.",
    reflection:
      "Hoje eu revisitaria a decisão de desenhar o fluxo assistido por IA sem definir, na mesma entrega, uma referência visual explícita do esforço de revisão frente ao registro original. Se corrigir uma minuta imprecisa consumir quase o mesmo esforço que redigir do zero, o recurso perde utilidade na rotina entre atendimentos. Eu acoplaria à arquitetura um critério estruturado para acompanhar edições frequentes, omissões e consultas ao histórico completo.",
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
    vencimentos: "Consulta unificada de vencimentos e eventos",
    "hub-liquidez": "Consolidação de composição de liquidez",
    movimentacoes: "Transição Extrato EA para IFA",
    campanhas: "Operação e parametrização em lote",
    "registros-atendimento": "Resumos assistidos por IA com supervisão",
  }

  const data: CasePresentationData = {
    title: `Itaú · ${project.title}`,

    context: "íon for Advisors · 2024–2026",

    headline: project.title,

    subtitle: project.subtitle,

    role: "Senior Product Designer",

    team: "Design, Produto, Engenharia e áreas de negócio",

    scope: story.scope,

    keyMetricLabel: "ENTREGA PRINCIPAL",
    keyMetric: itauKeyMetrics[caseSlug] || "Operação financeira",

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
          context: "HIAE × Foursys · 2022",
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
        tag: story.flowTag,
        title: story.flowTitle,

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
                <p>{story.outOfScope}</p>
              </div>
              <div className="cp-feature-card">
                <span className="cp-feature-tag">Reflexão Crítica</span>
                <h3>O que eu revisitaria hoje</h3>
                <p>{story.reflection}</p>
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
                      target="_blank"
                      rel="noopener noreferrer"
                    >
                      Base de conhecimento funcional do produto
                      <span className="pf-sr-only"> (abre em nova aba)</span>
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
                  contratos de dados e fluxos operacionais de investimentos.
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
