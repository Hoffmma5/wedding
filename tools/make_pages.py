"""Generate the inner pages from one template (run from the project root).

  python tools/make_pages.py

Only re-run this before you have edited the pages by hand: it overwrites them.
"""

NAV = [
    ("program", "Program"),
    ("accommodation", "Stay"),
    ("travel", "Travel"),
    ("weather", "Weather"),
    ("location", "Location"),
    ("map", "Guests"),
]

CONTENT = {
    "accommodation": ("Accommodation", "Where to stay, close to the celebrations.", """
    <h2>Where we recommend staying</h2>
    <p class="placeholder">Hotels, guesthouses and holiday rentals near the venue &mdash; coming soon.</p>
    <h2>Getting to the venue</h2>
    <p class="placeholder">Shuttles, taxis and parking &mdash; coming soon.</p>"""),
    "program": ("Program", "Three days in the Algarve, 1 &ndash; 3 October 2027.", """
    <h2>Friday, 1 October</h2>
    <p class="placeholder">Welcome evening &mdash; details coming soon.</p>
    <h2>Saturday, 2 October</h2>
    <p class="placeholder">Ceremony, dinner and dancing &mdash; times coming soon.</p>
    <h2>Sunday, 3 October</h2>
    <p class="placeholder">Farewell &mdash; details coming soon.</p>"""),
    "travel": ("Travel", "Finding your way to the Algarve.", """
    <h2>Flying in</h2>
    <p>The Algarve&rsquo;s airport is <strong>Faro (FAO)</strong>. Lisbon is a good alternative, about a 2.5&ndash;3 hour drive away.</p>
    <p class="placeholder">Our tips on flights and connections &mdash; coming soon.</p>
    <h2>Getting around</h2>
    <p class="placeholder">Car hire, trains, buses and transfers &mdash; coming soon.</p>"""),
    "weather": ("Weather &amp; packing", "Early October in the Algarve is usually warm, sunny and calm.", """
    <h2>What to expect</h2>
    <div class="stats">
      <div class="stat"><b>~24&nbsp;&deg;C</b><span>Daytime</span></div>
      <div class="stat"><b>~16&nbsp;&deg;C</b><span>Evenings</span></div>
      <div class="stat"><b>~20&nbsp;&deg;C</b><span>Sea</span></div>
      <div class="stat"><b>Mostly dry</b><span>The odd shower</span></div>
    </div>
    <p class="note">Typical values for early October. We&rsquo;ll share the forecast closer to the date.</p>
    <h2>What to pack</h2>
    <ul>
      <li>Sunscreen, sunglasses and a hat</li>
      <li>A light jacket or knit for the evenings</li>
      <li>Comfortable shoes &mdash; Portuguese cobbles and heels don&rsquo;t mix</li>
      <li>Swimwear &mdash; the sea is still warm enough</li>
    </ul>
    <h2>Dress code</h2>
    <p class="placeholder">Coming soon.</p>"""),
    "rsvp": ("RSVP", "Let us know if you can join us on 1 &ndash; 3 October 2027.", """
    <p class="placeholder">The RSVP form will appear here soon.</p>"""),
    "location": ("Location", "Where it all happens, in the Algarve.", """
    <h2>The venue</h2>
    <p class="placeholder">Venue name, address and a map &mdash; coming soon.</p>
    <h2>Around the area</h2>
    <p class="placeholder">Beaches, towns and places we love nearby &mdash; coming soon.</p>"""),
}

HEAD = """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title} · Marek &amp; Paulo</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500;600&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="css/style.css">
  <script>
    (function () {{
      var saved = null;
      try {{ saved = localStorage.getItem('theme'); }} catch (e) {{}}
      var night = saved ? saved === 'night'
        : window.matchMedia && matchMedia('(prefers-color-scheme: dark)').matches;
      document.documentElement.dataset.theme = night ? 'night' : 'day';
    }})();
  </script>
</head>
<body{body_class}>
  <header class="nav">
    <a class="brand" href="index.html"><span class="mark" aria-hidden="true"></span>Marek &amp; Paulo</a>
    <nav class="nav-links" id="nav-links" aria-label="Pages">
{nav}
      <a class="nav-cta" href="rsvp.html">RSVP</a>
    </nav>
    <button class="icon-btn theme-toggle" type="button" aria-pressed="false" aria-label="Switch to night">
      <svg class="i-moon" viewBox="0 0 24 24" aria-hidden="true"><path d="M20 14.5A8 8 0 0 1 9.5 4a8 8 0 1 0 10.5 10.5Z"/></svg>
      <svg class="i-sun" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2.5v2M12 19.5v2M2.5 12h2M19.5 12h2M5.3 5.3l1.4 1.4M17.3 17.3l1.4 1.4M5.3 18.7l1.4-1.4M17.3 6.7l1.4-1.4"/></svg>
    </button>
    <button class="icon-btn menu-toggle" type="button" aria-expanded="false" aria-controls="nav-links" aria-label="Menu">
      <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 8h16M4 16h16"/></svg>
    </button>
  </header>
"""

FOOT = """  <script src="js/site.js"></script>
</body>
</html>
"""


def nav():
    return "\n".join(f'      <a href="{slug}.html">{label}</a>' for slug, label in NAV)


def main():
    for slug, (h1, lead, body) in CONTENT.items():
        html = HEAD.format(title=h1, body_class="", nav=nav())
        html += f"""  <main class="page">
    <p class="eyebrow">Marek &amp; Paulo &middot; 1 &ndash; 3 October 2027</p>
    <h1>{h1}</h1>
    <p class="lead">{lead}</p>{body}
  </main>
""" + FOOT
        open(f"{slug}.html", "w", encoding="utf-8").write(html)

    html = HEAD.format(title="Guest map", body_class=' class="map-page"', nav=nav())
    html += """  <main>
    <div class="map-head">
      <p class="eyebrow">Guest map</p>
      <h1>Where our guests come from</h1>
      <p>Everyone travelling to the Algarve to celebrate with us.</p>
    </div>
    <div class="map-embed">
      <iframe src="https://hoffmma5.github.io/wedding-map/" title="Map of where our wedding guests come from" loading="lazy" allow="fullscreen"></iframe>
    </div>
  </main>
""" + FOOT
    open("map.html", "w", encoding="utf-8").write(html)
    print("pages written")


if __name__ == "__main__":
    main()
