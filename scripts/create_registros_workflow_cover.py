import os
from PIL import Image, ImageDraw, ImageFont

OUTPUT = 'site/public/images/itau-registros-workflow-1600.webp'

# Dimensions
W, H = 1600, 900

# Colors from design system
BG = (23, 32, 25) # #172019 / dark forest
CARD_BG = (30, 48, 38) # #1e3026
BORDER_COLOR = (45, 75, 60)
LIME = (217, 255, 99) # #D9FF63
WHITE = (255, 253, 247)
MUTED = (162, 174, 168)
ACCENT_GREEN = (72, 179, 131)

img = Image.new("RGB", (W, H), BG)
draw = ImageDraw.Draw(img)

# Try to load fonts, fallback to default
try:
    font_title = ImageFont.truetype("arialbd.ttf", 38)
    font_subtitle = ImageFont.truetype("arial.ttf", 22)
    font_step_num = ImageFont.truetype("arialbd.ttf", 18)
    font_step_title = ImageFont.truetype("arialbd.ttf", 24)
    font_body = ImageFont.truetype("arial.ttf", 17)
    font_badge = ImageFont.truetype("arialbd.ttf", 15)
except:
    font_title = font_subtitle = font_step_num = font_step_title = font_body = font_badge = ImageFont.load_default()

# Header
draw.text((100, 80), "ARQUITETURA DE SERVIÇO & SALVAGUARDAS DE IA", fill=LIME, font=font_badge)
draw.text((100, 115), "Registros de Atendimento · Síntese Assistida e Supervisão Humana", fill=WHITE, font=font_title)
draw.text((100, 168), "Fluxo operacional para captura de contexto, sumarização por LLM e conformidade bancária obrigatória.", fill=MUTED, font=font_subtitle)

# 3 Step Cards
cards = [
    {
        "step": "01",
        "tag": "CAPTURA DE CONTEXTO",
        "title": "Recuperação do Histórico",
        "desc": "Aproximação dos 5 atendimentos e eventos recentes diretamente no momento de consulta do assessor, eliminando troca de abas e esforço mnemônico.",
        "pills": ["Eventos Recentes", "Linha do Tempo", "Contexto Persistente"],
        "color": ACCENT_GREEN
    },
    {
        "step": "02",
        "tag": "INTELIGÊNCIA ARTIFICIAL",
        "title": "Minuta Assistida por IA",
        "desc": "Estruturação automática de atas preliminares a partir de tópicos-chave e diretrizes de reunião. A IA atua estritamente como redatora de sugestões.",
        "pills": ["Sugestão Editável", "Sumarização Factual", "Sem Persistência Direta"],
        "color": LIME
    },
    {
        "step": "03",
        "tag": "GOVERNANÇA & CONFORMIDADE",
        "title": "Supervisão Humana Ativa",
        "desc": "Validação e edição obrigatória pelo profissional responsável antes de qualquer gravação na base bancária. Salvaguarda formal de conformidade.",
        "pills": ["Human-in-the-loop", "Auditabilidade", "Responsabilidade Legal"],
        "color": (255, 175, 75)
    }
]

card_w = 420
card_h = 450
gap = 50
start_x = 100
start_y = 240

for i, c in enumerate(cards):
    x = start_x + i * (card_w + gap)
    y = start_y
    
    # Draw card background
    draw.rounded_rectangle([x, y, x + card_w, y + card_h], radius=16, fill=CARD_BG, outline=BORDER_COLOR, width=1)
    
    # Header inside card
    draw.rounded_rectangle([x + 24, y + 24, x + 70, y + 56], radius=8, fill=(15, 25, 20), outline=c["color"], width=1)
    draw.text((x + 36, y + 30), c["step"], fill=c["color"], font=font_step_num)
    
    draw.text((x + 85, y + 32), c["tag"], fill=c["color"], font=font_badge)
    
    # Card Title
    draw.text((x + 24, y + 80), c["title"], fill=WHITE, font=font_step_title)
    
    # Divider
    draw.line([x + 24, y + 125, x + card_w - 24, y + 125], fill=BORDER_COLOR, width=1)
    
    # Card Description (wrapped)
    words = c["desc"].split()
    line = ""
    line_y = y + 145
    for w in words:
        test_line = line + " " + w if line else w
        bbox = draw.textbbox((0, 0), test_line, font=font_body)
        if bbox[2] - bbox[0] > card_w - 48:
            draw.text((x + 24, line_y), line, fill=MUTED, font=font_body)
            line_y += 26
            line = w
        else:
            line = test_line
    if line:
        draw.text((x + 24, line_y), line, fill=MUTED, font=font_body)
        
    # Pills at bottom
    pill_y = y + card_h - 90
    draw.line([x + 24, pill_y - 15, x + card_w - 24, pill_y - 15], fill=BORDER_COLOR, width=1)
    
    cur_px = x + 24
    for p in c["pills"]:
        p_bbox = draw.textbbox((0, 0), p, font=font_badge)
        pw = p_bbox[2] - p_bbox[0] + 16
        if cur_px + pw > x + card_w - 24:
            break
        draw.rounded_rectangle([cur_px, pill_y, cur_px + pw, pill_y + 28], radius=14, fill=(20, 35, 28), outline=BORDER_COLOR, width=1)
        draw.text((cur_px + 8, pill_y + 5), p, fill=WHITE, font=font_badge)
        cur_px += pw + 8

# Footer line
draw.line([100, 750, 1500, 750], fill=BORDER_COLOR, width=1)
draw.text((100, 775), "íon for Advisors · Itaú Unibanco · Modelo de Decisão e Governança de IA", fill=MUTED, font=font_subtitle)
draw.text((1200, 775), "Evidência Conceitual e Operacional", fill=LIME, font=font_subtitle)

# Save
img.save(OUTPUT, format="WEBP", quality=92, method=6)
print(f"Generated {OUTPUT} ({os.path.getsize(OUTPUT)//1024} KB)")

