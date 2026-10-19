from PIL import Image

src = r"C:\Users\OMEN\.gemini\antigravity-ide\brain\bf6de799-a5f8-4130-abc4-d2f2a26c98ba\hand_holding_ashtray_desk_1792392515109.jpg"
dst = r"assets\4k\img_24.webp"

with Image.open(src) as img:
    img.save(dst, "WEBP", quality=92, method=6)
    print("img_24.webp updated successfully!", img.size)
