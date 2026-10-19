import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace the base color variables
# Old root:
# :root{--ch:#16140f;--ch2:#1f1c17;--ch3:#2a2620;--wal:#6b4428;--wal2:#8a5a36;--cu:#c89a6a;--cp:#e3c9a3;--ow:#f2ede4;--mu:#a59d90;--gr:#5f8b5a;--line:rgba(242,237,228,.12);--hh:68px;--f:'Archivo',system-ui,sans-serif;--fn:'Archivo Narrow','Archivo',sans-serif}
#
# In our new White & Warm Beige palette:
# Background: crisp warm cream / pure white blend (#faf8f5 / #f4eee5)
# Card/Section background: #fbf9f6 / #ffffff
# Deep contrasting text: #231e18
# Warm Walnut & Copper accents: #8a5a36, #c89a6a, #7a5030
# Soft muted body text: #685e52
# Subtle borders: rgba(35, 30, 24, 0.12)
# Highlight button: #3a2718 with white text, or rich copper #c89a6a

old_root = ":root{--ch:#16140f;--ch2:#1f1c17;--ch3:#2a2620;--wal:#6b4428;--wal2:#8a5a36;--cu:#c89a6a;--cp:#e3c9a3;--ow:#f2ede4;--mu:#a59d90;--gr:#5f8b5a;--line:rgba(242,237,228,.12);--hh:68px;--f:'Archivo',system-ui,sans-serif;--fn:'Archivo Narrow','Archivo',sans-serif}"

new_root = ":root{--ch:#fbf9f5;--ch2:#f4ede4;--ch3:#eae1d3;--wal:#6b4428;--wal2:#8a5a36;--cu:#9b6f43;--cp:#4a3525;--ow:#231f1a;--mu:#756a5c;--gr:#3b6e37;--line:rgba(50,40,30,.12);--hh:68px;--f:'Archivo',system-ui,sans-serif;--fn:'Archivo Narrow','Archivo',sans-serif}"

text = text.replace(old_root, new_root)

# Meta theme color
text = text.replace('content="#16140f"', 'content="#fbf9f5"')

# Header background & blur
# .hdr.solid{background:rgba(22,20,15,.86);
text = text.replace('background:rgba(22,20,15,.86);', 'background:rgba(251,249,245,.92);')
text = text.replace('color:rgba(242,237,228,.78);', 'color:rgba(35,31,26,.82);')
text = text.replace('background:var(--ow);transition:transform .3s', 'background:var(--ow);transition:transform .3s')

# Button styles:
# .btn{... background:var(--cp);color:var(--ch)
# In light mode, button with dark brown background and white/cream text looks ultra premium
text = text.replace('background:var(--cp);color:var(--ch);', 'background:#2c2118;color:#faf7f2;')
text = text.replace('background:var(--ow);transform:scaleX(0);', 'background:#9b6f43;transform:scaleX(0);')
text = text.replace('transition:color .3s;isolation:isolate', 'transition:color .3s;isolation:isolate;box-shadow:0 6px 20px rgba(44,33,24,.15)')
text = text.replace('.btn:hover:after{transform:scaleX(1);transform-origin:left}', '.btn:hover:after{transform:scaleX(1);transform-origin:left}.btn:hover{color:#fff!important}')
text = text.replace('box-shadow:inset 0 0 0 1px rgba(242,237,228,.4)', 'box-shadow:inset 0 0 0 1px rgba(35,31,26,.3);color:var(--ow)')
text = text.replace('.btn-ghost:hover{color:var(--ch)}', '.btn-ghost:hover{color:#faf7f2;background:#2c2118}')

# Hero gradients
# background:radial-gradient(48% 62% at 58% 52%,var(--tint),var(--ch) 74%)
text = text.replace(':root{--ln:rgba(200,154,106,.55);--tint:#3d2617}', ':root{--ln:rgba(155,111,67,.45);--tint:#ede3d5}')
text = text.replace('body[data-f=beech]{--tint:#5e4b33}', 'body[data-f=beech]{--tint:#f2eae0}')
text = text.replace('background:radial-gradient(48% 62% at 58% 52%,var(--tint),var(--ch) 74%);', 'background:radial-gradient(55% 65% at 56% 50%,#f0e5d5 0%,#fbf9f5 72%);')

# Big background watermark typography in hero
text = text.replace('.hx-a{top:8vh;left:-3vw;color:rgba(242,237,228,.055)}', '.hx-a{top:8vh;left:-3vw;color:rgba(155,111,67,.07)}')
text = text.replace('-webkit-text-stroke:1px rgba(200,154,106,.42)', '-webkit-text-stroke:1px rgba(155,111,67,.28)')

# Swatches
text = text.replace('border:1px solid rgba(242,237,228,.18)', 'border:1px solid rgba(50,40,30,.15);background:rgba(255,255,255,.6)')
text = text.replace('body[data-f=walnut] .sw-w,body[data-f=beech] .sw-b{background:var(--ch3);color:var(--ow);box-shadow:inset 0 0 0 1px var(--cu)}', 'body[data-f=walnut] .sw-w,body[data-f=beech] .sw-b{background:#fff;color:var(--ow);box-shadow:0 2px 8px rgba(0,0,0,.08),inset 0 0 0 1px var(--cu)}')

# Edge words stroke
text = text.replace('-webkit-text-stroke:1px rgba(200,154,106,.22)', '-webkit-text-stroke:1px rgba(155,111,67,.18)')

