"""Favicons from the logo orange (run from the project root).

  python tools/make_favicon.py

The olive orange (assets/logo-mark.png) on a small cream disc, so it reads on
light and dark browser tabs alike:
  favicon.ico           16 / 32 / 48 px, browser tabs
  assets/icon-192.png   Android home screen
  apple-touch-icon.png  iPhone home screen (180 px, full square of paper)
"""
from PIL import Image, ImageDraw

PAPER = (246, 241, 228, 255)
mark = Image.open("assets/logo-mark.png").convert("RGBA")


def icon(size, disc=True, scale=.68):
    big = size * 4                                   # draw large, shrink once: smooth edges
    im = Image.new("RGBA", (big, big), (0, 0, 0, 0))
    if disc:
        ImageDraw.Draw(im).ellipse((0, 0, big - 1, big - 1), fill=PAPER)
    else:
        im.paste(PAPER, (0, 0, big, big))
    w = int(big * scale)
    h = int(w * mark.height / mark.width)
    m = mark.resize((w, h), Image.LANCZOS)
    im.alpha_composite(m, ((big - w) // 2, (big - h) // 2 + big // 40))
    return im.resize((size, size), Image.LANCZOS)


icon(48).save("favicon.ico", sizes=[(16, 16), (32, 32), (48, 48)])
icon(192).save("assets/icon-192.png", optimize=True)
icon(180, disc=False, scale=.62).convert("RGB").save("apple-touch-icon.png", optimize=True)
print("favicon.ico, assets/icon-192.png, apple-touch-icon.png written")
