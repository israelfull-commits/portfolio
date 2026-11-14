with open(r'C:\Users\Israel Rozar\.gemini\antigravity\brain\ec9956e5-078d-4d87-9a8e-74481434c7dc\.system_generated\steps\2781\output.txt', 'r', encoding='utf-8') as f:
    figma_text = f.read()

# Let's extract the exact chapter texts from Figma 59:2
# In Figma 59:2, let's see how each chapter is defined
import re

chapters_data = []
# split by Heading 2
h2_splits = re.split(r'data-name="Heading 2"', figma_text)
print(f"H2 splits count: {len(h2_splits)}")

for i in range(1, len(h2_splits)):
    sec = h2_splits[i]
    # title is in <p ...>...</p>
    title_m = re.search(r'<p[^>]*>([^<]+)</p>', sec)
    title = title_m.group(1).strip() if title_m else "No title"
    
    # extract all paragraphs up to next major section
    paras = re.findall(r'<p[^>]*>([^<]+)</p>', sec[:5000])
    print(f"\n--- Chapter {i}: {title} ---")
    for p in paras[1:6]:
        p_clean = p.strip()
        if p_clean and not p_clean.isdigit() and len(p_clean) > 20:
            print("  - ", p_clean[:120])

