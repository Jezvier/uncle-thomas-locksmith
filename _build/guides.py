"""
Guides: short, genuinely helpful articles people search for at the moment they
need a locksmith. Written for the owner of the lock — never break-in techniques.
"""

from guides_a import GUIDES_A
from guides_b import GUIDES_B
from guides_c import GUIDES_C
from guides_d import GUIDES_D

GUIDES = GUIDES_A + GUIDES_B + GUIDES_C + GUIDES_D
from guides_extra import EXTRA, TAKEAWAYS, MORE_FAQS
for _g in GUIDES:
    _extra = EXTRA.get(_g["slug"], "")
    if _extra:
        _k = _g["body"].rfind('<div class="callout navy">')
        _g["body"] = _g["body"][:_k] + _extra + _g["body"][_k:] if _k != -1 else _g["body"] + _extra
    if _g["slug"] in TAKEAWAYS:
        _g["body"] = ('<div class="toc"><strong>Key takeaways</strong><ul>' +
                      "".join(f"<li>{t}</li>" for t in TAKEAWAYS[_g["slug"]]) + "</ul></div>" + _g["body"])
    if _g["slug"] in MORE_FAQS:
        _g["faqs"] = _g["faqs"] + [MORE_FAQS[_g["slug"]]]
PUBLISHED = {g["slug"]: ("2026-10-25" if i < 4 else "2026-10-26") for i, g in enumerate(GUIDES_A + GUIDES_B)}
PUBLISHED.update({g["slug"]: "2026-10-27" for g in GUIDES_C + GUIDES_D})

def _modified(path, slug):
    """Date the guide's content last changed (tracked by build.py in lastmod.json)."""
    import json, os
    try:
        lm = json.load(open(os.path.join(os.path.dirname(__file__), "lastmod.json")))
        return max(lm.get(path, {}).get("date", PUBLISHED[slug]), PUBLISHED[slug])
    except (OSError, ValueError):
        return PUBLISHED[slug]


def build(x):
    C = x["C"]
    # hub
    crumbs = [("Home", ""), ("Guides", "guides/")]
    title = "Locksmith Guides Singapore | Lockouts, Digital Locks & Safes"
    desc = "Practical guides from Uncle Thomas, a Singapore locksmith since 1998: what to do when locked out, digital lock problems, forgotten safe codes and more."
    cards = "".join(f'<a class="card" href="~/guides/{g["slug"]}/"><h3>{g["h1"]}</h3><p>{g["card"]}</p><span class="more">Read the guide →</span></a>' for g in GUIDES)
    body = (x["page_hero"](crumbs, "Locksmith Guides", "Practical, honest advice for when something goes wrong with a lock — written by a locksmith with {YEARS}+ years in the trade.") +
            f'<section class="section"><div class="container"><div class="grid g2">{cards}</div></div></section>' + x["cta_band"]())
    nodes = x["page_schema"]("guides/", title, desc, crumbs, page_type="CollectionPage")
    x["render"]("guides/", title, desc, body, nodes, priority="0.6")

    for g in GUIDES:
        path = f"guides/{g['slug']}/"
        crumbs = [("Home", ""), ("Guides", "guides/"), (g["short"], path)]
        assert len(g["title"]) <= 65, g["title"]
        body = (f'<section class="page-hero"><div class="container narrow">{_bc(crumbs)}<h1>{g["h1"]}</h1>'
                f'<p class="meta-line">By <a href="~/about/">Uncle Thomas</a>, locksmith since {{FOUNDED}} · Updated {{MONTH_YEAR}}</p>'
                f'{x["cta_buttons"]("")}</div></section>'
                f'<article class="section"><div class="container narrow prose">{g["body"]}</div></article>'
                f'<section class="section section-alt"><div class="container narrow">{x["faq_html"](g["faqs"], "Quick Answers")}</div></section>' +
                x["cta_band"]())
        art = {"@type": "Article", "@id": C.SITE + "/" + path + "#article", "headline": g["h1"], "description": g["desc"],
               "author": {"@id": x["PERSON_ID"]}, "publisher": {"@id": x["BUSINESS_ID"]},
               "datePublished": PUBLISHED[g["slug"]], "dateModified": _modified(path, g["slug"]),
               "mainEntityOfPage": C.SITE + "/" + path, "image": C.SITE + "/assets/img/og-2026.jpg", "inLanguage": "en-SG"}
        nodes = x["page_schema"](path, g["title"], g["desc"], crumbs, faqs=g["faqs"], extra=[art, x["person_node"]()])
        x["render"](path, g["title"], g["desc"], body, nodes, og_type="article", priority="0.6")


def _bc(crumbs):
    items = []
    for i, (n, p) in enumerate(crumbs):
        items.append(f'<li aria-current="page">{n}</li>' if i == len(crumbs) - 1 else f'<li><a href="~/{p}">{n}</a></li>')
    return f'<nav class="breadcrumb" aria-label="Breadcrumb"><ol>{"".join(items)}</ol></nav>'
