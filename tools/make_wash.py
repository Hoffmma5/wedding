"""The terracotta watercolour wash behind the home page's strip of pages.

  out: assets/wash-wide.webp, assets/wash-tall.webp            (day)
       assets/wash-wide-night.webp, assets/wash-tall-night.webp (night)

A brushed band with ragged top and bottom edges, pigment pooling darker at the
rims, soft blotches and paper grain. "wide" is for desktop (6 pages in a row),
"tall" for phones (3 x 2). Night versions use the same tint as the night
painting (tools/make_layers.py), so the strip sits in the same dusk.

The pigment stays dark enough for cream text (lightest areas ~4.5 : 1).
Run from the project root:  python tools/make_wash.py
"""
import numpy as np
from PIL import Image
from scipy import ndimage

PIGMENT = np.array([186, 68, 22])        # roof terracotta, a touch deeper than the roofs
NIGHT_TINT = np.array([0.24, 0.29, 0.48])


def night(rgb):
    lum = rgb @ np.array([.299, .587, .114])
    return (rgb * .7 + lum[..., None] * .3) * NIGHT_TINT * 1.9   # a little lighter than the walls


def noise(rng, h, w, cell, amp):
    small = rng.normal(0, 1, (h // cell + 2, w // cell + 2)).astype(np.float32)
    return np.asarray(Image.fromarray(small).resize((w, h), Image.BICUBIC)) * amp


def edge(rng, w, amp):
    # a ragged brush edge: long swells plus a little bristle
    xs = np.arange(w)
    e = np.zeros(w)
    for cell, a in ((320, 1.0), (110, .4), (36, .1)):
        knots = rng.normal(0, 1, w // cell + 3)
        e += np.interp(xs / cell, np.arange(len(knots)), knots) * a
    return e * amp


def wash(w, h, seed):
    rng = np.random.default_rng(seed)
    margin = min(round(h * .09), 26)
    top = margin + edge(rng, w, margin * .55)
    bottom = h - margin + edge(rng, w, margin * .55)
    yy = np.arange(h)[:, None]
    xx = np.arange(w)[None, :]
    # the brush ends: ragged, slightly rounded tips instead of a straight cut
    end = min(round(w * .014), 14)
    left = end + edge(rng, h, end * .8)[:, None] + (2 * (yy / h) - 1) ** 2 * end * 1.4
    right = w - end + edge(rng, h, end * .8)[:, None] - (2 * (yy / h) - 1) ** 2 * end * 1.4
    inside = np.minimum.reduce([yy - top[None, :], bottom[None, :] - yy, xx - left, right - xx])
    inside = np.clip(inside, -2, 60)
    alpha = np.clip(inside / 2.2 + .5, 0, 1)

    # pigment pools at the drying edge: darker within ~10 px of the rim
    rim = np.exp(-np.clip(inside, 0, None) / 9.0) * alpha
    blotch = noise(rng, h, w, 120, .07) + noise(rng, h, w, 34, .035)
    grain = rng.normal(0, .025, (h, w))
    grain = ndimage.gaussian_filter(grain, .6)
    shade = 1 + blotch + grain - .16 * rim                     # < 1 = more pigment
    rgb = PIGMENT[None, None, :] * np.clip(shade, .8, 1.0)[..., None]
    # a few lighter, wetter pools in the middle of the band
    pools = np.clip(noise(rng, h, w, 200, 1.0) - .9, 0, None) * .03
    rgb = rgb + (255 - rgb) * pools[..., None] * alpha[..., None]
    return np.clip(rgb, 0, 255), alpha


for name, (w, h, seed) in {"wide": (1800, 240, 11), "tall": (900, 520, 12)}.items():
    rgb, a = wash(w, h, seed)
    for suffix, col in (("", rgb), ("-night", night(rgb))):
        out = np.dstack([np.clip(col, 0, 255), a * 255]).astype(np.uint8)
        Image.fromarray(out, "RGBA").save(f"assets/wash-{name}{suffix}.webp", quality=86, alpha_quality=90, method=6)
    print(name, (w, h), "lightest", rgb[a > .99].max(0).round(), "darkest", rgb[a > .99].min(0).round())
