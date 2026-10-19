import glob, os
from PIL import Image
import numpy as np

brain_dir = r'C:\Users\OMEN\.gemini\antigravity-ide\brain\bf6de799-a5f8-4130-abc4-d2f2a26c98ba'

matches = glob.glob(os.path.join(brain_dir, 'walnut_ashtray_hero*.jpg'))
print("Matches:", matches)
if matches:
    im = Image.open(matches[0]).convert('RGBA')
    arr = np.array(im)
    print("Array shape:", arr.shape)
    
    # Check pixels in the upper collar region
    # Look at collar pixel values:
    collar_crop = arr[100:300, 300:700]
    r, g, b = collar_crop[:, :, 0], collar_crop[:, :, 1], collar_crop[:, :, 2]
    high_pixels = (r > 240) & (g > 240) & (b > 240)
    print("Collar high pixels (>240):", np.sum(high_pixels))
    high_pixels_248 = (r > 248) & (g > 248) & (b > 248)
    print("Collar high pixels (>248):", np.sum(high_pixels_248))
