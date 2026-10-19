from PIL import Image
import os

source_path = r"C:\Users\OMEN\.gemini\antigravity-ide\brain\bf6de799-a5f8-4130-abc4-d2f2a26c98ba\car_driver_smoke_ashtray_1792391464210.jpg"
dest_path = r"assets\4k\img_16.webp"

with Image.open(source_path) as img:
    # Resize / optimize to crisp 4K WebP
    img.save(dest_path, "WEBP", quality=92, method=6)
    print(f"Saved {dest_path} successfully. Dimensions: {img.size}")
