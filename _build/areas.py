"""
Areas hub + individual town pages.
Each town has genuinely local text (estates, housing, MRT, common jobs) so the
pages are useful, not copy-paste "doorway" pages. Add a town by appending to TOWNS.
"""

TOWNS = [
dict(slug="toa-payoh", name="Toa Payoh", region="Central",
 places=["Toa Payoh Central", "Lorong 1–8", "Kim Keat", "Bidadari", "Braddell", "Caldecott"],
 mrt=["Toa Payoh", "Braddell", "Caldecott"],
 intro="Toa Payoh is one of Singapore's oldest HDB towns, so many homes here still have the original main door and gate locks — and older locks are the ones most likely to jam, wear out or snap a key.",
 housing="Most calls here come from HDB flats around Toa Payoh Central and the Lorong blocks, along with the newer Bidadari BTO estates and private homes towards Braddell and Caldecott.",
 jobs=["Worn HDB main door locks that jam or won't turn", "Metal gate locks rusted after years of corridor washing", "Digital lock upgrades in older flats", "Toilet and bedroom doors locked from inside"],
 nearby=["bishan", "ang-mo-kio", "serangoon"]),
dict(slug="ang-mo-kio", name="Ang Mo Kio", region="North-East",
 places=["Ang Mo Kio Central", "AMK Avenues 1–10", "Teck Ghee", "Cheng San", "Kebun Baru", "Yio Chu Kang", "Mayflower"],
 mrt=["Ang Mo Kio", "Yio Chu Kang", "Mayflower"],
 intro="Ang Mo Kio is a large, mature estate where long-time residents and young families live side by side — which means we see everything from decades-old mechanical locks to brand-new digital locks.",
 housing="We regularly help residents in the HDB blocks along the AMK Avenues, around AMK Hub, Teck Ghee and Cheng San, and private homes near Yio Chu Kang and Mayflower.",
 jobs=["Elderly residents locked out after the door swung shut", "Digital lock batteries going flat", "Letterbox lock replacements", "Main door lock changes after moving in"],
 nearby=["bishan", "toa-payoh", "serangoon", "yishun"]),
dict(slug="bishan", name="Bishan", region="Central",
 places=["Bishan Streets 11–24", "Bishan Central", "Sin Ming", "Marymount", "Upper Thomson"],
 mrt=["Bishan", "Marymount", "Upper Thomson"],
 intro="Bishan mixes HDB estates, private condominiums and landed homes towards Thomson, plus workshops and offices around Sin Ming — so jobs here range from home lockouts to commercial locks and safes.",
 housing="Calls come from the HDB blocks around Bishan Central and Junction 8, condos along Bishan and Sin Ming, and landed homes near Upper Thomson and Marymount.",
 jobs=["Condo main door and digital lock lockouts", "Landed home gate and side door locks", "Office and workshop lock changes in Sin Ming", "Home safe opening"],
 nearby=["toa-payoh", "ang-mo-kio", "serangoon"]),
dict(slug="serangoon", name="Serangoon", region="North-East",
 places=["Serangoon Central", "Serangoon North", "Serangoon Gardens", "Lorong Chuan", "Upper Serangoon"],
 mrt=["Serangoon", "Lorong Chuan"],
 intro="Serangoon combines busy HDB estates around Serangoon Central with the landed homes of Serangoon Gardens — two very different kinds of locks, both of which Uncle Thomas handles every week.",
 housing="We help HDB residents near Serangoon Central and Serangoon North, condo owners along Lorong Chuan, and landed homeowners in Serangoon Gardens.",
 jobs=["Landed home main gate and door lockouts", "Digital lock installation on condo doors", "HDB gate lock replacements", "Car lockouts at shopping centre carparks"],
 nearby=["hougang", "ang-mo-kio", "bishan"]),
dict(slug="hougang", name="Hougang", region="North-East",
 places=["Hougang Central", "Hougang Avenues", "Kovan", "Buangkok", "Upper Serangoon Road"],
 mrt=["Hougang", "Kovan", "Buangkok"],
 intro="Hougang is a mature, family-heavy town where many flats have been home to the same family for decades — and where newer blocks near Buangkok have brought plenty of digital locks.",
 housing="Our calls come from HDB estates around Hougang Central and the Hougang Avenues, the shophouses and condos near Kovan, and newer blocks around Buangkok.",
 jobs=["Old main door locks replaced with new locks", "Digital lock lockouts in newer flats", "Shophouse and shop lockouts near Kovan", "Children locked in bedrooms or toilets"],
 nearby=["serangoon", "sengkang", "punggol"]),
dict(slug="sengkang", name="Sengkang", region="North-East",
 places=["Compassvale", "Rivervale", "Anchorvale", "Fernvale", "Sengkang Central"],
 mrt=["Sengkang", "Buangkok", "Sengkang LRT"],
 intro="Sengkang is a younger town full of families in BTO flats — and many of those flats have digital locks on the main door or gate, which means flat batteries and forgotten PINs are common calls.",
 housing="We regularly help residents in Compassvale, Rivervale, Anchorvale and Fernvale, and in the condos around Sengkang Central.",
 jobs=["Digital lock battery flat or keypad not responding", "Digital lock installation on BTO doors and gates", "Kids locked in rooms", "Letterbox lock replacements"],
 nearby=["punggol", "hougang", "serangoon"]),
dict(slug="punggol", name="Punggol", region="North-East",
 places=["Punggol Waterway", "Northshore", "Sumang", "Matilda", "Punggol Digital District"],
 mrt=["Punggol", "Punggol LRT"],
 intro="Punggol is Singapore's newest waterfront town, with modern BTO flats and condos — and a high share of digital locks, many installed at key collection.",
 housing="We help residents across the Waterway and Northshore estates, the Sumang and Matilda neighbourhoods, condos along the waterfront, and businesses in the Punggol Digital District.",
 jobs=["Digital lock lockouts and forgotten PINs", "Replacing or upgrading digital locks fitted at key collection", "Gate digital lock installation", "Office and shop locks in the Digital District"],
 nearby=["sengkang", "hougang"]),
dict(slug="tampines", name="Tampines", region="East",
 places=["Tampines Central", "Tampines North", "Tampines East", "Tampines West", "Simei"],
 mrt=["Tampines", "Tampines East", "Tampines West", "Simei"],
 intro="Tampines is one of Singapore's biggest towns — from mature estates around Tampines Central to brand-new BTO flats in Tampines North — so we see the full range of locks here.",
 housing="Calls come from HDB estates across Tampines North, East, West and Central, condos near Simei, and offices and shops around the Tampines regional centre.",
 jobs=["HDB main door and gate lockouts", "Digital lock installation in new Tampines North flats", "Office lockouts in the regional centre", "Car lockouts at mall carparks"],
 nearby=["bedok"]),
dict(slug="bedok", name="Bedok", region="East",
 places=["Bedok North", "Bedok South", "Bedok Reservoir", "Chai Chee", "Kaki Bukit", "Siglap"],
 mrt=["Bedok", "Tanah Merah", "Kembangan", "Bedok North", "Bedok Reservoir"],
 intro="Bedok has a bit of everything — mature HDB estates, private condos, landed homes around Siglap, and industrial units in Kaki Bukit — so our work here covers homes, cars and businesses.",
 housing="We help HDB residents in Bedok North, Bedok South and Chai Chee, landed homeowners in Siglap and Frankel, and businesses in Kaki Bukit.",
 jobs=["Landed home gate and door locks", "Warehouse and factory lock changes in Kaki Bukit", "HDB lockouts at night", "Safe opening for homes and businesses"],
 nearby=["tampines"]),
dict(slug="jurong", name="Jurong East & Jurong West", region="West",
 places=["Jurong Gateway", "Teban Gardens", "Yuhua", "Boon Lay", "Pioneer", "Jurong West Streets"],
 mrt=["Jurong East", "Chinese Garden", "Lakeside", "Boon Lay", "Pioneer"],
 intro="Jurong covers both the busy Jurong Gateway business district and the large HDB estates of Jurong West — plus Singapore's biggest industrial zone, where safes and commercial locks are a regular part of our work.",
 housing="We help residents in Jurong East (Teban Gardens, Yuhua) and Jurong West (Boon Lay, Pioneer and the Jurong West Streets), offices around Jurong Gateway, and factories and warehouses in the Jurong industrial estates.",
 jobs=["HDB lockouts in Jurong West", "Office lockouts around Jurong Gateway", "Factory, warehouse and safe opening in the industrial estates", "Car lockouts at mall and industrial carparks"],
 nearby=["woodlands"]),
dict(slug="woodlands", name="Woodlands", region="North",
 places=["Woodlands Central", "Marsiling", "Admiralty", "Woodlands North", "Woodlands South"],
 mrt=["Woodlands", "Marsiling", "Admiralty", "Woodlands North", "Woodlands South"],
 intro="Woodlands is a large northern town with mature estates around Marsiling and newer flats towards Woodlands North — and a lot of residents who commute across the Causeway at odd hours.",
 housing="We help residents in Woodlands Central, Marsiling, Admiralty and Woodlands North and South, as well as businesses in the Woodlands industrial areas.",
 jobs=["Late-night lockouts after returning from Johor", "Digital lock battery and keypad problems", "HDB gate and main door lock replacement", "Industrial unit lock changes"],
 nearby=["yishun"]),
dict(slug="yishun", name="Yishun", region="North",
 places=["Yishun Central", "Khatib", "Chong Pang", "Nee Soon", "Yishun Ring Road"],
 mrt=["Yishun", "Khatib"],
 intro="Yishun has grown fast, with new BTO estates alongside long-established blocks around Chong Pang and Nee Soon — a mix of digital locks and older mechanical locks.",
 housing="Calls come from HDB estates around Yishun Central and Northpoint, Khatib, Chong Pang and Nee Soon, and the newer BTO projects across the town.",
 jobs=["Digital lock lockouts in new BTO flats", "Older main door locks jamming", "Letterbox lock replacements", "Bedroom and toilet doors locked from inside"],
 nearby=["woodlands", "ang-mo-kio"]),
]

