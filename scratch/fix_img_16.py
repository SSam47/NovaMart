import math
import numpy as np
from PIL import Image, ImageDraw, ImageFilter

im16 = Image.open('assets/4k/img_16.webp').convert('RGBA')
im17 = Image.open('assets/4k/img_17.webp').convert('RGBA')

# 1. Clean background plate - covers through x=940 to cleanly erase all ash
rgb16 = np.array(im16.convert('RGB'), dtype=np.float32)
x_start, x_end = 750, 945
y_start, y_end = 0, 310

left_strip = rgb16[y_start:y_end, 738:750, :].mean(axis=1) # (310, 3)
right_strip = rgb16[y_start:y_end, 942:954, :].mean(axis=1) # (310, 3)

clean_bg = np.zeros((y_end - y_start, x_end - x_start, 3), dtype=np.float32)
for i in range(x_end - x_start):
    t = i / float(x_end - x_start)
    t_smooth = 0.5 * (1 - math.cos(t * math.pi))
    clean_bg[:, i, :] = (1 - t_smooth) * left_strip + t_smooth * right_strip

clean_bg_img = Image.fromarray(np.clip(clean_bg, 0, 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(radius=5.0))

bg_mask_img = Image.new('L', (x_end - x_start, y_end - y_start), 0)
draw_bg = ImageDraw.Draw(bg_mask_img)

# Coords relative to (750, 0):
poly_cut = [
    (15, 0),
    (x_end - x_start - 5, 0),
    (x_end - x_start - 5, 270),
    (145, 290),
    (58, 244),
    (15, 170)
]
draw_bg.polygon(poly_cut, fill=255)

bg_mask_feathered = bg_mask_img.filter(ImageFilter.GaussianBlur(radius=8.0))

im16_cleaned = im16.copy()
im16_cleaned.paste(clean_bg_img, (x_start, y_start), bg_mask_feathered)

# 2. Extract cork filter tip from im17
tip_crop = im17.crop((630, 415, 735, 510))
mask_img = Image.new('L', tip_crop.size, 0)
draw_tip = ImageDraw.Draw(mask_img)

poly_tip = [(26, 49), (84, 28), (90, 35), (90, 47), (84, 54), (34, 66)]
draw_tip.polygon(poly_tip, fill=255)
mask_smooth = mask_img.filter(ImageFilter.GaussianBlur(radius=0.7))

tip_rgba = tip_crop.copy()
tip_rgba.putalpha(mask_smooth)

# 3. Scale and rotate tip
scale_factor = 1.36
scaled_w = int(tip_rgba.width * scale_factor)
scaled_h = int(tip_rgba.height * scale_factor)
tip_scaled = tip_rgba.resize((scaled_w, scaled_h), Image.Resampling.LANCZOS)
tip_rotated = tip_scaled.rotate(28, Image.Resampling.BICUBIC, expand=True)

# 4. Composite onto im16_cleaned
target_x = 750
target_y = 168

final_img = im16_cleaned.copy()
final_img.paste(tip_rotated, (target_x, target_y), tip_rotated)

# 5. Restore front rim of silicone collar
collar_crop = im16.crop((780, 240, 870, 310))
collar_mask = Image.new('L', collar_crop.size, 0)
draw_cm = ImageDraw.Draw(collar_mask)

poly_front_rim = [
    (28, 6),
    (38, 22),
    (60, 38),
    (85, 48),
    (90, 70),
    (0, 70),
    (0, 26)
]
draw_cm.polygon(poly_front_rim, fill=255)
collar_mask_smooth = collar_mask.filter(ImageFilter.GaussianBlur(radius=1.0))
final_img.paste(collar_crop, (780, 240), collar_mask_smooth)

final_img.convert('RGB').save('scratch/test_final_16_v4.webp', 'WEBP', quality=95, method=6)
print('Done test_final_16_v4.webp')
