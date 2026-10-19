import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Find all <p class="eyebrow">...</p>
matches = re.findall(r'<p[^>]*class=["\'][^"\']*eyebrow[^"\']*["\'][^>]*>(.*?)</p>', text)
print("All eyebrow elements found:")
for m in matches:
    print("-", m)