TOWN_BY_SLUG = {t["slug"]: t for t in TOWNS}

# Towns without their own page yet (listed on the hub so every searcher sees coverage)
OTHER_TOWNS = {
 "Central": ["CBD & Raffles Place", "Orchard", "Novena", "Bukit Timah", "Tanglin", "Queenstown", "Bukit Merah", "Kallang & Whampoa", "Marine Parade", "Geylang"],
 "East": ["Pasir Ris", "Changi", "Katong", "Paya Lebar"],
 "West": ["Clementi", "Bukit Batok", "Bukit Panjang", "Choa Chu Kang", "Tengah"],
 "North": ["Sembawang", "Canberra", "Kranji"],
 "North-East": ["Seletar Hills", "Lentor"],
}


def build(x):
    C = x["C"]
    content = x["content"]
    regions = ["Central", "East", "West", "North", "North-East"]

    # ---- hub ----
    crumbs = [("Home", ""), ("Areas", "areas/")]
    title = "Locksmith Near Me Singapore | Every Town, 24/7 | Uncle Thomas"
    desc = "Need a locksmith near you? Uncle Thomas covers every town in Singapore 24/7 — Toa Payoh, Ang Mo Kio, Tampines, Jurong, Woodlands and more. Call 9224 9224."
    cards = []
    for r in regions:
        linked = "".join(f'<a href="~/areas/{t["slug"]}/">{t["name"]}</a>' for t in TOWNS if t["region"] == r)
        other = "".join(f"<span>{n}</span>" for n in OTHER_TOWNS.get(r, []))
        cards.append(f'<div class="card area-card"><h3>{r}</h3><div class="town-links">{linked}{other}</div></div>')
    body = (x["page_hero"](crumbs, "Locksmith Near Me — Every Town in Singapore",
            "Wherever you are on the island, Uncle Thomas and his team can reach you — 24 hours a day, including weekends and public holidays.",
            ["24/7 islandwide", "We set off immediately", "From {P_LOCKOUT}"]) +
            f'''<section class="section"><div class="container"><h2 class="section-title">Areas We Serve</h2>
<p class="section-lead">Tap your town for local details. Don't see your area? We still cover it — every part of Singapore.</p>
<div class="grid g3">{"".join(cards)}</div>
<div class="prose" style="max-width:820px;margin:40px auto 0">
<h2>Why "near me" matters less for a mobile locksmith</h2>
<p>A locksmith doesn't need a shop next to you — what matters is that someone sets off the moment you call. Uncle Thomas's team works on the move across the island, so whether you're in an HDB flat in the heartlands, a condo in town or an industrial unit in the west, we come to you. Call or WhatsApp <a href="{C.WA_LINK}" target="_blank" rel="noopener">{C.PHONE}</a> with your location and we'll give you an honest arrival estimate and the price before we leave.</p>
</div></div></section>''' + x["cta_band"]())
    nodes = x["page_schema"]("areas/", title, desc, crumbs, page_type="CollectionPage", extra=[
        {"@type": "ItemList", "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "url": C.SITE + f"/areas/{t['slug']}/", "name": "Locksmith " + t["name"]}
            for i, t in enumerate(TOWNS)]}])
    x["render"]("areas/", title, desc, body, nodes, priority="0.8")

    # ---- town pages ----
    for t in TOWNS:
        path = f"areas/{t['slug']}/"
        n = t["name"]
        crumbs = [("Home", ""), ("Areas", "areas/"), (n, path)]
        title = f"Locksmith {n} 24/7 | Doors, Digital Locks & Safes"
        if len(title) > 60:
            title = f"Locksmith {n} 24/7 | Uncle Thomas"
        desc = f"24/7 locksmith in {n} — door lockouts, digital locks, safes and car lockouts. Uncle Thomas sets off as soon as you call. From S$80. Call 9224 9224."
        if len(desc) > 158:
            desc = f"24/7 locksmith in {n}: lockouts, digital locks, safes & cars. We set off as soon as you call. From S$80. Call 9224 9224."
        places = "".join(f"<li>{p}</li>" for p in t["places"])
        jobs = "".join(f"<li>{j}</li>" for j in t["jobs"])
        near = [TOWN_BY_SLUG[s] for s in t["nearby"] if s in TOWN_BY_SLUG]
        near_html = ", ".join(f'<a href="~/areas/{m["slug"]}/">{m["name"]}</a>' for m in near)
        svc_links = "".join(f'<li><a href="~/{s["path"]}">{s["short"]} in {n}</a> — from {C.price(s["path"])}</li>'
                            for s in content.SERVICES)
        faqs = [
            (f"Do you have a locksmith in {n} right now?", f"Yes. Uncle Thomas Locksmith works 24/7 across {n} and the rest of Singapore. Call or WhatsApp {{PHONE}} and we set off as soon as you call."),
            (f"How much does a locksmith in {n} cost?", "The same as anywhere in Singapore — lockouts from {P_LOCKOUT} (9am–6pm) and {P_AFTERHOURS} after hours. We confirm the price before we start."),
            (f"Do you serve all of {n}?", f"Yes — including {', '.join(t['places'][:4])} and the surrounding estates."),
        ]
        body = (x["page_hero"](crumbs, f"Locksmith in {n} — 24/7 Emergency Service",
                f"Locked out in {n}? {t['intro']}", ["24/7 incl. public holidays", "From {P_LOCKOUT}", "ID verified"]) +
                f'''<section class="section"><div class="container narrow prose">
<h2>Locksmith services across {n}</h2>
<p>{t["housing"]}</p>
<ul class="tags">{places}</ul>
<p>Nearest MRT/LRT: {", ".join(t["mrt"])}. We come to you — just send your block or address.</p>

<h2>Jobs we often do in {n}</h2>
<ul>{jobs}</ul>

<h2>Our services in {n}</h2>
<ul>{svc_links}</ul>

<div class="callout"><p><strong>Price before work, ID checked:</strong> we confirm the price before we start, and check proof of residence or ownership before opening any door, car or safe. Every lock replacement and installation comes with our no-expiry warranty.</p></div>

<h2>Led by Uncle Thomas — {{YEARS}}+ years in the trade</h2>
<p>Uncle Thomas has been a locksmith since {{FOUNDED}}, trained in safesmithing in the United States, and is known in the trade as "Shifu". He and his small team serve {n} and every other part of Singapore. <a href="~/about/">Read his story</a>.</p>
{"<p>We also serve nearby " + near_html + ".</p>" if near_html else ""}
</div></section>
<section class="section section-alt"><div class="container narrow">{x["faq_html"](faqs, f"{n} Locksmith FAQs")}</div></section>''' +
                x["cta_band"](f"Need a Locksmith in {n} Now?"))
        svc = {"@type": "Service", "@id": C.SITE + "/" + path + "#service", "name": f"Locksmith in {n}",
               "serviceType": "Locksmith", "provider": {"@id": x["BUSINESS_ID"]},
               "areaServed": {"@type": "Place", "name": f"{n}, Singapore"}, "url": C.SITE + "/" + path}
        nodes = x["page_schema"](path, title, desc, crumbs, faqs=faqs, extra=[svc])
        x["render"](path, title, desc, body, nodes, priority="0.7")
