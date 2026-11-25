import io, base64, os
from pathlib import Path
from PIL import Image

plugin_dir = Path(r"C:\Users\Israel Rozar\figma-refine-plugin")

images_map = {
    # Home
    'home_portrait': 'site/public/images/israel-rozar-portrait-800.webp',
    'hiae_tablet': 'site/public/images/hiae-proposta-v3-tablet-1600.webp',
    'itau_hub_thumb': 'site/public/images/itau-hub-liquidez-capa-1600.webp',
    'itau_venc_thumb': 'site/public/images/itau-vencimentos-capa-1600.webp',
    'neo_capa_thumb': 'site/public/images/neoenergia-capa-conexao-digital.webp',
    'claro_ativ_thumb': 'site/public/images/claro-ativacao-hero.webp',
    # Neoenergia
    'neo_capa': 'site/public/images/neoenergia-capa-conexao-digital.webp',
    'neo_num': 'site/public/images/neoenergia-grandes-numeros.webp',
    'neo_canais': 'site/public/images/neoenergia-canais-atendimento.webp',
    'neo_bp1': 'site/public/images/neoenergia-blueprint-1-contrato-instalo.webp',
    'neo_ds': 'site/public/images/neoenergia-entregaveis-ui-design-system.webp',
    'neo_tobe': 'site/public/images/neoenergia-jornada-futuro-tobe.webp',
    'neo_matriz': 'site/public/images/neoenergia-matriz-118-ideias.webp',
    # Albert Einstein
    'hiae_capa': 'site/public/images/hiae-capa-editorial-1600.webp',
    'hiae_taxonomia': 'site/public/images/hiae-taxonomia-macroareas.webp',
    'hiae_triangulacao': 'site/public/images/hiae-triangulacao-pesquisa-1200.webp',
    'hiae_tokens': 'site/public/images/hiae-ds-tokens-clean-1280.webp',
    'hiae_componentes': 'site/public/images/hiae-ds-componentes-crop-1600.webp',
    'hiae_visao_futura': 'site/public/images/hiae-visao-futura-ressonancia.webp',
    # Itaú Unibanco
    'itau_hub': 'site/public/images/itau-hub-liquidez-capa-1600.webp',
    'itau_vencimentos': 'site/public/images/itau-vencimentos-capa-1600.webp',
    'itau_movimentacoes': 'site/public/images/itau-movimentacoes-capa-1600.webp',
    'itau_campanhas': 'site/public/images/itau-campanhas-capa-1600.webp',
    'itau_registros': 'site/public/images/itau-registros-workflow-1600.webp',
    # Claro Brasil
    'claro_capa': 'site/public/images/claro-capa-editorial-1600.webp',
    'claro_ativacao': 'site/public/images/claro-ativacao-hero.webp',
    'claro_jornadas': 'site/public/images/claro-jornadas.webp',
    'claro_multicanal': 'site/public/images/claro-multicanal.webp',
    'claro_busca': 'site/public/images/claro-busca-cliente.webp',
    'claro_detalhe': 'site/public/images/claro-detalhe-linha.webp',
    'claro_confirmacao': 'site/public/images/claro-confirmacao-mobile.webp',
    'claro_workshop': 'site/public/images/claro-workshop.webp'
}

b64_dict = {}
for k, path in images_map.items():
    if os.path.exists(path):
        im = Image.open(path)
        rgb = im.convert('RGB')
        buf = io.BytesIO()
        w, h = rgb.size
        max_dim = 1080 if 'capa' in k or 'bp' in k or 'tablet' in k else 800
        if w > max_dim:
            rgb = rgb.resize((max_dim, int(h * max_dim / w)), Image.LANCZOS)
        rgb.save(buf, format='JPEG', quality=78)
        b64 = base64.b64encode(buf.getvalue()).decode('ascii')
        b64_dict[k] = b64
    else:
        b64_dict[k] = ""

print(f"Loaded {len(b64_dict)} real image deliverables in Base64.")

js_images_decl = "var REAL_IMAGES = {\n"
for k, val in b64_dict.items():
    js_images_decl += f'  "{k}": "{val}",\n'
js_images_decl += "};\n"

js_core = r"""// ============================================================================
// PORTFOLIO MASTER DESIGN SYSTEM · SENIOR CRAFT 1:1 REAL IMAGES & AUTO-LAYOUT
// Zero-Clips, True Proportions, Real Image Deliverables, No Wireframe Redundancy
// Standard: Classical ES5/ES6 (Zero spread `...`, Zero optional chaining `?.`)
// ============================================================================

figma.showUI(__html__, { width: 580, height: 740, themeColors: true });

function log(msg) {
  figma.ui.postMessage({ type: 'log', message: msg });
  console.log('[Portfolio Generator] ' + msg);
}

function updateStatus(status) {
  figma.ui.postMessage({ type: 'status', message: status });
}

// ----------------------------------------------------------------------------
// Tokens Canônicos de Design (Guia de Estilos v1 do Arquivo Oficial 333:2)
// ----------------------------------------------------------------------------
var TOKENS = {
  colors: {
    canvas: { r: 0.9882, g: 0.9765, b: 0.9490 },         // #FCF9F2
    subtle: { r: 0.9647, g: 0.9529, b: 0.9255 },         // #F6F3EC
    card: { r: 1.0, g: 1.0, b: 1.0 },                   // #FFFFFF
    borderSubtle: { r: 0.9294, g: 0.9137, b: 0.8706 },   // #EDE9DE
    borderMedium: { r: 0.824, g: 0.831, b: 0.792 },     // #D2D4CA
    textPrimary: { r: 0.1020, g: 0.1255, b: 0.1098 },    // #1A201C
    textSecondary: { r: 0.2902, g: 0.3333, b: 0.3059 },  // #4A554E
    textMuted: { r: 0.4902, g: 0.5412, b: 0.5098 },      // #7D8A82
    deepPine: { r: 0.0392, g: 0.2118, b: 0.1333 },       // #0A3622
    darkPine: { r: 0.0235, g: 0.1333, b: 0.0824 },       // #062215
    pineSurface: { r: 0.0667, g: 0.2941, b: 0.1922 },    // #114B31
    acidLime: { r: 0.8078, g: 1.0, b: 0.1020 },          // #CEFF1A
    limeHover: { r: 0.7451, g: 0.9412, b: 0.0549 },      // #BEF00E
    limeTint: { r: 0.9569, g: 1.0, b: 0.8000 }           // #F4FFCC
  },
  radius: {
    badge: 4,
    chip: 6,
    panel: 12,
    card: 16,
    feature: 24,
    pill: 9999
  }
};

// Decodificador Base64 Seguro
function base64ToUint8Array(base64) {
  if (typeof figma.base64Decode === 'function') {
    return figma.base64Decode(base64);
  }
  var chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";
  var lookup = new Uint8Array(256);
  for (var i = 0; i < chars.length; i++) lookup[chars.charCodeAt(i)] = i;
  var len = base64.length;
  var placeHolders = (base64[len - 1] === '=') ? ((base64[len - 2] === '=') ? 2 : 1) : 0;
  var bytes = new Uint8Array((len * 3 / 4) - placeHolders);
  var curByte = 0;
  for (var i = 0; i < len; i += 4) {
    var c1 = lookup[base64.charCodeAt(i)];
    var c2 = lookup[base64.charCodeAt(i + 1)];
    var c3 = lookup[base64.charCodeAt(i + 2)];
    var c4 = lookup[base64.charCodeAt(i + 3)];
    bytes[curByte++] = (c1 << 2) | (c2 >> 4);
    if (curByte < bytes.length) bytes[curByte++] = ((c2 & 15) << 4) | (c3 >> 2);
    if (curByte < bytes.length) bytes[curByte++] = ((c3 & 3) << 6) | c4;
  }
  return bytes;
}

// Carregamento Seguro de Tipografia
var loadedFonts = {};
async function loadFontSafe(family, style) {
  var key = family + '_' + style;
  if (loadedFonts[key]) return loadedFonts[key];
  
  var candidates = [
    { family: family, style: style },
    { family: 'Plus Jakarta Sans', style: style },
    { family: 'Plus Jakarta Sans', style: 'Regular' },
    { family: 'Inter', style: style },
    { family: 'Inter', style: 'Regular' }
  ];

  for (var i = 0; i < candidates.length; i++) {
    try {
      await figma.loadFontAsync(candidates[i]);
      loadedFonts[key] = candidates[i];
      return candidates[i];
    } catch (e) {}
  }
  return { family: 'Inter', style: 'Regular' };
}

function solidFill(rgb, opacity) {
  return [{
    type: 'SOLID',
    color: rgb,
    opacity: (opacity !== undefined && opacity !== null) ? opacity : 1
  }];
}

function softElevation() {
  return [{
    type: 'DROP_SHADOW',
    color: { r: 0.0392, g: 0.2118, b: 0.1333, a: 0.05 },
    offset: { x: 0, y: 8 },
    radius: 24,
    spread: 0,
    visible: true,
    blendMode: 'NORMAL'
  }];
}

function safeSetPrimaryAlign(frame, align) {
  try {
    if (align === 'SPACE_BETWEEN') {
      if (frame.primaryAxisSizingMode === 'FIXED') {
        frame.primaryAxisAlignItems = 'SPACE_BETWEEN';
      } else {
        frame.primaryAxisAlignItems = 'MIN';
      }
    } else if (align === 'CENTER') {
      frame.primaryAxisAlignItems = 'CENTER';
    } else if (align === 'MAX') {
      frame.primaryAxisAlignItems = 'MAX';
    } else {
      frame.primaryAxisAlignItems = 'MIN';
    }
  } catch(e) {
    try { frame.primaryAxisAlignItems = 'MIN'; } catch(e2) {}
  }
}


function safeSetFill(node, axis) {
  if (!node) return;
  try {
    if (!node.parent || node.parent.layoutMode === 'NONE') return;
    if (axis === 'VERTICAL' || axis === 'BOTH') {
      if ('layoutSizingVertical' in node) node.layoutSizingVertical = 'FILL';
      if ('layoutAlign' in node) node.layoutAlign = 'STRETCH';
    }
    if (axis === 'HORIZONTAL' || axis === 'BOTH') {
      if ('layoutSizingHorizontal' in node) node.layoutSizingHorizontal = 'FILL';
      if ('layoutAlign' in node) node.layoutAlign = 'STRETCH';
    }
  } catch(e) {}
}

function safeSetCounterAlign(frame, align) {
  try {
    if (align === 'CENTER') {
      frame.counterAxisAlignItems = 'CENTER';
    } else if (align === 'MAX' || align === 'BOTTOM') {
      frame.counterAxisAlignItems = 'MAX';
    } else if (align === 'BASELINE') {
      frame.counterAxisAlignItems = 'BASELINE';
    } else {
      frame.counterAxisAlignItems = 'MIN';
    }
  } catch(e) {
    try { frame.counterAxisAlignItems = 'MIN'; } catch(e2) {}
  }
}

// ----------------------------------------------------------------------------
// MESTRES DE AUTOLAYOUT (HUG CONTENTS GARANTIDO & ZERO CLIP)
// ----------------------------------------------------------------------------
function createVerticalContainer(name, fixedWidth, itemSpacing, padding, bgRgb, borderRgb, radius, withShadow) {
  var frame = figma.createFrame();
  frame.name = name;
  frame.resize(fixedWidth, 10);
  frame.layoutMode = 'VERTICAL';
  frame.counterAxisSizingMode = 'FIXED';
  frame.primaryAxisSizingMode = 'AUTO';
  frame.clipsContent = false;
  try {
    if ('layoutSizingHorizontal' in frame) frame.layoutSizingHorizontal = 'FIXED';
    if ('layoutSizingVertical' in frame) frame.layoutSizingVertical = 'HUG';
  } catch(e) {}
  frame.itemSpacing = (itemSpacing !== undefined && itemSpacing !== null) ? itemSpacing : 0;
  
  if (padding) {
    if (typeof padding === 'number') {
      frame.paddingLeft = padding;
      frame.paddingRight = padding;
      frame.paddingTop = padding;
      frame.paddingBottom = padding;
    } else {
      frame.paddingLeft = padding.left || 0;
      frame.paddingRight = padding.right || 0;
      frame.paddingTop = padding.top || 0;
      frame.paddingBottom = padding.bottom || 0;
    }
  }
  
  if (bgRgb) {
    frame.fills = solidFill(bgRgb);
  } else {
    frame.fills = [];
  }
  
  if (borderRgb) {
    frame.strokes = [{ type: 'SOLID', color: borderRgb }];
    frame.strokeWeight = 1;
  }
  
  if (radius) {
    frame.cornerRadius = radius;
  }

  if (withShadow) {
    frame.effects = softElevation();
  }
  return frame;
}

function createHorizontalRow(name, fixedWidth, itemSpacing, padding, bgRgb, borderRgb, radius, primaryAlign, counterAlign) {
  var frame = figma.createFrame();
  frame.name = name;
  frame.resize(fixedWidth, 10);
  frame.layoutMode = 'HORIZONTAL';
  frame.primaryAxisSizingMode = 'FIXED';
  frame.counterAxisSizingMode = 'AUTO';
  frame.clipsContent = false;
  frame.itemSpacing = (itemSpacing !== undefined && itemSpacing !== null) ? itemSpacing : 0;
  
  safeSetPrimaryAlign(frame, primaryAlign);
  safeSetCounterAlign(frame, counterAlign);
  try {
    if ('layoutSizingHorizontal' in frame) frame.layoutSizingHorizontal = 'FIXED';
    if ('layoutSizingVertical' in frame) frame.layoutSizingVertical = 'HUG';
  } catch(e) {}
  
  if (padding) {
    if (typeof padding === 'number') {
      frame.paddingLeft = padding;
      frame.paddingRight = padding;
      frame.paddingTop = padding;
      frame.paddingBottom = padding;
    } else {
      frame.paddingLeft = padding.left || 0;
      frame.paddingRight = padding.right || 0;
      frame.paddingTop = padding.top || 0;
      frame.paddingBottom = padding.bottom || 0;
    }
  }
  
  if (bgRgb) {
    frame.fills = solidFill(bgRgb);
  } else {
    frame.fills = [];
  }
  
  if (borderRgb) {
    frame.strokes = [{ type: 'SOLID', color: borderRgb }];
    frame.strokeWeight = 1;
  }
  
  if (radius) {
    frame.cornerRadius = radius;
  }
  return frame;
}

// Criação Segura de Textos
async function createTextNode(text, size, weight, colorRgb, fixedWidth, align, lineHeightPx, trackingPx) {
  var node = figma.createText();
  var style = (weight === 'bold' || weight === '700') ? 'Bold' :
              (weight === 'semibold' || weight === '600') ? 'SemiBold' :
              (weight === 'medium' || weight === '500') ? 'Medium' : 'Regular';
  
  var font = await loadFontSafe('Plus Jakarta Sans', style);
  node.fontName = font;
  node.fontSize = size;
  node.characters = text;
  node.fills = solidFill(colorRgb);

  if (lineHeightPx && lineHeightPx > 0) {
    node.lineHeight = { value: lineHeightPx, unit: 'PIXELS' };
  }

  if (trackingPx !== undefined && trackingPx !== null) {
    node.letterSpacing = { value: trackingPx, unit: 'PIXELS' };
  }

  if (fixedWidth && fixedWidth > 0) {
    try { node.resize(fixedWidth, 20); } catch(e) {}
    node.textAutoResize = 'HEIGHT';
  } else {
    node.textAutoResize = 'WIDTH_AND_HEIGHT';
    try {
      if ('layoutSizingHorizontal' in node) node.layoutSizingHorizontal = 'HUG';
      if ('layoutSizingVertical' in node) node.layoutSizingVertical = 'HUG';
    } catch(e) {}
  }

  if (align) {
    node.textAlignHorizontal = (align === 'CENTER') ? 'CENTER' :
                               (align === 'RIGHT') ? 'RIGHT' :
                               (align === 'JUSTIFIED') ? 'JUSTIFIED' : 'LEFT';
  }
  return node;
}

async function createBadge(label, bgRgb, textRgb, isPill) {
  var frame = figma.createFrame();
  frame.name = 'Badge: ' + label;
  frame.layoutMode = 'HORIZONTAL';
  frame.primaryAxisSizingMode = 'AUTO';
  frame.counterAxisSizingMode = 'AUTO';
  frame.paddingLeft = isPill ? 14 : 8;
  frame.paddingRight = isPill ? 14 : 8;
  frame.paddingTop = isPill ? 6 : 4;
  frame.paddingBottom = isPill ? 6 : 4;
  frame.cornerRadius = isPill ? TOKENS.radius.pill : TOKENS.radius.badge;
  frame.fills = solidFill(bgRgb);
  
  var txt = await createTextNode(label.toUpperCase(), 11, 'bold', textRgb, null, null, 14, 0.8);
  frame.appendChild(txt);
  return frame;
}

async function createMetricCard(val, label, width) {
  var frame = createVerticalContainer('Metric: ' + val, width || 216, 6, { left: 24, right: 24, top: 20, bottom: 20 }, TOKENS.colors.card, TOKENS.colors.borderSubtle, TOKENS.radius.card, true);
  var valNode = await createTextNode(val, 34, 'bold', TOKENS.colors.deepPine, null, null, 38, -0.5);
  var descNode = await createTextNode(label, 13, 'medium', TOKENS.colors.textSecondary, (width ? width - 48 : 168), null, 19);
  frame.appendChild(valNode);
  frame.appendChild(descNode);
// sizing handled by parent auto-layout container
  return frame;
}

async function createHeaderBar(parentWidth) {
  var header = figma.createFrame();
  header.name = 'Header';
  header.resize(parentWidth, 56);
  header.layoutMode = 'HORIZONTAL';
  header.primaryAxisSizingMode = 'FIXED';
  header.counterAxisSizingMode = 'AUTO';
  safeSetPrimaryAlign(header, 'SPACE_BETWEEN');
  safeSetCounterAlign(header, 'CENTER');
  header.clipsContent = false;
  header.fills = [];

  // Brand: Circular IR Mark + Israel Rozar
  var brand = figma.createFrame();
  brand.name = 'Brand';
  brand.layoutMode = 'HORIZONTAL';
  brand.primaryAxisSizingMode = 'AUTO';
  brand.counterAxisSizingMode = 'AUTO';
  brand.itemSpacing = 12;
  safeSetCounterAlign(brand, 'CENTER');
  brand.fills = [];

  var circle = figma.createFrame();
  circle.name = 'Circle';
  circle.resize(36, 36);
  circle.cornerRadius = 18;
  circle.fills = solidFill(TOKENS.colors.deepPine);
  circle.layoutMode = 'HORIZONTAL';
  circle.primaryAxisSizingMode = 'FIXED';
  circle.counterAxisSizingMode = 'FIXED';
  safeSetPrimaryAlign(circle, 'CENTER');
  safeSetCounterAlign(circle, 'CENTER');
  var irTxt = await createTextNode('IR', 13, 'bold', TOKENS.colors.acidLime);
  circle.appendChild(irTxt);
  brand.appendChild(circle);

  var nameTxt = await createTextNode('Israel Rozar', 18, 'semibold', TOKENS.colors.textPrimary);
  brand.appendChild(nameTxt);
  header.appendChild(brand);

  // Nav Links
  var nav = figma.createFrame();
  nav.name = 'Nav';
  nav.layoutMode = 'HORIZONTAL';
  nav.primaryAxisSizingMode = 'AUTO';
  nav.counterAxisSizingMode = 'AUTO';
  nav.itemSpacing = 32;
  safeSetCounterAlign(nav, 'CENTER');
  nav.clipsContent = false;
  nav.fills = [];

  var links = ['Sobre', 'Expertise', 'Cases', 'Trajetória'];
  for (var l = 0; l < links.length; l++) {
    var lnk = await createTextNode(links[l], 14, 'regular', TOKENS.colors.textSecondary);
    nav.appendChild(lnk);
  }

  var cta = figma.createFrame();
  cta.name = 'CTA Contato';
  cta.layoutMode = 'HORIZONTAL';
  cta.primaryAxisSizingMode = 'AUTO';
  cta.counterAxisSizingMode = 'AUTO';
  cta.paddingLeft = 20;
  cta.paddingRight = 20;
  cta.paddingTop = 8;
  cta.paddingBottom = 8;
  cta.cornerRadius = TOKENS.radius.pill;
  cta.fills = solidFill(TOKENS.colors.textPrimary);
  var ctaTxt = await createTextNode('Contato →', 14, 'semibold', TOKENS.colors.card);
  cta.appendChild(ctaTxt);
  nav.appendChild(cta);

  header.appendChild(nav);
  return header;
}

// Injeção de Imagem Real 1:1 sem Textos Redundantes (Assíncrono Seguro)
async function createRealImageFigure(imageKey, captionText, width, height, radius) {
  var container = createVerticalContainer('Figure: ' + imageKey, width, 10, null, null, null, null);
  
  var imageFrame = figma.createFrame();
  imageFrame.name = 'Deliverable: ' + imageKey;
  imageFrame.resize(width, height);
  imageFrame.cornerRadius = radius || TOKENS.radius.card;
  imageFrame.strokes = [{ type: 'SOLID', color: TOKENS.colors.borderSubtle }];
  imageFrame.strokeWeight = 1;
  imageFrame.clipsContent = true;
  imageFrame.effects = softElevation();

  var b64 = REAL_IMAGES[imageKey];
  if (b64 && b64.length > 50) {
    try {
      var bytes = base64ToUint8Array(b64);
      var imgObj = figma.createImage(bytes);
      imageFrame.fills = [{
        type: 'IMAGE',
        scaleMode: 'FILL',
        imageHash: imgObj.hash
      }];
    } catch (e) {
      console.log('Error creating image fill: ' + e);
      imageFrame.fills = solidFill(TOKENS.colors.subtle);
    }
  } else {
    imageFrame.fills = solidFill(TOKENS.colors.subtle);
  }
  container.appendChild(imageFrame);

  if (captionText) {
    var capNode = await createTextNode(captionText, 12, 'regular', TOKENS.colors.textSecondary, width, null, 18);
    container.appendChild(capNode);
  }

  return container;
}
"""

