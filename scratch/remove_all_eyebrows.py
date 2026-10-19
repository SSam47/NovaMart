import re

for filename in ['index.html', 'nova-mart-aone.html']:
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()

    # Remove all <p class="eyebrow...">...</p> tags
    text = re.sub(r'<p[^>]*class=["\'][^"\']*eyebrow[^"\']*["\'][^>]*>.*?<\/p>\s*', '', text, flags=re.DOTALL)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(text)

    print(f"Removed all eyebrow tags from {filename}.")
