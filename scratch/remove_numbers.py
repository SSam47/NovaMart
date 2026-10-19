import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Remove <span class="num">01 / 05</span> etc.
text = re.sub(r'<span class="num">\s*\d+\s*/\s*\d+\s*</span>', '', text)

# 2. In anatomy figcaption: <b>01</b>, <b>02</b>, etc.
text = re.sub(r'<figcaption><b>\d+</b>', '<figcaption>', text)

# 3. In why-l list items: <li><span>01</span><h3> -> <li><h3>
text = re.sub(r'<li><span>\d+</span><h3>', '<li><h3>', text)

# 4. Remove the story progress bar at bottom of story pin: <div class="story-bar"><i></i></div>
text = text.replace('<div class="story-bar"><i></i></div>', '')

# 5. Fix CSS for why-l grid layout since the number column is gone
text = text.replace('grid-template-columns:80px 1fr;', 'grid-template-columns:1fr;')
text = text.replace('grid-template-columns:44px 1fr;', 'grid-template-columns:1fr;')

# 6. Clean up anatomy figcaption CSS so pseudo element line doesn't misalign
# .a figcaption:before{content:"";order:0;width:34px;height:1px;background:var(--cu);box-shadow:0 0 6px rgba(0,0,0,.5)}
text = text.replace('.a figcaption b{margin:0;order:-1}', '')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)

with open('nova-mart-aone.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Applied clean removal of numbers.")
