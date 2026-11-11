"""Generate the inner pages from one template (run from the project root).

  python tools/make_pages.py

Content comes from the Tavira invitation. Edit the text here and re-run,
or edit the generated .html files by hand (then stop using this script).
"""

NAV = [
    ("program", "Program"),
    ("accommodation", "Stay"),
    ("travel", "Travel"),
    ("weather", "Weather"),
    ("location", "Location"),
    ("map", "Guests"),
]

# Invitation colours, one per topic
BLUE, RUST, BROWN, OLIVE, WINE, CORAL = "#1f4fa0", "#b5432a", "#8b5523", "#7b8152", "#7a3b3b", "#d4504c"

VENUE = """Hotel Rural Quinta do Marco</strong><span>Sítio do Marco, 632A<br>
          Santa Catarina da Fonte do Bispo 8800-164<br>Tavira &ndash; Algarve, Portugal</span>"""

PAGES = {}

PAGES["travel"] = ("Travel", BLUE, f"""
    <header class="inv-head">
      <p class="sc">Let us help you plan your</p>
      <h1 class="script">Travel</h1>
    </header>
    <div class="inv-grid map-grid">
      <div class="prose">
        <dl class="facts-list">
          <div><dt class="sc">Dates</dt><dd><strong>1st, 2nd &amp; 3rd of October 2027</strong><span>Friday to Sunday</span></dd></div>
          <div><dt class="sc">Wedding venue</dt><dd><strong>{VENUE}</dd></div>
          <div><dt class="sc">Closest airport</dt><dd><strong>FAO &ndash; Faro</strong><span>30 min by car</span></dd></div>
        </dl>
        <p>If you&rsquo;re traveling from Czech Republic we recommend to fly out from two airports: <strong>Prague</strong> or <strong>Nuremberg</strong>.</p>
        <p class="ps">P.S. The flights are often cheaper from Germany.</p>
      </div>
      <figure class="art map-art">
        <img src="assets/art/iberia.webp" alt="Watercolour map of Portugal and Spain with Tavira marked" width="613" height="802">
        <span class="place" aria-hidden="true">Tavira</span>
        <img class="pearl" src="assets/art/pearl.webp" alt="" width="360" height="268">
      </figure>
    </div>

    <section class="inv-section" style="--topic:{BROWN}">
      <div class="inv-grid">
        <div>
          <header class="inv-head">
            <p class="sc">From the airport to Tavira&hellip;</p>
            <h2 class="script">transfer</h2>
          </header>
          <div class="prose">
            <p>If you arrive on the 1st of October, <strong>we will take care of your transfer</strong>. The same applies if you fly back on Sunday, the 3rd &ndash; <strong>we will take you back to the airport</strong>.</p>
            <p>However, if you arrive earlier or leave later than the mentioned dates, we ask that you plan your transfer. The best option would be renting/sharing a car or taking a taxi.</p>
          </div>
        </div>
        <figure class="art"><img src="assets/art/shrimp.webp" alt="" width="640" height="479"></figure>
      </div>
    </section>""")

