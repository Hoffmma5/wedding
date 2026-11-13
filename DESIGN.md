# Design — Marek & Paulo

The current visual style of the wedding site, written down as the starting
point for the redesign. **This is the look we keep and build on, not one we
replace.** When a change contradicts this document, either the change is
wrong or this document gets updated in the same commit.

## The idea in one sentence

A hand-painted invitation to an Algarve summer: a watercolour street of
whitewashed Tavira houses you can walk into, and behind each door a page that
reads like the printed Tavira invitation — handwritten titles in their own
ink colour, small-caps labels, a bookish serif, and a watercolour object
beside the text.

## Two registers

The site speaks in two voices that share one paper colour.

| | Home (the village) | Inner pages (the invitation) |
|---|---|---|
| Hero | Full-width watercolour street (`village-day/night.webp`), every object a link | Script title in the topic colour + a small-caps line |
| Display type | Cormorant Garamond 600, uppercase, wide tracking (taken from the logo) | Beth Ellen (handwritten script) |
| Labels | Cormorant SC 700, 16 px | Cormorant SC 700, 16 px |
| Body | Lora 400, 17 px | Lora 400, 17 px, line-height 1.75 |
| Imagery | One big scene, layered for day/night | One watercolour object per section (disco ball, shrimp, oysters, sardine on an azulejo, torn-out paper map of Portugal and western Spain with a pearl on Tavira, sun, crabs, long table, hotel landscape) |

## Colour

### Base

| Token | Day | Night | Role |
|---|---|---|---|
| `--bg` | `#fcfafa` | `#0f1426` | Page. Day = the paper colour of the village painting, so the picture has no edge. |
| `--sky` | `#fcfafa` | `rgb(60,73,120)` | Sky band above the houses |
| `--surface` | `#ffffff` | `#182038` | Cards, tooltips, menus |
| `--text` | `#171a21` | `#eef0f7` | Body text |
| `--muted` | `#6b7180` | `#9aa2bd` | Secondary text (4.7 : 1 on `--bg` by day) |
| `--line` | `rgba(23,26,33,.09)` | `rgba(238,240,247,.1)` | Hairlines, hover fills |
| `--olive` | `#4b4b31` | `#ece4c6` | Logo ink: brand name, hero title, small caps |

### The three houses

Taken straight from the painting; used on the home page for the card dots and
in the hero objects.

| Token | Hex | From |
|---|---|---|
| `--accent` | `#2f5fb5` (night `#8fb0ff`) | the blue house; also the focus ring colour |
| `--yellow` | `#f2b705` | the yellow house |
| `--coral` | `#e8664a` | the coral house |

### Invitation inks (`--topic`)

Each inner page and section sets `style="--topic:…"`; script titles, `strong`,
links and accents use it through `--topic-c`. At night `--topic-c` is mixed
50 % with white. Defined in `tools/make_pages.py`.

| Name | Hex | Used for |
|---|---|---|
| BLUE | `#1f4fa0` | Travel, Algarve, Guests — azulejo blue |
| RUST | `#b5432a` | Weather, dishes to try |
| BROWN | `#8b5523` | Transfer, Sunday |
| OLIVE | `#7b8152` | The Hotel, at the Quinta, the Wedding Day, RSVP |
| WINE | `#7a3b3b` | The Program, the Bedrooms |
| CORAL | `#d4504c` | Friday |

### Night

Night is a full second palette, not an inverted one: deep indigo
`#0f1426`, the painting swaps to its night layer, windows and the lamp glow
amber (`rgba(255,196,102,…)` with `mix-blend-mode: screen`), the sun becomes a
crescent moon. Saved in `localStorage` (`theme`), defaults to the OS setting.

## Typography

One job per family, same on every page (all pages load all five). Tokens
live at the top of `style.css`.

| Token | Family | Role |
|---|---|---|
| `--serif` | Lora 400/600/italic | **Everything you read**: body (the `body` default), card text, facts, figures |
| `--sc` | Cormorant SC 700 | **Every label**: the line above/below a title, `<dt>`, fact labels, place categories, the hero date line. Never tracked-out uppercase. |
| `--script` | Beth Ellen | **Titles**: `.script` h1 48–76 px, h2 40–58 px, mostly lowercase ("the Program", "how we got here") |
| `--sans` | Inter 400–600 | **Controls and fine print only**: nav, buttons, chips, tooltips, map UI, credits |
| `--display` | Cormorant Garamond 500/600 | Brand name in the nav and the hero title (uppercase, wide tracking, from the logo) |

Size scale (around 17 px body): `--fs-xs` 12 · `--fs-s` 14 · `--fs-m` 15 ·
`--fs-base` 17 · `--fs-l` 20 · `--fs-xl` 24 · `--fs-xxl` 28; labels
`--fs-label` 16 (Cormorant SC has a small x-height). Display sizes use
`clamp()`.

Hero: h1 `clamp(26px, 50u, 56px)`, `.14em` tracking; tagline "To this and every
summer" 10–17 px, `.24em`; date line in small caps 14–18 px. `u` is one pixel
of the 1926 px painting, so the title scales with the picture.

A label above a script title is tucked in close (`-.12em`); a label below it
sits just under the baseline (`.3em`), clear of the long descenders.

## Layout and spacing

- **Nav**: fixed, 60 px, transparent over the home hero, frosted
  (`blur(12px)`, 82 % `--bg`) once scrolled and always on inner pages. Pill
  links (`999px`), RSVP as a dark pill. Below 820 px a hamburger opens a card
  menu.
