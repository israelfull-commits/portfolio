import re

with open('site/src/pages/CasePages.tsx', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Update einsteinPresentation hero
text = re.sub(
    r"kicker:\s*'Saúde · Laudos Médicos',\s*cover:\{[^\}]+\},",
    """kicker: 'Saúde · Laudos Médicos',
  hero: {
    src: '/images/mockup-hero-einstein.webp',
    width: 1376,
    height: 768,
    alt: 'Mockup 3D macro do relatório de laudos laboratoriais Einstein',
    caption: 'Direção de Arte e Mockup 3D: Linguagem modular clínica desconstruída em painéis de vidro fosco bisotado e papel archival com tipografia diagnóstica.',
  },""",
    text
)

# 2. Update claroPresentation hero
text = re.sub(
    r"kicker:\s*'Telecom · Enterprise UX',\s*hero:claroImages\[0\],",
    """kicker: 'Telecom · Enterprise UX',
  hero: {
    src: '/images/mockup-hero-claro.webp',
    width: 1376,
    height: 768,
    alt: 'Mockup 3D editorial da ativação e vendas multicanal Claro',
    caption: 'Direção de Arte e Mockup 3D: Composição assimétrica em concreto aparente e dispositivos integrados exibindo o fluxo de ativação e carrinho financeiro em tempo real.',
  },""",
    text
)

# 3. Update neoenergiaPresentation hero
text = re.sub(
    r"kicker:\s*'Utilities · Service Design',\s*cover:\{[^\}]+\},",
    """kicker: 'Utilities · Service Design & Discovery',
  hero: {
    src: '/images/mockup-hero-neoenergia.webp',
    width: 1376,
    height: 768,
    alt: 'Mockup 3D desconstruído da plataforma omnicanal Neoenergia Conexão Digital',
    caption: 'Direção de Arte e Mockup 3D: Ecossistema de atendimento e gestão de rede elétrica em camadas físicas de acrílico translúcido, blueprint e tablet metálico.',
  },""",
    text
)

with open('site/src/pages/CasePages.tsx', 'w', encoding='utf-8') as f:
    f.write(text)

print("SUCCESS: Updated heroes in CasePages.tsx!")

