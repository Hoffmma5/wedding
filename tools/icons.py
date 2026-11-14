"""The site's one icon family.

Drawn like the weather icons: 24 x 24, one thin line (1.35, set in CSS as
.ico), and a faint tint of the same colour inside closed shapes (class "f").
No solid parts. The colour comes from where the icon is used (currentColor).

index.html carries a copy of the STRIP icons; tools/make_pages.py uses this
file directly.
"""

STRIP = {
    # two glasses, clinking
    "program": '<path class="f" d="M5 3.5h5l-.7 5.4a1.8 1.8 0 0 1-3.6 0Z"/><path d="M7.5 10.6V19M5.4 19h4.2"/>'
               '<path class="f" d="M14 3.5h5l-.7 5.4a1.8 1.8 0 0 1-3.6 0Z"/><path d="M16.5 10.6V19M14.4 19h4.2M12 1.5v1.5"/>',
    # a little Algarve house with its chimney
    "accommodation": '<path class="f" d="M3.5 11 12 7.5l8.5 3.5v9.5h-17Z"/><path d="M16 9.6V5.8h2.4v4.8M8 20.5V16h3v4.5M14 14h3v2.5h-3Z"/>',
    # plane
    "travel": '<path class="f" transform="rotate(45 12 12)" d="M12 3c.8 0 1.3.9 1.3 2.2v4.3l6.7 4v1.8l-6.7-2v3.9l1.9 1.5v1.5L12 19.4l-3.2.8v-1.5l1.9-1.5v-3.9L4 15.3v-1.8l6.7-4V5.2C10.7 3.9 11.2 3 12 3Z"/>',
    # sun
    "weather": '<circle class="f" cx="12" cy="12" r="4"/><path d="M12 2.5v2M12 19.5v2M2.5 12h2M19.5 12h2M5.3 5.3l1.4 1.4M17.3 17.3l1.4 1.4M5.3 18.7l1.4-1.4M17.3 6.7l1.4-1.4"/>',
    # a sardine
    "location": '<path class="f" d="M2.5 12c3.2-4 9.5-5 14-1.6l3.8-2.9v9l-3.8-2.9c-4.5 3.4-10.8 2.4-14-1.6Z"/><circle cx="6.4" cy="11.3" r=".7"/><path d="M9 9.8c.8 1.4.8 3 0 4.4"/>',
    # the world
    "map": '<circle class="f" cx="12" cy="12" r="8.5"/><path d="M3.5 12h17M12 3.5c2.3 2.4 3.4 5.2 3.4 8.5s-1.1 6.1-3.4 8.5c-2.3-2.4-3.4-5.2-3.4-8.5S9.7 5.9 12 3.5Z"/>',
}

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
    # clock
    ('<circle class="f" cx="12" cy="12" r="8.5"/><path d="M12 7v5l3 2"/>',
     '<b>1 hour</b> behind Prague: 12:00 there is 11:00 here'),
    # a euro coin
    ('<circle class="f" cx="12" cy="12" r="8.5"/><path d="M15.2 8.6a4.3 4.3 0 1 0 0 6.8M7.5 10.8h5.5M7.5 13.2h5.5"/>',
     'Cards are mostly accepted &ndash; bring <b>some euros</b>, just in case'),
    # phone with signal
    ('<rect class="f" x="6.5" y="3" width="9" height="18" rx="2"/><path d="M10 17.8h2M18.2 7.6a5 5 0 0 1 0 6.3M20.6 5.2a8.4 8.4 0 0 1 0 11.1"/>',
     'Calls and <b>data like at home</b> &ndash; no roaming in the EU'),
    # passport
    ('<rect class="f" x="5" y="3" width="14" height="18" rx="1.6"/><circle cx="12" cy="10.5" r="3.2"/><path d="M8.8 10.5h6.4M12 7.3c1 .9 1.4 2 1.4 3.2s-.4 2.3-1.4 3.2M9 17h6"/>',
     'From the EU: <b>ID card</b> &ndash; from elsewhere: <b>passport</b>'),
    # car
    ('<path class="f" d="M3.5 16.5v-4l2.2-4.8a1.6 1.6 0 0 1 1.5-1h9.6a1.6 1.6 0 0 1 1.5 1l2.2 4.8v4Z"/><path d="M3.5 12.5h17M6.5 16.5v2.2M17.5 16.5v2.2"/><circle cx="7.2" cy="14.5" r=".8"/><circle cx="16.8" cy="14.5" r=".8"/>',
     'Driving: max <b>0.5&nbsp;&permil;</b> &ndash; about 2&ndash;3 small beers'),
    # phone handset
    ('<path class="f" d="M8.4 3.5 6 4.2C4.4 4.7 3.6 6.4 4.1 8a17 17 0 0 0 11.9 11.9c1.6.5 3.3-.3 3.8-1.9l.7-2.4-4.4-2.2-1.9 1.9a11 11 0 0 1-5.6-5.6l1.9-1.9Z"/>',
     'Emergency: <b>112</b>, same as at home'),
]


def svg(paths, cls="ico"):
    return f'<svg class="{cls}" viewBox="0 0 24 24" aria-hidden="true">{paths}</svg>'
