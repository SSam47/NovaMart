from PIL import Image

src = r"C:\Users\OMEN\.gemini\antigravity-ide\brain\bf6de799-a5f8-4130-abc4-d2f2a26c98ba\portable_pocket_ashtray_slim_1792392956622.jpg"
dst = r"assets\4k\img_06.webp"

with Image.open(src) as img:
    img.save(dst, "WEBP", quality=93, method=6)
    print("img_06.webp successfully updated:", img.size)
