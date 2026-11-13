"""The three houses of the village as a small flat drawing, for the footer.

Same houses as the painting, simplified: whitewashed walls, each house's
colour on the corners, the base band (barra) and the cornice, terracotta
roofs with scalloped tile ends, chimneys with coloured caps, doors and windows
in coloured frames, the orange tree, the street lamp and the bougainvillea.

  from village_mini import village_svg
"""

WALL, ROOF, ROOF_LINE, TILE_END = "#fffdf8", "#e2683a", "#c4522a", "#f08b5e"
GLASS, DOOR, GREEN_DOOR = "#9dbccb", "#b65b2b", "#6f9a3b"
EAVE, GROUND = 44, 90

HOUSES = [  # x0, x1, ridge x, ridge y, colour, door x, door colour, window xs, chimney x
    (10, 110, 58, 30, "#2f6ac2", 20, DOOR, [60], 24),
    (110, 220, 164, 28, "#f2b705", 154, DOOR, [124, 192], 178),
    (220, 322, 270, 30, "#ec6a4c", 236, GREEN_DOOR, [274], 296),
]


def rect(x, y, w, h, fill):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}"/>'


def roof(x0, x1, xm, ym):
    a, b = x0 - 5, x1 + 5
    out = [f'<path d="M{a} {EAVE}L{xm} {ym}L{b} {EAVE}Z" fill="{ROOF}"/>']
    for y in (EAVE - 5, EAVE - 10):                      # tile rows, parallel to the eave
        t = (EAVE - y) / (EAVE - ym)
        out.append(f'<path d="M{a + t * (xm - a):.1f} {y}H{b - t * (b - xm):.1f}" stroke="{ROOF_LINE}" stroke-width=".8"/>')
    arcs = "".join("a2 2 0 0 0 4 0" for _ in range(int((b - a) // 4)))
    out.append(f'<path d="M{a} {EAVE}{arcs}" fill="{TILE_END}"/>')   # scalloped tile ends
    return "".join(out)


def window(x, colour):
    y = 54
    s = rect(x, y, 18, 18, colour) + rect(x + 2, y + 2, 14, 14, WALL)
    for dx in (3.5, 9.5):
        for dy in (3.5, 9.5):
            s += rect(x + dx, y + dy, 5, 5, GLASS)
    return s


def house(x0, x1, xm, ym, colour, door_x, door_colour, windows, chimney_x):
    w = x1 - x0
    s = (f'<rect x="{chimney_x}" y="{ym - 6}" width="10" height="18" fill="#f1ebe1" stroke="#ddd3c2" stroke-width=".8"/>'
         + rect(chimney_x - 2, ym - 9, 14, 4, colour))
    s += rect(x0, EAVE, w, GROUND - EAVE, WALL)
    s += rect(x0, GROUND - 8, w, 8, colour)                          # barra
    s += rect(x0, EAVE, 4, GROUND - EAVE, colour) + rect(x1 - 4, EAVE, 4, GROUND - EAVE, colour)
    s += rect(x0, EAVE, w, 3, colour)                                # cornice
    s += roof(x0, x1, xm, ym)
    s += rect(door_x, 58, 20, GROUND - 58, colour) + rect(door_x + 3, 61, 14, GROUND - 61, door_colour)
    for x in windows:
        s += window(x, colour)
    return s


def village_svg(cls="village"):
    parts = [house(*h) for h in HOUSES]
    # flower box under the blue window
    parts.append(rect(60, 72, 18, 3, "#c9773d") + "".join(
        f'<circle cx="{x}" cy="70.5" r="1.6" fill="#e2445b"/>' for x in (63, 67.5, 72, 76)))
    # orange tree between the blue and the yellow house
    parts.append('<path d="M111 90c0-10 1-18 .5-30" stroke="#8a5a33" stroke-width="2.4" fill="none" stroke-linecap="round"/>')
    parts.append("".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#5f9a36"/>' for x, y, r in ((105, 55, 6.5), (117, 54, 6.5), (111, 48, 7), (104, 49, 5), (118, 47, 5))))
    parts.append("".join(f'<circle cx="{x}" cy="{y}" r="1.7" fill="#f28a1e"/>' for x, y in ((103, 52), (111, 45), (117, 50), (119, 56), (107, 58))))
    # street lamp in front of the yellow house
    parts.append(rect(206.2, 58, 1.6, 32, "#3a3f4a") + '<path d="M203.5 50h7l-1 8h-5Z" fill="#f6e7b5" stroke="#3a3f4a" stroke-width="1"/>'
                 + rect(203, 48, 8, 2, "#3a3f4a"))
    # bougainvillea over the coral house, in its pot
    parts.append("".join(f'<circle cx="{x}" cy="{y}" r="2.6" fill="{c}"/>' for x, y, c in (
        (300, 48, "#5f9a36"), (306, 46, "#e2407c"), (311, 49, "#e2407c"), (316, 46, "#5f9a36"),
        (303, 52, "#e2407c"), (309, 53, "#5f9a36"), (314, 52, "#e2407c"), (318, 50, "#e2407c"))))
    parts.append('<path d="M314 56c-2 8 2 14-1 26" stroke="#8a5a33" stroke-width="1.2" fill="none"/>'
                 '<path d="M308 82h10l-1.5 8h-7Z" fill="#c9773d"/>')
    parts.append(f'<path d="M2 {GROUND}h328" stroke="#d8ccb6" stroke-width="1.2"/>')
    return (f'<svg class="{cls}" viewBox="0 0 332 92" aria-hidden="true">'
            + "".join(parts) + "</svg>")
