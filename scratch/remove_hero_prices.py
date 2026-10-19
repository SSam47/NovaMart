import re

for filename in ['index.html', 'nova-mart-aone.html']:
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()

    # 1. Remove the prices list from the hero banner
    # <ul class="hero-prices"><li><b>1 Piece</b><span>$11</span></li><li><b>2 Pieces</b><span>$18</span></li><li><b>3 Pieces</b><span>$24</span></li></ul>
    text = re.sub(r'<ul class=["\']hero-prices["\']>.*?<\/ul>\s*', '', text, flags=re.DOTALL)

    # 2. Remove the static free delivery line directly beneath it in hero
    # <p class="ship"><em class="dot"></em>Free Delivery <span>| Arrives in 2 to 4 days</span></p>
    text = re.sub(r'<p class=["\']ship["\']><em class=["\']dot["\']><\/em>Free Delivery.*?<\/p>\s*', '', text, flags=re.DOTALL)

    # 3. Clean GSAP hero animation selector so it doesn't try to query missing elements
    text = text.replace(
        ".from('.hero .eyebrow, .hero .lede, .hero .cta, .hero-prices, .hero .ship', { opacity: 0, y: 14, duration: .8, stagger: .07, ease: E }, .55);",
        ".from('.hero .lede, .hero .cta', { opacity: 0, y: 14, duration: .8, stagger: .07, ease: E }, .55);"
    )

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(text)

    print(f"Removed hero price blocks and static delivery tag from {filename}.")
