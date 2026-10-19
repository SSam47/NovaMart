from PIL import Image, ImageFilter
import numpy as np

# Load high-res beech hero master
src_path = r'C:\Users\OMEN\.gemini\antigravity-ide\brain\bf6de799-a5f8-4130-abc4-d2f2a26c98ba\beech_ashtray_hero_1792388573030.jpg'
im = Image.open(src_path).convert('RGB')

# Let's crop the cylinder cleanly
# The cylinder in im (1024x1024) spans roughly:
# x: 380..635, y: 10..980
arr = np.array(im)
# Find bounding box of object (non-white pixels)
r, g, b = arr[:, :, 0], arr[:, :, 1], arr[:, :, 2]
is_not_white = (r < 250) | (g < 250) | (b < 250)

# Get vertical and horizontal bounds
y_indices, x_indices = np.where(is_not_white)
ymin, ymax = y_indices.min(), y_indices.max()
xmin, xmax = x_indices.min(), x_indices.max()
print(f'Object bounds: x=[{xmin}, {xmax}], y=[{ymin}, {ymax}]')

# Create a clean high-res canvas (1200 x 1600) matching the story section's warm luxury aesthetic
canvas_w, canvas_h = 1200, 1600

# Background: soft subtle radial gradient from #f4ece1 to #ebe1d2
bg = Image.new('RGB', (canvas_w, canvas_h))
bg_arr = np.zeros((canvas_h, canvas_w, 3), dtype=np.float32)

cx, cy = canvas_w * 0.5, canvas_h * 0.5
c_center = np.array([244.0, 236.0, 225.0]) # #f4ece1
c_outer = np.array([230.0, 220.0, 206.0])  # #e6dcd0

for y in range(canvas_h):
    for x in range(canvas_w):
        dx = (x - cx) / (canvas_w * 0.6)
        dy = (y - cy) / (canvas_h * 0.6)
        dist = min(1.0, np.sqrt(dx*dx + dy*dy))
        bg_arr[y, x] = (1 - dist) * c_center + dist * c_outer

bg = Image.fromarray(np.clip(bg_arr, 0, 255).astype(np.uint8))

# Isolate cylinder object with smooth antialiased alpha
alpha = np.zeros((1024, 1024), dtype=np.uint8)
# Floodfill or mask non-white
from scipy import ndimage
obj_mask = ndimage.binary_fill_holes(is_not_white)
alpha = (obj_mask * 255).astype(np.uint8)
alpha_img = Image.fromarray(alpha, mode='L').filter(ImageFilter.GaussianBlur(radius=0.8))

cyl_rgba = im.copy().convert('RGBA')
cyl_rgba.putalpha(alpha_img)

# Crop tight to cylinder
cyl_crop = cyl_rgba.crop((xmin - 10, ymin - 10, xmax + 10, ymax + 10))

# Scale cylinder to look majestic and prominent in the frame
# Desired cylinder height: ~1250 px
scale = 1250.0 / cyl_crop.height
new_w = int(cyl_crop.width * scale)
new_h = int(cyl_crop.height * scale)
cyl_scaled = cyl_crop.resize((new_w, new_h), Image.Resampling.LANCZOS)

# Soft luxury ambient contact shadow behind cylinder
shadow = Image.new('RGBA', (canvas_w, canvas_h), (0, 0, 0, 0))
pos_x = (canvas_w - new_w) // 2
pos_y = (canvas_h - new_h) // 2

# Draw realistic contact shadow
shadow_strip = Image.new('L', (new_w + 100, new_h + 100), 0)
s_arr = np.zeros((new_h + 100, new_w + 100), dtype=np.float32)
# Shadow below cylinder
s_arr[new_h + 10:new_h + 60, 50:new_w + 50] = 70.0
shadow_strip = Image.fromarray(s_arr.astype(np.uint8), mode='L').filter(ImageFilter.GaussianBlur(radius=25.0))

shadow.paste(Image.new('RGBA', shadow_strip.size, (40, 28, 18, 120)), (pos_x - 50, pos_y), shadow_strip)

# Composite final image
final = bg.convert('RGBA')
final = Image.alpha_composite(final, shadow)
final.paste(cyl_scaled, (pos_x, pos_y), cyl_scaled)

out_webp = 'scratch/test_beech_story_macro.webp'
final.convert('RGB').save(out_webp, 'WEBP', quality=96, method=6)
print(f'Saved ultra-sharp high-res {out_webp}: {final.size}')
