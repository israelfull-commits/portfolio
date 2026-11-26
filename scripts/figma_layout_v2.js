// ============================================================================
// LAYOUT KIT V2 — Grid 12 col (74/24), escala tipográfica fixa, base 8px.
// REGRAS: (1) largura sempre explícita, altura sempre HUG; (2) nunca FILL no
// eixo cruzado de pai HUG; (3) entregáveis crescem na altura, nunca cortam;
// (4) linhas horizontais só com filhos de largura calculada que somam o total.
// ES5 clássico: sem spread, sem optional chaining.
// ============================================================================
var GRID = { page: 1280, margin: 64, content: 1152, col: 74, gutter: 24 };
function span(n) { return n * GRID.col + (n - 1) * GRID.gutter; }

var TY2 = {
  display: { s: 40, lh: 48, w: 'bold', t: -0.8 },
  h2: { s: 28, lh: 36, w: 'bold', t: -0.4 },
  h3: { s: 20, lh: 28, w: 'semibold', t: -0.2 },
  bodyL: { s: 18, lh: 28, w: 'regular' },
  body: { s: 16, lh: 26, w: 'regular' },
  small: { s: 14, lh: 22, w: 'regular' },
  smallStrong: { s: 14, lh: 22, w: 'semibold' },
  caption: { s: 12, lh: 18, w: 'regular' },
  overline: { s: 12, lh: 16, w: 'bold', t: 0.6 },
  metric: { s: 32, lh: 40, w: 'bold', t: -0.6 },
  metricL: { s: 40, lh: 48, w: 'bold', t: -1 }
};

var RISK = {
  BAIXO: { bg: { r: 0.871, g: 0.957, b: 0.882 }, fg: { r: 0.067, g: 0.373, b: 0.165 } },
  MEDIO: { bg: { r: 1.0, g: 0.945, b: 0.8 }, fg: { r: 0.48, g: 0.33, b: 0.0 } },
  ALTO: { bg: { r: 0.992, g: 0.886, b: 0.886 }, fg: { r: 0.62, g: 0.11, b: 0.11 } }
};

async function t2(text, k, color, width) {
  var st = TY2[k];
  var tr = (st.t !== undefined) ? st.t : null;
  return await createTextNode(text, st.s, st.w, color, width || null, null, st.lh, tr);
}

function vbox2(name, w, gap, pad, bg, stroke, radius) {
  return createVerticalContainer(name, w, gap, pad, bg || null, stroke || null, radius || null, false);
}

function hbox2(name, w, gap, pad, bg, stroke, radius, pAlign, cAlign) {
  return createHorizontalRow(name, w, gap, pad, bg || null, stroke || null, radius || null, pAlign || 'MIN', cAlign || 'MIN');
}

function rect2(name, w, h, color, radius) {
  var r = figma.createFrame();
  r.name = name;
  r.resize(Math.max(1, w), Math.max(1, h));
  r.fills = solidFill(color);
  r.cornerRadius = radius || 0;
  r.clipsContent = false;
  return r;
}

function colWidths(total, n, gap) {
  var avail = total - gap * (n - 1);
  var base = Math.floor(avail / n);
  var arr = [];
  for (var i = 0; i < n; i++) arr.push(base);
  arr[n - 1] = arr[n - 1] + (avail - base * n);
  return arr;
}

async function pill2(text, bg, fg) {
  var f = figma.createFrame();
  f.name = 'Pill: ' + text;
  f.layoutMode = 'HORIZONTAL';
  f.primaryAxisSizingMode = 'AUTO';
  f.counterAxisSizingMode = 'AUTO';
  f.paddingLeft = 12; f.paddingRight = 12; f.paddingTop = 4; f.paddingBottom = 4;
  f.cornerRadius = 999;
  f.fills = solidFill(bg);
  f.clipsContent = false;
  f.appendChild(await t2(text.toUpperCase(), 'overline', fg));
  return f;
}

