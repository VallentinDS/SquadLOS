from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import pygmt

# The satellite map image is 4096x4096 pixels
map_im = Image.open("data/kohat_map.webp")
# The heightmap image is 4065x4065 pixels
im = Image.open("data/kohat_heightmap_raw.png")
buf = im.load()
im_array = np.array(im)
print("min:", np.min(im_array) * 0.75 / 100)  # Prints 1 meter
print("max:", np.max(im_array) * 0.75 / 100)  # Prints 420 meters

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# The satellite map image is 4096x4096 pixels
map_im = Image.open("data/kohat_map.webp")
# The heightmap image is 4065x4065 pixels
im = Image.open("data/kohat_heightmap_raw.png")
buf = im.load()
im_array = np.array(im)

# Print min and max height values
print("min:", np.min(im_array) * 0.75 / 100)  # Prints 1 meter
print("max:", np.max(im_array) * 0.75 / 100)  # Prints 420 meters

# Plotting the images
fig, ax = plt.subplots()
ax.imshow(map_im, extent=[0, map_im.width, 0, map_im.height])
ax.imshow(im_array, cmap="jet", alpha=0.5, extent=[0, map_im.width, 0, map_im.height])
plt.show()
