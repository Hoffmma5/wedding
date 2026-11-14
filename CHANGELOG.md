# Changelog

All notable changes to the Marek & Paulo wedding website.
Newest first. Dates are when the change was made; "Unreleased" is not pushed to GitHub Pages yet.

## Unreleased

### Changed
- **One icon style across the site:** the home strip, Stay facilities, good to know and weather now share the light style of the weather icons – a thin line with a faint tint, no solid parts, one size.
- **Good to know** has six tips with the details people asked about: "12:00 there is 11:00 here", "Cards are mostly accepted – bring some euros, just in case", "Calls and data like at home", "From the EU: ID card – from elsewhere: passport", "Driving: max 0.5 ‰ – about 2–3 small beers", "Emergency: 112, same as at home". *Obrigado* and *um imperial* are gone.
- **Weather numbers** are an open row between two hairlines instead of three boxed cards, with the icons tinted in the page's ink.
- **On phones the watercolour objects are small accents** (sun, crabs, disco ball, oysters, sardine – 150 px at most) instead of filling a screen each.
- **The home strip is a plain brick band across the full width of the page** – muted brick with cream labels instead of the bright orange block, and a deep, quiet brick at night so the icons no longer glare.
- **One ink per page, from the village:** titles and accents use only the painting's three pigments – azulejo blue, roof terracotta, sage olive – and every section keeps its page's ink (Program was wine, coral and brown; Stay had a wine section; Travel a brown one; dishes rust).
- **Footer:** the little drawing is replaced by the village painting itself, small – the same three houses as on the home page, and at night the dark version with the windows lit.
- **Home:** "Everything in the village is clickable…" now sits between the village and the orange strip.

### Fixed
- **Our favourites map** starts zoomed in on the coast from Albufeira to Tavira (with Loulé and the Quinta) instead of fitting every place on the list, and the **minimap now follows the big map**: it re-centres on wherever you pan and frames the visible area.

## 2026-11-13 – simplified

### Changed
- **The footer village looks like the village again:** instead of a thin outline, a small flat drawing of the three houses – white walls with blue, yellow and coral trims, terracotta tile roofs, chimneys with coloured caps, the orange tree, the lamp and the bougainvillea.
- **Icons with more character:** the home strip and the Stay facilities use small two-tone pictograms from the wedding's world – clinking glasses for the Program, a little Algarve house for Stay, a sardine for the Algarve, the globe with a heart for the guests, a cocktail with an orange slice, a lotus for the spa, a sheep for the animal farm – instead of plain outlines.
- **Drive the west coast** is two sentences instead of two paragraphs, without the tinted box.
- **Dishes to try** is a simple two-column list – the dish and what it is ("Pastel de nata – custard tart") – instead of eleven photo cards with descriptions and credits. The photos stay in `assets/dishes/` in case they are wanted back.
- **Stay:** "For the little ones" and "For the grown-ups" are replaced by eight facility icons (heated pool, pool bar, restaurant, spa & sauna, gym, playground, animal farm, views to the sea) and a link to the hotel's website. "find us" is now "on the map".
- **Minimal footer:** the painted village strip and the script "previous / next door" titles are replaced by one quiet row – "‹ Guests", a small line drawing of the three houses that leads home (still with the zoom-out), "Home ›" – and the names line.
- **Plain placeholders:** the taped paper notes are gone. Content that is still to come is one quiet line ("Details of the day to follow.", "Reply form to follow."); Friday's note is dropped, and the home page hides the story section until the StoryMap link is in.
- **Home page is simpler:** the six pages sit on an orange strip right under the village, each with a small line icon and a plain label, instead of the watercolour index in script. The RSVP block and the countdown (the strip below and the tile above the RSVP door) are gone; RSVP stays in the menu and behind the coral door.

## 2026-11-13 – the redesign

