#!/usr/bin/env python3
"""
Uncle Thomas Locksmith — static site generator.

HOW TO USE
  python3 _build/build.py

It regenerates every .html page, sitemap.xml, robots.txt, llms.txt,
site.webmanifest, script.js and _headers in the repo root from:
  _build/config.py   business facts, prices, domain, reviews, photos (edit here first)
  _build/content.py  page text for home, services, prices, about
  _build/areas.py    town pages
  _build/brands.py   digital lock brand pages
  _build/cars.py     car brand pages
  _build/guides.py   guide articles
  _build/zh.py       Chinese pages
  _build/styles.css  the stylesheet (inlined into every page for speed)

Do NOT hand-edit the generated .html files — edits are overwritten on the
next build. (Folders starting with "_" are not published by GitHub Pages.)
Requires Python 3 and Pillow (pip install pillow) only if you add photos.
"""
import json, os, re, sys, html
from datetime import date

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

import config as C
import content, areas, guides, brands, cars, zh, icons

TODAY = date.today().isoformat()
PAGES = []          # (path, priority) for sitemap
CSS = ""            # minified stylesheet, inlined into every page


def esc(s):
    return html.escape(s, quote=True)


def abs_url(path):
    return C.SITE + "/" + path if path else C.SITE + "/"


def rel_prefix(path):
    depth = path.count("/")
    return "../" * depth if depth else ""


def fill(s, prefix):
    """Replace ~/ tokens with the page's relative prefix and {PLACEHOLDERS}."""
    s = s.replace('"~/"', '"%s"' % (prefix or "./"))
    s = s.replace("~/", prefix)
    for k, v in C.TOKENS.items():
        s = s.replace("{" + k + "}", v)
    return s


# ---------- UI strings (English / Chinese) ----------
T = {
 "en": dict(topbar_long=f"24/7 Emergency Locksmith · Islandwide Singapore · Since {C.FOUNDED}",
            topbar_short=f"24/7 · Islandwide · Since {C.FOUNDED}",
            call=f"Call {C.PHONE}", wa="WhatsApp Us", call_now="Call Now", wa_short="WhatsApp",
            skip="Skip to content", menu_open="Open menu", home="Home", services="Services", more="More",
            prices="Prices", areas="Areas we serve", guides="Guides", about="About Uncle Thomas",
            hotline="24/7 hotline", email="Email", hours="Hours", hours_v="24 hours, 7 days, incl. public holidays",
            coverage="Coverage", coverage_v="Islandwide Singapore", google="Find us on Google",
            f_services="Services", f_areas="Areas", f_guides="Guides", all_areas="All areas →",
            cta_title="Need a Locksmith Right Now?",
            cta_lead="Call or WhatsApp Uncle Thomas — 24/7, islandwide. We set off as soon as you call.",
            bottom="Singapore · 24/7 Emergency Locksmith", wa_link=C.WA_LINK, other_lang="中文"),
 "zh": dict(topbar_long=f"24小时紧急锁匠 · 全岛服务 · 自{C.FOUNDED}年",
            topbar_short=f"24小时 · 全岛 · 自{C.FOUNDED}年",
            call=f"致电 {C.PHONE}", wa="WhatsApp", call_now="立即致电", wa_short="WhatsApp",
            skip="跳到内容", menu_open="打开菜单", home="首页", services="服务（英文）", more="更多",
            prices="价格", areas="服务地区", guides="指南", about="关于 Uncle Thomas",
            hotline="24小时热线", email="电邮", hours="营业时间", hours_v="全天24小时，全年无休（包括公共假期）",
            coverage="服务范围", coverage_v="新加坡全岛", google="在 Google 上找到我们",
            f_services="服务", f_areas="地区", f_guides="指南", all_areas="所有地区 →",
            cta_title="现在需要锁匠吗？",
            cta_lead="致电或 WhatsApp Uncle Thomas — 24小时，全岛服务。接到电话立即出发。",
            bottom="新加坡 · 24小时紧急锁匠", wa_link=C.WA_LINK_ZH, other_lang="English"),
}


# ---------- shared schema pieces ----------
BUSINESS_ID = C.SITE + "/#business"
PERSON_ID = C.SITE + "/about/#uncle-thomas"
ALL_DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]


