from pathlib import Path

css = Path("site/src/portfolio.css").read_text(encoding="utf-8")

# Let's inspect all media queries in portfolio.css
import re
media_queries = re.findall(r'@media[^{]+\{[^}]+\}', css)
for mq in media_queries:
    print(mq)
    print('-'*40)