// Converte o texto bruto em blocos: parágrafos e itens "Rótulo: corpo"
function parseBlocks2(raw) {
  var out = [];
  if (!raw) return out;
  var lines = raw.split('\n');
  for (var i = 0; i < lines.length; i++) {
    var line = lines[i].trim();
    if (!line) continue;
    var isItem = /^(•|-|\d+\.)\s*/.test(line);
    if (isItem) {
      var clean = line.replace(/^(•|-|\d+\.)\s*/, '').trim();
      var ci = clean.indexOf(':');
      if (ci > 0 && ci < 48) { var bd = clean.substring(ci + 1).trim(); bd = bd.charAt(0).toUpperCase() + bd.substring(1); out.push({ type: 'item', label: clean.substring(0, ci).trim(), body: bd }); }
      else out.push({ type: 'item', label: '', body: clean });
    } else {
      out.push({ type: 'p', body: line });
    }
  }
  return out;
}

async function renderBody2(raw, w) {
  var col = vbox2('Texto', w, 24, null);
  var blocks = parseBlocks2(raw);
  var list = null;
  for (var i = 0; i < blocks.length; i++) {
    var b = blocks[i];
    if (b.type === 'p') {
      list = null;
      col.appendChild(await t2(b.body, 'body', TOKENS.colors.textSecondary, w));
    } else {
      if (!list) { list = vbox2('Lista de decisões', w, 16, null); col.appendChild(list); }
      var it = vbox2('Item: ' + (b.label || 'nota'), w, 4, null);
      if (b.label) it.appendChild(await t2(b.label, 'smallStrong', TOKENS.colors.deepPine, w));
      it.appendChild(await t2(b.body, 'small', TOKENS.colors.textPrimary, w));
      list.appendChild(it);
    }
  }
  return col;
}

async function callout2(title, raw, w) {
  var box = vbox2('Destaque: ' + title, w, 12, { left: 24, right: 24, top: 24, bottom: 24 }, TOKENS.colors.subtle, TOKENS.colors.borderSubtle, 12);
  box.appendChild(await t2(title.toUpperCase(), 'overline', TOKENS.colors.deepPine));
  var blocks = parseBlocks2(raw);
  for (var i = 0; i < blocks.length; i++) {
    var b = blocks[i];
    var it = vbox2('Ponto', w - 48, 4, null);
    if (b.label) it.appendChild(await t2(b.label, 'smallStrong', TOKENS.colors.textPrimary, w - 48));
    it.appendChild(await t2(b.body, 'small', TOKENS.colors.textSecondary, w - 48));
    box.appendChild(it);
  }
  return box;
}

// Moldura padrão dos entregáveis (largura fixa, altura HUG)
async function panel2(name, w, dark, tag, title) {
  var p = vbox2(name, w, 24, { left: 24, right: 24, top: 24, bottom: 24 },
    dark ? TOKENS.colors.darkPine : TOKENS.colors.card,
    dark ? TOKENS.colors.pineSurface : TOKENS.colors.borderSubtle, 16);
  var head = vbox2('Cabeçalho', w - 48, 8, null);
  head.appendChild(await pill2(tag, dark ? TOKENS.colors.pineSurface : TOKENS.colors.subtle, dark ? TOKENS.colors.acidLime : TOKENS.colors.deepPine));
  head.appendChild(await t2(title, 'h3', dark ? TOKENS.colors.canvas : TOKENS.colors.textPrimary, w - 48));
  p.appendChild(head);
  return p;
}

async function kvRow2(label, value, w, labelColor, valueColor, strong) {
  var r = hbox2('Linha: ' + label, w, 12, null, null, null, null, 'SPACE_BETWEEN', 'CENTER');
  var vw = 112;
  r.appendChild(await t2(label, 'small', labelColor, w - vw - 12));
  var v = await t2(value, strong ? 'smallStrong' : 'small', valueColor, vw);
  v.textAlignHorizontal = 'RIGHT';
  r.appendChild(v);
  return r;
}

async function kvStack2(label, value, w, labelColor, valueColor) {
  var b = vbox2('Dado: ' + label, w, 0, null);
  b.appendChild(await t2(label, 'caption', labelColor, w));
  b.appendChild(await t2(value, 'smallStrong', valueColor, w));
  return b;
}

