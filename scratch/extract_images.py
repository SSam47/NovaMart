import re, os, base64

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Extract all img tags
img_tags = re.findall(r'<img[^>]+>', text)
print(f"Total img tags: {len(img_tags)}")

os.makedirs('extracted_images', exist_ok=True)

# Also find where they are in the markup (hero, story, anatomy, fits, life, gallery, order)
for i, tag in enumerate(img_tags):
    m = re.search(r'src=["\']([^"\']+)["\']', tag)
    if not m:
        continue
    src = m.group(1)
    if src.startswith('data:'):
        header, data = src.split(',', 1)
        ext = 'png' if 'png' in header else 'jpg'
        img_bytes = base64.b64decode(data)
        out_path = f"extracted_images/img_{i+1:02d}.{ext}"
        with open(out_path, 'wb') as img_f:
            img_f.write(img_bytes)
        print(f"Saved {out_path}: {len(img_bytes)/1024:.1f} KB")
    else:
        print(f"Image {i+1}: {src}")