### Added
- **Walking back zooms out:** clicking the village strip at the bottom of a page fades the page to paper, and the home page opens close up on the street and zooms out to the whole village – the mirror of walking in through a door. Skipped when the visitor prefers reduced motion.
- **Handwritten notes for things still to come:** the grey "coming soon" boxes on Program and RSVP are now paper notes taped onto the page, written in script in the section's colour ("The welcome party is still being planned – time and place coming soon."). On the home page the empty story-map frame is replaced by a note too ("Our story map is still being drawn – Marek is on it."); the full frame comes back as soon as the StoryMap link is filled in.
- **The street continues:** every inner page (and the guest map) now ends with the previous and next door – the neighbouring pages' titles in their own colours – and a strip of the village painting that takes you back home, lit windows and all at night. No more dead ends after the last paragraph.
- **Countdown tile in the village:** a second azulejo tile, painted above the RSVP door on the coral house, counts down in Portuguese – *322 dias*, then *amanhã*, *hoje!* (also in party mode) and finally *casados*. Hover shows the English. On phones, where the street opens away from the coral house, the countdown is also written under the RSVP button.

### Changed
- **New Travel map:** a piece torn out of an old paper map instead of Portugal on a faded wash. The invitation's watercolour Portugal sits next to western Spain (pale land with a real coastline from Galicia to Cádiz), the Atlantic has cartographic water lines, and crisp labels name Portugal, España, the ocean and Faro. A dotted flight path lands at Faro and the pearl marks Tavira. It looks the same at night instead of turning smoky, and nothing is cut off.
- **Footer village strip** is framed higher: it starts just under the eaves, so the windows, the top of the orange tree and the bougainvillea are whole, and the doors fade out below. Phones still show the whole street.
- **Street footer is quieter:** smaller previous/next door titles (26–32 px instead of 36–52 px), smaller grey labels, a lower village strip; on phones both doors fit on one line.
- **Guests page:** a two-sentence intro instead of three paragraphs (the note about Marek's work is gone), and the map now fills nearly the whole screen.
- **Home page reads like the invitation:** the When / Where / Countdown strip and the seven link cards are gone. In their place is an index of the pages, each written in its own ink with its watercolour (disco ball, the hotel landscape, Portugal, the sun, the sardine, the pearl), and below it an RSVP reply block with the long table, *RSVP* in script, a **Reply to the invitation** button and the countdown. On phones each page is one compact row.
- **One type system on every page:** Lora for everything you read, Cormorant SC small caps for every label (no more tracked-out Inter capitals), Beth Ellen for titles, Inter only for buttons, menus, chips and credits. Sizes come from one scale (`--fs-*` tokens). The home page now loads the invitation fonts too.
- **Home:** the date line under the names is set in small caps; "Our story" became an invitation heading – *how we got here* in script with a small-caps line above it.
- **Small caps under script titles** no longer run into the long descenders ("friday", "the Wedding Day").

### Fixed
- The Stay page is called **"the Stay"** in the street footer and the home index, matching the *Stay* tab in the menu (was "the Hotel").
- **Lit windows at night look clean again:** only the glass panes glow now, measured pane by pane on the painting, so the white frames and crossbars stay crisp instead of being covered by ragged yellow and heavy brown bars. The brush strokes in the glass still show through the light.
- **Readable inks:** small text in a section's colour (bold text, links, card titles, the selected map chip) now uses a slightly darker `--ink`, so olive and coral pass WCAG AA (were ~3.9 : 1). Script titles keep the full colour.
- **Keyboard focus** is visible on the home-page cards (was only a soft shadow).
- **RSVP in the menu** stays a dark button on the RSVP page, with a ring for "you are here" (it used to turn grey).
- **"Good to know" and "at the Quinta" grids** line up with the text again (a list rule indented them by ~19 px).
- **"How we got here"** is readable before you scroll (it started at 15 % opacity).
- "Coming soon" boxes have darker text; dish cards no longer lift on hover, as they aren't links.
- **Weather on phones:** the three numbers are rows instead of three cramped columns.

## 2026-11-13 (night)

### Fixed
- **Both maps showed "could not load" on SDK 5.2:** `ui: { components: ['zoom', 'attribution'] }` is no longer valid in 5.x – `'attribution'` isn't a UI component any more (the SDK adds the attribution line by itself) and passing it crashed the MapView. Now `['zoom']`.
- Map errors are no longer swallowed: if a map fails, the real error is logged to the browser console (`[wedding map] …`) before the friendly fallback text appears.
- The minimap no longer shows its own "Powered by Esri" line (the main map shows it).

## 2026-11-13 (evening)

### Fixed
- **Algarve map didn't load** on the live site (`can't access property "scale"` in MapView): the minimum zoom was set to 5.5, but the SDK only accepts whole zoom levels there. Now 5 – still out to the whole of Portugal.

### Changed
- **Maps upgraded to ArcGIS Maps SDK for JavaScript 5.2 and Calcite Components 5.2.1** (from 4.31 / 2.13). 5.x no longer ships the old AMD `init.js`, so the SDK is now loaded as ES modules through `js/arcgis-boot.js` (Calcite + core only, without the AI / charts / coding components) and classes are imported with `$arcgis.import()`.

## 2026-11-13 (later)

### Added
- **Algarve map:** full-screen button (under the zoom buttons) that opens the whole app – list and map – full screen; on iPhone it fills the window instead. Esc or the button exits; in full screen the mouse wheel zooms the map directly.

### Changed
- **Algarve map:** you can now zoom out as far as the whole of Portugal (was limited to the Algarve).
- **Algarve map on phones:** the minimap sits in the top-right corner so it never covers a popup; tablets and desktops keep it bottom-right.

## 2026-11-13

### Added
- **Stay:** the Google Maps embed is replaced by a custom ArcGIS map on Marek's *Azulejo Complete* basemap – the hotel marked with the wedding emblem (the orange) and a popup with the address and directions, plus Tavira and Faro airport for orientation. A clearly visible **Open in Google Maps** button sits on the map.
- `js/arcgis-common.js`: shared map setup for both pages (loads the ArcGIS SDK once and only when needed, the azulejo basemap with night dimming, fallback to Esri's grey canvas if the tiles can't load).

### Changed
- **Algarve favourites map** now uses *Azulejo Complete* as its basemap, from country scale down to street level; the overview inset uses it too (the old *Azulejo Atlas* service is no longer online).

## 2026-11-12 (night)

### Changed
- **Algarve map:** the Azulejo Atlas inset moved to the bottom-right corner.

## 2026-11-12 (evening)

### Changed
- **Favourites map** works like one app: a slim side list (icon, name, category) next to the map, with the tips and a Directions button in Esri-style popups. Clicking a row zooms to the place and opens its popup; clicking a marker highlights its row. On phones the map sits above a scrollable list. The Azulejo Atlas inset moved to the top-right corner.
- **Tavira tab renamed to Algarve** (page "The Algarve"): the heading is now "the Algarve", with Tavira and the venue woven into the intro text; menu, homepage card and the village tile label updated.
- **Dishes:** porco preto now shows a plated grilled pork dish (CC0) instead of the pig.

## 2026-11-12 (later)

### Added
- **Tavira map:** Marek & Paulo's own recommendations replace the example places – beaches (Pego Fundo, Barril, Ninho de Andorinha, plus the west coast: Castelejo, Bordeira, Amado, Amoreira, Odeceixe), restaurants (Casa Velha, Copos & Petiscos, O Teodósio), things to do (Monterosa olive oil, Loulé market, kayaking and boat trips in Albufeira, paddle boarding and the old town in Lagos).
- **Tavira map:** new "With kids" filter with four waterparks (Aquashow, Zoomarine, Aqualand, Slide & Splash), shown with crab markers; tips remind to check seasonal opening dates.
- **Tavira:** "Drive the west coast" note about the Rota Vicentina road trip from Lagos to Sines, surfing, and the coastal road via Lisbon.
- **Tavira:** "dishes to try" – 11 cards with photos and descriptions (pastel de nata, bola de Berlim, bacalhau com natas, bacalhau à Brás, polvo à lagareiro, grilled fish, garlic prawns, clams, cataplana, seafood & tomato rice, porco preto). Photos from Wikimedia Commons under free licences, credited on each card (`assets/dishes/credits.json`).
- **Travel:** two new cards – ordering beer like a local (*imperial* 0.2 l vs *caneca*) and the 0.5 ‰ drink-driving limit.

## 2026-11-12

### Added
- **Stay:** "at the Quinta" – a short, warm intro with what there is for the little ones (playground, animal farm, pool) and for the grown-ups (pool & bar, spa, gym), plus a link to the hotel's website.
- **Stay:** two photo carousels, one for the hotel and one for the bedrooms, styled as a row of polaroids that curve away like a ring, with handwritten captions; arrows, dots, swipe, keyboard, and a full-screen viewer.
- **Stay:** "find us" section with the venue address and Google map (moved here from Location).
- **Travel:** "good to know" cards in a friendly voice: time difference, euros, phone & data, ID, a word of Portuguese, emergency number.
- **Guests:** thank-you text above the guest map.
- **Tavira:** "our favourites" map built with the ArcGIS Maps SDK for JavaScript 4.31. Places come from `assets/data/places.geojson`, the invitation watercolours are the markers (shell = beaches, sardine = eat & drink, shrimp = things to do, orange = the wedding), and there are category chips, popups with tips and directions, and a matching list of cards under the map. The basemap is Esri's light/dark grey canvas, following night mode, with Marek's own *Azulejo Atlas* vector tiles as an overview inset in the corner (the atlas only reaches ~1:1M, so it can't be the detailed map); the SDK only loads when the map is about to scroll into view. Seeded with 7 example places plus the venue, all to be replaced with real favourites.
- `CHANGELOG.md` (this file).

### Changed
- **Location** is now **Tavira** (page title "Tavira & the Algarve"): Tavira intro, the Algarve, and the favourites map. Menu, homepage card and the "Algarve" tile label updated.
- **Stay:** the watercolour landscape is back at the top, under the heading.
- **Stay:** bedrooms text shortened and warmed up; carousel caption "Farm friends" is now "The animal farm".

## 2026-11-11

### Added
- **Weathervane easter egg:** press and hold the weathervane and it turns towards the visitor's location, showing the distance to Tavira. A normal click still opens the guest map.
- **Disco:** light flecks pulse to an original ~7 s acid-techno loop generated with Web Audio; "Stop the party" button and Esc to stop.
- **Easter eggs:** scuttling/walking crabs (Weather), swimming sardine (Location), orange-juice note after 10 shakes of the tree, secret words *sardinha / sardine / sardinka* release a school of sardines, wedding-weekend party mode with bunting (preview with `?party`).
- **Travel:** Spain painted faintly behind Portugal so the map no longer looks like an island.
- **Weather:** link to current conditions in Tavira on yr.no.

### Changed
- **Phones:** the village scrolls sideways again (swipe hint now stays until the visitor swipes).
- **Travel:** pearl moved to Tavira's real position; "Spain" label removed.
- **Location:** sardine tile no longer overlaps the map on phones.
- **Guests:** title written as "the guests" so the handwritten G isn't read as a Q.
- Embedded yr.no card replaced by a simple link.

### Content
- Inner pages filled with the Tavira invitation's text, lettering (Beth Ellen, Cormorant SC, Lora), topic colours and watercolour illustrations.

## 2026-11-10

### Added
- First public version on GitHub Pages: the illustrated village homepage (doors, sun/moon, plane, weathervane, house tile, street lamp day/night switch, orange tree), logo heading, night mode, countdown, page cards and the "Our story" StoryMap section.
- Inner pages: Program, Stay, Travel, Weather, Location, Guests (embedded guest map), RSVP.
