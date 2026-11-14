"""Line icons with a little character, shared by the pages.

24 x 24, drawn with a 1.6 stroke in currentColor. Shapes with class "f" also
get a soft tint fill (--tint, set where the icon is used) and "s" shapes are
solid currentColor (eyes, hearts). index.html carries a copy of the strip
icons; tools/make_pages.py uses this file directly.
"""

STRIP = {
    # clinking glasses
    "program": '<g transform="rotate(6 8 19)"><path class="f" d="M5.5 3.5h5l-.8 5.6a1.7 1.7 0 0 1-3.4 0Z"/><path d="M8 10.8V19M5.8 19h4.4"/></g>'
               '<g transform="rotate(-6 16 19)"><path class="f" d="M13.5 3.5h5l-.8 5.6a1.7 1.7 0 0 1-3.4 0Z"/><path d="M16 10.8V19M13.8 19h4.4"/></g>'
               '<path d="M12 .8v1.8M9.6 1.5l1 1.1M14.4 1.5l-1 1.1"/>',
    # a little Algarve house: low tiled roof, chimney with its cap, door, window
    "accommodation": '<path class="f" d="M2.5 11 12 7l9.5 4Z"/><path d="M4 11v9.5h16V11M16 9.3V5.5h2.6v4.8M15.4 5.5h3.8M8 20.5V16h3v4.5M14 14h3v2.6h-3Z"/>',
    # plane, nose to the top right
    "travel": '<path class="f" transform="rotate(45 12 12)" d="M12 2.5c.9 0 1.4 1 1.4 2.4v4.4l7.1 4.2v2l-7.1-2.1v4.1l2 1.6v1.6L12 19.8l-3.4.9v-1.6l2-1.6v-4.1l-7.1 2.1v-2l7.1-4.2V4.9c0-1.4.5-2.4 1.4-2.4Z"/>',
    # sun with long and short rays
    "weather": '<circle class="f" cx="12" cy="12" r="4.4"/><path d="M12 1.8v3M12 19.2v3M1.8 12h3M19.2 12h3M5.4 5.4l1.4 1.4M17.2 17.2l1.4 1.4M5.4 18.6l1.4-1.4M17.2 6.8l1.4-1.4"/>',
    # a sardine
    "location": '<path class="f" d="M2.5 12c3.2-4.2 9.6-5.2 14.2-1.6L20.5 7.5v9l-3.8-2.9C12.1 17.2 5.7 16.2 2.5 12Z"/><circle class="s" cx="6.3" cy="11.2" r=".9"/><path d="M9 9.6c.9 1.5.9 3.3 0 4.8"/><circle class="s" cx="12" cy="11.4" r=".6"/><circle class="s" cx="14.2" cy="11.6" r=".6"/>',
    # the world, with a heart
    "map": '<circle class="f" cx="10.5" cy="13" r="7.5"/><path d="M3 13h15M10.5 5.5c2.1 2.2 3.1 4.7 3.1 7.5s-1 5.3-3.1 7.5c-2.1-2.2-3.1-4.7-3.1-7.5s1-5.3 3.1-7.5Z"/>'
           '<path class="s" d="M18.5 10.2s-3.4-2-3.4-4.3a1.8 1.8 0 0 1 3.4-.9 1.8 1.8 0 0 1 3.4.9c0 2.3-3.4 4.3-3.4 4.3Z"/>',
}

FACILITIES = [
    ("Heated pool", '<path class="f" d="M3 15.8c1.5 1.2 3 1.2 4.5 0s3-1.2 4.5 0 3 1.2 4.5 0 3-1.2 4.5 0V20.5H3Z"/>'
                    '<path d="M9 15V5.8a1.6 1.6 0 0 0-3.2 0M15.2 15V5.8a1.6 1.6 0 0 0-3.2 0M9 8.3h6.2M9 11.5h6.2M19.5 3c-.9 1.1.9 2 0 3.2"/>'),
    ("Pool bar", '<path class="f" d="M4 5h12.5L10.3 12.5Z"/><path d="M10.3 12.5V20M7 20h6.6M12.5 9.5 17.8 2.5"/><circle cx="17.3" cy="5.3" r="2.6"/><path d="M17.3 2.7v5.2M14.7 5.3h5.2"/>'),
    ("Restaurant", '<circle class="f" cx="12" cy="12.5" r="5.2"/><circle cx="12" cy="12.5" r="3"/><path d="M2.8 3.5V8a1.6 1.6 0 0 0 3.2 0V3.5M4.4 3.5v17M21.2 20.5v-17c-1.7 1-2.6 3.2-2.6 6.4h2.6"/>'),
    ("Spa &amp; sauna", '<path class="f" d="M12 18.5c-3-2-4.4-5-3.8-9 2.6 1.5 3.8 4.5 3.8 9Zm0 0c3-2 4.4-5 3.8-9-2.6 1.5-3.8 4.5-3.8 9Zm0 0c-4 0-7-1.4-8.6-4 3.1-.6 6.1.8 8.6 4Zm0 0c4 0 7-1.4 8.6-4-3.1-.6-6.1.8-8.6 4Z"/>'
                        '<path d="M12 3c-.8 1 .8 1.8 0 2.8M4 21.5h16"/>'),
    ("Gym", '<path class="f" d="M5 7h3v10H5ZM16 7h3v10h-3Z"/><path d="M2.8 9.5H5v5H2.8ZM19 9.5h2.2v5H19ZM8 12h8"/>'),
    ("Playground", '<path class="f" d="M9 8c3.3 0 4.5 3 6.2 7s2.7 5.5 5.8 5.5V18c-1.9 0-2.9-1.4-4.4-4.8S12.6 8 9 8Z"/><path d="M4.5 20.5V8H9v12.5M4.5 11h4.5M4.5 14h4.5M4.5 17h4.5M3 20.5h18"/>'),
    # a sheep (the farm has donkeys, goats and peacocks too)
    ("Animal farm", '<path class="f" d="M8.2 9.3a2.6 2.6 0 0 1 4.4-1.5 2.7 2.7 0 0 1 4.7.6 2.5 2.5 0 0 1 1.9 4.3 2.4 2.4 0 0 1-2.2 3.6H9.5a2.5 2.5 0 0 1-1.9-4.2 2.4 2.4 0 0 1 .6-2.8Z"/>'
                    '<ellipse class="s" cx="5.6" cy="11" rx="1.9" ry="2.6" transform="rotate(-24 5.6 11)"/><path d="M4.4 8.9 2.6 8.4M10.5 16.3v3.7M15.5 16.3v3.7"/>'),
    ("Views to the sea", '<path class="f" d="M2.5 16.5c2.8-4.6 5.6-6.5 8.5-6.5s5 2 7 3.8 2.6 2.2 3.5 2.2v1.5H2.5Z"/><circle cx="17" cy="5.5" r="2.2"/>'
                         '<path d="M2.5 20.5c1.5 1 3 1 4.5 0s3-1 4.5 0 3 1 4.5 0 3-1 4.5 0"/>'),
]


