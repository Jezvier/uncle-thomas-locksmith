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
# Google Place ID (matched to the CID above on 27 Oct 2026) and the direct "write a review" link.
PLACE_ID = "ChIJW1IOQGYX2jERKiFMX6nMhjk"
GOOGLE_REVIEW_URL = "https://search.google.com/local/writereview?placeid=" + PLACE_ID
# Browser key for the live Google reviews on the homepage. Public by design: Google only
# accepts it from singapore-locksmiths.com and only for Places / Maps JavaScript.
# (The private server key for the nightly rating update lives in GitHub secrets.)
GOOGLE_BROWSER_KEY = "AIzaSyCUNm-S2hDRP6pABYF1hCNOqgVpN6_wgbI"
# ACRA registration (sole proprietorship, registered 21 Feb 1998). Shown in the footer + schema.
UEN = "52862311K"
LEGAL_NAME = "Thomas Locksmith"
# Other names customers and listings know the business by (Google Business Profile = "Singapore Locksmith").
ALT_NAMES = ["Thomas Locksmith", "Singapore Locksmith"]
# FILL: Google Analytics 4 Measurement ID (e.g. "G-ABC123XYZ"). None = analytics off.
GA4_ID = "G-DSL14WM5HH"

# Add Facebook / Instagram / Carousell / directory profile URLs here as you create them.
SAME_AS = [GOOGLE_PROFILE]
LANGUAGES = ["English", "Mandarin", "Malay", "Hokkien", "Cantonese"]   # confirmed by owner 31 Oct 2026 ("all languages")
TEAM = ["Thomas", "Ong", "Melvin", "Andrew"]   # confirmed 31 Oct 2026
PAYMENT = "PayNow"   # confirmed 31 Oct 2026

# Title style for homepage + service pages:
#   "KEEP PRICE"           -> "24/7 Locksmith Singapore from S$80 | Uncle Thomas Since 1998"
#   "LEAD WITH EXPERIENCE" -> "24/7 Locksmith Singapore | Since 1998 · US-Trained Safesmith"
TITLE_STYLE = "KEEP PRICE"

DESCRIPTION = ("24/7 emergency locksmith in Singapore since 1998, led by Uncle Thomas — a US-trained safesmith. "
               "Door lockouts, digital lock opening and installation, safe opening, car lockouts, lock and "
               "letterbox replacement, islandwide.")

DIGITAL_LOCK_BRANDS = ["Samsung", "Zigbang", "Yale", "Philips", "Igloohome", "Kaadas", "Solity", "Gateman", "Häfele",
                       "Aqara", "Xiaomi", "Lenovo", "Schlage", "Eufy", "Tapo", "Prism+", "Ezviz", "Lockly", "Yew",
                       "Epic", "Milre", "Dessmann", "Lockin", "Zeus", "Kaiser+", "Starke"]
# Digital / smart lock brands that get their own page at /digital-lock-opening/<brand>/
BRAND_PAGES = ["Samsung", "Zigbang", "Yale", "Philips", "Igloohome", "Gateman", "Kaadas", "Solity", "Häfele", "Schlage",
               "Aqara", "Xiaomi", "Lenovo", "Eufy", "Tapo", "Prism+", "Ezviz", "Lockly", "Yew"]

# Car brands. Owner: Uncle Thomas opens and clones fobs for all makes EXCEPT Tesla — so Tesla is never listed.
# CAR_BRAND_PAGES get their own page at /car-locksmith/<brand>/ (content in _build/cars.py).
CAR_BRAND_PAGES = ["BYD", "Toyota", "Honda", "Mercedes-Benz", "BMW", "Audi", "Volkswagen", "Mazda", "Lexus",
                   "Land Rover", "Hyundai", "Kia", "Nissan", "Porsche", "Volvo", "Mitsubishi", "Subaru",
                   "MG", "Mini", "Skoda", "Peugeot", "Suzuki"]
