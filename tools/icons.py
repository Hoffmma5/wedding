"""The site's one icon family: ink and wash, like the painting.

Each icon is drawn on a 24 x 24 grid as plain shapes. svg() turns it into
two layers:

  wash  the closed shapes (class "f"), filled with the ink at low opacity,
        nudged down-right by a pixel and roughened by the #wash filter, so
        the colour sits slightly off the line like a watercolour fill;
  line  every shape as a thin pen line (1.2, set in CSS as .ico),
        wobbled very slightly by the #ink filter.

Shapes with class "bg" are filled with the paper colour, so a coin can sit
on top of a card. The colour comes from where the icon is used
(currentColor). FILTERS must be on every page that shows icons; make_pages.py
puts it at the top of <body> and into the home page's strip.
"""

import re

FILTERS = (
    '<svg class="ico-defs" width="0" height="0" aria-hidden="true" focusable="false"><defs>'
    '<filter id="ink" x="-10%" y="-10%" width="120%" height="120%">'
    '<feTurbulence type="fractalNoise" baseFrequency=".12" numOctaves="1" seed="4"/>'
    '<feDisplacementMap in="SourceGraphic" scale=".55" xChannelSelector="R" yChannelSelector="G"/></filter>'
    '<filter id="wash" x="-25%" y="-25%" width="150%" height="150%">'
    '<feTurbulence type="fractalNoise" baseFrequency=".14" numOctaves="2" seed="9"/>'
    '<feDisplacementMap in="SourceGraphic" scale="3.4" xChannelSelector="R" yChannelSelector="G"/>'
    '<feGaussianBlur stdDeviation=".3" result="b"/>'
    # watercolour pools at its edges: add a darker rim
    '<feMorphology in="b" operator="erode" radius=".8" result="inner"/>'
    '<feComposite in="b" in2="inner" operator="out" result="rim"/>'
    '<feMerge><feMergeNode in="b"/><feMergeNode in="rim"/></feMerge></filter>'
    '</defs></svg>'
)

STRIP = {
    # two glasses, clinking
    "program": '<path class="f" d="M5 3.5h5l-.7 5.4a1.8 1.8 0 0 1-3.6 0Z"/><path d="M7.5 10.6V19M5.4 19h4.2"/>'
               '<path class="f" d="M14 3.5h5l-.7 5.4a1.8 1.8 0 0 1-3.6 0Z"/><path d="M16.5 10.6V19M14.4 19h4.2M12 1.5v1.5"/>',
    # a little Algarve house with its chimney
    "accommodation": '<path class="f" d="M3.5 11 12 7.5l8.5 3.5v9.5h-17Z"/><path d="M16 9.6V5.8h2.4v4.8M8 20.5V16h3v4.5M14 14h3v2.5h-3Z"/>',
    # a suitcase with a luggage tag
    "travel": '<rect class="f" x="3.5" y="8" width="17" height="12" rx="2.2"/>'
              '<path d="M9 8V5.8c0-.7.5-1.3 1.3-1.3h3.4c.8 0 1.3.6 1.3 1.3V8M7.5 8v12M16.5 8v12M16.5 11.5l2.4 2.6"/>'
              '<rect x="17.6" y="13.6" width="2.6" height="3.4" rx=".6" transform="rotate(-20 18.9 15.3)"/>',
    # sun
    "weather": '<circle class="f" cx="12" cy="12" r="4"/><path d="M12 2.5v2M12 19.5v2M2.5 12h2M19.5 12h2M5.3 5.3l1.4 1.4M17.3 17.3l1.4 1.4M5.3 18.7l1.4-1.4M17.3 6.7l1.4-1.4"/>',
    # a sardine
    "location": '<path class="f" d="M2.5 12c3.2-4 9.5-5 14-1.6l3.8-2.9v9l-3.8-2.9c-4.5 3.4-10.8 2.4-14-1.6Z"/><circle cx="6.4" cy="11.3" r=".7"/><path d="M9 9.8c.8 1.4.8 3 0 4.4"/>',
    # the world
    "map": '<circle class="f" cx="12" cy="12" r="8.5"/><path d="M3.5 12h17M12 3.5c2.3 2.4 3.4 5.2 3.4 8.5s-1.1 6.1-3.4 8.5c-2.3-2.4-3.4-5.2-3.4-8.5S9.7 5.9 12 3.5Z"/>',
}

STRIP_LABELS = [
    ("program", "Program"),
    ("accommodation", "Stay"),
    ("travel", "Travel"),
    ("weather", "Weather"),
    ("location", "Algarve"),
    ("map", "Guests"),
]

