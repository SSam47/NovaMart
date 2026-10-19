import re, os

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace each image src with its corresponding assets/4k path
# We know there are exactly 26 img tags in order
img_count = 0

def replace_img(match):
    global img_count
    img_count += 1
    tag = match.group(0)
    ext = 'png' if img_count in (1, 2) else 'webp'
    new_src = f"/assets/4k/img_{img_count:02d}.{ext}"
    # replace src="data:..." with src="/assets/4k/..."
    updated = re.sub(r'src=["\'][^"\']+["\']', f'src="{new_src}"', tag)
    return updated

new_text = re.sub(r'<img[^>]+>', replace_img, text)

print(f"Replaced {img_count} images.")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_text)

with open('nova-mart-aone.html', 'w', encoding='utf-8') as f:
    f.write(new_text)

print("Saved updated index.html and nova-mart-aone.html with 4K image sources.")
