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
    'hiae_taxonomia': 'site/public/images/hiae-taxonomia-laudo-2000.webp',
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

  var links = ['Cases', 'Sobre', 'Currículo'];
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
  var c3Action = await createTextNode('➜ DECISÃO: Adicionar painel de saúde financeira agregada para engajar o RH como patrocinador.', 12, 'bold', TOKENS.colors.deepPine, pColW - 32, null, 16);
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
  var gfTxt = await createTextNode('Resultado Cognitivo: Mudança da percepção de "endividamento" para "benefício transparente e sob controle".', 12, 'semibold', TOKENS.colors.acidLime);
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
  var pill = await createBadge('ITAÚ ÍON FOR ADVISORS · IFA', TOKENS.colors.darkPine, TOKENS.colors.acidLime, true);
  var stat = await createBadge('DADOS SINTETIZADOS · LGPD', TOKENS.colors.pineSurface, TOKENS.colors.canvas, true);
  top.appendChild(pill);
  top.appendChild(stat);
  frame.appendChild(top);

  var tNode = await createTextNode('Hub de Liquidez e Oportunidades', 16, 'bold', TOKENS.colors.canvas, width - 40, null, 22);
  frame.appendChild(tNode);

  var statsRow = createHorizontalRow('Stats', width - 40, 10, null, null, null, null, 'SPACE_BETWEEN', 'MIN');
  var sW = (width - 40 - 20) / 3;
  var sData = [
    { k: 'DISPONÍVEL AGORA', v: 'Itaú + Open Fin.' },
    { k: 'JANELAS', v: 'Dia · 7d · 30d' },
    { k: 'FILA OPERACIONAL', v: 'Status ativo' }
  ];
  for (var i = 0; i < sData.length; i++) {
    var sc = createVerticalContainer('S' + i, sW, 4, { left: 10, right: 10, top: 8, bottom: 8 }, TOKENS.colors.darkPine, TOKENS.colors.pineSurface, 8);
    var sk = await createTextNode(sData[i].k, 9, 'bold', TOKENS.colors.textMuted);
    var sv = await createTextNode(sData[i].v, 13, 'bold', TOKENS.colors.acidLime);
    sc.appendChild(sk);
    sc.appendChild(sv);
    statsRow.appendChild(sc);
  }
  frame.appendChild(statsRow);

  var assetRow = createHorizontalRow('Asset Preview', width - 40, 8, { left: 12, right: 12, top: 10, bottom: 10 }, TOKENS.colors.darkPine, TOKENS.colors.pineSurface, 8, 'SPACE_BETWEEN', 'CENTER');
  var aLbl = await createTextNode('Posição atual · Variação prevista · Liquidez projetada', 11, 'medium', TOKENS.colors.canvas);
  var aBtn = await createBadge('FILTRAR ➔', TOKENS.colors.acidLime, TOKENS.colors.deepPine, true);
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
  var pill = await createBadge('ABAS UNIFICADAS · IFA', TOKENS.colors.subtle, TOKENS.colors.deepPine, false);
  var stat = await createBadge('FILTROS COMBINÁVEIS', TOKENS.colors.acidLime, TOKENS.colors.deepPine, true);
  top.appendChild(pill);
  top.appendChild(stat);
  frame.appendChild(top);

  var tNode = await createTextNode('Consulta de Vencimentos, Eventos Futuros e Open Finance', 16, 'bold', TOKENS.colors.canvas, width - 40, null, 22);
  frame.appendChild(tNode);

  var calRow = createHorizontalRow('Cal Strip', width - 40, 8, null, null, null, null, 'SPACE_BETWEEN', 'CENTER');
  var calDays = ['Vencimentos', 'Eventos futuros', 'Open Finance'];
  for (var d = 0; d < calDays.length; d++) {
    var isAct = (d === 0);
    var dChip = await createBadge(calDays[d], isAct ? TOKENS.colors.acidLime : TOKENS.colors.pineSurface, isAct ? TOKENS.colors.deepPine : TOKENS.colors.canvas, isAct);
    calRow.appendChild(dChip);
  }
  frame.appendChild(calRow);

  var alertCard = createHorizontalRow('Alert Card', width - 40, 8, { left: 12, right: 12, top: 10, bottom: 10 }, TOKENS.colors.deepPine, TOKENS.colors.pineSurface, 8, 'SPACE_BETWEEN', 'CENTER');
  var alTxt = await createTextNode('Busca, prazo, status e registro de atuação (dados sintetizados)', 11, 'medium', TOKENS.colors.canvas);
  var alAction = await createBadge('ATUAR ➔', TOKENS.colors.canvas, TOKENS.colors.deepPine, true);
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
  var steps = ['1. CPF', '2. Linha', '3. Oferta', '4. Resumo', '5. Ativação'];
  for (var s = 0; s < steps.length; s++) {
    var isLast = (s === 4);
    var sBadge = await createBadge(steps[s], isLast ? TOKENS.colors.acidLime : TOKENS.colors.deepPine, isLast ? TOKENS.colors.deepPine : TOKENS.colors.canvas, isLast);
    stepRow.appendChild(sBadge);
  }
  frame.appendChild(stepRow);

  var simStrip = createHorizontalRow('Plan Strip', width - 40, 8, { left: 12, right: 12, top: 10, bottom: 10 }, TOKENS.colors.deepPine, TOKENS.colors.darkPine, 8, 'SPACE_BETWEEN', 'CENTER');
  var pTxt = await createTextNode('Claro Pós 4G · Combo Residencial + Móvel (dados sintetizados)', 11, 'medium', TOKENS.colors.canvas);
  var pBtn = await createBadge('RESUMO ➔', TOKENS.colors.acidLime, TOKENS.colors.deepPine, true);
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
  var provHome = await buildProvenanceBanner(1152);
  container.appendChild(provHome);

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
  subtitle: 'No P&D ANEEL da Neoenergia (EY × Livework), conduzi frentes de Service Design pela EY para reduzir rupturas entre canais digitais, atendimento e campo nas 4 distribuidoras. Estruturamos 5 Service Blueprints e 118 ideias priorizadas como baseline estratégico (etapa de P&D, sem código final neste ciclo).',
  metadata: [
    { label: 'MEU PAPEL', val: 'Senior Product Designer · Service Design' },
    { label: 'EQUIPE', val: 'EY Business Transformation × Livework e áreas da Neoenergia' },
    { label: 'ESCOPO', val: 'Diagnóstico de 11 canais, 5 Service Blueprints, base multi-tenant e 118 ideias' },
    { label: 'ENTREGA PRINCIPAL', val: '4 distribuidoras · 5 Service Blueprints · 118 ideias (P&D ANEEL)' }
  ],
  heroImgKey: 'neo_capa',
  heroCaption: 'Por que cruzar Service Blueprint, escala nacional e priorização: mostrar que falhas de atendimento e fatura exigiam alinhar operação e backoffice nas 4 distribuidoras antes de redesenhar portais.',
  metrics: [
    { n: '4', d: 'distribuidoras mapeadas' },
    { n: '5', d: 'Service Blueprints' },
    { n: '118', d: 'ideias priorizadas' },
    { n: '34M', d: 'habitantes nas concessões' },
    { n: '13,9M', d: 'clientes em 18 estados' }
  ],
  prevCaseTitle: 'Claro · Ativação simplificada',
  nextCaseTitle: 'Albert Einstein · Consumo de Resultados',
  chapters: [
    {
      num: '01',
      tag: 'ESCALA NACIONAL (34M)',
      short: 'Escala e diagnóstico de 11 canais',
      title: 'Unificação do atendimento para 34 milhões de habitantes e 13,9 milhões de clientes.',
      imgKey: 'neo_num',
      caption: 'Por que dimensionar a escala antes de propor interfaces: qualquer falha de processo se multiplica por 13,9 milhões de clientes e 4 operações regionais (Elektro, Coelba, Celpe e Cosern).',
      p: 'Em 2020, entrevistas qualitativas, acompanhamento do atendimento e auditoria de processos mapearam 3 perfis de clientes em 11 pontos de contato — de agências presenciais a portal, aplicativo, SMS, WhatsApp, call center e equipes de campo. Conduzi pela EY roteiros de diagnóstico, estruturação dos 5 Service Blueprints e diretrizes de arquitetura multi-tenant.'
    },
    {
      num: '02',
      tag: 'AUDITORIA DE BACKSTAGE',
      short: 'Auditoria de backstage',
      title: 'Auditoria de backstage: quando a insatisfação com a fatura revela silos operacionais.',
      imgKey: 'neo_bp1',
      caption: 'Por que mapear frontstage e backstage na mesma prancha: tornar visível onde falhas internas de sistemas legados e campo causavam retrabalho para o cliente nas 4 distribuidoras.',
      p: 'A auditoria mostrou que a insatisfação com a fatura raramente era um problema de tela. Ela vinha de leituras por estimativa, regras de cobrança pouco claras e falta de sincronização entre despacho técnico e faturamento.'
    },
    {
      num: '03',
      tag: '5 SERVICE BLUEPRINTS',
      short: 'Os 5 estágios do ciclo de vida',
      title: 'Os 5 estágios do ciclo de vida do cliente mapeados em Service Blueprints.',
      imgKey: 'neo_tobe',
      caption: 'Por que destacar a curva de criticidade no estágio Uso e Pago: apontar onde análise de cobrança e pagamento elevam o atrito para direcionar ações imediatas.',
      p: 'Para superar a fragmentação entre as 4 distribuidoras, consolidamos a jornada do cliente em 5 estágios com frontstage e backstage: 1. Contrato e instalo, 2. Uso e pago, 3. Preciso de suporte, 4. Mudo o contrato e 5. Abandono.'
    },
    {
      num: '04',
      tag: 'SERVIÇO & BASE MULTI-TENANT',
      short: 'Decisões de serviço e base multi-tenant',
      title: 'Desburocratização de backoffice antes de redesenho de portal e base multi-tenant.',
      imgKey: 'neo_ds',
      caption: 'Por que sequenciar UI Roadmap, Style Guide e biblioteca de componentes na Etapa 6 (Sprints de Execução): garantir que os padrões visuais nascessem dos Service Blueprints validados nas Etapas 4 e 5.',
      p: 'Decisão 1 (serviço antes da tela): priorizamos os 5 Service Blueprints antes da interface, aceitando adiar o código do portal final para não digitalizar processos quebrados (como três notas de serviço desintegradas na ligação nova). Decisão 2 (base multi-tenant): defendi componentes compartilhados com temas por marca para evitar quadruplicar a manutenção, aceitando maior governança entre regionais.'
    },
    {
      num: '05',
      tag: '118 IDEIAS PRIORIZADAS',
      short: 'Priorização, desacordo e reflexão',
      title: '118 ideias distribuídas na jornada futura como baseline para o roadmap de serviços.',
      imgKey: 'neo_matriz',
      caption: 'Por que ancorar as 118 ideias na curva de criticidade da jornada futura: impedir que iniciativas entrassem no roadmap desconectadas dos pontos reais de atrito operacional.',
      p: 'Decisão 3 (priorização): sequenciamos ações imediatas em fatura e autoleitura antes de telemedição, aceitando postergar investimentos de longo prazo. Desacordo estratégico: diretorias regionais pediram 4 portais isolados; cruzando os blueprints com o esforço de backoffice, defendemos a base multi-tenant. Reflexão: eu reverteria conduzir os workshops só com pranchas estáticas sem protótipos navegáveis de dois fluxos críticos de campo.'
    },
    {
      num: '06',
      tag: 'GOVERNANÇA P&D ANEEL',
      short: 'Governança e escopo do P&D',
      title: 'Fontes oficiais de P&D ANEEL, governança executiva e equipe EY × Livework.',
      imgKey: 'neo_capa',
      caption: 'Governança executiva: 5 Service Blueprints e 118 ideias aprovados pelas diretorias de operação e atendimento no programa P&D Estratégico ANEEL (sem implementação em código neste ciclo).',
      p: 'Resultado qualitativo (2020): os 5 Service Blueprints e as 118 ideias foram aprovados como baseline do P&D Estratégico ANEEL, criando linguagem compartilhada entre atendimento, backoffice e campo das 4 distribuidoras. Por ser etapa de P&D, não houve implementação em código nem linha de base medida em produção neste ciclo.'
    }
  ]
};

