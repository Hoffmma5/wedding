"""Favicons from the logo orange (run from the project root).

  python tools/make_favicon.py

The orange from the logo in terracotta (#B66238, the title colour), as big
as the icon allows, on a transparent background:
  favicon.svg           modern browsers; a lighter terracotta on dark tabs
  favicon.ico           16 / 32 / 48 px, older browsers
  assets/icon-192.png   Android home screen (transparent)
  apple-touch-icon.png  iPhone home screen - iOS needs a solid square, so
                        the orange sits large on the paper colour
"""
import base64
import io

from PIL import Image

INK = (182, 98, 56)          # #B66238
DARK_TAB = "#b66238"         # the same terracotta on dark tabs too
PAPER = (252, 250, 250)

mark = Image.open("assets/logo-mark.png").convert("RGBA")
mark = mark.crop(mark.getbbox())                   # no empty margin: as big as possible
tinted = Image.new("RGBA", mark.size, INK + (255,))
tinted.putalpha(mark.split()[3])
mark = tinted                                      # the logo shape, in terracotta


def icon(size, margin=0.02, background=None):
    big = size * 4                                   # draw large, shrink once: smooth edges
    im = Image.new("RGBA", (big, big), background + (255,) if background else (0, 0, 0, 0))
    room = big * (1 - 2 * margin)
    scale = room / max(mark.width, mark.height)
    w, h = round(mark.width * scale), round(mark.height * scale)
    m = mark.resize((w, h), Image.LANCZOS)
    im.alpha_composite(m, ((big - w) // 2, (big - h) // 2))
    return im.resize((size, size), Image.LANCZOS)


icon(48).save("favicon.ico", sizes=[(16, 16), (32, 32), (48, 48)])
icon(192).save("assets/icon-192.png", optimize=True)
icon(180, margin=0.12, background=PAPER).convert("RGB").save("apple-touch-icon.png", optimize=True)

# SVG: the mark as an alpha mask over a rectangle in the ink colour, so CSS
# can swap the colour for dark browser themes
buf = io.BytesIO()
mark.resize((128, round(128 * mark.height / mark.width)), Image.LANCZOS).save(buf, "PNG", optimize=True)
data = base64.b64encode(buf.getvalue()).decode()
w, h = 128, round(128 * mark.height / mark.width)
pad = (w - h) / 2
svg = f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 {-pad:g} {w} {w}">
<style>rect{{fill:#b66238}}@media (prefers-color-scheme:dark){{rect{{fill:{DARK_TAB}}}}}</style>
<mask id="m" style="mask-type:alpha" maskUnits="userSpaceOnUse" x="0" y="0" width="{w}" height="{h}"><image width="{w}" height="{h}" href="data:image/png;base64,{data}"/></mask>
<rect width="{w}" height="{h}" mask="url(#m)"/>
</svg>
'''
open("favicon.svg", "w", encoding="utf-8", newline="\n").write(svg)
print("favicon.svg, favicon.ico, assets/icon-192.png, apple-touch-icon.png written")