// ---------------------------------------------------------------------------
// ENTREGÁVEIS SALARYNOW V2
// ---------------------------------------------------------------------------
async function snHeroSimulator(w) {
  var p = await panel2('Entregável: Simulador de antecipação', w, true, 'Tela de confirmação · redesenho', 'Antecipação de salário');
  var inner = w - 48;
  var amount = vbox2('Valor recebido', inner, 4, null);
  amount.appendChild(await t2('VOCÊ RECEBE HOJE NO PIX', 'overline', TOKENS.colors.subtle));
  amount.appendChild(await t2('R$ 300,00', 'metricL', TOKENS.colors.acidLime));
  p.appendChild(amount);

  var cw = colWidths(inner, 2, 12);
  var row = hbox2('Custos (região comum)', inner, 12, null);
  var a = vbox2('Taxa', cw[0], 4, { left: 16, right: 16, top: 16, bottom: 16 }, TOKENS.colors.pineSurface, null, 12);
  a.appendChild(await t2('Taxa única', 'caption', TOKENS.colors.subtle, cw[0] - 32));
  a.appendChild(await t2('R$ 12,00', 'h3', TOKENS.colors.canvas, cw[0] - 32));
  var b = vbox2('Desconto', cw[1], 4, { left: 16, right: 16, top: 16, bottom: 16 }, TOKENS.colors.pineSurface, null, 12);
  b.appendChild(await t2('Desconto no salário', 'caption', TOKENS.colors.subtle, cw[1] - 32));
  b.appendChild(await t2('R$ 312,00', 'h3', TOKENS.colors.canvas, cw[1] - 32));
  row.appendChild(a); row.appendChild(b);
  p.appendChild(row);

  p.appendChild(await kvRow2('Salário previsto após o desconto', 'R$ 2.688,00', inner, TOKENS.colors.subtle, TOKENS.colors.acidLime, true));
  var btn = hbox2('Botão confirmar', inner, 0, { left: 16, right: 16, top: 12, bottom: 12 }, TOKENS.colors.acidLime, null, 999, 'CENTER', 'CENTER');
  btn.appendChild(await t2('Confirmar antecipação', 'smallStrong', TOKENS.colors.deepPine));
  p.appendChild(btn);
  return p;
}

async function snFunnel(w) {
  var p = await panel2('Entregável: Funil de ativação', w, false, 'Dados de uso · linha de base', 'Onde os colaboradores desistiam');
  var inner = w - 48;
  var labelW = 196, valW = 56, gap = 12;
  var trackW = inner - labelW - valW - gap * 2;
  var rows = [
    { l: 'Cadastrados', v: 100, t: '100%', c: TOKENS.colors.deepPine },
    { l: 'Concluíram a 1ª antecipação', v: 32, t: '32%', c: TOKENS.colors.pineSurface },
    { l: 'Repetiram no mês seguinte (base: quem usou)', v: 74, t: '74%', c: TOKENS.colors.pineSurface }
  ];
  var list = vbox2('Barras', inner, 16, null);
  for (var i = 0; i < rows.length; i++) {
    var r = hbox2('Etapa ' + (i + 1), inner, gap, null, null, null, null, 'MIN', 'CENTER');
    r.appendChild(await t2(rows[i].l, 'small', TOKENS.colors.textPrimary, labelW));
    var track = hbox2('Trilho', trackW, 0, null, TOKENS.colors.subtle, null, 6, 'MIN', 'MIN');
    track.appendChild(rect2('Barra ' + rows[i].t, Math.round(trackW * rows[i].v / 100), 24, rows[i].c, 6));
    r.appendChild(track);
    var v = await t2(rows[i].t, 'smallStrong', TOKENS.colors.textPrimary, valW);
    v.textAlignHorizontal = 'RIGHT';
    r.appendChild(v);
    list.appendChild(r);
  }
  p.appendChild(list);
  var alert = vbox2('Ponto de abandono', inner, 4, { left: 16, right: 16, top: 16, bottom: 16 }, RISK.ALTO.bg, null, 12);
  alert.appendChild(await t2('68% nunca concluíam a primeira operação', 'smallStrong', RISK.ALTO.fg, inner - 32));
  alert.appendChild(await t2('A maior perda acontecia entre a tela de saldo e a tela de confirmação, onde a taxa aparecia em percentual.', 'small', TOKENS.colors.textPrimary, inner - 32));
  p.appendChild(alert);
  return p;
}

