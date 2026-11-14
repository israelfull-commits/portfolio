import re

with open('site/src/pages/Home.tsx', 'r', encoding='utf-8') as f:
    text = f.read()

images_in_home = re.findall(r'src=["\']([^"\']+)["\']', text)
print('Images in Home.tsx:', images_in_home)

links_in_home = re.findall(r'href=["\'](/cases/[^"\']+)["\']', text)
print('Case links in Home.tsx:', links_in_home)