var CASE_EINSTEIN = {
  name: 'Case Albert Einstein',
  frameName: 'Case · Albert Einstein — Consumo de Resultados',
  kickerTag: 'SAÚDE · UX LEAD',
  kickerCompany: 'Hospital Israelita Albert Einstein (HIAE) × Foursys · 2022',
  title: 'Uma linguagem visual modular para laudos heterogêneos.',
  subtitle: 'Como UX Lead no Hospital Israelita Albert Einstein (HIAE × Foursys), liderei o projeto Consumo de Resultados. Conduzi pesquisa, arquitetura da informação e componentes para mais de 80 tipos de laudos em tela e impressão P&B. Nos testes de protótipo, 81,6% reconheceram o documento e 77,8% focaram primeiro em exame, resultado e referência.',
  metadata: [
    { label: 'MEU PAPEL', val: 'UX Lead' },
    { label: 'EQUIPE', val: 'Design (Foursys) × Corpo clínico e Engenharia (Einstein)' },
    { label: 'ESCOPO', val: 'Pesquisa, arquitetura da informação e prototipagem' },
    { label: 'VALIDAÇÃO E ESCOPO', val: '81,6% reconhecimento · 14 entregáveis' }
  ],
  heroImgKey: 'hiae_capa',
  heroCaption: 'Proposta v3 estruturada sobre mais de 80 exames reais para manter a mesma ordem de leitura em papel A4, web e celular, sem depender de cor isolada. Dados clínicos anonimizados sob LGPD.',
  metrics: [
    { n: '121', d: 'pacientes no questionário' },
    { n: '4', d: 'médicos especialistas entrevistados' },
    { n: '14', d: 'entregáveis (EN-1 a EN-14)' },
    { n: '81,6%', d: 'reconhecimento no protótipo' },
    { n: '77,8%', d: 'foco em exame e referência' }
  ],
  prevCaseTitle: 'Neoenergia · Service Design',
  nextCaseTitle: 'Itaú Unibanco · Hub de Liquidez',
  chapters: [
    {
      num: '01',
      tag: 'TESE CLÍNICA',
      short: 'Tese clínica e descoberta',
      title: 'Organizar resultados sem perder o contexto clínico.',
      imgKey: 'hiae_triangulacao',
      caption: 'Triangulação de 2022: 121 respostas anônimas (LGPD), 4 entrevistas médicas, inventário de 80+ exames e benchmark de serviços de saúde.',
      p: 'Laboratórios e hospitais parceiros emitiam exames em layouts distintos, dificultando a leitura clínica e a padronização dos sistemas laudadores. Pergunta norteadora: como facilitar a localização e a leitura do laudo sem induzir uma interpretação clínica isolada? Pacientes buscam localizar o resultado para levar à consulta, enquanto médicos precisam cruzar valor, referência e método.'
    },
    {
      num: '02',
      tag: 'TELA & PAPEL (ANTES/DEPOIS)',
      short: 'Restrições e decisões clínicas',
      title: 'Uma hierarquia que funcione na tela e no papel.',
      imgKey: 'hiae_tablet',
      caption: 'Antes vs. Depois: aproximei resultado, unidade e valor de referência no mesmo bloco visual para reduzir erro de associação entre colunas afastadas no documento legado.',
      p: 'Decisão 01 (alertas por cor): entre selos interpretativos ("normal/alterado") pedidos por parte do negócio ou valor e referência lado a lado com ícone redundante, negociei com apoio dos 4 médicos descartar os selos, a custo de não oferecer leitura binária instantânea, preservando impressão P&B. Decisão 02 (taxonomia comum): priorizei decompor 80+ exames em 3 macroáreas com examTitle e dataField, a custo de menor liberdade visual em exames atípicos.'
    },
    {
      num: '03',
      tag: 'TAXONOMIA DE DADOS',
      short: 'Taxonomia em 3 macroáreas',
      title: 'Do documento ao dado.',
      imgKey: 'hiae_taxonomia',
      caption: 'Taxonomia em 3 macroáreas (Metodologia, Resultado e Conclusão diagnóstica): reutiliza a mesma ordem de leitura em exames laboratoriais e de imagem sob LGPD.',
      p: 'Todos os mais de 80 exames reais auditados convergem para três macroáreas fixas: 1. Metodologia (prescrição, material biológico e equipamento), 2. Resultado (achados e intervalos de referência alinhados) e 3. Conclusão diagnóstica (parecer assinado pelo médico).'
    },
    {
      num: '04',
      tag: 'ANATOMIA DO COMPONENTE',
      short: 'Anatomia v3 e Zera 1.0',
      title: 'Preservar relações entre resultado, referência e contexto.',
      imgKey: 'hiae_tokens',
      caption: 'Design System Zera 1.0 e Protrombina (v3): ícones redundantes à cor e tokens de espaçamento 8px em dataField e examTitle reduzem divergências entre sistemas laudadores.',
      p: 'No componente Tempo de Protrombina (plasma), Atividade e Relação (RNI) ficam em linhas dedicadas com valor e referência lado a lado e ícone redundante à cor. Decisão 03 (compatibilidade): priorizei cabeçalho e rodapé comuns compatíveis com Microsoft Word e impressão P&B, a custo de adiar o redesenho completo do portal.'
    },
    {
      num: '05',
      tag: 'ESCALA EM 80+ EXAMES',
      short: 'Escala multicanal (A4, web, celular)',
      title: 'Uma estrutura única para qualquer tipo de exame.',
      imgKey: 'hiae_visao_futura',
      caption: 'Paridade em 3 canais (papel A4, web e celular) em laudos descritivos (mamografia) e tabulares (ressonância): mantém a mesma ordem sem reaprendizado ao trocar de suporte.',
      p: 'Estruturei a mesma anatomia modular para laudos descritivos longos (mamografia e biópsias) e tabelas numéricas densas (ressonâncias e hemogramas). Reaproveitar cabeçalho, hierarquia e blocos reduz a quantidade de templates mantidos nos sistemas laudadores.'
    },
    {
      num: '06',
      tag: 'COMPREENSÃO, ESCOPO & NDA',
      short: 'Validação, escopo, reflexão e NDA',
      title: 'Clareza de leitura e diagnóstico clínico: papéis complementares.',
      imgKey: 'hiae_capa',
      caption: 'Testes do protótipo v3 (2022, EN-7 e EN-14): 81,6% reconhecimento, 77,8% foco visual, 58,8% objetivo e 56,2% interpretação autônoma — diferença de 21,6 p.p. entre foco e interpretação.',
      p: 'A diferença de 21,6 p.p. entre foco visual (77,8%) e interpretação autônoma (56,2%) — e de 25,4 p.p. desde o reconhecimento (81,6%) — confirmou que clareza percebida não equivale a compreensão clínica. O escopo encerrou na entrega da especificação v3 (EN-1 a EN-14), sem linha de base do legado nem medição pós-lançamento; implantação sob gestão interna e arquivos restritos por NDA. Reflexão: eu reverteria consolidar os componentes digitais antes de testar quebras de página em PDF.'
    }
  ]
};

