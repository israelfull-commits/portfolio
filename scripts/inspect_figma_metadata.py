from pathlib import Path
import json

txt_path = Path(r"C:\Users\Israel Rozar\.gemini\antigravity\brain\ec9956e5-078d-4d87-9a8e-74481434c7dc\.system_generated\steps\3313\output.txt")
text = txt_path.read_text(encoding="utf-8")
print("Metadata length:", len(text))
try:
    data = json.loads(text)
    print("Keys:", data.keys())
    if "document" in data:
        for page in data["document"].get("children", []):
            print(f"Page: {page.get('name')} (id: {page.get('id')})")
            for frame in page.get("children", []):
                print(f"  Frame: {frame.get('name')} (id: {frame.get('id')})")
except Exception as e:
    # Maybe it's a string or snippet
    print("Not json:", text[:1000])

