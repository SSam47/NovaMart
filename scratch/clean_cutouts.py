import os, glob
from PIL import Image, ImageFilter
import numpy as np
from scipy import ndimage

brain_dir = r'C:\Users\OMEN\.gemini\antigravity-ide\brain\bf6de799-a5f8-4130-abc4-d2f2a26c98ba'

def floodfill_cutout(jpg_name, out_png):
    matches = glob.glob(os.path.join(brain_dir, jpg_name + '*.jpg'))
    if not matches:
        print("Missing:", jpg_name)
        return
    img_path = matches[0]
    im = Image.open(img_path).convert('RGB')
    arr = np.array(im, dtype=np.uint8)
    h, w, _ = arr.shape
    
    # 1. Identify pure/near-white pixels
    r, g, b = arr[:, :, 0], arr[:, :, 1], arr[:, :, 2]
    # Background threshold
    is_white = (r > 240) & (g > 240) & (b > 240)
    
    # 2. Seed from the 4 outer image borders (guaranteed outside background)
    seed_mask = np.zeros((h, w), dtype=bool)
    seed_mask[0, :] = is_white[0, :]
    seed_mask[-1, :] = is_white[-1, :]
    seed_mask[:, 0] = is_white[:, 0]
    seed_mask[:, -1] = is_white[:, -1]
    
    # 3. Flood fill / binary dilation to only connect contiguous background
    # ndimage.binary_dilation guided by is_white
    bg_connected = ndimage.binary_propagation(seed_mask, mask=is_white)
    
    # Fill any background holes that are clearly outside
    # The foreground object is the inverse
    fg_mask = ~bg_connected
    
    # Fill internal holes in the product so metallic highlights inside are 100% solid
    fg_filled = ndimage.binary_fill_holes(fg_mask)
    
    # Smooth edges with slight antialiasing (1.5px blur on alpha)
    alpha_img = Image.fromarray((fg_filled * 255).astype(np.uint8), mode='L')
    alpha_smooth = alpha_img.filter(ImageFilter.GaussianBlur(radius=0.8))
    
    # Create RGBA image
    res = Image.new('RGBA', (w, h))
    res.paste(im, (0, 0))
    res.putalpha(alpha_smooth)
    
    # Crop to bounding box
    bbox = res.getbbox()
    if bbox:
        cropped = res.crop(bbox)
        # Pad slightly
        padded = Image.new('RGBA', (cropped.width + 40, cropped.height + 40), (0,0,0,0))
        padded.paste(cropped, (20, 20))
        padded.save(out_png, 'PNG', optimize=True)
        print(f"Saved solid clean cutout {out_png}: {padded.size}")

floodfill_cutout('walnut_ashtray_hero', 'assets/4k/img_01.png')
floodfill_cutout('beech_ashtray_hero', 'assets/4k/img_02.png')
