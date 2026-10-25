"""
Business facts used across the whole site. Edit here, then run:
    python3 _build/build.py

Anything set to None (or an empty list) is HIDDEN on the live site until you
fill it in — so customers never see placeholders. Search this file for
"FILL" to see everything still waiting for real information.
"""
from urllib.parse import quote

# ---- Domain -------------------------------------------------------------
# The live domain (no trailing slash). Canonical URLs, sitemap and
# structured data all use this. When thomaslocksmith.sg goes live, also add
# a file called CNAME (containing: thomaslocksmith.sg) to the repo root and
# set BASE_PATH = "/".
SITE = "https://thomaslocksmith.sg"
# Path the site is served from right now (only used by the 404 page).
BASE_PATH = "/uncle-thomas-locksmith/"

# Bump this after changing script.js so browsers fetch the new file.
ASSET_VERSION = "3"

# ---- Business -----------------------------------------------------------
NAME = "Uncle Thomas Locksmith"
SLOGAN = "Unlocking your needs since 1998"
FOUNDED = 1998
YEARS = 2026 - FOUNDED            # shown as "28 years" etc.
PHONE = "9224 9224"
PHONE_E164 = "+6592249224"
WA_MESSAGE = "Hi Uncle Thomas, I need a locksmith. My location is: ___ . Lock type/photo: ___"
WA_LINK = "https://wa.me/6592249224?text=" + quote(WA_MESSAGE)
WA_MESSAGE_ZH = "你好 Uncle Thomas，我需要锁匠。我的位置：___ 。锁的类型/照片：___"
WA_LINK_ZH = "https://wa.me/6592249224?text=" + quote(WA_MESSAGE_ZH)

# FILL: business email (e.g. hello@thomaslocksmith.sg). None = no email shown anywhere.
EMAIL = None
# FILL: full Google Maps URL of the business profile
#   (Google Maps → your business → Share → Copy link, or the https://www.google.com/maps/place/... URL).
#   Until filled, the short share link below is used.
GOOGLE_MAPS_URL = None
GOOGLE_SHARE_LINK = "https://share.google/pcY4Ywtr5iTrQpRfk"
GOOGLE_PROFILE = GOOGLE_MAPS_URL or GOOGLE_SHARE_LINK
# FILL: ACRA UEN (e.g. "53XXXXXXXA"). None = not shown.
UEN = None
# FILL: Google Analytics 4 Measurement ID (e.g. "G-ABC123XYZ"). None = analytics off.
GA4_ID = None

# Add Facebook / Instagram / Carousell / directory profile URLs here as you create them.
SAME_AS = [GOOGLE_PROFILE]
LANGUAGES = ["English"]   # FILL: add "Chinese", "Malay" etc. if Uncle Thomas or the team speak them

# Title style for homepage + service pages:
#   "KEEP PRICE"           -> "24/7 Locksmith Singapore from S$80 | Uncle Thomas Since 1998"
#   "LEAD WITH EXPERIENCE" -> "24/7 Locksmith Singapore | Since 1998 · US-Trained Safesmith"
TITLE_STYLE = "KEEP PRICE"

DESCRIPTION = ("24/7 emergency locksmith in Singapore since 1998, led by Uncle Thomas — a US-trained safesmith. "
               "Door lockouts, digital lock opening and installation, safe opening, car lockouts, lock and "
               "letterbox replacement, islandwide.")

DIGITAL_LOCK_BRANDS = ["Samsung", "Yale", "Philips", "Igloohome", "Solity", "Gateman", "Kaadas",
                       "Häfele", "Aqara", "Schlage"]
# Brands that get their own page at /digital-lock-opening/<brand>/
# FILL: confirm this list with Uncle Thomas (only brands he handles).
BRAND_PAGES = ["Samsung", "Yale", "Philips", "Igloohome", "Gateman"]

# ---- Reviews ------------------------------------------------------------
# FILL: up to 3 REAL Google reviews. The reviews section stays hidden until at
# least one is added. Copy them word for word (shorten with "…" if needed).
# Example:
#   dict(text="Locked out at 2am and he came quickly…", name="Sarah", estate="Tampines", month="Oct 2026"),
REVIEWS = [
]

