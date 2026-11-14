from pathlib import Path
import re

txt_path = Path(r"C:\Users\Israel Rozar\.gemini\antigravity\brain\ec9956e5-078d-4d87-9a8e-74481434c7dc\.system_generated\steps\3279\output.txt")
text = txt_path.read_text(encoding="utf-8")

# Let's search for "Movimentações", "Hub de Liquidez", "Gestão de Campanhas" in step 3279 (Figma node 370:16614)
print("Found Movimentações in 370:16614:", "Movimentações" in text)
print("Found Hub de Liquidez in 370:16614:", "Hub de Liquidez" in text)
print("Found Campanhas in 370:16614:", "Campanhas" in text)

# Let's search in all figma outputs or previous steps if there is a frame with those cards

