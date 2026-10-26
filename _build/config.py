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
# structured data all use this. Hosted on Cloudflare Pages; www. redirects
# here via a Cloudflare redirect rule.
SITE = "https://singapore-locksmiths.com"
# Path the site is served from (only used by the 404 page).
BASE_PATH = "/"

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

# FILL: business email (e.g. info@singapore-locksmiths.com). None = no email shown anywhere.
EMAIL = None
# FILL: full Google Maps URL of the business profile
#   (Google Maps → your business → Share → Copy link, or the https://www.google.com/maps/place/... URL).
#   Until filled, the short share link below is used.
GOOGLE_MAPS_URL = "https://maps.google.com/?cid=4145225534861484330"
GOOGLE_SHARE_LINK = "https://share.google/pcY4Ywtr5iTrQpRfk"
GOOGLE_PROFILE = GOOGLE_MAPS_URL or GOOGLE_SHARE_LINK
# ACRA registration (sole proprietorship, registered 21 Feb 1998). Shown in the footer + schema.
UEN = "52862311K"
LEGAL_NAME = "Thomas Locksmith"
# Other names customers and listings know the business by (Google Business Profile = "Singapore Locksmith").
ALT_NAMES = ["Thomas Locksmith", "Singapore Locksmith"]
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

DIGITAL_LOCK_BRANDS = ["Samsung", "Yale", "Philips", "Igloohome", "Kaadas", "Solity", "Gateman", "Häfele",
                       "Aqara", "Xiaomi", "Lenovo", "Schlage", "Epic", "Milre", "Dessmann", "Lockin", "Ezviz"]
# Digital / smart lock brands that get their own page at /digital-lock-opening/<brand>/
BRAND_PAGES = ["Samsung", "Yale", "Philips", "Igloohome", "Gateman", "Kaadas", "Solity", "Häfele", "Aqara", "Xiaomi", "Lenovo"]

# Car brands. Owner: Uncle Thomas opens and clones fobs for all makes EXCEPT Tesla — so Tesla is never listed.
# CAR_BRAND_PAGES get their own page at /car-locksmith/<brand>/ (content in _build/cars.py).
CAR_BRAND_PAGES = ["Toyota", "Honda", "Mercedes-Benz", "BMW", "Audi", "Volkswagen", "Mazda", "Lexus",
                   "Land Rover", "Hyundai", "Kia", "Nissan", "Porsche", "Volvo", "Mitsubishi", "Subaru"]
CAR_BRANDS_MORE = ["BYD", "MG", "Mini", "Peugeot", "Skoda", "Suzuki", "Ford", "Jaguar", "Jeep", "Renault",
                   "Citroën", "Opel", "Infiniti", "Alfa Romeo", "Maserati", "Bentley", "Ferrari", "Lamborghini",
                   "Rolls-Royce", "Chevrolet", "Cupra", "Polestar"]

# Real jobs per brand, shown as "Recent job" on that brand's page (car or lock).
# FILL over time with REAL jobs only, e.g. "Kaadas": ["Oct 2026, Punggol: gate lock batteries flat, opened in 20 minutes."]
BRAND_JOBS = {
}

# Safe brands mentioned on the safe opening page (Uncle Thomas opens all makes).
SAFE_BRANDS = ["Bumil", "Chubb", "Glory", "Uchida", "Eagle", "Phoenix", "Sentry", "Yale", "Lion", "Diplomat",
               "Gunnebo", "Kokuyo", "Kaba", "Sargent & Greenleaf"]

# ---- Google rating ------------------------------------------------------
# Shown on the homepage first screen. _build/rating.json (written daily by the
# "Update Google rating" GitHub Action) overrides these when it exists.
# FILL: current Google rating (e.g. 4.6) and review count (e.g. 34). None = badge hidden.
GOOGLE_RATING = 4.6
GOOGLE_REVIEW_COUNT = 34
try:
    import json as _json, os as _os
    _rf = _os.path.join(_os.path.dirname(__file__), "rating.json")
    if _os.path.exists(_rf):
        _r = _json.load(open(_rf))
        GOOGLE_RATING = _r.get("rating") or GOOGLE_RATING
        GOOGLE_REVIEW_COUNT = _r.get("count") or GOOGLE_REVIEW_COUNT
