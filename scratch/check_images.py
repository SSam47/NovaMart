import os, re
from PIL import Image

root = r"c:\Users\OMEN\Desktop\WaveBuild\Websites Clients\NovaMart"
html_file = os.path.join(root, "index.html")

with open(html_file, "r", encoding="utf-8") as f:
    lines = f.readlines()

print("=== IMAGE USAGE IN INDEX.HTML ===")
for i, l in enumerate(lines):
    matches = re.findall(r"assets/4k/(img_\d+\.(?:png|webp))", l)
    for m in matches:
        # Get context 3 lines before and after
        start = max(0, i - 3)
        end = min(len(lines), i + 4)
        snippet = " | ".join(x.strip() for x in lines[start:end] if x.strip() and not x.strip().startswith("<!--"))
        # clean snippet
        snippet = re.sub(r"\s+", " ", snippet)
        print(f"L{i+1:4d} | {m:11s} | {snippet[:120]}")
