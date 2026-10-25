#!/usr/bin/env python3
"""
Uncle Thomas Locksmith — static site generator.

HOW TO USE
  python3 _build/build.py

It regenerates every .html page, styles.css, sitemap.xml, robots.txt,
llms.txt and site.webmanifest in the repo root from:
  _build/config.py   business facts, prices, domain (edit here first)
  _build/content.py  page text for home, services, prices, about
  _build/areas.py    town pages
  _build/guides.py   guide articles
  _build/styles.css  the stylesheet

Do NOT hand-edit the generated .html files — edits are overwritten on the
next build. (Folders starting with "_" are not published by GitHub Pages.)
"""
import json, os, re, shutil, sys, html
from datetime import date

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

import config as C
import content, areas, guides

TODAY = date.today().isoformat()
PAGES = []          # (path, priority) for sitemap


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


# ---------- shared schema pieces ----------
BUSINESS_ID = C.SITE + "/#business"
PERSON_ID = C.SITE + "/about/#uncle-thomas"


def business_node(full=False):
    node = {
        "@type": "Locksmith",
        "@id": BUSINESS_ID,
        "name": C.NAME,
        "url": C.SITE + "/",
        "telephone": C.PHONE_E164,
        "image": C.SITE + "/assets/img/logo-640.jpg",
        "logo": C.SITE + "/assets/img/logo-640.jpg",
        "priceRange": "S$" + str(min(p[2] for p in C.PRICES if isinstance(p[2], int))) + "+",
        "address": {"@type": "PostalAddress", "addressLocality": "Singapore", "addressCountry": "SG"},
        "areaServed": {"@type": "Country", "name": "Singapore"},
        "openingHoursSpecification": {
            "@type": "OpeningHoursSpecification",
            "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
            "opens": "00:00", "closes": "23:59"},
    }
    if full:
        node.update({
            "description": C.DESCRIPTION,
            "slogan": C.SLOGAN,
            "email": C.EMAIL,
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
                             "hoursAvailable": {"@type": "OpeningHoursSpecification",
                                                "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
                                                "opens": "00:00", "closes": "23:59"}},
            "sameAs": C.SAME_AS,
        })
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
    return {
        "@type": "Person", "@id": PERSON_ID, "name": "Uncle Thomas",
        "jobTitle": "Master Locksmith & Safesmith",
        "description": "Singapore locksmith since 1998. Trained in safesmithing in the United States; has opened safes on ships and in Thailand, Malaysia, China and Hong Kong.",
        "knowsAbout": ["Locksmithing", "Safesmithing", "Safe opening", "Digital locks"],
        "worksFor": {"@id": BUSINESS_ID},
        "url": C.SITE + "/about/",
        "image": C.SITE + "/assets/img/logo-640.jpg",
    }


def breadcrumb_node(crumbs):
    return {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": abs_url(p)} for i, (n, p) in enumerate(crumbs)]}


def faq_node(faqs):
    return {"@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": strip_tags(a)}} for q, a in faqs]}


def strip_tags(s):
    s = re.sub(r"<[^>]+>", "", s)
    for k, v in C.TOKENS.items():
        s = s.replace("{" + k + "}", v)
    return html.unescape(re.sub(r"\s+", " ", s)).strip()


# ---------- HTML building blocks ----------
WA_ICON = "💬"
PHONE_ICON = "📞"


def cta_buttons(size="btn-lg", center=False, wa_text="WhatsApp Us"):
    return (f'<div class="cta-row{" center" if center else ""}">'
            f'<a href="tel:{C.PHONE_E164}" class="btn btn-call {size}">{PHONE_ICON} Call {C.PHONE}</a>'
            f'<a href="{C.WA_LINK}" class="btn btn-wa {size}" target="_blank" rel="noopener">{WA_ICON} {wa_text}</a></div>')


def faq_html(faqs, title="Frequently Asked Questions"):
    out = [f'<h2 class="section-title">{title}</h2><div style="margin-top:28px">']
    for q, a in faqs:
        out.append(f'<details class="faq"><summary>{esc(q)}</summary><div class="faq-a"><p>{a}</p></div></details>')
    out.append("</div>")
    return "".join(out)


