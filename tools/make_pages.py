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
    ("location", "Algarve"),
    ("map", "Guests"),
]

# Invitation colours, one per topic
BLUE, RUST, BROWN, OLIVE, WINE, CORAL = "#1f4fa0", "#b5432a", "#8b5523", "#7b8152", "#7a3b3b", "#d4504c"

VENUE = """Hotel Rural Quinta do Marco</strong><span>Sítio do Marco, 632A<br>
          Santa Catarina da Fonte do Bispo 8800-164<br>Tavira &ndash; Algarve, Portugal</span>"""

import icons   # tools/icons.py

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
        <img src="assets/art/iberia-map.webp" alt="Map of Portugal and western Spain: Tavira is on the Algarve coast, just east of Faro airport" width="723" height="922">
        <svg class="map-labels" viewBox="0 0 723 922" aria-hidden="true">
          <path class="route" d="M712 24C650 320 430 560 268 784"/>
          <path class="plane" transform="translate(466 520) rotate(216) scale(2.2) translate(-12 -12)" d="M21 16v-2l-8-5V3.5c0-.83-.67-1.5-1.5-1.5S10 2.67 10 3.5V9l-8 5v2l8-2.5V19l-2 1.5V22l3.5-1 3.5 1v-1.5L13 19v-5.5l8 2.5z"/>
          <text class="country" transform="translate(316 470) rotate(-84)">Portugal</text>
          <text class="country es" x="598" y="420">España</text>
          <text class="sea" transform="translate(66 500) rotate(-84)">Oceano Atlântico</text>
          <circle class="town" cx="265" cy="788" r="5"/>
          <text class="town-name" x="252" y="830">Faro</text>
          <image href="assets/art/pearl.webp" x="276" y="750" width="68" height="51"/>
          <text class="tavira" x="300" y="868">Tavira</text>
        </svg>
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
    </section>

    <section class="inv-section">
      <header class="inv-head">
        <p class="sc">A few little things</p>
        <h2 class="script">good to know</h2>
      </header>
      <ul class="highlights">
        <li><b>Set your watch</b>Portugal runs one hour behind Prague &ndash; a free extra hour of sleep on your first morning.</li>
        <li><b>Bring a few euros</b>Cards work almost everywhere, but a couple of coins come in handy for a coffee and a <em>pastel de nata</em>.</li>
        <li><b>Stay connected</b>Your phone works just like at home &ndash; no roaming fees in the EU, so send us all the sunset photos.</li>
        <li><b>Pack your ID</b>From the EU? Your ID card is all you need. Coming from further away &ndash; don&rsquo;t forget your passport.</li>
        <li><b>Say <em>obrigado</em></b>Most people here speak English, but a smiling <em>obrigado</em> (or <em>obrigada</em>) always wins hearts.</li>
        <li><b>Order a beer like a local</b>A beer here is <em>um imperial</em> &ndash; just 0.2&nbsp;l, so it&rsquo;s always ice cold. Used to a proper half-litre? Ask for <em>uma caneca</em>.</li>
        <li><b>If you&rsquo;re driving</b>Unlike Czechia, Portugal allows a little alcohol behind the wheel (0.5&nbsp;&permil;) &ndash; but that&rsquo;s only an <em>imperial</em> or two. Better still: pick a driver and let them be the hero.</li>
        <li><b>Just in case</b>112 is the emergency number, same as at home. We hope you&rsquo;ll never need it!</li>
      </ul>
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

FACILITIES_HTML = "\n".join(f'        <li>{icons.svg(paths)}{name}</li>' for name, paths in icons.FACILITIES)

