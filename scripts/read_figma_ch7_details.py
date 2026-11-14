with open(r'C:\Users\Israel Rozar\.gemini\antigravity\brain\ec9956e5-078d-4d87-9a8e-74481434c7dc\.system_generated\steps\2781\output.txt', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('Autoria e colabora')
chunk = text[pos-200:pos+1500]
print(chunk.encode('ascii', errors='replace').decode('ascii'))