CAR_BRANDS_MORE = ["Ford", "Jaguar", "Jeep", "Renault",
                   "Citroën", "Opel", "Infiniti", "Alfa Romeo", "Maserati", "Bentley", "Ferrari", "Lamborghini",
                   "Rolls-Royce", "Chevrolet", "Cupra", "Polestar"]

# Real jobs per brand, shown as "Recent job" on that brand's page (car or lock).
# FILL over time with REAL jobs only, e.g. "Kaadas": ["Oct 2026, Punggol: gate lock batteries flat, opened in 20 minutes."]
BRAND_JOBS = {}   # filled from JOBS below

# Safe brands mentioned on the safe opening page (Uncle Thomas opens all makes).
SAFE_BRANDS = ["Yale", "SentrySafe", "Phoenix", "Honeywell", "Godrej", "Diplomat", "Eagle", "Bumil", "Booil", "Chubb",
               "Burg-Wächter", "Glory", "Uchida", "Lion", "Gunnebo", "Kokuyo", "Kaba", "Sargent & Greenleaf"]
# Safe brands without their own page (mentioned on the safe opening hub).
SAFE_BRANDS_MORE = ["Nikawa", "Uchida", "Kokuyo", "Lion", "Glory", "Gunnebo", "Kaba", "Sargent & Greenleaf"]

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
    "hero":       ("uncle-thomas-safe-dial-hero.jpg", "Uncle Thomas, Singapore safesmith, wearing a mask and turning the combination dial of a stainless steel safe with a dial tool", "Uncle Thomas working the combination dial of a safe"),
    "about_portrait": ("uncle-thomas-safesmith-combination-safe.jpg", "Uncle Thomas, Singapore locksmith and safesmith, opening a combination lock on an office safe cabinet", "Uncle Thomas at work on a combination safe"),
    "about_van":  ("locksmith-fitting-new-door-lock-hdb.jpg", "Locksmith from Uncle Thomas's team fitting a new lock to a main door, with the floor covered to protect the home", "Our team fitting a new main door lock, floor covered first"),
    "about_tools": ("uncle-thomas-opening-office-safe.jpg", "Uncle Thomas working the dial of a combination lock on a filing safe", "Uncle Thomas working the dial of a combination safe"),
    # Homepage "Recent jobs" gallery
    "home_work": [
        ('car-lockout-condo-carpark.jpg', "Uncle Thomas kneeling beside a dark car in a Woodlands carpark, opening the locked driver's door without damage", 'Uncle Thomas opening a locked car door (Woodlands)'),
        ("uncle-thomas-opening-office-safe.jpg", "Uncle Thomas working the dial of a combination lock on a filing safe", "Uncle Thomas working the dial of a combination safe"),
        ('orchard-room-door-lock-replacement.jpg', 'Uncle Thomas fitting a new stainless steel knob lockset to a bedroom door in an Orchard apartment', 'Fitting a new lockset after a bedroom door lock cracked (Orchard)'),
        ("bumil-safe-new-keypad-after.jpg", "Bumil home safe with a new electronic keypad lock fitted", "New keypad fitted to a home safe"),
        ("digital-lock-installation-after.jpg", "Slim black digital door lock with camera installed on a wooden door", "Digital lock installed"),
        ("hdb-door-lock-replacement-after.jpg", "New stainless steel lever handle and lock plate fitted on a wooden main door in Singapore", "Main door lock replaced"),
    ],
    "emergency-locksmith/":       [('orchard-locked-room-door-before.jpg', 'Uncle Thomas arriving at a locked white room door on Orchard Road', 'Arriving at the locked room door (Orchard Road, Nov 2026)'), ('orchard-room-door-open-under-a-minute.jpg', 'The same white room door swung open, with Uncle Thomas stepping into the room', 'Under a minute later: door open, no damage'), ('orchard-broken-door-knob-removal.jpg', 'Uncle Thomas removing a worn-out brass door knob that broke and locked a resident out of her room', 'Removing a worn-out knob that broke and locked a resident out (Orchard)'), ('orchard-room-door-lock-replacement.jpg', 'Uncle Thomas fitting a new stainless steel knob lockset to a bedroom door in an Orchard apartment', 'Fitting a new lockset after a bedroom door lock cracked (Orchard)')],
    "areas/woodlands/":           [('car-lockout-condo-carpark.jpg', "Uncle Thomas kneeling beside a dark car in a Woodlands carpark, opening the locked driver's door without damage", 'Uncle Thomas opening a locked car door (Woodlands)')],
    "areas/serangoon/":           [('serangoon-lever-door-lock-cylinder.jpg', 'Brushed steel lever handle with a key cylinder on a wooden door in Serangoon', 'The lever-handle lock that took about 30 minutes (Serangoon)'), ('serangoon-lever-lock-key.jpg', 'Silver key for the lever-handle lock, on a white counter', 'The key for that Serangoon lever lock')],
    "areas/bishan/":              ('bishan-room-door-knob-lock-opened.jpg', 'Stainless steel knob lockset on a dark wooden room door, opened, in Bishan', 'Room door knob lock, opened (Bishan, Nov 2026)'),
    "safe-opening/bumil/":        ('cbd-bumil-keypad-safe-override-lock.jpg', 'Uncle Thomas opening a Bumil electronic safe, with a pick set in its override key lock', 'A Bumil keypad safe we opened through its override lock (CBD, Nov 2026)'),
    "areas/cbd-orchard/":         [('orchard-locked-room-door-before.jpg', 'Uncle Thomas arriving at a locked white room door on Orchard Road', 'Arriving at the locked room door (Orchard Road, Nov 2026)'), ('orchard-room-door-open-under-a-minute.jpg', 'The same white room door swung open, with Uncle Thomas stepping into the room', 'Under a minute later: door open, no damage'), ('orchard-room-door-lock-replacement.jpg', 'Uncle Thomas fitting a new stainless steel knob lockset to a bedroom door in an Orchard apartment', 'Fitting a new lockset after a bedroom door lock cracked (Orchard)'), ('orchard-broken-door-knob-removal.jpg', 'Uncle Thomas removing a worn-out brass door knob that broke and locked a resident out of her room', 'Removing a worn-out knob that broke and locked a resident out (Orchard)'), ('cbd-bumil-keypad-safe-override-lock.jpg', 'Uncle Thomas opening a Bumil electronic safe, with a pick set in its override key lock', 'Opening a Bumil keypad safe through its override lock (CBD)'), ('cbd-metal-gate-opened.jpg', 'Black metal gate swung open, showing the bolt of its surface-mounted gate lock', 'Metal gate opened, lock still working (CBD)')],
    "digital-lock-opening/":      ("kaadas-digital-lock-gate-and-door.jpg", "Kaadas digital locks on a black metal gate and a wooden main door in Singapore", "Kaadas digital locks on a gate and main door — we open all brands"),
    "hdb-gate-digital-lock/":     ("kaadas-digital-lock-gate-and-door.jpg", "Kaadas digital locks on a black metal gate and a wooden main door in Singapore", "A matching digital lock set on an HDB gate and main door"),
    "digital-lock-installation/": [
        ("digital-lock-installation-before.jpg", "Wooden door with drilled holes left after the old lock was removed", "Before: old lock removed, holes in the door"),
        ("digital-lock-installation-after.jpg", "Slim black digital door lock with camera installed on a wooden door", "After: new digital lock installed"),
    ],
    "safe-opening/": [
        ("uncle-thomas-opening-office-safe.jpg", "Uncle Thomas working the dial of a combination lock on a filing safe", "Uncle Thomas working the dial of a combination safe"),
        ("uncle-thomas-safe-dial-tool.jpg", "Uncle Thomas, Singapore safesmith, using a dial tool on the combination lock of a large stainless steel safe", "Uncle Thomas working the combination dial of a large safe"),
        ("bumil-safe-faulty-keypad-before.jpg", "Bumil home safe with its original electronic keypad lock", "1. The safe with its original keypad lock"),
        ("bumil-safe-opened-lock-mechanism.jpg", "Safe door with the lock panel removed, showing the bolt mechanism and wiring", "2. Lock panel off, mechanism exposed"),
        ("bumil-safe-new-keypad-after.jpg", "Bumil home safe with a new electronic keypad lock fitted", "3. New keypad lock fitted"),
        ("chubb-safe-singapore.jpg", "Older Chubb safe with a spoked handle, combination dial and key lock in a Singapore storeroom", "Older Chubb safe: combination dial plus key lock"),
    ],
    "safe-combination-change/": [
        ("bumil-safe-faulty-keypad-before.jpg", "Bumil home safe with its original electronic keypad lock, before the lock was replaced", "Before: the safe's original keypad lock had failed"),
        ("bumil-safe-new-keypad-after.jpg", "Bumil home safe with a new electronic keypad lock fitted by Uncle Thomas Locksmith", "After: new keypad lock fitted, same safe"),
    ],
    "safe-installation/": [
        ("office-safe-opening.jpg", "Tall office safe cabinet with keypad lock in a Singapore office", "An office safe cabinet with a keypad lock"),
        ("chubb-safe-singapore.jpg", "Older Chubb safe with a spoked handle, combination dial and key lock in a Singapore storeroom", "A heavier dual-lock safe: combination dial plus key"),
    ],
    "commercial-safe-services/": [
        ("uncle-thomas-safe-dial-tool.jpg", "Uncle Thomas, Singapore safesmith, using a dial tool on the combination lock of a large stainless steel safe", "Uncle Thomas working the combination dial of a large safe"),
        ("uncle-thomas-opening-office-safe.jpg", "Uncle Thomas working the dial of a combination lock on a filing safe in an office", "Uncle Thomas opening a filing safe in an office"),
    ],
    "hdb-main-door-lock-replacement/": [
        ("hdb-door-lock-replacement-before.jpg", "Damaged wooden HDB main door with the old lock removed and a splintered edge", "Before: damaged door, old lock removed"),
        ("hdb-door-lock-replacement-after.jpg", "New stainless steel lever handle and lock plate fitted on a wooden main door in Singapore", "After: new lever lock and cover plate"),
        ("locksmith-fitting-new-door-lock-hdb.jpg", "Locksmith from Uncle Thomas's team fitting a new lock to a main door, with the floor covered to protect the home", "Our team fitting a new main door lock, floor covered first"),
        ("door-lock-cover-plate-hides-old-holes.jpg", "Stainless steel cover plate and new cylinder lock on a wooden door, hiding the holes from the old lock", "A cover plate neatly hides the old lock holes"),
    ],
    "car-locksmith/":             ('car-lockout-condo-carpark.jpg', "Uncle Thomas kneeling beside a dark car in a Woodlands carpark, opening the locked driver's door without damage", 'Uncle Thomas opening a locked car door (Woodlands)'),
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
# Real jobs confirmed by the owner. One list; area, service and brand pages are filled from it.
# area = areas slug, service = service page path, brand = car or lock brand page name, or "safe:<Brand>" for a safe brand page (optional).
JOBS = [
    dict(date="Nov 2026", area="serangoon", service="emergency-locksmith/",
         text="Serangoon: a lever-handle door whose key cylinder put up a real fight. One of the tougher openings this month: Uncle Thomas stayed on it for about 30 minutes of patient work, and the lock came open without being broken."),
    dict(date="Nov 2026", area="bishan", service="emergency-locksmith/",
         text="Bishan: a room door shut and locked on its stainless knob lockset. A routine opening for Uncle Thomas, sorted in one short visit."),
    dict(date="Nov 2026", area="cbd-orchard", service="safe-opening/", brand="safe:Bumil",
         text="CBD: a Bumil electronic keypad safe that refused to open. Uncle Thomas opened it through its override key lock, so the safe itself was left intact."),
    dict(date="Nov 2026", area="cbd-orchard", service="emergency-locksmith/",
         text="CBD: a black metal gate held shut by a surface-mounted gate lock. Uncle Thomas opened it the usual way, and the lock still throws its bolt as it should."),
    dict(date="Nov 2026", area="cbd-orchard", service="emergency-locksmith/",
         text="Orchard Road: a painter was locked out of a room. Uncle Thomas had the door open in under a minute, without damaging the door or the lock."),
    dict(date="Nov 2026", area="woodlands", service="safe-opening/",
         text="Woodlands: an elderly couple could no longer open their small, unbranded home safe. Uncle Thomas opened it for them on the spot."),
    dict(date="Nov 2026", area="toa-payoh", service="commercial-locksmith/",
         text="Toa Payoh: opened a locked factory door fitted with a Nelon lock, for a business client."),
    dict(date="Nov 2026", area="cbd-orchard", service="lock-replacement/",
         text="Orchard Road: a cracked bedroom door lock left the resident locked out of her room. Uncle Thomas removed the broken lock and fitted a new lockset in the same visit."),
    dict(date="Oct 2026", area="cbd-orchard", service="emergency-locksmith/",
         text="Orchard Road: a worn-out door knob broke and locked the resident out of her room in the evening. Uncle Thomas removed the broken knob and had her back in within 2 minutes."),
    dict(date="Oct 2026", area="punggol", service="car-locksmith/", brand="Nissan",
         text="Punggol: Nissan car lockout. Arrived within 15 minutes and opened the door in under 2 minutes."),
]
RECENT_JOBS, SERVICE_JOBS = {}, {}
for _j in JOBS:
    _line = f'{_j["date"]}, {_j["text"]}'
    RECENT_JOBS.setdefault(_j["area"], []).append(_line)
    SERVICE_JOBS.setdefault(_j["service"], []).append(_line)
    if _j.get("brand"):
        BRAND_JOBS.setdefault(_j["brand"], []).append(_line)