PAGES["weather"] = ("Weather &amp; what to pack", RUST, """
    <div class="inv-grid">
      <div>
        <header class="inv-head">
          <h1 class="script">the Weather</h1>
          <p class="sc">A forecast for the festivities</p>
        </header>
        <div class="prose">
          <p>October in the Algarve usually brings warm, sunny afternoons and cooler evenings. The weather can be a little unpredictable, though, so pack your sunglasses, but bring an umbrella too &ndash; just in case the skies have other plans!</p>
        </div>
      </div>
      <figure class="art"><img src="assets/art/sun.webp" alt="" width="520" height="520"></figure>
    </div>
    <div class="wx">
      <div><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2.5v2M12 19.5v2M2.5 12h2M19.5 12h2M5.3 5.3l1.4 1.4M17.3 17.3l1.4 1.4M5.3 18.7l1.4-1.4M17.3 6.7l1.4-1.4"/></svg><b>25&nbsp;&deg;C</b><span>Average daytime high</span></div>
      <div><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M19 14.5A7.5 7.5 0 0 1 9.5 5a7.5 7.5 0 1 0 9.5 9.5Z"/></svg><b>16&nbsp;&deg;C</b><span>Average nighttime low</span></div>
      <div><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M7 15a4 4 0 0 1-.6-8A5.5 5.5 0 0 1 17 8a3.5 3.5 0 0 1 .5 7H7Z"/><path d="M9 18l-1 2.5M13 18l-1 2.5M17 18l-1 2.5"/></svg><b>6 days</b><span>With measurable rain per month</span></div>
    </div>
    <p class="wx-link"><a href="https://www.yr.no/en/forecast/daily-table/2-2262744/Portugal/Faro/Tavira" target="_blank" rel="noopener">Current weather in Tavira on yr.no &nearr;</a></p>

    <section class="inv-section">
      <div class="inv-grid">
        <div>
          <header class="inv-head"><h2 class="script">What to Pack</h2></header>
          <div class="prose">
            <ul>
              <li>Wedding clothes</li>
              <li>Swimwear &amp; flip-flops</li>
              <li>A jacket for the evening</li>
              <li>1 umbrella</li>
            </ul>
          </div>
        </div>
        <figure class="art"><img class="crabs" src="assets/art/crabs.webp" alt="Two crabs" tabindex="0" role="button" width="560" height="585" style="max-width:260px;margin-left:auto"></figure>
      </div>
    </section>""")

PAGES["accommodation"] = ("The hotel", OLIVE, """
    <header class="inv-head">
      <h1 class="script">the Hotel</h1>
      <p class="sc">Your home for the weekend</p>
    </header>
    <figure class="wide-art"><img src="assets/art/hotel-landscape.webp" alt="Watercolour of the countryside near Tavira, with the sea behind" width="1059" height="437"></figure>
    <div class="prose">
      <p>Our hotel is <strong>Hotel Quinta do Marco</strong> &ndash; located in the countryside of the village, it offers a heated outdoor pool, gym, a little farm with animals and great views. <strong>We will provide accommodation to everyone for the 2 nights and the main meals during the 3 days.</strong></p>
      <dl class="times">
        <dt class="sc">Check in</dt><dd>Friday, 01.10.2027, 14:00</dd>
        <dt class="sc">Check out</dt><dd>Sunday, 03.10.2027, 12:00</dd>
      </dl>
      <p class="contact">
        <a href="mailto:reservas@hotelquintadomarco.com">reservas@hotelquintadomarco.com</a>
        <a href="tel:+351281971500">+351 281 971 500</a>
        <a href="https://www.hotelquintadomarco.com/en/" target="_blank" rel="noopener">hotelquintadomarco.com &nearr;</a>
      </p>
    </div>

    <section class="inv-section" style="--topic:#7a3b3b">
      <div class="inv-grid">
        <div>
          <header class="inv-head">
            <h2 class="script">the Bedrooms</h2>
            <p class="sc">Where will we sleep?</p>
          </header>
          <div class="prose">
            <p>Everyone stays with us at Hotel Quinta do Marco for both nights. We&rsquo;ll let each of you know personally which room is yours.</p>
          </div>
        </div>
        <figure class="art"><img src="assets/art/shell.webp" alt="" width="459" height="771" style="max-width:180px;margin:0 auto"></figure>
      </div>
    </section>""")

PAGES["location"] = ("Location", BLUE, f"""
    <div class="inv-grid">
      <div>
        <header class="inv-head">
          <p class="sc">Where it all happens</p>
          <h1 class="script">Tavira</h1>
        </header>
        <div class="prose">
          <p>Tavira is a little town where life moves at its own pace. Think whitewashed houses, terracotta rooftops, cobbled streets, and a river running through the town. Just beyond, you&rsquo;ll find salt flats, endless sandy beaches, and the Atlantic Ocean.</p>
          <dl class="facts-list">
            <div><dt class="sc">Wedding venue</dt><dd><strong>{VENUE}</dd></div>
          </dl>
        </div>
      </div>
      <figure class="art tile-art">
        <img class="tile" src="assets/art/tile.webp" alt="" width="640" height="644">
        <img class="sardine" src="assets/art/sardine.webp" alt="Sardine" title="Psst, give it a tap" tabindex="0" role="button" width="900" height="319">
      </figure>
    </div>
    <div class="map-frame">
      <iframe src="https://maps.google.com/maps?q=Hotel%20Rural%20Quinta%20do%20Marco%2C%20Tavira&amp;z=11&amp;output=embed" title="Map: Hotel Rural Quinta do Marco, Tavira" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
    </div>
    <p class="contact" style="margin-top:12px"><a href="https://maps.google.com/?q=Hotel%20Rural%20Quinta%20do%20Marco%2C%20Tavira" target="_blank" rel="noopener">Open in Google Maps &nearr;</a></p>

    <section class="inv-section" style="--topic:{BROWN}">
      <header class="inv-head">
        <h2 class="script">the Algarve</h2>
        <p class="sc">The south of Portugal&hellip;</p>
      </header>
      <div class="prose">
        <p>We come back to the Algarve every summer. Our routines include beach, pool and long dinners with a full house. The house door stays open to let the wind through and we don&rsquo;t leave the table for at least 3 hours.</p>
      </div>
    </section>""")

