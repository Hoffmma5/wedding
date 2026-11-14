"""The site's one icon family: ink and wash.

Each icon is a pen sketch over a watercolour wash, like the notes in the
margin of a hand-painted invitation:

  - the line: 24 x 24, one thin stroke in the ink (--ink, set in CSS as
    .ico .line), roughened by the #ink-hand filter so it wobbles like a pen;
  - the wash: a soft blot of the accent behind it (.ico .wash), its edge
    frayed by the #ink-wash filter, never the same place twice.

No fills in the line, no solid parts. Both filters live in INK_DEFS, which
every page carries once, right after <body>. index.html carries a copy of
the GLANCE icons; tools/make_pages.py uses this file directly.
"""

# Once per page: the two filters (pen wobble, frayed wash)
INK_DEFS = (
    '<svg class="ink-defs" width="0" height="0" aria-hidden="true" focusable="false">'
    '<filter id="ink-hand" x="-10%" y="-10%" width="120%" height="120%">'
    '<feTurbulence type="fractalNoise" baseFrequency=".07" numOctaves="1" seed="7" result="n"/>'
    '<feDisplacementMap in="SourceGraphic" in2="n" scale="1.1" xChannelSelector="R" yChannelSelector="G"/>'
    '</filter>'
    '<filter id="ink-wash" x="-25%" y="-25%" width="150%" height="150%">'
    '<feTurbulence type="fractalNoise" baseFrequency=".16" numOctaves="3" seed="3" result="n"/>'
    '<feDisplacementMap in="SourceGraphic" in2="n" scale="5" xChannelSelector="R" yChannelSelector="G" result="d"/>'
    '<feGaussianBlur in="d" stdDeviation=".5"/>'
    '</filter>'
    '</svg>'
)

# Where the wash sits behind the line, in turn: a little off-centre, so it
# reads as a hand-laid blot, not a badge.
WASHES = [(13.6, 13.8, 8.4), (10.8, 13.2, 8.0), (12.8, 10.8, 8.2), (11.6, 12.8, 8.6)]

# Home: the weekend at a glance
GLANCE = {
    # a page torn from a calendar, the 1st ringed
    "when": '<path d="M5 6.5h14v13H5Z"/><path d="M5 10h14M9 4.5v3M15 4.5v3"/>'
            '<path d="M10.2 15.2c.4-1.5 2.9-1.9 3.7-.6.7 1.2-.4 2.6-2 2.6-1.3 0-2-1-1.7-2Z"/>',
    # a little Algarve house with its chimney
    "where": '<path d="M3.5 11 12 7l8.5 4v9.5h-17Z"/><path d="M16 9v-3.5h2.3v4.6M10 20.5V16h3.5v4.5"/>',
    # a suitcase
    "travel": '<path d="M4 8.5h16v11H4Z"/><path d="M9 8.5V6a1 1 0 0 1 1-1h4a1 1 0 0 1 1 1v2.5M8 8.5v11M16 8.5v11"/>',
}

FACILITIES = [
    ("Heated pool", '<path d="M3 17c1.5 1 3 1 4.5 0s3-1 4.5 0 3 1 4.5 0 3-1 4.5 0"/>'
                    '<path d="M3 20.5c1.5 1 3 1 4.5 0s3-1 4.5 0 3 1 4.5 0 3-1 4.5 0"/>'
                    '<path d="M9 15V6a1.6 1.6 0 0 0-3.2 0M15.2 15V6a1.6 1.6 0 0 0-3.2 0M9 8.5h6.2M9 11.7h6.2"/>'),
    ("Pool bar", '<path d="M4.5 5h12L10.5 12Z"/><path d="M10.5 12v8M7.3 20h6.4M12.5 9.6 17.5 3"/><circle cx="17.6" cy="5.2" r="2.2"/>'),
    ("Restaurant", '<circle cx="12.5" cy="12.5" r="5"/><path d="M3.5 3.5V8a1.5 1.5 0 0 0 3 0V3.5M5 3.5v17M21 20.5v-17c-1.6 1-2.5 3.1-2.5 6.2H21"/>'),
    ("Spa &amp; sauna", '<path d="M12 18.5c-2.8-2-4.1-4.8-3.6-8.6 2.5 1.4 3.6 4.3 3.6 8.6Zm0 0c2.8-2 4.1-4.8 3.6-8.6-2.5 1.4-3.6 4.3-3.6 8.6Z"/>'
                        '<path d="M12 18.5c-3.8 0-6.6-1.3-8.1-3.8 2.9-.6 5.7.7 8.1 3.8Zm0 0c3.8 0 6.6-1.3 8.1-3.8-2.9-.6-5.7.7-8.1 3.8ZM4 21.5h16"/>'),
    ("Gym", '<path d="M5.5 7.5h2.5v9H5.5ZM16 7.5h2.5v9H16Z"/><path d="M3.5 10v4M20.5 10v4M8 12h8"/>'),
    ("Playground", '<path d="M9 8c3.2 0 4.4 2.9 6 6.8s2.6 5.2 5.5 5.2"/><path d="M4.5 20.5V8H9v12.5M4.5 11h4.5M4.5 14h4.5M4.5 17h4.5M3 20.5h18"/>'),
    ("Animal farm", '<path d="M8.5 9.5a2.5 2.5 0 0 1 4.2-1.4 2.6 2.6 0 0 1 4.5.6 2.4 2.4 0 0 1 1.8 4.1 2.3 2.3 0 0 1-2.1 3.4H9.8a2.4 2.4 0 0 1-1.8-4 2.3 2.3 0 0 1 .5-2.7Z"/>'
                    '<ellipse cx="5.8" cy="11.2" rx="1.8" ry="2.5" transform="rotate(-24 5.8 11.2)"/><path d="M10.6 16.2v3.8M15.4 16.2v3.8"/>'),
    ("Views to the sea", '<path d="M2.5 16c2.8-4.3 5.6-6.2 8.5-6.2s5 1.9 7 3.6 2.6 2.1 3.5 2.1"/><circle cx="17" cy="5.8" r="2"/>'
                         '<path d="M2.5 20c1.5 1 3 1 4.5 0s3-1 4.5 0 3 1 4.5 0 3-1 4.5 0"/>'),
]

