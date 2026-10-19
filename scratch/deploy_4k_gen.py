import os, glob
from PIL import Image
import numpy as np

brain_dir = r'C:\Users\OMEN\.gemini\antigravity-ide\brain\bf6de799-a5f8-4130-abc4-d2f2a26c98ba'
os.makedirs('assets/4k', exist_ok=True)

# 1. Process Hero cutouts (walnut and beech): Remove pure white background to make transparent PNG
def make_transparent_cutout(jpg_name, out_png):
    matches = glob.glob(os.path.join(brain_dir, jpg_name + '*.jpg'))
    if not matches:
        print("Missing:", jpg_name)
        return
    img_path = matches[0]
    im = Image.open(img_path).convert('RGBA')
    arr = np.array(im)
    
    # White background threshold: r > 248, g > 248, b > 248
    r, g, b, a = arr[:, :, 0], arr[:, :, 1], arr[:, :, 2], arr[:, :, 3]
    white_mask = (r > 248) & (g > 248) & (b > 248)
    
    # Also feather edges slightly
    arr[white_mask, 3] = 0
    
    res = Image.fromarray(arr)
    # Crop to object bounding box
    bbox = res.getbbox()
    if bbox:
        cropped = res.crop(bbox)
        # Pad slightly to keep safe borders
        padded = Image.new('RGBA', (cropped.width + 40, cropped.height + 40), (0,0,0,0))
        padded.paste(cropped, (20, 20))
        padded.save(out_png, 'PNG', optimize=True)
        print(f"Saved transparent {out_png}: {padded.size}")

make_transparent_cutout('walnut_ashtray_hero', 'assets/4k/img_01.png')
make_transparent_cutout('beech_ashtray_hero', 'assets/4k/img_02.png')

# 2. Process lifestyle photos into WebP
def convert_lifestyle(jpg_prefix, out_webp):
    matches = glob.glob(os.path.join(brain_dir, jpg_prefix + '*.jpg'))
    if not matches:
        print("Missing:", jpg_prefix)
        return
    im = Image.open(matches[0]).convert('RGB')
    im.save(out_webp, 'WEBP', quality=94, method=6)
    print(f"Saved 4K {out_webp}: {im.size}")

# img_03: cupholder_fit (used in story 01 & gallery)
convert_lifestyle('cupholder_fit', 'assets/4k/img_03.webp')
convert_lifestyle('cupholder_fit', 'assets/4k/img_14.webp')
convert_lifestyle('cupholder_fit', 'assets/4k/img_19.webp')

# img_08, img_18, img_26: desk_lifestyle_ashtray
convert_lifestyle('desk_lifestyle_ashtray', 'assets/4k/img_08.webp')
convert_lifestyle('desk_lifestyle_ashtray', 'assets/4k/img_18.webp')
convert_lifestyle('desk_lifestyle_ashtray', 'assets/4k/img_26.webp')

# img_16, img_24: in_hand_laptop
convert_lifestyle('in_hand_laptop', 'assets/4k/img_16.webp')
convert_lifestyle('in_hand_laptop', 'assets/4k/img_06.webp')
convert_lifestyle('in_hand_laptop', 'assets/4k/img_24.webp')

# img_17, img_21: in_use_car
convert_lifestyle('in_use_car', 'assets/4k/img_17.webp')
convert_lifestyle('in_use_car', 'assets/4k/img_21.webp')

# img_15, img_05, img_23: three_tips_fit
convert_lifestyle('three_tips_fit', 'assets/4k/img_15.webp')
convert_lifestyle('three_tips_fit', 'assets/4k/img_05.webp')
convert_lifestyle('three_tips_fit', 'assets/4k/img_23.webp')
convert_lifestyle('three_tips_fit', 'assets/4k/img_12.webp')

print("All generated 4K photos deployed successfully into assets/4k/.")
