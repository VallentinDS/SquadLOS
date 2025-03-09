import pygmt
import numpy as np
from PIL import Image
import xarray as xr

map_dict = {
    "albasrah": 10.0,
    "anvil": 45.0,
    "belaya": 120.0,
    "blackcoast": 80.0,
    "chora": 400.0,
    "fallujah": 100.0,
    "foolsroad": 320.0,
    "goosebay": 40.0,
    "gorodok": 1000.0,
    "harju": 100.0,
    "kamdesh": 135.0,
    "kohat": 75.0,
    "kokan": 100.0,
    "lashkar": 150.0,
    "logar": 49.98999,
    "manicouagan": 300.0,
    "mestia": 120.0,
    "mutaha": 30.0,
    "narva": 100.0,
    "sumari": 75.0,
    "tallil": 125.0,
    "yehorivka": 400.0,
}

for MAP, SCALE_Z in map_dict.items():
    print(f"Processing {MAP}...")
    ORIGINAL_PATH = f"backup_data/satmaps/{MAP}.webp"
    SATMAP_PATH = f"data/satmaps/{MAP}_sat.png"
    HEIGHTMAP_PATH = f"backup_data/heightmaps/{MAP}_heightmap.png"
    ARRAYMAP_PATH = f"data/heightmaps/{MAP}_array.csv"
    CONTOUR_PATH = f"data/contourmaps/{MAP}_contour.png"
    COLOR_PATH = f"data/colormaps/{MAP}_color.png"

    satmap = Image.open(ORIGINAL_PATH)
    # Save as png in satmap path
    satmap.save(SATMAP_PATH)
    satmap_shape = satmap.size

    heightmap = Image.open(HEIGHTMAP_PATH)
    heightmap = heightmap.resize(satmap_shape)
    heightmap = np.array(heightmap)
    heightmap = heightmap.astype(np.uint16)
    heightmap = heightmap[:, :, 0] * 256 + heightmap[:, :, 1]
    heightmap = heightmap * (SCALE_Z / 100) / 100
    heightmap = np.flipud(heightmap)

    np.savetxt(ARRAYMAP_PATH, heightmap, delimiter=",", fmt="%d")
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
    contour.save(CONTOUR_PATH)

    color_fig = pygmt.Figure()

    color_fig.grdimage(
        grid=heightmap,
        cmap="bamako",
    )

    color_fig.savefig(COLOR_PATH, transparent=True, dpi=800)

    colormap = Image.open(COLOR_PATH)
    colormap = colormap.resize(satmap_shape)
    colormap.save(COLOR_PATH)