PAGES["program"] = ("Program", WINE, f"""
    <header class="inv-head">
      <p class="sc">Three days in Tavira</p>
      <h1 class="script">the Program</h1>
    </header>

    <article class="day" style="--topic:{CORAL}">
      <div class="prose">
        <h2 class="script">friday</h2>
        <p class="sc">Welcome party &middot; 01.10.2027</p>
        <ul>
          <li>Transfer from Faro airport</li>
          <li>Check in at Hotel Quinta do Marco from 14:00</li>
        </ul>
        <p class="placeholder">Time and details of the welcome party &mdash; coming soon.</p>
      </div>
      <img class="day-art disco" src="assets/art/disco-ball.webp" alt="Disco ball" title="Give it a spin" tabindex="0" role="button" width="337" height="436" style="max-width:170px">
    </article>

    <article class="day full" style="--topic:{OLIVE}">
      <div class="prose">
        <h2 class="script">the Wedding Day</h2>
        <p class="sc">Saturday &middot; 02.10.2027</p>
        <p class="placeholder">The plan for the day &mdash; coming soon.</p>
      </div>
      <img src="assets/art/long-table.webp" alt="Watercolour of guests at a long dinner table" width="1061" height="194" style="width:100%;height:auto">
    </article>

    <article class="day" style="--topic:{BROWN}">
      <div class="prose">
        <h2 class="script">sunday</h2>
        <p class="sc">Farewell &middot; 03.10.2027</p>
        <ul>
          <li>Check out by 12:00</li>
          <li>Transfer back to Faro airport</li>
        </ul>
      </div>
      <img class="day-art" src="assets/art/oysters.webp" alt="" width="520" height="522" style="max-width:200px">
    </article>""")

PAGES["rsvp"] = ("RSVP", OLIVE, """
    <header class="inv-head">
      <p class="sc">Let us know if you can join us</p>
      <h1 class="script">RSVP</h1>
    </header>
    <div class="prose">
      <p>We&rsquo;d love to celebrate with you in Tavira on <strong>1st, 2nd &amp; 3rd of October 2027</strong>.</p>
      <p class="placeholder">The RSVP form will appear here soon.</p>
    </div>""")

HEAD = """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title} · Marek &amp; Paulo</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Beth+Ellen&family=Cormorant+Garamond:wght@500;600&family=Cormorant+SC:wght@700&family=Inter:wght@300;400;500;600&family=Lora:ital,wght@0,400;0,600;1,400&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="css/style.css?v=9">
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

FOOT = """  <script src="js/site.js?v=9"></script>
  <script src="js/eggs.js?v=9"></script>
</body>
</html>
"""


def nav():
    return "\n".join(f'      <a href="{slug}.html">{label}</a>' for slug, label in NAV)


def main():
    for slug, (title, topic, body) in PAGES.items():
        html = HEAD.format(title=title, body_class="", nav=nav())
        html += f'  <main class="page inv" style="--topic:{topic}">{body}\n  </main>\n' + FOOT
        open(f"{slug}.html", "w", encoding="utf-8").write(html)

    html = HEAD.format(title="Guest map", body_class=' class="map-page"', nav=nav())
    html += f"""  <main>
    <div class="map-head inv" style="--topic:{BLUE}">
      <p class="sc">Everyone&rsquo;s coming to the Algarve</p>
      <h1 class="script">the guests</h1>
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
