import pygmt
import numpy as np
from PIL import Image

# Load the satellite map image
map_im = Image.open("data/kohat_map.webp")
map_array = np.array(map_im)

# Load the heightmap image
im = Image.open("data/kohat_heightmap_raw.png")
im_array = np.array(im)
im_array = im_array * 0.75 / 100  # Convert to meters

# Save the heightmap array to a temporary file
np.savetxt("heightmap.txt", im_array, fmt="%0.2f")

# Create a pygmt figure
fig = pygmt.Figure()

# Plot the satellite map image
fig.grdimage(grid="heightmap.txt", cmap="gray", projection="X10c/10c", frame=True)

# Add contour lines
fig.grdcontour(grid="heightmap.txt", interval=10, annotation="10+f6p", pen="1p,black")

# Save to a PNG file
fig.savefig("output.png")