def cta_band(title="Need a Locksmith Right Now?", lead=None):
    lead = lead or f"Call or WhatsApp Uncle Thomas — 24/7, islandwide. We set off as soon as you call."
    return (f'<section class="section cta-band"><div class="container narrow">'
            f'<h2 class="section-title">{title}</h2><p class="section-lead">{lead}</p>'
            f'{cta_buttons(center=True, wa_text="WhatsApp " + C.PHONE)}</div></section>')


def breadcrumb_html(crumbs):
    items = []
    for i, (n, p) in enumerate(crumbs):
        if i == len(crumbs) - 1:
            items.append(f'<li aria-current="page">{esc(n)}</li>')
        else:
            items.append(f'<li><a href="~/{p}">{esc(n)}</a></li>')
    return f'<nav class="breadcrumb" aria-label="Breadcrumb"><ol>{"".join(items)}</ol></nav>'


def page_hero(crumbs, h1, sub, badges=None):
    b = ""
    if badges:
        b = '<ul class="badges">' + "".join(f"<li>{x}</li>" for x in badges) + "</ul>"
    return (f'<section class="page-hero"><div class="container">{breadcrumb_html(crumbs)}'
            f'<h1>{h1}</h1><p class="hero-sub">{sub}</p>{cta_buttons()}{b}</div></section>')


NAV = [("Services", "services/"), ("Prices", "prices/"), ("Areas", "areas/"),
       ("Guides", "guides/"), ("About", "about/")]


def header_html(path):
    nav = []
    for label, p in NAV:
        cur = ' aria-current="page"' if path == p or (path.startswith(p) and p != "") else ""
        nav.append(f'<a href="~/{p}"{cur}>{label}</a>')
    svc = "".join(f'<li><a href="~/{s["path"]}">{s["short"]}</a></li>' for s in content.SERVICES)
    return f'''<a class="skip" href="#main">Skip to content</a>
<div class="topbar"><span class="long">24/7 Emergency Locksmith · Islandwide Singapore · Since {C.FOUNDED}</span><span class="short">24/7 · Islandwide · Since {C.FOUNDED}</span></div>
<header class="header">
  <div class="container header-inner">
    <a href="~/" class="brand" aria-label="{C.NAME} — home">
      <picture><source srcset="~/assets/img/logo-112.webp" type="image/webp"><img src="~/assets/img/logo-112.png" alt="{C.NAME} logo" width="52" height="52"></picture>
      <span class="brand-text"><strong>Uncle Thomas</strong><small>Locksmith · Since {C.FOUNDED}</small></span>
    </a>
    <nav class="nav" aria-label="Main">{"".join(nav)}</nav>
    <a href="tel:{C.PHONE_E164}" class="btn btn-call header-call">{PHONE_ICON} {C.PHONE}</a>
    <button class="menu-btn" aria-expanded="false" aria-controls="mobile-menu" aria-label="Open menu">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h16"/></svg>
    </button>
  </div>
  <nav class="mobile-menu" id="mobile-menu" aria-label="Mobile">
    <ul>
      <li><a href="~/">Home</a></li>
      <li class="sub">Services</li>{svc}
      <li class="sub">More</li>
      <li><a href="~/prices/">Prices</a></li>
      <li><a href="~/areas/">Areas we serve</a></li>
      <li><a href="~/guides/">Guides</a></li>
      <li><a href="~/about/">About Uncle Thomas</a></li>
    </ul>
  </nav>
</header>'''