- **Home hero**: the picture is 1926 × 817 px plus a 360 px sky band. Every
  hotspot is placed in picture pixels with `--x/--y/--w/--h`. Width fills the
  screen but keeps the doors above the fold; under 860 px the street stays
  860 px wide and scrolls sideways ("Swipe to see the whole street").
- **Home below the village**: an **orange strip** (`.strip`, roof-tile
  `#c4521f`, white text 4.6 : 1) right under the painting with the six pages:
  a small line icon above a plain Inter label, 6 across on desktop, 3 × 2 on
  phones. Then a one-line hint that the village is clickable. No RSVP block
  and no countdown on the home page; RSVP lives in the menu and the coral door.
- **Inner pages**: `.page.inv`, 1000 px max, 108 px top padding. Text left,
  watercolour object right (`.inv-grid`, `1fr / 200–320px`); sections separated
  by a hairline and 48–80 px of space. One column under 760 px, art centred
  above or below the text.
- **Footer** (every inner page and Guests): one hairline, then a single row:
  "‹ Previous page" (Inter, muted), a small **line drawing of the three
  houses** in the middle that leads home, "Next page ›". Under it the
  names/date line in 12 px. Order = the menu, from Home round to RSVP and
  back (`WALK` in `tools/make_pages.py`).
- **Radii**: 16 px (cards, maps, story frame), 14 px (highlights, weather
  tiles, list items), 12 px (stats, placeholders), 999 px (pills, chips),
  3 px (polaroids).
- **Shadow**: one soft shadow, `0 1px 2px / 0 8px 24px` at 4–8 % black, used
  on hover and on floating UI.
- Fluid spacing with `clamp()` throughout; content is left-aligned on inner
  pages and centred on the home page and the Guests intro.

## Components

- **Icons** (`tools/icons.py`): small two-tone pictograms from the wedding's
  world – clinking glasses, a little Algarve house, a plane, the sun, a
  sardine, the globe with a heart; on Stay a pool, a cocktail with an orange
  slice, a lotus, a slide, a sheep. 24 × 24, stroke 1.6–1.5 in
  `currentColor`; shapes with `.f` get a soft tint (`--tint`), `.s` are solid.
- **Facilities** (Stay, `ul.facilities`): eight line icons in the section's ink
  with a short Inter label, 4 across, no boxes; details are on the hotel's site.
- **Facts list** (`dl.facts-list`): small-caps term, Lora value in topic colour,
  muted detail line.
- **Highlights** (`ul.highlights`): grid of bordered tiles, Lora title in topic
  colour, Inter muted body.
- **Weather tiles** (`.wx`): icon, big Lora number, muted caption.
- **Polaroid carousel** (Stay): off-white polaroids with a handwritten caption,
  curving away like a ring; the centre one faces you; full-screen viewer.
- **Places app** (Algarve): side list with category chips + ArcGIS map on
  Marek's *Azulejo Complete* basemap, overview inset, full-screen mode.
- **Dishes to try**: a plain two-column list – the name in the section's ink,
  what it is in muted italic below, hairlines between rows. No photos.
- **Content still to come** (`p.tbc`): one quiet line in muted italic, no
  box ("Details of the day to follow."). The home Story section is hidden
  until `data-storymap` has a link.
- **Travel map** (`.map-art`, `tools/make_iberia.py`): a piece torn out of an
  old paper map, tilted 1.2°. The invitation's watercolour Portugal, western
  Spain as pale sand with a pencilled coast, the Atlantic with cartographic
  water lines. Labels, Faro, the pearl on Tavira and a dotted flight path
  landing at Faro are an SVG in the same 723 × 922 canvas. Like the polaroids
  and notes it stays paper at night (only dimmed).
- **Toast**: Lora italic message at the bottom of the screen.

## Motion

- Day ↔ night: 1.2 s cross-fade of every colour and painting layer; window
  lights come on 0.6–0.8 s later; the lamp flickers on.
- Hotspots answer the visitor: doors swing open (3D `rotateY(70deg)`, warm
  interior at night), the plane speeds up, the weathervane spins (press and hold:
  it points to where you are), the house tile lifts, the orange tree drops
  oranges that roll away.
- Ambient: the plane drifts (6 s), the vane sways (7 s). Nothing else moves on
  its own.
- Entering a page from the village: the hero zooms 3.2× towards the clicked
  door and fades to paper.
- The way back is the mirror: the village outline in a page's footer fades
  the page to paper, and the home page opens 2.4× close up on the street and
  zooms out to the whole village (`returning` → `zooming-out` on `<html>`;
  flag in `sessionStorage`, set in `site.js`, read in the home page's head).
- Story section unfolds with scroll (`--p`: width, radius and offset).
- Easter eggs: disco ball (music and lights), crabs walk off sideways, the
  sardine swims away, a school of sardines, wedding-weekend party mode with
  bunting (`?party`).
- `prefers-reduced-motion` switches off all animation and transitions.

## Tone of voice

Warm, personal, first person plural, a little playful ("we don't leave the
table for at least 3 hours", "pick a driver and let them be the hero").
English, with Portuguese words in italics (*obrigado*, *um imperial*). Titles
are lowercase and handwritten ("the Program", "good to know").

## Practical notes

- Inner pages are generated by `tools/make_pages.py`; change the template and
  re-run rather than editing the HTML by hand.
- CSS is one file, `css/style.css`, cache-busted with `?v=` in every page.
- Painting coordinates are in picture pixels (1926 × 817); see the comment at
  the top of `style.css`.