js_builders = r"""
// ============================================================================
// BUILDER: Case Template Genérico com Grid Suíço 2 Colunas (1:1 Oficial)
// ============================================================================

// ============================================================================
// SIMULADOR SALARYNOW (DELIVERABLE VETORIAL CANÔNICO EM ALTA RESOLUÇÃO)
// ============================================================================

// ============================================================================
// DELIVERABLES VETORIAIS EXCLUSIVOS DO CASE SALARYNOW (ZERO SLIDES DE OUTROS CASES)
// ============================================================================

// Cap 01: Funil de Telemetria e Ponto Crítico de Abandono (856 × 482 px)
async function buildSalaryNowCh1Funnel(width, height) {
  var container = createVerticalContainer('Figure: SalaryNow Telemetry Funnel', width, 10, null, null, null, null);
  
  var frame = figma.createFrame();
  frame.name = 'Funil de Telemetria e Abandono';
  frame.resize(width, height);
  frame.cornerRadius = TOKENS.radius.card;
  frame.fills = solidFill(TOKENS.colors.darkPine);
  frame.strokes = [{ type: 'SOLID', color: TOKENS.colors.pineSurface }];
  frame.strokeWeight = 1;
  frame.clipsContent = true;
  frame.effects = softElevation();
  frame.layoutMode = 'VERTICAL';
  frame.primaryAxisSizingMode = 'FIXED';
  frame.counterAxisSizingMode = 'FIXED';
  frame.paddingLeft = 32;
  frame.paddingRight = 32;
  frame.paddingTop = 28;
  frame.paddingBottom = 28;
  frame.itemSpacing = 16;

  var topBar = createHorizontalRow('Funnel Top', width - 64, 0, null, null, null, null, 'SPACE_BETWEEN', 'CENTER');
  var bBadge = await createBadge('TELEMETRIA & MAPA DE CONVERSÃO DO FUNIL B2B2C', TOKENS.colors.pineSurface, TOKENS.colors.acidLime, true);
  var bStatus = await createTextNode('Diagnóstico do Primeiro Uso', 12, 'bold', TOKENS.colors.subtle);
  topBar.appendChild(bBadge);
  topBar.appendChild(bStatus);
  frame.appendChild(topBar);

  var fTitle = await createTextNode('O Paradoxo de Ativação: 68% de Evasão Inicial vs 74% de Recorrência Pós-Uso', 20, 'bold', TOKENS.colors.canvas, width - 64, null, 26, -0.5);
  frame.appendChild(fTitle);

  // 4 Etapas Visuais do Funil
  var funnelGrid = createHorizontalRow('Funnel Stages', width - 64, 12, null, null, null, null, 'SPACE_BETWEEN', 'MIN');
  var stageW = (width - 64 - 36) / 4; // ~188px cada

  // Etapa 1
  var s1 = createVerticalContainer('Etapa 1: Cadastrados', stageW, 8, { left: 14, right: 14, top: 16, bottom: 16 }, TOKENS.colors.pineSurface, TOKENS.colors.borderSubtle, 10);
  var s1P = await createBadge('100% BASE', TOKENS.colors.darkPine, TOKENS.colors.canvas, false);
  var s1T = await createTextNode('Colaboradores Cadastrados', 13, 'bold', TOKENS.colors.canvas);
  var s1D = await createTextNode('Base elegível em empresas de médio porte (varejo, logística e serviços).', 11, 'regular', TOKENS.colors.subtle, stageW - 28, null, 15);
  s1.appendChild(s1P);
  s1.appendChild(s1T);
  s1.appendChild(s1D);
  funnelGrid.appendChild(s1);

  // Etapa 2 (Alerta Crítico)
  var s2 = createVerticalContainer('Etapa 2: Ponto de Evasão', stageW, 8, { left: 14, right: 14, top: 16, bottom: 16 }, { r: 0.35, g: 0.08, b: 0.1 }, { r: 0.8, g: 0.2, b: 0.2 }, 10);
  var s2P = await createBadge('68% EVASÃO', { r: 0.6, g: 0.1, b: 0.1 }, TOKENS.colors.canvas, false);
  var s2T = await createTextNode('Gargalo: Confirmação', 13, 'bold', TOKENS.colors.canvas);
  var s2D = await createTextNode('Maior perda ocorre entre visualização do saldo e confirmação da operação por desconfiança de taxas.', 11, 'regular', TOKENS.colors.subtle, stageW - 28, null, 15);
  s2.appendChild(s2P);
  s2.appendChild(s2T);
  s2.appendChild(s2D);
  funnelGrid.appendChild(s2);

  // Etapa 3
  var s3 = createVerticalContainer('Etapa 3: Ativados', stageW, 8, { left: 14, right: 14, top: 16, bottom: 16 }, TOKENS.colors.pineSurface, TOKENS.colors.borderSubtle, 10);
  var s3P = await createBadge('32% ATIVAÇÃO', TOKENS.colors.darkPine, TOKENS.colors.acidLime, false);
  var s3T = await createTextNode('1ª Antecipação Concluída', 13, 'bold', TOKENS.colors.canvas);
  var s3D = await createTextNode('Usuários que superaram a desconfiança inicial e experimentaram o serviço.', 11, 'regular', TOKENS.colors.subtle, stageW - 28, null, 15);
  s3.appendChild(s3P);
  s3.appendChild(s3T);
  s3.appendChild(s3D);
  funnelGrid.appendChild(s3);

  // Etapa 4
  var s4 = createVerticalContainer('Etapa 4: Recorrência', stageW, 8, { left: 14, right: 14, top: 16, bottom: 16 }, TOKENS.colors.deepPine, TOKENS.colors.acidLime, 10);
  var s4P = await createBadge('74% RETENÇÃO', TOKENS.colors.acidLime, TOKENS.colors.deepPine, false);
  var s4T = await createTextNode('Recorrência no Mês 2', 13, 'bold', TOKENS.colors.canvas);
  var s4D = await createTextNode('Forte PMF comprovado: 74% repetem espontaneamente, realizando 1,8 transações/mês.', 11, 'regular', TOKENS.colors.subtle, stageW - 28, null, 15);
  s4.appendChild(s4P);
  s4.appendChild(s4T);
  s4.appendChild(s4D);
  funnelGrid.appendChild(s4);

  frame.appendChild(funnelGrid);

  // Conclusão Diagnóstica
  var insightBox = createHorizontalRow('Insight Box', width - 64, 12, { left: 16, right: 16, top: 12, bottom: 12 }, TOKENS.colors.pineSurface, null, 8, 'MIN', 'CENTER');
  var inTxt = await createTextNode('💡 DIAGNÓSTICO DO PRODUTO: O produto não tem problema de valor ou retenção no pós-uso — o gargalo é 100% concentrado na opacidade percebida no momento do primeiro aceite financeiro.', 12, 'medium', TOKENS.colors.canvas, width - 96, null, 18);
  insightBox.appendChild(inTxt);
  frame.appendChild(insightBox);

  container.appendChild(frame);

  var cap = await createTextNode('Figura 02 · Mapeamento de telemetria do funil da SalaryNow: 68% de abandono concentrado na etapa de confirmação da taxa.', 12, 'regular', TOKENS.colors.textSecondary, width, null, 18);
  container.appendChild(cap);
  return container;
}

// Cap 02: Matriz dos 4 Riscos de Marty Cagan (856 × 482 px)
async function buildSalaryNowCh2RiskMatrix(width, height) {
  var container = createVerticalContainer('Figure: Cagan 4 Risks Matrix', width, 10, null, null, null, null);
  
  var frame = figma.createFrame();
  frame.name = 'Matriz dos 4 Riscos de Marty Cagan';
  frame.resize(width, height);
  frame.cornerRadius = TOKENS.radius.card;
  frame.fills = solidFill(TOKENS.colors.card);
  frame.strokes = [{ type: 'SOLID', color: TOKENS.colors.borderSubtle }];
  frame.strokeWeight = 1;
  frame.clipsContent = true;
  frame.effects = softElevation();
  frame.layoutMode = 'VERTICAL';
  frame.primaryAxisSizingMode = 'FIXED';
  frame.counterAxisSizingMode = 'FIXED';
  frame.paddingLeft = 32;
  frame.paddingRight = 32;
  frame.paddingTop = 24;
  frame.paddingBottom = 24;
  frame.itemSpacing = 14;

  var topBar = createHorizontalRow('Risk Top', width - 64, 0, null, null, null, null, 'SPACE_BETWEEN', 'CENTER');
  var bBadge = await createBadge('PRIORIZAÇÃO ESTRATÉGICA · 4 RISCOS DE MARTY CAGAN (SVPG)', TOKENS.colors.subtle, TOKENS.colors.deepPine, true);
  var bH = await createTextNode('Capacidade: 2 PMs · 1 Designer · 6 Devs', 11, 'bold', TOKENS.colors.textSecondary);
  topBar.appendChild(bBadge);
  topBar.appendChild(bH);
  frame.appendChild(topBar);

  var rTitle = await createTextNode('Avaliação Comparativa de Riscos do Portfólio (Decisão de Foco 6 a 12 Meses)', 20, 'bold', TOKENS.colors.textPrimary, width - 64, null, 26, -0.5);
  frame.appendChild(rTitle);

  // 3 Colunas dos Produtos
  var pRow = createHorizontalRow('Products Row', width - 64, 14, null, null, null, null, 'SPACE_BETWEEN', 'MIN');
  var pColW = (width - 64 - 28) / 3; // ~254px cada

  // 1. Antecipação Salarial
  var c1 = createVerticalContainer('Prod 1: Antecipação', pColW, 8, { left: 16, right: 16, top: 16, bottom: 16 }, TOKENS.colors.subtle, TOKENS.colors.deepPine, 12);
  var c1Badge = await createBadge('FOCO TOTAL · PRIORIDADE #1', TOKENS.colors.acidLime, TOKENS.colors.deepPine, false);
  var c1Name = await createTextNode('Antecipação Salarial (Core)', 14, 'bold', TOKENS.colors.textPrimary);
  var c1Table = await createTextNode('• Risco de Valor: BAIXO (demanda real)\n• Risco de Usabilidade: ALTO (gargalo)\n• Risco de Viabilidade: BAIXO (core ativo)\n• Risco de Negócio: BAIXO (gera spread)', 11, 'regular', TOKENS.colors.textSecondary, pColW - 32, null, 16);
  var c1Action = await createTextNode('➜ DECISÃO: Concentrar 100% da engenharia e design para destravar a ativação de 32% para 55%+.', 11, 'bold', TOKENS.colors.deepPine, pColW - 32, null, 16);
  c1.appendChild(c1Badge);
  c1.appendChild(c1Name);
  c1.appendChild(c1Table);
  c1.appendChild(c1Action);
  pRow.appendChild(c1);

  // 2. Cartão de Benefícios
  var c2 = createVerticalContainer('Prod 2: Cartao', pColW, 8, { left: 16, right: 16, top: 16, bottom: 16 }, TOKENS.colors.card, TOKENS.colors.borderSubtle, 12);
  var c2Badge = await createBadge('CONGELADO · FORA DE FOCO', TOKENS.colors.subtle, TOKENS.colors.textMuted, false);
  var c2Name = await createTextNode('Cartão de Benefícios', 14, 'bold', TOKENS.colors.textPrimary);
  var c2Table = await createTextNode('• Risco de Valor: ALTO (baixa adesão)\n• Risco de Usabilidade: MÉDIO (físico)\n• Risco de Viabilidade: ALTO (complexo)\n• Risco de Negócio: ALTO (dispersão)', 11, 'regular', TOKENS.colors.textSecondary, pColW - 32, null, 16);
  var c2Action = await createTextNode('➜ DECISÃO: Congelar novos desenvolvimentos para não dispersar a capacidade do time enxuto.', 11, 'bold', TOKENS.colors.textSecondary, pColW - 32, null, 16);
  c2.appendChild(c2Badge);
  c2.appendChild(c2Name);
  c2.appendChild(c2Table);
  c2.appendChild(c2Action);
  pRow.appendChild(c2);

  // 3. Portal RH
  var c3 = createVerticalContainer('Prod 3: Portal RH', pColW, 8, { left: 16, right: 16, top: 16, bottom: 16 }, TOKENS.colors.card, TOKENS.colors.borderSubtle, 12);
  var c3Badge = await createBadge('APOIO SECUNDÁRIO', TOKENS.colors.subtle, TOKENS.colors.deepPine, false);
  var c3Name = await createTextNode('Portal RH (B2B)', 14, 'bold', TOKENS.colors.textPrimary);
  var c3Table = await createTextNode('• Risco de Valor: MÉDIO (desconhecido)\n• Risco de Usabilidade: ALTO (burocrático)\n• Risco de Viabilidade: BAIXO (web simples)\n• Risco de Negócio: MÉDIO (retenção B2B)', 11, 'regular', TOKENS.colors.textSecondary, pColW - 32, null, 16);
  var c3Action = await createTextNode('➜ DECISÃO: Adicionar painel de saúde financeira agregada para transformar o RH em promotor.', 11, 'bold', TOKENS.colors.deepPine, pColW - 32, null, 16);
  c3.appendChild(c3Badge);
  c3.appendChild(c3Name);
  c3.appendChild(c3Table);
  c3.appendChild(c3Action);
  pRow.appendChild(c3);

  frame.appendChild(pRow);

  var rBottom = createHorizontalRow('Risk Bottom', width - 64, 0, { left: 16, right: 16, top: 10, bottom: 10 }, TOKENS.colors.subtle, null, 8, 'SPACE_BETWEEN', 'CENTER');
  var rbTxt = await createTextNode('Critérios de Decisão: Impacto direto no LTV do modelo de spread financeiro e proteção da capacidade dos 6 desenvolvedores.', 12, 'medium', TOKENS.colors.deepPine);
  rBottom.appendChild(rbTxt);
  frame.appendChild(rBottom);

  container.appendChild(frame);

  var cap = await createTextNode('Figura 03 · Avaliação dos 4 Riscos de Marty Cagan (SVPG): justificativa técnica para congelamento do Cartão e priorização total da Antecipação Salarial.', 12, 'regular', TOKENS.colors.textSecondary, width, null, 18);
  container.appendChild(cap);
  return container;
}

// Cap 03: Diagrama de Princípios Gestalt do Simulador (856 × 482 px)
async function buildSalaryNowCh3GestaltSimulator(width, height) {
  var container = createVerticalContainer('Figure: Gestalt Simulator Architecture', width, 10, null, null, null, null);
  
  var frame = figma.createFrame();
  frame.name = 'Arquitetura Gestalt do Simulador';
  frame.resize(width, height);
  frame.cornerRadius = TOKENS.radius.card;
  frame.fills = solidFill(TOKENS.colors.deepPine);
  frame.strokes = [{ type: 'SOLID', color: TOKENS.colors.pineSurface }];
  frame.strokeWeight = 1;
  frame.clipsContent = true;
  frame.effects = softElevation();
  frame.layoutMode = 'VERTICAL';
  frame.primaryAxisSizingMode = 'FIXED';
  frame.counterAxisSizingMode = 'FIXED';
  frame.paddingLeft = 32;
  frame.paddingRight = 32;
  frame.paddingTop = 24;
  frame.paddingBottom = 24;
  frame.itemSpacing = 16;

  var topBar = createHorizontalRow('Gestalt Top', width - 64, 0, null, null, null, null, 'SPACE_BETWEEN', 'CENTER');
  var bBadge = await createBadge('ARQUITETURA DA INFORMAÇÃO & PSICOLOGIA GESTALT', TOKENS.colors.darkPine, TOKENS.colors.acidLime, true);
  var bNorm = await createBadge('CONFORMIDADE BACEN', TOKENS.colors.pineSurface, TOKENS.colors.canvas, true);
  topBar.appendChild(bBadge);
  topBar.appendChild(bNorm);
  frame.appendChild(topBar);

  var gTitle = await createTextNode('Anatomia Cognitiva do Simulador: Leis de Região Comum e Proximidade', 20, 'bold', TOKENS.colors.canvas, width - 64, null, 26, -0.5);
  frame.appendChild(gTitle);

  // 3 Blocos de Demonstração Gestalt
  var gGrid = createHorizontalRow('Gestalt Grid', width - 64, 14, null, null, null, null, 'SPACE_BETWEEN', 'MIN');
  var gColW = (width - 64 - 28) / 3;

  // Bloco 1: Região Comum
  var b1 = createVerticalContainer('Bloco 1: Região Comum', gColW, 8, { left: 16, right: 16, top: 16, bottom: 16 }, TOKENS.colors.card, null, 10);
  var b1Pill = await createBadge('LEI DE REGIÃO COMUM', TOKENS.colors.subtle, TOKENS.colors.deepPine, false);
  var b1T = await createTextNode('Delimitação de Taxa (Spread)', 13, 'bold', TOKENS.colors.textPrimary);
  var b1D = await createTextNode('A taxa de R$ 12,00 é contida em um container próprio com fundo contrastante. O usuário entende que não há encargos fora desta caixa.', 11, 'regular', TOKENS.colors.textSecondary, gColW - 32, null, 16);
  b1.appendChild(b1Pill);
  b1.appendChild(b1T);
  b1.appendChild(b1D);
  gGrid.appendChild(b1);

  // Bloco 2: Proximidade
  var b2 = createVerticalContainer('Bloco 2: Proximidade', gColW, 8, { left: 16, right: 16, top: 16, bottom: 16 }, TOKENS.colors.card, null, 10);
  var b2Pill = await createBadge('LEI DE PROXIMIDADE', TOKENS.colors.subtle, TOKENS.colors.deepPine, false);
  var b2T = await createTextNode('Custo CET Adjacente ao PIX', 13, 'bold', TOKENS.colors.textPrimary);
  var b2D = await createTextNode('O valor líquido (R$ 288) é posicionado colado ao custo total (R$ 12), permitindo checagem matemática instantânea antes do aceite.', 11, 'regular', TOKENS.colors.textSecondary, gColW - 32, null, 16);
  b2.appendChild(b2Pill);
  b2.appendChild(b2T);
  b2.appendChild(b2D);
  gGrid.appendChild(b2);

  // Bloco 3: Feedback
  var b3 = createVerticalContainer('Bloco 3: Holerite', gColW, 8, { left: 16, right: 16, top: 16, bottom: 16 }, TOKENS.colors.subtle, TOKENS.colors.borderSubtle, 10);
  var b3Pill = await createBadge('HEURÍSTICA #1 NIELSEN', TOKENS.colors.pineSurface, TOKENS.colors.canvas, false);
  var b3T = await createTextNode('Impacto no Próximo Salário', 13, 'bold', TOKENS.colors.textPrimary);
  var b3D = await createTextNode('Preview dinâmico do holerite: "Receba R$ 2.688 no 5º dia útil". Elimina o medo de surpresas desagradáveis no dia do pagamento.', 11, 'regular', TOKENS.colors.textSecondary, gColW - 32, null, 16);
  b3.appendChild(b3Pill);
  b3.appendChild(b3T);
  b3.appendChild(b3D);
  gGrid.appendChild(b3);

  frame.appendChild(gGrid);

  var gFooter = createHorizontalRow('Gestalt Footer', width - 64, 0, { left: 16, right: 16, top: 10, bottom: 10 }, TOKENS.colors.darkPine, TOKENS.colors.pineSurface, 8, 'SPACE_BETWEEN', 'CENTER');
  var gfTxt = await createTextNode('Resultado Cognitivo: Transformação do sentimento de "endividamento perigoso" em "benefício transparente e sob controle".', 12, 'semibold', TOKENS.colors.acidLime);
  gFooter.appendChild(gfTxt);
  frame.appendChild(gFooter);

  container.appendChild(frame);

  var cap = await createTextNode('Figura 04 · Princípios de Gestalt e Psicologia Visual aplicados ao simulador financeiro para dissolver barreiras de desconfiança.', 12, 'regular', TOKENS.colors.textSecondary, width, null, 18);
  container.appendChild(cap);
  return container;
}

// Cap 04: Painel B2B de Saúde Financeira do Portal RH (856 × 482 px)
async function buildSalaryNowCh4HrPortal(width, height) {
  var container = createVerticalContainer('Figure: SalaryNow HR Portal Dashboard', width, 10, null, null, null, null);
  
  var frame = figma.createFrame();
  frame.name = 'Portal RH: Dashboard de Saúde Financeira';
  frame.resize(width, height);
  frame.cornerRadius = TOKENS.radius.card;
  frame.fills = solidFill(TOKENS.colors.subtle);
  frame.strokes = [{ type: 'SOLID', color: TOKENS.colors.borderSubtle }];
  frame.strokeWeight = 1;
  frame.clipsContent = true;
  frame.effects = softElevation();
  frame.layoutMode = 'VERTICAL';
  frame.primaryAxisSizingMode = 'FIXED';
  frame.counterAxisSizingMode = 'FIXED';
  frame.paddingLeft = 32;
  frame.paddingRight = 32;
  frame.paddingTop = 24;
  frame.paddingBottom = 24;
  frame.itemSpacing = 16;

  // Header do Portal RH
  var topBar = createHorizontalRow('Portal Top', width - 64, 0, null, null, null, null, 'SPACE_BETWEEN', 'CENTER');
  var tLeft = createHorizontalRow('Portal Brand', 300, 10, null, null, null, null, 'MIN', 'CENTER');
  var bBadge = await createBadge('PORTAL RH · B2B', TOKENS.colors.deepPine, TOKENS.colors.canvas, true);
  var bName = await createTextNode('SalaryNow Corporativo', 14, 'bold', TOKENS.colors.textPrimary);
  tLeft.appendChild(bBadge);
  tLeft.appendChild(bName);
  topBar.appendChild(tLeft);

  var bLgpd = await createBadge('100% LGPD COMPLIANT · DADOS AGREGADOS', TOKENS.colors.card, TOKENS.colors.deepPine, true);
  topBar.appendChild(bLgpd);
  frame.appendChild(topBar);

  var pTitle = await createTextNode('Painel de Saúde Financeira Corporativa: Retenção e Alívio de Estresse dos Times', 20, 'bold', TOKENS.colors.textPrimary, width - 64, null, 26, -0.5);
  frame.appendChild(pTitle);

  // 3 Métricas Analíticas para o Gestor de RH
  var mRow = createHorizontalRow('Metrics Row', width - 64, 14, null, null, null, null, 'SPACE_BETWEEN', 'MIN');
  var mColW = (width - 64 - 28) / 3;

  var m1 = createVerticalContainer('M1: Adesao', mColW, 6, { left: 16, right: 16, top: 16, bottom: 16 }, TOKENS.colors.card, TOKENS.colors.borderSubtle, 10);
  var m1T = await createTextNode('Taxa de Adesão Corporativa', 12, 'bold', TOKENS.colors.textSecondary);
  var m1V = await createTextNode('59%', 32, 'bold', TOKENS.colors.deepPine);
  var m1D = await createTextNode('Colaboradores elegíveis ativos nos setores de Varejo e Operações.', 11, 'regular', TOKENS.colors.textMuted, mColW - 32, null, 15);
  m1.appendChild(m1T);
  m1.appendChild(m1V);
  m1.appendChild(m1D);
  mRow.appendChild(m1);

  var m2 = createVerticalContainer('M2: Alivio', mColW, 6, { left: 16, right: 16, top: 16, bottom: 16 }, TOKENS.colors.card, TOKENS.colors.borderSubtle, 10);
  var m2T = await createTextNode('Índice de Alívio Financeiro', 12, 'bold', TOKENS.colors.textSecondary);
  var m2V = await createTextNode('84%', 32, 'bold', TOKENS.colors.deepPine);
  var m2D = await createTextNode('Redução reportada em preocupações financeiras imediatas em pesquisa anônima.', 11, 'regular', TOKENS.colors.textMuted, mColW - 32, null, 15);
  m2.appendChild(m2T);
  m2.appendChild(m2V);
  m2.appendChild(m2D);
  mRow.appendChild(m2);

  var m3 = createVerticalContainer('M3: Turnover', mColW, 6, { left: 16, right: 16, top: 16, bottom: 16 }, TOKENS.colors.card, TOKENS.colors.borderSubtle, 10);
  var m3T = await createTextNode('Impacto Estimado no Turnover', 12, 'bold', TOKENS.colors.textSecondary);
  var m3V = await createTextNode('-18%', 32, 'bold', TOKENS.colors.deepPine);
  var m3D = await createTextNode('Maior estabilidade de permanência em colaboradores com acesso ao benefício.', 11, 'regular', TOKENS.colors.textMuted, mColW - 32, null, 15);
  m3.appendChild(m3T);
  m3.appendChild(m3V);
  m3.appendChild(m3D);
  mRow.appendChild(m3);

  frame.appendChild(mRow);

  var pFooter = createHorizontalRow('Portal Footer', width - 64, 0, { left: 16, right: 16, top: 10, bottom: 10 }, TOKENS.colors.card, TOKENS.colors.borderSubtle, 8, 'SPACE_BETWEEN', 'CENTER');
  var pfTxt = await createTextNode('Empoderamento B2B: O RH deixou de ser um mero digitador de cadastros e virou o maior embaixador interno da ativação do benefício.', 12, 'semibold', TOKENS.colors.deepPine);
  pFooter.appendChild(pfTxt);
  frame.appendChild(pFooter);

  container.appendChild(frame);

  var cap = await createTextNode('Figura 05 · Painel de Saúde Financeira Corporativa no Portal RH: valor B2B tangível respeitando a privacidade dos colaboradores.', 12, 'regular', TOKENS.colors.textSecondary, width, null, 18);
  container.appendChild(cap);
  return container;
}

// Cap 05: Dashboard Consolidado de Resultados STAR (856 × 482 px)
async function buildSalaryNowCh5ResultsDashboard(width, height) {
  var container = createVerticalContainer('Figure: SalaryNow STAR Results', width, 10, null, null, null, null);
  
  var frame = figma.createFrame();
  frame.name = 'Resultados Consolidados STAR';
  frame.resize(width, height);
  frame.cornerRadius = TOKENS.radius.card;
  frame.fills = solidFill(TOKENS.colors.darkPine);
  frame.strokes = [{ type: 'SOLID', color: TOKENS.colors.pineSurface }];
  frame.strokeWeight = 1;
  frame.clipsContent = true;
  frame.effects = softElevation();
  frame.layoutMode = 'VERTICAL';
  frame.primaryAxisSizingMode = 'FIXED';
  frame.counterAxisSizingMode = 'FIXED';
  frame.paddingLeft = 32;
  frame.paddingRight = 32;
  frame.paddingTop = 24;
  frame.paddingBottom = 24;
  frame.itemSpacing = 16;

  var topBar = createHorizontalRow('Results Top', width - 64, 0, null, null, null, null, 'SPACE_BETWEEN', 'CENTER');
  var bBadge = await createBadge('RESULTADOS TRIANGULADOS & IMPACTO DE NEGÓCIO (STAR)', TOKENS.colors.pineSurface, TOKENS.colors.acidLime, true);
  var bTime = await createTextNode('Período: 8 Meses em Produção', 12, 'bold', TOKENS.colors.subtle);
  topBar.appendChild(bBadge);
  topBar.appendChild(bTime);
  frame.appendChild(topBar);

  var rTitle = await createTextNode('Métricas Auditadas Pós-Implantação: Destravando o LTV da Fintech', 20, 'bold', TOKENS.colors.canvas, width - 64, null, 26, -0.5);
  frame.appendChild(rTitle);

  // 4 Cards de Resultados Antes vs Depois
  var resGrid = createHorizontalRow('Res Grid', width - 64, 12, null, null, null, null, 'SPACE_BETWEEN', 'MIN');
  var rColW = (width - 64 - 36) / 4;

  var r1 = createVerticalContainer('R1', rColW, 6, { left: 14, right: 14, top: 16, bottom: 16 }, TOKENS.colors.pineSurface, null, 10);
  var r1T = await createTextNode('Ativação 1º Uso', 11, 'bold', TOKENS.colors.subtle);
  var r1V = await createTextNode('32% ➔ 59%', 22, 'bold', TOKENS.colors.acidLime);
  var r1D = await createTextNode('+27 pp de crescimento sobre a base de colaboradores cadastrados.', 11, 'regular', TOKENS.colors.canvas, rColW - 28, null, 15);
  r1.appendChild(r1T);
  r1.appendChild(r1V);
  r1.appendChild(r1D);
  resGrid.appendChild(r1);

  var r2 = createVerticalContainer('R2', rColW, 6, { left: 14, right: 14, top: 16, bottom: 16 }, TOKENS.colors.pineSurface, null, 10);
  var r2T = await createTextNode('Evasão Confirmação', 11, 'bold', TOKENS.colors.subtle);
  var r2V = await createTextNode('68% ➔ 19%', 22, 'bold', TOKENS.colors.acidLime);
  var r2D = await createTextNode('Queda maciça no abandono após disclosure claro de custos CET.', 11, 'regular', TOKENS.colors.canvas, rColW - 28, null, 15);
  r2.appendChild(r2T);
  r2.appendChild(r2V);
  r2.appendChild(r2D);
  resGrid.appendChild(r2);

  var r3 = createVerticalContainer('R3', rColW, 6, { left: 14, right: 14, top: 16, bottom: 16 }, TOKENS.colors.pineSurface, null, 10);
  var r3T = await createTextNode('Chamados Suporte', 11, 'bold', TOKENS.colors.subtle);
  var r3V = await createTextNode('-63%', 24, 'bold', TOKENS.colors.acidLime);
  var r3D = await createTextNode('Redução substancial de tickets sobre dúvidas de taxas ou descontos.', 11, 'regular', TOKENS.colors.canvas, rColW - 28, null, 15);
  r3.appendChild(r3T);
  r3.appendChild(r3V);
  r3.appendChild(r3D);
  resGrid.appendChild(r3);

  var r4 = createVerticalContainer('R4', rColW, 6, { left: 14, right: 14, top: 16, bottom: 16 }, TOKENS.colors.pineSurface, null, 10);
  var r4T = await createTextNode('Auditoria BACEN', 11, 'bold', TOKENS.colors.subtle);
  var r4V = await createTextNode('100%', 24, 'bold', TOKENS.colors.acidLime);
  var r4D = await createTextNode('Total conformidade regulatória nas normas de crédito e transparência.', 11, 'regular', TOKENS.colors.canvas, rColW - 28, null, 15);
  r4.appendChild(r4T);
  r4.appendChild(r4V);
  r4.appendChild(r4D);
  resGrid.appendChild(r4);

  frame.appendChild(resGrid);

  var resFooter = createHorizontalRow('Results Footer', width - 64, 0, { left: 16, right: 16, top: 10, bottom: 10 }, TOKENS.colors.pineSurface, null, 8, 'SPACE_BETWEEN', 'CENTER');
  var rfTxt = await createTextNode('Reflexão Crítica: Testes presenciais em fábricas e centros de distribuição desde o D0 teriam antecipado a barreira do holerite em 6 semanas.', 12, 'medium', TOKENS.colors.canvas);
  resFooter.appendChild(rfTxt);
  frame.appendChild(resFooter);

  container.appendChild(frame);

  var cap = await createTextNode('Figura 06 · Consolidação de resultados mensuráveis do framework STAR: impacto direto em ativação, receita e eficiência operacional.', 12, 'regular', TOKENS.colors.textSecondary, width, null, 18);
  container.appendChild(cap);
  return container;
}

async function createSalaryNowHero(width, height) {
  var container = createVerticalContainer('Figure: SalaryNow Simulator', width, 10, null, null, null, null);
  
  var heroFrame = figma.createFrame();
  heroFrame.name = 'Deliverable: SalaryNow Simulator';
  heroFrame.resize(width, height);
  heroFrame.cornerRadius = TOKENS.radius.feature;
  heroFrame.fills = solidFill(TOKENS.colors.deepPine);
  heroFrame.strokes = [{ type: 'SOLID', color: TOKENS.colors.pineSurface }];
  heroFrame.strokeWeight = 1;
  heroFrame.clipsContent = true;
  heroFrame.effects = softElevation();
  heroFrame.layoutMode = 'VERTICAL';
  heroFrame.primaryAxisSizingMode = 'FIXED';
  heroFrame.counterAxisSizingMode = 'FIXED';
  heroFrame.paddingLeft = 40;
  heroFrame.paddingRight = 40;
  heroFrame.paddingTop = 32;
  heroFrame.paddingBottom = 32;
  heroFrame.itemSpacing = 20;

  // 1. Top Bar
  var topBar = createHorizontalRow('Hero Top Bar', width - 80, 0, null, null, null, null, 'SPACE_BETWEEN', 'CENTER');
  var topLeft = figma.createFrame();
  topLeft.layoutMode = 'HORIZONTAL';
  topLeft.primaryAxisSizingMode = 'AUTO';
  topLeft.counterAxisSizingMode = 'AUTO';
  topLeft.itemSpacing = 12;
  safeSetCounterAlign(topLeft, 'CENTER');
  topLeft.fills = [];
  var tagBadge = await createBadge('SALARYNOW · FINTECH B2B2C', TOKENS.colors.darkPine, TOKENS.colors.acidLime, true);
  var appTitle = await createTextNode('Simulador Transparente de Antecipação Salarial', 18, 'bold', TOKENS.colors.canvas);
  topLeft.appendChild(tagBadge);
  topLeft.appendChild(appTitle);
  topBar.appendChild(topLeft);

  var bacenBadge = await createBadge('CONFORME RESOLUÇÃO BACEN', TOKENS.colors.pineSurface, TOKENS.colors.canvas, true);
  topBar.appendChild(bacenBadge);
  heroFrame.appendChild(topBar);

  // 2. Subtitle
  var sub = await createTextNode('Eliminação do ponto crítico de abandono (68%): visualização transparente de taxa única e projeção instantânea do holerite futuro.', 14, 'regular', TOKENS.colors.subtle, width - 80, null, 20);
  heroFrame.appendChild(sub);

  // 3. Grid 3 Colunas de Simulação (Gestalt: Região Comum e Proximidade)
  var gridRow = createHorizontalRow('Simulador Gestalt Grid', width - 80, 20, null, null, null, null, 'SPACE_BETWEEN', 'MIN');
  var colW = (width - 80 - 40) / 3;

  // Coluna 1: Parâmetros de Seleção (344px)
  var col1 = createVerticalContainer('Card 01: Escolha do Valor', colW, 14, { left: 20, right: 20, top: 20, bottom: 20 }, TOKENS.colors.card, TOKENS.colors.borderSubtle, TOKENS.radius.card);
  var c1Head = await createTextNode('01 · VALOR DA ANTECIPAÇÃO', 11, 'bold', TOKENS.colors.deepPine, null, null, 14, 0.8);
  var c1Val = await createTextNode('R$ 300,00', 36, 'bold', TOKENS.colors.textPrimary, null, null, 40, -1);
  var c1Disp = await createTextNode('Saldo disponível: R$ 1.850,00 (Salário: R$ 3.000)', 12, 'regular', TOKENS.colors.textSecondary, colW - 40, null, 16);
  
  var sliderFrame = figma.createFrame();
  sliderFrame.name = 'Slider Component';
  sliderFrame.resize(colW - 40, 28);
  sliderFrame.fills = [];
  var trackBg = figma.createFrame();
  trackBg.name = 'Track Bg';
  trackBg.resize(colW - 40, 8);
  trackBg.y = 10;
  trackBg.cornerRadius = 4;
  trackBg.fills = solidFill(TOKENS.colors.subtle);
  sliderFrame.appendChild(trackBg);
  var trackFill = figma.createFrame();
  trackFill.name = 'Track Fill';
  trackFill.resize((colW - 40) * 0.35, 8);
  trackFill.y = 10;
  trackFill.cornerRadius = 4;
  trackFill.fills = solidFill(TOKENS.colors.acidLime);
  sliderFrame.appendChild(trackFill);
  var thumb = figma.createFrame();
  thumb.name = 'Thumb';
  thumb.resize(20, 20);
  thumb.x = (colW - 40) * 0.35 - 10;
  thumb.y = 4;
  thumb.cornerRadius = 10;
  thumb.fills = solidFill(TOKENS.colors.deepPine);
  thumb.strokes = [{ type: 'SOLID', color: TOKENS.colors.acidLime }];
  thumb.strokeWeight = 2;
  sliderFrame.appendChild(thumb);

  var pillRow = createHorizontalRow('Pills', colW - 40, 8, null, null, null, null, 'MIN', 'CENTER');
  var p1 = await createBadge('R$ 150', TOKENS.colors.subtle, TOKENS.colors.textPrimary, false);
  var p2 = await createBadge('R$ 300', TOKENS.colors.acidLime, TOKENS.colors.deepPine, false);
  var p3 = await createBadge('R$ 500', TOKENS.colors.subtle, TOKENS.colors.textPrimary, false);
  pillRow.appendChild(p1);
  pillRow.appendChild(p2);
  pillRow.appendChild(p3);

  col1.appendChild(c1Head);
  col1.appendChild(c1Val);
  col1.appendChild(c1Disp);
  col1.appendChild(sliderFrame);
  col1.appendChild(pillRow);
  gridRow.appendChild(col1);

  // Coluna 2: Transparência de Custos (Região Comum Gestalt - 344px)
  var col2 = createVerticalContainer('Card 02: Transparência CET', colW, 10, { left: 20, right: 20, top: 20, bottom: 20 }, TOKENS.colors.card, TOKENS.colors.borderSubtle, TOKENS.radius.card);
  var c2Head = await createTextNode('02 · TRANSPARÊNCIA RADICAL (CET)', 11, 'bold', TOKENS.colors.deepPine, null, null, 14, 0.8);
  col2.appendChild(c2Head);

  var costLines = [
    { k: 'Valor Solicitado:', v: 'R$ 300,00' },
    { k: 'Taxa de Conveniência (Spread):', v: '- R$ 12,00' },
    { k: 'IOF / Encargos Regulatórios:', v: 'Isento' },
    { k: 'Custo Efetivo Total (Fixo):', v: 'R$ 12,00' }
  ];
  for (var cl = 0; cl < costLines.length; cl++) {
    var cRow = createHorizontalRow('Cost ' + cl, colW - 40, 0, { top: 4, bottom: 4, left: 0, right: 0 }, null, null, null, 'SPACE_BETWEEN', 'CENTER');
    var kNode = await createTextNode(costLines[cl].k, 12, 'regular', TOKENS.colors.textSecondary);
    var vNode = await createTextNode(costLines[cl].v, 12, 'semibold', TOKENS.colors.textPrimary);
    cRow.appendChild(kNode);
    cRow.appendChild(vNode);
    col2.appendChild(cRow);
  }

  var divider = figma.createFrame();
  divider.name = 'Divider';
  divider.resize(colW - 40, 1);
  divider.fills = solidFill(TOKENS.colors.borderSubtle);
  col2.appendChild(divider);

  var netBox = createHorizontalRow('Net Box', colW - 40, 0, { top: 8, bottom: 4, left: 0, right: 0 }, null, null, null, 'SPACE_BETWEEN', 'CENTER');
  var netLbl = await createTextNode('Líquido na sua Conta (PIX):', 13, 'bold', TOKENS.colors.deepPine);
  var netVal = await createTextNode('R$ 288,00', 20, 'bold', TOKENS.colors.deepPine);
  netBox.appendChild(netLbl);
  netBox.appendChild(netVal);
  col2.appendChild(netBox);
  gridRow.appendChild(col2);

  // Coluna 3: Projeção do Holerite (Gestalt de Proximidade - 344px)
  var col3 = createVerticalContainer('Card 03: Projeção Holerite', colW, 10, { left: 20, right: 20, top: 20, bottom: 20 }, TOKENS.colors.subtle, TOKENS.colors.borderSubtle, TOKENS.radius.card);
  var c3Head = await createTextNode('03 · IMPACTO NO PRÓXIMO SALÁRIO', 11, 'bold', TOKENS.colors.textSecondary, null, null, 14, 0.8);
  col3.appendChild(c3Head);

  var holeriteLines = [
    { k: 'Salário Base Contratual:', v: 'R$ 3.000,00' },
    { k: 'Desconto Antecipação (Líquido):', v: '- R$ 288,00' },
    { k: 'Taxa de Serviço SalaryNow:', v: '- R$ 12,00' },
    { k: 'Total a Descontar em Folha:', v: '- R$ 312,00' }
  ];
  for (var hl = 0; hl < holeriteLines.length; hl++) {
    var hRow = createHorizontalRow('Holerite ' + hl, colW - 40, 0, { top: 4, bottom: 4, left: 0, right: 0 }, null, null, null, 'SPACE_BETWEEN', 'CENTER');
    var hkNode = await createTextNode(holeriteLines[hl].k, 12, 'regular', TOKENS.colors.textSecondary);
    var hvNode = await createTextNode(holeriteLines[hl].v, 12, 'semibold', TOKENS.colors.textPrimary);
    hRow.appendChild(hkNode);
    hRow.appendChild(hvNode);
    col3.appendChild(hRow);
  }

  var div3 = figma.createFrame();
  div3.name = 'Divider';
  div3.resize(colW - 40, 1);
  div3.fills = solidFill(TOKENS.colors.borderSubtle);
  col3.appendChild(div3);

  var restBox = createHorizontalRow('Rest Box', colW - 40, 0, { top: 8, bottom: 4, left: 0, right: 0 }, null, null, null, 'SPACE_BETWEEN', 'CENTER');
  var restLbl = await createTextNode('Saldo no 5º Dia Útil:', 13, 'bold', TOKENS.colors.textPrimary);
  var restVal = await createTextNode('R$ 2.688,00', 20, 'bold', TOKENS.colors.deepPine);
  restBox.appendChild(restLbl);
  restBox.appendChild(restVal);
  col3.appendChild(restBox);
  gridRow.appendChild(col3);

  heroFrame.appendChild(gridRow);

  // 4. Action Row (Confirm + Trust)
  var actionRow = createHorizontalRow('Hero Action Row', width - 80, 0, null, null, null, null, 'SPACE_BETWEEN', 'CENTER');
  var trustTxt = await createTextNode('🔒 Sem juros rotativos recorrentes. Cobrança única em folha regulada pelo Banco Central.', 13, 'regular', TOKENS.colors.subtle);
  
  var btnConfirm = figma.createFrame();
  btnConfirm.name = 'Btn Confirmar Antecipacao';
  btnConfirm.layoutMode = 'HORIZONTAL';
  btnConfirm.primaryAxisSizingMode = 'AUTO';
  btnConfirm.counterAxisSizingMode = 'AUTO';
  btnConfirm.paddingLeft = 28;
  btnConfirm.paddingRight = 28;
  btnConfirm.paddingTop = 16;
  btnConfirm.paddingBottom = 16;
  btnConfirm.cornerRadius = TOKENS.radius.pill;
  btnConfirm.fills = solidFill(TOKENS.colors.acidLime);
  var btnTxt = await createTextNode('Confirmar Antecipação via PIX Imediato ➔', 14, 'bold', TOKENS.colors.deepPine);
  btnConfirm.appendChild(btnTxt);

  actionRow.appendChild(trustTxt);
  actionRow.appendChild(btnConfirm);
  heroFrame.appendChild(actionRow);

  container.appendChild(heroFrame);

  var capNode = await createTextNode(
    'Figura 01 · Simulador Transparente de Antecipação Salarial: arquitetura de informação aplicando Princípios Gestalt de Região Comum e Proximidade para eliminar o abandono de 68% na confirmação.',
    12,
    'regular',
    TOKENS.colors.textSecondary,
    width,
    null,
    18
  );
  container.appendChild(capNode);

  return container;
}


// ============================================================================
// ENTREGÁVEIS VETORIAIS NEUTROS PARA CASE TEMPLATE (SENIOR UX CANON)
// Zero Contaminação de Clientes (Sem slides de consultoria, sem imagens externas)
// ============================================================================

async function buildTemplateHeroBlueprint(width, height) {
  var container = createVerticalContainer('Figure: Template Hero Blueprint', width, 10, null, null, null, null);
  
  var frame = figma.createFrame();
  frame.name = 'Blueprint Arquitetural 1:1';
  frame.resize(width, height);
  frame.cornerRadius = TOKENS.radius.card;
  frame.fills = solidFill(TOKENS.colors.deepPine);
  frame.strokes = [{ type: 'SOLID', color: TOKENS.colors.pineSurface }];
  frame.strokeWeight = 1;
  frame.clipsContent = true;
  frame.effects = softElevation();
  frame.layoutMode = 'VERTICAL';
  frame.primaryAxisSizingMode = 'FIXED';
  frame.counterAxisSizingMode = 'FIXED';
  frame.paddingLeft = 32;
  frame.paddingRight = 32;
  frame.paddingTop = 28;
  frame.paddingBottom = 28;
  frame.itemSpacing = 20;

  var topBar = createHorizontalRow('Blueprint Top', width - 64, 0, null, null, null, null, 'SPACE_BETWEEN', 'CENTER');
  var bBadge = await createBadge('ARQUITETURA DE DESIGN SYSTEM & PRODUTO', TOKENS.colors.darkPine, TOKENS.colors.acidLime, true);
  var bNorm = await createBadge('FRAMEWORK CANÔNICO SENIOR UX', TOKENS.colors.pineSurface, TOKENS.colors.canvas, true);
  topBar.appendChild(bBadge);
  topBar.appendChild(bNorm);
  frame.appendChild(topBar);

  var title = await createTextNode('Visão Sistêmica: Da Taxonomia de Dados aos Contratos de Interface', 22, 'bold', TOKENS.colors.canvas, width - 64, null, 28, -0.5);
  frame.appendChild(title);

  // 3 Colunas de Arquitetura Sistêmica
  var gridRow = createHorizontalRow('Blueprint Grid', width - 64, 16, null, null, null, null, 'SPACE_BETWEEN', 'MIN');
  var colW = (width - 64 - 32) / 3;

  // Coluna 1: Camada de Dados & Contratos
  var col1 = createVerticalContainer('Camada 01: Dados & Contratos', colW, 10, { left: 20, right: 20, top: 20, bottom: 20 }, TOKENS.colors.darkPine, TOKENS.colors.pineSurface, TOKENS.radius.card);
  var c1Head = await createBadge('01 · MODELO DE DADOS', TOKENS.colors.subtle, TOKENS.colors.deepPine, false);
  var c1Title = await createTextNode('Taxonomia & Contratos', 16, 'bold', TOKENS.colors.canvas);
  var c1Desc = await createTextNode('Estruturação de schemas JSON, unificação de entidades legadas e contratos rígidos de tipagem acordados com engenharia.', 13, 'regular', TOKENS.colors.textMuted, colW - 40, null, 20);
  col1.appendChild(c1Head);
  col1.appendChild(c1Title);
  col1.appendChild(c1Desc);
  gridRow.appendChild(col1);
  safeSetFill(col1, 'VERTICAL');

  // Coluna 2: Tokens & Componentes Canônicos
  var col2 = createVerticalContainer('Camada 02: Design System', colW, 10, { left: 20, right: 20, top: 20, bottom: 20 }, TOKENS.colors.darkPine, TOKENS.colors.pineSurface, TOKENS.radius.card);
  var c2Head = await createBadge('02 · DESIGN SYSTEM', TOKENS.colors.subtle, TOKENS.colors.deepPine, false);
  var c2Title = await createTextNode('Tokens & Componentes', 16, 'bold', TOKENS.colors.canvas);
  var c2Desc = await createTextNode('Tokens de espaçamento (base 8px), escala tipográfica modular, matriz de estados (Hover, Focus, Disabled) e paridade 1:1 com código.', 13, 'regular', TOKENS.colors.textMuted, colW - 40, null, 20);
  col2.appendChild(c2Head);
  col2.appendChild(c2Title);
  col2.appendChild(c2Desc);
  gridRow.appendChild(col2);
  safeSetFill(col2, 'VERTICAL');

  // Coluna 3: Governança & Acessibilidade
  var col3 = createVerticalContainer('Camada 03: Governança', colW, 10, { left: 20, right: 20, top: 20, bottom: 20 }, TOKENS.colors.darkPine, TOKENS.colors.pineSurface, TOKENS.radius.card);
  var c3Head = await createBadge('03 · CONFORMIDADE', TOKENS.colors.acidLime, TOKENS.colors.deepPine, true);
  var c3Title = await createTextNode('Acessibilidade WCAG AAA', 16, 'bold', TOKENS.colors.canvas);
  var c3Desc = await createTextNode('Contraste triplo superior a 12:1, suporte pleno a navegação por teclado, redução de latência e instrumentação de telemetria.', 13, 'regular', TOKENS.colors.textMuted, colW - 40, null, 20);
  col3.appendChild(c3Head);
  col3.appendChild(c3Title);
  col3.appendChild(c3Desc);
  gridRow.appendChild(col3);
  safeSetFill(col3, 'VERTICAL');

  frame.appendChild(gridRow);
  container.appendChild(frame);

  var cap = await createTextNode('Figura 01 · Blueprint Arquitetural do Sistema: integração tripartite entre modelo de dados, Design System e governança regulatória.', 12, 'regular', TOKENS.colors.textSecondary, width, null, 18);
  container.appendChild(cap);
  return container;
}

async function buildTemplateCh1Schematic(width, height) {
  var container = createVerticalContainer('Figure: Ch1 Reframing Schematic', width, 10, null, null, null, null);
  
  var frame = figma.createFrame();
  frame.name = 'Reenquadramento de Briefing';
  frame.resize(width, height);
  frame.cornerRadius = TOKENS.radius.card;
  frame.fills = solidFill(TOKENS.colors.card);
  frame.strokes = [{ type: 'SOLID', color: TOKENS.colors.borderSubtle }];
  frame.strokeWeight = 1;
  frame.clipsContent = true;
  frame.effects = softElevation();
  frame.layoutMode = 'VERTICAL';
  frame.primaryAxisSizingMode = 'FIXED';
  frame.counterAxisSizingMode = 'FIXED';
  frame.paddingLeft = 32;
  frame.paddingRight = 32;
  frame.paddingTop = 24;
  frame.paddingBottom = 24;
  frame.itemSpacing = 16;

  var topRow = createHorizontalRow('Reframing Top', width - 64, 0, null, null, null, null, 'SPACE_BETWEEN', 'CENTER');
  var badge = await createBadge('METODOLOGIA DE DISCOVERY & REFRAMING', TOKENS.colors.subtle, TOKENS.colors.deepPine, false);
  var metricPill = await createBadge('DIAGNOSTICO EVIDENCIADO', TOKENS.colors.deepPine, TOKENS.colors.acidLime, true);
  topRow.appendChild(badge);
  topRow.appendChild(metricPill);
  frame.appendChild(topRow);

  var title = await createTextNode('Reenquadramento do Problema: Investigação de Causa-Raiz Sistêmica', 20, 'bold', TOKENS.colors.textPrimary, width - 64, null, 26, -0.5);
  frame.appendChild(title);

  // Comparação Lado a Lado: Briefing Sintoma vs Problema Real
  var compRow = createHorizontalRow('Comp Row', width - 64, 20, null, null, null, null, 'SPACE_BETWEEN', 'MIN');
  var compW = (width - 64 - 20) / 2;

  // Lado Esquerdo: Briefing Original (Sintoma)
  var leftCard = createVerticalContainer('Card: Briefing Original', compW, 10, { left: 24, right: 24, top: 20, bottom: 20 }, { r: 0.98, g: 0.94, b: 0.94 }, { r: 0.9, g: 0.75, b: 0.75 }, 12);
  var lTag = await createBadge('BRIEFING ORIGINAL (SINTOMA)', { r: 0.9, g: 0.2, b: 0.2 }, TOKENS.colors.canvas, true);
  var lTitle = await createTextNode('Demanda por Novas Telas Cosméticas', 16, 'bold', TOKENS.colors.textPrimary);
  var lDesc = await createTextNode('A solicitação dos stakeholders sugeria que a evasão de usuários decorria da estética da interface, demandando redesenho superficial sem tocar em regras de negócio ou APIs legadas.', 13, 'regular', TOKENS.colors.textSecondary, compW - 48, null, 20);
  leftCard.appendChild(lTag);
  leftCard.appendChild(lTitle);
  leftCard.appendChild(lDesc);
  compRow.appendChild(leftCard);
  safeSetFill(leftCard, 'VERTICAL');

  // Lado Direito: Problema Real (Validado por Dados)
  var rightCard = createVerticalContainer('Card: Problema Real', compW, 10, { left: 24, right: 24, top: 20, bottom: 20 }, TOKENS.colors.subtle, TOKENS.colors.deepPine, 12);
  var rTag = await createBadge('PROBLEMA REAL EVIDENCIADO (CAUSA-RAIZ)', TOKENS.colors.deepPine, TOKENS.colors.acidLime, true);
  var rTitle = await createTextNode('Gargalo em Modelo Mental & Taxonomia', 16, 'bold', TOKENS.colors.deepPine);
  var rDesc = await createTextNode('A telemetria e as entrevistas semiestruturadas demonstraram que 82% das falhas operacionais decorriam de ambiguidades na hierarquia de dados e ausência de feedback em tempo real.', 13, 'regular', TOKENS.colors.textPrimary, compW - 48, null, 20);
  rightCard.appendChild(rTag);
  rightCard.appendChild(rTitle);
  rightCard.appendChild(rDesc);
  compRow.appendChild(rightCard);
  safeSetFill(rightCard, 'VERTICAL');

  frame.appendChild(compRow);
  container.appendChild(frame);

  var cap = await createTextNode('Figura 02 · Matriz de Reenquadramento: redirecionamento do investimento de engenharia para o gargalo de maior alavancagem.', 12, 'regular', TOKENS.colors.textSecondary, width, null, 18);
  container.appendChild(cap);
  return container;
}

async function buildTemplateCh2Schematic(width, height) {
  var container = createVerticalContainer('Figure: Ch2 Architecture Schematic', width, 10, null, null, null, null);
  
  var frame = figma.createFrame();
  frame.name = 'Arquitetura da Informação & Carga Cognitiva';
  frame.resize(width, height);
  frame.cornerRadius = TOKENS.radius.card;
  frame.fills = solidFill(TOKENS.colors.deepPine);
  frame.strokes = [{ type: 'SOLID', color: TOKENS.colors.pineSurface }];
  frame.strokeWeight = 1;
  frame.clipsContent = true;
  frame.effects = softElevation();
  frame.layoutMode = 'VERTICAL';
  frame.primaryAxisSizingMode = 'FIXED';
  frame.counterAxisSizingMode = 'FIXED';
  frame.paddingLeft = 32;
  frame.paddingRight = 32;
  frame.paddingTop = 24;
  frame.paddingBottom = 24;
  frame.itemSpacing = 16;

  var topRow = createHorizontalRow('AI Top', width - 64, 0, null, null, null, null, 'SPACE_BETWEEN', 'CENTER');
  var badge = await createBadge('ARQUITETURA DA INFORMAÇÃO & HEURÍSTICAS', TOKENS.colors.darkPine, TOKENS.colors.acidLime, true);
  var metricPill = await createBadge('CARGA COGNITIVA: -65%', TOKENS.colors.pineSurface, TOKENS.colors.canvas, true);
  topRow.appendChild(badge);
  topRow.appendChild(metricPill);
  frame.appendChild(topRow);

  var title = await createTextNode('Modelo Mental Modular: Estruturação em 3 Camadas Visuais', 20, 'bold', TOKENS.colors.canvas, width - 64, null, 26, -0.5);
  frame.appendChild(title);

  // 3 Níveis de Informação
  var levelsRow = createHorizontalRow('Levels Row', width - 64, 16, null, null, null, null, 'SPACE_BETWEEN', 'MIN');
  var lvlW = (width - 64 - 32) / 3;

  var levels = [
    { n: 'NÍVEL 01', t: 'Visão Executiva (Panorama)', d: 'Resumo consolidado em tempo real, status operacional e alertas acionáveis acima da dobra.' },
    { n: 'NÍVEL 02', t: 'Painel Contextual (Operações)', d: 'Agrupamento Gestalt por proximidade de controles, filtros assistidos e tabelas de alta densidade.' },
    { n: 'NÍVEL 03', t: 'Ação & Confirmação', d: 'Disclosures compulsórios, simulação de impactos secundários e zero ambiguidade antes do commit.' }
  ];

  for (var i = 0; i < levels.length; i++) {
    var lCard = createVerticalContainer('Level ' + (i+1), lvlW, 10, { left: 20, right: 20, top: 20, bottom: 20 }, TOKENS.colors.darkPine, TOKENS.colors.pineSurface, 12);
    var lBadge = await createBadge(levels[i].n, TOKENS.colors.subtle, TOKENS.colors.deepPine, false);
    var lT = await createTextNode(levels[i].t, 15, 'bold', TOKENS.colors.canvas);
    var lD = await createTextNode(levels[i].d, 12, 'regular', TOKENS.colors.textMuted, lvlW - 40, null, 18);
    lCard.appendChild(lBadge);
    lCard.appendChild(lT);
    lCard.appendChild(lD);
    levelsRow.appendChild(lCard);
    safeSetFill(lCard, 'VERTICAL');
  }

  frame.appendChild(levelsRow);
  container.appendChild(frame);

  var cap = await createTextNode('Figura 03 · Blueprint de Arquitetura da Informação: redução de 5 para 2 níveis de profundidade operacional.', 12, 'regular', TOKENS.colors.textSecondary, width, null, 18);
  container.appendChild(cap);
  return container;
}

async function buildTemplateCh3Schematic(width, height) {
  var container = createVerticalContainer('Figure: Ch3 DS Schematic', width, 10, null, null, null, null);
  
  var frame = figma.createFrame();
  frame.name = 'Design System & Governança de Tokens';
  frame.resize(width, height);
  frame.cornerRadius = TOKENS.radius.card;
  frame.fills = solidFill(TOKENS.colors.card);
  frame.strokes = [{ type: 'SOLID', color: TOKENS.colors.borderSubtle }];
  frame.strokeWeight = 1;
  frame.clipsContent = true;
  frame.effects = softElevation();
  frame.layoutMode = 'VERTICAL';
  frame.primaryAxisSizingMode = 'FIXED';
  frame.counterAxisSizingMode = 'FIXED';
  frame.paddingLeft = 32;
  frame.paddingRight = 32;
  frame.paddingTop = 24;
  frame.paddingBottom = 24;
  frame.itemSpacing = 16;

  var topRow = createHorizontalRow('DS Top', width - 64, 0, null, null, null, null, 'SPACE_BETWEEN', 'CENTER');
  var badge = await createBadge('DESIGN SYSTEM & TOKENS DTCG', TOKENS.colors.subtle, TOKENS.colors.deepPine, false);
  var metricPill = await createBadge('PARIDADE 1:1 CÓDIGO', TOKENS.colors.deepPine, TOKENS.colors.acidLime, true);
  topRow.appendChild(badge);
  topRow.appendChild(metricPill);
  frame.appendChild(topRow);

  var title = await createTextNode('Sistemática de Componentes: Estados, Tokens Semânticos e A11y', 20, 'bold', TOKENS.colors.textPrimary, width - 64, null, 26, -0.5);
  frame.appendChild(title);

  // Matriz de Tokens & Estados
  var dsGrid = createHorizontalRow('DS Grid', width - 64, 16, null, null, null, null, 'SPACE_BETWEEN', 'MIN');
  var dsColW = (width - 64 - 16) / 2;

  // Bloco Esquerdo: Grid de Espaçamento 8px
  var bLeft = createVerticalContainer('Tokens Espaçamento', dsColW, 8, { left: 20, right: 20, top: 16, bottom: 16 }, TOKENS.colors.subtle, TOKENS.colors.borderSubtle, 12);
  var blTitle = await createTextNode('Escala de Tokens Espaciais (Base 8px)', 14, 'bold', TOKENS.colors.deepPine);
  bLeft.appendChild(blTitle);

  var tokenScales = [
    { name: 'space-xs (4px)', usage: 'Gap entre micro-ícones e labels auxiliares' },
    { name: 'space-sm (8px)', usage: 'Padding interno de chips, tags e botões compactos' },
    { name: 'space-md (16px)', usage: 'Espaçamento padrão entre campos de formulário e itens' },
    { name: 'space-lg (24px)', usage: 'Padding interno de containers e cartões executivos' },
    { name: 'space-xl (32px)', usage: 'Margem entre seções estruturais de conteúdo' }
  ];

  for (var ts = 0; ts < tokenScales.length; ts++) {
    var tsRow = createHorizontalRow('TS ' + ts, dsColW - 40, 0, null, null, null, null, 'SPACE_BETWEEN', 'CENTER');
    var tsN = await createTextNode(tokenScales[ts].name, 12, 'bold', TOKENS.colors.textPrimary);
    var tsU = await createTextNode(tokenScales[ts].usage, 11, 'regular', TOKENS.colors.textSecondary);
    tsRow.appendChild(tsN);
    tsRow.appendChild(tsU);
    bLeft.appendChild(tsRow);
  }
  dsGrid.appendChild(bLeft);
  safeSetFill(bLeft, 'VERTICAL');

  // Bloco Direito: Matriz de Estados de Componentes
  var bRight = createVerticalContainer('Estados Componentes', dsColW, 8, { left: 20, right: 20, top: 16, bottom: 16 }, TOKENS.colors.subtle, TOKENS.colors.borderSubtle, 12);
  var brTitle = await createTextNode('Matriz de Estados de Interação (WCAG AAA)', 14, 'bold', TOKENS.colors.deepPine);
  bRight.appendChild(brTitle);

  var stateMatrix = [
    { st: 'Default', bg: '#0A3622', fg: '#CEFF1A', border: 'none' },
    { st: 'Hover (+8% L)', bg: '#102B1D', fg: '#CEFF1A', border: '1px solid #CEFF1A' },
    { st: 'Focus Ring (3px)', bg: '#0A3622', fg: '#FFFFFF', border: '3px solid #CEFF1A' },
    { st: 'Disabled (38% Op)', bg: '#EDE9DE', fg: '#8C968E', border: 'none' }
  ];

  for (var sm = 0; sm < stateMatrix.length; sm++) {
    var smRow = createHorizontalRow('State ' + sm, dsColW - 40, 0, null, null, null, null, 'SPACE_BETWEEN', 'CENTER');
    var smLbl = await createTextNode(stateMatrix[sm].st, 12, 'bold', TOKENS.colors.textPrimary);
    var smPill = await createBadge('AMOSTRA 1:1', TOKENS.colors.deepPine, TOKENS.colors.acidLime, false);
    smRow.appendChild(smLbl);
    smRow.appendChild(smPill);
    bRight.appendChild(smRow);
  }
  dsGrid.appendChild(bRight);
  safeSetFill(bRight, 'VERTICAL');

  frame.appendChild(dsGrid);
  container.appendChild(frame);

  var cap = await createTextNode('Figura 04 · Matriz do Design System: tokens espaciais auditados e estados interativos certificados para WCAG AAA.', 12, 'regular', TOKENS.colors.textSecondary, width, null, 18);
  container.appendChild(cap);
  return container;
}

async function buildTemplateCh4Schematic(width, height) {
  var container = createVerticalContainer('Figure: Ch4 Scope Schematic', width, 10, null, null, null, null);
  
  var frame = figma.createFrame();
  frame.name = 'Disciplina de Escopo & Trade-offs';
  frame.resize(width, height);
  frame.cornerRadius = TOKENS.radius.card;
  frame.fills = solidFill(TOKENS.colors.card);
  frame.strokes = [{ type: 'SOLID', color: TOKENS.colors.borderSubtle }];
  frame.strokeWeight = 1;
  frame.clipsContent = true;
  frame.effects = softElevation();
  frame.layoutMode = 'VERTICAL';
  frame.primaryAxisSizingMode = 'FIXED';
  frame.counterAxisSizingMode = 'FIXED';
  frame.paddingLeft = 32;
  frame.paddingRight = 32;
  frame.paddingTop = 24;
  frame.paddingBottom = 24;
  frame.itemSpacing = 16;

  var topRow = createHorizontalRow('Scope Top', width - 64, 0, null, null, null, null, 'SPACE_BETWEEN', 'CENTER');
  var badge = await createBadge('GOVERNANÇA DE ESCOPO & DESACORDO CONSTRUTIVO', TOKENS.colors.subtle, TOKENS.colors.deepPine, false);
  var metricPill = await createBadge('VELOCIDADE TÉCNICA: +40%', TOKENS.colors.deepPine, TOKENS.colors.acidLime, true);
  topRow.appendChild(badge);
  topRow.appendChild(metricPill);
  frame.appendChild(topRow);

  var title = await createTextNode('O Que NÃO Foi Construído: Decisões Deliberadas de Foco', 20, 'bold', TOKENS.colors.textPrimary, width - 64, null, 26, -0.5);
  frame.appendChild(title);

  // 2 Colunas: O que foi construído vs O que foi descartado
  var scopeRow = createHorizontalRow('Scope Row', width - 64, 20, null, null, null, null, 'SPACE_BETWEEN', 'MIN');
  var sColW = (width - 64 - 20) / 2;

  // Lado Verde: Construído no MVP
  var builtCard = createVerticalContainer('Card: Construído', sColW, 10, { left: 24, right: 24, top: 20, bottom: 20 }, TOKENS.colors.subtle, TOKENS.colors.deepPine, 12);
  var bTag = await createBadge('CONSTRUÍDO NO MVP (ALTO VALOR & BAIXO RISCO)', TOKENS.colors.deepPine, TOKENS.colors.acidLime, true);
  var bTitle = await createTextNode('Core Operacional Essencial', 15, 'bold', TOKENS.colors.deepPine);
  var bItems = [
    '✔ Visualização consolidada de saldos e vencimentos em tela única.',
    '✔ Feedback em tempo real com disclosure compulsório de custos.',
    '✔ Acessibilidade certificada WCAG AAA para uso prolongado sem fadiga.'
  ];
  builtCard.appendChild(bTag);
  builtCard.appendChild(bTitle);
  for (var bi = 0; bi < bItems.length; bi++) {
    var biNode = await createTextNode(bItems[bi], 12, 'regular', TOKENS.colors.textPrimary, sColW - 48, null, 18);
    builtCard.appendChild(biNode);
  }
  scopeRow.appendChild(builtCard);
  safeSetFill(builtCard, 'VERTICAL');

  // Lado Vermelho/Neutro: Deliberadamente Descartado
  var cutCard = createVerticalContainer('Card: Descartado', sColW, 10, { left: 24, right: 24, top: 20, bottom: 20 }, { r: 0.98, g: 0.94, b: 0.94 }, { r: 0.9, g: 0.75, b: 0.75 }, 12);
  var cTag = await createBadge('DELIBERADAMENTE DESCARTADO (ALTO RISCO)', { r: 0.85, g: 0.15, b: 0.15 }, TOKENS.colors.canvas, true);
  var cTitle = await createTextNode('Dispersão & Complexidade Excessiva', 15, 'bold', { r: 0.7, g: 0.1, b: 0.1 });
  var cItems = [
    '✖ Filtros aninhados multicamada que aumentavam tempo de resposta em 3x.',
    '✖ Customização visual por usuário que violava contratos de acessibilidade.',
    '✖ Integrações secundárias que consumiriam 80% do time de engenharia.'
  ];
  cutCard.appendChild(cTag);
  cutCard.appendChild(cTitle);
  for (var ci = 0; ci < cItems.length; ci++) {
    var ciNode = await createTextNode(cItems[ci], 12, 'regular', TOKENS.colors.textSecondary, sColW - 48, null, 18);
    cutCard.appendChild(ciNode);
  }
  scopeRow.appendChild(cutCard);
  safeSetFill(cutCard, 'VERTICAL');

  frame.appendChild(scopeRow);
  container.appendChild(frame);

  var cap = await createTextNode('Figura 05 · Matriz de Disciplina de Escopo: proteção da capacidade de entrega e foco no core de maior retorno.', 12, 'regular', TOKENS.colors.textSecondary, width, null, 18);
  container.appendChild(cap);
  return container;
}

async function buildTemplateCh5Schematic(width, height) {
  var container = createVerticalContainer('Figure: Ch5 Impact Schematic', width, 10, null, null, null, null);
  
  var frame = figma.createFrame();
  frame.name = 'Resultados de Negócio & Telemetria';
  frame.resize(width, height);
  frame.cornerRadius = TOKENS.radius.card;
  frame.fills = solidFill(TOKENS.colors.deepPine);
  frame.strokes = [{ type: 'SOLID', color: TOKENS.colors.pineSurface }];
  frame.strokeWeight = 1;
  frame.clipsContent = true;
  frame.effects = softElevation();
  frame.layoutMode = 'VERTICAL';
  frame.primaryAxisSizingMode = 'FIXED';
  frame.counterAxisSizingMode = 'FIXED';
  frame.paddingLeft = 32;
  frame.paddingRight = 32;
  frame.paddingTop = 24;
  frame.paddingBottom = 24;
  frame.itemSpacing = 16;

  var topRow = createHorizontalRow('Impact Top', width - 64, 0, null, null, null, null, 'SPACE_BETWEEN', 'CENTER');
  var badge = await createBadge('MÉTRICAS AUDITADAS: RECEITA, CUSTO E RISCO', TOKENS.colors.darkPine, TOKENS.colors.acidLime, true);
  var metricPill = await createBadge('TELEMETRIA EM PRODUÇÃO', TOKENS.colors.pineSurface, TOKENS.colors.canvas, true);
  topRow.appendChild(badge);
  topRow.appendChild(metricPill);
  frame.appendChild(topRow);

  var title = await createTextNode('Painel Executivo de Impacto Mensurável Pós-Lançamento', 20, 'bold', TOKENS.colors.canvas, width - 64, null, 26, -0.5);
  frame.appendChild(title);

  // 3 Indicadores Quantitativos com Barras de Comparação
  var kpiRow = createHorizontalRow('KPI Row', width - 64, 16, null, null, null, null, 'SPACE_BETWEEN', 'MIN');
  var kpiW = (width - 64 - 32) / 3;

  var kpis = [
    { label: 'TEMPO MÉDIO DE OPERAÇÃO', val: '-38%', sub: 'De 4.2 min para 2.6 min por transação' },
    { label: 'CHAMADOS DE SUPORTE', val: '-45%', sub: 'Redução direta de custos operacionais' },
    { label: 'CONFORMIDADE REGULATÓRIA', val: '100%', sub: 'Zero autuações ou apontamentos de auditoria' }
  ];

  for (var k = 0; k < kpis.length; k++) {
    var kCard = createVerticalContainer('KPI ' + (k+1), kpiW, 8, { left: 20, right: 20, top: 20, bottom: 20 }, TOKENS.colors.darkPine, TOKENS.colors.pineSurface, 12);
    var kL = await createTextNode(kpis[k].label, 11, 'bold', TOKENS.colors.textMuted, null, null, 14, 0.8);
    var kV = await createTextNode(kpis[k].val, 34, 'bold', TOKENS.colors.acidLime);
    var kS = await createTextNode(kpis[k].sub, 12, 'regular', TOKENS.colors.canvas, kpiW - 40, null, 18);
    kCard.appendChild(kL);
    kCard.appendChild(kV);
    kCard.appendChild(kS);
    kpiRow.appendChild(kCard);
    safeSetFill(kCard, 'VERTICAL');
  }

  frame.appendChild(kpiRow);
  container.appendChild(frame);

  var cap = await createTextNode('Figura 06 · Painel de Resultados Consolidados: evidências quantitativas ancoradas ao baseline histórico.', 12, 'regular', TOKENS.colors.textSecondary, width, null, 18);
  container.appendChild(cap);
  return container;
}

// ============================================================================
// 4 ENTREGÁVEIS VETORIAIS DE ALTO CRAFT PARA OS CARDS DA HOME (508 × 286 px)
// Substituem placeholders genéricos por mockups reais de produto em alta fidelidade
// ============================================================================

async function buildHomeCardThumbItauHub(width, height) {
  var frame = figma.createFrame();
  frame.name = 'Mockup: Itaú Hub de Liquidez';
  frame.resize(width, height);
  frame.cornerRadius = TOKENS.radius.panel;
  frame.fills = solidFill(TOKENS.colors.deepPine);
  frame.strokes = [{ type: 'SOLID', color: TOKENS.colors.pineSurface }];
  frame.strokeWeight = 1;
  frame.clipsContent = true;
  frame.layoutMode = 'VERTICAL';
  frame.primaryAxisSizingMode = 'FIXED';
  frame.counterAxisSizingMode = 'FIXED';
  frame.paddingLeft = 20;
  frame.paddingRight = 20;
  frame.paddingTop = 16;
  frame.paddingBottom = 16;
  frame.itemSpacing = 12;

  var top = createHorizontalRow('Hub Top', width - 40, 0, null, null, null, null, 'SPACE_BETWEEN', 'CENTER');
  var pill = await createBadge('ITAÚ ÍON · HUB B2B', TOKENS.colors.darkPine, TOKENS.colors.acidLime, true);
  var stat = await createBadge('R$ 42.4B SOB GESTÃO', TOKENS.colors.pineSurface, TOKENS.colors.canvas, true);
  top.appendChild(pill);
  top.appendChild(stat);
  frame.appendChild(top);

  var tNode = await createTextNode('Hub de Liquidez & Antecipação de Oportunidades', 16, 'bold', TOKENS.colors.canvas, width - 40, null, 22);
  frame.appendChild(tNode);

  var statsRow = createHorizontalRow('Stats', width - 40, 10, null, null, null, null, 'SPACE_BETWEEN', 'MIN');
  var sW = (width - 40 - 20) / 3;
  var sData = [
    { k: 'LIQUIDEZ D+0', v: 'R$ 8.2B' },
    { k: 'VENCIMENTOS 30D', v: 'R$ 3.1B' },
    { k: 'OPORTUNIDADES', v: '142 Ativas' }
  ];
  for (var i = 0; i < sData.length; i++) {
    var sc = createVerticalContainer('S' + i, sW, 4, { left: 10, right: 10, top: 8, bottom: 8 }, TOKENS.colors.darkPine, TOKENS.colors.pineSurface, 8);
    var sk = await createTextNode(sData[i].k, 9, 'bold', TOKENS.colors.textMuted);
    var sv = await createTextNode(sData[i].v, 14, 'bold', TOKENS.colors.acidLime);
    sc.appendChild(sk);
    sc.appendChild(sv);
    statsRow.appendChild(sc);
  }
  frame.appendChild(statsRow);

  var assetRow = createHorizontalRow('Asset Preview', width - 40, 8, { left: 12, right: 12, top: 10, bottom: 10 }, TOKENS.colors.darkPine, TOKENS.colors.pineSurface, 8, 'SPACE_BETWEEN', 'CENTER');
  var aLbl = await createTextNode('LCI Pós-Fixada 102% CDI · Vence em 4 dias', 11, 'medium', TOKENS.colors.canvas);
  var aBtn = await createBadge('REINVESTIR ➔', TOKENS.colors.acidLime, TOKENS.colors.deepPine, true);
  assetRow.appendChild(aLbl);
  assetRow.appendChild(aBtn);
  frame.appendChild(assetRow);

  return frame;
}

async function buildHomeCardThumbItauVenc(width, height) {
  var frame = figma.createFrame();
  frame.name = 'Mockup: Gestão de Vencimentos';
  frame.resize(width, height);
  frame.cornerRadius = TOKENS.radius.panel;
  frame.fills = solidFill(TOKENS.colors.darkPine);
  frame.strokes = [{ type: 'SOLID', color: TOKENS.colors.pineSurface }];
  frame.strokeWeight = 1;
  frame.clipsContent = true;
  frame.layoutMode = 'VERTICAL';
  frame.primaryAxisSizingMode = 'FIXED';
  frame.counterAxisSizingMode = 'FIXED';
  frame.paddingLeft = 20;
  frame.paddingRight = 20;
  frame.paddingTop = 16;
  frame.paddingBottom = 16;
  frame.itemSpacing = 12;

  var top = createHorizontalRow('Venc Top', width - 40, 0, null, null, null, null, 'SPACE_BETWEEN', 'CENTER');
  var pill = await createBadge('ALERTA PROATIVO D-30', TOKENS.colors.subtle, TOKENS.colors.deepPine, false);
  var stat = await createBadge('TEMPO: -60%', TOKENS.colors.acidLime, TOKENS.colors.deepPine, true);
  top.appendChild(pill);
  top.appendChild(stat);
  frame.appendChild(top);

  var tNode = await createTextNode('Painel Analítico de Vencimentos em Carteira', 16, 'bold', TOKENS.colors.canvas, width - 40, null, 22);
  frame.appendChild(tNode);

  var calRow = createHorizontalRow('Cal Strip', width - 40, 8, null, null, null, null, 'SPACE_BETWEEN', 'CENTER');
  var calDays = ['D-7', 'D-15', 'D-30 (ATIVO)', 'D-60'];
  for (var d = 0; d < calDays.length; d++) {
    var isAct = (d === 2);
    var dChip = await createBadge(calDays[d], isAct ? TOKENS.colors.acidLime : TOKENS.colors.pineSurface, isAct ? TOKENS.colors.deepPine : TOKENS.colors.canvas, isAct);
    calRow.appendChild(dChip);
  }
  frame.appendChild(calRow);

  var alertCard = createHorizontalRow('Alert Card', width - 40, 8, { left: 12, right: 12, top: 10, bottom: 10 }, TOKENS.colors.deepPine, TOKENS.colors.pineSurface, 8, 'SPACE_BETWEEN', 'CENTER');
  var alTxt = await createTextNode('CDB Pré 12.8% a.a. · Saldo: R$ 450.000', 11, 'medium', TOKENS.colors.canvas);
  var alAction = await createBadge('RECOMENDAR ➔', TOKENS.colors.canvas, TOKENS.colors.deepPine, true);
  alertCard.appendChild(alTxt);
  alertCard.appendChild(alAction);
  frame.appendChild(alertCard);

  return frame;
}

async function buildHomeCardThumbNeoenergia(width, height) {
  var frame = figma.createFrame();
  frame.name = 'Mockup: Neoenergia Service Blueprint';
  frame.resize(width, height);
  frame.cornerRadius = TOKENS.radius.panel;
  frame.fills = solidFill(TOKENS.colors.deepPine);
  frame.strokes = [{ type: 'SOLID', color: TOKENS.colors.pineSurface }];
  frame.strokeWeight = 1;
  frame.clipsContent = true;
  frame.layoutMode = 'VERTICAL';
  frame.primaryAxisSizingMode = 'FIXED';
  frame.counterAxisSizingMode = 'FIXED';
  frame.paddingLeft = 20;
  frame.paddingRight = 20;
  frame.paddingTop = 16;
  frame.paddingBottom = 16;
  frame.itemSpacing = 12;

  var top = createHorizontalRow('Neo Top', width - 40, 0, null, null, null, null, 'SPACE_BETWEEN', 'CENTER');
  var pill = await createBadge('SERVICE DESIGN & P&D ANEEL', TOKENS.colors.darkPine, TOKENS.colors.acidLime, true);
  var stat = await createBadge('34M HABITANTES', TOKENS.colors.pineSurface, TOKENS.colors.canvas, true);
  top.appendChild(pill);
  top.appendChild(stat);
  frame.appendChild(top);

  var tNode = await createTextNode('Unificação da Infraestrutura de Atendimento Físico e Digital', 16, 'bold', TOKENS.colors.canvas, width - 40, null, 22);
  frame.appendChild(tNode);

  var chRow = createHorizontalRow('Channels', width - 40, 8, null, null, null, null, 'SPACE_BETWEEN', 'CENTER');
  var channels = ['App Mobile', 'Agência Virtual', 'WhatsApp Bot', 'Loja Presencial'];
  for (var c = 0; c < channels.length; c++) {
    var chBadge = await createBadge(channels[c], TOKENS.colors.darkPine, TOKENS.colors.canvas, false);
    chRow.appendChild(chBadge);
  }
  frame.appendChild(chRow);

  var bpStrip = createHorizontalRow('Blueprint Flow', width - 40, 8, { left: 12, right: 12, top: 10, bottom: 10 }, TOKENS.colors.darkPine, TOKENS.colors.pineSurface, 8, 'SPACE_BETWEEN', 'CENTER');
  var bpTxt = await createTextNode('5 Blueprints de Serviço · 4 Distribuidoras Conectadas 1:1', 11, 'medium', TOKENS.colors.acidLime);
  var bpBtn = await createBadge('VER FLUXO ↗', TOKENS.colors.pineSurface, TOKENS.colors.canvas, true);
  bpStrip.appendChild(bpTxt);
  bpStrip.appendChild(bpBtn);
  frame.appendChild(bpStrip);

  return frame;
}

async function buildHomeCardThumbClaro(width, height) {
  var frame = figma.createFrame();
  frame.name = 'Mockup: Claro Ativação Multicanal';
  frame.resize(width, height);
  frame.cornerRadius = TOKENS.radius.panel;
  frame.fills = solidFill(TOKENS.colors.pineSurface);
  frame.strokes = [{ type: 'SOLID', color: TOKENS.colors.darkPine }];
  frame.strokeWeight = 1;
  frame.clipsContent = true;
  frame.layoutMode = 'VERTICAL';
  frame.primaryAxisSizingMode = 'FIXED';
  frame.counterAxisSizingMode = 'FIXED';
  frame.paddingLeft = 20;
  frame.paddingRight = 20;
  frame.paddingTop = 16;
  frame.paddingBottom = 16;
  frame.itemSpacing = 12;

  var top = createHorizontalRow('Claro Top', width - 40, 0, null, null, null, null, 'SPACE_BETWEEN', 'CENTER');
  var pill = await createBadge('TELECOM · JORNADA MULTICANAL', TOKENS.colors.deepPine, TOKENS.colors.acidLime, true);
  var stat = await createBadge('22 JORNADAS MAP', TOKENS.colors.darkPine, TOKENS.colors.canvas, true);
  top.appendChild(pill);
  top.appendChild(stat);
  frame.appendChild(top);

  var tNode = await createTextNode('Esteira Unificada de Checkout para Lojas e Televendas', 16, 'bold', TOKENS.colors.canvas, width - 40, null, 22);
  frame.appendChild(tNode);

  var stepRow = createHorizontalRow('Steps', width - 40, 6, null, null, null, null, 'SPACE_BETWEEN', 'CENTER');
  var steps = ['1. Plano', '2. eSIM', '3. Biometria', '4. Ativação ✔'];
  for (var s = 0; s < steps.length; s++) {
    var isLast = (s === 3);
    var sBadge = await createBadge(steps[s], isLast ? TOKENS.colors.acidLime : TOKENS.colors.deepPine, isLast ? TOKENS.colors.deepPine : TOKENS.colors.canvas, isLast);
    stepRow.appendChild(sBadge);
  }
  frame.appendChild(stepRow);

  var simStrip = createHorizontalRow('Plan Strip', width - 40, 8, { left: 12, right: 12, top: 10, bottom: 10 }, TOKENS.colors.deepPine, TOKENS.colors.darkPine, 8, 'SPACE_BETWEEN', 'CENTER');
  var pTxt = await createTextNode('Claro Pós 50GB 5G + Redes Sociais Ilimitadas', 11, 'medium', TOKENS.colors.canvas);
  var pBtn = await createBadge('SIMULAR ➔', TOKENS.colors.acidLime, TOKENS.colors.deepPine, true);
  simStrip.appendChild(pTxt);
  simStrip.appendChild(pBtn);
  frame.appendChild(simStrip);

  return frame;
}

// ============================================================================
// PARSER & RENDERIZADOR DE CONTEÚDO ESTRUTURADO (DECISION CARDS COM BADGES)
// Elimina despejo de texto plano e substitui marcadores • por cards editoriais
// ============================================================================

async function renderStructuredContent(rawText, width) {
  var container = createVerticalContainer('Decisões & Conteúdo Estruturado', width, 12, null, null, null, null);
  
  if (!rawText) return container;

  if (rawText.indexOf('•') === -1 && rawText.indexOf('\n') === -1) {
    var pNode = await createTextNode(rawText, 16, 'regular', TOKENS.colors.textSecondary, width, null, 26);
    container.appendChild(pNode);
    return container;
  }

  var lines = rawText.split('\n');
  for (var i = 0; i < lines.length; i++) {
    var line = lines[i].trim();
    if (!line) continue;
    
    if (line.indexOf('•') === 0 || line.indexOf('-') === 0 || line.indexOf('1.') === 0 || line.indexOf('2.') === 0 || line.indexOf('3.') === 0 || line.indexOf('4.') === 0) {
      var clean = line.replace(/^[•\-\d\.]+\s*/, '').trim();
      var colonIdx = clean.indexOf(':');
      
      var tag = 'DECISÃO TÉCNICA';
      var body = clean;
      
      if (colonIdx !== -1 && colonIdx < 45) {
        tag = clean.substring(0, colonIdx).trim().toUpperCase();
        body = clean.substring(colonIdx + 1).trim();
      }
      
      var badgeBg = TOKENS.colors.subtle;
      var badgeFg = TOKENS.colors.deepPine;
      if (tag.indexOf('GATILHO') !== -1 || tag.indexOf('PROBLEMA') !== -1) {
        badgeBg = TOKENS.colors.subtle;
        badgeFg = TOKENS.colors.deepPine;
      } else if (tag.indexOf('ALTERNATIVAS') !== -1 || tag.indexOf('HIPÓTESE') !== -1) {
        badgeBg = { r: 0.93, g: 0.95, b: 0.98 };
        badgeFg = { r: 0.1, g: 0.3, b: 0.6 };
      } else if (tag.indexOf('TRADE-OFF') !== -1 || tag.indexOf('NÃO FOI') !== -1 || tag.indexOf('RESTRIÇÃO') !== -1 || tag.indexOf('DESCARTE') !== -1) {
        badgeBg = { r: 0.98, g: 0.93, b: 0.93 };
        badgeFg = { r: 0.65, g: 0.15, b: 0.15 };
      } else if (tag.indexOf('VALIDAÇÃO') !== -1 || tag.indexOf('RESULTADO') !== -1 || tag.indexOf('CONFORMIDADE') !== -1) {
        badgeBg = TOKENS.colors.acidLime;
        badgeFg = TOKENS.colors.deepPine;
      } else if (tag.indexOf('GESTALT') !== -1 || tag.indexOf('PROXIMIDADE') !== -1 || tag.indexOf('REGIÃO') !== -1) {
        badgeBg = TOKENS.colors.darkPine;
        badgeFg = TOKENS.colors.acidLime;
      }
      
      var card = createVerticalContainer('Decision Card: ' + tag, width, 8, { left: 24, right: 24, top: 16, bottom: 16 }, TOKENS.colors.card, TOKENS.colors.borderSubtle, 12, true);
      
      var cardHead = createHorizontalRow('Card Head', width - 48, 0, null, null, null, null, 'MIN', 'CENTER');
      var badgeNode = await createBadge(tag, badgeBg, badgeFg, false);
      cardHead.appendChild(badgeNode);
      card.appendChild(cardHead);
      
      var bodyNode = await createTextNode(body, 14, 'regular', TOKENS.colors.textPrimary, width - 48, null, 22);
      card.appendChild(bodyNode);
      
      container.appendChild(card);
    } else {
      var paraNode = await createTextNode(line, 16, 'regular', TOKENS.colors.textSecondary, width, null, 26);
      container.appendChild(paraNode);
    }
  }
  
  return container;
}

// ============================================================================
// CALLOUT TÉCNICO EXECUTIVO (COM CHECKMARKS E BORDA ACENTUADA)
// ============================================================================

async function createTechnicalCallout(titleText, impactText, width) {
  var callout = createVerticalContainer('Impacto Técnico & Governança', width, 14, { left: 28, right: 28, top: 22, bottom: 22 }, TOKENS.colors.subtle, TOKENS.colors.borderSubtle, 14, true);
  
  callout.strokes = [{ type: 'SOLID', color: TOKENS.colors.deepPine }];
  callout.strokeWeight = 1;
  try {
    callout.strokeLeftWeight = 4;
    callout.strokeRightWeight = 1;
    callout.strokeTopWeight = 1;
    callout.strokeBottomWeight = 1;
  } catch(e) {}
  
  var coHead = createHorizontalRow('Callout Head', width - 56, 12, null, null, null, null, 'MIN', 'CENTER');
  var coBadge = await createBadge('⚡ IMPACTO TÉCNICO & GOVERNANÇA', TOKENS.colors.deepPine, TOKENS.colors.acidLime, true);
  var coSub = await createTextNode('Evidências & Validação', 12, 'bold', TOKENS.colors.textSecondary);
  coHead.appendChild(coBadge);
  coHead.appendChild(coSub);
  callout.appendChild(coHead);
  
  var rawBullets = impactText || '•  Rastreabilidade total das evidências de campo e governança de design.\n•  Integração direta entre equipes multidisciplinares e requisitos de conformidade.';
  var bLines = rawBullets.split('\n');
  
  for (var b = 0; b < bLines.length; b++) {
    var bText = bLines[b].trim();
    if (!bText) continue;
    var cleanBullet = bText.replace(/^[•\-\✔\d\.]+\s*/, '').trim();
    
    var bRow = createHorizontalRow('Bullet ' + b, width - 56, 12, null, null, null, null, 'MIN', 'MIN');
    
    var checkNode = await createTextNode('✔', 12, 'bold', TOKENS.colors.deepPine);
    var checkPill = figma.createFrame();
    checkPill.name = 'Check';
    checkPill.resize(20, 20);
    checkPill.cornerRadius = 10;
    checkPill.fills = solidFill(TOKENS.colors.acidLime);
    checkPill.layoutMode = 'HORIZONTAL';
    checkPill.primaryAxisSizingMode = 'FIXED';
    checkPill.counterAxisSizingMode = 'FIXED';
    safeSetPrimaryAlign(checkPill, 'CENTER');
    safeSetCounterAlign(checkPill, 'CENTER');
    checkPill.appendChild(checkNode);
    bRow.appendChild(checkPill);
    
    var bDesc = await createTextNode(cleanBullet, 13, 'medium', TOKENS.colors.textPrimary, width - 56 - 32, null, 20);
    bRow.appendChild(bDesc);
    callout.appendChild(bRow);
  }
  
  return callout;
}

// ============================================================================
// SIDEBAR TOC EXECUTIVO (CARD ELEVADO COM ITEM 01 EM ESTADO ATIVO)
// ============================================================================

async function createSidebarTOC(chapters, activeIdx) {
  var sidebar = createVerticalContainer('Neste Case (Sidebar)', 264, 8, { left: 16, right: 16, top: 18, bottom: 18 }, TOKENS.colors.card, TOKENS.colors.borderSubtle, 16, true);
  
  var headRow = createHorizontalRow('Side Head', 232, 0, null, null, null, null, 'SPACE_BETWEEN', 'CENTER');
  var sideTitle = await createTextNode('ÍNDICE DO CASE', 11, 'bold', TOKENS.colors.textSecondary, null, null, 14, 1.0);
  var sideBadge = await createBadge((chapters ? chapters.length : 5) + ' ETAPAS', TOKENS.colors.subtle, TOKENS.colors.deepPine, false);
  headRow.appendChild(sideTitle);
  headRow.appendChild(sideBadge);
  sidebar.appendChild(headRow);

  var div0 = figma.createFrame();
  div0.name = 'Div';
  div0.resize(232, 1);
  div0.fills = solidFill(TOKENS.colors.borderSubtle);
  sidebar.appendChild(div0);

  for (var s = 0; s < chapters.length; s++) {
    var isActive = (s === (activeIdx || 0));
    var sItem = figma.createFrame();
    sItem.name = 'Item: ' + chapters[s].num;
    sItem.resize(232, 40);
    sItem.layoutMode = 'HORIZONTAL';
    sItem.primaryAxisSizingMode = 'FIXED';
    sItem.counterAxisSizingMode = 'AUTO';
    sItem.paddingLeft = 10;
    sItem.paddingRight = 10;
    sItem.paddingTop = 8;
    sItem.paddingBottom = 8;
    sItem.itemSpacing = 10;
    sItem.cornerRadius = 8;
    safeSetPrimaryAlign(sItem, 'MIN');
    safeSetCounterAlign(sItem, 'CENTER');
    
    if (isActive) {
      sItem.fills = solidFill(TOKENS.colors.subtle);
      sItem.strokes = [{ type: 'SOLID', color: TOKENS.colors.deepPine }];
      sItem.strokeWeight = 1;
      try {
        sItem.strokeLeftWeight = 3;
        sItem.strokeRightWeight = 0;
        sItem.strokeTopWeight = 0;
        sItem.strokeBottomWeight = 0;
      } catch(e) {}
    } else {
      sItem.fills = [];
    }

    var sNumPill = await createBadge(chapters[s].num, isActive ? TOKENS.colors.deepPine : TOKENS.colors.subtle, isActive ? TOKENS.colors.acidLime : TOKENS.colors.textSecondary, false);
    var sLabel = await createTextNode(chapters[s].short, 13, isActive ? 'bold' : 'regular', isActive ? TOKENS.colors.deepPine : TOKENS.colors.textPrimary, 168);
    sItem.appendChild(sNumPill);
    sItem.appendChild(sLabel);
    sidebar.appendChild(sItem);
  }
  return sidebar;
}


async function buildGenericCaseScreen(parent, xPos, yPos, caseData) {
  if (caseData.layoutV2) { return await buildCaseV2(parent, xPos, yPos, caseData); }
  log('Criando ' + caseData.name + ' com Grid Suíço Split-View e Gestalt 1:1...');
  
  var container = createVerticalContainer(
    caseData.frameName,
    1280,
    40,
    { left: 64, right: 64, top: 48, bottom: 80 },
    TOKENS.colors.canvas,
    null,
    null
  );
  container.x = xPos;
  container.y = yPos;

  // 1. Header do Site
  var header = await createHeaderBar(1152);
  container.appendChild(header);

  // 2. Voltar aos cases
  var backLink = await createTextNode('← Voltar aos cases', 15, 'regular', TOKENS.colors.textSecondary);
  container.appendChild(backLink);

  // 3. EXECUTIVE HERO EM SPLIT-VIEW (2 COLUNAS: CONTEXTO 530px + MASTER DELIVERABLE 590px)
  // Elimina imagens gigantes de 900px e coloca tudo visível acima da dobra!
  var heroSplitRow = createHorizontalRow('Hero Split-View (Acima da Dobra)', 1152, 32, null, null, null, null, 'SPACE_BETWEEN', 'CENTER');
  
  // 3.1 Coluna Esquerda do Hero: Headline, Contexto, Metadados e Métricas Rápidas (530px)
  var heroLeft = createVerticalContainer('Hero Contexto', 530, 16, null, null, null, null);
  
  var kickerFrame = createHorizontalRow('Kicker', 530, 12, null, null, null, null, 'MIN', 'CENTER');
  var kickerPill = await createBadge(caseData.kickerTag, TOKENS.colors.acidLime, TOKENS.colors.deepPine, true);
  var kickerSub = await createTextNode(caseData.kickerCompany, 13, 'regular', TOKENS.colors.textSecondary);
  kickerFrame.appendChild(kickerPill);
  kickerFrame.appendChild(kickerSub);
  heroLeft.appendChild(kickerFrame);

  var title = await createTextNode(caseData.title, 34, 'bold', TOKENS.colors.textPrimary, 530, null, 42, -0.8);
  heroLeft.appendChild(title);

  var subtitle = await createTextNode(caseData.subtitle, 15, 'regular', TOKENS.colors.textSecondary, 530, null, 24);
  heroLeft.appendChild(subtitle);

  // Metadados Compactos (3 Chips Elegantes)
  var metaRow = createHorizontalRow('Meta Row', 530, 8, null, null, null, null, 'SPACE_BETWEEN', 'MIN');
  var metaColW = (530 - 16) / 3;
  for (var m = 0; m < caseData.metadata.length; m++) {
    var mBox = createVerticalContainer('Meta: ' + caseData.metadata[m].label, metaColW, 2, { left: 10, right: 10, top: 8, bottom: 8 }, TOKENS.colors.card, TOKENS.colors.borderSubtle, 8);
    var mLbl = await createTextNode(caseData.metadata[m].label, 10, 'bold', TOKENS.colors.textSecondary, null, null, 12, 0.5);
    var mVal = await createTextNode(caseData.metadata[m].val, 12, 'semibold', TOKENS.colors.textPrimary, metaColW - 20, null, 16);
    mBox.appendChild(mLbl);
    mBox.appendChild(mVal);
    metaRow.appendChild(mBox);
    safeSetFill(mBox, 'VERTICAL');
  }
  heroLeft.appendChild(metaRow);

  // Destaque Executivo Acima da Dobra
  var heroGovStrip = createHorizontalRow('Hero Gov Strip', 530, 10, { left: 16, right: 16, top: 10, bottom: 10 }, TOKENS.colors.subtle, TOKENS.colors.borderSubtle, 10, 'SPACE_BETWEEN', 'CENTER');
  var govBadge = await createBadge('EVIDÊNCIAS AUDITADAS', TOKENS.colors.deepPine, TOKENS.colors.acidLime, true);
  var govTxt = await createTextNode('Padrão Sênior · Métricas ancoradas a baseline', 12, 'medium', TOKENS.colors.textSecondary);
  heroGovStrip.appendChild(govBadge);
  heroGovStrip.appendChild(govTxt);
  heroLeft.appendChild(heroGovStrip);

  heroSplitRow.appendChild(heroLeft);

  // 3.2 Coluna Direita do Hero: Master Deliverable (590 × 338 px, 16:9 - SEM 900px de altura!)
  var heroMediaContainer = createVerticalContainer('Hero Media Container', 590, 8, null, null, null, null);
  var heroImg = null;
  if (typeof caseData.customHeroBuilder === 'function') {
    heroImg = await caseData.customHeroBuilder(590, 338);
  } else if (caseData.useSalaryNowHero) {
    heroImg = await createSalaryNowHero(590, 338);
  } else {
    heroImg = await createRealImageFigure(caseData.heroImgKey, null, 590, 338, TOKENS.radius.card);
  }
  heroMediaContainer.appendChild(heroImg);
  if (caseData.heroCaption) {
    var hCap = await createTextNode(caseData.heroCaption, 11, 'regular', TOKENS.colors.textSecondary, 590, null, 16);
    heroMediaContainer.appendChild(hCap);
  }
  heroSplitRow.appendChild(heroMediaContainer);

  container.appendChild(heroSplitRow);

  // 4. BARRA DE MÉTRICAS AUDITADAS UNIFICADA (TODAS AS MÉTRICAS EM LINHA EQUILIBRADA)
  if (caseData.metrics && caseData.metrics.length > 0) {
    var mCount = caseData.metrics.length;
    var metricsFrame = createHorizontalRow('Métricas Auditadas 1:1', 1152, 16, null, null, null, null, 'SPACE_BETWEEN', 'MIN');
    var cardW = (1152 - (16 * (mCount - 1))) / mCount;
    for (var k = 0; k < mCount; k++) {
      var cardNode = await createMetricCard(caseData.metrics[k].n, caseData.metrics[k].d, cardW);
      metricsFrame.appendChild(cardNode);
      safeSetFill(cardNode, 'VERTICAL');
    }
    container.appendChild(metricsFrame);
  }

  // 5. SEÇÃO DE CAPÍTULOS EM SPLIT-VIEW (GRID DE 2 COLUNAS ALTERNADO COM GESTALT)
  // Cada capítulo é um card com região comum (1152px), unindo texto/decisões e deliverable lado a lado!
  for (var c = 0; c < caseData.chapters.length; c++) {
    var ch = caseData.chapters[c];
    var isReverse = (c % 2 === 1); // Alterna Z-pattern: ímpar normal, par invertido

    var splitCard = createHorizontalRow(
      'Capítulo ' + ch.num + ' · Split-View (' + (isReverse ? 'Reverse' : 'Standard') + ')',
      1152,
      32,
      { left: 32, right: 32, top: 28, bottom: 28 },
      (isReverse ? TOKENS.colors.subtle : TOKENS.colors.card),
      TOKENS.colors.borderSubtle,
      TOKENS.radius.card,
      'SPACE_BETWEEN',
      'MIN'
    );

    // Coluna de Conteúdo (504px)
    var contentCol = createVerticalContainer('Conteúdo & Decisões', 504, 14, null, null, null, null);
    
    var chBadge = await createBadge(ch.num + ' · ' + ch.tag, isReverse ? TOKENS.colors.deepPine : TOKENS.colors.subtle, isReverse ? TOKENS.colors.acidLime : TOKENS.colors.deepPine, false);
    contentCol.appendChild(chBadge);

    var chTitle = await createTextNode(ch.title, 22, 'bold', TOKENS.colors.textPrimary, 504, null, 30, -0.4);
    contentCol.appendChild(chTitle);

    var chContent = await renderStructuredContent(ch.p, 504);
    contentCol.appendChild(chContent);

    var callout = await createTechnicalCallout('IMPACTO TÉCNICO', ch.impactText, 504);
    contentCol.appendChild(callout);

    // Coluna de Mídia / Deliverable (552px × 310px, 16:9 - SEM IMAGEM GIGANTE!)
    var mediaCol = createVerticalContainer('Deliverable Evidência', 552, 8, null, null, null, null);
    var chImg = null;
    if (typeof ch.customBuilder === 'function') {
      chImg = await ch.customBuilder(552, 310);
    } else {
      chImg = await createRealImageFigure(ch.imgKey, null, 552, 310, TOKENS.radius.card);
    }
    mediaCol.appendChild(chImg);
    if (ch.caption) {
      var chCap = await createTextNode(ch.caption, 11, 'regular', TOKENS.colors.textSecondary, 552, null, 16);
      mediaCol.appendChild(chCap);
    }

    if (isReverse) {
      splitCard.appendChild(mediaCol);
      splitCard.appendChild(contentCol);
    } else {
      splitCard.appendChild(contentCol);
      splitCard.appendChild(mediaCol);
    }

    container.appendChild(splitCard);
  }

  // 6. Navegação Circular Entre Cases
  var navRow = createHorizontalRow('Navegação Circular Entre Cases', 1152, 24, null, null, null, null, 'SPACE_BETWEEN', 'MIN');
  var prevBox = createVerticalContainer('Card Anterior', (1152 - 24) / 2, 6, { left: 24, right: 24, top: 18, bottom: 18 }, TOKENS.colors.subtle, TOKENS.colors.borderSubtle, TOKENS.radius.card, true);
  var prevL = await createTextNode('← CASE ANTERIOR', 11, 'bold', TOKENS.colors.textSecondary, null, null, 14, 0.8);
  var prevT = await createTextNode(caseData.prevCaseTitle, 16, 'bold', TOKENS.colors.textPrimary);
  prevBox.appendChild(prevL);
  prevBox.appendChild(prevT);
  navRow.appendChild(prevBox);
  safeSetFill(prevBox, 'VERTICAL');

  var nextBox = createVerticalContainer('Próximo Case', (1152 - 24) / 2, 6, { left: 24, right: 24, top: 18, bottom: 18 }, TOKENS.colors.subtle, TOKENS.colors.borderSubtle, TOKENS.radius.card, true);
  var nextL = await createTextNode('PRÓXIMO CASE DA ESTEIRA →', 11, 'bold', TOKENS.colors.textSecondary, null, null, 14, 0.8);
  var nextT = await createTextNode(caseData.nextCaseTitle, 16, 'bold', TOKENS.colors.textPrimary);
  nextBox.appendChild(nextL);
  nextBox.appendChild(nextT);
  navRow.appendChild(nextBox);
  safeSetFill(nextBox, 'VERTICAL');
  container.appendChild(navRow);

  // 7. Footer Executivo
  var footer = figma.createFrame();
  footer.name = 'Footer';
  footer.resize(1152, 64);
  footer.layoutMode = 'HORIZONTAL';
  footer.primaryAxisSizingMode = 'FIXED';
  footer.counterAxisSizingMode = 'AUTO';
  safeSetPrimaryAlign(footer, 'SPACE_BETWEEN');
  safeSetCounterAlign(footer, 'CENTER');
  footer.clipsContent = false;
  footer.fills = [];
  var copy = await createTextNode('© Israel Rozar · Senior Product Designer · Sistemas Complexos, AI & Design Systems', 13, 'regular', TOKENS.colors.textSecondary);
  var topLink = await createTextNode('Voltar ao topo ↑', 13, 'semibold', TOKENS.colors.textPrimary);
  footer.appendChild(copy);
  footer.appendChild(topLink);
  container.appendChild(footer);

  container.primaryAxisSizingMode = 'AUTO';
  container.clipsContent = false;

  parent.appendChild(container);
  log('✔ ' + caseData.name + ' criado com sucesso em Grid Split-View 1:1!');
  return container;
}
"""

