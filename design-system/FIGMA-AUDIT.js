// Executar no use_figma, com skillNames: figma-use.
// Somente leitura. Miniaturas de produtos não devem ser confundidas com narrativa.
const rootIds = ['370:16614', '370:17047', '375:366', '375:892'];
const paletteNode = await figma.getNodeByIdAsync('304:4060');
const palette = new Set(paletteNode.findAll(n => n.type === 'TEXT')
  .flatMap(n => n.characters.match(/#[0-9a-fA-F]{6}/g) || []).map(s => s.toUpperCase()));
const hex = c => '#' + [c.r, c.g, c.b].map(v => Math.round(v * 255).toString(16).padStart(2, '0')).join('').toUpperCase();
function isProductEvidence(n) {
  for (let p = n; p; p = p.parent) {
    if (/Mockup|Visão geral.*interface|Detalhe.*ampliado/i.test(p.name)) return true;
  }
  return false;
}
function rendered(n) {
  for (let p = n; p; p = p.parent) if ('visible' in p && !p.visible) return false;
  return true;
}
const report = [];
for (const id of rootIds) {
  const root = await figma.getNodeByIdAsync(id);
  const result = {id, name: root.name, overflows: [], paletteExceptions: [], unboundNarrative: [], smallNarrative: [], evidenceTextCount: 0};
  for (const n of [root, ...root.findAll(() => true)]) {
    if (!rendered(n)) continue;
    const evidence = isProductEvidence(n);
    if (n.type === 'TEXT') {
      if (evidence) result.evidenceTextCount++;
      else {
        if (!n.textStyleId) result.unboundNarrative.push(n.id);
        if (typeof n.fontSize === 'number' && n.fontSize < 12) result.smallNarrative.push(n.id);
      }
    }
    if (!evidence) for (const prop of ['fills', 'strokes']) {
      const paints = Array.isArray(n[prop]) ? n[prop] : n.type === 'TEXT' && prop === 'fills'
        ? n.getStyledTextSegments(['fills']).flatMap(s => s.fills) : [];
      for (const paint of paints) if (paint.type === 'SOLID' && !palette.has(hex(paint.color)))
        result.paletteExceptions.push({id: n.id, prop, color: hex(paint.color)});
    }
    if ('children' in n && n.layoutMode !== 'NONE') for (const c of n.children) {
      if (!rendered(c) || c.layoutPositioning === 'ABSOLUTE' || !['FRAME', 'TEXT', 'INSTANCE'].includes(c.type)) continue;
      if (c.x < -2 || c.y < -2 || c.x + c.width > n.width + 2 || c.y + c.height > n.height + 2)
        result.overflows.push({parent: n.id, child: c.id, evidence: isProductEvidence(c)});
    }
  }
  report.push(result);
}
return report;
