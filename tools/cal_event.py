"""The wedding weekend as a calendar event: the .ics file and the links.

make_pages.py writes assets/marek-paulo-wedding.ics (Apple Calendar,
Outlook desktop, most phones) and puts the Google and Outlook.com links on
the Program page. Times are UTC: Portugal is on UTC+1 in early October,
so check-in 14:00 is 13:00Z and check-out 12:00 is 11:00Z.
"""
from urllib.parse import quote, urlencode

SITE = "https://marekandpaulo.com/"
ICS_PATH = "assets/marek-paulo-wedding.ics"

TITLE = "Marek & Paulo's wedding"
START, END = "20271001T130000Z", "20271003T110000Z"
START_ISO, END_ISO = "2027-10-01T13:00:00Z", "2027-10-03T11:00:00Z"
LOCATION = "Hotel Rural Quinta do Marco, Sítio do Marco 632A, 8800-164 Santa Catarina da Fonte do Bispo, Tavira, Portugal"
DETAILS = ("Three days in Tavira, Algarve. Check in from 14:00 on Friday, "
           "check out by 12:00 on Sunday. Program, stay and travel: " + SITE)


def _esc(text):
    return text.replace("\\", "\\\\").replace(";", "\\;").replace(",", "\\,").replace("\n", "\\n")


def _fold(line):
    """iCalendar lines are at most 75 octets; longer ones continue after CRLF + space."""
    out, cur = [], b""
    for ch in line:
        b = ch.encode("utf-8")
        if len(cur) + len(b) > (75 if not out else 74):
            out.append(cur)
            cur = b""
        cur += b
    out.append(cur)
    return b"\r\n ".join(out)


def ics():
    lines = [
        "BEGIN:VCALENDAR",
        "VERSION:2.0",
        "PRODID:-//Marek & Paulo//Wedding//EN",
        "CALSCALE:GREGORIAN",
        "METHOD:PUBLISH",
        "BEGIN:VEVENT",
        "UID:wedding-20271001@hoffmma5.github.io",
        "DTSTAMP:20261114T120000Z",
        f"DTSTART:{START}",
        f"DTEND:{END}",
        f"SUMMARY:{_esc(TITLE)}",
        f"LOCATION:{_esc(LOCATION)}",
        f"DESCRIPTION:{_esc(DETAILS)}",
        f"URL:{SITE}",
        "BEGIN:VALARM",
        "ACTION:DISPLAY",
        f"DESCRIPTION:{_esc(TITLE)}",
        "TRIGGER:-P7D",
        "END:VALARM",
        "END:VEVENT",
        "END:VCALENDAR",
    ]
    return b"\r\n".join(_fold(l) for l in lines) + b"\r\n"


def google_url():
    return "https://calendar.google.com/calendar/render?" + urlencode({
        "action": "TEMPLATE", "text": TITLE, "dates": f"{START}/{END}",
        "location": LOCATION, "details": DETAILS}, quote_via=quote)


def outlook_url():
    return "https://outlook.live.com/calendar/0/deeplink/compose?" + urlencode({
        "path": "/calendar/action/compose", "rru": "addevent", "subject": TITLE,
        "startdt": START_ISO, "enddt": END_ISO, "location": LOCATION, "body": DETAILS}, quote_via=quote)


def write():
    open(ICS_PATH, "wb").write(ics())