def business_node(full=False):
    node = {
        "@type": "Locksmith",
        "@id": BUSINESS_ID,
        "name": C.NAME,
        "url": C.SITE + "/",
        "telephone": C.PHONE_E164,
        "image": C.SITE + "/assets/img/logo-640.jpg",
        "logo": C.SITE + "/assets/img/logo-640.jpg",
        "priceRange": C.PRICE_RANGE,
        "address": {"@type": "PostalAddress", "addressLocality": "Singapore", "addressCountry": "SG"},
        "areaServed": {"@type": "Country", "name": "Singapore"},
        "openingHoursSpecification": {"@type": "OpeningHoursSpecification", "dayOfWeek": ALL_DAYS,
                                      "opens": "00:00", "closes": "23:59"},
    }
    if C.UEN:
        node["taxID"] = C.UEN
    if getattr(C, "LEGAL_NAME", None):
        node["legalName"] = C.LEGAL_NAME
    if getattr(C, "ALT_NAMES", None):
        node["alternateName"] = C.ALT_NAMES
    if full:
        node.update({
            "description": C.DESCRIPTION,
            "slogan": C.SLOGAN,
            "foundingDate": str(C.FOUNDED),
            "founder": {"@id": PERSON_ID},
            "knowsAbout": ["Emergency lockout", "Digital lock opening", "Digital lock installation",
                           "Safe opening", "Safesmithing", "Car lockout", "HDB door and gate locks",
                           "Letterbox locks", "Commercial locks"],
            "areaServed": [{"@type": "Country", "name": "Singapore"}] +
                          [{"@type": "Place", "name": t["name"] + ", Singapore"} for t in areas.TOWNS],
            "hasOfferCatalog": offer_catalog(),
            "contactPoint": {"@type": "ContactPoint", "telephone": C.PHONE_E164, "contactType": "customer service",
                             "areaServed": "SG", "availableLanguage": C.LANGUAGES,
                             "hoursAvailable": {"@type": "OpeningHoursSpecification", "dayOfWeek": ALL_DAYS,
                                                "opens": "00:00", "closes": "23:59"}},
            "sameAs": C.SAME_AS,
        })
        if C.EMAIL:
            node["email"] = C.EMAIL
        seen, imgs = set(), []
        for k in C.PHOTOS:
            for o in photos_schema(k):
                if o["contentUrl"] not in seen:
                    seen.add(o["contentUrl"]); imgs.append(o)
        if imgs:
            node["photo"] = imgs
    return node


def offer_catalog():
    items = []
    for label, path, price, note in C.PRICES:
        o = {"@type": "Offer", "itemOffered": {"@type": "Service", "name": label}}
        if path:
            o["itemOffered"]["url"] = C.SITE + "/" + path
        if isinstance(price, int):
            o["priceSpecification"] = {"@type": "PriceSpecification", "minPrice": price, "priceCurrency": "SGD"}
        items.append(o)
    return {"@type": "OfferCatalog", "name": "Locksmith services", "itemListElement": items}


def person_node():
    node = {
        "@type": "Person", "@id": PERSON_ID, "name": "Uncle Thomas",
        "jobTitle": "Master Locksmith & Safesmith",
        "description": "Singapore locksmith since 1998. Trained in safesmithing in the United States; has opened safes on ships and in Thailand, Malaysia, China and Hong Kong.",
        "knowsAbout": ["Locksmithing", "Safesmithing", "Safe opening", "Digital locks"],
        "worksFor": {"@id": BUSINESS_ID},
        "url": C.SITE + "/about/",
        "image": (photo_schema("about_portrait") or {}).get("contentUrl", C.SITE + "/assets/img/logo-640.jpg"),
    }
    return node


def breadcrumb_node(crumbs):
    return {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": abs_url(p)} for i, (n, p) in enumerate(crumbs)]}


def faq_node(faqs):
    return {"@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": strip_tags(q), "acceptedAnswer": {"@type": "Answer", "text": strip_tags(a)}} for q, a in faqs]}


def strip_tags(s):
    s = re.sub(r"<[^>]+>", "", s)
    for k, v in C.TOKENS.items():
        s = s.replace("{" + k + "}", v)
    return html.unescape(re.sub(r"\s+", " ", s)).strip()


# ---------- photos ----------
PHOTO_DIR = os.path.join(ROOT, "assets", "photos")
PHOTO_OUT = os.path.join(ROOT, "assets", "img", "photos")
_photo_cache = {}


