import os, hashlib

k4_dir = r"assets\4k"
brain_dir = r"C:\Users\OMEN\.gemini\antigravity-ide\brain\bf6de799-a5f8-4130-abc4-d2f2a26c98ba"
extracted_dir = r"extracted_images"

# Build hash index of all brain jpgs and extracted images
sources = {}

for folder, name in [(brain_dir, "brain"), (extracted_dir, "extracted")]:
    if not os.path.exists(folder):
        continue
    for root, dirs, files in os.walk(folder):
        for f in files:
            path = os.path.join(root, f)
            try:
                # We can't direct match webp to jpg hash, but let's list brain jpgs and scripts
                pass
            except:
                pass

print("List of scripts that touch assets/4k:")
import glob
for py in glob.glob("scratch/*.py"):
    txt = open(py, encoding="utf-8", errors="ignore").read()
    if "assets/4k" in txt or "assets\\4k" in txt:
        print(f"--- {py} ---")
        for line in txt.splitlines():
            if any(k in line for k in ["assets", "img_", "src", "brain", "jpg"]):
                print("  ", line.strip()[:100])
