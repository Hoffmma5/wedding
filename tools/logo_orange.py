"""The orange emblem in colour, for the footer: an orange body, green leaves.

  in:  assets/logo-mark.png   (the emblem as alpha, from tools/make_layers.py)
  out: assets/logo-orange.webp

The emblem is one ink, so it is coloured by shape: everything inside the
body's circle is the orange (the M&P stays cut out), everything outside it
(the leaves and the stem) is the leaf green. Both get a soft light-to-dark
wash, top left to bottom right, like the oranges in the painting.
Run from the project root:  python tools/logo_orange.py
"""
import numpy as np
from PIL import Image, ImageDraw, ImageFilter

BODY = (104.5, 101.0, 56.5)          # the body's circle in the mark: cx, cy, r (px)
ORANGE = ((246, 160, 66), (214, 98, 30))   # light, dark
GREEN = ((122, 160, 72), (74, 110, 44))

mark = Image.open("assets/logo-mark.png").convert("RGBA")
a = np.asarray(mark)[..., 3].astype(float) / 255
h, w = a.shape
y, x = np.mgrid[0:h, 0:w]
cx, cy, r = BODY
inside = (x - cx) ** 2 + (y - cy) ** 2 <= r ** 2
circle = inside
# the big leaf's base reaches into the circle: keep only what is joined to
# the body's centre there (the logo's white gap separates the two)
seed = Image.fromarray(((a > .5) & inside).astype(np.uint8) * 255, "L").copy()
ImageDraw.floodfill(seed, (int(cx), int(cy) + 20), 128)
inside = np.asarray(seed) == 128
inside = (np.asarray(Image.fromarray(inside.astype(np.uint8) * 255).filter(ImageFilter.MaxFilter(5))) > 0) & circle   # take in the soft edges
t = np.clip(((x / w) + (y / h)) / 2, 0, 1)[..., None]          # 0 top left, 1 bottom right


def wash(pair):
    lo, hi = np.array(pair[0], float), np.array(pair[1], float)
    return lo * (1 - t) + hi * t


rgb = np.where(inside[..., None], wash(ORANGE), wash(GREEN))
out = np.dstack([rgb, a * 255]).astype(np.uint8)
im = Image.fromarray(out, "RGBA")
im = im.resize((w * 2, h * 2), Image.LANCZOS)     # crisp enough on 2x screens at footer size
im.save("assets/logo-orange.webp", quality=90, alpha_quality=95, method=6)
print("logo-orange", im.size)