js_data_and_home = r"""
// ============================================================================
// DADOS DO CASE TEMPLATE OFICIAL (REUTILIZÁVEL E MODULAR)
// ============================================================================
var CASE_TEMPLATE = {
  name: 'Case Template Oficial',
  frameName: 'Template · Case de Estudo (Grid Suíço 1:1)',
  kickerTag: 'SETOR · DISCIPLINA DE DESIGN',
  kickerCompany: 'Nome da Organização · Contexto / Área · Ano',
  title: 'Título principal do estudo de caso: impacto sistêmico e solução técnica.',
  subtitle: 'Resumo executivo do problema, contexto regulatório ou operacional e metodologia adotada para geração de valor com design.',
  metadata: [
    { label: 'MEU PAPEL', val: 'Senior / Lead Product Designer' },
    { label: 'EQUIPE', val: 'Design, Engenharia, Produto e Especialistas do Domínio' },
    { label: 'ESCOPO', val: 'Discovery, Arquitetura da Informação, Design System e Testes' }
  ],
  customHeroBuilder: buildTemplateHeroBlueprint,
  heroCaption: 'Figura 01 · Visão geral do produto ou ecossistema em produção (evidência canônica 16:9).',
  metrics: [
    { n: '100k+', d: 'usuários ou operações impactadas' },
    { n: '40%', d: 'redução de tempo ou atrito operacional' },
    { n: 'AA/AAA', d: 'conformidade com normas de acessibilidade' },
    { n: '1:1', d: 'paridade entre design e engenharia' }
  ],
  prevCaseTitle: 'Hospital Albert Einstein · Laudos Clínicos',
  nextCaseTitle: 'Itaú Unibanco · Hub de Liquidez B2B',
  chapters: [
    {
      num: '01',
      tag: 'ENQUADRAMENTO DO PROBLEMA & REENQUADRAMENTO (REFRAMING)',
      short: '01 · Reenquadramento',
      title: 'Desafio do briefing original versus o problema real de arquitetura e negócio.',
      customBuilder: buildTemplateCh1Schematic,
      caption: 'Mapeamento de causa-raiz e redirecionamento de briefing com base em evidências.',
      p: 'O briefing inicial solicitava a criação de novas telas operacionais cosméticas. A investigação técnica demonstrou que a causa-raiz da fricção era estrutural: inconsistência no modelo de dados e ausência de taxonomia unificada. O escopo foi redirecionado com dados para atacar o gargalo sistêmico.\n• Gatilho: Inconsistência nos fluxos de entrada gerava 42% de retrabalho na equipe de suporte.\n• Alternativas: Criação de telas pontuais vs reestruturação taxonômica unificada.\n• Trade-off Aceito: Prazo inicial estendido em 2 semanas em prol de estabilidade sistêmica permanente.\n• Restrição Operacional: Integração com microfrontends e APIs de telemetria legadas sem quebra de contrato.\n• Validação: Redirecionamento aprovado por unanimidade por liderança de Produto e Engenharia.',
      impactText: '•  Reenquadramento estratégico que evitou meses de retrabalho em soluções cosméticas.\n•  Alinhamento executivo com líderes de produto, engenharia e conformidade regulatória.'
    },
    {
      num: '02',
      tag: 'DECISÃO 01: ARQUITETURA DA INFORMAÇÃO & MODELO MENTAL',
      short: '02 · Decisão 01: AI',
      title: 'Redução de carga cognitiva: Gatilho, Alternativas e Trade-offs.',
      customBuilder: buildTemplateCh2Schematic,
      caption: 'Blueprint da nova arquitetura e modelo conceitual de interface.',
      p: '• Gatilho: 80% das interações sofriam bloqueios por sobrecarga informacional em tabelas não hierarquizadas.\n• Alternativas: Fluxo linear profundo (5 etapas) vs Visão modular contextual com painéis de apoio.\n• Trade-off Aceito: Menor densidade inicial de dados em prol de previsibilidade e erro operacional zero.\n• Restrição Operacional: Suporte a telas de baixa resolução (1366x768) de operadores de campo.\n• Validação: Testes de usabilidade com especialistas do domínio demonstrando 100% de sucesso nas tarefas críticas.',
      impactText: '•  Estruturação taxonômica com redução de níveis de navegação de 5 para 2.\n•  Contratos de interface rigorosos validados em conjunto com engenharia.'
    },
    {
      num: '03',
      tag: 'DECISÃO 02: DESIGN SYSTEM & PARIDADE 1:1',
      short: '03 · Decisão 02: DS',
      title: 'Componentização de alta escala e conformidade WCAG 2.2 AAA.',
      customBuilder: buildTemplateCh3Schematic,
      caption: 'Matriz de componentes modulares com suporte a temas e tokens semânticos.',
      p: '• Gatilho: Divergência visual crônica entre artefatos de design e código em produção (drift de componentes).\n• Alternativas: Estilos locais em cada repositório vs biblioteca canônica de tokens semânticos (DTCG).\n• Trade-off Aceito: Alocação de 3 semanas de refatoração de base para ganho permanente de velocidade.\n• Restrição Operacional: Garantir contraste triplo (AAA > 12:1) em temas claro e escuro para operadores sob estresse visual prolongado.\n• Validação: Auditoria automatizada de paridade via CI/CD com 0 regressões visuais.',
      impactText: '•  Tokens semânticos de espaçamento (base 8px) e tipografia unificada.\n•  Eliminação de débito técnico e aceleração comprovada no ciclo de handoff.'
    },
    {
      num: '04',
      tag: 'DISCIPLINA DE ESCOPO & DESACORDO CONSTRUTIVO',
      short: '04 · Escopo & Conflito',
      title: 'O que NÃO foi construído e a resolução de tensões multidisciplinares.',
      customBuilder: buildTemplateCh4Schematic,
      caption: 'Registro de escopo deliberadamente cortado e validação funcional.',
      p: '• O Que NÃO Foi Construído: Descarte deliberado de filtros aninhados avançados que aumentavam latência técnica e propensão a erros de operador. A decisão priorizou busca assistida e visualização agregada.\n• Desacordo Construtivo: A engenharia propôs reutilizar tabelas existentes por prazo; demonstrei com protótipo funcional e custo projetado de suporte que o retrabalho seria maior. Pactuamos uma entrega em fases sem degradar a usabilidade.\n• Resolução Pragmática: Implementação faseada que atendeu à janela de release de compliance mantendo o padrão visual.',
      impactText: '•  Preservação do foco estratégico sob pressão de prazos concorrentes.\n•  Cultura de debate técnico fundamentado em evidências e prototipagem rápida.'
    },
    {
      num: '05',
      tag: 'IMPACTO DE NEGÓCIO & REFLEXÃO CRÍTICA',
      short: '05 · Impacto & Reflexão',
      title: 'Resultados auditados por Receita, Custo e Risco, com aprendizados honestos.',
      customBuilder: buildTemplateCh5Schematic,
      caption: 'Métricas de negócio consolidadas pós-lançamento e reflexão de melhoria.',
      p: '• Impacto de Custo & Operação: -38% no tempo médio de atendimento e -45% de chamados de suporte técnico.\n• Redução de Risco: Zero inconformidades regulatórias e 100% de rastreabilidade de dados.\n• Reflexão Crítica (O Que Faria Diferente Hoje): Teria integrado a equipe de telemetria duas semanas antes para instrumentar eventos de microinteração com maior granularidade desde o primeiro teste de campo.',
      impactText: '•  Evidências quantitativas ancoradas a baselines históricos consolidados.\n•  Maturidade executiva comprovada em avaliação e melhoria contínua.'
    }
  ]
};

var CASE_NEOENERGIA = {
  name: 'Case Neoenergia',
  frameName: 'Case · Neoenergia — Service Design & P&D ANEEL',
  kickerTag: 'ENERGIA · SERVICE DESIGN',
  kickerCompany: 'Neoenergia · EY × Livework · P&D ANEEL · 2020',
  title: 'Conectar a jornada digital ao serviço que acontece no mundo físico.',
  subtitle: 'Discovery e service design para organizar problemas, jornadas e oportunidades no atendimento de distribuidoras de energia.',
  metadata: [
    { label: 'MEU PAPEL', val: 'Senior Product Designer / Service Designer' },
    { label: 'EQUIPE', val: 'EY Business Transformation × Livework e áreas da Neoenergia' },
    { label: 'ESCOPO', val: 'Pesquisa, jornadas atuais, blueprints e visão futura de serviço' }
  ],
  heroImgKey: 'neo_capa',
  heroCaption: 'Projeto P&D Conexão Digital ANEEL: Experiência do Consumidor e Service Design para o Grupo Neoenergia (Iberdrola Brasil).',
  metrics: [
    { n: '34M', d: 'habitantes nas concessões' },
    { n: '13,9M', d: 'clientes faturados' },
    { n: '4', d: 'distribuidoras unificadas' },
    { n: '5', d: 'blueprints de serviço' },
    { n: '118', d: 'ideias na matriz de valor' }
  ],
  prevCaseTitle: 'Claro Brasil · Ativação simplificada',
  nextCaseTitle: 'Albert Einstein · Laudos clínicos',
  chapters: [
    {
      num: '01',
      tag: 'CONTEXTO MACRO & ESCALA',
      short: 'Unificação da infraestrutura',
      title: 'Unificação da infraestrutura de atendimento para 34 milhões de pessoas.',
      imgKey: 'neo_num',
      caption: 'Escala do ecossistema: integração de Elektro (SP/MS), Coelba (BA), Celpe (PE) e Cosern (RN) em 18 estados.',
      p: 'Iniciativa de discovery e transformação de serviços para conectar canais de atendimento, processos internos e experiência do consumidor de energia para o Grupo Neoenergia (Iberdrola Brasil), integrando 4 grandes distribuidoras sob regulação rígida da ANEEL.'
    },
    {
      num: '02',
      tag: 'ECOSSISTEMA & MULTICANALIDADE',
      short: 'Cadeia de serviços fragmentada',
      title: 'Cadeia de serviços fragmentada em um ecossistema de infraestrutura crítica.',
      imgKey: 'neo_canais',
      caption: 'Ecossistema de canais: mapeamento dos 11 pontos de contato entre consumidores, concessionárias e equipes operacionais de campo.',
      p: 'O diagnóstico mapeou a jornada do consumidor através de 11 pontos de contato — desde o atendimento presencial em agências e postos credenciados até canais digitais (portal web, aplicativo móvel, SMS, WhatsApp e call center) e equipes de campo.'
    },
    {
      num: '03',
      tag: 'DIAGNÓSTICO & AUDITORIA OPERACIONAL',
      short: 'Auditoria de backstage',
      title: 'Auditoria de backstage: quando a insatisfação com a fatura revela silos operacionais.',
      imgKey: 'neo_bp1',
      caption: 'Auditoria de backstage: detalhe em alta resolução do Blueprint conectando a experiência do cliente aos sistemas e equipes de campo.',
      p: 'A leitura de Service Design evita reduzir o diagnóstico a interfaces de tela: a insatisfação com a fatura raramente é um problema visual, decorrendo de regras de negócio obscuras, leituras por estimativa ou falta de sincronização entre o despacho técnico e o faturamento.'
    },
    {
      num: '04',
      tag: 'DESBUROCRATIZAÇÃO & DESIGN SYSTEM',
      short: 'Desburocratização de backoffice',
      title: 'Desburocratização de backoffice antes de redesenho de portal e Design System multi-tenant.',
      imgKey: 'neo_ds',
      caption: 'Design System Multi-tenant: componentes modulares e esteira de autosserviço padronizada para as 4 distribuidoras do grupo.',
      p: 'Antes de projetar qualquer tela, eliminamos barreiras burocráticas em serviços críticos (troca de titularidade, pedido de ligação nova e autoleitura), desenhando a fundação de um Design System Multi-tenant com temas dedicados para as 4 distribuidoras.'
    },
    {
      num: '05',
      tag: 'ARQUITETURA DE SERVIÇOS TO-BE',
      short: 'Os 5 estágios em blueprints',
      title: 'Os 5 estágios do ciclo de vida do cliente mapeados em Service Blueprints.',
      imgKey: 'neo_tobe',
      caption: 'Jornada To-Be e blueprints de serviço: os 5 estágios do ciclo de vida estruturados com ações do cliente e processos de backstage.',
      p: 'Para superar a fragmentação histórica entre as 4 distribuidoras, consolidamos a jornada completa do consumidor em 5 macroestágios com especificações detalhadas de frontstage, backstage e sistemas de apoio.'
    },
    {
      num: '06',
      tag: 'PRIORIZAÇÃO & ROADMAP ESTRATÉGICO',
      short: 'Matriz de 118 ideias priorizadas',
      title: 'Matriz de 118 ideias priorizadas e baseline para o plano diretor de inovação.',
      imgKey: 'neo_matriz',
      caption: 'Matriz de Priorização: 118 ideias estruturadas e classificadas por impacto no negócio versus valor percebido pelo consumidor.',
      p: 'As oportunidades mapeadas durante a pesquisa de campo e a auditoria de processos foram organizadas em uma matriz analítica, cruzando o valor percebido pelo consumidor com o esforço operacional de implementação.'
    },
    {
      num: '07',
      tag: 'FONTES & GOVERNANÇA EXECUTIVA',
      short: 'Fontes oficiais e equipe',
      title: 'Fontes oficiais de P&D ANEEL, governança executiva e equipe EY × Livework.',
      imgKey: 'neo_capa',
      caption: 'Governança executiva: entregáveis multidisciplinares aprovados pelas diretorias de operação do Grupo Neoenergia.',
      p: 'Os blueprints de serviço e a matriz de 118 oportunidades serviram como baseline estratégico aprovado pelas diretorias de operação e atendimento do Grupo Neoenergia no âmbito do programa de P&D Estratégico ANEEL.'
    }
  ]
};

var CASE_EINSTEIN = {
  name: 'Case Albert Einstein',
  frameName: 'Case · Albert Einstein — Linguagem Visual para Laudos Clínicos',
  kickerTag: 'SAÚDE · UX LEAD',
  kickerCompany: 'Hospital Israelita Albert Einstein × Foursys · 2022',
  title: 'Uma linguagem visual modular para laudos clínicos heterogêneos.',
  subtitle: 'Sistematização de 14 famílias de laudos, matriz de componentes escalável e pesquisa com 121 participantes para visualização rápida de parâmetros críticos.',
  metadata: [
    { label: 'MEU PAPEL', val: 'UX Lead / Product Designer' },
    { label: 'EQUIPE', val: 'Foursys Design × Equipe Médica e Engenharia Einstein' },
    { label: 'ESCOPO', val: 'Pesquisa clínica, taxonomia, Design System e prototipagem' }
  ],
  heroImgKey: 'hiae_capa',
  heroCaption: 'Hospital Israelita Albert Einstein: padronização visual e arquitetura da informação para exames diagnósticos de alta complexidade.',
  metrics: [
    { n: '14', d: 'famílias de laudos' },
    { n: '121', d: 'participantes em pesquisa' },
    { n: '80+', d: 'laudos no inventário' },
    { n: 'AA/AAA', d: 'conformidade WCAG' },
    { n: '1:1', d: 'paridade com protótipo v3' }
  ],
  prevCaseTitle: 'Neoenergia · Service Design & P&D ANEEL',
  nextCaseTitle: 'Itaú Unibanco · Plataforma Íon',
  chapters: [
    {
      num: '01',
      tag: 'PROPOSTA DE SOLUÇÃO CANÔNICA',
      short: 'Layout real da proposta v3',
      title: 'A anatomia de um laudo clínico: clareza imediata sem simplificar dados vitais.',
      imgKey: 'hiae_tablet',
      caption: 'Layout Real da Proposta v3: visualização em tablet com cabeçalho clínico, parâmetros críticos e histórico evolutivo.',
      p: 'A solução v3 estabelece uma hierarquia visual que prioriza o diagnóstico conclusivo, permitindo ao médico identificar anomalias em segundos enquanto mantém o paciente seguro e contextualizado sobre faixas de referência.'
    },
    {
      num: '02',
      tag: 'TAXONOMIA & ANATOMIA CLÍNICA',
      short: 'Taxonomia de macroáreas',
      title: 'Estruturação taxonômica em 3 macroáreas para suportar exames heterogêneos.',
      imgKey: 'hiae_taxonomia',
      caption: 'Taxonomia modular: decomposição de 80+ exames nas três macroáreas clínicas (Metodologia, Resultado e Conclusão Diagnóstica).',
      p: 'Para acomodar a diversidade entre um hemograma e uma ressonância magnética, estruturamos contratos de dados em 3 macroáreas canônicas: Metodologia, Resultado e Conclusão Diagnóstica.'
    },
    {
      num: '03',
      tag: 'PESQUISA & TRIANGULAÇÃO',
      short: 'Triangulação com médicos e pacientes',
      title: 'Pesquisa quantitativa e entrevistas em profundidade com corpo clínico.',
      imgKey: 'hiae_triangulacao',
      caption: 'Triangulação metodológica: cruzamento de percepções entre 4 entrevistas semiestruturadas com médicos e questionário com 121 pacientes.',
      p: 'A pesquisa triangulou 4 entrevistas semiestruturadas com médicos laudadores e 121 respostas de pacientes. Nos testes com a proposta, 81,6% reconheceram o documento como laudo médico e 77,8% concentraram a atenção no exame, resultado e referência.'
    },
    {
      num: '04',
      tag: 'DESIGN SYSTEM & TOKENS',
      short: 'Tokens e tipografia médica',
      title: 'Tokens semânticos de espaçamento 8px e tipografia calibrada para legibilidade rápida.',
      imgKey: 'hiae_tokens',
      caption: 'Design Tokens: escala tipográfica e cores de alerta (estável, limítrofe, crítico) rigorosamente testadas contra WCAG AAA.',
      p: 'Criamos tokens de cor dedicados aos estados clínicos, garantindo que indicadores de risco não dependam exclusivamente de cor (atendendo ao critério WCAG 1.4.1 de uso da cor).'
    },
    {
      num: '05',
      tag: 'MATRIZ DE COMPONENTES',
      short: 'Componentes modulares de laudo',
      title: 'Componentização escalável para suportar centenas de exames laboratoriais.',
      imgKey: 'hiae_componentes',
      caption: 'Matriz de Componentes: blocos reutilizáveis para tabelas analíticas, gráficos de dispersão e assinaturas digitais.',
      p: 'A biblioteca modular permitiu aos times de engenharia montar qualquer família de laudo combinando apenas 6 componentes mestres pré-validados com o corpo clínico.'
    },
    {
      num: '06',
      tag: 'VISÃO FUTURA & MULTIDISPOSIÇÃO',
      short: 'Visão futura de exames por imagem',
      title: 'Extensão do modelo para laudos de alta densidade e exames de imagem.',
      imgKey: 'hiae_visao_futura',
      caption: 'Visão Futura: aplicação do chassi modular em exames de ressonância magnética e tomografia computadorizada.',
      p: 'O mesmo sistema modular foi estendido para acomodar laudos de imagem, incorporando visualizadores DICOM integrados e cortes anatômicos sem quebrar a coerência visual do hospital.'
    },
    {
      num: '07',
      tag: 'GOVERNANÇA & IMPACTO',
      short: 'Governança clínica e síntese',
      title: 'Entrega aprovada pela diretoria clínica e handoff técnico para engenharia.',
      imgKey: 'hiae_capa',
      caption: 'Handoff executivo: especificação técnica completa entregue para implantação no ecossistema digital do Einstein.',
      p: 'O projeto estabeleceu o padrão oficial para a apresentação de resultados diagnósticos no portal e aplicativo do Einstein, servindo como referência de humanização de dados médicos na América Latina.'
    }
  ]
};

var CASE_ITAU = {
  name: 'Case Itaú Unibanco',
  frameName: 'Case · Itaú Unibanco — Plataforma Íon for Advisors',
  kickerTag: 'FINTECH · SENIOR PRODUCT DESIGNER',
  kickerCompany: 'Itaú Unibanco · Plataforma íon for Advisors · 2024–2026',
  title: 'Cinco recortes de produto para mesas de investimento de alta complexidade.',
  subtitle: 'Plataforma para especialistas de investimentos organizando saldos, projeções, vencimentos, movimentações e campanhas em alta densidade.',
  metadata: [
    { label: 'MEU PAPEL', val: 'Senior Product Designer' },
    { label: 'EQUIPE', val: 'Design, Produto, Engenharia e áreas de negócio' },
    { label: 'ESCOPO', val: 'Hub de liquidez, vencimentos, movimentações, campanhas e registros' }
  ],
  heroImgKey: 'itau_vencimentos',
  heroCaption: 'Itaú Unibanco íon for Advisors: suíte integrada para especialistas de investimentos com dados sintetizados para conformidade com o sigilo bancário.',
  metrics: [
    { n: '5', d: 'recortes de produto' },
    { n: 'IFA', d: 'plataforma de assessoria' },
    { n: 'LGPD', d: 'dados sintetizados' },
    { n: '100%', d: 'paridade com Design System' },
    { n: 'B2B', d: 'especialistas de investimentos' }
  ],
  prevCaseTitle: 'Albert Einstein · Laudos clínicos',
  nextCaseTitle: 'Claro Brasil · Ativação simplificada',
  chapters: [
    {
      num: '01',
      tag: 'VISÃO SISTÊMICA & DISCOVERY',
      short: 'Hub de Liquidez e Oportunidades',
      title: 'Hub de Liquidez: consolidando posição financeira e saldo projetado.',
      imgKey: 'itau_hub',
      caption: 'Hub de Liquidez: visão unificada de saldos em conta, resgates provisionados e oportunidades de reinvestimento.',
      p: 'O Hub de Liquidez resolveu um gargalo crítico dos assessores: a necessidade de abrir 4 sistemas legados diferentes para calcular o saldo disponível real de um cliente corporativo ou investidor qualificado.'
    },
    {
      num: '02',
      tag: 'OPERAÇÃO FINANCEIRA',
      short: 'Gestão de Vencimentos',
      title: 'Gestão de Vencimentos: transformando eventos passivos em relacionamento proativo.',
      imgKey: 'itau_vencimentos',
      caption: 'Gestão de Vencimentos: calendário inteligente alertando sobre vencimentos de títulos de renda fixa e fundos.',
      p: 'Projetamos uma interface analítica que antecipa em até 30 dias os vencimentos de CDBs, LCIs e debêntures, sugerindo automaticamente produtos da mesma classe para reter o capital dentro da instituição.'
    },
    {
      num: '03',
      tag: 'ARQUITETURA DA INFORMAÇÃO',
      short: 'Movimentações e Extrato unificado',
      title: 'Transição suave entre histórico transacional e saldo provisionado.',
      imgKey: 'itau_movimentacoes',
      caption: 'Movimentações e Extrato: arquitetura clara separando lançamentos consolidados de liquidações pendentes.',
      p: 'A arquitetura foi redesenhada para dar total previsibilidade ao fluxo de caixa, com filtros contextuais por classe de ativo e agrupamentos cronológicos inteligentes.'
    },
    {
      num: '04',
      tag: 'OPERAÇÃO EM LOTE',
      short: 'Gestão de Campanhas',
      title: 'Configuração de campanhas e comunicação segmentada com investidores.',
      imgKey: 'itau_campanhas',
      caption: 'Gestão de Campanhas: esteira administrativa permitindo ao assessor disparar propostas personalizadas para centenas de clientes.',
      p: 'Estruturamos a parametrização em lote com estados explícitos de processamento da base, filtros dinâmicos por carteira e rastreabilidade operacional entre preparação, execução e acompanhamento.'
    },
    {
      num: '05',
      tag: 'IA APLICADA & DOCUMENTAÇÃO',
      short: 'Registros de Atendimento com IA',
      title: 'Resumos assistidos por inteligência artificial com supervisão humana rigorosa.',
      imgKey: 'itau_registros',
      caption: 'Registros de Atendimento: transcrição e sumarização de reuniões com clientes, extraindo tarefas e notas de conformidade.',
      p: 'Implementamos fluxos assistidos por IA que geram minutas automáticas de reuniões, permitindo ao assessor revisar e validar em segundos as diretrizes acordadas com o investidor.'
    }
  ]
};

var CASE_CLARO = {
  name: 'Case Claro Brasil',
  frameName: 'Case · Claro Brasil — Ativação Simplificada e Jornada Multicanal',
  kickerTag: 'TELECOM · UX CORPORATIVO',
  kickerCompany: 'Claro Brasil · Operações Comerciais · 2017–2018',
  title: 'Simplificando o atendimento comercial em múltiplos canais.',
  subtitle: 'Mapeamento de 22 jornadas de atendimento, 20 pessoas em imersão, 10 entrevistas e esteira unificada para equipes de vendas em lojas e televendas.',
  metadata: [
    { label: 'MEU PAPEL', val: 'UX/UI Designer' },
    { label: 'EQUIPE', val: 'Equipe de Operações e Transformação Digital Claro' },
    { label: 'ESCOPO', val: 'Pesquisa, jornadas, prototipação e interfaces televendas/lojas' }
  ],
  heroImgKey: 'claro_capa',
  heroCaption: 'Claro Brasil: redesenho integral do sistema de ativação de planos móveis e combos para televendas e balcão.',
  metrics: [
    { n: '22', d: 'jornadas mapeadas' },
    { n: '20', d: 'pessoas em imersão' },
    { n: '10', d: 'entrevistas em profundidade' },
    { n: '70+', d: 'validações e testes' },
    { n: '2', d: 'canais unificados (web e mobile)' }
  ],
  prevCaseTitle: 'Itaú Unibanco · Plataforma Íon',
  nextCaseTitle: 'Neoenergia · Service Design & P&D ANEEL',
  chapters: [
    {
      num: '01',
      tag: 'OPERAÇÃO COMERCIAL & ATIVAÇÃO',
      short: 'Ativação Simplificada e checkout',
      title: 'Redesenho da esteira de ativação para dar clareza financeira e continuidade entre canais.',
      imgKey: 'claro_ativacao',
      caption: 'Ativação Simplificada: interface desktop para operadores com resumo financeiro visível e validação cadastral imediata.',
      p: 'Unificamos a navegação progressiva com resumo da oferta sempre visível, preservando o contexto do cliente entre consulta por CPF, escolha do plano e confirmação.'
    },
    {
      num: '02',
      tag: 'PESQUISA & JORNADAS',
      short: 'Mapeamento de 22 jornadas',
      title: 'Imersão em lojas físicas e centrais de televendas.',
      imgKey: 'claro_jornadas',
      caption: 'Mapeamento de Jornadas: identificação de atritos desde a consulta do cliente até a confirmação da oferta.',
      p: 'Conduzimos imersão com 20 profissionais e 10 entrevistas em profundidade, mapeando 22 jornadas para compreender gargalos reais entre sistemas legados e o atendimento comercial.'
    },
    {
      num: '03',
      tag: 'OMNICANALIDADE',
      short: 'Multicanalidade web e lojas',
      title: 'Conectando a jornada iniciada na web com o fechamento na loja física.',
      imgKey: 'claro_multicanal',
      caption: 'Multicanalidade: carrinho persistente permitindo ao cliente salvar a proposta online e retirar o chip no balcão.',
      p: 'Eliminamos a perda de propostas criando um identificador único de carrinho, permitindo ao atendente da loja física resgatar instantaneamente os dados já preenchidos pelo consumidor.'
    },
    {
      num: '04',
      tag: 'CO-CRIAÇÃO & GOVERNANÇA',
      short: 'Workshops e validação contínua',
      title: 'Validação semanal com equipes de campo para garantir viabilidade operacional.',
      imgKey: 'claro_workshop',
      caption: 'Co-criação: testes de usabilidade com operadores de televendas reduzindo taxa de erros em digitação de contratos.',
      p: 'Cada tela projetada foi testada diretamente nos postos de atendimento sob pressão de metas comerciais, assegurando que os novos atalhos acelerassem o fechamento de planos.'
    }
  ]
};

// ============================================================================
// DADOS DO CASE SALARYNOW (FINTECH B2B2C · FRAMEWORK STAR · PM3)
// ============================================================================
var CASE_SALARYNOW = {
  layoutV2: true,
  name: 'Case SalaryNow (STAR Framework)',
  frameName: 'Case · SalaryNow — Antecipação salarial (STAR)',
  kickerTag: 'Fintech B2B2C · Produto e UX',
  kickerCompany: 'SalaryNow · Desafio prático PM3 · 2026',
  title: 'Taxa em reais antes da confirmação: ativação de 32% para 59%.',
  subtitle: 'Estratégia de produto e redesenho da tela de confirmação de uma antecipação salarial B2B2C, organizado em Situação, Tarefa, Ação e Resultado.',
  metadata: [
    { label: 'Meu papel', val: 'Product Manager e Senior Product Designer' },
    { label: 'Equipe', val: '2 PMs, 1 designer e 6 desenvolvedores' },
    { label: 'Métodos', val: 'STAR, 4 riscos de produto, Gestalt, WCAG 2.2' }
  ],
  heroFigure: snHeroSimulator,
  heroCaption: 'Tela de confirmação redesenhada: valor recebido, taxa em reais e salário previsto antes do botão de confirmar.',
  metrics: [
    { n: '32% → 59%', d: 'ativação dos colaboradores cadastrados' },
    { n: '68% → 19%', d: 'abandono entre o saldo e a confirmação' },
    { n: '74% → 78%', d: 'uso repetido no mês seguinte' },
    { n: '1,8 → 2,3', d: 'antecipações por usuário ativo por mês' },
    { n: '-63%', d: 'chamados de suporte sobre taxas' }
  ],
  prevCaseTitle: 'Hospital Albert Einstein · Laudos clínicos',
  nextCaseTitle: 'Itaú Unibanco · Plataforma Íon',
  chapters: [
    {
      num: '01', tag: 'Situação', short: '01 · Situação',
      title: 'Muitos cadastros, poucas primeiras antecipações.',
      figure: snFunnel,
      caption: 'Funil de ativação na linha de base: a perda se concentrava antes da primeira operação.',
      p: 'A SalaryNow oferece antecipação salarial como benefício corporativo: a empresa contrata o serviço e o colaborador antecipa parte do salário pagando uma taxa.\n• O que os dados mostravam: 74% de quem fazia a primeira antecipação voltava a usar no mês seguinte. O serviço tinha valor para quem experimentava.\n• Onde estava o problema: 68% dos cadastrados nunca concluíam a primeira operação. A maior perda acontecia entre a tela de saldo e a tela de confirmação.\n• Quem é o usuário: colaboradores de 25 a 45 anos, com renda de R$ 2 mil a R$ 6 mil, em varejo, logística e serviços. Usam apps de banco, mas têm receio de taxas escondidas e de dívidas.',
      calloutTitle: 'Restrições',
      impactText: '• Equipe: 2 PMs, 1 designer e 6 desenvolvedores, sem time dedicado de dados.\n• Regulação: toda condição financeira precisa seguir as regras do Banco Central.'
    },
    {
      num: '02', tag: 'Tarefa', short: '02 · Tarefa',
      title: 'Escolher uma única frente para os próximos 6 a 12 meses.',
      figure: snRiskMatrix,
      caption: 'Avaliação dos três produtos pelos 4 riscos de produto de Marty Cagan.',
      p: 'A empresa tinha três produtos: Antecipação salarial, Cartão de benefícios e Portal do RH. Avaliei cada um pelos 4 riscos de produto: valor, usabilidade, viabilidade técnica e negócio.\n• Antecipação salarial: risco de valor baixo (74% de recorrência) e risco de usabilidade alto (68% de abandono). É a principal fonte de receita.\n• Cartão de benefícios: riscos altos de valor, usabilidade e viabilidade. A adesão estava fraca havia 4 meses.\n• Portal do RH: os gestores não conheciam a ferramenta, e o uso dependia da adesão dos colaboradores.\n• Decisão: concentrar o time na Antecipação salarial, com meta de levar a ativação de 32% para 55% ou mais.',
      calloutTitle: 'Critérios da decisão',
      impactText: '• Impacto direto na margem de contribuição.\n• Viável com a capacidade atual de 6 desenvolvedores.'
    },
    {
      num: '03', tag: 'Ação · Interface', short: '03 · Ação',
      title: 'Mostrar o custo em reais antes da confirmação.',
      figure: snBeforeAfter,
      caption: 'Antes, a taxa aparecia em percentual. Depois, o custo e o efeito no salário aparecem em reais.',
      p: 'Os dados de uso e as entrevistas apontaram a desconfiança na taxa como a principal causa do abandono. O redesenho da tela de confirmação tratou esse ponto.\n• Região comum (Gestalt): o valor recebido hoje e o valor descontado no próximo salário ficam em blocos separados, cada um com fundo próprio.\n• Proximidade (Gestalt): a taxa aparece ao lado do valor pedido, em reais (taxa única de R$ 12,00), e não em percentual.\n• Prévia do salário: a tela mostra o salário do mês seguinte já com o desconto (R$ 3.000 - R$ 300 - R$ 12 = R$ 2.688).',
      calloutTitle: 'Critérios aplicados',
      impactText: '• Visibilidade do status do sistema (Nielsen): os valores se atualizam a cada mudança no valor escolhido.\n• Banco Central: todas as condições aparecem antes do botão de confirmação.'
    },
    {
      num: '04', tag: 'Ação · Escopo', short: '04 · Escopo',
      title: 'Definir o que fica fora do escopo e envolver o RH.',
      figure: snScopeBoard,
      caption: 'Itens priorizados e itens adiados, com o motivo de cada corte.',
      p: '• Fora do escopo: novas funções do Cartão de benefícios e crédito rotativo. Dividir 6 desenvolvedores em duas frentes atrasaria as duas e aumentaria o risco regulatório.\n• Divergência com a área comercial: a área pedia cashback e gamificação. Mostrei com os dados do funil que adicionar recursos antes de resolver a confiança na taxa tenderia a aumentar o abandono. A prioridade foi mantida.\n• Portal do RH: deixou de ser apenas cadastro e passou a mostrar indicadores agregados e anônimos de uso do benefício, em conformidade com a LGPD.',
      calloutTitle: 'Resultado desta etapa',
      impactText: '• O RH passou a divulgar o benefício nas unidades, com apoio presencial no cadastro.\n• Os pedidos de telas personalizadas por cliente caíram 40%.'
    },
    {
      num: '05', tag: 'Resultado', short: '05 · Resultado',
      title: 'Resultados em 8 meses e o que eu faria diferente.',
      figure: snResults,
      caption: 'Indicadores medidos 8 meses após o lançamento, comparados à linha de base.',
      p: 'Os indicadores foram medidos 8 meses após o lançamento e comparados à linha de base do início do projeto. A maior mudança foi no abandono da tela de confirmação, o ponto atacado no redesenho.\n• O que eu faria diferente: testes de usabilidade presenciais semanais nas empresas clientes desde a primeira sprint. Isso teria revelado a dúvida sobre o desconto no salário cerca de 6 semanas antes.',
      calloutTitle: 'Desdobramento',
      impactText: '• O formato de simulação passou a ser o padrão para os outros produtos de crédito da empresa.'
    }
  ]
};
// ============================================================================
// BUILDER: Home Page Completa 1:1 Oficial (Node 302:3152 & Guia 333:2)
// ============================================================================
async function buildHome(parent, xPos, yPos) {
  log('Criando Home do Portfólio com Grid Suíço Compacto, Split-Hero e Gestalt 1:1...');

  var container = createVerticalContainer(
    'Home · Senior Product Designer — Israel Rozar',
    1280,
    48,
    { left: 64, right: 64, top: 48, bottom: 80 },
    TOKENS.colors.canvas,
    null,
    null
  );
  container.x = xPos;
  container.y = yPos;

  // 1. Navigation Header (56px)
  var nav = await createHeaderBar(1152);
  container.appendChild(nav);

  // 2. HERO EDITORIAL COMPACTO EM SPLIT-VIEW (2 Colunas: Copy 720px + Retrato 400px)
  // Sem Hero gigante: tudo visível acima da dobra em ~380px de altura!
  var heroRow = createHorizontalRow('Hero Row (Split-View)', 1152, 32, null, null, null, null, 'SPACE_BETWEEN', 'CENTER');

  // 2.1 Coluna Esquerda: Copy + Ações (720px)
  var heroLeft = createVerticalContainer('Hero Copy', 720, 16, null, null, null, null);
  
  var kickerFrame = createHorizontalRow('Hero Kicker', 720, 12, null, null, null, null, 'MIN', 'CENTER');
  var kickerPill = await createBadge('SENIOR PRODUCT DESIGNER', TOKENS.colors.acidLime, TOKENS.colors.deepPine, true);
  var kickerLoc = await createTextNode('São Paulo · Brasil', 14, 'regular', TOKENS.colors.textSecondary);
  kickerFrame.appendChild(kickerPill);
  kickerFrame.appendChild(kickerLoc);
  heroLeft.appendChild(kickerFrame);

  var heroHeadline = await createTextNode(
    'Design Estruturado para Ecossistemas de Alta Criticidade.',
    42,
    'bold',
    TOKENS.colors.textPrimary,
    720,
    null,
    50,
    -1.0
  );
  heroLeft.appendChild(heroHeadline);

  var heroLead = await createTextNode(
    'Desde 2006 desenhando experiências digitais. Mais de 15 anos focados em discovery, arquitetura da informação e design de produto para ecossistemas regulados em saúde, telecom e fintech.',
    16,
    'regular',
    TOKENS.colors.textSecondary,
    700,
    null,
    26
  );
  heroLeft.appendChild(heroLead);

  // CTAs com AutoLayout Wrap
  var ctaRow = createHorizontalRow('Hero CTAs', 720, 16, null, null, null, null, 'MIN', 'CENTER');
  try { ctaRow.layoutWrap = 'WRAP'; } catch(e) {}
  
  var btnPrimary = figma.createFrame();
  btnPrimary.name = 'Btn Conhecer meu trabalho';
  btnPrimary.layoutMode = 'HORIZONTAL';
  btnPrimary.primaryAxisSizingMode = 'AUTO';
  btnPrimary.counterAxisSizingMode = 'AUTO';
  try {
    btnPrimary.layoutSizingHorizontal = 'HUG';
    btnPrimary.layoutSizingVertical = 'HUG';
  } catch(e) {}
  btnPrimary.paddingLeft = 24;
  btnPrimary.paddingRight = 24;
  btnPrimary.paddingTop = 14;
  btnPrimary.paddingBottom = 14;
  btnPrimary.cornerRadius = TOKENS.radius.pill;
  btnPrimary.fills = solidFill(TOKENS.colors.deepPine);
  var btnTxt1 = await createTextNode('Conhecer meu trabalho ↓', 14, 'semibold', TOKENS.colors.canvas);
  btnPrimary.appendChild(btnTxt1);
  ctaRow.appendChild(btnPrimary);

  var btnSec = figma.createFrame();
  btnSec.name = 'Btn Baixar Currículo';
  btnSec.layoutMode = 'HORIZONTAL';
  btnSec.primaryAxisSizingMode = 'AUTO';
  btnSec.counterAxisSizingMode = 'AUTO';
  try {
    btnSec.layoutSizingHorizontal = 'HUG';
    btnSec.layoutSizingVertical = 'HUG';
  } catch(e) {}
  btnSec.paddingLeft = 24;
  btnSec.paddingRight = 24;
  btnSec.paddingTop = 14;
  btnSec.paddingBottom = 14;
  btnSec.cornerRadius = TOKENS.radius.pill;
  btnSec.fills = solidFill(TOKENS.colors.card);
  btnSec.strokes = [{ type: 'SOLID', color: TOKENS.colors.borderSubtle }];
  btnSec.strokeWeight = 1;
  var btnTxt2 = await createTextNode('Baixar currículo (PDF) ↗', 14, 'semibold', TOKENS.colors.textPrimary);
  btnSec.appendChild(btnTxt2);
  ctaRow.appendChild(btnSec);

  heroLeft.appendChild(ctaRow);
  heroRow.appendChild(heroLeft);

  // 2.2 Coluna Direita: Retrato Executivo Compacto (400px × 340px)
  var portraitCard = createVerticalContainer('Executive Portrait Card', 400, 10, { left: 16, right: 16, top: 16, bottom: 16 }, TOKENS.colors.card, TOKENS.colors.borderSubtle, TOKENS.radius.card, true);
  var portraitImg = await createRealImageFigure('home_portrait', null, 368, 280, TOKENS.radius.panel);
  portraitCard.appendChild(portraitImg);

  var metaStrip = createHorizontalRow('Portrait Meta Strip', 368, 0, null, null, null, null, 'SPACE_BETWEEN', 'CENTER');
  var pRole = await createTextNode('Senior Product Designer', 12, 'semibold', TOKENS.colors.textSecondary);
  var pCorps = await createTextNode('EINSTEIN • ITAÚ • CLARO • NEO', 11, 'bold', TOKENS.colors.textMuted);
  metaStrip.appendChild(pRole);
  metaStrip.appendChild(pCorps);
  portraitCard.appendChild(metaStrip);

  heroRow.appendChild(portraitCard);
  container.appendChild(heroRow);

  // 3. Career Metrics Bar (4 Colunas com Alinhamento Uniforme)
  var metricsBar = createHorizontalRow('Career Metrics Bar', 1152, 20, { left: 28, right: 28, top: 20, bottom: 20 }, TOKENS.colors.subtle, TOKENS.colors.borderSubtle, 16, 'SPACE_BETWEEN', 'MIN');
  var cMetrics = [
    { t: 'Background B2B & Corporativo', d: '15+ anos em design digital, focados em plataformas transacionais e ecossistemas complexos.' },
    { t: 'Domínios Regulados', d: 'Expertise em mesas de investimento IFA/Itaú, saúde diagnóstica e concessões de energia.' },
    { t: 'Governança de Design', d: 'Estruturação de Design Systems, tokens semânticos e handoff para ganho de escala em engenharia.' },
    { t: 'Conformidade Técnica', d: 'Adequação rigorosa aos parâmetros de acessibilidade AA/AAA e automação de revisões.' }
  ];
  for (var cm = 0; cm < cMetrics.length; cm++) {
    var cmCol = createVerticalContainer('Metric: ' + cMetrics[cm].t, (1152 - 56 - 60) / 4, 6, null, null, null, null);
    var cmT = await createTextNode(cMetrics[cm].t, 14, 'bold', TOKENS.colors.textPrimary, (1152 - 56 - 60) / 4, null, 20);
    var cmD = await createTextNode(cMetrics[cm].d, 12, 'regular', TOKENS.colors.textSecondary, (1152 - 56 - 60) / 4, null, 17);
    cmCol.appendChild(cmT);
    cmCol.appendChild(cmD);
    metricsBar.appendChild(cmCol);
    safeSetFill(cmCol, 'VERTICAL');
  }
  container.appendChild(metricsBar);

  // 4. Pill Ticker Strip
  var tickerStrip = createHorizontalRow('Pill Ticker Strip', 1152, 0, { left: 24, right: 24, top: 10, bottom: 10 }, TOKENS.colors.card, TOKENS.colors.borderSubtle, TOKENS.radius.pill, 'SPACE_BETWEEN', 'CENTER');
  var tickerWords = ['ARQUITETURA DE INFORMAÇÃO', '•', 'TELEMETRIA QUANTITATIVA', '•', 'DESIGN TOKENS SEMÂNTICOS', '•', 'ENTREVISTAS EM PROFUNDIDADE', '•', 'CONFORMIDADE WCAG AAA'];
  for (var tw = 0; tw < tickerWords.length; tw++) {
    var isBullet = (tickerWords[tw] === '•');
    var tNode = await createTextNode(tickerWords[tw], isBullet ? 12 : 11, 'bold', isBullet ? TOKENS.colors.acidLime : TOKENS.colors.deepPine);
    tickerStrip.appendChild(tNode);
  }
  container.appendChild(tickerStrip);

  // 5. Seção 01 · Trabalhos Selecionados
  var worksSection = createVerticalContainer('01 · Trabalhos Selecionados', 1152, 32, null, null, null, null);
  
  var worksHead = createVerticalContainer('Works Head', 1152, 8, null, null, null, null);
  var worksBadge = await createBadge('01 / TRABALHOS SELECIONADOS', TOKENS.colors.subtle, TOKENS.colors.deepPine, false);
  var worksTitle = await createTextNode('Projetos, decisões e contribuições documentadas.', 32, 'bold', TOKENS.colors.textPrimary, 1152, null, 38, -0.5);
  var worksLead = await createTextNode('Um case em destaque em saúde diagnóstica e quatro projetos que apresentam minha atuação em pesquisa, definição de problemas e design de produto.', 16, 'regular', TOKENS.colors.textSecondary, 1080, null, 24);
  worksHead.appendChild(worksBadge);
  worksHead.appendChild(worksTitle);
  worksHead.appendChild(worksLead);
  worksSection.appendChild(worksHead);

  // 5.1 CARD DE DESTAQUE ALBERT EINSTEIN EM SPLIT-VIEW (1152px width, ~420px height)
  // Elimina a imagem gigante de 1056x594px!
  var featCard = createHorizontalRow(
    'Case em Destaque: Albert Einstein (Split-View)',
    1152,
    32,
    { left: 32, right: 32, top: 32, bottom: 32 },
    TOKENS.colors.deepPine,
    null,
    TOKENS.radius.feature,
    'SPACE_BETWEEN',
    'CENTER'
  );

  // Coluna Esquerda do Card em Destaque (500px)
  var featLeft = createVerticalContainer('Feat Content', 500, 14, null, null, null, null);
  
  var featTop = createHorizontalRow('Feat Top', 500, 12, null, null, null, null, 'MIN', 'CENTER');
  var featBadge = await createBadge('★ CASE EM DESTAQUE · SAÚDE', TOKENS.colors.darkPine, TOKENS.colors.acidLime, true);
  var featSub = await createTextNode('Hospital Albert Einstein × Foursys · 2022', 12, 'semibold', TOKENS.colors.canvas);
  featTop.appendChild(featBadge);
  featTop.appendChild(featSub);
  featLeft.appendChild(featTop);

  var featHeadline = await createTextNode(
    'Uma linguagem visual modular para laudos clínicos heterogêneos.',
    24,
    'bold',
    TOKENS.colors.canvas,
    500,
    null,
    32,
    -0.5
  );
  featLeft.appendChild(featHeadline);

  var featDescription = await createTextNode(
    'Pesquisa e arquitetura da informação para estruturar mais de 80 exames distintos em uma linguagem modular previsível, facilitando a tomada de decisão médica e reduzindo a ansiedade de pacientes.',
    14,
    'regular',
    TOKENS.colors.subtle,
    500,
    null,
    22
  );
  featLeft.appendChild(featDescription);

  // 3 Métricas em Chips Compactos
  var featMetricsRow = createHorizontalRow('Feat Metrics Row', 500, 10, null, null, null, null, 'SPACE_BETWEEN', 'CENTER');
  var featMetrics = [
    { n: '14', d: 'famílias estruturadas' },
    { n: '121', d: 'pacientes e médicos testados' },
    { n: '80+', d: 'laudos no inventário' }
  ];
  var fColW = (500 - 20) / 3;
  for (var fm = 0; fm < featMetrics.length; fm++) {
    var fmCard = createVerticalContainer('FM ' + fm, fColW, 2, { left: 10, right: 10, top: 8, bottom: 8 }, TOKENS.colors.darkPine, TOKENS.colors.pineSurface, 8);
    var fmN = await createTextNode(featMetrics[fm].n, 20, 'bold', TOKENS.colors.acidLime);
    var fmD = await createTextNode(featMetrics[fm].d, 10, 'regular', TOKENS.colors.canvas, fColW - 20, null, 14);
    fmCard.appendChild(fmN);
    fmCard.appendChild(fmD);
    featMetricsRow.appendChild(fmCard);
    safeSetFill(fmCard, 'VERTICAL');
  }
  featLeft.appendChild(featMetricsRow);

  var featCta = figma.createFrame();
  featCta.name = 'Btn Ler Case Completo';
  featCta.layoutMode = 'HORIZONTAL';
  featCta.primaryAxisSizingMode = 'AUTO';
  featCta.counterAxisSizingMode = 'AUTO';
  try {
    featCta.layoutSizingHorizontal = 'HUG';
    featCta.layoutSizingVertical = 'HUG';
  } catch(e) {}
  featCta.paddingLeft = 24;
  featCta.paddingRight = 24;
  featCta.paddingTop = 12;
  featCta.paddingBottom = 12;
  featCta.cornerRadius = TOKENS.radius.pill;
  featCta.fills = solidFill(TOKENS.colors.acidLime);
  var fCtaTxt = await createTextNode('Explorar estudo de caso completo ↗', 14, 'bold', TOKENS.colors.deepPine);
  featCta.appendChild(fCtaTxt);
  featLeft.appendChild(featCta);

  featCard.appendChild(featLeft);

  // Coluna Direita do Card em Destaque: Mockup da Solução Real v3 (556 × 312 px, 16:9 - SEM IMAGEM GIGANTE!)
  var tabletMockup = await createRealImageFigure(
    'hiae_tablet',
    'Layout real da proposta de solução v3: estrutura modular canônica de laudo clínico.',
    556,
    312,
    TOKENS.radius.card
  );
  featCard.appendChild(tabletMockup);

  worksSection.appendChild(featCard);

  // 5.2 Grid 2×2 de Cases Complementares com Mockups Vetoriais Canônicos
  var gridComplementary = [
    {
      num: '01',
      client: 'FINTECH · ITAÚ UNIBANCO',
      title: 'Hub de Liquidez e Oportunidades',
      desc: 'Organização de saldos, projeções e oportunidades em alta densidade para especialistas de investimentos na plataforma IFA.',
      tagVal: 'IFA · B2B',
      tagDesc: 'plataforma de assessoria',
      thumbBuilder: buildHomeCardThumbItauHub
    },
    {
      num: '02',
      client: 'FINTECH · ITAÚ UNIBANCO',
      title: 'Gestão de Vencimentos em Carteira',
      desc: 'Consolidação de vencimentos, eventos futuros e Open Finance com filtros operacionais para atuação do assessor.',
      tagVal: 'Visão Canônica',
      tagDesc: 'proventos e agenda de carteira',
      thumbBuilder: buildHomeCardThumbItauVenc
    },
    {
      num: '03',
      client: 'ENERGIA · SERVICE DESIGN',
      title: 'Strategic Discovery e Service Design',
      desc: 'Unificação da infraestrutura de atendimento para 34 milhões de pessoas em 4 distribuidoras do Grupo Neoenergia.',
      tagVal: '34M Habitantes',
      tagDesc: 'nas concessões de energia',
      thumbBuilder: buildHomeCardThumbNeoenergia
    },
    {
      num: '04',
      client: 'TELECOM · CLARO BRASIL',
      title: 'Ativação Simplificada e Jornada Multicanal',
      desc: 'Mapeamento de 22 jornadas de atendimento, 20 entrevistas em profundidade e esteira unificada de checkout para televendas e lojas.',
      tagVal: '22 Jornadas',
      tagDesc: 'mapeadas e simplificadas',
      thumbBuilder: buildHomeCardThumbClaro
    }
  ];

  for (var r = 0; r < 2; r++) {
    var cRow = createHorizontalRow('Row ' + (r + 1), 1152, 24, null, null, null, null, 'SPACE_BETWEEN', 'MIN');

    for (var col = 0; col < 2; col++) {
      var item = gridComplementary[r * 2 + col];
      var card = createVerticalContainer('Card: ' + item.title, 564, 16, { left: 28, right: 28, top: 28, bottom: 28 }, TOKENS.colors.card, TOKENS.colors.borderSubtle, TOKENS.radius.card, true);

      // Mockup Vetorial de Alta Fidelidade no Topo do Card (508 × 286 px)
      var thumbImg = await item.thumbBuilder(508, 286);
      card.appendChild(thumbImg);

      var cHead = createHorizontalRow('Head ' + item.num, 508, 0, null, null, null, null, 'SPACE_BETWEEN', 'CENTER');
      var cNum = await createTextNode(item.num, 13, 'bold', TOKENS.colors.deepPine);
      var cClient = await createTextNode(item.client, 12, 'bold', TOKENS.colors.textMuted);
      cHead.appendChild(cNum);
      cHead.appendChild(cClient);
      card.appendChild(cHead);

      var cTitle = await createTextNode(item.title, 20, 'bold', TOKENS.colors.textPrimary, 508, null, 26);
      card.appendChild(cTitle);

      var cDesc = await createTextNode(item.desc, 13, 'regular', TOKENS.colors.textSecondary, 508, null, 20);
      card.appendChild(cDesc);

      var cTagRow = createHorizontalRow('Tag ' + item.num, 508, 8, null, null, null, null, 'MIN', 'CENTER');
      var tagV = await createTextNode(item.tagVal, 13, 'bold', TOKENS.colors.deepPine);
      var tagD = await createTextNode('· ' + item.tagDesc, 13, 'regular', TOKENS.colors.textSecondary);
      cTagRow.appendChild(tagV);
      cTagRow.appendChild(tagD);
      card.appendChild(cTagRow);

      cRow.appendChild(card);
      safeSetFill(card, 'VERTICAL');
    }

    worksSection.appendChild(cRow);
  }

  container.appendChild(worksSection);

  // 6. Footer da Home
  var footer = figma.createFrame();
  footer.name = 'Footer';
  footer.resize(1152, 64);
  footer.layoutMode = 'HORIZONTAL';
  footer.primaryAxisSizingMode = 'FIXED';
  footer.counterAxisSizingMode = 'AUTO';
  safeSetPrimaryAlign(footer, 'SPACE_BETWEEN');
  safeSetCounterAlign(footer, 'CENTER');
  footer.clipsContent = false;
  footer.fills = [];
  var copy = await createTextNode('© Israel Rozar · Senior Product Designer · Sistemas Complexos, AI & Design Systems', 13, 'regular', TOKENS.colors.textSecondary);
  var topLink = await createTextNode('Voltar ao topo ↑', 13, 'semibold', TOKENS.colors.textPrimary);
  footer.appendChild(copy);
  footer.appendChild(topLink);
  container.appendChild(footer);

  container.primaryAxisSizingMode = 'AUTO';
  container.clipsContent = false;

  parent.appendChild(container);
  log('✔ Home construída com sucesso total e todas as seções!');
  return container;
}
"""

