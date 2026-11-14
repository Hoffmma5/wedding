"""Render the link-preview picture (run from the project root).

  python tools/make_og.py

Opens tools/og-card.html in headless Chrome (or Edge) at 1200 x 630 and
saves assets/og-image.jpg, the picture WhatsApp, Messenger, email and
social sites show when the site is shared. Needs Pillow and an internet
connection (the fonts come from Google Fonts).
"""
import os
import pathlib
import subprocess
import tempfile

from PIL import Image

BROWSERS = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "google-chrome",
    "chromium",
]

root = pathlib.Path(__file__).resolve().parent.parent
card = (root / "tools" / "og-card.html").as_uri()
browser = next(b for b in BROWSERS if os.path.exists(b) or "/" not in b and "\\" not in b)

with tempfile.TemporaryDirectory() as tmp:
    png = pathlib.Path(tmp) / "og.png"
    subprocess.run([browser, "--headless=new", "--disable-gpu", "--hide-scrollbars",
                    "--allow-file-access-from-files", "--force-device-scale-factor=1",
                    "--window-size=1200,630", "--virtual-time-budget=8000",
                    f"--screenshot={png}", card], check=True, capture_output=True)
    Image.open(png).convert("RGB").crop((0, 0, 1200, 630)).save(
        root / "assets" / "og-image.jpg", quality=86, optimize=True, progressive=True)
print("assets/og-image.jpg written")
