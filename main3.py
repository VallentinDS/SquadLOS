import pygmt
import numpy as np
from PIL import Image
import pygmt
import xarray as xr

im = Image.open("data/kohat_heightmap_raw.png")
im_array = np.array(im)
im_array = im_array * 0.75 / 100

da = xr.DataArray(im_array)

fig = pygmt.Figure()
fig.grdcontour(
    grid=da,
    region=[
        0,
        da.shape[1],
        0,
        da.shape[0],
    ],
)
fig.savefig("data/kohat_contour.png", transparent=True, dpi=700)