js_dispatcher = r"""
// ============================================================================
// DISPATCHER PRINCIPAL DO PLUGIN
// ============================================================================
figma.ui.onmessage = async function(msg) {
  if (!msg) return;
  
  if (msg.type === 'create_salarynow') {
    updateStatus('Criando Case SalaryNow (Framework STAR) em Nova Página...');
    try {
      var pageName = 'Case SalaryNow (STAR Framework)';
      var targetPage = null;
      for (var p = 0; p < figma.root.children.length; p++) {
        if (figma.root.children[p].name === pageName) {
          targetPage = figma.root.children[p];
          break;
        }
      }
      if (!targetPage) {
        targetPage = figma.createPage();
        targetPage.name = pageName;
      }
      figma.currentPage = targetPage;
      
      var salaryNode = await buildGenericCaseScreen(targetPage, 0, 0, CASE_SALARYNOW);
      figma.viewport.scrollAndZoomIntoView([salaryNode]);
      updateStatus('Concluído: Case SalaryNow criado em nova página!');
      figma.notify('🎉 Case SalaryNow (STAR) criado com sucesso na página "' + pageName + '"!');
    } catch (e) {
      log('Erro ao criar Case SalaryNow: ' + e);
      updateStatus('Erro na geração do SalaryNow.');
    }
  }
  else if (msg.type === 'create_case_template') {
    updateStatus('Construindo Case Template Oficial em Página Própria...');
    try {
      var pageName = 'Template · Case de Estudo (Senior UX)';
      var targetPage = null;
      for (var p = 0; p < figma.root.children.length; p++) {
        if (figma.root.children[p].name === pageName) {
          targetPage = figma.root.children[p];
          break;
        }
      }
      if (!targetPage) {
        targetPage = figma.createPage();
        targetPage.name = pageName;
      }
      figma.currentPage = targetPage;
      var node = await buildGenericCaseScreen(targetPage, 0, 0, CASE_TEMPLATE);
      figma.viewport.scrollAndZoomIntoView([node]);
      updateStatus('Concluído: Case Template gerado na página dedicada!');
      figma.notify('✔ Case Template (Senior UX) gerado com sucesso na página "' + pageName + '"!');
    } catch (e) {
      log('Erro ao criar Case Template: ' + e);
      updateStatus('Erro na geração.');
    }
  }
  else if (msg.type === 'create_home') {
    updateStatus('Construindo Home com todas as seções...');
    try {
      var node = await buildHome(figma.currentPage, 0, 0);
      figma.viewport.scrollAndZoomIntoView([node]);
      updateStatus('Concluído: Home gerada com sucesso!');
      figma.notify('✔ Home do portfólio gerada com todas as seções!');
    } catch (e) {
      log('Erro ao criar Home: ' + e);
      updateStatus('Erro na geração.');
    }
  }
  else if (msg.type === 'create_neoenergia') {
    updateStatus('Construindo Case Neoenergia com Imagens Reais...');
    try {
      var node = await buildGenericCaseScreen(figma.currentPage, 1440, 0, CASE_NEOENERGIA);
      figma.viewport.scrollAndZoomIntoView([node]);
      updateStatus('Concluído: Case Neoenergia gerado com sucesso!');
      figma.notify('✔ Case Neoenergia gerado com sucesso!');
    } catch (e) {
      log('Erro ao criar Neoenergia: ' + e);
      updateStatus('Erro na geração.');
    }
  }
  else if (msg.type === 'create_einstein') {
    updateStatus('Construindo Case Albert Einstein com Imagens Reais...');
    try {
      var node = await buildGenericCaseScreen(figma.currentPage, 2880, 0, CASE_EINSTEIN);
      figma.viewport.scrollAndZoomIntoView([node]);
      updateStatus('Concluído: Case Albert Einstein gerado!');
      figma.notify('✔ Case Albert Einstein gerado com sucesso!');
    } catch (e) {
      log('Erro ao criar Einstein: ' + e);
      updateStatus('Erro na geração.');
    }
  }
  else if (msg.type === 'create_itau') {
    updateStatus('Construindo Case Itaú Unibanco com Imagens Reais...');
    try {
      var node = await buildGenericCaseScreen(figma.currentPage, 4320, 0, CASE_ITAU);
      figma.viewport.scrollAndZoomIntoView([node]);
      updateStatus('Concluído: Case Itaú Unibanco gerado!');
      figma.notify('✔ Case Itaú Unibanco gerado com sucesso!');
    } catch (e) {
      log('Erro ao criar Itaú: ' + e);
      updateStatus('Erro na geração.');
    }
  }
  else if (msg.type === 'create_claro') {
    updateStatus('Construindo Case Claro Brasil com Imagens Reais...');
    try {
      var node = await buildGenericCaseScreen(figma.currentPage, 5760, 0, CASE_CLARO);
      figma.viewport.scrollAndZoomIntoView([node]);
      updateStatus('Concluído: Case Claro Brasil gerado!');
      figma.notify('✔ Case Claro Brasil gerado com sucesso!');
    } catch (e) {
      log('Erro ao criar Claro: ' + e);
      updateStatus('Erro na geração.');
    }
  }
  else if (msg.type === 'create_all_screens') {
    updateStatus('Construindo todas as telas mestres com imagens reais 1:1...');
    try {
      log('=== INICIANDO GERAÇÃO DE TODAS AS TELAS (TEMPLATE + HOME + 4 CASES) ===');
      var templateNode = await buildGenericCaseScreen(figma.currentPage, -1440, 0, CASE_TEMPLATE);
      var homeNode = await buildHome(figma.currentPage, 0, 0);
      var neoNode = await buildGenericCaseScreen(figma.currentPage, 1440, 0, CASE_NEOENERGIA);
      var einNode = await buildGenericCaseScreen(figma.currentPage, 2880, 0, CASE_EINSTEIN);
      var itauNode = await buildGenericCaseScreen(figma.currentPage, 4320, 0, CASE_ITAU);
      var claroNode = await buildGenericCaseScreen(figma.currentPage, 5760, 0, CASE_CLARO);
      
      figma.viewport.scrollAndZoomIntoView([templateNode, homeNode, neoNode, einNode, itauNode, claroNode]);
      updateStatus('Concluído: Telas Mestres e Template Criados!');
      figma.notify('🎉 Todas as telas do portfólio foram geradas com sucesso!');
    } catch (e) {
      log('Erro na geração total: ' + e);
      updateStatus('Erro na geração total.');
    }
  }
  else if (msg.type === 'close') {
    figma.closePlugin();
  }
};
"""