# Story section pin
# .story-bg{position:absolute;inset:0;background:radial-gradient(60% 70% at 70% 50%,#3a2a1c 0%,var(--ch) 70%);will-change:opacity}
text = text.replace('background:radial-gradient(60% 70% at 70% 50%,#3a2a1c 0%,var(--ch) 70%);', 'background:radial-gradient(60% 70% at 70% 50%,#ece2d2 0%,var(--ch) 70%);')

# Life section dark overlays:
# .lf:after{content:"";position:absolute;inset:0;background:linear-gradient(90deg,rgba(22,20,15,.8),transparent 55%)}
# For life section with dark photography and text overlay, let text be crisp white with refined gradient
text = text.replace('.lf h3{font-size:clamp(40px,5vw,80px)}', '.lf h3{font-size:clamp(40px,5vw,80px);color:#fff}')
text = text.replace('.lf-c .eyebrow{', '.lf-c .eyebrow{color:#e8cbb0;')
text = text.replace('.lf .eyebrow{', '.lf .eyebrow{color:#e8cbb0;')

# Anatomy cards:
text = text.replace('.a{position:relative;overflow:hidden;background:var(--ch2)}', '.a{position:relative;overflow:hidden;background:#fff;border-radius:4px;box-shadow:0 4px 24px rgba(35,30,24,.06)}')
text = text.replace('.a:after{content:"";position:absolute;inset:0;background:linear-gradient(transparent 55%,rgba(22,20,15,.75));pointer-events:none}', '.a:after{content:"";position:absolute;inset:0;background:linear-gradient(transparent 50%,rgba(20,16,12,.7));pointer-events:none}')
text = text.replace('.a figcaption{background:none;padding:0;left:16px;bottom:16px;right:auto;display:flex;align-items:center;gap:10px;color:var(--ow);text-shadow:0 1px 10px rgba(0,0,0,.7)}', '.a figcaption{background:none;padding:0;left:16px;bottom:16px;right:auto;display:flex;align-items:center;gap:10px;color:#fff;text-shadow:0 1px 10px rgba(0,0,0,.85)}')

# Pricing cards
text = text.replace('.price{background:var(--ch2)}', '.price{background:var(--ch2);background:#f5efe5}')
text = text.replace('.plan{position:relative;display:flex;flex-direction:column;align-items:flex-start;gap:10px;padding:44px 36px;text-align:left;transition:background .3s}', '.plan{position:relative;display:flex;flex-direction:column;align-items:flex-start;gap:10px;padding:44px 36px;text-align:left;transition:background .3s;background:#fff}')
text = text.replace('.plan.on{background:var(--ch3);box-shadow:inset 0 0 0 1px var(--cu)}', '.plan.on{background:#fff;box-shadow:0 8px 32px rgba(155,111,67,.18),inset 0 0 0 2px var(--cu)}')
text = text.replace('.plan:hover{background:rgba(242,237,228,.03)}', '.plan:hover{background:#faf8f5}')
text = text.replace('.tag{position:absolute;top:20px;right:20px;font:700 10px/1 var(--f);letter-spacing:.2em;text-transform:uppercase;font-style:normal;padding:7px 10px;background:var(--cu);color:var(--ch)}', '.tag{position:absolute;top:20px;right:20px;font:700 10px/1 var(--f);letter-spacing:.2em;text-transform:uppercase;font-style:normal;padding:7px 10px;background:#2c2118;color:#fff}')

# Form section
text = text.replace('.form{background:var(--ch2);padding:clamp(24px,4vw,48px);border:1px solid var(--line)}', '.form{background:#fff;padding:clamp(24px,4vw,48px);border:1px solid var(--line);border-radius:4px;box-shadow:0 8px 30px rgba(35,30,24,.06)}')
text = text.replace('border-bottom:1px solid rgba(242,237,228,.25);color:var(--ow);', 'border-bottom:1px solid rgba(50,40,30,.2);color:var(--ow);')
text = text.replace('.qty span{display:flex;align-items:center;justify-content:center;height:52px;border:1px solid rgba(242,237,228,.22);font:600 15px/1 var(--f);cursor:pointer;transition:all .25s}', '.qty span{display:flex;align-items:center;justify-content:center;height:52px;border:1px solid rgba(50,40,30,.18);background:#faf8f5;font:600 15px/1 var(--f);cursor:pointer;transition:all .25s}')
text = text.replace('.qty input:checked+span{border-color:var(--cu);background:var(--ch3);color:var(--cp)}', '.qty input:checked+span{border-color:var(--cu);background:#f2e8da;color:var(--ow);box-shadow:inset 0 0 0 1px var(--cu)}')

# Footer
text = text.replace('.ftr{background:#0f0e0b;padding:72px 0 40px;border-top:1px solid var(--line)}', '.ftr{background:#eae2d5;padding:72px 0 40px;border-top:1px solid var(--line)}')

# Mobile buybar
text = text.replace('background:rgba(31,28,23,.94);', 'background:rgba(251,249,245,.96);')

# Subtle grain opacity adjustment so it blends with white/beige
text = text.replace('opacity:.12;mix-blend-mode:overlay;', 'opacity:.04;mix-blend-mode:multiply;')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)

with open('nova-mart-aone.html', 'w', encoding='utf-8') as f:
    f.write(text)

print('Transformed website theme to white & warm beige.')
