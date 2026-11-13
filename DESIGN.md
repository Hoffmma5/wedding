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
| Labels | Inter 500, 11–12 px, uppercase, `.16em` tracking | Cormorant SC 700, 16 px, `.1em` tracking |
| Body | Inter 400, 16 px | Lora 400, 17 px, line-height 1.75 |
| Imagery | One big scene, layered for day/night | One watercolour object per section (disco ball, shrimp, oysters, sardine on an azulejo, Iberia map with a pearl on Tavira, sun, crabs, long table, hotel landscape) |

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

Five families, loaded from Google Fonts (home loads only the first two).

| Family | Weights | Role |
|---|---|---|
| Cormorant Garamond | 500, 600 | Brand name in the nav (17 px, `.12em`, uppercase), hero title |
| Inter | 300–600 | UI: nav, buttons, chips, tooltips; all home-page body text; card text on inner pages |
| Beth Ellen | 400 | Script titles: h1 44–76 px, h2 38–58 px, line-height 1.5, mostly lowercase ("the Program", "friday", "good to know") |
| Cormorant SC | 700 | Small-caps labels: the line above or below a script title, `<dt>` in fact lists, dish subtitles |
| Lora | 400, 600, italic | Inner-page prose, card titles in highlights, weather numbers |

Hero: h1 `clamp(26px, 50u, 56px)`, `.14em` tracking; tagline "To this and every
summer" 10–17 px, `.24em`; date line 11 px Inter caps. `u` is one pixel of the
1926 px painting, so the title scales with the picture.

The small-caps line is pulled into the script title with negative margins
(`-.15em` above, `-.55em` below) so the two overlap like hand lettering on the
invitation.

## Layout and spacing

- **Nav**: fixed, 60 px, transparent over the home hero, frosted
  (`blur(12px)`, 82 % `--bg`) once scrolled and always on inner pages. Pill
  links (`999px`), RSVP as a dark pill. Below 820 px a hamburger opens a card
  menu.
- **Home hero**: the picture is 1926 × 817 px plus a 360 px sky band. Every
  hotspot is placed in picture pixels with `--x/--y/--w/--h`. Width fills the
  screen but keeps the doors above the fold; under 860 px the street stays
  860 px wide and scrolls sideways ("Swipe to see the whole street").
- **Home details**: 1080 px column; a three-column facts strip
  (When / Where / Countdown) between hairlines; an auto-fill grid of seven
  link cards (220 px min), the RSVP card inverted.
- **Inner pages**: `.page.inv`, 1000 px max, 108 px top padding. Text left,
  watercolour object right (`.inv-grid`, `1fr / 200–320px`); sections separated
  by a hairline and 48–80 px of space. One column under 760 px, art centred
  above or below the text.
- **Radii**: 16 px (cards, maps, story frame), 14 px (highlights, weather
  tiles, list items), 12 px (stats, placeholders), 999 px (pills, chips),
  3 px (polaroids).
- **Shadow**: one soft shadow, `0 1px 2px / 0 8px 24px` at 4–8 % black, used
  on hover and on floating UI.
- Fluid spacing with `clamp()` throughout; content is left-aligned on inner
  pages and centred on the home page and the Guests intro.

## Components

- **Link cards** (home): white, 1 px line, coloured dot (house colour), title +
  one-line description, `→` on the right, lift 2 px on hover.
- **Facts list** (`dl.facts-list`): small-caps term, Lora value in topic colour,
  muted detail line.
- **Highlights** (`ul.highlights`): grid of bordered tiles, Lora title in topic
  colour, Inter muted body.
- **Weather tiles** (`.wx`): icon, big Lora number, muted caption.
- **Polaroid carousel** (Stay): off-white polaroids with a handwritten caption,
  curving away like a ring; the centre one faces you; full-screen viewer.
- **Places app** (Algarve): side list with category chips + ArcGIS map on
  Marek's *Azulejo Complete* basemap, overview inset, full-screen mode.
- **Dish cards**: photo 4:3, Lora name in rust, Cormorant SC subtitle, credit.
- **Placeholders**: grey rounded box, muted Inter text ("coming soon").
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