FACILITIES = [
    ("Heated pool", '<path class="f" d="M3 16c1.5 1.1 3 1.1 4.5 0s3-1.1 4.5 0 3 1.1 4.5 0 3-1.1 4.5 0v4.5H3Z"/>'
                    '<path d="M9 15V6a1.6 1.6 0 0 0-3.2 0M15.2 15V6a1.6 1.6 0 0 0-3.2 0M9 8.5h6.2M9 11.7h6.2"/>'),
    ("Pool bar", '<path class="f" d="M4.5 5h12L10.5 12Z"/><path d="M10.5 12v8M7.3 20h6.4M12.5 9.6 17.5 3"/><circle class="f" cx="17.6" cy="5.2" r="2.4"/>'),
    ("Restaurant", '<circle class="f" cx="12" cy="12.5" r="5"/><path d="M3 3.5V8a1.5 1.5 0 0 0 3 0V3.5M4.5 3.5v17M21 20.5v-17c-1.6 1-2.5 3.1-2.5 6.2H21"/>'),
    ("Spa &amp; sauna", '<path class="f" d="M12 18.5c-2.8-2-4.1-4.8-3.6-8.6 2.5 1.4 3.6 4.3 3.6 8.6Zm0 0c2.8-2 4.1-4.8 3.6-8.6-2.5 1.4-3.6 4.3-3.6 8.6Z"/>'
                        '<path d="M12 18.5c-3.8 0-6.6-1.3-8.1-3.8 2.9-.6 5.7.7 8.1 3.8Zm0 0c3.8 0 6.6-1.3 8.1-3.8-2.9-.6-5.7.7-8.1 3.8ZM4 21.5h16"/>'),
    ("Gym", '<path class="f" d="M5.5 7.5h2.5v9H5.5ZM16 7.5h2.5v9H16Z"/><path d="M3.5 10v4M20.5 10v4M8 12h8"/>'),
    ("Playground", '<path class="f" d="M9 8c3.2 0 4.4 2.9 6 6.8s2.6 5.2 5.5 5.2V17.8c-1.8 0-2.7-1.3-4.2-4.6S12.5 8 9 8Z"/><path d="M4.5 20.5V8H9v12.5M4.5 11h4.5M4.5 14h4.5M4.5 17h4.5M3 20.5h18"/>'),
    ("Animal farm", '<path class="f" d="M8.5 9.5a2.5 2.5 0 0 1 4.2-1.4 2.6 2.6 0 0 1 4.5.6 2.4 2.4 0 0 1 1.8 4.1 2.3 2.3 0 0 1-2.1 3.4H9.8a2.4 2.4 0 0 1-1.8-4 2.3 2.3 0 0 1 .5-2.7Z"/>'
                    '<ellipse cx="5.8" cy="11.2" rx="1.8" ry="2.5" transform="rotate(-24 5.8 11.2)"/><path d="M10.6 16.2v3.8M15.4 16.2v3.8"/>'),
    ("Views to the sea", '<path class="f" d="M2.5 16.5c2.8-4.5 5.6-6.4 8.5-6.4s5 1.9 7 3.7 2.6 2.2 3.5 2.2v1.5h-19Z"/><circle class="f" cx="17" cy="5.8" r="2"/>'
                         '<path d="M2.5 20.5c1.5 1 3 1 4.5 0s3-1 4.5 0 3 1 4.5 0 3-1 4.5 0"/>'),
]

WEATHER = {
    "sun": STRIP["weather"],
    "moon": '<path class="f" d="M19 14.5A7.5 7.5 0 0 1 9.5 5a7.5 7.5 0 1 0 9.5 9.5Z"/>',
    "rain": '<path class="f" d="M7 15a4 4 0 0 1-.6-8A5.5 5.5 0 0 1 17 8a3.5 3.5 0 0 1 .5 7H7Z"/><path d="M9 18l-1 2.5M13 18l-1 2.5M17 18l-1 2.5"/>',
}