async function snRiskMatrix(w) {
  var p = await panel2('Entregável: Matriz de riscos', w, false, '4 riscos de produto · Marty Cagan', 'Comparação dos três produtos');
  var inner = w - 48;
  var nameW = 148, gap = 8;
  var cellW = Math.floor((inner - nameW - gap * 4) / 4);
  nameW = inner - cellW * 4 - gap * 4;
  var head = hbox2('Cabeçalho da tabela', inner, gap, null, null, null, null, 'MIN', 'CENTER');
  head.appendChild(await t2('Produto', 'caption', TOKENS.colors.textSecondary, nameW));
  var hs = ['Valor', 'Usabilidade', 'Viabilidade', 'Negócio'];
  for (var h = 0; h < hs.length; h++) {
    var ht = await t2(hs[h], 'caption', TOKENS.colors.textSecondary, cellW);
    ht.textAlignHorizontal = 'CENTER';
    head.appendChild(ht);
  }
  var data = [
    { n: 'Antecipação salarial', r: ['BAIXO', 'ALTO', 'BAIXO', 'BAIXO'], focus: true },
    { n: 'Cartão de benefícios', r: ['ALTO', 'ALTO', 'ALTO', 'ALTO'] },
    { n: 'Portal do RH', r: ['MEDIO', 'ALTO', 'BAIXO', 'MEDIO'] }
  ];
  var labels = { BAIXO: 'Baixo', MEDIO: 'Médio', ALTO: 'Alto' };
  var table = vbox2('Tabela de riscos', inner, 0, null);
  table.appendChild(head);
  for (var i = 0; i < data.length; i++) {
    var row = hbox2('Linha: ' + data[i].n, inner, gap, { left: 0, right: 0, top: 8, bottom: 8 }, null, null, null, 'MIN', 'CENTER');
    row.appendChild(await t2(data[i].n, data[i].focus ? 'smallStrong' : 'small', TOKENS.colors.textPrimary, nameW));
    for (var c = 0; c < 4; c++) {
      var lv = RISK[data[i].r[c]];
      var cell = hbox2('Risco', cellW, 0, { left: 0, right: 0, top: 4, bottom: 4 }, lv.bg, null, 6, 'CENTER', 'CENTER');
      cell.appendChild(await t2(labels[data[i].r[c]], 'caption', lv.fg));
      row.appendChild(cell);
    }
    table.appendChild(row);
  }
  p.appendChild(table);
  var dec = vbox2('Decisão', inner, 4, { left: 16, right: 16, top: 16, bottom: 16 }, TOKENS.colors.limeTint, null, 12);
  dec.appendChild(await t2('Decisão: foco na Antecipação salarial', 'smallStrong', TOKENS.colors.deepPine, inner - 32));
  dec.appendChild(await t2('Único produto com valor comprovado e um problema concentrado em usabilidade, que o time consegue resolver.', 'small', TOKENS.colors.textPrimary, inner - 32));
  p.appendChild(dec);
  return p;
}