PAGES["accommodation"] = ("The hotel", OLIVE, f"""
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
    </div>

    <div class="carousel" aria-label="Photos of Hotel Quinta do Marco">
      <figure class="slide"><img src="assets/gallery/hotel/01.webp" alt="The quinta from above, with the hills and orchards around it" width="1200" height="800"><figcaption>The quinta from above</figcaption></figure>
      <figure class="slide"><img src="assets/gallery/hotel/02.webp" alt="The main building and the pool lawn with sun loungers" width="1200" height="800" loading="lazy"><figcaption>Pool &amp; main house</figcaption></figure>
      <figure class="slide"><img src="assets/gallery/hotel/03.webp" alt="The salt-water pool at golden hour" width="1200" height="800" loading="lazy"><figcaption>The salt-water pool</figcaption></figure>
      <figure class="slide"><img src="assets/gallery/hotel/04.webp" alt="A shaded terrace with a hanging chair and views over the hills" width="1200" height="800" loading="lazy"><figcaption>Terrace with a view</figcaption></figure>
      <figure class="slide"><img src="assets/gallery/hotel/05.webp" alt="Inside the Farroba restaurant, with tables by the windows" width="1200" height="800" loading="lazy"><figcaption>Farroba restaurant</figcaption></figure>
      <figure class="slide"><img src="assets/gallery/hotel/06.webp" alt="The Quinta do Marco swing overlooking the valley" width="1200" height="800" loading="lazy"><figcaption>The swing with a view</figcaption></figure>
      <figure class="slide"><img src="assets/gallery/hotel/07.webp" alt="Three goats looking over the farm fence" width="1200" height="800" loading="lazy"><figcaption>The animal farm</figcaption></figure>
      <figure class="slide"><img src="assets/gallery/hotel/08.webp" alt="The children's playground with a slide and swings" width="1200" height="800" loading="lazy"><figcaption>Playground</figcaption></figure>
      <figure class="slide"><img src="assets/gallery/hotel/09.webp" alt="The hotel nestled in the green Algarve hills" width="1200" height="800" loading="lazy"><figcaption>In the Algarve hills</figcaption></figure>
    </div>

    <section class="inv-section">
      <header class="inv-head">
        <p class="sc">Something for everyone</p>
        <h2 class="script">at the Quinta</h2>
      </header>
      <ul class="facilities">
{FACILITIES_HTML}
      </ul>
      <p class="contact"><a href="https://www.hotelquintadomarco.com/en/" target="_blank" rel="noopener">More about the hotel on its website &nearr;</a></p>
    </section>

    <section class="inv-section" style="--topic:#7a3b3b">
      <header class="inv-head">
        <h2 class="script">the Bedrooms</h2>
        <p class="sc">Where will we sleep?</p>
      </header>
      <div class="prose">
        <p>Everyone stays with us at Hotel Quinta do Marco for both nights. We&rsquo;ll let each of you know personally which room is yours.</p>
        <p>The rooms are bright and comfortable, and each one has its own balcony or terrace looking out over the hills &ndash; perfect for a slow morning coffee after a long night.</p>
      </div>
    <div class="carousel" aria-label="Photos of the bedrooms">
      <figure class="slide"><img src="assets/gallery/rooms/01.webp" alt="Double room with a terracotta-red bedspread and a view to the hills" width="1200" height="800"><figcaption>Double room</figcaption></figure>
      <figure class="slide"><img src="assets/gallery/rooms/02.webp" alt="Bright double room with a desk and sunflowers" width="1200" height="800" loading="lazy"><figcaption>Double room</figcaption></figure>
      <figure class="slide"><img src="assets/gallery/rooms/03.webp" alt="Superior room with a wooden screen and two extra beds" width="1200" height="800" loading="lazy"><figcaption>Superior room</figcaption></figure>
      <figure class="slide"><img src="assets/gallery/rooms/04.webp" alt="Family room with a double bed, two singles and a sofa" width="1200" height="800" loading="lazy"><figcaption>Family room</figcaption></figure>
      <figure class="slide"><img src="assets/gallery/rooms/05.webp" alt="Balcony with two chairs looking out over the hills" width="1200" height="800" loading="lazy"><figcaption>Balcony with a view</figcaption></figure>
      <figure class="slide"><img src="assets/gallery/rooms/06.webp" alt="Bathroom with a walk-in shower" width="1200" height="800" loading="lazy"><figcaption>Bathroom</figcaption></figure>
      <figure class="slide"><img src="assets/gallery/rooms/07.webp" alt="Bathroom with blue-edged tiles and two basins" width="1200" height="800" loading="lazy"><figcaption>Bathroom</figcaption></figure>
      <figure class="slide"><img src="assets/gallery/rooms/08.webp" alt="Dark stone bathroom with a vessel basin" width="1200" height="800" loading="lazy"><figcaption>Bathroom</figcaption></figure>
    </div>
    </section>

    <section class="inv-section">
      <header class="inv-head">
        <p class="sc">Hotel Rural Quinta do Marco</p>
        <h2 class="script">on the map</h2>
      </header>
      <div class="prose">
        <dl class="facts-list">
          <div><dt class="sc">Address</dt><dd><strong>{VENUE}</dd></div>
          <div><dt class="sc">From Faro airport</dt><dd><strong>About 30 min by car</strong><span>Transfers on the 1st and 3rd are on us &ndash; see <a href="travel.html">Travel</a>.</span></dd></div>
        </dl>
      </div>
      <div class="venue-map-wrap">
        <div id="venue-map" class="venue-map" role="region" aria-label="Map: Hotel Rural Quinta do Marco, near Tavira"></div>
        <a class="map-btn" href="https://maps.google.com/?q=Hotel%20Rural%20Quinta%20do%20Marco%2C%20Tavira" target="_blank" rel="noopener">
          <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2.5c-3.9 0-7 3-7 6.8 0 5 7 12.2 7 12.2s7-7.2 7-12.2c0-3.8-3.1-6.8-7-6.8Zm0 9.3a2.6 2.6 0 1 1 0-5.2 2.6 2.6 0 0 1 0 5.2Z"/></svg>
          Open in Google Maps
        </a>
      </div>
      <p class="map-credit">Basemap: <em>Azulejo Complete</em> by Marek Hoffmann &middot; &copy; OpenStreetMap contributors, Natural Earth</p>
    </section>""")


