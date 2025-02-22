import pygmt
import numpy as np
from PIL import Image
import pygmt
import xarray as xr

im = Image.open("data/gorodok_heightmap.png")
im_array = np.array(im)
target = im_array[1000, 1300]
target = (target[0] << 8) + target[1]

im_array = im_array.astype(np.uint16)

im_array = im_array[:, :, 0] * 256 + im_array[:, :, 1]

im_array = im_array * (1000 / 100) / 100

im_array = np.flipud(im_array)

da = xr.DataArray(im_array)

fig = pygmt.Figure()
"""fig.grdimage(
    grid=da,
    cmap="bamako",
)"""
fig.grdcontour(
    grid=da,
    levels=10,
    annotation="20+f4p",
    pen="0.1p,black",
)

fig.savefig("data/gorodok_contour.png", transparent=True, dpi=700)
