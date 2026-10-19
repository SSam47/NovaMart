import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# CSS for marquee ticker ribbon
marquee_css = """
/* Marquee ticker ribbon */
.marquee{position:relative;width:100%;overflow:hidden;background:#f3ecdf;border-top:1px solid var(--line);border-bottom:1px solid var(--line);padding:14px 0;display:flex;user-select:none;isolation:isolate}
.marquee-track{display:flex;width:max-content;animation:marqueeScroll 26s linear infinite;will-change:transform}
.marquee:hover .marquee-track{animation-play-state:paused}
.marquee-item{display:inline-flex;align-items:center;gap:18px;padding:0 28px;white-space:nowrap;font:700 13px/1 var(--f);letter-spacing:.22em;text-transform:uppercase;color:#4a3828}
.marquee-item .m-dot{display:inline-block;width:6px;height:6px;border-radius:50%;background:var(--cu)}
.marquee-item b{color:#9b6f43;font-weight:800}
.marquee-item span{color:var(--mu);font-weight:500;letter-spacing:.14em}
@keyframes marqueeScroll{0%{transform:translateX(0)}100%{transform:translateX(-50%)}}
"""

# Insert CSS before </style>
text = text.replace('</style>', marquee_css + '\n</style>')

# HTML markup for seamless repeating ticker (two identical sets inside .marquee-track for -50% translateX)
single_group = """
    <div class="marquee-item"><span class="m-dot"></span><b>FREE DELIVERY</b><span>NATIONWIDE IN 2–4 DAYS</span></div>
    <div class="marquee-item"><span class="m-dot"></span><b>FREE SHIPPING</b><span>ON ALL 1, 2 & 3 PIECE PACKS</span></div>
    <div class="marquee-item"><span class="m-dot"></span><b>FREE DELIVERY</b><span>CASH & WHATSAPP CONFIRMATION</span></div>
    <div class="marquee-item"><span class="m-dot"></span><b>FAST DELIVERY</b><span>DISPATCHED WITHIN 24 HOURS</span></div>
"""

marquee_html = f"""
<div class="marquee" aria-label="Free Delivery Announcement">
  <div class="marquee-track">
    {single_group}
    {single_group}
  </div>
</div>
"""

# Place the marquee right after the hero section (before the story section)
hero_end = '</section>\n\n<section class="story"'
text = text.replace('</section>\n\n<section class="story"', '</section>\n' + marquee_html + '\n<section class="story"')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)

with open('nova-mart-aone.html', 'w', encoding='utf-8') as f:
    f.write(text)

print('Added seamless repetitive moving line for Free Delivery.')