# Travel: "good to know", one icon and one short line each
TIPS = [
    # an alarm clock on little feet
    ('<circle class="f" cx="12" cy="13" r="7"/><path d="M12 9.2V13l2.6 1.6M7.3 19.2l-1.3 1.8M16.7 19.2l1.3 1.8"/>'
     '<path d="M3.8 7.2a3 3 0 0 1 4-3.4M20.2 7.2a3 3 0 0 0-4-3.4"/>',
     '<b>1 hour</b> behind Prague: 12:00 there is 11:00 here'),
    # a card with a euro coin on top
    ('<rect class="f" x="2.5" y="5" width="14.5" height="10" rx="1.6"/><path d="M2.5 8.3h14.5M5 12.2h3.5"/>'
     '<circle class="f bg" cx="16.5" cy="15.5" r="5"/><path d="M18.3 13.5a2.7 2.7 0 1 0 0 4M14 14.9h3.2M14 16.2h3.2"/>',
     'Cards are mostly accepted &ndash; bring <b>some euros</b>, just in case'),
    # a phone sending a little signal
    ('<rect class="f" x="5" y="3" width="10" height="18" rx="2.4"/><path d="M8.8 18h2.4"/>'
     '<path d="M17.8 9.2a4.2 4.2 0 0 1 0 5.6M20.2 7a7.5 7.5 0 0 1 0 10"/>',
     'Calls and <b>data like at home</b> &ndash; no roaming in the EU'),
    # a passport
    ('<path class="f" d="M5.5 3.5h11.2c1 0 1.8.8 1.8 1.8v13.4c0 1-.8 1.8-1.8 1.8H5.5Z"/><path d="M8 3.5v17"/>'
     '<circle cx="13.3" cy="10.3" r="2.8"/><path d="M10.5 10.3h5.6M13.3 7.5c.8.8 1.2 1.7 1.2 2.8s-.4 2-1.2 2.8M11 16.3h4.6"/>',
     'From the EU: <b>ID card</b> &ndash; from elsewhere: <b>passport</b>'),
    # a little old car, from the side
    ('<path class="f" d="M2.5 16.5v-2.8c0-.8.5-1.4 1.2-1.6l3-.8 2.5-3.3c.4-.5 1-.8 1.6-.8h4.3c.7 0 1.3.3 1.7.9l2.4 3.3 1.6.4c.8.2 1.2.8 1.2 1.6v3.1Z"/>'
     '<path d="M8.7 11.2h9.1M13 8v3.2"/><circle class="f bg" cx="7.2" cy="16.8" r="2"/><circle class="f bg" cx="16.8" cy="16.8" r="2"/>',
     'Driving: max <b>0.5&nbsp;&permil;</b> &ndash; about 2&ndash;3 small beers'),
    # an old telephone handset
    ('<path class="f" d="M8.4 3.5 6 4.2C4.4 4.7 3.6 6.4 4.1 8a17 17 0 0 0 11.9 11.9c1.6.5 3.3-.3 3.8-1.9l.7-2.4-4.4-2.2-1.9 1.9a11 11 0 0 1-5.6-5.6l1.9-1.9Z"/>'
     '<path d="M14.5 3.8a6 6 0 0 1 5.7 5.7M14.2 6.7a3 3 0 0 1 3.1 3.1"/>',
     'Emergency: <b>112</b>, same as at home'),
]

# Footer: the orange tree from the village, drawn in the same ink and wash.
# Its oranges keep their own colour (class "o").
TREE = (
    '<path class="f" d="M24 5.5c-5.2 0-9 3.4-9.8 7.6-3.9.8-6.4 4-5.7 7.8.7 3.8 4.4 6.2 8.4 5.6 1.9 2.4 4.8 3.2 7.4 2.3 2.7 1.3 6.3.6 8.4-1.8 3.9-.2 6.6-3.3 6.4-7.1-.2-3.5-2.8-6.1-6-6.6C32.4 8.9 28.7 5.5 24 5.5Z"/>'
    '<path d="M24 29v13.5M24 35.5l-4.2-3.4M24.2 33.4l3.6-3.6M15 42.5h18"/>'
    '<circle class="o" cx="17" cy="16.5" r="1.9"/><circle class="o" cx="28.5" cy="12.5" r="1.9"/>'
    '<circle class="o" cx="33" cy="21" r="1.9"/><circle class="o" cx="21.5" cy="23" r="1.9"/><circle class="o" cx="12.5" cy="22.5" r="1.9"/>'
)

_FILLED = re.compile(r'<(path|circle|rect|ellipse)\b([^>]*?)\bclass="f( bg)?"([^>]*)/>')


def svg(paths, cls="ico", box=24):
    """Two layers: the offset wash under the pen line (see the docstring)."""
    wash = "".join(f'<{m[0]}{m[1]}{m[3]}/>' for m in _FILLED.findall(paths))
    nudge = box / 24
    return (f'<svg class="{cls}" viewBox="0 0 {box} {box}" aria-hidden="true">'
            f'<g class="wash" transform="translate({1.8 * nudge:g} {1.5 * nudge:g})">{wash}</g>'
            f'<g class="line">{paths}</g></svg>')


def strip_html():
    rows = [f'        <li><a href="{slug}.html">{svg(STRIP[slug])}<span>{label}</span></a></li>'
            for slug, label in STRIP_LABELS]
    return "\n".join(rows)
