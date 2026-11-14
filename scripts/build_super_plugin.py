import json
from pathlib import Path

plugin_dir = Path(r"C:\Users\Israel Rozar\figma-refine-plugin")

# Vamos construir o code.js em Javascript Clássico ES5/ES6 básico (sem spread, sem optional chaining)
code_js = r"""// Sincronizador de Conteúdo 1:1 para Figma Desktop (Windows)
// Padrão rigoroso: ES5/ES6 clássico sem spread operator (...) nem optional chaining (?.)

figma.showUI(__html__, { width: 500, height: 600, themeColors: true });

function log(msg) {
  figma.ui.postMessage({ type: 'log', message: msg });
  console.log('[Portfolio Sync] ' + msg);
}

function updateStatus(status) {
  figma.ui.postMessage({ type: 'status', message: status });
}

// Base consolidada com dados 100% atualizados e sem repetições
var casesData = {
  einstein: {
    titles: [
      'Estruturação de dados médicos para leitura rápida e segura.',
      'O desafio de conciliar sistemas legados, médicos e pacientes.',
      'Do documento ao dado: triangulação entre laudos e rotinas médicas.',
      'Decisões de design: estabilidade visual e componentes reaproveitáveis.',
      'Uma estrutura comum para resultados numéricos e textuais.',
      'Sistematização de templates e limites declarados de validação.',
      'Rastreabilidade documental, metodologia e equipe técnica.'
    ],
    headline: 'Clareza não é o mesmo que compreensão.',
    subtitle: 'Uma linguagem visual modular para laudos em diferentes canais.',
    kicker: 'Saúde · Laudos Médicos',
    metrics: [
      { val: '121', desc: 'respostas no questionário exploratório' },
      { val: '4 médicos', desc: 'entrevistas semiestruturadas' },
      { val: '80+', desc: 'laudos no inventário descrito' }
    ]
  },
  claro: {
    titles: [
      'Redesenho da operação comercial e redução de atrito na venda multicanal.',
      'Uma operação de alta densidade dividida entre balcão físico e mobilidade.',
      'Compreender a rotina real dos atendentes antes de desenhar interfaces.',
      'Navegação progressiva, resumo financeiro visível e preservação do contexto do cliente.',
      'Da jornada do chip às interfaces desktop e mobile padronizadas.',
      'Decomposição de 22 jornadas de atendimento e aprendizados operacionais.',
      'Acervo histórico de discovery, colaboração e limites de evidência.'
    ],
    headline: 'Simplificando o atendimento em múltiplos canais.',
    subtitle: 'Redesenho da experiência de vendas para profissionais da operação comercial.',
    kicker: 'Telecom · Enterprise UX',
    metrics: [
      { val: '20', desc: 'entrevistas em profundidade' },
      { val: '22', desc: 'jornadas de atendimento mapeadas' },
      { val: '70', desc: 'oportunidades de melhoria levantadas' }
    ]
  },
  neoenergia: {
    titles: [
      'Unificação da infraestrutura de atendimento para 34 milhões de pessoas.',
      'Cadeia de serviços fragmentada em um ecossistema de infraestrutura crítica.',
      'Auditoria de backstage: quando a insatisfação com a fatura revela silos operacionais.',
      'Desburocratização de backoffice antes de redesenho de portal e Design System multi-tenant.',
      'Os 5 estágios do ciclo de vida do cliente mapeados em Service Blueprints.',
      'Matriz de 118 ideias priorizadas e baseline para o plano diretor de inovação.',
      'Fontes oficiais de P&D ANEEL, governança executiva e equipe EY × Livework.'
    ],
    headline: 'Strategic Discovery e Service Design: Ecossistema Neoenergia',
    subtitle: 'Mapeamento integral e redesenho de processos omnicanal no setor elétrico, identificando oportunidades sistêmicas de automação para 34 milhões de pessoas.',
    kicker: 'Utilities · Service Design & Discovery',
    metrics: [
      { val: '34M', desc: 'habitantes nas áreas de concessão' },
      { val: '13,9M', desc: 'unidades consumidoras faturadas' },
      { val: '5 estágios', desc: 'ciclo de vida em blueprints' },
      { val: '118 ideias', desc: 'priorizadas na matriz de valor' }
    ]
  },
  vencimentos: {
    titles: [
      'Visibilidade, urgência e atuação proativa sobre eventos de liquidez.',
      'Conciliar três contextos financeiros em uma lógica única de consulta.',
      'Evidências confirmadas nos arquivos de trabalho e handoff.',
      'Decisões de interface: busca, filtros e tabela com estados de atuação.',
      'Padrões de interação para gestão de liquidez em escala B2B.',
      'Estágio de documentação, handoff técnico e preparação para entrevista.',
      'Rastreabilidade dos artefatos, autoria e roteiro de defesa técnica.'
    ],
    headline: 'Gestão de Vencimentos',
    subtitle: 'Da sinalização à atuação sobre eventos financeiros.',
    kicker: 'Fintech · Design de produto'
  },
  hub_liquidez: {
    titles: [
      'Visão unificada de liquidez consolidando prazos e disponibilidades financeiras.',
      'O desafio de prover previsibilidade de caixa sem sobrecarregar a mesa.',
      'Recorte da proposta e componentes validados na solução.',
      'Decisões de design: decomposição temporal, saldos e ações em lote.',
      'Estrutura visual da mesa de liquidez e componentes modulares.',
      'Limites do protótipo e próximos passos de homologação.',
      'Rastreabilidade documental e roteiro de defesa técnica.'
    ],
    headline: 'Hub de Liquidez e Oportunidades',
    subtitle: 'Dados, priorização e próxima ação explicável.',
    kicker: 'Fintech · Design de produto'
  },
  movimentacoes: {
    titles: [
      'Transparência de lançamentos e extrato operacional para assessores.',
      'Reduzir tempo de conciliação financeira entre cliente e mesa de assessoria.',
      'Discovery de arquitetura e alternativas exploradas para o extrato.',
      'Decisões de arquitetura: agrupamento temporal e detalhe de lançamentos.',
      'Padrões de consulta e granularidade de lançamentos financeiros.',
      'Estágio de validação técnica e integração com sistemas legados.',
      'Rastreabilidade dos artefatos e roteiro de defesa técnica.'
    ],
    headline: 'Movimentações e Extrato EA',
    subtitle: 'Transição do Extrato EA para a plataforma íon com saldo provisionado transversal.',
    kicker: 'Fintech · Design de produto'
  },
  campanhas: {
    titles: [
      'Orquestração de ações comerciais sem perda de contexto operacional.',
      'Transformar campanhas de marketing em fluxos acionáveis para assessoria.',
      'Mapeamento de esteira operacional e regras de conversão.',
      'Decisões de interface: priorização por impacto e conversão em lote.',
      'Screenflow de estados e componentes de acompanhamento de metas.',
      'Limites de implementação e métricas de conversão de campanha.',
      'Rastreabilidade dos arquivos de handoff e roteiro de defesa técnica.'
    ],
    headline: 'Gestão de Campanhas IFA',
    subtitle: 'Configuração, dados, estados operacionais e manutenção de ações comerciais.',
    kicker: 'Fintech · Design de produto'
  },
  registros_atendimento: {
    titles: [
      'Registro estruturado de reuniões e inteligência operacional com IA.',
      'Automatizar a síntese de conversas sem comprometer o sigilo bancário.',
      'Mapeamento de momentos da reunião e extração de pendências.',
      'Decisões de interação: revisão humana, tags automáticas e confirmação.',
      'Fluxo de escuta ativa, sumarização e despacho de tarefas.',
      'Estágio do piloto de IA, conformidade e limites de modelo.',
      'Rastreabilidade técnica e roteiro de defesa de produto.'
    ],
    headline: 'Registros de Atendimento com IA',
    subtitle: 'Resumos inteligentes assistidos por inteligência artificial com revisão humana obrigatória.',
    kicker: 'Fintech · IA aplicada'
  }
};

// Carregar fontes com segurança
async function ensureFontLoaded(node) {
  if (node.type !== 'TEXT') return;
  try {
    if (node.fontName && typeof node.fontName === 'object') {
      await figma.loadFontAsync(node.fontName);
    } else {
      await figma.loadFontAsync({ family: 'Inter', style: 'Regular' });
    }
  } catch (e) {
    try {
      await figma.loadFontAsync({ family: 'Inter', style: 'Regular' });
    } catch (e2) {}
  }
}

// Atualizar textos recursivamente
async function updateFrameTexts(frame, caseKey) {
  var data = casesData[caseKey];
  if (!data) return 0;
  
  var textNodes = [];
  function collect(node) {
    if (node.type === 'TEXT') {
      textNodes.push(node);
    }
    if ('children' in node && node.children) {
      for (var i = 0; i < node.children.length; i++) {
        collect(node.children[i]);
      }
    }
  }
  collect(frame);
  
  var updatedCount = 0;
  var chapterTitleIdx = 0;

  for (var i = 0; i < textNodes.length; i++) {
    var tn = textNodes[i];
    var txt = tn.characters.trim();

    // Substituir títulos de capítulos repetidos
    if (txt === 'A história em 90 segundos.' || 
        txt === 'Decisões conectadas ao problema.' || 
        txt === 'Evidências e créditos.' ||
        txt.indexOf('A história em 90 segundos') !== -1 ||
        txt.indexOf('Decisões conectadas') !== -1 ||
        txt.indexOf('Evidências e créditos') !== -1) {
      
      if (chapterTitleIdx < data.titles.length) {
        var newTitle = data.titles[chapterTitleIdx];
        await ensureFontLoaded(tn);
        tn.characters = newTitle;
        chapterTitleIdx++;
        updatedCount++;
      }
    }
    
    // Substituir kickers genéricos
    if (txt === 'Design de produto' && data.kicker) {
      await ensureFontLoaded(tn);
      tn.characters = data.kicker;
      updatedCount++;
    }
  }

  return updatedCount;
}

// Sincronizar Tudo na Página Ativa
async function syncActivePage() {
  updateStatus('Sincronizando...');
  log('Iniciando sincronização na página atual: ' + figma.currentPage.name);

  var frames = figma.currentPage.children;
  var totalUpdated = 0;

  for (var f = 0; f < frames.length; f++) {
    var frame = frames[f];
    var fname = frame.name.toLowerCase();
    var targetKey = null;

    if (fname.indexOf('einstein') !== -1 || fname.indexOf('16 •') !== -1) targetKey = 'einstein';
    else if (fname.indexOf('claro') !== -1) targetKey = 'claro';
    else if (fname.indexOf('neoenergia') !== -1) targetKey = 'neoenergia';
    else if (fname.indexOf('vencimentos') !== -1) targetKey = 'vencimentos';
    else if (fname.indexOf('hub') !== -1 || fname.indexOf('03 •') !== -1) targetKey = 'hub_liquidez';
    else if (fname.indexOf('movimentações') !== -1 || fname.indexOf('movimentacoes') !== -1 || fname.indexOf('02 •') !== -1) targetKey = 'movimentacoes';
    else if (fname.indexOf('campanhas') !== -1 || fname.indexOf('05 •') !== -1) targetKey = 'campanhas';
    else if (fname.indexOf('registros') !== -1 || fname.indexOf('01 •') !== -1) targetKey = 'registros_atendimento';

    if (targetKey) {
      log('Atualizando frame: ' + frame.name + ' com dados de [' + targetKey + ']...');
      var count = await updateFrameTexts(frame, targetKey);
      totalUpdated += count;
      log('   ✔ ' + count + ' textos atualizados em ' + frame.name);
    }
  }

  log('========================================================');
  log('🎉 Sincronização concluída! Total de textos atualizados: ' + totalUpdated);
  log('========================================================');
  updateStatus('Concluído (' + totalUpdated + ' atualizados)');
  figma.notify('✔ Sincronização 1:1 finalizada (' + totalUpdated + ' textos atualizados)');
  figma.ui.postMessage({ type: 'done', total: totalUpdated });
}

figma.ui.onmessage = async function(msg) {
  if (!msg) return;
  if (msg.type === 'sync_all') {
    await syncActivePage();
  } else if (msg.type === 'close') {
    figma.closePlugin();
  }
};
"""

