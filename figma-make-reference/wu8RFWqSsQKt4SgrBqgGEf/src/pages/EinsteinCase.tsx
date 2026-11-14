import { Link, Pill, Text } from "../design-system"
import { PageMeta } from "../components/PageMeta"
import { SiteFooter, SiteHeader } from "../components/SiteChrome"

export default function EinsteinCase() {
  return (
    <>
      <PageMeta
        title="Consumo de Resultados — Case de Israel Rozar"
        description="Case de UX Lead sobre a sistematização de laudos para pacientes e médicos no Einstein."
      />
      <Link className="skip-link" href="#conteudo">
        Pular para o conteúdo
      </Link>
      <SiteHeader casePage />
      <main id="conteudo">
        <section
          className="case-page-hero"
          id="topo"
          aria-labelledby="case-page-title"
        >
          <Link className="case-back-link" href="/#trabalho">
            ← Voltar ao trabalho selecionado
          </Link>
          <Pill tone="accent">Case documentado · Saúde</Pill>
          <Text as="h1" id="case-page-title">
            Consumo de Resultados
          </Text>
          <Text className="case-page-deck">
            Como um trabalho coletivo transformou laudos heterogêneos em uma
            linguagem visual modular — e revelou que clareza percebida não é o
            mesmo que compreensão.
          </Text>
          <div className="case-page-meta" aria-label="Contexto do projeto">
            <div>
              <Text as="span">Organizações</Text>
              <Text as="strong">Einstein × Foursys</Text>
            </div>
            <div>
              <Text as="span">Papel documentado</Text>
              <Text as="strong">UX Lead</Text>
            </div>
            <div>
              <Text as="span">Período</Text>
              <Text as="strong">Registros de 2022</Text>
            </div>
          </div>
        </section>

        <section
          className="section work case-page-content"
          aria-labelledby="case-heading"
        >
          <article className="featured-case">
            <div className="case-summary">
              <div className="case-kicker">
                <Pill>Saúde · UX Lead</Pill>
                <Text>Einstein × Foursys · registros de 2022</Text>
              </div>
              <Text as="h2" id="case-heading">
                Uma linguagem visual modular para laudos heterogêneos.
              </Text>
              <Text className="case-lead">
                Um trabalho coletivo entre pesquisa, conteúdo, interface e
                viabilidade técnica para facilitar a localização de informações
                sem simplificar indevidamente o contexto clínico.
              </Text>
              <div className="case-role">
                <Text as="strong">Atuação documentada</Text>
                <ul>
                  <li>Israel Rozar — UX Lead</li>
                  <li>Pesquisa com médicos e questionário com pacientes</li>
                  <li>Sistematização de dados, exceções e componentes</li>
                  <li>Testes, revisão pós-teste e discussão com arquitetura</li>
                </ul>
              </div>
            </div>

            <div className="case-evidence" aria-label="Escopo da pesquisa">
              <Text as="span">Universos de evidência</Text>
              <div className="evidence-grid">
                <div>
                  <Text as="strong">04</Text>
                  <Text>entrevistas médicas semiestruturadas</Text>
                </div>
                <div>
                  <Text as="strong">121</Text>
                  <Text>respostas no questionário exploratório</Text>
                </div>
                <div>
                  <Text as="strong">14</Text>
                  <Text>categorias de laudos no escopo</Text>
                </div>
                <div>
                  <Text as="strong">44</Text>
                  <Text>participantes reportados nos testes</Text>
                </div>
              </div>
              <Text className="evidence-note">
                Amostras com objetivos diferentes: não se somam e não
                representam conquistas individuais.
              </Text>
            </div>
          </article>

          <div className="case-detail">
            <div className="case-question">
              <Text as="span">Desafio enquadrado</Text>
              <Text as="h3">
                Como facilitar a localização e a leitura do laudo sem induzir
                uma interpretação clínica isolada?
              </Text>
              <div className="case-perspectives">
                <div>
                  <Text as="strong">Paciente</Text>
                  <Text>
                    Busca o próprio resultado e precisa localizar o que importa
                    para levar à conversa clínica.
                  </Text>
                </div>
                <div>
                  <Text as="strong">Médico</Text>
                  <Text>
                    Relaciona resultado, referência, comentários, histórico e
                    contexto clínico.
                  </Text>
                </div>
              </div>
            </div>

            <div className="case-principles" aria-label="Decisões de design">
              <Text as="span">Decisões que estruturaram o sistema</Text>
              <ol>
                <li>
                  <span>01</span>
                  <div>
                    <Text as="strong">Âncora de leitura estável</Text>
                    <Text>
                      Nome, material, resultado e referência formam o primeiro
                      nível de leitura.
                    </Text>
                  </div>
                </li>
                <li>
                  <span>02</span>
                  <div>
                    <Text as="strong">Componentes para variação real</Text>
                    <Text>
                      Resultados numéricos, textuais, múltiplos e comentários
                      usam uma lógica comum sem apagar exceções.
                    </Text>
                  </div>
                </li>
                <li>
                  <span>03</span>
                  <div>
                    <Text as="strong">Sinais redundantes</Text>
                    <Text>
                      Texto, posição e tratamento visual trabalham juntos; cor
                      nunca comunica o estado sozinha.
                    </Text>
                  </div>
                </li>
              </ol>
            </div>
          </div>

          <div className="case-comparison">
            <div className="comparison-heading">
              <div>
                <Text as="span">Antes e proposta</Text>
                <Text as="h3">
                  Menos competição visual. Mais relação entre os dados.
                </Text>
              </div>
              <Text>
                A comparação evidencia uma mudança de hierarquia, não uma
                alegação de eficácia clínica.
              </Text>
            </div>

            <div className="comparison-grid">
              <figure className="source-report">
                <figcaption>
                  <span>01</span>
                  Documento original · recorte anonimizado
                </figcaption>
                <div>
                  <img
                    src="/images/hiae-laudo-original-recorte.webp"
                    width="1120"
                    height="640"
                    alt="Recorte anonimizado do laudo original, com título, técnica, indicação e análise em uma composição textual densa"
                    loading="lazy"
                    decoding="async"
                  />
                </div>
              </figure>

              <figure className="proposed-report">
                <figcaption>
                  <span>02</span>
                  Estrutura proposta · reconstrução demonstrativa
                </figcaption>
                <div>
                  <img
                    src="/images/hiae-laudo-proposta-completa.webp"
                    width="1600"
                    height="1199"
                    alt="Estrutura proposta completa, com título destacado e resultados organizados em colunas de valor, unidade e referência"
                    loading="lazy"
                    decoding="async"
                    style={{ objectFit: "contain" }}
                  />
                </div>
                <Link
                  className="image-full-link"
                  href="/images/hiae-laudo-proposta-completa.webp"
                >
                  Ver proposta em tamanho completo
                </Link>
              </figure>
            </div>
          </div>

          <div className="case-test">
            <div className="test-intro">
              <Text as="span">O aprendizado mais importante</Text>
              <Text as="h3">
                Clareza percebida não é o mesmo que compreensão.
              </Text>
              <Text>
                A documentação registra exposição breve, avaliações e tarefas.
                Os resultados abaixo medem dimensões diferentes e não são uma
                comparação antes/depois.
              </Text>
            </div>
            <div className="test-results">
              <div className="test-metric test-metric--accent">
                <Text as="span">Percepção</Text>
                <Text as="strong">84,3%</Text>
                <Text>avaliaram as informações como claras</Text>
              </div>
              <div className="test-metric">
                <Text as="span">Desempenho</Text>
                <Text as="strong">56,25%</Text>
                <Text>interpretaram corretamente na tarefa documentada</Text>
              </div>
            </div>
          </div>

          <div className="case-limits">
            <div>
              <Text as="span">Evidências do trabalho</Text>
              <ul>
                <li>Pesquisa e análise documental registradas</li>
                <li>Sistema modular e iterações de protótipo</li>
                <li>Teste da proposta com resultados documentados</li>
                <li>Discussão de viabilidade com arquitetura</li>
              </ul>
            </div>
            <div>
              <Text as="span">O que não está demonstrado</Text>
              <ul>
                <li>Lançamento ou integração concluída</li>
                <li>Redução de tempo, erros ou custo operacional</li>
                <li>Melhoria causal de compreensão entre versões</li>
                <li>Certificação clínica ou de acessibilidade</li>
              </ul>
            </div>
            <div className="case-next">
              <Text as="span">Próxima validação recomendada</Text>
              <Text>
                Medir separadamente tempo para localizar o resultado, associação
                entre valor, unidade e referência, interpretação correta e erros
                críticos — com revisão clínica e tecnologias assistivas.
              </Text>
            </div>
          </div>

          <aside className="case-disclosure">
            <Text as="strong">Nota de transparência</Text>
            <Text>
              Case reconstruído a partir de registros históricos de 2022. O
              trabalho foi coletivo; protótipos não equivalem a implementação.
              Dados reais sensíveis foram omitidos; a proposta utiliza conteúdo
              fictício demonstrativo.
            </Text>
          </aside>
        </section>
      </main>
      <SiteFooter />
    </>
  )
}