# Dishes to try (Algarve page): name and what it is. The photos and their
# credits are still in assets/dishes/ if they are ever wanted back.
DISHES = [
    ("pastel-de-nata", "Pastel de nata", "custard tart",
     "Crisp, flaky pastry with a warm, wobbly custard inside. Best straight from the oven with a dusting of cinnamon &ndash; and never just one."),
    ("bolo-de-berlim", "Bola de Berlim", "the beach doughnut",
     "Not a tourist trap &ndash; the Portuguese love it! A sugary doughnut sold by vendors walking along the sand, <em>com creme</em> (filled with custard) or <em>sem creme</em> (plain)."),
    ("bacalhau-com-natas", "Bacalhau com natas", "salt cod with cream",
     "Salt cod baked with cream and potatoes until golden on top. Portuguese comfort food at its best."),
    ("bacalhau-a-bras", "Bacalhau &agrave; Br&aacute;s", "salt cod with egg &amp; fries",
     "Shredded salt cod tossed with onions, matchstick fries and soft scrambled egg, finished with black olives and parsley."),
    ("polvo", "Polvo &agrave; lagareiro", "roasted octopus",
     "Tender octopus roasted with lots of olive oil and garlic, served with little &lsquo;punched&rsquo; potatoes."),
    ("sardinhas", "Sardinhas &amp; peixe grelhado", "grilled fish",
     "Grilled sardines taste like a Portuguese summer. Also ask for the catch of the day &ndash; <em>dourada</em> (sea bream) or <em>robalo</em> (sea bass), simply grilled."),
    ("camarao", "Camar&atilde;o ao alho", "garlic prawns",
     "Prawns sizzling in olive oil, garlic and a little chilli. Keep some bread for the sauce."),
    ("ameijoas", "Am&ecirc;ijoas &agrave; Bulh&atilde;o Pato", "clams",
     "Clams from the Ria Formosa, steamed with garlic, coriander, olive oil and a squeeze of lemon."),
    ("cataplana", "Cataplana", "the Algarve&rsquo;s own",
     "Named after the copper pan it&rsquo;s cooked in: seafood (or pork and clams) steamed in a rich tomato broth and opened at the table. Made for sharing."),
    ("arroz-de-marisco", "Arroz de marisco &amp; arroz de tomate", "seafood rice &amp; tomato rice",
     "Not a paella: a soupy, tomatoey rice full of prawns, clams and crab. Its simpler sister, <em>arroz de tomate</em>, usually comes with fried fish."),
    ("porco-preto", "Porco preto", "black Iberian pork",
     "From the black Iberian pig. Order <em>secretos</em> or <em>plumas</em> &ndash; juicy grilled cuts with loads of flavour."),
]


