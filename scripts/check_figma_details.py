with open(r'C:\Users\Israel Rozar\.gemini\antigravity\brain\ec9956e5-078d-4d87-9a8e-74481434c7dc\.system_generated\steps\2781\output.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's search for details/accordion in node 59:2
import re
details = re.findall(r'data-name="(Details[^"]*|Autoria[^"]*|Limites[^"]*)"[\s\S]*?<p[^>]*>([^<]+)</p>', text)
print("Details in 59:2:")
for d, content in details:
    print(f"  {d}: {content.strip()[:100]}")

