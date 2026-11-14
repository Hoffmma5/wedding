"""Favicons from the logo orange (run from the project root).

  python tools/make_favicon.py

The orange from the logo, as big as the icon allows, on a transparent
background:
  favicon.svg           modern browsers: the olive orange, and in dark mode
                        (dark tabs) the same orange in cream, so it never
                        disappears
  favicon.ico           16 / 32 / 48 px, older browsers (olive)
  assets/icon-192.png   Android home screen (olive, transparent)
  apple-touch-icon.png  iPhone home screen - iOS needs a solid square, so
                        the orange sits large on the paper colour
"""
import base64
import io

from PIL import Image

OLIVE = (75, 75, 49)
CREAM = "#ece4c6"            # the logo ink at night (--olive in night mode)
PAPER = (252, 250, 250)

mark = Image.open("assets/logo-mark.png").convert("RGBA")
mark = mark.crop(mark.getbbox())                   # no empty margin: as big as possible


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
<style>rect{{fill:#4b4b31}}@media (prefers-color-scheme:dark){{rect{{fill:{CREAM}}}}}</style>
<mask id="m" style="mask-type:alpha" maskUnits="userSpaceOnUse" x="0" y="0" width="{w}" height="{h}"><image width="{w}" height="{h}" href="data:image/png;base64,{data}"/></mask>
<rect width="{w}" height="{h}" mask="url(#m)"/>
</svg>
'''
open("favicon.svg", "w", encoding="utf-8", newline="\n").write(svg)
print("favicon.svg, favicon.ico, assets/icon-192.png, apple-touch-icon.png written")