def dishes_html():
    # Just the name and what it is; the longer notes stay in DISHES for later
    rows = [f'        <li><b>{name}</b><span>{sub}</span></li>' for slug, name, sub, text in DISHES]
    return "\n".join(rows)


DISHES_HTML = dishes_html()

PAGES["location"] = ("The Algarve", BLUE, f"""
    <div class="inv-grid">
      <div>
        <header class="inv-head">
          <p class="sc">The south of Portugal&hellip;</p>
          <h1 class="script">the Algarve</h1>
        </header>
        <div class="prose">
          <p>We come back to the Algarve every summer. Our routines include beach, pool and long dinners with a full house. The house door stays open to let the wind through and we don&rsquo;t leave the table for at least 3 hours.</p>
          <p>Our wedding is near <strong>Tavira</strong>, a little town where life moves at its own pace. Think whitewashed houses, terracotta rooftops, cobbled streets, and a river running through the town. Just beyond, you&rsquo;ll find salt flats, endless sandy beaches, and the Atlantic Ocean.</p>
          <p>The celebration itself is up in the hills at <a href="accommodation.html">Hotel Quinta do Marco</a>, about 15 minutes from town. If you come early or stay a little longer, here is the Algarve we love &ndash; from Tavira all the way to the wild west coast.</p>
        </div>
      </div>
      <figure class="art tile-art">
        <img class="tile" src="assets/art/tile.webp" alt="" width="640" height="644">
        <img class="sardine" src="assets/art/sardine.webp" alt="Sardine" title="Psst, give it a tap" tabindex="0" role="button" width="900" height="319">
      </figure>
    </div>
    <section class="inv-section">
      <header class="inv-head">
        <p class="sc">Beaches, food &amp; things to do</p>
        <h2 class="script">our favourites</h2>
      </header>
      <div class="places-app">
        <div class="places-side">
          <div class="place-chips" role="group" aria-label="Show on the map">
            <button type="button" data-cat="" aria-pressed="true">All</button>
            <button type="button" data-cat="beach" aria-pressed="false">Beaches</button>
            <button type="button" data-cat="food" aria-pressed="false">Eat &amp; drink</button>
            <button type="button" data-cat="sight" aria-pressed="false">Things to do</button>
            <button type="button" data-cat="kids" aria-pressed="false">With kids</button>
          </div>
          <ul id="places-list" class="places-list" aria-label="Places"></ul>
        </div>
        <div class="places-map-wrap">
          <div id="places-map" class="places-map" role="region" aria-label="Map of our favourite places in the Algarve"></div>
        </div>
      </div>
      <p class="map-credit">Basemap: <em>Azulejo Complete</em> by Marek Hoffmann &middot; &copy; OpenStreetMap contributors, Natural Earth</p>

      <aside class="road-trip">
        <p class="sc">Got a few extra days?</p>
        <h3>Drive the west coast</h3>
        <p>From Lagos up to Sines: fishing villages, fresh fish, big cliffs and wild, windy beaches. Our favourites are Castelejo, Bordeira, Amado and Odeceixe.</p>
      </aside>
    </section>

    <section class="inv-section" style="--topic:{RUST}">
      <header class="inv-head">
        <p class="sc">Eat like a local</p>
        <h2 class="script">dishes to try</h2>
      </header>
      <ul class="dishes">
{DISHES_HTML}
      </ul>
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
      </div>
      <img class="day-art disco" src="assets/art/disco-ball.webp" alt="Disco ball" title="Give it a spin" tabindex="0" role="button" width="337" height="436" style="max-width:170px">
    </article>

    <article class="day full" style="--topic:{OLIVE}">
      <div class="prose">
        <h2 class="script">the Wedding Day</h2>
        <p class="sc">Saturday &middot; 02.10.2027</p>
        <p class="tbc">Details of the day to follow.</p>
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
      <p class="tbc">Reply form to follow.</p>
    </div>""")