def _entries(key):
    """PHOTOS[key] may be one (file, alt, caption) tuple or a list of them."""
    v = C.PHOTOS.get(key)
    if not v:
        return []
    return v if isinstance(v, list) else [v]


def _prepare(fname, alt, caption):
    """Make 400/800px WebP + 800px JPG versions of one photo. Returns dict or None."""
    if not fname:
        return None
    if fname in _photo_cache:
        return dict(_photo_cache[fname], alt=alt, caption=caption)
    src = os.path.join(PHOTO_DIR, fname)
    if not os.path.exists(src):
        print(f"  ! Photo not found: assets/photos/{fname} (hidden)")
        return None
    try:
        from PIL import Image, ImageOps
    except ImportError:
        sys.exit("Pillow is needed for photos: pip install pillow")
    os.makedirs(PHOTO_OUT, exist_ok=True)
    stem = re.sub(r"[^a-z0-9]+", "-", os.path.splitext(fname)[0].lower()).strip("-")
    im = ImageOps.exif_transpose(Image.open(src)).convert("RGB")
    outs = {}
    for w in (400, 800):
        h = round(im.height * w / im.width)
        r = im.resize((w, h), Image.LANCZOS)
        r.save(os.path.join(PHOTO_OUT, f"{stem}-{w}.webp"), quality=78, method=6)
        outs[w] = h
    im.resize((800, outs[800]), Image.LANCZOS).save(os.path.join(PHOTO_OUT, f"{stem}-800.jpg"), quality=80, optimize=True, progressive=True)
    import hashlib
    ver = hashlib.md5(open(src, "rb").read()).hexdigest()[:8]   # cache-buster: assets are cached for a year
    _photo_cache[fname] = dict(stem=stem, w=800, h=outs[800], ver=ver)
    return dict(_photo_cache[fname], alt=alt, caption=caption)


def _photos(key):
    return [p for p in (_prepare(*e) for e in _entries(key)) if p]


def _figure(p, eager, cls, sizes):
    load = 'fetchpriority="high"' if eager else 'loading="lazy" decoding="async"'
    base, q = f'~/assets/img/photos/{p["stem"]}', f'?v={p["ver"]}'
    return (f'<figure class="{cls}"><picture><source type="image/webp" srcset="{base}-400.webp{q} 400w, {base}-800.webp{q} 800w" '
            f'sizes="{sizes}"><img src="{base}-800.jpg{q}" alt="{esc(p["alt"])}" width="{p["w"]}" '
            f'height="{p["h"]}" {load}></picture><figcaption>{esc(p["caption"])}</figcaption></figure>')


def photo(key, eager=False, cls="photo"):
    """One <figure>, or a 2-column grid of figures when the slot holds a list.
    Hidden FILL comment if the slot is empty."""
    ps = _photos(key)
    if not ps:
        alt = (_entries(key) or [(None, key, "")])[0][1]
        return f'<!-- FILL: real photo for slot "{key}" ({alt}). Add it in _build/config.py → PHOTOS. -->'
    if len(ps) == 1 and not isinstance(C.PHOTOS.get(key), list):
        return _figure(ps[0], eager, cls, "(min-width: 860px) 780px, 100vw")
    figs = "".join(_figure(p, eager and i == 0, "photo", "(min-width: 860px) 390px, 50vw") for i, p in enumerate(ps))
    return f'<div class="photo-grid">{figs}</div>'


def _image_object(p):
    return {"@type": "ImageObject", "contentUrl": f'{C.SITE}/assets/img/photos/{p["stem"]}-800.jpg',
            "caption": p["caption"], "description": p["alt"], "width": p["w"], "height": p["h"]}


def photo_schema(key):
    """ImageObject for the first photo in a slot (or None)."""
    ps = _photos(key)
    return _image_object(ps[0]) if ps else None


def photos_schema(key):
    """ImageObjects for every photo in a slot."""
    return [_image_object(p) for p in _photos(key)]


# ---------- HTML building blocks ----------
WA_ICON = '<svg class="bi" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 11.5a8.4 8.4 0 0 1-9 8.4 8.6 8.6 0 0 1-3.8-.9L3 21l1.9-5A8.4 8.4 0 1 1 21 11.5z"/></svg>'
PHONE_ICON = '<svg class="bi bi-phone" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2a1 1 0 0 1 1-.25 11.4 11.4 0 0 0 3.6.57 1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 17 0 0 1 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1c0 1.25.2 2.45.57 3.57a1 1 0 0 1-.25 1z"/></svg>'