async function snBeforeAfter(w) {
  var p = await panel2('Entregável: Antes e depois da confirmação', w, false, 'Tela de confirmação', 'Como a taxa era mostrada');
  var inner = w - 48;
  var cw = colWidths(inner, 2, 12);
  var row = hbox2('Comparação', inner, 12, null);
  var before = vbox2('Antes', cw[0], 12, { left: 16, right: 16, top: 16, bottom: 16 }, TOKENS.colors.card, TOKENS.colors.borderMedium, 12);
  before.appendChild(await pill2('Antes', RISK.ALTO.bg, RISK.ALTO.fg));
  before.appendChild(await kvStack2('Valor', 'R$ 300,00', cw[0] - 32, TOKENS.colors.textSecondary, TOKENS.colors.textPrimary));
  before.appendChild(await kvStack2('Taxa', 'Percentual ao mês + IOF', cw[0] - 32, TOKENS.colors.textSecondary, TOKENS.colors.textPrimary));
  before.appendChild(await t2('O colaborador precisava calcular o custo e não via o efeito no salário.', 'caption', TOKENS.colors.textSecondary, cw[0] - 32));
  var after = vbox2('Depois', cw[1], 12, { left: 16, right: 16, top: 16, bottom: 16 }, TOKENS.colors.limeTint, TOKENS.colors.deepPine, 12);
  after.appendChild(await pill2('Depois', TOKENS.colors.deepPine, TOKENS.colors.acidLime));
  after.appendChild(await kvStack2('Você recebe', 'R$ 300,00', cw[1] - 32, TOKENS.colors.textSecondary, TOKENS.colors.textPrimary));
  after.appendChild(await kvStack2('Taxa única', 'R$ 12,00', cw[1] - 32, TOKENS.colors.textSecondary, TOKENS.colors.textPrimary));
  after.appendChild(await kvStack2('Salário previsto', 'R$ 2.688,00', cw[1] - 32, TOKENS.colors.textSecondary, TOKENS.colors.deepPine));
  row.appendChild(before); row.appendChild(after);
  p.appendChild(row);
  p.appendChild(await t2('Região comum: o que entra hoje e o que sai no próximo salário ficam em blocos separados. Proximidade: a taxa em reais fica ao lado do valor pedido.', 'caption', TOKENS.colors.textSecondary, inner));
  return p;
}

async function snScopeBoard(w) {
  var p = await panel2('Entregável: Escopo', w, false, 'Disciplina de escopo', 'O que entrou e o que ficou fora');
  var inner = w - 48;
  var cw = colWidths(inner, 2, 12);
  var row = hbox2('Colunas de escopo', inner, 12, null);
  var inC = vbox2('Entrou', cw[0], 12, { left: 16, right: 16, top: 16, bottom: 16 }, TOKENS.colors.limeTint, null, 12);
  inC.appendChild(await pill2('Entrou', TOKENS.colors.deepPine, TOKENS.colors.acidLime));
  var ins = ['Tela de confirmação com custo em reais', 'Prévia do próximo salário', 'Painel do RH com dados agregados e anônimos'];
  for (var i = 0; i < ins.length; i++) inC.appendChild(await t2('• ' + ins[i], 'small', TOKENS.colors.textPrimary, cw[0] - 32));
  var outC = vbox2('Ficou fora', cw[1], 12, { left: 16, right: 16, top: 16, bottom: 16 }, TOKENS.colors.subtle, null, 12);
  outC.appendChild(await pill2('Ficou fora', RISK.ALTO.bg, RISK.ALTO.fg));
  var outs = [['Novas funções do cartão', 'dividiria os 6 devs'], ['Crédito rotativo', 'risco regulatório'], ['Cashback e gamificação', 'não resolve a confiança na taxa']];
  for (var j = 0; j < outs.length; j++) {
    var it = vbox2('Item fora', cw[1] - 32, 4, null);
    it.appendChild(await t2(outs[j][0], 'smallStrong', TOKENS.colors.textPrimary, cw[1] - 32));
    it.appendChild(await t2(outs[j][1], 'caption', TOKENS.colors.textSecondary, cw[1] - 32));
    outC.appendChild(it);
  }
  row.appendChild(inC); row.appendChild(outC);
  p.appendChild(row);
  return p;
}