var CASE_ITAU = {
  name: 'Case Itaú Unibanco',
  frameName: 'Case · Itaú Unibanco — Plataforma íon for Advisors',
  kickerTag: 'FINTECH · ITAÚ UNIBANCO',
  kickerCompany: 'Itaú Unibanco · Plataforma íon for Advisors · 2024–2026',
  title: 'Cinco recortes de produto na plataforma íon for Advisors (IFA).',
  subtitle: 'Atuação como Senior Product Designer em cinco módulos para especialistas de investimentos e os assessores que os auxiliam: Hub de Liquidez, Vencimentos, Movimentações, Campanhas e Registros.',
  metadata: [
    { label: 'MEU PAPEL', val: 'Senior Product Designer' },
    { label: 'EQUIPE', val: 'Design, Produto, Engenharia e áreas de negócio' },
    { label: 'ESCOPO', val: 'Hub de Liquidez, Vencimentos, Movimentações, Campanhas e Registros' },
    { label: 'ENTREGA PRINCIPAL', val: '5 recortes documentados com dados sintetizados (LGPD)' }
  ],
  heroImgKey: 'itau_hub',
  heroCaption: 'íon for Advisors (IFA): interface para especialistas de investimentos e assessores com dados sintetizados para conformidade com o sigilo bancário (LGPD).',
  metrics: [
    { n: '5', d: 'recortes de produto' },
    { n: 'IFA', d: 'plataforma íon for Advisors' },
    { n: 'LGPD', d: 'dados sintetizados' },
    { n: 'iDS', d: 'componentes do Design System' },
    { n: 'B2B', d: 'especialistas e assessores' }
  ],
  prevCaseTitle: 'Albert Einstein · Consumo de Resultados',
  nextCaseTitle: 'Claro · Ativação simplificada',
  chapters: [
    {
      num: '01',
      tag: 'HUB DE LIQUIDEZ E OPORTUNIDADES',
      short: 'Hub de Liquidez',
      title: 'Separar saldo disponível, variação prevista e liquidez projetada em uma única leitura.',
      imgKey: 'itau_hub',
      caption: 'Hub de Liquidez: separa saldo disponível agora, variação prevista e projeção (fim do dia, 7 e 30 dias) para impedir leitura de valores futuros como disponibilidade imediata.',
      p: 'Conduzi a hierarquia financeira e os contratos de visualização no Hub de Liquidez, conectando posição atual (Itaú e Open Finance), projeção por janela e fila operacional de clientes. Decisão-chave: descartei indicador totalizador único para separar disponibilidade imediata de projeção, a custo de maior espaço no cabeçalho. Sem métricas pós-produção publicadas neste recorte.'
    },
    {
      num: '02',
      tag: 'GESTÃO DE VENCIMENTOS',
      short: 'Gestão de Vencimentos',
      title: 'Gestão de Vencimentos: consulta unificada de eventos financeiros e registro de atuação.',
      imgKey: 'itau_vencimentos',
      caption: 'Gestão de Vencimentos: abas separam Vencimentos, Eventos futuros e Open Finance mantendo a mesma busca, filtros e tabela para especialistas e assessores.',
      p: 'Conduzi a arquitetura de consulta, filtros combináveis por prazo, status e valor, tabela densa e estados vazios. A estrutura liga identificação do evento ao registro de atuação sem perder o contexto do cliente. Entrega consolidada na interface canônica e especificação de estados para handoff.'
    },
    {
      num: '03',
      tag: 'MOVIMENTAÇÕES (EXTRATO EA ➔ IFA)',
      short: 'Movimentações e saldo provisionado',
      title: 'Movimentações: saldo provisionado no cabeçalho e limites em contexto.',
      imgKey: 'itau_movimentacoes',
      caption: 'Movimentações: saldo provisionado fixo no cabeçalho entre jornadas; CEP, CEP Plus, limite e lançamentos contextualizados no módulo.',
      p: 'No discovery da transição do Extrato EA para o IFA, comparei seis alternativas e defini o saldo provisionado persistente no cabeçalho. Conta corrente, investimentos, conta gráfica e limites permaneceram em Movimentações para não sobrecarregar a navegação global. Etapa de discovery e prototipagem, sem medição em produção neste recorte.'
    },
    {
      num: '04',
      tag: 'GESTÃO DE CAMPANHAS',
      short: 'Gestão de Campanhas',
      title: 'Sincronizar configuração da base, execução comercial e visão gerencial por estados explícitos.',
      imgKey: 'itau_campanhas',
      caption: 'Gestão de Campanhas: separa configuração da base, estados de processamento e ativação para alinhar administradores de backoffice, especialistas e gestores.',
      p: 'Conduzi os fluxos de tela de criação, importação de base e manutenção em lote com estados explícitos de carregamento, vazio, processamento e erro. Separei configuração e ativação, aceitando um passo extra de conferência para evitar publicar bases incompletas.'
    },
    {
      num: '05',
      tag: 'REGISTROS DE ATENDIMENTO · IA',
      short: 'Registros de Atendimento com IA',
      title: 'Aproximar os 5 últimos resumos e exigir confirmação humana antes de gravar notas assistidas por IA.',
      imgKey: 'itau_registros',
      caption: 'Registros de Atendimento (diagrama ilustrativo): aproxima os 5 últimos resumos e exige confirmação humana obrigatória (Human-in-the-Loop) antes da gravação no prontuário.',
      p: 'Conduzi a arquitetura de interação para aproximar os 5 últimos resumos e gerar minutas preliminares editáveis assistidas por IA. Descartei salvamento automático e defini revisão e confirmação humana obrigatória antes da gravação para preservar fidelidade técnica e conformidade bancária.'
    }
  ]
};

