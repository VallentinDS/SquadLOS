import pygmt
import numpy as np
from PIL import Image
import xarray as xr

MAP = "manicouagan"
SATMAP_PATH = "data/satmaps/Manicouagan_Map.png"
HEIGHTMAP_PATH = "data/heightmaps/Manicouagan_Heightmap.png"
ARRAYMAP_PATH = "data/arraymaps/manicouagan_array.csv"
CONTOUR_PATH = "data/contourmaps/manicouagan_contour.png"
COLOR_PATH = "data/colormaps/manicouagan_colormap.png"
SCALE_Z = 300

satmap = Image.open(SATMAP_PATH)
satmap_shape = satmap.size

heightmap = Image.open(HEIGHTMAP_PATH)
heightmap = heightmap.resize(satmap_shape)
heightmap = np.array(heightmap)
heightmap = heightmap.astype(np.uint16)
heightmap = heightmap[:, :, 0] * 256 + heightmap[:, :, 1]
heightmap = heightmap * (SCALE_Z / 100) / 100
heightmap = np.flipud(heightmap)
np.savetxt(ARRAYMAP_PATH, heightmap, delimiter=",")
heightmap = xr.DataArray(heightmap)

fig = pygmt.Figure()

fig.grdcontour(
    grid=heightmap,
    levels=10,
    annotation="20+f4p",
    pen="0.1p,black",
)

fig.savefig(CONTOUR_PATH, transparent=True, dpi=800)

contour = Image.open(CONTOUR_PATH)
contour = contour.resize(satmap_shape)
contour.save("data/contourmaps/manicouagan_contour.png")

color_fig = pygmt.Figure()

color_fig.grdimage(
    grid=heightmap,
    cmap="bamako",
)

color_fig.savefig(COLOR_PATH, transparent=True, dpi=800)

colormap = Image.open(COLOR_PATH)
colormap = colormap.resize(satmap_shape)
colormap.save("data/colormaps/manicouagan_colormap.png")