WEATHER = {
    # sun: a ring and short, uneven rays
    "sun": '<circle cx="12" cy="12" r="4"/><path d="M12 3v2M12 19v2M3 12h2M19 12h2M5.6 5.6l1.4 1.4M17 17l1.4 1.4M5.6 18.4 7 17M17 7l1.4-1.4"/>',
    "moon": '<path d="M19 14.5A7.5 7.5 0 0 1 9.5 5a7.5 7.5 0 1 0 9.5 9.5Z"/><path d="M17 4.5v2M16 5.5h2"/>',
    "rain": '<path d="M7 15a4 4 0 0 1-.6-8A5.5 5.5 0 0 1 17 8a3.5 3.5 0 0 1 .5 7H7Z"/><path d="M9 18l-1 2.5M13 18l-1 2.5M17 18l-1 2.5"/>',
}

# Travel: "good to know", one icon and one short line each
TIPS = [
    # a pocket watch
    ('<circle cx="12" cy="13" r="7.5"/><path d="M12 9.5V13l2.5 1.6M10.5 3.5h3M12 3.5v2"/>',
     '<b>1 hour</b> behind Prague: 12:00 there is 11:00 here'),
    # two coins, the front one with a euro
    ('<circle cx="14.5" cy="13.5" r="6.5"/><path d="M8.6 16.2A6.5 6.5 0 1 1 15.6 6.6"/>'
     '<path d="M17 11.2a2.8 2.8 0 1 0 0 4.6M12.2 12.6h3.4M12.2 14.4h3.4"/>',
     'Cards are mostly accepted &ndash; bring <b>some euros</b>, just in case'),
    # a phone with a little wave of signal
    ('<path d="M7 3.5h8.5a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H7a1 1 0 0 1-1-1v-15a1 1 0 0 1 1-1Z"/><path d="M10.2 17.8h2.1M19 8.2a4.6 4.6 0 0 1 0 5.6M21.2 6a8 8 0 0 1 0 10"/>',
     'Calls and <b>data like at home</b> &ndash; no roaming in the EU'),
    # a passport with the globe on its cover
    ('<path d="M6 3.5h11.5a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6Z"/><circle cx="12" cy="10.5" r="3.2"/><path d="M8.8 10.5h6.4M12 7.3c1 .9 1.4 2 1.4 3.2s-.4 2.3-1.4 3.2M9.5 17h5"/>',
     'From the EU: <b>ID card</b> &ndash; from elsewhere: <b>passport</b>'),
    # a little old car, side on
    ('<path d="M3 16h1.8M9.3 16h5.4M19.2 16H21v-2.6c0-.8-.5-1.4-1.3-1.6l-2.9-.7-2.4-2.9a1.8 1.8 0 0 0-1.4-.7H8.6a1.8 1.8 0 0 0-1.5.8L5.3 11 4 11.5a1.5 1.5 0 0 0-1 1.4V16"/>'
     '<circle cx="7" cy="16.4" r="2"/><circle cx="17" cy="16.4" r="2"/><path d="M7.8 11h8.6M11.5 8.2V11"/>',
     'Driving: max <b>0.5&nbsp;&permil;</b> &ndash; about 2&ndash;3 small beers'),
    # an old telephone handset
    ('<path d="M8.4 3.5 6 4.2C4.4 4.7 3.6 6.4 4.1 8a17 17 0 0 0 11.9 11.9c1.6.5 3.3-.3 3.8-1.9l.7-2.4-4.4-2.2-1.9 1.9a11 11 0 0 1-5.6-5.6l1.9-1.9Z"/>',
     'Emergency: <b>112</b>, same as at home'),
]

_n = [0]


def svg(paths, cls="ico"):
    """One icon: a frayed wash of the accent, then the pen line on top."""
    x, y, r = WASHES[_n[0] % len(WASHES)]
    _n[0] += 1
    return (f'<svg class="{cls}" viewBox="0 0 24 24" aria-hidden="true">'
            f'<circle class="wash" cx="{x}" cy="{y}" r="{r}"/>'
            f'<g class="line">{paths}</g></svg>')


if __name__ == "__main__":
    # print the GLANCE icons for pasting into index.html
    for k, v in GLANCE.items():
        print(k, svg(v))
