# Changelog

All notable changes to the Marek & Paulo wedding website.
Newest first. Dates are when the change was made; "Unreleased" is not pushed to GitHub Pages yet.

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
