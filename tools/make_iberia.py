"""Paint Spain as a soft watercolour wash behind the invitation's Portugal map.

  in:  assets/art/portugal.webp   (Portugal only, from the invitation)
  out: assets/art/iberia.webp     (Portugal + a faint Spain, transparent background)

Run from the project root:  python tools/make_iberia.py
"""
import numpy as np
from PIL import Image, ImageFilter

rng = np.random.default_rng(3)

pt = Image.open("assets/art/portugal.webp").convert("RGBA")
pw, ph = pt.size                    # 373 x 722
TOP, RIGHT, BOTTOM = 34, 240, 46    # extra canvas around Portugal
W, H = pw + RIGHT, ph + TOP + BOTTOM
SAND = np.array([226, 214, 192])

alpha_pt = np.asarray(pt)[..., 3]

# Spain's south coast east of the Guadiana mouth (Portugal pixel coords):
# Guadiana mouth -> Huelva (a little north) -> Guadalquivir / Doñana -> towards Cádiz
COAST = [(200, 692), (230, 684), (266, 678), (292, 690), (318, 716), (336, 744), (350, 790)]


def coast_y(x):
    xs, ys = zip(*COAST)
    if x <= xs[0]:
        return ys[0]
    if x >= xs[-1]:
        return 10_000                # beyond the last point the coast has turned south: all land
    return float(np.interp(x, xs, ys))


def low_noise(w, h, cell, amp):
    small = rng.normal(0, 1, (h // cell + 2, w // cell + 2)).astype(np.float32)
    return np.asarray(Image.fromarray(small).resize((w, h), Image.BICUBIC)) * amp


mask = np.zeros((H, W), np.float32)
for y in range(H):
    py = y - TOP
    if py < 56:
        x0 = 92 + 9 * np.sin(y / 7.0) + 5 * np.sin(y / 3.1)   # Galicia's rías, north of the Minho
    elif py < ph:
        xs = np.where(alpha_pt[py] > 60)[0]
        x0 = (xs.max() - 10) if len(xs) else 200   # tuck under Portugal's eastern border
    else:
        x0 = 200
    for x in range(int(x0), W):
        if py >= 0 and py > coast_y(x):
            continue                               # sea (Gulf of Cádiz)
        mask[y, x] = 1.0

# Ragged, soft fade towards the east and the north so there is no hard box
xx = np.arange(W)[None, :]
yy = np.arange(H)[:, None]
edge_n = low_noise(W, H, 46, 16)
fade_e = np.clip((W - 10 - xx + edge_n) / 150, 0, 1) ** 1.3
fade_n = np.clip((yy + 2 + edge_n * .6) / 46, 0, 1)
soft = np.asarray(Image.fromarray((mask * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(3))).astype(np.float32) / 255
# painted, slightly irregular shoreline instead of a clean cut
soft = np.clip((soft - .5) / .35 + .5 + low_noise(W, H, 9, .35), 0, 1)
mask = soft * fade_e * fade_n

# Watercolour: blotchy wash, a little pigment pooling at the coast, paper grain
wash = 1 + low_noise(W, H, 110, .025) + low_noise(W, H, 26, .012)
edge = np.asarray(Image.fromarray((mask * 255).astype(np.uint8)).filter(ImageFilter.FIND_EDGES)).astype(np.float32) / 255
col = SAND[None, None, :] * wash[..., None] * (1 - .08 * edge[..., None])
col *= (1 + rng.normal(0, .015, (H, W)))[..., None]
alpha = np.clip(mask * (.7 + low_noise(W, H, 120, .04)), 0, 1)

spain = Image.fromarray(np.dstack([np.clip(col, 0, 255), alpha * 255]).astype(np.uint8), "RGBA")
spain.alpha_composite(pt, (0, TOP))
spain.save("assets/art/iberia.webp", quality=85, alpha_quality=90, method=6)
print("iberia", spain.size, "portugal offset", (0, TOP))