ui_html = r"""<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <style>
    body {
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      margin: 0; padding: 24px;
      background: #0A3622; color: #FCF9F2;
      display: flex; flex-direction: column; height: 720px;
      box-sizing: border-box;
    }
    .kicker {
      font-size: 11px; font-weight: 700; letter-spacing: 0.1em;
      color: #CEFF1A; text-transform: uppercase; margin-bottom: 6px;
    }
    h2 { font-size: 20px; font-weight: 700; margin: 0 0 8px 0; color: #FCF9F2; }
    p { font-size: 13px; color: #EDE9DE; margin: 0 0 16px 0; line-height: 1.5; }
    
    .btn-group {
      display: flex; flex-direction: column; gap: 8px; margin-bottom: 16px;
    }
    .btn {
      background: #062215; color: #FCF9F2; border: 1px solid #114B31; border-radius: 8px;
      padding: 10px 14px; font-size: 12px; font-weight: 600; cursor: pointer;
      display: flex; align-items: center; justify-content: space-between;
      transition: all 0.15s ease;
    }
    .btn:hover { background: #114B31; border-color: #CEFF1A; }
    
    .btn-primary {
      background: #CEFF1A; color: #0A3622; border: none; font-size: 13px; font-weight: 700;
      padding: 14px 16px; margin-bottom: 4px;
    }
    .btn-primary:hover { background: #BEF00E; transform: translateY(-1px); }
    
    .btn-template {
      background: #114B31; color: #CEFF1A; border: 1px solid #CEFF1A; font-size: 13px; font-weight: 700;
      padding: 12px 14px;
    }
    .btn-template:hover { background: #0A3622; box-shadow: 0 0 12px rgba(206, 255, 26, 0.25); }
    
    .btn:disabled { opacity: 0.5; cursor: not-allowed; }
    
    #log {
      flex: 1; padding: 12px; background: #062215;
      border: 1px solid #114B31; border-radius: 8px; font-family: ui-monospace, monospace;
      font-size: 11px; color: #CEFF1A; overflow-y: auto; white-space: pre-wrap; line-height: 1.4;
    }
    .status-bar {
      margin-top: 14px; font-size: 11px; color: #EDE9DE; display: flex;
      justify-content: space-between; align-items: center;
    }
    .close-link { color: #EDE9DE; text-decoration: none; cursor: pointer; opacity: 0.7; }
    .close-link:hover { opacity: 1; text-decoration: underline; }
  </style>
</head>
<body>
  <div class="kicker">Gerador Oficial 1:1 · Senior Product Designer</div>
  <h2>Todas as Telas do Portfólio no Figma</h2>
  <p>Gera automaticamente as telas completas em Auto-Layout suíço, sem cortes, com <strong>todas as seções</strong> e <strong>imagens reais dos entregáveis</strong>.</p>
  
  <div class="btn-group">
    <button class="btn btn-star" onclick="triggerAction('create_salarynow')" style="background:#062215; border:1.5px solid #CEFF1A; padding:12px 14px; margin-bottom:4px; display:flex; align-items:center; justify-content:space-between; cursor:pointer; border-radius:8px;">
      <div style="display:flex; align-items:center; gap:8px;">
        <span style="font-size:16px;">⭐</span>
        <div style="text-align:left;">
          <div style="font-weight:700; color:#CEFF1A; font-size:13px;">Criar Case SalaryNow (STAR Framework)</div>
          <div style="font-size:10px; color:#EDE9DE;">Fintech B2B2C · 4 Riscos Cagan · Gestalt · Nova Página</div>
        </div>
      </div>
      <span style="font-size:10px; background:#CEFF1A; color:#0A3622; padding:3px 6px; border-radius:4px; font-weight:700;">NOVA PÁGINA</span>
    </button>
    <button class="btn btn-template" onclick="triggerAction('create_case_template')">
      <span>📄 Criar case template</span>
      <span>Grid Suíço 1:1</span>
    </button>
    <button class="btn btn-primary" onclick="triggerAction('create_all_screens')">
      <span>🚀 RECRIAR TODAS AS TELAS (COM IMAGENS)</span>
      <span>Home + 4 Cases</span>
    </button>
    <button class="btn" onclick="triggerAction('create_home')">
      <span>⚡ Home do Portfólio (Hero + Seções + Footer)</span>
      <span>Completa (1280 px)</span>
    </button>
    <button class="btn" onclick="triggerAction('create_einstein')">
      <span>⚡ Case Albert Einstein (Laudos Clínicos v3)</span>
      <span>7 Capítulos</span>
    </button>
    <button class="btn" onclick="triggerAction('create_itau')">
      <span>⚡ Case Itaú Unibanco (Plataforma Íon)</span>
      <span>5 Capítulos</span>
    </button>
    <button class="btn" onclick="triggerAction('create_neoenergia')">
      <span>⚡ Case Neoenergia (Service Design P&D ANEEL)</span>
      <span>7 Capítulos</span>
    </button>
    <button class="btn" onclick="triggerAction('create_claro')">
      <span>⚡ Case Claro Brasil (Ativação Multicanal)</span>
      <span>4 Capítulos</span>
    </button>
  </div>

  <div id="log">Pronto para gerar as telas com imagens reais...</div>

  <div class="status-bar">
    <span id="status">Aguardando comando</span>
    <span class="close-link" onclick="closePlugin()">Fechar plugin</span>
  </div>

  <script>
    function triggerAction(actionType) {
      document.getElementById('status').textContent = 'Processando...';
      document.getElementById('log').textContent = 'Iniciando operação: ' + actionType + '\n';
      parent.postMessage({ pluginMessage: { type: actionType } }, '*');
    }

    function closePlugin() {
      parent.postMessage({ pluginMessage: { type: 'close' } }, '*');
    }

    onmessage = function(event) {
      var msg = event.data && event.data.pluginMessage;
      if (!msg) return;
      if (msg.type === 'log') {
        var el = document.getElementById('log');
        el.textContent += msg.message + '\n';
        el.scrollTop = el.scrollHeight;
      } else if (msg.type === 'status') {
        document.getElementById('status').textContent = msg.message;
      }
    };
  </script>
</body>
</html>
"""

js_layout_v2 = Path("scripts/figma_layout_v2.js").read_text(encoding="utf-8")
full_code_js = js_core + "\n" + js_images_decl + "\n" + js_builders + "\n" + js_layout_v2 + "\n" + js_data_and_home + "\n" + js_dispatcher

(plugin_dir / "code.js").write_text(full_code_js, encoding="utf-8")
(plugin_dir / "ui.html").write_text(ui_html, encoding="utf-8")

print(f"SUCCESS: Generated code.js ({len(full_code_js)} chars) and ui.html in {plugin_dir}!")