def cta_buttons(size="btn-lg", center=False, wa_text=None, lang="en", pos="hero"):
    t = T[lang]
    wa_text = wa_text or t["wa"]
    return (f'<div class="cta-row{" center" if center else ""}">'
            f'<a href="tel:{C.PHONE_E164}" class="btn btn-call {size}" data-pos="{pos}">{PHONE_ICON} {t["call"]}</a>'
            f'<a href="{t["wa_link"]}" class="btn btn-wa {size}" target="_blank" rel="noopener" data-pos="{pos}">{WA_ICON} {wa_text}</a></div>')


def faq_html(faqs, title="Frequently Asked Questions"):
    out = [f'<h2 class="section-title">{title}</h2><div style="margin-top:28px">']
    for q, a in faqs:
        out.append(f'<details class="faq"><summary>{q}</summary><div class="faq-a"><p>{a}</p></div></details>')
    out.append("</div>")
    return "".join(out)


def cta_band(title=None, lead=None, lang="en"):
    t = T[lang]
    return (f'<section class="section cta-band"><div class="container narrow">'
            f'<h2 class="section-title">{title or t["cta_title"]}</h2><p class="section-lead">{lead or t["cta_lead"]}</p>'
            f'{cta_buttons(center=True, wa_text=("WhatsApp " + C.PHONE) if lang == "en" else None, lang=lang, pos="cta_band")}</div></section>')


def breadcrumb_html(crumbs):
    items = []
    for i, (n, p) in enumerate(crumbs):
        if i == len(crumbs) - 1:
            items.append(f'<li aria-current="page">{esc(n)}</li>')
        else:
            items.append(f'<li><a href="~/{p}">{esc(n)}</a></li>')
    return f'<nav class="breadcrumb" aria-label="Breadcrumb"><ol>{"".join(items)}</ol></nav>'


def page_hero(crumbs, h1, sub, badges=None, lang="en"):
    b = ""
    if badges:
        b = '<ul class="badges">' + "".join(f"<li>{x}</li>" for x in badges) + "</ul>"
    return (f'<section class="page-hero"><div class="container">{breadcrumb_html(crumbs)}'
            f'<h1>{h1}</h1><p class="hero-sub">{sub}</p>{cta_buttons(lang=lang)}{b}</div></section>')


NAV = {"en": [("Services", "services/"), ("Prices", "prices/"), ("Areas", "areas/"), ("Guides", "guides/"), ("About", "about/")],
       "zh": [("首页", "zh/"), ("紧急开锁", "zh/emergency-locksmith/"), ("价格", "prices/"), ("关于", "about/")]}


def header_html(path, lang="en", alt_path=None):
    t = T[lang]
    nav = []
    for label, p in NAV[lang]:
        cur = ' aria-current="page"' if path == p or (path.startswith(p) and p not in ("", "zh/")) else ""
        nav.append(f'<a href="~/{p}"{cur}>{label}</a>')
    svc = "".join(f'<li><a href="~/{s["path"]}">{zh.ZH_NAMES.get(s["path"], s["short"]) if lang == "zh" else s["short"]}</a></li>' for s in content.SERVICES)
    switch = f' · <a class="lang-switch" href="~/{alt_path}" hreflang="{"zh-SG" if lang == "en" else "en-SG"}">{t["other_lang"]}</a>' if alt_path is not None else ""
    home = "~/zh/" if lang == "zh" else "~/"
    zh_items = ('<li><a href="~/zh/">中文首页</a></li><li><a href="~/zh/emergency-locksmith/">紧急开锁</a></li>'
                if lang == "zh" else "")
    return f'''<a class="skip" href="#main">{t["skip"]}</a>
<div class="topbar"><span class="long">{t["topbar_long"]}</span><span class="short">{t["topbar_short"]}</span>{switch}</div>
<header class="header">
  <div class="container header-inner">
    <a href="{home}" class="brand" aria-label="{C.NAME} — {t["home"]}">
      <picture><source srcset="~/assets/img/logo-112.webp" type="image/webp"><img src="~/assets/img/logo-112.png" alt="{C.NAME} logo" width="52" height="52"></picture>
      <span class="brand-text"><strong>Uncle Thomas</strong><small>Locksmith · Since {C.FOUNDED}</small></span>
    </a>
    <nav class="nav" aria-label="Main">{"".join(nav)}</nav>
    <a href="tel:{C.PHONE_E164}" class="btn btn-call header-call" data-pos="header">{PHONE_ICON} {C.PHONE}</a>
    <button class="menu-btn" aria-expanded="false" aria-controls="mobile-menu" aria-label="{t["menu_open"]}">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h16"/></svg>
    </button>
  </div>
  <nav class="mobile-menu" id="mobile-menu" aria-label="Mobile">
    <ul>
      <li><a href="~/">{"English home" if lang == "zh" else t["home"]}</a></li>{zh_items}
      <li class="sub">{t["services"]}</li>{svc}
      <li class="sub">{t["more"]}</li>
      <li><a href="~/prices/">{t["prices"]}</a></li>
      <li><a href="~/areas/">{t["areas"]}</a></li>
      <li><a href="~/guides/">{t["guides"]}</a></li>
      <li><a href="~/about/">{t["about"]}</a></li>
      {'<li><a href="~/zh/" hreflang="zh-SG">中文 (Chinese)</a></li>' if lang == "en" else ""}
    </ul>
  </nav>
</header>'''


