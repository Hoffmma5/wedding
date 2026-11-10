"""Build every image layer the homepage uses from the source pictures.

Sources (keep these):
  assets/village.webp            the village painting (1926 x 817)
  assets/src/lamp.png            the street lamp painting (white background)
  assets/src/logo.png            the logo (olive ink on white)

Outputs:
  assets/village-day.webp        village with the paper background made transparent
  assets/village-night.webp      same, darkened and tinted for night
  assets/lights-windows.png      lit window glass (night)
  assets/lamp-day.png / lamp-night.png / lamp-lit.png
  assets/logo-mark.png           the orange emblem (alpha = ink), recoloured in CSS
  assets/logo-leaf.png           the small leaf ornament

Run from the project root:  python tools/make_layers.py
"""
import numpy as np
from PIL import Image, ImageDraw, ImageFilter

NIGHT_TINT = np.array([0.24, 0.29, 0.48])
WARM_HI = np.array([255, 222, 150])
WARM_LO = np.array([238, 150, 60])
MULLION = np.array([74, 52, 36])

# Window glass rectangles in the village picture (x0, y0, x1, y1)
WINDOWS = [
    (433, 391, 522, 504),    # blue house
    (779, 391, 859, 499),    # yellow house, left
    (1241, 391, 1325, 497),  # yellow house, right
    (1716, 398, 1794, 504),  # coral house
]


def night(rgb):
    lum = rgb @ np.array([.299, .587, .114])
    return (rgb * .7 + lum[..., None] * .3) * NIGHT_TINT


def paper_to_alpha(rgb, paper, tol=22, grow=15):
    """Make the paper that touches the picture's edges transparent ('colour to alpha'),
    keeping enclosed whites (walls, lamp glass) opaque. Returns (colour, alpha)."""
    h, w, _ = rgb.shape
    diff = np.clip(paper[None, None, :] - rgb, 0, None).max(-1)
    binary = Image.fromarray(np.where(diff < tol, 255, 0).astype(np.uint8), "L").copy()  # copy: writable
    seeds = [(x, y) for x in range(0, w, 15) for y in (0, h - 1)] + \
            [(x, y) for y in range(0, h, 15) for x in (0, w - 1)]
    for s in seeds:
        if binary.getpixel(s) == 255:
            ImageDraw.floodfill(binary, s, 128)
    region = np.asarray(binary) == 128
    region = np.asarray(Image.fromarray(region.astype(np.uint8) * 255).filter(ImageFilter.MaxFilter(grow))) > 0

    a = np.clip(((paper[None, None, :] - rgb) / paper[None, None, :]).max(-1), 0, 1)
    alpha = np.where(region, a, 1.0)
    safe = np.maximum(alpha, 1e-3)[..., None]
    colour = np.where(region[..., None], paper - (paper - rgb) / safe, rgb)
    colour = np.clip(colour, 0, 255)
    return colour, alpha


def rgba(colour, alpha):
    out = np.dstack([np.clip(colour, 0, 255), np.clip(alpha * 255, 0, 255)])
    return Image.fromarray(out.round().astype(np.uint8), "RGBA")


def lit_windows(rgb):
    h, w, _ = rgb.shape
    out = np.zeros((h, w, 4), np.uint8)
    for x0, y0, x1, y1 in WINDOWS:
        win = rgb[y0:y1, x0:x1]
        lum = win @ np.array([.299, .587, .114])
        sat = win.max(-1) - win.min(-1)
        r, g, b = win[..., 0], win[..., 1], win[..., 2]
        glass = ~(((r > b + 30) & (sat > 50)) | ((g > b + 35) & (sat > 60)))   # skip pots, flowers, leaves
        bars = glass & (lum > 225) & (sat < 18)
        t = np.clip((lum - 40) / 170, 0, 1)[..., None]
        col = WARM_LO + (WARM_HI - WARM_LO) * t
        col[bars] = MULLION
        out[y0:y1, x0:x1, :3] = col.astype(np.uint8)
        out[y0:y1, x0:x1, 3] = np.where(bars, 230, np.where(glass, 255, 0))
    return Image.fromarray(out, "RGBA")


def lamp_layers():
    src = np.asarray(Image.open("assets/src/lamp.png").convert("RGB")).astype(float)
    colour, alpha = paper_to_alpha(src, np.array([255., 255., 255.]), tol=18, grow=7)
    rgba(colour, alpha).save("assets/lamp-day.png", optimize=True)
    rgba(night(colour), alpha).save("assets/lamp-night.png", optimize=True)

    # Lit glass: the warm, light panes in the lamp head
    lum = src @ np.array([.299, .587, .114])
    r, g, b = src[..., 0], src[..., 1], src[..., 2]
    glass = (r > 150) & (r > b + 8) & (lum > 135) & (alpha > .9)
    glass[:112] = False                         # below the roof of the lantern
    glass[260:] = False                         # head only
    t = np.clip((lum - 135) / 110, 0, 1)[..., None]
    col = np.array([255, 196, 110]) + (np.array([255, 246, 214]) - np.array([255, 196, 110])) * t
    out = np.zeros(src.shape[:2] + (4,), np.uint8)
    out[..., :3] = col.astype(np.uint8)
    out[..., 3] = np.where(glass, 255, 0)
    Image.fromarray(out, "RGBA").filter(ImageFilter.GaussianBlur(.6)).save("assets/lamp-lit.png", optimize=True)


def logo_layers():
    src = np.asarray(Image.open("assets/src/logo.png").convert("RGB")).astype(float)
    lum = src @ np.array([.299, .587, .114])
    ink = np.clip((250 - lum) / (250 - 80), 0, 1)
    def save(box, name):
        x0, y0, x1, y1 = box
        a = (ink[y0:y1, x0:x1] * 255).astype(np.uint8)
        im = np.zeros(a.shape + (4,), np.uint8)
        im[..., :3] = (75, 75, 49)
        im[..., 3] = a
        Image.fromarray(im, "RGBA").save(name, optimize=True)
    save((684, 238, 850, 398), "assets/logo-mark.png")
    save((736, 558, 800, 596), "assets/logo-leaf.png")


def main():
    rgb = np.asarray(Image.open("assets/village.webp").convert("RGB")).astype(float)
    paper = np.median(rgb[4:40, 4:40].reshape(-1, 3), axis=0)
    colour, alpha = paper_to_alpha(rgb, paper)
    rgba(colour, alpha).save("assets/village-day.webp", quality=90, alpha_quality=100, method=6)
    rgba(night(colour), alpha).save("assets/village-night.webp", quality=90, alpha_quality=100, method=6)
    lit_windows(rgb).save("assets/lights-windows.png", optimize=True)
    lamp_layers()
    logo_layers()
    n = night(paper[None, None, :])[0, 0]
    print("paper (day sky):", paper, " night sky:", n.round())


if __name__ == "__main__":
    main()