def footer_html():
    svc = "".join(f'<li><a href="~/{s["path"]}">{s["short"]}</a></li>' for s in content.SERVICES)
    towns = "".join(f'<li><a href="~/areas/{t["slug"]}/">Locksmith {t["name"]}</a></li>' for t in areas.TOWNS[:8])
    gd = "".join(f'<li><a href="~/guides/{g["slug"]}/">{g["short"]}</a></li>' for g in guides.GUIDES)
    return f'''<footer class="footer">
  <div class="container footer-grid">
    <div>
      <div class="footer-brand"><img src="~/assets/img/logo-112.webp" alt="" width="48" height="48" loading="lazy"><div><strong>{C.NAME}</strong><br>{C.SLOGAN}</div></div>
      <p><strong style="color:#fff">24/7 hotline:</strong> <a href="tel:{C.PHONE_E164}">{C.PHONE}</a><br>
      <strong style="color:#fff">WhatsApp:</strong> <a href="{C.WA_LINK}" target="_blank" rel="noopener">{C.PHONE}</a><br>
      <strong style="color:#fff">Email:</strong> <a href="mailto:{C.EMAIL}">{C.EMAIL}</a><br>
      <strong style="color:#fff">Hours:</strong> 24 hours, 7 days, incl. public holidays<br>
      <strong style="color:#fff">Coverage:</strong> Islandwide Singapore</p>
      <p style="margin-top:10px"><a href="{C.GOOGLE_PROFILE}" target="_blank" rel="noopener">★ Find us on Google</a></p>
    </div>
    <div><h2>Services</h2><ul>{svc}<li><a href="~/prices/">Prices</a></li></ul></div>
    <div><h2>Areas</h2><ul>{towns}<li><a href="~/areas/">All areas →</a></li></ul></div>
    <div><h2>Guides</h2><ul>{gd}<li><a href="~/about/">About Uncle Thomas</a></li></ul></div>
  </div>
  <div class="footer-bottom"><div class="container">© <span data-year>{date.today().year}</span> {C.NAME} · Singapore · 24/7 Emergency Locksmith</div></div>
</footer>
<div class="mobile-bar">
  <a href="tel:{C.PHONE_E164}" class="mobile-btn mobile-call">{PHONE_ICON} Call Now</a>
  <a href="{C.WA_LINK}" class="mobile-btn mobile-wa" target="_blank" rel="noopener">{WA_ICON} WhatsApp</a>
</div>'''


def render(path, title, desc, body, schema_nodes, og_type="website", preload_img=None, priority="0.7"):
    assert len(title) <= 65, f"Title too long ({len(title)}): {title}"
    assert len(desc) <= 160, f"Description too long ({len(desc)}) on {path}"
    prefix = rel_prefix(path)
    url = abs_url(path)
    graph = {"@context": "https://schema.org", "@graph": schema_nodes}
    pre = f'\n<link rel="preload" as="image" href="~/{preload_img}" type="image/webp" fetchpriority="high">' if preload_img else ""
    doc = f'''<!DOCTYPE html>
<html lang="en-SG">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{url}">
<meta name="robots" content="index, follow, max-image-preview:large">
<meta name="theme-color" content="#d3a80c">
<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="{C.NAME}">
<meta property="og:locale" content="en_SG">
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
<link rel="stylesheet" href="~/styles.css?v={C.ASSET_VERSION}">
<script type="application/ld+json">{json.dumps(graph, ensure_ascii=False, separators=(",", ":"))}</script>
</head>
<body>
{header_html(path)}
<main id="main">
{body}
</main>
{footer_html()}
<script src="~/script.js?v={C.ASSET_VERSION}" defer></script>
</body>
</html>
'''
    doc = fill(doc, prefix)
    out = os.path.join(ROOT, path, "index.html") if path else os.path.join(ROOT, "index.html")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(doc)
    PAGES.append((path, priority))


def page_schema(path, title, desc, crumbs, extra=None, faqs=None, page_type="WebPage"):
    nodes = [{"@type": page_type, "@id": abs_url(path) + "#webpage", "url": abs_url(path), "name": title,
              "description": desc, "inLanguage": "en-SG", "isPartOf": {"@id": C.SITE + "/#website"},
              "about": {"@id": BUSINESS_ID}, "breadcrumb": {"@id": abs_url(path) + "#breadcrumb"},
              "primaryImageOfPage": {"@type": "ImageObject", "url": C.SITE + "/assets/img/og.jpg"}}]
    bc = breadcrumb_node(crumbs); bc["@id"] = abs_url(path) + "#breadcrumb"
    nodes.append(bc)
    nodes.append(business_node())
    if faqs:
        nodes.append(faq_node(faqs))
    if extra:
        nodes.extend(extra)
    return nodes


