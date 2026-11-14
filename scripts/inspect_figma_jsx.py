with open(r'C:\Users\Israel Rozar\.gemini\antigravity\brain\ec9956e5-078d-4d87-9a8e-74481434c7dc\.system_generated\steps\2781\output.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's find VigenteEinsteinConsumoDeResultadosIsraelRozar
pos = text.find('export default function VigenteEinsteinConsumoDeResultadosIsraelRozar')
print(text[pos:pos+4000])