async function snResults(w) {
  var p = await panel2('Entregável: Resultados', w, true, 'Resultados após 8 meses', 'Indicadores antes e depois');
  var inner = w - 48;
  var vW = 88, gap = 12;
  var nW = inner - vW * 2 - gap * 2;
  var head = hbox2('Cabeçalho', inner, gap, null, null, null, null, 'MIN', 'CENTER');
  head.appendChild(await t2('Indicador', 'caption', TOKENS.colors.subtle, nW));
  var h1 = await t2('Antes', 'caption', TOKENS.colors.subtle, vW); h1.textAlignHorizontal = 'RIGHT'; head.appendChild(h1);
  var h2 = await t2('Depois', 'caption', TOKENS.colors.subtle, vW); h2.textAlignHorizontal = 'RIGHT'; head.appendChild(h2);
  var table = vbox2('Tabela de resultados', inner, 0, null);
  table.appendChild(head);
  var rows = [
    ['Ativação dos cadastrados', '32%', '59%'],
    ['Abandono na confirmação', '68%', '19%'],
    ['Uso repetido no mês seguinte', '74%', '78%'],
    ['Antecipações por usuário ativo/mês', '1,8', '2,3'],
    ['Chamados sobre taxas (índice)', '100', '37']
  ];
  for (var i = 0; i < rows.length; i++) {
    var r = hbox2('Linha: ' + rows[i][0], inner, gap, { left: 0, right: 0, top: 12, bottom: 12 }, null, null, null, 'MIN', 'CENTER');
    r.appendChild(await t2(rows[i][0], 'small', TOKENS.colors.canvas, nW));
    var a = await t2(rows[i][1], 'small', TOKENS.colors.subtle, vW); a.textAlignHorizontal = 'RIGHT'; r.appendChild(a);
    var b = await t2(rows[i][2], 'smallStrong', TOKENS.colors.acidLime, vW); b.textAlignHorizontal = 'RIGHT'; r.appendChild(b);
    table.appendChild(rect2('Divisor', inner, 1, TOKENS.colors.pineSurface, 0));
    table.appendChild(r);
  }
  p.appendChild(table);
  return p;
}

// ---------------------------------------------------------------------------
// PÁGINA DE CASE V2
// ---------------------------------------------------------------------------
async function figure2(ch, w) {
  var col = vbox2('Figura ' + ch.num, w, 12, null);
  if (typeof ch.figure === 'function') col.appendChild(await ch.figure(w));
  else col.appendChild(await createRealImageFigure(ch.imgKey, null, w, Math.round(w * 9 / 16), 12));
  if (ch.caption) col.appendChild(await t2(ch.caption, 'caption', TOKENS.colors.textSecondary, w));
  return col;
}

async function chapter2(ch, idx) {
  var sec = vbox2('Capítulo ' + ch.num, GRID.content, 32, null);
  sec.appendChild(rect2('Divisor', GRID.content, 1, TOKENS.colors.borderSubtle, 0));
  var head = vbox2('Título do capítulo', span(8), 12, null);
  head.appendChild(await t2((ch.num + ' · ' + ch.tag).toUpperCase(), 'overline', TOKENS.colors.deepPine, span(8)));
  head.appendChild(await t2(ch.title, 'h2', TOKENS.colors.textPrimary, span(8)));
  sec.appendChild(head);

  var body = hbox2('Corpo (2 colunas)', GRID.content, GRID.gutter, null);
  var textCol = vbox2('Coluna de texto', span(6), 32, null);
  textCol.appendChild(await renderBody2(ch.p, span(6)));
  if (ch.impactText) textCol.appendChild(await callout2(ch.calloutTitle || 'Pontos-chave', ch.impactText, span(6)));
  var figCol = await figure2(ch, span(6));
  if (idx % 2 === 1) { body.appendChild(figCol); body.appendChild(textCol); }
  else { body.appendChild(textCol); body.appendChild(figCol); }
  sec.appendChild(body);
  return sec;
}