def footer_html(lang="en"):
    t = T[lang]
    svc = "".join(f'<li><a href="~/{s["path"]}">{zh.ZH_NAMES.get(s["path"], s["short"]) if lang == "zh" else s["short"]}</a></li>' for s in content.SERVICES)
    towns = "".join(f'<li><a href="~/areas/{a["slug"]}/">Locksmith {a["name"]}</a></li>' for a in areas.TOWNS[:8])
    gd = "".join(f'<li><a href="~/guides/{g["slug"]}/">{g["short"]}</a></li>' for g in guides.GUIDES[:6])
    email = (f'<li><span class="lbl">{t["email"]}:</span> <a href="mailto:{C.EMAIL}">{C.EMAIL}</a></li>'
             if C.EMAIL else "<!-- FILL: business email in _build/config.py -->")
    uen = f' · {getattr(C, "LEGAL_NAME", C.NAME)} (UEN {C.UEN})' if C.UEN else "<!-- FILL: ACRA UEN in _build/config.py -->"
    return f'''<footer class="footer">
  <div class="container footer-grid">
    <div>
      <div class="footer-brand"><img src="~/assets/img/logo-112.webp" alt="" width="48" height="48" loading="lazy"><div><strong>{C.NAME}</strong><br>{C.SLOGAN}</div></div>
      <ul class="contact-list">
        <li><span class="lbl">{t["hotline"]}:</span> <a href="tel:{C.PHONE_E164}" data-pos="footer">{C.PHONE}</a></li>
        <li><span class="lbl">WhatsApp:</span> <a href="{t["wa_link"]}" target="_blank" rel="noopener" data-pos="footer">{C.PHONE}</a></li>
        {email}
        <li><span class="lbl">{t["hours"]}:</span> {t["hours_v"]}</li>
        <li><span class="lbl">{t["coverage"]}:</span> {t["coverage_v"]}</li>
        <li><a href="{C.GOOGLE_PROFILE}" target="_blank" rel="noopener" class="g-link">{icons.svg("star", cls="bi bi-star", fill=True)} {t["google"]}</a></li>
      </ul>
    </div>
    <div><h2>{t["f_services"]}</h2><ul>{svc}<li><a href="~/prices/">Prices</a></li></ul></div>
    <div><h2>{t["f_areas"]}</h2><ul>{towns}<li><a href="~/areas/">{t["all_areas"]}</a></li></ul></div>
    <div><h2>{t["f_guides"]}</h2><ul>{gd}<li><a href="~/guides/">All guides →</a></li><li><a href="~/about/">About Uncle Thomas</a></li><li><a href="~/zh/" hreflang="zh-SG">中文</a></li></ul></div>
  </div>
  <div class="footer-bottom"><div class="container">© <span data-year>{date.today().year}</span> {C.NAME}{uen} · {t["bottom"]}</div></div>
</footer>
<div class="mobile-bar">
  <a href="tel:{C.PHONE_E164}" class="mobile-btn mobile-call" data-pos="mobile_bar">{PHONE_ICON} {t["call_now"]}</a>
  <a href="{t["wa_link"]}" class="mobile-btn mobile-wa" target="_blank" rel="noopener" data-pos="mobile_bar">{WA_ICON} {t["wa_short"]}</a>
</div>'''


