"""Render the link-preview card (tools/og-card.html) to assets/og-image.jpg.

  python tools/make_og.py

Needs Google Chrome and Pillow, and the site served on localhost:5001
(python -m http.server 5001) so the card can load its fonts and images.
"""
import os
import subprocess
import tempfile

from PIL import Image

CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
URL = "http://localhost:5001/tools/og-card.html"

tmp = tempfile.mkdtemp()
png = os.path.join(tmp, "og.png")
subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
                "--user-data-dir=" + os.path.join(tmp, "profile"),
                "--force-device-scale-factor=1", "--virtual-time-budget=6000",
                "--window-size=1200,630", "--screenshot=" + png, URL],
               check=True, capture_output=True, timeout=90)
Image.open(png).convert("RGB").crop((0, 0, 1200, 630)).save("assets/og-image.jpg", quality=86, optimize=True, progressive=True)
print("assets/og-image.jpg", os.path.getsize("assets/og-image.jpg") // 1024, "KB")
