#!/usr/bin/env python3
"""
Share images (Open Graph / WhatsApp / Facebook previews), 1200x630.

Run by hand when a headline or photo changes, then commit the images:
    python3 _build/og.py

Same layout as the original og-v4.jpg: white panel with the badge logo, a two-line
headline, one line of services, the red Call / WhatsApp pill, and a real job photo
on the right behind a red divider. build.py picks the image for each page with
og_image(path); pages without their own image keep og-v4.jpg.

Bump OG_VERSION when the art changes: /assets/ is cached for a year.
"""
import os, sys
from PIL import Image, ImageDraw, ImageFont, ImageOps

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import config as C

OG_VERSION = "1"
OUT = os.path.join(ROOT, "assets", "img", "og")
FONT = os.path.join(ROOT, "assets", "fonts", "poppins-latin-{w}-normal.woff2")
RED, BLACK, GREY, WHITE = (231, 19, 40), (21, 21, 21), (85, 85, 85), (255, 255, 255)
W, H, SPLIT = 1200, 630, 730

# section key -> (headline line 1, line 2, services line, photo in assets/photos)
SECTIONS = {
    "safes":   ("Safe Opening", "in Singapore", "All safe types · Code changes · Installs", "uncle-thomas-safe-dial-tool.jpg"),
    "cars":    ("Car Locksmith", "in Singapore", "Car lockouts · Key fob cloning · 24/7", "car-lockout-condo-carpark.jpg"),
    "digital": ("Digital Lock", "Opening, 24/7", "All digital & smart lock brands", "kaadas-digital-lock-gate-and-door.jpg"),
    "doors":   ("Locked Out?", "24/7 Locksmith", "Doors · Gates · Lock changes · Islandwide", "orchard-room-door-open-under-a-minute.jpg"),
    "guides":  ("Locksmith Guides", "by Uncle Thomas", "Practical advice from a locksmith since 1998", "uncle-thomas-safesmith-combination-safe.jpg"),
    "areas":   ("Locksmith Near You", "Every Town, 24/7", "Usually there in 25–30 minutes", "locksmith-fitting-new-door-lock-hdb.jpg"),
}
AREA_PHOTO = "locksmith-fitting-new-door-lock-hdb.jpg"
# Towns whose first page photo crops badly into the narrow panel.
AREA_OVERRIDE = {"cbd-orchard": "cbd-bumil-keypad-safe-override-lock.jpg"}


def font(weight, size):
    return ImageFont.truetype(FONT.format(w=weight), size)


def fit(draw, text, weight, size, max_w):
    """Largest font size (down from `size`) at which `text` fits in max_w."""
    while size > 20:
        f = font(weight, size)
        if draw.textlength(text, font=f) <= max_w:
            return f
        size -= 2
    return font(weight, size)


def photo_panel(name, w, h):
    src = os.path.join(ROOT, "assets", "photos", name)
    im = ImageOps.exif_transpose(Image.open(src)).convert("RGB")
    return ImageOps.fit(im, (w, h), Image.LANCZOS, centering=(0.5, 0.4))


def make(fname, line1, line2, services, photo):
    img = Image.new("RGB", (W, H), WHITE)
    img.paste(photo_panel(photo, W - SPLIT - 10, H), (SPLIT + 10, 0))
    d = ImageDraw.Draw(img)
    d.rectangle([SPLIT, 0, SPLIT + 9, H], fill=RED)
    d.rectangle([0, H - 12, SPLIT, H], fill=BLACK)
    badge = Image.open(os.path.join(HERE, "brand", "logo-badge-master.png")).convert("RGBA").resize((104, 104), Image.LANCZOS)
    img.paste(badge, (60, 46), badge)
    d.text((184, 64), C.NAME, font=font(800, 30), fill=BLACK)
    d.text((184, 106), f"Singapore · Since {C.FOUNDED}", font=font(400, 22), fill=GREY)
    max_w = SPLIT - 120
    d.text((60, 186), line1, font=fit(d, line1, 800, 70, max_w), fill=RED)
    d.text((60, 268), line2, font=fit(d, line2, 800, 70, max_w), fill=BLACK)
    d.text((60, 366), services, font=fit(d, services, 400, 26, max_w), fill=BLACK)
    pill = f"Call / WhatsApp {C.PHONE}"
    pf = font(800, 30)
    pw = d.textlength(pill, font=pf) + 68
    d.rounded_rectangle([60, 424, 60 + pw, 500], radius=38, fill=RED)
    d.text((94, 440), pill, font=pf, fill=WHITE)
    d.text((60, 532), "Islandwide · Price confirmed first", font=font(400, 22), fill=GREY)
    os.makedirs(OUT, exist_ok=True)
    img.save(os.path.join(OUT, fname), quality=84, optimize=True, progressive=True)


def main():
    import areas
    for key, (l1, l2, svc, ph) in SECTIONS.items():
        make(f"og-{key}-v{OG_VERSION}.jpg", l1, l2, svc, ph)
    for t in areas.TOWNS:
        own = C.PHOTOS.get("areas/" + t["slug"] + "/")
        ph = AREA_OVERRIDE.get(t["slug"]) or ((own[0] if isinstance(own, list) else own)[0] if own else AREA_PHOTO)
        make(f"og-area-{t['slug']}-v{OG_VERSION}.jpg", "Locksmith in", t["name"], "24/7 · Usually there in 25–30 minutes", ph)
    print("Share images written to assets/img/og/")


# ---- used by build.py --------------------------------------------------------
SAFE = ("safe-", "hotel-safe-opening/", "commercial-safe-services/")
DOORS = ("emergency-locksmith/", "lock-replacement/", "hdb-main-door-lock-replacement/", "hdb-gate-lock-replacement/",
         "letterbox-lock-replacement/", "broken-key-extraction/", "padlock-cutting/", "roller-shutter-lock/",
         "glass-door-lock/", "cabinet-lock/", "commercial-locksmith/")


def section(path):
    if path.startswith("areas/") and path.count("/") == 2:
        return "area-" + path.split("/")[1]
    if path.startswith(SAFE):
        return "safes"
    if path.startswith(("car-locksmith/", "car-key-duplicate/")):
        return "cars"
    if path.startswith(("digital-lock-", "hdb-gate-digital-lock/")):
        return "digital"
    if path.startswith(DOORS):
        return "doors"
    if path.startswith("guides/"):
        return "guides"
    if path == "areas/":
        return "areas"
    return None


def og_image(path):
    """Site-relative path of the share image for a page (falls back to og-v4.jpg)."""
    key = section(path)
    if key:
        rel = f"assets/img/og/og-{key}-v{OG_VERSION}.jpg"
        if os.path.exists(os.path.join(ROOT, rel)):
            return rel
    return "assets/img/og-v4.jpg"


if __name__ == "__main__":
    main()
