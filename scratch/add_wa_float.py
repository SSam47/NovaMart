import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# CSS for floating WhatsApp button
float_css = """
/* Floating bottom-right WhatsApp button */
.wa-float{position:fixed;right:24px;bottom:24px;z-index:99;display:flex;align-items:center;gap:10px;background:#25d366;color:#fff;padding:12px 18px 12px 14px;border-radius:999px;box-shadow:0 8px 24px rgba(37,211,102,.35),0 2px 8px rgba(0,0,0,.1);font:600 13px/1 var(--f);letter-spacing:.08em;text-transform:uppercase;transition:all .3s cubic-bezier(.34,1.56,.64,1);cursor:pointer;text-decoration:none}
.wa-float:hover{transform:translateY(-3px) scale(1.03);background:#20ba5a;box-shadow:0 12px 28px rgba(37,211,102,.45);color:#fff}
.wa-float svg{width:24px;height:24px;fill:currentColor;flex-shrink:0}
.wa-float .wa-pulse{position:absolute;inset:-4px;border-radius:999px;border:2px solid rgba(37,211,102,.6);animation:waPulse 2.4s cubic-bezier(.25,.46,.45,.94) infinite;pointer-events:none}
@keyframes waPulse{0%{transform:scale(.95);opacity:1}70%{transform:scale(1.15);opacity:0}100%{transform:scale(1.15);opacity:0}}

@media (max-width:900px){
  .wa-float{right:16px;bottom:calc(86px + env(safe-area-inset-bottom));padding:12px;border-radius:50%}
  .wa-float span{display:none}
  .wa-float svg{width:26px;height:26px}
}
"""

# Insert before </style>
text = text.replace('</style>', float_css + '\n</style>')

# HTML markup for floating button
float_html = """
<a class="wa-float" href="https://wa.me/96179355492" target="_blank" rel="noopener" aria-label="Chat on WhatsApp">
  <span class="wa-pulse" aria-hidden="true"></span>
  <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2Zm0 18.2a8.2 8.2 0 0 1-4.2-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2Zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8s-.4-.1-.6.1-.7.8-.8 1-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.3-.4.3-.4.7-1.3.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.7 11.8 11.8 0 0 0 4.5 4c1.7.7 2.3.8 3.2.6a2.7 2.7 0 0 0 1.8-1.2 2.2 2.2 0 0 0 .1-1.3c0-.1-.2-.2-.5-.3Z"/></svg>
  <span>Chat with us</span>
</a>
"""

# Insert right before </body>
text = text.replace('</body>', float_html + '\n</body>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)

with open('nova-mart-aone.html', 'w', encoding='utf-8') as f:
    f.write(text)

print('Added sticky bottom-right floating WhatsApp button.')
