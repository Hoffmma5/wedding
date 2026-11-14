"""The wash behind the home page's strip of pages, painted like the street
under the houses in the village painting.

  out: assets/wash-wide.webp, assets/wash-tall.webp            (day)
       assets/wash-wide-night.webp, assets/wash-tall-night.webp (night)

A pale sand wash in long horizontal strokes, a warmer sienna streak along the
top like the kerb, a faint violet shadow, edges that fade softly into the
paper. "wide" is for desktop (6 pages in a row), "tall" for phones (3 x 2).
Night versions use the night painting's tint, like the night street.

Dark olive labels sit on it by day (> 7 : 1), cream labels by night.
Run from the project root:  python tools/make_wash.py
"""
import numpy as np
from PIL import Image
from scipy import ndimage

SAND = np.array([241, 220, 199])          # the street in the painting
SIENNA = np.array([214, 166, 128])        # the kerb streak
SHADOW = np.array([214, 204, 222])        # faint violet shadow
NIGHT_TINT = np.array([0.24, 0.29, 0.48])


def night(rgb):
    lum = rgb @ np.array([.299, .587, .114])
    return (rgb * .7 + lum[..., None] * .3) * NIGHT_TINT * 1.05   # the night street


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
    inside = inside + np.clip(noise(rng, h, w, 60, feather * .3), -feather * .25, None) + noise(rng, h, w, 24, feather * .06)
    t = np.clip((inside + feather * .55) / (feather * 1.4), 0, 1)
    alpha = t * t * (3 - 2 * t)                   # smoothstep

    def strokes(cx, cy, amp):          # long horizontal brush strokes
        small = rng.normal(0, 1, (h // cy + 2, w // cx + 2)).astype(np.float32)
        return np.asarray(Image.fromarray(small).resize((w, h), Image.BICUBIC)) * amp

    rgb = SAND[None, None, :] * (1 + strokes(180, 9, .018) + strokes(60, 4, .01))[..., None]
    # sienna streak a third of the way down, broken up along its length
    y_kerb = top + (bottom - top) * .26
    kerb = np.exp(-((yy - y_kerb[None, :]) / (h * .06)) ** 2) * np.clip(.55 + strokes(140, 30, .45), 0, 1)
    rgb = rgb * (1 - kerb[..., None] * .55) + SIENNA[None, None, :] * (kerb[..., None] * .55)
    # a faint cool shadow lower down, like the painting's
    cool = np.exp(-((yy - (top + (bottom - top) * .6)[None, :]) / (h * .12)) ** 2) * np.clip(strokes(220, 40, .6), 0, 1) * .35
    rgb = rgb * (1 - cool[..., None]) + SHADOW[None, None, :] * cool[..., None]
    rgb = rgb * (1 + ndimage.gaussian_filter(rng.normal(0, .012, (h, w)), .6))[..., None]
    return np.clip(rgb, 0, 255), alpha


for name, (w, h, seed) in {"wide": (1800, 240, 11), "tall": (900, 520, 12)}.items():
    rgb, a = wash(w, h, seed)
    for suffix, col in (("", rgb), ("-night", night(rgb))):
        out = np.dstack([np.clip(col, 0, 255), a * 255]).astype(np.uint8)
        Image.fromarray(out, "RGBA").save(f"assets/wash-{name}{suffix}.webp", quality=86, alpha_quality=90, method=6)
    print(name, (w, h), "lightest", rgb[a > .99].max(0).round(), "darkest", rgb[a > .99].min(0).round(), "mean", rgb[a > .99].mean(0).round())