except Exception:
    pass

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
    # key: (file name or None, alt text, caption) — or a LIST of those for a 2-column grid.
    # Files live in assets/photos/ (already edited: straightened, colour-corrected, 4:5 crop).
    "hero":       ("uncle-thomas-safesmith-combination-safe.jpg", "Uncle Thomas, Singapore locksmith and safesmith, opening a combination lock on an office safe cabinet", "Uncle Thomas at work on a combination safe"),
    "about_portrait": ("uncle-thomas-safesmith-combination-safe.jpg", "Uncle Thomas, Singapore locksmith and safesmith, opening a combination lock on an office safe cabinet", "Uncle Thomas at work on a combination safe"),
    "about_van":  ("locksmith-fitting-new-door-lock-hdb.jpg", "Locksmith from Uncle Thomas's team fitting a new lock to a main door, with the floor covered to protect the home", "Our team fitting a new main door lock, floor covered first"),
    "about_tools": ("uncle-thomas-opening-office-safe.jpg", "Uncle Thomas working the dial of a combination lock on a filing safe", "Uncle Thomas working the dial of a combination safe"),
    # Homepage "Recent jobs" gallery
    "home_work": [
        ("uncle-thomas-opening-office-safe.jpg", "Uncle Thomas working the dial of a combination lock on a filing safe", "Uncle Thomas working the dial of a combination safe"),
        ("hdb-door-lock-replacement-after.jpg", "New stainless steel lever handle and lock plate fitted on a wooden main door in Singapore", "Main door lock replaced"),
        ("digital-lock-installation-after.jpg", "Slim black digital door lock with camera installed on a wooden door", "Digital lock installed"),
        ("bumil-safe-new-keypad-after.jpg", "Bumil home safe with a new electronic keypad lock fitted", "New keypad fitted to a home safe"),
        ("digital-letterbox-lock.jpg", "Digital keypad lock fitted to a stainless steel condo letterbox", "Digital letterbox lock"),
        ("rim-lock-replacement-after.jpg", "New rim lock with brass latch fitted to a white panelled door", "Rim lock replaced"),
    ],
    "emergency-locksmith/":       (None, "Locksmith opening an HDB main door without damage", "A damage-free HDB lockout job"),
    "digital-lock-opening/":      ("kaadas-digital-lock-gate-and-door.jpg", "Kaadas digital locks on a black metal gate and a wooden main door in Singapore", "Kaadas digital locks on a gate and main door — we open all brands"),
    "digital-lock-installation/": [
        ("digital-lock-installation-before.jpg", "Wooden door with drilled holes left after the old lock was removed", "Before: old lock removed, holes in the door"),
        ("digital-lock-installation-after.jpg", "Slim black digital door lock with camera installed on a wooden door", "After: new digital lock installed"),
    ],
    "safe-opening/": [
        ("uncle-thomas-opening-office-safe.jpg", "Uncle Thomas working the dial of a combination lock on a filing safe", "Uncle Thomas working the dial of a combination safe"),
        ("bumil-safe-faulty-keypad-before.jpg", "Bumil home safe with its original electronic keypad lock", "1. The safe with its original keypad lock"),
        ("bumil-safe-opened-lock-mechanism.jpg", "Safe door with the lock panel removed, showing the bolt mechanism and wiring", "2. Lock panel off, mechanism exposed"),
        ("bumil-safe-new-keypad-after.jpg", "Bumil home safe with a new electronic keypad lock fitted", "3. New keypad lock fitted"),
    ],
    "car-locksmith/":             (None, "Car door being unlocked with non-destructive tools", "Non-destructive car unlocking"),
    "lock-replacement/": [
        ("hdb-door-lock-replacement-before.jpg", "Damaged wooden main door with the old lock removed and splintered edge", "Before: damaged door, old lock removed"),
        ("hdb-door-lock-replacement-after.jpg", "New stainless steel lever handle and lock plate fitted on a wooden main door in Singapore", "After: new lever lock and cover plate"),
        ("rim-lock-replacement-before.jpg", "Old rusted rim lock on a white wooden door", "Before: old rusted rim lock"),
        ("rim-lock-replacement-after.jpg", "New rim lock with brass latch fitted to a white panelled door", "After: new rim lock fitted"),
        ("locksmith-fitting-new-door-lock-hdb.jpg", "Locksmith from Uncle Thomas's team fitting a new lock to a main door, with the floor covered to protect the home", "Our team fitting a new main door lock, floor covered first"),
        ("door-lock-cover-plate-hides-old-holes.jpg", "Stainless steel cover plate and new cylinder lock on a wooden door, hiding the holes from the old lock", "After: a cover plate neatly hides the old lock holes"),
    ],
    "letterbox-lock-replacement/": [
        ("hdb-letterbox-lock-replacement.jpg", "Key in a new lock on a stainless steel letterbox in Singapore", "Letterbox lock replaced"),
        ("digital-letterbox-lock.jpg", "Digital keypad lock fitted to a stainless steel condo letterbox", "Keyless digital letterbox lock"),
    ],
    "commercial-locksmith/": [
        ("uncle-thomas-safesmith-combination-safe.jpg", "Uncle Thomas, Singapore locksmith and safesmith, opening a combination lock on an office safe cabinet", "Uncle Thomas at work on a combination safe"),
        ("office-safe-opening.jpg", "Tall office safe cabinet with keypad lock in a Singapore office", "Office safe cabinet"),
    ],
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
    ("Car key fob cloning (spare key)", "car-locksmith/", "Quote on request", "All major car brands"),
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
