with open('site/src/pages/ItauPreparationCase.tsx', 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
for i, line in enumerate(lines):
    if i == 123 and '  },' in line and 'vencimentos' in lines[i+2]:
        new_lines.append('''    visuals: [
      {
        src: "/images/itau-registros-workflow-1600.webp",
        width: 1600,
        height: 900,
        alt: "Fluxo de arquitetura de serviço e governança de IA para Registros de Atendimento",
        label: "Arquitetura e Governança · IA com Supervisão Humana",
        caption:
          "Modelo operacional para registros de atendimento: recuperação de contexto recente, geração de ata preliminar assistida por IA e salvaguarda obrigatória de supervisão humana antes da persistência bancária.",
      },
    ],
  },\n''')
    else:
        new_lines.append(line)

with open('site/src/pages/ItauPreparationCase.tsx', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print("Inserted registros-atendimento visuals.")