def svg(paths, cls=""):
    c = f' class="{cls}"' if cls else ""
    return f'<svg{c} viewBox="0 0 24 24" aria-hidden="true">{paths}</svg>'


# Travel: "good to know", one icon and one short line each
TIPS = [
    # clock
    ('<circle class="f" cx="12" cy="12.5" r="8.5"/><path d="M12 7.5v5l3.2 2M9.5 2.5h5"/>',
     '<b>1 hour</b> behind Prague'),
    # coins
    ('<ellipse class="f" cx="9.5" cy="7" rx="5.5" ry="2.3"/><path d="M4 7v3.2c0 1.3 2.5 2.3 5.5 2.3s5.5-1 5.5-2.3V7"/>'
     '<ellipse class="f" cx="14.5" cy="15" rx="5.5" ry="2.3"/><path d="M9 15v3c0 1.3 2.5 2.3 5.5 2.3s5.5-1 5.5-2.3v-3"/>',
     'Cards work &ndash; bring <b>a few coins</b>'),
    # phone with signal
    ('<rect class="f" x="6.5" y="3" width="9" height="18" rx="2"/><path d="M10 17.8h2M18.2 7.2a5 5 0 0 1 0 6.6M20.6 4.8a8.5 8.5 0 0 1 0 11.4"/>',
     '<b>No roaming</b> in the EU'),
    # ID card
    ('<rect class="f" x="2.5" y="5" width="19" height="14" rx="2"/><circle cx="8" cy="11" r="2.2"/><path d="M4.8 16.2c.6-1.6 1.8-2.4 3.2-2.4s2.6.8 3.2 2.4M14 10h4.5M14 13.5h3"/>',
     'EU <b>ID card</b> is enough'),
    # speech bubble with a heart
    ('<path class="f" d="M4 5.5h16a1.5 1.5 0 0 1 1.5 1.5v9a1.5 1.5 0 0 1-1.5 1.5h-9l-4.5 3.5v-3.5H4A1.5 1.5 0 0 1 2.5 16V7A1.5 1.5 0 0 1 4 5.5Z"/>'
     '<path class="s" d="M12 14.6s-3.2-1.9-3.2-4a1.6 1.6 0 0 1 3.2-.7 1.6 1.6 0 0 1 3.2.7c0 2.1-3.2 4-3.2 4Z"/>',
     'Thank you: <i>obrigado</i>'),
    # a small glass of beer with foam
    ('<path class="f" d="M7 8.5h9l-1 12.5H8Z"/><path d="M6.5 8.5c-.8-2 .6-3.8 2.6-3.4.6-1.6 3-1.9 4-.5 1.6-.6 3.5.6 3.2 2.3-.1.6-.4 1.1-.8 1.6M16 11h1.6a1.8 1.8 0 0 1 1.8 1.8v2.4a1.8 1.8 0 0 1-1.8 1.8h-2"/>',
     'Small beer: <i>um imperial</i>'),
    # car
    ('<path class="f" d="M3.5 16.5v-4l2.2-4.8a1.6 1.6 0 0 1 1.5-1h9.6a1.6 1.6 0 0 1 1.5 1l2.2 4.8v4Z"/>'
     '<path d="M3.5 12.5h17M6.5 16.5v2.2M17.5 16.5v2.2"/><circle class="s" cx="7" cy="14.5" r=".9"/><circle class="s" cx="17" cy="14.5" r=".9"/>',
     'Driving: max <b>0.5&nbsp;&permil;</b>'),
    # first aid
    ('<circle class="f" cx="12" cy="12" r="9"/><path d="M12 7.5v9M7.5 12h9"/>',
     'Emergency: <b>112</b>'),
]
