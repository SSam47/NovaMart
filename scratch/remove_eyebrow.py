import re

for filename in ['index.html', 'nova-mart-aone.html']:
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()

    # Match and remove the hero eyebrow: <p class="eyebrow">Nova Mart Aone...Car Ashtray</span></p>
    text = re.sub(r'<p class=["\']eyebrow["\']>\s*Nova Mart Aone.*?Car Ashtray.*?<\/p>\s*', '', text, flags=re.DOTALL | re.IGNORECASE)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(text)

    print(f"Updated {filename}: removed hero eyebrow.")
