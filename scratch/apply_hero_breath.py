with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Update HTML: wrap cut and spec inside hx-product-wrap so pointers stay 100% attached to the breathing cylinder
old_stage_html = """<div class="hx-stage">
<div class="cut cut-w"><picture><img src="/assets/4k/img_01.png" width="222" height="905" alt="Nova Mart portable ashtray in walnut finish" class="" fetchpriority="high"></picture></div>
<div class="cut cut-b"><picture><img src="/assets/4k/img_02.png" width="171" height="785" alt="Nova Mart portable ashtray in beech finish" class=""></picture></div>
<div class="spec s1"><i></i><p>Tip insert<small>Regular, Medium, and Slim</small></p></div>
<div class="spec s2"><i></i><p>Metal collar<small>Stepped metal detailing</small></p></div>
<div class="spec s3"><i></i><p>Wood body<small class="fn">Walnut finish</small></p></div>
<div class="spec s4"><i></i><p>Compact form<small>Made to travel</small></p></div>
</div>"""

new_stage_html = """<div class="hx-stage">
<div class="hx-product-wrap">
<div class="cut cut-w"><picture><img src="/assets/4k/img_01.png" width="222" height="905" alt="Nova Mart portable ashtray in walnut finish" class="" fetchpriority="high"></picture></div>
<div class="cut cut-b"><picture><img src="/assets/4k/img_02.png" width="171" height="785" alt="Nova Mart portable ashtray in beech finish" class=""></picture></div>
<div class="spec s1"><i></i><p>Tip insert<small>Regular, Medium, and Slim</small></p></div>
<div class="spec s2"><i></i><p>Metal collar<small>Stepped metal detailing</small></p></div>
<div class="spec s3"><i></i><p>Wood body<small class="fn">Walnut finish</small></p></div>
<div class="spec s4"><i></i><p>Compact form<small>Made to travel</small></p></div>
</div>
</div>"""

assert old_stage_html in html, "Could not find old_stage_html"
html = html.replace(old_stage_html, new_stage_html)

# 2. Update CSS for .hx-product-wrap and the breathing keyframes
old_css_block = """.hx-stage {
  animation: breatheSlow 6s ease-in-out infinite alternate, glowPulse 8s ease-in-out infinite alternate;
}"""

new_css_block = """.hx-product-wrap {
  position: absolute;
  inset: 0;
  animation: breatheSlow 6.5s ease-in-out infinite alternate, glowPulse 8s ease-in-out infinite alternate;
  will-change: transform;
}"""

assert old_css_block in html, "Could not find old_css_block"
html = html.replace(old_css_block, new_css_block)

# 3. Add floating words animation for .hx-a, .hx-b, and edge spans
old_breathe_keyframes = """/* Motion graphics & Breathable idle animation */
@keyframes breatheSlow {
  0%, 100% { transform: translateY(0px) scale(1); }
  50% { transform: translateY(-7px) scale(1.008); }
}"""

new_breathe_keyframes = """/* Motion graphics & Breathable idle animation */
@keyframes breatheSlow {
  0% { transform: translateY(0px) rotate(0deg) scale(1); }
  50% { transform: translateY(-14px) rotate(0.8deg) scale(1.018); }
  100% { transform: translateY(0px) rotate(0deg) scale(1); }
}
@keyframes floatWordA {
  0%, 100% { transform: translate3d(0, 0, 0); }
  50% { transform: translate3d(-18px, -12px, 0); }
}
@keyframes floatWordB {
  0%, 100% { transform: translate3d(0, 0, 0); }
  50% { transform: translate3d(20px, 14px, 0); }
}
@keyframes floatWordEdge {
  0%, 100% { transform: translate3d(0, 0, 0); }
  50% { transform: translate3d(-14px, 0, 0); }
}

.hx-a {
  animation: floatWordA 12s ease-in-out infinite alternate;
}
.hx-b {
  animation: floatWordB 14s ease-in-out infinite alternate;
}
.edge span {
  animation: floatWordEdge 16s ease-in-out infinite alternate;
}"""

assert old_breathe_keyframes in html, "Could not find old_breathe_keyframes"
html = html.replace(old_breathe_keyframes, new_breathe_keyframes)

# Save both index.html and nova-mart-aone.html
with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

with open("nova-mart-aone.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Both files successfully updated with hero product breathing and background word drift!")