def analytics_head():
    if not C.GA4_ID:
        return "<!-- FILL: Google Analytics 4 ID (GA4_ID in _build/config.py). Analytics is off until set. -->"
    gid = C.GA4_ID
    # gtag is defined immediately (events queue in dataLayer) but the library
    # loads ~1.5s after the page has finished loading, so it never slows LCP.
    return (f"<script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments)}}"
            f"gtag('js',new Date());gtag('config','{gid}');"
            f"addEventListener('load',function(){{setTimeout(function(){{var s=document.createElement('script');"
            f"s.async=1;s.src='https://www.googletagmanager.com/gtag/js?id={gid}';document.head.appendChild(s)}},1500)}});</script>")


def render(path, title, desc, body, schema_nodes, og_type="website", preload_img=None, priority="0.7",
           lang="en", alternates=None):
    """alternates: {"en-SG": path, "zh-SG": path} for pages that have a translation."""
    assert len(title) <= 65, f"Title too long ({len(title)}): {title}"
    assert len(desc) <= 160, f"Description too long ({len(desc)}) on {path}"
    prefix = rel_prefix(path)
    url = abs_url(path)
    graph = {"@context": "https://schema.org", "@graph": schema_nodes}
    pre = f'\n<link rel="preload" as="image" href="~/{preload_img}" type="image/webp" fetchpriority="high">' if preload_img else ""
    hreflang, alt_path = "", None
    if alternates:
        hreflang = "".join(f'\n<link rel="alternate" hreflang="{k}" href="{abs_url(v)}">' for k, v in alternates.items())
        hreflang += f'\n<link rel="alternate" hreflang="x-default" href="{abs_url(alternates["en-SG"])}">'
        alt_path = alternates["zh-SG"] if lang == "en" else alternates["en-SG"]
    html_lang = "zh-SG" if lang == "zh" else "en-SG"
    og_locale = "zh_SG" if lang == "zh" else "en_SG"
    css = CSS.replace("url('assets/", "url('~/assets/")
    doc = f'''<!DOCTYPE html>
<html lang="{html_lang}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{url}">{hreflang}
<meta name="robots" content="index, follow, max-image-preview:large">
<meta name="theme-color" content="#d3a80c">
<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="{C.NAME}">
<meta property="og:locale" content="{og_locale}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{C.SITE}/assets/img/og.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(title)}">
<meta name="twitter:description" content="{esc(desc)}">
<meta name="twitter:image" content="{C.SITE}/assets/img/og.jpg">
<meta name="geo.region" content="SG">
<meta name="geo.placename" content="Singapore">
<link rel="icon" href="~/favicon.ico" sizes="48x48">
<link rel="icon" type="image/png" sizes="32x32" href="~/assets/img/favicon-32.png">
<link rel="apple-touch-icon" href="~/assets/img/apple-touch-icon.png">
<link rel="manifest" href="~/site.webmanifest">
<link rel="preload" href="~/assets/fonts/poppins-latin-800-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="~/assets/fonts/poppins-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin>{pre}
<style>{css}</style>
{analytics_head()}
<script type="application/ld+json">{json.dumps(graph, ensure_ascii=False, separators=(",", ":"))}</script>
</head>
<body>
{header_html(path, lang, alt_path)}
<main id="main">
{body}
</main>
{footer_html(lang)}
<script src="~/script.js?v={C.ASSET_VERSION}" defer></script>
</body>
</html>
'''
    doc = fill(doc, prefix)
    out = os.path.join(ROOT, path, "index.html") if path else os.path.join(ROOT, "index.html")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(doc)
    PAGES.append((path, priority, alternates))


def page_schema(path, title, desc, crumbs, extra=None, faqs=None, page_type="WebPage", lang="en-SG"):
    nodes = [{"@type": page_type, "@id": abs_url(path) + "#webpage", "url": abs_url(path), "name": title,
              "description": desc, "inLanguage": lang, "isPartOf": {"@id": C.SITE + "/#website"},
              "about": {"@id": BUSINESS_ID}, "breadcrumb": {"@id": abs_url(path) + "#breadcrumb"},
              "primaryImageOfPage": {"@type": "ImageObject", "url": C.SITE + "/assets/img/og.jpg"}}]
    bc = breadcrumb_node(crumbs); bc["@id"] = abs_url(path) + "#breadcrumb"
    nodes.append(bc)
    nodes.append(business_node())
    if faqs:
        nodes.append(faq_node(faqs))
    if extra:
        nodes.extend(e for e in extra if e)
    return nodes


