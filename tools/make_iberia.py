"""A torn-out piece of an old paper map: the invitation's watercolour Portugal,
western Spain as pale land, the Atlantic with cartographic water lines.

  in:  assets/art/portugal.webp      (Portugal only, from the invitation)
  out: assets/art/iberia-map.webp    (the torn map piece, transparent around it)

Labels, Tavira, Faro and the flight path are an SVG on top of the picture in
travel.html (tools/make_pages.py), in the same canvas coordinates (MAP_W x MAP_H),
so the text stays crisp.

The painted Portugal is stylised, so Spain's coasts are fitted to the painting,
not to true coordinates: about 114 px per degree east and 139 px per degree
north, anchored on the Guadiana mouth (212, 690 in portugal.webp pixels).

Run from the project root:  python tools/make_iberia.py
"""
import numpy as np
from PIL import Image, ImageFilter
from scipy import ndimage

rng = np.random.default_rng(7)

PAPER = np.array([247, 241, 227])     # old map paper
SEA = np.array([221, 232, 234])
WATERLINE = np.array([120, 160, 178])
LAND = np.array([239, 230, 207])      # Spain
COASTLINE = np.array([176, 152, 112])

pt = Image.open("assets/art/portugal.webp").convert("RGBA")
pw, ph = pt.size                      # 373 x 722
LEFT, TOP, RIGHT, BOTTOM = 120, 80, 230, 120
MAP_W, MAP_H = LEFT + pw + RIGHT, TOP + ph + BOTTOM      # 723 x 922

a_pt = np.zeros((MAP_H, MAP_W), np.float32)
a_pt[TOP:TOP + ph, LEFT:LEFT + pw] = np.asarray(pt)[..., 3] / 255.


def low_noise(cell, amp):
    small = rng.normal(0, 1, (MAP_H // cell + 2, MAP_W // cell + 2)).astype(np.float32)
    return np.asarray(Image.fromarray(small).resize((MAP_W, MAP_H), Image.BICUBIC)) * amp


# --- Spain ---------------------------------------------------------------
# Gulf of Cadiz, in portugal.webp pixels: Guadiana mouth, Huelva, Donana,
# Guadalquivir, Chipiona, Rota, Cadiz, towards Trafalgar
GULF = [(212, 690), (240, 687), (266, 686), (288, 697), (309, 712), (333, 744),
        (326, 751), (334, 766), (342, 781), (352, 800), (371, 828), (380, 900)]
# Galicia north of the Minho: coast x for a given y (above Portugal's top),
# with the Ria de Vigo and the Ria de Pontevedra cut in
RIAS = [(-16, 4, 16), (-44, 3.5, 13), (-68, 3, 10)]         # (y, half-width, depth)


def galicia_coast(py):
    x = 92 + .22 * py + 3 * np.sin(py / 7.0)      # the coast leans west going north
    for ry, hw, depth in RIAS:
        x += depth * np.exp(-((py - ry) / hw) ** 2)
    return x


spain = np.zeros((MAP_H, MAP_W), bool)
gx, gy = zip(*GULF)
for y in range(MAP_H):
    py = y - TOP
    if py < 64:                                   # Galicia and the Minho border: Spain runs on under Portugal
        x0 = galicia_coast(py) if py < 0 else 92
        spain[y, LEFT + int(x0):] = True
        continue
    row = a_pt[y] > .25
    xs = np.where(row)[0]
    if py < ph and len(xs):
        x_east = xs.max() - 6                     # tuck under Portugal's eastern edge
    else:
        x_east = LEFT + 212
    for x in range(int(x_east), MAP_W):
        px = x - LEFT
        coast = np.interp(px, gx, gy)             # sea south of this line
        if py <= coast:
            spain[y, x] = True

land = spain | (a_pt > .25)
# a slightly painted, uneven shoreline
soft = ndimage.gaussian_filter(land.astype(np.float32), 1.6) + low_noise(7, .12)
land_soft = np.clip((soft - .5) / .25 + .5, 0, 1)
spain_soft = np.clip(ndimage.gaussian_filter(spain.astype(np.float32), 1.6) + low_noise(7, .12), 0, 1)
spain_soft = np.clip((spain_soft - .5) / .25 + .5, 0, 1)   # Spain runs on under Portugal

# --- paper, sea and water lines ------------------------------------------
img = PAPER[None, None, :] * (1 + low_noise(60, .012) + low_noise(14, .008))[..., None]
img = img * (1 + rng.normal(0, .012, (MAP_H, MAP_W)))[..., None]

sea_tone = 1 - land_soft
img = img * (1 - .55 * sea_tone[..., None]) + SEA[None, None, :] * (.55 * sea_tone[..., None])

dist = ndimage.distance_transform_edt(~land)
lines = np.zeros_like(dist)
for k, (d, strength) in enumerate([(5, .7), (11, .55), (18, .4), (27, .27), (38, .16)]):
    wobble = low_noise(30, .9)
    lines = np.maximum(lines, np.clip(1 - np.abs(dist + wobble - d) / .75, 0, 1) * strength)
lines *= sea_tone
img = img * (1 - lines[..., None]) + WATERLINE[None, None, :] * lines[..., None]

# Spain: a pale wash with a pencilled coastline
wash = 1 + low_noise(90, .014) + low_noise(22, .008)
land_col = LAND[None, None, :] * wash[..., None]
img = img * (1 - spain_soft[..., None]) + land_col * spain_soft[..., None]
coast = np.clip(1 - np.abs(ndimage.distance_transform_edt(land) - 1.0) / 1.0, 0, 1) * (1 - np.clip(a_pt * 2, 0, 1))
img = img * (1 - .55 * coast[..., None]) + COASTLINE[None, None, :] * (.55 * coast[..., None])

canvas = Image.fromarray(np.clip(img, 0, 255).astype(np.uint8), "RGB").convert("RGBA")
canvas.alpha_composite(pt, (LEFT, TOP))

# --- torn edges ------------------------------------------------------------
yy, xx = np.mgrid[0:MAP_H, 0:MAP_W].astype(np.float32)
inset = 9
edge_d = np.minimum.reduce([xx - inset, MAP_W - 1 - inset - xx, yy - inset, MAP_H - 1 - inset - yy])
tear = low_noise(26, 3.2) + low_noise(6, 1.4) + rng.normal(0, .5, (MAP_H, MAP_W))
alpha = np.clip((edge_d + tear) / 1.2 + .5, 0, 1)
# torn paper shows a lighter, fibrous rim
rim = np.clip(1 - (edge_d + tear) / 4, 0, 1) * alpha
rgb = np.asarray(canvas)[..., :3].astype(np.float32)
rgb = rgb * (1 - .5 * rim[..., None]) + np.array([252, 249, 240]) * (.5 * rim[..., None])

out = np.dstack([np.clip(rgb, 0, 255), alpha * 255]).astype(np.uint8)
Image.fromarray(out, "RGBA").save("assets/art/iberia-map.webp", quality=88, alpha_quality=95, method=6)
print("iberia-map", (MAP_W, MAP_H), "portugal at", (LEFT, TOP))
