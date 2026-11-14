"""Small copies of the village painting for the footer of every page.

  in:  assets/village-day.webp, assets/village-night.webp, assets/lights-windows.png
  out: assets/village-mini-day.webp, assets/village-mini-night.webp (windows lit)

640 px wide (the footer shows it at up to 320 px, so it stays sharp on phones).
Run from the project root after tools/make_layers.py:  python tools/village_mini.py
"""
from PIL import Image

W = 640


def small(im):
    return im.resize((W, round(im.height * W / im.width)), Image.LANCZOS)


day = Image.open("assets/village-day.webp").convert("RGBA")
night = Image.open("assets/village-night.webp").convert("RGBA")
night.alpha_composite(Image.open("assets/lights-windows.png").convert("RGBA"))

small(day).save("assets/village-mini-day.webp", quality=88, alpha_quality=95, method=6)
small(night).save("assets/village-mini-night.webp", quality=88, alpha_quality=95, method=6)
print("village-mini", small(day).size)
