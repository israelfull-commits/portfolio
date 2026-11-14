import urllib.request
import re
import json

url = 'https://claude.ai/artifact/3qEz2T37PmCWTFyHqWHY9e'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})

try:
    with urllib.request.urlopen(req) as resp:
        html = resp.read().decode('utf-8')
    
    # Save raw html
    with open('tmp/claude_artifact.html', 'w', encoding='utf-8') as f:
        f.write(html)
    
    # Find scripts or json
    next_data = re.findall(r'<script id="__NEXT_DATA__"[^>]*>(.*?)</script>', html, re.DOTALL)
    if next_data:
        data = json.loads(next_data[0])
        with open('tmp/claude_artifact_data.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print("Wrote NEXT_DATA, searching for case-laudos...")
        data_str = json.dumps(data, ensure_ascii=False)
        for m in re.finditer(r'(case-laudos|laudos|protrombina|anatomia)', data_str, re.IGNORECASE):
            start = max(0, m.start() - 100)
            end = min(len(data_str), m.end() + 200)
            print("MATCH:", data_str[start:end])
    else:
        print("No NEXT_DATA found, checking html for text...")
        for m in re.finditer(r'(case-laudos|protrombina|examTitle)', html, re.IGNORECASE):
            start = max(0, m.start() - 100)
            end = min(len(html), m.end() + 200)
            print("MATCH:", html[start:end])
except Exception as e:
    print("Error:", e)