async function buildCaseV2(parent, xPos, yPos, d) {
  log('Criando ' + d.name + ' (layout V2: grid 12 col, base 8px)...');
  for (var k = parent.children.length - 1; k >= 0; k--) {
    if (parent.children[k].name === d.frameName) parent.children[k].remove();
  }
  var root = vbox2(d.frameName, GRID.page, 64, { left: GRID.margin, right: GRID.margin, top: 32, bottom: 96 }, TOKENS.colors.canvas);
  root.x = xPos; root.y = yPos;
  root.clipsContent = true;

  // Topo: header + hero
  var top = vbox2('Topo', GRID.content, 48, null);
  top.appendChild(await createHeaderBar(GRID.content));
  var hero = hbox2('Hero', GRID.content, GRID.gutter, null, null, null, null, 'MIN', 'CENTER');
  var hl = vbox2('Hero · texto', span(7), 32, null);
  hl.appendChild(await t2('← Voltar aos cases', 'small', TOKENS.colors.textSecondary));
  var intro = vbox2('Título', span(7), 16, null);
  intro.appendChild(await pill2(d.kickerTag, TOKENS.colors.acidLime, TOKENS.colors.deepPine));
  intro.appendChild(await t2(d.title, 'display', TOKENS.colors.textPrimary, span(7)));
  intro.appendChild(await t2(d.subtitle, 'bodyL', TOKENS.colors.textSecondary, span(6)));
  hl.appendChild(intro);
  var metaWrap = vbox2('Metadados', span(7), 16, null);
  metaWrap.appendChild(rect2('Divisor', span(7), 1, TOKENS.colors.borderSubtle, 0));
  var mw = colWidths(span(7), d.metadata.length, GRID.gutter);
  var meta = hbox2('Metadados · colunas', span(7), GRID.gutter, null);
  for (var m = 0; m < d.metadata.length; m++) {
    var mc = vbox2('Meta: ' + d.metadata[m].label, mw[m], 4, null);
    mc.appendChild(await t2(d.metadata[m].label.toUpperCase(), 'overline', TOKENS.colors.textSecondary, mw[m]));
    mc.appendChild(await t2(d.metadata[m].val, 'smallStrong', TOKENS.colors.textPrimary, mw[m]));
    meta.appendChild(mc);
  }
  metaWrap.appendChild(meta);
  hl.appendChild(metaWrap);
  hero.appendChild(hl);
  var hr = vbox2('Hero · entregável', span(5), 12, null);
  if (typeof d.heroFigure === 'function') hr.appendChild(await d.heroFigure(span(5)));
  else hr.appendChild(await createRealImageFigure(d.heroImgKey, null, span(5), Math.round(span(5) * 9 / 16), 12));
  if (d.heroCaption) hr.appendChild(await t2(d.heroCaption, 'caption', TOKENS.colors.textSecondary, span(5)));
  hero.appendChild(hr);
  top.appendChild(hero);
  root.appendChild(top);

  // Métricas: uma faixa, colunas iguais
  if (d.metrics && d.metrics.length) {
    var strip = hbox2('Métricas', GRID.content, GRID.gutter, { left: 32, right: 32, top: 24, bottom: 24 }, TOKENS.colors.card, TOKENS.colors.borderSubtle, 16);
    var cws = colWidths(GRID.content - 64, d.metrics.length, GRID.gutter);
    for (var i = 0; i < d.metrics.length; i++) {
      var mcol = vbox2('Métrica ' + (i + 1), cws[i], 4, null);
      mcol.appendChild(await t2(d.metrics[i].n, 'metric', TOKENS.colors.deepPine, cws[i]));
      mcol.appendChild(await t2(d.metrics[i].d, 'small', TOKENS.colors.textSecondary, cws[i]));
      strip.appendChild(mcol);
    }
    root.appendChild(strip);
  }

  for (var c = 0; c < d.chapters.length; c++) {
    root.appendChild(await chapter2(d.chapters[c], c));
  }

  // Navegação entre cases
  var nav = hbox2('Navegação entre cases', GRID.content, GRID.gutter, null);
  var nw = colWidths(GRID.content, 2, GRID.gutter);
  var pv = vbox2('Case anterior', nw[0], 4, { left: 24, right: 24, top: 24, bottom: 24 }, TOKENS.colors.card, TOKENS.colors.borderSubtle, 12);
  pv.appendChild(await t2('← CASE ANTERIOR', 'overline', TOKENS.colors.textSecondary));
  pv.appendChild(await t2(d.prevCaseTitle, 'h3', TOKENS.colors.textPrimary, nw[0] - 48));
  var nx = vbox2('Próximo case', nw[1], 4, { left: 24, right: 24, top: 24, bottom: 24 }, TOKENS.colors.deepPine, null, 12);
  nx.appendChild(await t2('PRÓXIMO CASE →', 'overline', TOKENS.colors.acidLime));
  nx.appendChild(await t2(d.nextCaseTitle, 'h3', TOKENS.colors.canvas, nw[1] - 48));
  nav.appendChild(pv); nav.appendChild(nx);
  root.appendChild(nav);

  parent.appendChild(root);
  log('✔ ' + d.name + ' criado (layout V2).');
  return root;
}