# ---------- build ----------
def main():
    ctx = dict(C=C, render=render, page_schema=page_schema, page_hero=page_hero, cta_buttons=cta_buttons,
               cta_band=cta_band, faq_html=faq_html, business_node=business_node, person_node=person_node,
               breadcrumb_node=breadcrumb_node, faq_node=faq_node, offer_catalog=offer_catalog, esc=esc,
               areas=areas, guides=guides, content=content, abs_url=abs_url, BUSINESS_ID=BUSINESS_ID,
               PERSON_ID=PERSON_ID)
    content.build(ctx)
    areas.build(ctx)
    guides.build(ctx)

    # stylesheet + script
    css = open(os.path.join(HERE, "styles.css"), encoding="utf-8").read()
    css = re.sub(r"/\*.*?\*/", "", css, flags=re.S)          # strip comments
    css = re.sub(r"\s+", " ", css)
    css = re.sub(r"\s*([{}:;,>])\s*", r"\1", css).replace(";}", "}")
    with open(os.path.join(ROOT, "styles.css"), "w", encoding="utf-8") as f:
        f.write("/* Generated from _build/styles.css - edit that file, then run python3 _build/build.py */\n" + css.strip() + "\n")
    with open(os.path.join(ROOT, "script.js"), "w") as f:
        f.write("""// Uncle Thomas Locksmith — tiny JS (mobile menu + footer year)
(function () {
  var b = document.querySelector('.menu-btn'), m = document.getElementById('mobile-menu');
  if (b && m) b.addEventListener('click', function () {
    var open = m.classList.toggle('open');
    b.setAttribute('aria-expanded', open ? 'true' : 'false');
    b.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
  });
  var y = document.querySelector('[data-year]');
  if (y) y.textContent = new Date().getFullYear();
})();
""")

    # 404 page (GitHub Pages serves /404.html)
    four = open(os.path.join(ROOT, "index.html"), encoding="utf-8").read()
    four = re.sub(r"<main id=\"main\">.*</main>", f'''<main id="main"><section class="page-hero"><div class="container narrow">
<h1>Page not found</h1><p class="hero-sub">Sorry, that page doesn't exist. If you're locked out, don't worry — call or WhatsApp Uncle Thomas now, 24/7.</p>
{cta_buttons()}<p style="margin-top:22px"><a href="./">← Back to the homepage</a></p></div></section></main>''', four, flags=re.S)
    four = re.sub(r"<title>.*?</title>", f"<title>Page Not Found | {C.NAME}</title>", four)
    four = four.replace('content="index, follow, max-image-preview:large"', 'content="noindex"')
    four = re.sub(r'<link rel="canonical"[^>]*>\n', "", four)
    # make relative links work from any URL depth: rewrite to site-root-relative using base path
    four = four.replace("<head>", "<head>\n<base href=\"" + C.BASE_PATH + "\">", 1)
    with open(os.path.join(ROOT, "404.html"), "w", encoding="utf-8") as f:
        f.write(four)

    # sitemap
    urls = "\n".join(f"  <url><loc>{abs_url(p)}</loc><lastmod>{TODAY}</lastmod><priority>{pr}</priority></url>"
                     for p, pr in PAGES)
    with open(os.path.join(ROOT, "sitemap.xml"), "w") as f:
        f.write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}\n</urlset>\n')
    with open(os.path.join(ROOT, "robots.txt"), "w") as f:
        f.write(f"User-agent: *\nAllow: /\n\nSitemap: {C.SITE}/sitemap.xml\n")

    # manifest
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
             "- Does NOT offer key duplication or lock repair.", "", "## Prices (from)"]
    for label, p, price, note in C.PRICES:
        lines.append(f"- {label}: {'S$' + str(price) if isinstance(price, int) else price}")
    lines += ["", "## Pages"]
    for p, _ in PAGES:
        lines.append(f"- {abs_url(p)}")
    with open(os.path.join(ROOT, "llms.txt"), "w") as f:
        f.write("\n".join(lines) + "\n")

    print(f"Built {len(PAGES)} pages.")


if __name__ == "__main__":
    main()