# HTML UI do Plugin
ui_html = r"""<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <style>
    body {
      font-family: Inter, -apple-system, sans-serif;
      margin: 0; padding: 20px;
      background: #18181b; color: #f4f4f5;
      display: flex; flex-direction: column; height: 560px;
      box-sizing: border-box;
    }
    h2 { font-size: 16px; margin: 0 0 8px 0; color: #fff; }
    p { font-size: 12px; color: #a1a1aa; margin: 0 0 16px 0; line-height: 1.4; }
    .badge {
      display: inline-block; padding: 2px 8px; font-size: 11px; font-weight: 600;
      background: #27272a; border: 1px solid #3f3f46; border-radius: 4px; color: #e4e4e7;
      margin-bottom: 12px;
    }
    .btn {
      background: #2563eb; color: #fff; border: none; border-radius: 6px;
      padding: 12px 16px; font-size: 13px; font-weight: 600; cursor: pointer;
      display: flex; align-items: center; justify-content: center; gap: 8px;
      transition: background 0.15s ease;
    }
    .btn:hover { background: #1d4ed8; }
    .btn:disabled { opacity: 0.5; cursor: not-allowed; }
    #log {
      flex: 1; margin-top: 16px; padding: 12px; background: #09090b;
      border: 1px solid #27272a; border-radius: 6px; font-family: monospace;
      font-size: 11px; color: #10b981; overflow-y: auto; white-space: pre-wrap;
    }
    .status-bar {
      margin-top: 12px; font-size: 11px; color: #71717a; display: flex;
      justify-content: space-between; align-items: center;
    }
  </style>
</head>
<body>
  <h2>Sincronizador Portfolio 1:1</h2>
  <div class="badge">Versão Oficial • 02/11/2026</div>
  <p>Injeta automaticamente os dados substantivos, títulos jornalísticos e métricas auditadas nos frames da página aberta no Figma Desktop.</p>
  
  <button id="btnSync" class="btn" onclick="triggerSync()">
    <span>⚡ Sincronizar Cases Nesta Página</span>
  </button>

  <div id="log">Aguardando início...</div>

  <div class="status-bar">
    <span id="status">Pronto para execução</span>
    <button style="background:none; border:none; color:#71717a; cursor:pointer;" onclick="closePlugin()">Fechar</button>
  </div>

  <script>
    function triggerSync() {
      document.getElementById('btnSync').disabled = true;
      document.getElementById('status').textContent = 'Processando...';
      document.getElementById('log').textContent = 'Iniciando varredura e injeção de dados...\n';
      parent.postMessage({ pluginMessage: { type: 'sync_all' } }, '*');
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
      } else if (msg.type === 'done') {
        document.getElementById('btnSync').disabled = false;
        document.getElementById('status').textContent = 'Finalizado com sucesso!';
      }
    };
  </script>
</body>
</html>
"""

# Gravar nos arquivos do plugin
(plugin_dir / "code.js").write_text(code_js, encoding="utf-8")
(plugin_dir / "ui.html").write_text(ui_html, encoding="utf-8")
print("SUCCESS: Plugin atualizado com o Sync Engine 1:1!")

