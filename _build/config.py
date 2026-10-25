"""
Business facts used across the whole site. Edit here, then run:
    python3 _build/build.py
"""

# ---- Domain -------------------------------------------------------------
# The live domain (no trailing slash). Canonical URLs, sitemap and
# structured data all use this. When thomaslocksmith.sg goes live, also add
# a file called CNAME (containing: thomaslocksmith.sg) to the repo root and
# set BASE_PATH = "/".
SITE = "https://thomaslocksmith.sg"
# Path the site is served from right now (only used by the 404 page).
BASE_PATH = "/uncle-thomas-locksmith/"

# Bump this after changing styles.css or script.js so browsers fetch the new file.
ASSET_VERSION = "2"

# ---- Business -----------------------------------------------------------
NAME = "Uncle Thomas Locksmith"
SLOGAN = "Unlocking your needs since 1998"
FOUNDED = 1998
YEARS = 2026 - FOUNDED            # shown as "28 years" etc.
PHONE = "9224 9224"
PHONE_E164 = "+6592249224"
WA_LINK = "https://wa.me/6592249224?text=Hi%20Uncle%20Thomas%2C%20I%20need%20a%20locksmith."
EMAIL = "Leongjezvier@gmail.com"
GOOGLE_PROFILE = "https://share.google/pcY4Ywtr5iTrQpRfk"
# Add Facebook / Instagram / Carousell / directory profile URLs here as you create them.
SAME_AS = [GOOGLE_PROFILE]
LANGUAGES = ["English", "Chinese"]   # OWNER TO CONFIRM (add Malay/Hokkien etc. if spoken)

DESCRIPTION = ("24/7 emergency locksmith in Singapore since 1998, led by Uncle Thomas — a US-trained safesmith. "
               "Door lockouts, digital lock opening and installation, safe opening, car lockouts, lock and "
               "letterbox replacement, islandwide.")

DIGITAL_LOCK_BRANDS = ["Samsung", "Yale", "Philips", "Igloohome", "Solity", "Gateman", "Kaadas",
                       "Häfele", "Aqara", "Schlage"]

# ---- Prices -------------------------------------------------------------
# (label, page path or None, "from" price in S$ (int) or text, short note)
# OWNER TO CONFIRM: Uncle Thomas must be willing to honour every "from" price.
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

def price(path):
    """'from' price for a page path, e.g. price('car-locksmith/') -> 'S$100'."""
    for label, p, pr, note in PRICES:
        if p == path and isinstance(pr, int):
            return f"S${pr}"
    return "Quote on request"

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
}
