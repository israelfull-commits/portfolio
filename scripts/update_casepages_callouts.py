import os

callout_jsx = '''          <CaseFigure
            image={{
              src: "/images/hiae-componente-protrombina-crop.webp",
              width: 1408,
              height: 534,
              alt: "Recorte macro de detalhe do protótipo documentado (v3) exibindo os campos de Tempo de Protrombina (RNI) e parâmetros de referência",
              caption:
                "Protótipo v3 reconstruído com dados demonstrativos. Não é a tela original nem orientação clínica.",
            }}
          />
          <ol className="cp-callout-list">
            <li className="cp-callout-item">
              <span className="cp-callout-badge">1</span>
              <div>
                <strong>examTitle.</strong> Nome do exame com o material (tempo de protrombina, plasma).
              </div>
            </li>
            <li className="cp-callout-item">
              <span className="cp-callout-badge">2</span>
              <div>
                <strong>Uma linha por parâmetro.</strong> Atividade e Relação (RNI) em linhas próprias.
              </div>
            </li>
            <li className="cp-callout-item">
              <span className="cp-callout-badge">3</span>
              <div>
                <strong>Sinal redundante, sem dependência de cor.</strong> Ícone de verificação e cor de feedback junto ao valor.
              </div>
            </li>
            <li className="cp-callout-item">
              <span className="cp-callout-badge">4</span>
              <div>
                <strong>Resultado e referência abaixo do título, lado a lado.</strong> Mudança da v3.0; a unidade acompanha a referência.
              </div>
            </li>
          </ol>
          <p style={{ fontSize: "0.875rem", color: "var(--cp-muted)", marginBottom: "2rem", lineHeight: 1.5 }}>
            Demais mudanças da v3.0: grid, espaçamento e largura do texto ajustados, cor do comentário alterada e metadados organizados em colunas, sem negrito.
          </p>'''

old_target = '''          <CaseFigure
            image={{
              src: "/images/hiae-componente-protrombina-crop.webp",
              width: 1408,
              height: 534,
              alt: "Recorte macro de detalhe do protótipo documentado (v3) exibindo os campos de Tempo de Protrombina (RNI) e parâmetros de referência",
              caption:
                "Detalhe de um protótipo reconstruído (v3), com dados anonimizados e conteúdo demonstrativo. Anatomia dos componentes DataField e ExamTitle.",
            }}
          />'''

for path in ['site/src/pages/CasePages.tsx', 'portfolio-verde/src/pages/CasePages.tsx']:
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    content = content.replace('width: 1600,\n  height: 900,', 'width: 2400,\n  height: 1327,')
    content = content.replace('width: 1600,\n    height: 900,', 'width: 2400,\n    height: 1327,')
    if old_target in content:
        content = content.replace(old_target, callout_jsx)
        print('Replaced target in', path)
    else:
        print('Target not found in', path)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
print('Updated CasePages.tsx in both projects')

