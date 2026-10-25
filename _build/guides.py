"""
Guides: short, genuinely helpful articles people search for at the moment they
need a locksmith. Written for the owner of the lock — never break-in techniques.
"""

GUIDES = [
dict(
 slug="locked-out-of-hdb-flat", short="Locked out of an HDB flat",
 title="Locked Out of Your HDB Flat? What to Do (Step by Step)",
 desc="Locked out of your HDB flat in Singapore? A locksmith's step-by-step checklist: what to try first, what to have ready, what it costs and how to avoid it.",
 h1="Locked Out of Your HDB Flat? What to Do, Step by Step",
 card="A calm checklist from a locksmith: what to try, what to have ready, and what it should cost.",
 body="""
<p>Getting locked out is stressful, especially late at night or with kids or elderly family inside. Here's what Uncle Thomas — a locksmith since 1998 — recommends, in order.</p>

<h2>1. Stay calm and check for anyone at risk</h2>
<p>If a child, an elderly person or someone unwell is alone inside, or you smell gas or see smoke, call <strong>995</strong> immediately. The SCDF handles emergencies where lives may be at risk.</p>

<h2>2. Check the easy options</h2>
<ul>
<li><strong>Is anyone else home or nearby</strong> with a key — family, a helper or a flatmate?</li>
<li><strong>Did you leave a spare key</strong> with a relative or neighbour?</li>
<li><strong>Is the gate locked but the door open</strong>, or the other way round? Different locks need different help.</li>
<li><strong>Digital lock?</strong> Try the steps in our <a href="~/guides/digital-lock-battery-dead/">digital lock guide</a> — a flat battery is the most common cause.</li>
</ul>

<h2>3. Don't force the door</h2>
<p>Kicking the door, prying the gate or poking the lock with a card or wire usually breaks the lock — turning a simple lockout into a lock replacement. HDB main doors are also fire-rated, so a damaged door can be costly to fix.</p>

<h2>4. Call a locksmith — and ask the price first</h2>
<p>When you call, ask for the <strong>total price before anyone sets off</strong>. A good locksmith will ask what type of lock you have (a photo on WhatsApp helps) and give you a clear figure. For reference, our lockouts start from {P_LOCKOUT} during the day and {P_AFTERHOURS} after hours — see our <a href="~/prices/">price list</a>.</p>

<h2>5. Have your ID ready</h2>
<p>A trustworthy locksmith will check that you live there before opening the door. Have something showing your name and the address — NRIC, a tenancy agreement, a bill or a letter. If it's inside the flat, tell the locksmith: they can usually verify it once the door is open, in front of you.</p>

<h2>6. Prevent it next time</h2>
<ul>
<li>Leave a spare key with a trusted relative or neighbour.</li>
<li>Consider a <a href="~/digital-lock-installation/">digital lock</a> — no keys to forget (but change the batteries when it warns you).</li>
<li>Replace stiff or worn locks before they fail — see <a href="~/lock-replacement/">lock replacement</a>.</li>
</ul>

<div class="callout navy"><p><strong>Locked out right now?</strong> Call or WhatsApp Uncle Thomas on <a href="tel:+6592249224">{PHONE}</a> — 24/7, islandwide. <a href="~/emergency-locksmith/">More about our emergency lockout service</a>.</p></div>
""",
 faqs=[
  ("Can the police or SCDF open my door if I'm locked out?", "The SCDF responds to emergencies where life or property is at risk (call 995). For an ordinary lockout, you'll need a locksmith."),
  ("Does HDB help if I'm locked out?", "HDB doesn't provide lockout services. Call a locksmith, and make sure they check your proof of residence."),
 ],
),
dict(
 slug="digital-lock-battery-dead", short="Digital lock battery dead",
 title="Digital Lock Battery Dead or Won't Open? What to Try First",
 desc="Digital lock dead or not opening? A Singapore locksmith's checklist: emergency power, backup key, privacy mode and keypad issues — and when to call for help.",
 h1="Digital Lock Battery Dead or Won't Open? Try These First",
 card="Flat battery, dead keypad or wrong-code lockout — the quick checks to try before calling.",
 body="""
<p>Digital locks are convenient — until they won't open. Most lockouts we're called to have one of a few causes. Here's what to check first, as the lock's owner. (Every brand is a little different, so check your manual if you have it.)</p>

<h2>1. Flat battery? Use the emergency power point</h2>
<p>Most digital locks warn you for weeks before the batteries run out. If they've died completely, many models — including popular Samsung, Yale and Philips locks — have an <strong>emergency power terminal</strong> on the outside, often for a 9V battery or a USB-C cable. Hold the power source to the terminal, then enter your code as normal. Once inside, replace <em>all</em> the batteries with fresh ones of the same type.</p>

<h2>2. Use the mechanical backup key</h2>
<p>Many digital locks have a hidden keyhole behind a small cover. If you kept the backup key that came with the lock, it can open the door even without power.</p>

<h2>3. Is the lock in privacy or double-lock mode?</h2>
<p>If someone inside switched on privacy mode (or "double lock"), the lock may refuse all codes from outside. If anyone is home, ask them to switch it off from the inside.</p>

<h2>4. Wrong code too many times?</h2>
<p>After several wrong attempts, most locks freeze the keypad for a few minutes. Wait for the time-out to end, then try once carefully.</p>

<h2>5. Keypad wet or not lighting up?</h2>
<p>Rain, corridor washing or condensation can stop a keypad responding. Gently dry the keypad and wait a few minutes. Don't spray anything into the lock.</p>

<h2>6. Still stuck? Don't force it</h2>
<p>Pulling hard on the handle or prying the lock can break the motor or the door. If none of the above works, call a locksmith who works with digital locks. Uncle Thomas has developed his own damage-free methods for opening faulty digital locks of all brands — see <a href="~/digital-lock-opening/">digital lock opening</a> (from {P_DIGITAL_OPEN}).</p>

<div class="callout"><p><strong>Tip:</strong> change your digital lock batteries as soon as the low-battery warning starts — and keep a 9V battery in your car or bag if your lock supports emergency power.</p></div>
<div class="callout navy"><p><strong>Locked out by your digital lock now?</strong> Call or WhatsApp {PHONE} — 24/7, all brands.</p></div>
""",
 faqs=[
  ("How long do digital lock batteries last?", "Typically several months to about a year, depending on the lock and how often it's used. Replace them as soon as the low-battery warning appears."),
  ("Will a flat battery reset my codes?", "Usually not — most locks keep their codes when the batteries run out. Check your lock's manual to be sure."),
 ],
),
dict(
 slug="forgot-safe-combination", short="Forgot safe combination",
 title="Forgot Your Safe Combination? What to Do Next | Singapore",
 desc="Forgot your safe code or lost the key? A US-trained safesmith explains what to try first, what not to do, and how professional safe opening works.",
 h1="Forgot Your Safe Combination? What to Do Next",
 card="Lost the code or key to your safe? What to try, what not to do, and how a safesmith helps.",
 body="""
<p>Forgetting a safe code happens more often than you'd think — after a long holiday, after inheriting a safe, or when the person who set it has left the company. Here's what Uncle Thomas, a US-trained safesmith, suggests.</p>

<h2>1. Check the batteries (electronic safes)</h2>
<p>A weak battery can make an electronic keypad behave strangely — accepting the code but not releasing the bolt. Many safes have an external battery point or a battery compartment you can reach from outside. Fresh batteries fix more "forgotten code" problems than you'd expect.</p>

<h2>2. Look for the override key</h2>
<p>Most home and hotel-style electronic safes come with an <strong>emergency override key</strong>, usually behind a small cover near the keypad. Check drawers, the original box and paperwork.</p>

<h2>3. Contact the manufacturer</h2>
<p>Some brands can provide a reset code or replacement key if you register the safe and prove ownership — have the serial number and your purchase receipt ready.</p>

<h2>4. Don't try to drill or force it</h2>
<p>Safes are designed to resist attack. Drilling in the wrong place, prying the door or hammering the bolts can trigger relockers that make the safe much harder — and more expensive — to open, and can damage what's inside.</p>

<h2>5. Call a safesmith</h2>
<p>A trained safesmith can usually open a safe with minimal damage. Uncle Thomas trained in safesmithing in the United States and has opened safes for multinational companies, on ships and across Asia. See <a href="~/safe-opening/">safe opening in Singapore</a>.</p>

<div class="callout"><p><strong>What to send for a quote:</strong> WhatsApp {PHONE} a photo of the safe's front, the keypad or dial, and any brand label. We'll need proof that the safe is yours or your company's before opening.</p></div>
""",
 faqs=[
  ("Can a safe be opened without damaging it?", "Often, yes — it depends on the safe and the fault. A trained safesmith will explain the method before starting."),
  ("How much does safe opening cost in Singapore?", "It depends on the make, size and lock type, so it's quoted per job. Send a photo for a price."),
 ],
),
dict(
 slug="how-to-choose-a-locksmith", short="How to choose a locksmith",
 title="How to Choose a Locksmith in Singapore (and Avoid Overcharging)",
 desc="How to choose a trustworthy locksmith in Singapore: get the price first, check reviews, expect an ID check, and spot the warning signs of overcharging.",
 h1="How to Choose a Locksmith in Singapore — and Avoid Overcharging",
 card="Seven checks that separate an honest locksmith from one who changes the price at your door.",
 body="""
<p>When you're locked out, you want help fast — and that's exactly when people get overcharged. Here's how to pick a locksmith you can trust, from someone who has been in the trade since 1998.</p>

<h2>1. Get the total price before anyone sets off</h2>
<p>Describe your lock (or send a photo) and ask: <em>"What will the total be?"</em> A good locksmith gives a clear figure, or a narrow range and what would change it. Be wary of anyone who only quotes a tiny "call-out fee".</p>

<h2>2. Be careful with very low "from" prices</h2>
<p>An advert that seems far cheaper than everyone else can be a sign of bait pricing — a low starting price that grows at your door. Compare a few locksmiths' price lists. Ours is published openly on our <a href="~/prices/">prices page</a>.</p>

<h2>3. Check real reviews</h2>
<p>Look at the locksmith's Google reviews — especially recent ones that mention price and honesty, not just speed.</p>

<h2>4. Expect an ID check — it's a good sign</h2>
<p>An honest locksmith will ask for proof that you live there before opening the door. If a locksmith opens any door without checking, they'd do the same for anyone — including someone trying to get into <em>your</em> home.</p>

<h2>5. Ask about damage-free entry</h2>
<p>Most lockouts can be opened without drilling. If a locksmith goes straight for the drill, ask why — and ask the price of a replacement lock before they start.</p>

<h2>6. Ask about a warranty</h2>
<p>If a lock is replaced or installed, ask what warranty comes with it. We cover every replacement and installation with a warranty that has no expiry date.</p>

<h2>7. Get a receipt</h2>
<p>Ask for a receipt or invoice showing what was done and what you paid. If you have a dispute, the Consumers Association of Singapore (CASE) can advise you.</p>

<div class="callout navy"><p><strong>Uncle Thomas Locksmith:</strong> price before work, ID verified, damage-free first, and a no-expiry warranty. Call or WhatsApp {PHONE}, 24/7. <a href="~/about/">Meet Uncle Thomas</a>.</p></div>
""",
 faqs=[
  ("What's a fair price for a locksmith in Singapore?", "For a standard daytime lockout, published prices in 2026 generally start from around S$80–S$90, with higher rates after hours. Digital locks, safes and replacements cost more. Always confirm the total before work begins."),
  ("Should a locksmith ask for my ID?", "Yes. Checking proof of residence or ownership is a sign of a trustworthy locksmith."),
 ],
),
]


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
               "datePublished": "2026-10-25", "dateModified": __import__("datetime").date.today().isoformat(),
               "mainEntityOfPage": C.SITE + "/" + path, "image": C.SITE + "/assets/img/og.jpg", "inLanguage": "en-SG"}
        nodes = x["page_schema"](path, g["title"], g["desc"], crumbs, faqs=g["faqs"], extra=[art, x["person_node"]()])
        x["render"](path, g["title"], g["desc"], body, nodes, og_type="article", priority="0.6")


def _bc(crumbs):
    items = []
    for i, (n, p) in enumerate(crumbs):
        items.append(f'<li aria-current="page">{n}</li>' if i == len(crumbs) - 1 else f'<li><a href="~/{p}">{n}</a></li>')
    return f'<nav class="breadcrumb" aria-label="Breadcrumb"><ol>{"".join(items)}</ol></nav>'
