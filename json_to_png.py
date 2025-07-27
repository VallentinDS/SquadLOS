# import json
# import numpy as np
# import matplotlib.pyplot as plt
# from PIL import Image

# # Load 2D height data from JSON
# data = json.load(open('D:\Squad\SquadLOS\heightmap.json'))
# arr = np.array(data, dtype=float)

# # Normalize array to [0,1] (in-place for efficiency):contentReference[oaicite:3]{index=3}:contentReference[oaicite:4]{index=4}
# arr -= arr.min()
# if arr.max() != 0:
#     arr /= arr.max()

# # Apply the 'terrain' colormap (dropping alpha channel)
# # terrain_map = plt.get_cmap('terrain')
# terrain_map = plt.colormaps.get_cmap('terrain')
# rgba_img = terrain_map(arr)          # Shape (h, w, 4), with floats in [0,1]
# rgb_img = (rgba_img[:, :, :3] * 255).astype(np.uint8)

# # Create an image and resize to 4065×4065 with high-quality resampling
# img = Image.fromarray(rgb_img)
# img = img.resize((4065, 4065), resample=Image.LANCZOS)
# img.save('D:\Squad\SquadLOS\heightmap_output.png')


# ----

import json
import numpy as np
from matplotlib import colormaps     # modern Matplotlib ≥3.7 API
from PIL import Image

JSON_PATH   = "D:\Squad\SquadLOS\heightmap.json"   # <-- change if needed
PREVIEW_PX  = 512                        # width & height of each panel
OUTFILE     = "D:\Squad\SquadLOS\colormap_comparison.png"
CMAPS       = ["terrain", "gist_earth", "viridis", "cividis"]

# 1) Load height-map
with open(JSON_PATH) as f:
    arr = np.array(json.load(f), dtype=float)

# 2) Normalise to 0-1
arr -= arr.min()
if arr.max():           # avoid divide-by-zero
    arr /= arr.max()

# 3) Down-sample for a quick preview (keeps big-picture patterns)
s = max(1, arr.shape[0] // PREVIEW_PX)       # stride
preview = arr[::s, ::s]

# 4) Build each colour panel
panels = []
for name in CMAPS:
    cmap = colormaps.get_cmap(name)              # modern call
    rgb  = (cmap(preview)[:, :, :3] * 255).astype(np.uint8)
    panels.append(Image.fromarray(rgb).resize((PREVIEW_PX, PREVIEW_PX),
                                              Image.NEAREST))

# 5) Stitch panels side-by-side
canvas = Image.new("RGB", (PREVIEW_PX * len(panels), PREVIEW_PX))
for i, p in enumerate(panels):
    canvas.paste(p, (i * PREVIEW_PX, 0))
canvas.save(OUTFILE)
print(f"Saved {OUTFILE}")