def minify_css(css):
    css = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
    css = re.sub(r"\s+", " ", css)
    css = re.sub(r"\s*([{}:;,>])\s*", r"\1", css).replace(";}", "}")
    # restore spaces needed inside media queries ("and(" is invalid)
    css = css.replace("and(", "and (")
    return css.strip()


SCRIPT_JS = """// Uncle Thomas Locksmith — tiny JS: mobile menu, footer year, call/WhatsApp click tracking
(function () {
  var b = document.querySelector('.menu-btn'), m = document.getElementById('mobile-menu');
  if (b && m) b.addEventListener('click', function () {
    var open = m.classList.toggle('open');
    b.setAttribute('aria-expanded', open ? 'true' : 'false');
  });
  var y = document.querySelector('[data-year]');
  if (y) y.textContent = new Date().getFullYear();
  // GA4 events: call_click / whatsapp_click, labelled by page and button position
  document.addEventListener('click', function (e) {
    var a = e.target.closest && e.target.closest('a[href]');
    if (!a || typeof window.gtag !== 'function') return;
    var h = a.getAttribute('href'), ev = null;
    if (h.indexOf('tel:') === 0) ev = 'call_click';
    else if (h.indexOf('wa.me') !== -1) ev = 'whatsapp_click';
    if (!ev) return;
    window.gtag('event', ev, {
      page_label: document.title,
      page_path: location.pathname,
      link_position: a.getAttribute('data-pos') || 'inline',
      transport_type: 'beacon'
    });
  });
})();
"""

HEADERS = """# Cache rules for Netlify / Cloudflare Pages (GitHub Pages ignores this file).
# Assets never change in place: if you replace an image or font, give it a new file name.
/assets/*
  Cache-Control: public, max-age=31536000, immutable

/favicon.ico
  Cache-Control: public, max-age=604800

/script.js
  Cache-Control: public, max-age=604800

# Build sources and notes are uploaded too: keep them out of Google.
/_build/*
  X-Robots-Tag: noindex

/README.md
  X-Robots-Tag: noindex

/.kiro/*
  X-Robots-Tag: noindex

# Pages' default for everything else (HTML) is already "public, max-age=0,
# must-revalidate". Don't set Cache-Control here: Cloudflare merges matching
# rules, so it would clash with the long cache on /assets/* above.
/*
  X-Content-Type-Options: nosniff
  Referrer-Policy: strict-origin-when-cross-origin
"""