HEAD = """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title} · Marek &amp; Paulo</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Beth+Ellen&family=Cormorant+Garamond:wght@500;600&family=Cormorant+SC:wght@700&family=Inter:wght@400;500;600&family=Lora:ital,wght@0,400;0,600;1,400&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="css/style.css?v=42">
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

FOOT = """  <script src="js/site.js?v=12"></script>
  <script src="js/eggs.js?v=11"></script>
</body>
</html>
"""


def nav():
    return "\n".join(f'      <a href="{slug}.html">{label}</a>' for slug, label in NAV)


# The walk through the site, in menu order. The footer links every page to
# the one before and after it, and the village outline leads home.
WALK = [
    ("index", "Home"),
    ("program", "Program"),
    ("accommodation", "Stay"),
    ("travel", "Travel"),
    ("weather", "Weather"),
    ("location", "Algarve"),
    ("map", "Guests"),
    ("rsvp", "RSVP"),
]

CHEVRON_L = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="m14.5 6-6 6 6 6"/></svg>'
CHEVRON_R = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="m9.5 6 6 6-6 6"/></svg>'

# The three houses as a small flat drawing (tools/village_mini.py)
from village_mini import village_svg
VILLAGE_MINI = village_svg()


def street(slug):
    i = [w[0] for w in WALK].index(slug)
    (p_slug, p_name), (n_slug, n_name) = WALK[i - 1], WALK[(i + 1) % len(WALK)]
    return f"""  <footer class="street">
    <nav class="pager" aria-label="Previous and next page">
      <a class="prev" href="{p_slug}.html">{CHEVRON_L}{p_name}</a>
      <a class="street-view" href="index.html" title="Back to the village" aria-label="Back to the village">
      {VILLAGE_MINI}
      </a>
      <a class="next" href="{n_slug}.html">{n_name}{CHEVRON_R}</a>
    </nav>
    <p class="foot">Marek &amp; Paulo &middot; 1 &ndash; 3 October 2027 &middot; Algarve</p>
  </footer>
"""


def main():
    for slug, (title, topic, body) in PAGES.items():
        html = HEAD.format(title=title, body_class="", nav=nav())
        foot = FOOT
        if 'class="carousel"' in body:
            foot = foot.replace('</body>', '  <script src="js/gallery.js?v=4"></script>\n</body>')
        if 'id="places-map"' in body or 'id="venue-map"' in body:
            foot = foot.replace('</body>', '  <script src="js/arcgis-common.js?v=3"></script>\n</body>')
        if 'id="places-map"' in body:
            foot = foot.replace('</body>', '  <script src="js/places-map.js?v=14"></script>\n</body>')
        if 'id="venue-map"' in body:
            foot = foot.replace('</body>', '  <script src="js/venue-map.js?v=3"></script>\n</body>')
        html += f'  <main class="page inv" style="--topic:{topic}">{body}\n  </main>\n' + street(slug) + foot
        open(f"{slug}.html", "w", encoding="utf-8").write(html)

    html = HEAD.format(title="Guest map", body_class=' class="map-page"', nav=nav())
    html += f"""  <main>
    <div class="map-head inv" style="--topic:{BLUE}">
      <p class="sc">Everyone&rsquo;s coming to the Algarve</p>
      <h1 class="script">the guests</h1>
    </div>
    <div class="guests-intro prose" style="--topic:{BLUE}">
      <p>This is where you&rsquo;re all coming from. Thank you for making the trip &ndash; we can&rsquo;t wait to see you in Tavira.</p>
    </div>
    <div class="map-embed">
      <iframe src="https://hoffmma5.github.io/wedding-map/" title="Map of where our wedding guests come from" loading="lazy" allow="fullscreen"></iframe>
    </div>
  </main>
""" + street("map") + FOOT
    open("map.html", "w", encoding="utf-8").write(html)
    print("pages written")


if __name__ == "__main__":
    main()