var CASE_CLARO = {
  name: 'Case Claro Brasil',
  frameName: 'Case · Claro Brasil — Ativação Simplificada',
  kickerTag: 'TELECOM · UX CORPORATIVO',
  kickerCompany: 'Claro Brasil · 2017–2018',
  title: '22 jornadas comerciais unificadas em uma esteira desktop e mobile.',
  subtitle: 'Na Claro Brasil (NET, Claro e Embratel), conduzi o desenho de fluxos e interfaces como UX/UI Designer. Unificamos 22 jornadas comerciais em uma esteira desktop e mobile de 5 etapas, com 70 oportunidades priorizadas e especificações V.2 entregues à engenharia, sem medição pós-implantação neste ciclo.',
  metadata: [
    { label: 'MEU PAPEL', val: 'UX/UI Designer' },
    { label: 'EQUIPE', val: 'Design, Produto, Engenharia de sistemas e operação comercial' },
    { label: 'ESCOPO', val: 'Discovery, 22 jornadas, protótipos e especificação desktop e mobile' },
    { label: 'ENTREGA PRINCIPAL', val: '22 jornadas unificadas · 70 oportunidades (especificações V.2)' }
  ],
  heroImgKey: 'claro_capa',
  heroCaption: 'Por que unificar desktop e mobile na mesma arquitetura: reunir 22 jornadas de NET, Claro e Embratel evita que o operador alterne entre sistemas legados durante a venda.',
  metrics: [
    { n: '20', d: 'entrevistas em profundidade' },
    { n: '22', d: 'jornadas unificadas na esteira' },
    { n: '70', d: 'oportunidades priorizadas' },
    { n: '5', d: 'etapas na esteira unificada' },
    { n: '2', d: 'canais (desktop V.2 e mobile)' }
  ],
  prevCaseTitle: 'Itaú Unibanco · Hub de Liquidez',
  nextCaseTitle: 'Neoenergia · Service Design',
  chapters: [
    {
      num: '01',
      tag: 'OPERAÇÃO FRAGMENTADA',
      short: 'Contexto e pesquisa operacional',
      title: 'Redesenho da operação comercial e redução de atrito na venda multicanal.',
      imgKey: 'claro_ativacao',
      caption: 'Por que validar o CPF na entrada: antecipar checagens cadastrais e antifraude antes da oferta evita montar um combo inelegível. Dados sintetizados sob LGPD.',
      p: 'Entre 2017 e 2018, benchmarking competitivo, 20 entrevistas em profundidade com operadores e lideranças, três dias de workshops e 10 perfis operacionais mostraram que o principal gargalo estava na troca manual de sistemas legados. Conduzi síntese, arquitetura de fluxos, protótipos e especificações desktop (V.2) e mobile.'
    },
    {
      num: '02',
      tag: '22 JORNADAS EM 5 ETAPAS',
      short: 'Decisões 1 e 2 (Esteira e desacordo)',
      title: 'Decomposição de 22 jornadas comerciais em uma esteira unificada.',
      imgKey: 'claro_jornadas',
      caption: 'Por que mapear a troca de chip antes das telas: expor dependências de validação, oferta e resumo financeiro revelou etapas duplicadas entre fluxos.',
      p: 'Decisão 1: propus consolidar 22 fluxos isolados em 5 etapas, aceitando mapear exceções por transação para eliminar validações duplicadas. Decisão 2 (desacordo construtivo): lideranças comerciais pediram tela única para reduzir cliques; demonstrei em sessões práticas com operadores que a densidade sem hierarquia aumentava erros. Negociei etapas progressivas com resumo financeiro lateral fixo.'
    },
    {
      num: '03',
      tag: 'CONTEXTO FIXO E RESUMO LATERAL',
      short: 'Cabeçalho fixo e resumo financeiro',
      title: 'Navegação progressiva, resumo financeiro visível e preservação do contexto do cliente.',
      imgKey: 'claro_capa',
      caption: 'Por que manter cabeçalho fixo e blocos expansíveis: o operador consulta linha, plano e fatura sem abandonar a venda nem perder os dados do cliente (LGPD).',
      p: 'Estruturei três regras de arquitetura de informação: 1. Navegação progressiva por etapas numeradas, 2. Cabeçalho fixo preservando dados da linha e status cadastral, e 3. Resumo financeiro lateral exibindo produtos, descontos aplicados e valor final durante toda a montagem da oferta.'
    },
    {
      num: '04',
      tag: 'PARIDADE DESKTOP E MOBILE',
      short: 'Decisão 3 (Consistência multicanal)',
      title: 'Da jornada do chip às interfaces desktop e mobile padronizadas.',
      imgKey: 'claro_multicanal',
      caption: 'Por que preservar a mesma taxonomia entre desktop e mobile: manter nomes de planos, resumo financeiro lateral e confirmação iguais reduz divergências entre lojas físicas e campo.',
      p: 'Decisão 3: entre replicar a tela densa do desktop no mobile ou criar fluxos independentes para o campo, mantive a mesma taxonomia, ordem de 5 etapas e confirmação adaptando a densidade visual. Aceitamos mais rolagem e blocos recolhidos no mobile para preservar continuidade operacional entre lojas físicas e campo.'
    },
    {
      num: '05',
      tag: 'ENTREGA, ESCOPO E REFLEXÃO',
      short: 'Status V.2, escopo, reflexão e NDA',
      title: 'Especificações entregues, escopo preservado e o que eu reverteria hoje.',
      imgKey: 'claro_capa',
      caption: 'Especificações desktop (V.2, 10/05/2018) e mobile (11/06/2018) entregues à engenharia; implantação sob gestão interna da Claro Brasil e arquivos sob NDA.',
      p: 'O ciclo encerrou com 22 jornadas unificadas, 70 oportunidades e especificações desktop (V.2) e mobile entregues à engenharia, sem medição quantitativa pós-implantação neste ciclo. Fora do recorte: faturamento legado e regras de crédito de backoffice. Reflexão: eu reverteria encerrar a entrega V.2 sem acordar uma linha de base de tempo por etapa e taxa de erro antes da implantação.'
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
    'Design de produtos para saúde, finanças e serviços essenciais.',
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
    'Com mais de 15 anos de experiência, estruturo fluxos operacionais e sistemas de interface com Produto e Engenharia. No Itaú Unibanco, conduzi pesquisa e design no íon for Advisors para especialistas de investimentos e assessores.',
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
  btnPrimary.name = 'Btn Ver projetos';
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
  var btnTxt1 = await createTextNode('Ver projetos', 14, 'semibold', TOKENS.colors.canvas);
  btnPrimary.appendChild(btnTxt1);
  ctaRow.appendChild(btnPrimary);

  var btnSec = figma.createFrame();
  btnSec.name = 'Btn Currículo (PDF)';
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
  var btnTxt2 = await createTextNode('Currículo (PDF)', 14, 'semibold', TOKENS.colors.textPrimary);
  btnSec.appendChild(btnTxt2);
  ctaRow.appendChild(btnSec);

  heroLeft.appendChild(ctaRow);
  heroRow.appendChild(heroLeft);

  // 2.2 Coluna Direita: Retrato Executivo Compacto (400px × 340px)
  var portraitCard = createVerticalContainer('Executive Portrait Card', 400, 10, { left: 16, right: 16, top: 16, bottom: 16 }, TOKENS.colors.card, TOKENS.colors.borderSubtle, TOKENS.radius.card, true);
  var portraitImg = await createRealImageFigure('home_portrait', null, 368, 280, TOKENS.radius.panel);
  portraitCard.appendChild(portraitImg);

  var metaStrip = createHorizontalRow('Portrait Meta Strip', 368, 0, null, null, null, null, 'SPACE_BETWEEN', 'CENTER');
  var pRole = await createTextNode('Israel Rozar', 12, 'semibold', TOKENS.colors.textPrimary);
  var pCorps = await createTextNode('ITAÚ · EINSTEIN · R/GA · EY', 12, 'semibold', TOKENS.colors.textSecondary);
  metaStrip.appendChild(pRole);
  metaStrip.appendChild(pCorps);
  portraitCard.appendChild(metaStrip);

  heroRow.appendChild(portraitCard);
  container.appendChild(heroRow);

  // 3. Career Metrics Bar (4 Colunas com Alinhamento Uniforme)
  var metricsBar = createHorizontalRow('Career Metrics Bar', 1152, 20, { left: 28, right: 28, top: 20, bottom: 20 }, TOKENS.colors.subtle, TOKENS.colors.borderSubtle, 16, 'SPACE_BETWEEN', 'MIN');
  var cMetrics = [
    { t: 'Atuação B2B e Corporativa', d: 'Mais de 15 anos em produtos digitais, com foco em plataformas transacionais e operações de dados.' },
    { t: 'Domínios Regulados', d: 'Atuação em plataformas financeiras no Itaú (IFA), laudos clínicos no Einstein, telecom e energia.' },
    { t: 'Sistemas de Interface', d: 'Estruturação de bibliotecas de componentes, tokens semânticos e handoff com Engenharia.' },
    { t: 'Acessibilidade e IA', d: 'Critérios WCAG 2.2 AA/AAA desde a concepção e uso prático de IA com revisão humana.' }
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
  var tickerWords = ['ARQUITETURA DA INFORMAÇÃO', '•', 'PESQUISA COM USUÁRIOS', '•', 'TOKENS SEMÂNTICOS', '•', 'ENTREVISTAS EM PROFUNDIDADE', '•', 'WCAG 2.2 AA/AAA'];
  for (var tw = 0; tw < tickerWords.length; tw++) {
    var isBullet = (tickerWords[tw] === '•');
    var tNode = await createTextNode(tickerWords[tw], 12, 'bold', isBullet ? TOKENS.colors.acidLime : TOKENS.colors.deepPine);
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
    'Pesquisa e arquitetura da informação para organizar laudos de diferentes exames em uma estrutura modular comum, preservando o contexto clínico.',
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
    { n: '14', d: 'entregáveis documentados' },
    { n: '121', d: 'pacientes no questionário' },
    { n: '4', d: 'médicos especialistas' }
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
      client: 'ITAÚ UNIBANCO',
      title: 'Hub de Liquidez e Oportunidades',
      desc: 'Organização de saldos, projeções e oportunidades para especialistas de investimentos e assessores na plataforma íon for Advisors.',
      tagVal: 'íon for Advisors',
      tagDesc: '5 módulos documentados',
      thumbBuilder: buildHomeCardThumbItauHub
    },
    {
      num: '02',
      client: 'ITAÚ UNIBANCO',
      title: 'Gestão de Vencimentos',
      desc: 'Consolidação de vencimentos, eventos futuros e Open Finance com filtros operacionais para especialistas de investimentos e assessores.',
      tagVal: 'Visão Canônica',
      tagDesc: 'filtros, estados e atuação',
      thumbBuilder: buildHomeCardThumbItauVenc
    },
    {
      num: '03',
      client: 'NEOENERGIA',
      title: 'Atendimento e operação de campo',
      desc: 'Mapeamento de jornadas e serviços para conectar o atendimento digital à operação em campo nas 4 distribuidoras.',
      tagVal: '4 Distribuidoras',
      tagDesc: '5 Service Blueprints · 118 ideias',
      thumbBuilder: buildHomeCardThumbNeoenergia
    },
    {
      num: '04',
      client: 'CLARO BRASIL',
      title: 'Ativação de planos e televendas',
      desc: 'Unificação da jornada de venda e ativação de planos para equipes de lojas físicas, televendas e campo.',
      tagVal: '22 Jornadas',
      tagDesc: '20 entrevistas · 70 oportunidades',
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
  var provHome = await buildProvenanceBanner(1152);
  container.appendChild(provHome);

  container.primaryAxisSizingMode = 'AUTO';
  container.clipsContent = false;

  parent.appendChild(container);
  log('✔ Home construída com sucesso total e todas as seções!');
  return container;
}
"""

js_dispatcher = r"""
// ============================================================================
// COMPONENTE DE PROVENIÊNCIA & RASTREABILIDADE (IA + DATAS + CONVERSA ID)
// ============================================================================
var PROVENANCE_META = {
  aiPlatform: 'Antigravity (Google DeepMind)',
  version: 'v3.10.2 (Produção GitHub Pages)',
  createdAt: '2026-11-01',
  updatedAt: '2026-11-26 10:45 BRT',
  conversationId: 'b9eff66e-96f2-48ed-af7d-28e8cea0dfad',
  conversationLink: 'conversation://b9eff66e-96f2-48ed-af7d-28e8cea0dfad',
  liveUrl: 'https://israelfull-commits.github.io/portfolio/',
  notionHub: 'https://app.notion.com/p/4168db39b34f805884bad8f933e004dd'
};

async function buildProvenanceBanner(width) {
  var w = width || 1152;
  var box = createVerticalContainer(
    'Proveniência · Antigravity ' + PROVENANCE_META.version,
    w,
    8,
    { top: 16, right: 24, bottom: 16, left: 24 },
    TOKENS.colors.deepPine,
    TOKENS.colors.acidLime,
    12,
    false
  );
  var line1 = await createTextNode(
    'PROVENIÊNCIA & RASTREABILIDADE  ·  Criado/Atualizado no ' + PROVENANCE_META.aiPlatform + '  ·  ' + PROVENANCE_META.version,
    11,
    'bold',
    TOKENS.colors.acidLime,
    w - 48,
    null,
    16,
    0.8
  );
  var line2 = await createTextNode(
    'Data de criação: ' + PROVENANCE_META.createdAt +
    '   |   Última atualização: ' + PROVENANCE_META.updatedAt +
    '   |   Chat ID: ' + PROVENANCE_META.conversationId +
    '\nLink da conversa: ' + PROVENANCE_META.conversationLink +
    '   |   Produção: ' + PROVENANCE_META.liveUrl +
    '   |   Notion Ops: ' + PROVENANCE_META.notionHub,
    12,
    'regular',
    TOKENS.colors.canvas,
    w - 48,
    null,
    18
  );
  box.appendChild(line1);
  box.appendChild(line2);
  return box;
}

// ============================================================================
// PRANCHA DE DOCUMENTAÇÃO DESIGN SYSTEM, COMPONENTES, REGRAS & HANDOFF V3.10.2
// ============================================================================
async function buildDesignSystemDocsFrame(parent, xPos, yPos) {
  await loadFonts();
  var docFrame = createVerticalContainer('Documentação · Design System, Componentes & Handoff V3.10.2', 1280, 24, { top: 48, right: 64, bottom: 64, left: 64 }, TOKENS.colors.canvas, TOKENS.colors.border, 0, false);
  docFrame.x = xPos;
  docFrame.y = yPos;

  var headerBadge = await createBadge('GOVERNANÇA, DESIGN SYSTEM & HANDOFF · V3.10.2', TOKENS.colors.deepPine, TOKENS.colors.acidLime, true);
  docFrame.appendChild(headerBadge);

  var title = await createTextNode('Documentação Canônica V3.10.2: Design System, Componentes, Regras, Handoff & Versões', 36, 'bold', TOKENS.colors.textPrimary, 1152, null, 44, -0.8);
  docFrame.appendChild(title);

  var subtitle = await createTextNode('Fonte única sincronizada 1:1 com o código React/Vite em produção (GitHub Pages), espelho local (portfolio-verde/) e Notion Portfolio Ops. Score 99/100 · UX Companion 30/30 · Sentinel v2 14/14 PASS.', 16, 'regular', TOKENS.colors.textSecondary, 1152, null, 24);
  docFrame.appendChild(subtitle);

  var topProv = await buildProvenanceBanner(1152);
  docFrame.appendChild(topProv);

  var sections = [
    {
      tag: '01 · PALETA SEMÂNTICA UNIFICADA (HOME ↔ CASES) & WCAG 2.2 AAA',
      body: '• Papel Canônico (--paper #F4F2E9) + Ink (--ink #111B15): contraste > 14:1 (AAA)\n• Superfície Elevada (--paper-deep #E9E6DA) + Borda (--line #D2D4CA) + Ink Muted (#3B4740): > 7.5:1 (AAA)\n• Forest Pine (--forest #173E2D / --forest-deep #10291E) + Texto Claro (#F4F2E9): > 11.5:1 (cards .cp-note)\n• Acid Lime (--lime #D9FF63) + Ink Escuro (#172019): > 11:1 (Regra: Lime nunca usa texto branco)\n• Focus Visible (--focus #174FDA): outline >= 2px (0.2rem) + scroll-padding-top 88px (WCAG 2.2 2.4.11 / 2.4.13)'
    },
    {
      tag: '02 · TIPOGRAFIA MONOTÔNICA & GRID ESTRITO BASE 8PX',
      body: '• Família única: Plus Jakarta Sans (400, 600, 700) embutida localmente em site/src/assets/fonts/\n• Home (/): H1 56px -> H2 32px -> H3 24px -> Body 16px (100% monotônica, zero colisão H2/H3)\n• Cases: H1 56px -> H2 36px -> H3 19px -> Caption 14px -> Body 16px\n• Grid estrito 8px: .cp-chapter padding-bottom 72px | .cp-split padding 24px / gap 32px | .cp-note 24px 32px | .cp-cards-grid gap 24px\n• Responsividade: 0px overflow horizontal validado em 1440px, 768px e 390px'
    },
    {
      tag: '03 · BIBLIOTECA DE COMPONENTES CANÔNICOS & ESTADOS',
      body: '• SiteHeader: barra fixa com blur (.is-scrolled > 12px), <= 6 itens de navegação e contato anti-spam dinâmico\n• CaseAccessGate: proteção híbrida padrão nos cases (Home aberta), validação exclusiva por hash SHA-256 em sessionStorage, autoComplete="current-password" e paste liberado (WCAG 2.2 3.3.8)\n• Master Hero (.cp-hero-visual): 1120x630px edge-to-edge (16:9, aspectDiff = 0.0000, 0px letterboxing) com Combo Campeão 2400x1350 WebP\n• CaseFigure (.cp-figure): estilo único em todo o site (0px padding, fundo transparente, borda arredondada) + Lightbox 96vw x 94vh com zoom 1:1 no clique\n• CasePresentation: suporta id, tag e contagem própria de capítulos por case (eliminação total de template repetido)'
    },
    {
      tag: '04 · REGRAS PERMANENTES & BOAS PRÁTICAS (AGENTS.MD SEÇÕES 1–11)',
      body: '• Anti-Template de Bootcamp: Einstein (6 caps) · Itaú Decision-Led (5 caps, decisões no cap. 2) · Claro Multicanal (5 caps) · Neoenergia Service Design (6 caps)\n• UX Companion 2026 (30/30) + NN/g: Hero 15s, Framing com tensão nomeada, 3 Decisões com trade-offs, Outcomes com atribuição honesta (Contínuas/Discretas/Binárias), Reflection concreta e Disciplina de Escopo\n• Postura Editorial: zero termos defensivos/clichês, dados sintetizados/anonimizados sob LGPD, sigilo médico e bancário\n• Proveniência Obrigatória: toda prancha Figma e doc canônico informa IA (Antigravity), data de criação, última atualização e ID/link da conversa'
    },
    {
      tag: '05 · HANDOFF TÉCNICO, ROTAS SPA & AUTOMAÇÃO QA (15 GATES)',
      body: '• Stack: React 19 + Vite 6 + TypeScript + React Router 7 | Ativos 100% via assetUrl() para subdiretório /portfolio/\n• Rotas SPA Estáticas: generate_spa_routes.js gera index.html com title/OG/canonical próprios para todas as 8 rotas + 404.html (HTTP 200 OK direto)\n• Script Único de Validação: scripts/portfolio_qa_sentinel.py (15/15 PASS: 10 estáticos + 5 Chromium runtime incluindo WCAG 2.2 2.4.11/2.4.13/2.5.8/3.3.8, contraste :hover e Gate 15 TX/TH)\n• Automação em 3 Camadas: Hook .githooks/pre-push (bloqueio local) + npm run qa / qa:full / qa:sync + CI Gate em .github/workflows/deploy.yml\n• Higiene do Repositório: raiz com arquivos canônicos e scripts/ com 2 motores oficiais (legados arquivados em D:\\arquivo-morto-portfolio\\)'
    },
    {
      tag: '06 · HISTÓRICO COMPLETO DE VERSÕES (V0.1 ➔ V4.2.0)',
      body: '• v0.1.0 (UXfolio · Score 52): baseline inicial sem controle de a11y ou trade-offs\n• v2.0.0–v3.0.0 (Figma Make · Score 67–73): identidade visual inicial e primeiros cases estruturados\n• v3.5.0–v3.8.0 (GitHub Pages · Score 87–99): código React próprio, 4 arquiteturas sob medida, CaseAccessGate SHA-256 e Sentinel v2\n• v3.9.0–v4.0.2 (Guia Consolidado 2026): 90 códigos congelados, 3 skills, Home Híbrida V4.0.0 e auditoria integral do Hero\n• v4.1.0–v4.1.1 (Auditoria Editorial & CTAs): saneamento integral de textos, remoção de botões duplicados em #sobre e padronização A-23\n• v4.2.0 (VIGENTE · Varredura Exaustiva dos Cases): 3 decisões no micro-template CS-06 em todos os cases, CS-01 de 4 frases, metaDescription + OG estático por rota, A-01 corrigido na Neoenergia, 21,6 p.p. no Einstein, 0 invenções no plugin Figma e paridade 1:1 omnicanal'
    }
  ];

  for (var s = 0; s < sections.length; s++) {
    var sec = sections[s];
    var card = createVerticalContainer(sec.tag, 1152, 12, { top: 24, right: 24, bottom: 24, left: 24 }, TOKENS.colors.white, TOKENS.colors.border, 16, true);
    var sTag = await createTextNode(sec.tag, 12, 'bold', TOKENS.colors.deepPine, 1104, null, 18, 0.8);
    var sBody = await createTextNode(sec.body, 14, 'regular', TOKENS.colors.textPrimary, 1104, null, 24);
    card.appendChild(sTag);
    card.appendChild(sBody);
    docFrame.appendChild(card);
  }

  parent.appendChild(docFrame);
  log('✔ Prancha de Documentação, Componentes & Handoff V4.2.0 criada com sucesso!');
  return docFrame;
}

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
  else if (msg.type === 'create_ds_docs') {
    updateStatus('Construindo Prancha de Documentação, Componentes & Handoff V3.10.2...');
    try {
      var docNode = await buildDesignSystemDocsFrame(figma.currentPage, 7200, 0);
      figma.viewport.scrollAndZoomIntoView([docNode]);
      updateStatus('Concluído: Documentação & Handoff V3.10.2 gerada no Figma!');
      figma.notify('✔ Prancha de Documentação & Handoff V3.10.2 gerada!');
    } catch (e) {
      log('Erro ao criar Documentação V3.10.2: ' + e);
      updateStatus('Erro na geração.');
    }
  }
  else if (msg.type === 'create_all_screens') {
    updateStatus('Construindo todas as telas mestres + Documentação & Handoff V3.10.2...');
    try {
      log('=== INICIANDO GERAÇÃO DE TODAS AS TELAS (TEMPLATE + HOME + 4 CASES + DOCS/HANDOFF V3.10.2) ===');
      var templateNode = await buildGenericCaseScreen(figma.currentPage, -1440, 0, CASE_TEMPLATE);
      var homeNode = await buildHome(figma.currentPage, 0, 0);
      var neoNode = await buildGenericCaseScreen(figma.currentPage, 1440, 0, CASE_NEOENERGIA);
      var einNode = await buildGenericCaseScreen(figma.currentPage, 2880, 0, CASE_EINSTEIN);
      var itauNode = await buildGenericCaseScreen(figma.currentPage, 4320, 0, CASE_ITAU);
      var claroNode = await buildGenericCaseScreen(figma.currentPage, 5760, 0, CASE_CLARO);
      var docsNode = await buildDesignSystemDocsFrame(figma.currentPage, 7200, 0);
      
      figma.viewport.scrollAndZoomIntoView([templateNode, homeNode, neoNode, einNode, itauNode, claroNode, docsNode]);
      updateStatus('Concluído: Telas Mestres e Documentação/Handoff V3.10.2 Criados!');
      figma.notify('🎉 Todas as telas + Documentação/Handoff V3.10.2 foram geradas com Proveniência Antigravity!');
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
    <button class="btn" onclick="triggerAction('create_ds_docs')">
      <span>📐 Documentação Design System, Componentes & Handoff V3.10.2</span>
      <span>Prancha Canônica</span>
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
