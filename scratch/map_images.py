import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Find each img tag and surrounding 150 characters
matches = [m.start() for m in re.finditer(r'<img\s', text)]
print(f"Total img tags: {len(matches)}")

for i, pos in enumerate(matches):
    start = max(0, pos - 120)
    end = min(len(text), pos + 100)
    snippet = text[start:pos]
    # find parent classes
    classes = re.findall(r'class=["\']([^"\']+)["\']', snippet)
    tag_match = re.search(r'<img[^>]*src=["\']([^"\']{1,40})', text[pos:])
    src_preview = tag_match.group(1) if tag_match else ""
    print(f"Img {i+1:02d} | classes: {classes[-3:]} | src: {src_preview[:30]}")
