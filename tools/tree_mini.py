"""The orange tree, cut out of the village painting, for the footer.

  in:  assets/village-day.webp, assets/village-night.webp
  out: assets/tree-day.webp, assets/tree-night.webp (transparent background)

The tree stands in front of the blue and yellow houses, so it is cut out by
colour: leaves (green), oranges and the trunk (orange-brown) stay; the
whitewash, the blue trim and the yellow wall go. The mask is made once from
the day painting and used for both layers, so day and night line up.
Run from the project root:  python tools/tree_mini.py
"""
import colorsys

import numpy as np
from PIL import Image, ImageDraw, ImageFilter

# The tree in picture pixels (1926 x 817): canopy top to the foot of the trunk
BOX = (478, 278, 766, 712)
H_OUT = 320                            # px tall; the footer shows it at up to 110 px
TRUNK = (612 - BOX[0], 600 - BOX[1])   # a point on the trunk, in the crop


def mask_from(day):
    a = np.asarray(day.convert("RGB"), dtype=np.float32) / 255
    r, g, b = a[..., 0], a[..., 1], a[..., 2]
    mx, mn = a.max(-1), a.min(-1)
    sat = np.where(mx > 0, (mx - mn) / np.maximum(mx, 1e-6), 0)
    hue = np.vectorize(lambda r_, g_, b_: colorsys.rgb_to_hsv(r_, g_, b_)[0] * 360)(r, g, b)
    leaves = (hue > 62) & (hue < 170) & (sat > .18)
    fruit_trunk = ((hue < 38) | (hue > 340)) & (sat > .3)
    m = (leaves | fruit_trunk).astype(np.uint8) * 255
    im = Image.fromarray(m, "L").filter(ImageFilter.MedianFilter(3))
    # keep only the tree: the shape connected to the trunk (drops the flower
    # pots in the blue window and specks of the street)
    grow = im.filter(ImageFilter.MaxFilter(3))          # bridge leaf-to-leaf gaps for the flood only
    ImageDraw.floodfill(grow, TRUNK, 128)
    tree = grow.point(lambda v: 255 if v == 128 else 0)
    t = np.minimum(np.asarray(im), np.asarray(tree))
    t[170:270, :62] = 0                                   # the flower pots in the blue window
    # fill what the tree encloses (the oranges' pale highlights)
    padded = np.pad(255 - t, 1, constant_values=255)     # a clear border to flood from
    outside = Image.fromarray(padded.astype(np.uint8), "L").copy()   # fromarray is read-only to floodfill
    ImageDraw.floodfill(outside, (0, 0), 128)
    holes = np.asarray(outside)[1:-1, 1:-1] == 255
    t = np.where(holes, 255, t).astype(np.uint8)
    im = Image.fromarray(t)
    # a slightly soft edge, like a wet brush, without a halo of wall colour
    return im.filter(ImageFilter.MinFilter(3)).filter(ImageFilter.GaussianBlur(.7))


def cut(src, mask):
    im = Image.open(src).convert("RGBA").crop(BOX)
    im.putalpha(mask)
    w = round(im.width * H_OUT / im.height)
    return im.resize((w, H_OUT), Image.LANCZOS)


day_crop = Image.open("assets/village-day.webp").crop(BOX)
mask = mask_from(day_crop)
for name in ("day", "night"):
    out = cut(f"assets/village-{name}.webp", mask)
    out.save(f"assets/tree-{name}.webp", quality=88, alpha_quality=92, method=6)
    print(f"tree-{name}", out.size)
