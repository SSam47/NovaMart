import math
import numpy as np
from PIL import Image, ImageDraw, ImageFilter

# Load fresh original car_driver image (unedited)
src_orig = r'C:\Users\OMEN\.gemini\antigravity-ide\brain\bf6de799-a5f8-4130-abc4-d2f2a26c98ba\car_driver_smoke_ashtray_1792391464210.jpg'
orig = Image.open(src_orig).convert('RGBA')
im17 = Image.open('assets/4k/img_17.webp').convert('RGBA')

# 1. Background clean plate to erase smoke and the burnt ash tip above the cigarette shaft
# The shaft ends around (760+115, 200+15) = (875, 215) and (760+137, 200+39) = (897, 239)
# Burnt ash is above that: y < 225, x > 870
# Smoke extends upwards: y: 0..220, x: 750..920

rgb_orig = np.array(orig.convert('RGB'), dtype=np.float32)
x_start, x_end = 760, 950
y_start, y_end = 0, 240

left_strip = rgb_orig[y_start:y_end, 745:758, :].mean(axis=1) # (240, 3)
right_strip = rgb_orig[y_start:y_end, 945:958, :].mean(axis=1) # (240, 3)

clean_bg = np.zeros((y_end - y_start, x_end - x_start, 3), dtype=np.float32)
for i in range(x_end - x_start):
    t = i / float(x_end - x_start)
    t_smooth = 0.5 * (1 - math.cos(t * math.pi))
    clean_bg[:, i, :] = (1 - t_smooth) * left_strip + t_smooth * right_strip

clean_bg_img = Image.fromarray(np.clip(clean_bg, 0, 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(radius=5.0))

# Mask covers smoke and the burnt tip, but stops ABOVE the clean cylinder cap
bg_mask_img = Image.new('L', (x_end - x_start, y_end - y_start), 0)
draw_bg = ImageDraw.Draw(bg_mask_img)

# Coords relative to (760, 0):
# Cap line in im16 coords: (872, 212) to (898, 238)
# In local coords: (872-760, 212) = (112, 212) to (898-760, 238) = (138, 238)
poly_cut = [
    (15, 0),
    (x_end - x_start - 5, 0),
    (x_end - x_start - 5, 230),
    (138, 236),
    (112, 212),
    (15, 140)
]
draw_bg.polygon(poly_cut, fill=255)
bg_mask_feathered = bg_mask_img.filter(ImageFilter.GaussianBlur(radius=6.0))

cleaned = orig.copy()
cleaned.paste(clean_bg_img, (x_start, y_start), bg_mask_feathered)

# 2. Extract cork filter from im17
tip_crop = im17.crop((630, 415, 735, 510))
mask_img = Image.new('L', tip_crop.size, 0)
draw_tip = ImageDraw.Draw(mask_img)

# Exact cork cylinder polygon in tip_crop:
# Top edge: (26, 49) to (84, 28)
# Circular end: (84, 28) -> (90, 35) -> (90, 47) -> (84, 54)
# Bottom edge: (84, 54) to (34, 66)
# Base: (34, 66) to (26, 49)
poly_tip = [(26, 49), (84, 28), (90, 35), (90, 47), (84, 54), (34, 66)]
draw_tip.polygon(poly_tip, fill=255)
mask_smooth = mask_img.filter(ImageFilter.GaussianBlur(radius=0.7))

tip_rgba = tip_crop.copy()
tip_rgba.putalpha(mask_smooth)

# Scale and rotate to match the exact shaft dimensions:
# Original shaft width in im16 is 30px (from (74,52) to (96,76) distance = sqrt(22^2 + 24^2) = 32.5px)
# In tip_crop, base width is sqrt(8^2 + 17^2) = 18.8px
# Scale factor = 32.5 / 18.8 = 1.72 (or 1.65)
# Angle: counter-clockwise 28 deg
scale_factor = 1.68
scaled_w = int(tip_rgba.width * scale_factor)
scaled_h = int(tip_rgba.height * scale_factor)
tip_scaled = tip_rgba.resize((scaled_w, scaled_h), Image.Resampling.LANCZOS)
tip_rotated = tip_scaled.rotate(28, Image.Resampling.BICUBIC, expand=True)

# Find the base center of tip_rotated:
# In tip_crop, base center was at ((26+34)/2, (49+66)/2) = (30, 57.5)
# After scale: (30 * 1.68, 57.5 * 1.68) = (50.4, 96.6)
# Relative to rotated box center:
w_rot, h_rot = tip_rotated.size
# Let's inspect where base is by placing it:
# We want base to land at (845, 264) in im16 coordinates!
target_x = 818
target_y = 158

test_img = cleaned.copy()
test_img.paste(tip_rotated, (target_x, target_y), tip_rotated)

crop_test = test_img.crop((750, 150, 920, 340))
crop_test.save('scratch/exact_tip_test.png')
print('exact_tip_test.png saved')
