"""The terracotta watercolour wash behind the home page's strip of pages.

  out: assets/wash-wide.webp, assets/wash-tall.webp            (day)
       assets/wash-wide-night.webp, assets/wash-tall-night.webp (night)

A band painted wet-in-wet: its edges fade and bloom softly into the paper,
with soft blotches and paper grain inside. "wide" is for desktop (6 pages in a row),
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
    """Wet-in-wet: the pigment fades and blooms into the paper instead of
    stopping at a hard brush edge."""
    rng = np.random.default_rng(seed)
    margin = min(round(h * .17), 44)              # room for the soft fade
    feather = margin * .85
    top = margin + edge(rng, w, margin * .3)
    bottom = h - margin + edge(rng, w, margin * .3)
    yy = np.arange(h)[:, None]
    xx = np.arange(w)[None, :]
    end = min(round(w * .035), 60)                # long, soft tapering ends
    left = end + edge(rng, h, end * .3)[:, None] + (2 * (yy / h) - 1) ** 2 * end * .8
    right = w - end + edge(rng, h, end * .3)[:, None] - (2 * (yy / h) - 1) ** 2 * end * .8
    inside = np.minimum.reduce([yy - top[None, :], bottom[None, :] - yy, xx - left, right - xx])
    # blooms: the wet edge creeps out unevenly
    inside = inside + noise(rng, h, w, 60, feather * .4) + noise(rng, h, w, 24, feather * .08)
    t = np.clip((inside + feather * .55) / (feather * 1.4), 0, 1)
    alpha = t * t * (3 - 2 * t)                   # smoothstep

    blotch = noise(rng, h, w, 120, .06) + noise(rng, h, w, 34, .03)
    grain = ndimage.gaussian_filter(rng.normal(0, .022, (h, w)), .6)
    shade = 1 + blotch + grain
    rgb = PIGMENT[None, None, :] * np.clip(shade, .82, 1.0)[..., None]
    return np.clip(rgb, 0, 255), alpha


for name, (w, h, seed) in {"wide": (1800, 240, 11), "tall": (900, 520, 12)}.items():
    rgb, a = wash(w, h, seed)
    for suffix, col in (("", rgb), ("-night", night(rgb))):
        out = np.dstack([np.clip(col, 0, 255), a * 255]).astype(np.uint8)
        Image.fromarray(out, "RGBA").save(f"assets/wash-{name}{suffix}.webp", quality=86, alpha_quality=90, method=6)
    print(name, (w, h), "lightest", rgb[a > .99].max(0).round(), "darkest", rgb[a > .99].min(0).round())
