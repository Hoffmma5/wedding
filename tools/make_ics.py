"""Save the date: the calendar file guests can add (Apple Calendar, Outlook,
and anything else that opens .ics).

  out: assets/marek-paulo-wedding.ics

All-day, Friday 1 to Sunday 3 October 2027 (DTEND is the day after, as the
format wants). CRLF line endings and lines folded at 75 octets, per RFC 5545;
.gitattributes keeps git from rewriting the endings.
Run from the project root:  python tools/make_ics.py
"""

SITE = "https://hoffmma5.github.io/wedding/"

FIELDS = [
    ("BEGIN", "VCALENDAR"),
    ("VERSION", "2.0"),
    ("PRODID", "-//Marek & Paulo//Wedding//EN"),
    ("CALSCALE", "GREGORIAN"),
    ("METHOD", "PUBLISH"),
    ("BEGIN", "VEVENT"),
    ("UID", "marek-paulo-wedding-2027@hoffmma5.github.io"),
    ("DTSTAMP", "20261114T120000Z"),
    ("DTSTART;VALUE=DATE", "20271001"),
    ("DTEND;VALUE=DATE", "20271004"),
    ("SUMMARY", "Marek & Paulo’s wedding"),
    ("LOCATION", "Hotel Rural Quinta do Marco\\, Santa Catarina da Fonte do Bispo\\, Tavira\\, Portugal"),
    ("DESCRIPTION", "Three days in Tavira: welcome party (Friday)\\, the wedding (Saturday)\\, "
                    "farewell (Sunday). Everything else: " + SITE),
    ("URL", SITE),
    ("TRANSP", "TRANSPARENT"),
    ("END", "VEVENT"),
    ("END", "VCALENDAR"),
]


def fold(line):
    """Split a content line into 75-octet pieces, continuations starting with a space."""
    out, cur = [], b""
    for ch in line:
        b = ch.encode("utf-8")
        limit = 75 if not out else 74
        if len(cur) + len(b) > limit:
            out.append(cur)
            cur = b""
        cur += b
    out.append(cur)
    return b"\r\n ".join(out)


data = b"\r\n".join(fold(f"{k}:{v}") for k, v in FIELDS) + b"\r\n"
open("assets/marek-paulo-wedding.ics", "wb").write(data)
print("ics", len(data), "bytes")