# ---- Photos -------------------------------------------------------------
# FILL: real photos. Put the original JPG/PNG in assets/photos/ and write the
# file name below. The build makes fast WebP versions automatically and the
# photo appears on the site. None = slot hidden.
PHOTOS = {
    # key: (file name or None, alt text, caption)
    "hero":       (None, "Uncle Thomas, Singapore locksmith, with his toolbox", "Uncle Thomas — locksmith since 1998"),
    "about_portrait": (None, "Portrait of Uncle Thomas, master locksmith and safesmith", "Uncle Thomas"),
    "about_van":  (None, "Uncle Thomas Locksmith service van", "Our van — on the road 24/7"),
    "about_tools": (None, "Locksmith tools used by Uncle Thomas", "The tools of the trade"),
    "emergency-locksmith/":       (None, "Locksmith opening an HDB main door without damage", "A damage-free HDB lockout job"),
    "digital-lock-opening/":      (None, "Digital lock being opened by a locksmith", "Opening a faulty digital lock"),
    "digital-lock-installation/": (None, "Newly installed digital lock on an HDB main door", "A finished digital lock installation"),
    "safe-opening/":              (None, "Uncle Thomas opening a safe", "Safe opening job"),
    "car-locksmith/":             (None, "Car door being unlocked with non-destructive tools", "Non-destructive car unlocking"),
    "lock-replacement/":          (None, "Before and after: old and new HDB door lock", "Before and after lock replacement"),
    "letterbox-lock-replacement/": (None, "New lock fitted to an HDB letterbox", "Letterbox lock replaced"),
    "commercial-locksmith/":      (None, "Office door lock being changed", "Commercial lock change"),
}

# ---- Recent jobs per town ------------------------------------------------
# FILL: real job notes, e.g. "toa-payoh": ["Oct 2026 — HDB main door lockout at Lorong 4, opened damage-free"]
# A town's "Recent jobs" section stays hidden until it has at least one entry.
RECENT_JOBS = {
}

# ---- Prices -------------------------------------------------------------
# (label, page path or None, "from" price in S$ (int) or text, short note)
# FILL / CONFIRM: Uncle Thomas must be willing to honour every "from" price.
PRICES = [
    ("Home / office lockout (9am–6pm)", "emergency-locksmith/", 80, "Damage-free entry where possible"),
    ("Lockout after hours, weekends & public holidays", "emergency-locksmith/", 120, "24/7, islandwide"),
    ("Digital lock emergency opening", "digital-lock-opening/", 150, "All brands"),
    ("Digital lock installation (labour)", "digital-lock-installation/", 120, "Lock supplied by you or us"),
    ("Car lockout (non-destructive)", "car-locksmith/", 100, "All makes and models"),
    ("Main door / gate lock replacement (supply + install)", "lock-replacement/", 100, "Warranty included"),
    ("Letterbox lock replacement", "letterbox-lock-replacement/", 60, "HDB & condo letterboxes"),
    ("Safe opening", "safe-opening/", "Quote on request", "Depends on safe type"),
]
# One consistent framing for schema priceRange: the lowest "from" price.
LOWEST_PRICE = min(p[2] for p in PRICES if isinstance(p[2], int))
PRICE_RANGE = f"From S${LOWEST_PRICE}"


def price(path):
    """'from' price for a page path, e.g. price('car-locksmith/') -> 'S$100'; None if quoted."""
    for label, p, pr, note in PRICES:
        if p == path and isinstance(pr, int):
            return f"S${pr}"
    return None


TOKENS = {
    "PHONE": PHONE,
    "YEARS": str(YEARS),
    "FOUNDED": str(FOUNDED),
    "P_LOCKOUT": "S$80",
    "P_AFTERHOURS": "S$120",
    "P_DIGITAL_OPEN": "S$150",
    "P_DIGITAL_INSTALL": "S$120",
    "P_CAR": "S$100",
    "P_REPLACE": "S$100",
    "P_LETTERBOX": "S$60",
    "P_LOWEST": f"S${LOWEST_PRICE}",
}