# ---------- build ----------
def main():
    global CSS
    CSS = minify_css(open(os.path.join(HERE, "styles.css"), encoding="utf-8").read())
    ctx = dict(C=C, render=render, page_schema=page_schema, page_hero=page_hero, cta_buttons=cta_buttons,
               cta_band=cta_band, faq_html=faq_html, business_node=business_node, person_node=person_node,
               breadcrumb_node=breadcrumb_node, faq_node=faq_node, offer_catalog=offer_catalog, esc=esc,
               areas=areas, guides=guides, content=content, brands=brands, cars=cars, abs_url=abs_url, zh_pages=list(zh.ZH_PAGES),
               BUSINESS_ID=BUSINESS_ID, PERSON_ID=PERSON_ID, photo=photo, photo_schema=photo_schema, photos_schema=photos_schema,
               breadcrumb_html=breadcrumb_html)
    content.build(ctx)
    brands.build(ctx)
    cars.build(ctx)
    areas.build(ctx)
    guides.build(ctx)
    zh.build(ctx)
    zh.build_more(ctx)

    old_css = os.path.join(ROOT, "styles.css")
    if os.path.exists(old_css):
        os.remove(old_css)          # CSS is now inlined into each page
    with open(os.path.join(ROOT, "script.js"), "w") as f:
        f.write(SCRIPT_JS)
    with open(os.path.join(ROOT, "_headers"), "w") as f:
        f.write(HEADERS)

    # 404 page (GitHub Pages serves /404.html)
    four = open(os.path.join(ROOT, "index.html"), encoding="utf-8").read()
    four = re.sub(r"<main id=\"main\">.*</main>", f'''<main id="main"><section class="page-hero"><div class="container narrow">
<h1>Page not found</h1><p class="hero-sub">Sorry, that page doesn't exist. If you're locked out, don't worry — call or WhatsApp Uncle Thomas now, 24/7.</p>
{cta_buttons(pos="404")}<p style="margin-top:22px"><a href="./">← Back to the homepage</a></p></div></section></main>''', four, flags=re.S)
    four = re.sub(r"<title>.*?</title>", f"<title>Page Not Found | {C.NAME}</title>", four)
    four = four.replace('content="index, follow, max-image-preview:large"', 'content="noindex"')
    four = re.sub(r'<link rel="canonical"[^>]*>', "", four)
    four = re.sub(r'<link rel="alternate" hreflang[^>]*>', "", four)
    four = re.sub(r'<script type="application/ld\+json">.*?</script>', "", four, flags=re.S)
    four = four.replace("<head>", "<head>\n<base href=\"" + C.BASE_PATH + "\">", 1)
    with open(os.path.join(ROOT, "404.html"), "w", encoding="utf-8") as f:
        f.write(four)

    # sitemap (with hreflang alternates)
    entries = []
    for p, pr, alts in PAGES:
        x = ""
        if alts:
            x = "".join(f'<xhtml:link rel="alternate" hreflang="{k}" href="{abs_url(v)}"/>' for k, v in alts.items())
            x += f'<xhtml:link rel="alternate" hreflang="x-default" href="{abs_url(alts["en-SG"])}"/>'
        entries.append(f"  <url><loc>{abs_url(p)}</loc><lastmod>{TODAY}</lastmod><priority>{pr}</priority>{x}</url>")
    with open(os.path.join(ROOT, "sitemap.xml"), "w") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
                'xmlns:xhtml="http://www.w3.org/1999/xhtml">\n' + "\n".join(entries) + "\n</urlset>\n")
    with open(os.path.join(ROOT, "robots.txt"), "w") as f:
        f.write(f"User-agent: *\nAllow: /\n\nSitemap: {C.SITE}/sitemap.xml\n")

    with open(os.path.join(ROOT, "site.webmanifest"), "w") as f:
        json.dump({"name": C.NAME, "short_name": "Uncle Thomas", "start_url": "./", "display": "standalone",
                   "background_color": "#ffffff", "theme_color": "#d3a80c",
                   "icons": [{"src": "assets/img/icon-192.png", "sizes": "192x192", "type": "image/png"},
                             {"src": "assets/img/icon-512.png", "sizes": "512x512", "type": "image/png"}]}, f, indent=2)

    # llms.txt (summary for AI assistants / answer engines)
    lines = [f"# {C.NAME}", "", f"> {C.DESCRIPTION}", "",
             f"- Phone / WhatsApp: {C.PHONE} ({C.PHONE_E164}) — 24/7, islandwide Singapore",
             f"- Founded: {C.FOUNDED}. Lead locksmith: Uncle Thomas (US-trained safesmith), with a small team.",
             "- Verifies proof of residence or ownership before opening any door, car or safe.",
             "- Warranty on every lock replacement and installation, with no expiry date.",
             "- Does NOT offer key duplication, key cutting or lock repair. Only exception: clones car key fobs (all major brands)."]
    if C.UEN:
        lines.append(f"- UEN: {C.UEN}")
    if C.EMAIL:
        lines.append(f"- Email: {C.EMAIL}")
    lines += ["", "## Prices (from)"]
    for label, p, price, note in C.PRICES:
        lines.append(f"- {label}: {'S$' + str(price) if isinstance(price, int) else price}")
    groups = [("Main pages", lambda p: p.count("/") <= 1 and not p.startswith(("areas", "guides", "zh"))),
              ("Digital lock brands", lambda p: p.startswith("digital-lock-opening/") and p.count("/") == 2),
              ("Car brands", lambda p: p.startswith("car-locksmith/") and p.count("/") == 2),
              ("Areas", lambda p: p.startswith("areas")),
              ("Guides", lambda p: p.startswith("guides")),
              ("Chinese (中文)", lambda p: p.startswith("zh"))]
    for name, test in groups:
        lines += ["", f"## {name}"] + [f"- {abs_url(p)}" for p, _, _ in PAGES if test(p)]
    with open(os.path.join(ROOT, "llms.txt"), "w") as f:
        f.write("\n".join(lines) + "\n")

    print(f"Built {len(PAGES)} pages.")


if __name__ == "__main__":
    main()