# ---- Prices -------------------------------------------------------------
# (label, page path or None, "from" price in S$ (int) or text, short note)
# FILL / CONFIRM: Uncle Thomas must be willing to honour every "from" price.
PRICES = [
    ("Home / office lockout (9am–6pm)", "emergency-locksmith/", 70, "Damage-free entry where possible"),
    ("Lockout after hours, weekends & public holidays", "emergency-locksmith/", 90, "24/7, islandwide"),
    ("Digital lock emergency opening", "digital-lock-opening/", 150, "All brands"),
    ("Digital lock installation (labour)", "digital-lock-installation/", 150, "Lock supplied by you or us"),
    ("Car lockout (non-destructive)", "car-locksmith/", 80, "All makes and models"),
    ("Car key fob cloning (spare key)", "car-locksmith/", "S$100–S$1,000", "Remote keys; depends on the car, call to enquire"),
    ("Main door / gate lock replacement (supply + install)", "lock-replacement/", 100, "Warranty included"),
    ("Letterbox lock replacement", "letterbox-lock-replacement/", 60, "HDB & condo letterboxes"),
    ("Safe opening", "safe-opening/", 120, "All safe types; exact price confirmed from photos"),
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
    "P_LOCKOUT": "S$70",
    "P_AFTERHOURS": "S$90",
    "P_DIGITAL_OPEN": "S$150",
    "P_DIGITAL_INSTALL": "S$150",
    "P_CAR": "S$80",
    "P_REPLACE": "S$100",
    "P_LETTERBOX": "S$60",
    "P_FOB": "S$100–S$1,000",
    "P_SAFE": "S$120",
    "ARRIVAL": "25–30 minutes",
    "P_LOWEST": f"S${LOWEST_PRICE}",
    "UEN": UEN or "",
}
