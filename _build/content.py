"""
Page text for: home, services hub, each service page, prices, about.
Links use "~/" for the site root (converted to relative links at build time).
{PHONE}, {YEARS}, {P_LOCKOUT} etc. are replaced from config.TOKENS.
"""
import config as C

BRANDS = ", ".join(C.DIGITAL_LOCK_BRANDS)

ID_POLICY = ("For your security, we always check proof of residence or ownership before opening anything — "
             "for example NRIC with your address, a tenancy agreement or utility bill, or the car's log card.")
WARRANTY = "Every lock replacement and installation comes with our warranty — with no expiry date."
NO_REPAIR = ("We don't do lock repairs or key duplication. If a lock is faulty, we open it and replace it, "
             "so the problem doesn't come back.")

# ======================================================================
# SERVICES
# ======================================================================
SERVICES = [
# ----------------------------------------------------------------------
dict(
 path="emergency-locksmith/", short="Emergency lockout", icon="🚪",
 card="Locked out of your HDB, condo, house or office? We get you back in — damage-free wherever possible.",
 title="Emergency Locksmith Singapore 24/7 | Lockouts from S$80",
 title_exp="Emergency Locksmith Singapore 24/7 | Trusted Since 1998",
 desc="Locked out? Uncle Thomas is Singapore's 24/7 emergency locksmith since 1998. HDB, condo, landed & office lockouts islandwide, from S$80. Call 9224 9224.",
 h1="24/7 Emergency Locksmith in Singapore",
 sub="Locked out of your home or office? Call Uncle Thomas — day or night, weekends and public holidays. We set off as soon as you call and open your door damage-free wherever possible.",
 badges=["From {P_LOCKOUT} (office hours)", "24/7 islandwide", "ID verified for your safety"],
 body="""
<h2>Locked out? Here's what happens when you call</h2>
<ol>
<li><strong>Call or WhatsApp {PHONE}.</strong> Tell us your address and what kind of lock it is. A photo of the lock on WhatsApp helps us bring the right tools.</li>
<li><strong>Get a clear price first.</strong> We tell you the price before we set off, so there are no surprises at the door.</li>
<li><strong>We're on our way right away.</strong> Uncle Thomas or one of his team heads to you immediately, anywhere in Singapore.</li>
<li><strong>Quick ID check, then we open the door.</strong> We confirm you live there, then open the lock using damage-free methods wherever possible.</li>
</ol>

<h2>Lockouts we handle every day</h2>
<ul>
<li><strong>HDB flats</strong> — main doors, metal gates, room doors and toilet doors locked from the inside.</li>
<li><strong>Condominiums</strong> — main doors, deadbolts and digital locks.</li>
<li><strong>Landed homes</strong> — main doors, gates and back doors.</li>
<li><strong>Offices and shops</strong> — office doors, glass doors, cabinets and roller shutters. See <a href="~/commercial-locksmith/">commercial locksmith</a>.</li>
<li><strong>Digital lock won't open?</strong> Flat battery, forgotten PIN or faulty keypad — see <a href="~/digital-lock-opening/">digital lock opening</a>.</li>
<li><strong>Keys locked in the car?</strong> See <a href="~/car-locksmith/">car lockout</a>.</li>
</ul>

<h2>Damage-free first</h2>
<p>With {YEARS}+ years in the trade, Uncle Thomas opens most mechanical and digital locks without drilling or forcing the door. If a lock is badly worn or broken and can't be opened cleanly, we explain your options and the price <em>before</em> doing anything else. If the lock then needs changing, we can <a href="~/lock-replacement/">replace it on the spot</a> — and every replacement comes with our no-expiry warranty.</p>

<div class="callout"><p><strong>Why we ask for ID:</strong> {ID_POLICY} It protects you — a locksmith who opens any door without checking is a risk to everyone.</p></div>

<h2>How much does an emergency locksmith cost in Singapore?</h2>
<p>Our door lockouts start from <strong>{P_LOCKOUT}</strong> between 9am and 6pm, and from <strong>{P_AFTERHOURS}</strong> after hours, on weekends and public holidays. The final price depends on the lock type and whether a part needs replacing — we always confirm it with you before we start. See the full <a href="~/prices/">price list</a>.</p>

<h2>Islandwide, 24 hours a day</h2>
<p>We cover every part of Singapore, from <a href="~/areas/woodlands/">Woodlands</a> to <a href="~/areas/tampines/">Tampines</a> and <a href="~/areas/jurong/">Jurong</a> to <a href="~/areas/toa-payoh/">Toa Payoh</a>. See <a href="~/areas/">all the areas we serve</a>.</p>
<p>Not locked out yet but worried? Read our guide: <a href="~/guides/locked-out-of-hdb-flat/">locked out of your HDB flat — what to do</a>.</p>
""",
 faqs=[
  ("How fast can an emergency locksmith reach me?", "We set off as soon as you call, 24/7. Arrival time depends on where you are and traffic — we'll give you an honest estimate on the phone."),
  ("Will you damage my door?", "We use damage-free methods wherever possible, and most lockouts are opened without any damage. If a lock can't be opened cleanly, we explain the options and price before doing anything."),
  ("What do I need to show before you open the door?", "Proof that you live there — for example your NRIC with the address, a tenancy agreement or a utility bill. This protects you and your home."),
  ("Do you charge more at night?", "Lockouts start from {P_LOCKOUT} from 9am to 6pm and from {P_AFTERHOURS} after hours, weekends and public holidays. You'll always know the price before we start."),
  ("Do you open locks for tenants?", "Yes — as long as you can show you live there, for example with a tenancy agreement or a letter with your name and the address."),
 ],
),
# ----------------------------------------------------------------------
dict(
 path="digital-lock-opening/", short="Digital lock opening", icon="🔐",
 card="Flat battery, forgotten PIN or faulty keypad? We open all digital lock brands, 24/7.",
 title="Digital Lock Opening Singapore 24/7 | All Brands from S$150",
 title_exp="Digital Lock Opening Singapore 24/7 | All Brands, Since 1998",
 desc="Locked out by your digital lock? Flat battery, forgotten PIN or faulty keypad — Uncle Thomas opens all brands, 24/7 islandwide. From S$150. Call 9224 9224.",
 h1="Digital Lock Won't Open? 24/7 Digital Lock Opening",
 sub="Flat battery, forgotten PIN, dead keypad or a lock that just won't respond — Uncle Thomas has developed his own damage-free techniques for opening digital locks of every brand.",
 badges=["All brands", "From {P_DIGITAL_OPEN}", "24/7 islandwide"],
 body="""
<h2>Common digital lock problems we solve</h2>
<ul>
<li><strong>Battery went flat</strong> and the emergency power option didn't work.</li>
<li><strong>Forgotten PIN</strong> or fingerprint no longer recognised.</li>
<li><strong>Keypad dead or not lighting up</strong> — often after rain or a corridor wash.</li>
<li><strong>Lock jammed or motor not turning</strong>, even with the right code.</li>
<li><strong>Locked from the inside</strong> — privacy or double-lock mode left on.</li>
<li><strong>Lost the backup key</strong> for the mechanical override.</li>
</ul>
<p>Before you call, it's worth trying the quick checks in our guide: <a href="~/guides/digital-lock-battery-dead/">digital lock battery dead or not opening — what to try first</a>.</p>

<h2>Every brand, including</h2>
<ul class="tags">""" + "".join(f"<li>{b}</li>" for b in C.DIGITAL_LOCK_BRANDS) + """<li>and more</li></ul>
<p>Main door locks, gate locks, rim locks and mortise digital locks — on HDB flats, condos, landed homes and offices.</p>
{BRAND_LINKS}

<h2>Uncle Thomas's own digital lock techniques</h2>
<p>As Singapore homes moved from keys to keypads, Uncle Thomas kept learning. Over the years he has worked out his own damage-free ways to open faulty and locked digital locks — so in most cases you get back in <em>without</em> having to buy a new lock. Where a lock is truly beyond saving, we tell you honestly and can <a href="~/digital-lock-installation/">install a new one</a> on the spot.</p>

<div class="callout"><p>{NO_REPAIR}</p></div>

<h2>What it costs</h2>
<p>Digital lock emergency opening starts from <strong>{P_DIGITAL_OPEN}</strong>. The price depends on the brand, model and fault — WhatsApp a photo of the lock (front and inside if possible) to {PHONE} and we'll give you a firm price before we come. See all <a href="~/prices/">prices</a>.</p>

<div class="callout"><p><strong>Security first:</strong> {ID_POLICY}</p></div>
""",
 faqs=[
  ("Can you open a digital lock without damaging it?", "In most cases, yes. Uncle Thomas has developed his own damage-free techniques. If a lock is completely broken we'll explain the options before doing anything."),
  ("Which digital lock brands do you open?", "All brands — including " + ", ".join(C.DIGITAL_LOCK_BRANDS) + "."),
  ("My digital lock battery is flat. What should I do?", "Most digital locks have an emergency power point (often a 9V battery terminal) or a backup key. If those don't work, call or WhatsApp {PHONE} and we'll open it for you."),
  ("Do you repair digital locks?", "No — we don't do repairs. We open the lock, and if it's faulty we can replace it with a new one, covered by our no-expiry installation warranty."),
  ("How much does it cost to open a digital lock?", "From {P_DIGITAL_OPEN}. Send a photo on WhatsApp for an exact price before we come."),
 ],
),
# ----------------------------------------------------------------------
dict(
 path="digital-lock-installation/", short="Digital lock installation", icon="📲",
 card="Neat, correct installation for HDB main doors, gates, condos and offices — with a no-expiry warranty.",
 title="Digital Lock Installation Singapore | HDB, Condo & Office",
 title_exp="Digital Lock Installation Singapore | No-Expiry Warranty",
 desc="Professional digital lock installation for HDB doors & gates, condos and offices. All brands, labour from S$120, warranty with no expiry. Call 9224 9224.",
 h1="Digital Lock Installation in Singapore",
 sub="Thinking of going keyless? Uncle Thomas installs digital locks of every brand on HDB main doors and gates, condo doors and offices — fitted properly, set up with you, and covered by a warranty that never expires.",
 badges=["Labour from {P_DIGITAL_INSTALL}", "All brands", "No-expiry warranty"],
 body="""
<h2>Why installation matters</h2>
<p>Most digital lock problems we're called out for start with a poor installation — a misaligned strike plate, a cable pinched in the door, or a lock that doesn't suit the door. A digital lock is only as good as how it's fitted. With {YEARS}+ years of opening and fitting locks, Uncle Thomas knows exactly what makes a lock last in Singapore's humid weather.</p>

<h2>What we install</h2>
<ul>
<li><strong>HDB main door digital locks</strong> — including replacing an old mechanical lock.</li>
<li><strong>HDB gate digital locks</strong> — rim and mortise types for metal gates.</li>
<li><strong>Condo and landed home locks</strong> — main doors, side doors and gates.</li>
<li><strong>Office and shop locks</strong> — keypad and card access for small businesses. See <a href="~/commercial-locksmith/">commercial locksmith</a>.</li>
</ul>
<p>We work with all brands, including """ + BRANDS + """. Bought your own lock online? We'll install it. Not sure which to get? Tell us your door and budget and we'll recommend one that fits.</p>

<h2>How it works</h2>
<ol>
<li>WhatsApp {PHONE} a photo of your door (outside and inside edge) and the lock you want.</li>
<li>We confirm the lock fits and give you a fixed price.</li>
<li>We install, test every function, and set up your PIN, fingerprints and cards with you.</li>
<li>You get our <strong>no-expiry warranty</strong> on the installation.</li>
</ol>

<div class="callout navy"><p><strong>Our warranty:</strong> {WARRANTY}</p></div>

<h2>Price</h2>
<p>Digital lock installation (labour) starts from <strong>{P_DIGITAL_INSTALL}</strong>. The total depends on the door, whether old locks need removing, and whether you supply the lock. See the full <a href="~/prices/">price list</a>.</p>
<p>Locked out of a digital lock right now? Go to <a href="~/digital-lock-opening/">digital lock opening</a>.</p>
""",
 faqs=[
  ("Can I install a digital lock on my HDB main door?", "Yes. Digital locks are common on HDB main doors and gates. We check your door's thickness and existing cut-outs so the lock fits properly."),
  ("Can you install a lock I bought online?", "Yes. Send us a photo of the lock and your door first so we can confirm it will fit."),
  ("How long does installation take?", "Most installations are completed in one visit. We test every function and set up your codes and fingerprints before we leave."),
  ("Is there a warranty?", "Yes — every installation comes with our warranty, with no expiry date."),
  ("Do you repair digital locks?", "No, we don't do repairs. If an existing lock is faulty we can replace it with a new one."),
 ],
),
# ----------------------------------------------------------------------
dict(
 path="safe-opening/", short="Safe opening", icon="🗄️",
 card="Forgotten combination or faulty safe? Opened by a US-trained safesmith who has worked on ships and across Asia.",
 title="Safe Opening Singapore | US-Trained Safesmith | Uncle Thomas",
 title_exp="Safe Opening Singapore | US-Trained Safesmith Since 1998",
 desc="Forgot your safe combination or lost the key? Uncle Thomas is a US-trained safesmith who has opened safes on ships and across Asia. Call 9224 9224.",
 h1="Safe Opening in Singapore by a US-Trained Safesmith",
 sub="Forgotten combination, lost key, flat battery or a jammed safe — Uncle Thomas trained in safesmithing in the United States and has opened safes for multinational companies, on ships and across Asia.",
 badges=["US-trained safesmith", "Home & business safes", "Discreet service"],
 body="""
<h2>Why a safesmith, not just a locksmith</h2>
<p>Opening a safe is a different skill from opening a door. Safes are built to resist forced entry, so the wrong approach can destroy the safe — or its contents. In Singapore, few locksmiths have formal safe training. Uncle Thomas spent a year in the United States training in <strong>safesmithing</strong>, and has since been called to open safes for multinational companies, on board ships and cruise liners, and in Thailand, Malaysia, China and Hong Kong.</p>

<h2>Safes we open</h2>
<ul>
<li><strong>Home safes</strong> — electronic keypad, key and combination safes.</li>
<li><strong>Hotel-style and wardrobe safes</strong>.</li>
<li><strong>Office and business safes</strong> — cash safes, drop safes and document safes.</li>
<li><strong>Older mechanical dial safes</strong>.</li>
<li><strong>Safes on ships and vessels</strong>.</li>
</ul>

<h2>Common reasons people call us</h2>
<ul>
<li>Forgot the combination or PIN.</li>
<li>Lost the key, or the override key.</li>
<li>Electronic keypad dead even after changing the batteries.</li>
<li>Bolt jammed — the code is accepted but the door won't open.</li>
<li>Inherited a safe and no one knows the code.</li>
</ul>
<p>Before you call, try the steps in our guide: <a href="~/guides/forgot-safe-combination/">forgot your safe combination — what to do</a>.</p>

<div class="callout"><p><strong>Proof of ownership:</strong> Before opening any safe we confirm it belongs to you or your business — for example a purchase receipt, company authorisation or proof of residence where the safe is kept. Jobs are handled discreetly.</p></div>

<h2>Price</h2>
<p>Safe opening is <strong>quoted per job</strong>, because it depends on the safe's make, size and lock type. WhatsApp {PHONE} a photo of the safe (front, keypad or dial, and the brand label) and we'll give you a price before we come.</p>
<p>Read more about <a href="~/about/">Uncle Thomas's background</a>.</p>
""",
 faqs=[
  ("Can you open a safe without destroying it?", "In many cases, yes — that's what safesmith training is for. The method depends on the safe. We'll explain the approach and price before we start."),
  ("I forgot my safe code. Can you help?", "Yes. Try the manufacturer's reset steps first (see our guide). If that doesn't work, WhatsApp us a photo of the safe and we'll quote you."),
  ("Do you open safes for businesses?", "Yes — offices, shops and vessels. We'll need authorisation from the business before opening."),
  ("How much does safe opening cost?", "It's quoted per job, depending on the safe. Send a photo on WhatsApp to {PHONE} for a price."),
 ],
),
# ----------------------------------------------------------------------
dict(
 path="car-locksmith/", short="Car lockout", icon="🚗",
 card="Keys locked in the car? Non-destructive car unlocking for all makes and models, 24/7.",
 title="Car Locksmith Singapore 24/7 | Car Lockout from S$100",
 title_exp="Car Locksmith Singapore 24/7 | Non-Destructive · Since 1998",
 desc="Keys locked in your car? Uncle Thomas unlocks all makes and models without damage, 24/7 islandwide. Car lockout from S$100. Call or WhatsApp 9224 9224.",
 h1="Car Locksmith Singapore — Keys Locked in the Car?",
 sub="Keys locked inside, or the remote stopped working? Uncle Thomas opens cars of all makes and models with non-destructive tools — no broken windows, no scratched doors.",
 badges=["From {P_CAR}", "All makes & models", "24/7 islandwide"],
 body="""
<h2>Car lockouts we handle</h2>
<ul>
<li>Keys locked inside the car or boot.</li>
<li>Remote key battery dead and the door won't open.</li>
<li>Car locked at a carpark, petrol station or roadside — anywhere in Singapore.</li>
<li>Cars, vans and light commercial vehicles.</li>
</ul>

<h2>Non-destructive unlocking</h2>
<p>We use professional car entry tools that open the door without damaging the paintwork, rubber seals or windows. It's much cheaper than breaking a window — and safer than trying a coat hanger yourself, which can damage the door's wiring and airbag sensors.</p>

<div class="callout"><p><strong>Proof of ownership:</strong> Before unlocking, we check that the car is yours — for example your NRIC against the vehicle log card, or a rental or company car agreement.</p></div>

<h2>Price</h2>
<p>Car lockouts start from <strong>{P_CAR}</strong>. WhatsApp {PHONE} your location and car model and we'll confirm the price before we set off. See all <a href="~/prices/">prices</a>.</p>
<p>Please note: we open locked cars. We don't cut or programme car keys.</p>
""",
 faqs=[
  ("Can you open my car without damaging it?", "Yes. We use non-destructive car entry tools that don't damage the paint, seals or windows."),
  ("Which cars can you open?", "All makes and models of cars, plus vans and light commercial vehicles."),
  ("Can you make a new car key?", "No — we open locked cars, but we don't cut or programme car keys."),
  ("How much is a car lockout?", "From {P_CAR}. We'll confirm the price before we set off."),
 ],
),
# ----------------------------------------------------------------------
dict(
 path="lock-replacement/", short="Lock replacement", icon="🔧",
 card="Main door, gate, room and toilet door locks replaced with quality hardware — warranty with no expiry.",
 title="Door & Gate Lock Replacement Singapore | HDB from S$100",
 title_exp="Door & Gate Lock Replacement Singapore | No-Expiry Warranty",
 desc="Main door, HDB gate, room and toilet door lock replacement islandwide. Quality hardware, no-expiry warranty, from S$100. Uncle Thomas Locksmith, 9224 9224.",
 h1="Door & Gate Lock Replacement in Singapore",
 sub="Lost your keys, moved into a new home, or have a lock that's worn out? Uncle Thomas replaces main door, gate and room door locks with quality hardware — and every replacement has a warranty that never expires.",
 badges=["From {P_REPLACE}", "No-expiry warranty", "Same-visit replacement"],
 body="""
<h2>When to change your locks</h2>
<ul>
<li><strong>You moved into a new home</strong> — you never know how many old keys are out there.</li>
<li><strong>Keys lost or stolen</strong>.</li>
<li><strong>A tenant or helper has moved out</strong>.</li>
<li><strong>The lock is stiff, loose or jams</strong> — a worn lock can fail and lock you out.</li>
<li><strong>After a break-in or attempted break-in</strong>.</li>
<li><strong>Upgrading security</strong> — or switching to a <a href="~/digital-lock-installation/">digital lock</a>.</li>
</ul>

<h2>Locks we replace</h2>
<ul>
<li>HDB main door locks — mortise locks, cylinder locks, deadbolts and lever handles.</li>
<li>HDB metal gate locks — hook bolts, padlocks and gate locksets.</li>
<li>Room, toilet and bedroom door locks and knobs.</li>
<li>Condo, landed and office door locks.</li>
<li><a href="~/letterbox-lock-replacement/">Letterbox and mailbox locks</a>.</li>
</ul>

<div class="callout navy"><p><strong>Our warranty:</strong> {WARRANTY}</p></div>

<h2>Replace, don't repair</h2>
<p>{NO_REPAIR} A new lock is usually more reliable, often not much more expensive than a repair, and comes with our warranty.</p>

<h2>Price</h2>
<p>Main door and gate lock replacement starts from <strong>{P_REPLACE}</strong>, including supply and installation. Higher-security locks cost more — WhatsApp a photo of your current lock to {PHONE} for a fixed price. See all <a href="~/prices/">prices</a>.</p>
""",
 faqs=[
  ("Should I change my locks after moving into a new flat?", "Yes, it's a good idea. Previous owners, tenants or contractors may still have keys."),
  ("Do you repair locks?", "No. We replace faulty locks with new ones, which are more reliable and come with our no-expiry warranty."),
  ("Can you replace my lock if I'm locked out?", "Yes — we open the door first, then replace the lock in the same visit if needed."),
  ("Is there a warranty on replacement locks?", "Yes. Every lock replacement comes with our warranty, with no expiry date."),
 ],
),
# ----------------------------------------------------------------------
dict(
 path="letterbox-lock-replacement/", short="Letterbox lock", icon="📮",
 card="Lost your letterbox key? We open and replace HDB and condo letterbox locks.",
 title="Letterbox Lock Replacement Singapore | HDB from S$60",
 title_exp="Letterbox Lock Replacement Singapore | Since 1998",
 desc="Lost your HDB or condo letterbox key? Uncle Thomas opens and replaces letterbox locks islandwide, from S$60, with a no-expiry warranty. Call 9224 9224.",
 h1="Letterbox Lock Replacement in Singapore",
 sub="Lost the key to your HDB or condo letterbox, or the lock is broken? We open it and fit a new lock with new keys — quickly, with proof of residence checked first.",
 badges=["From {P_LETTERBOX}", "HDB & condo", "No-expiry warranty"],
 body="""
<h2>We can help if…</h2>
<ul>
<li>You lost your letterbox key.</li>
<li>The lock is jammed, rusty or broken.</li>
<li>You just moved in and want to make sure no one else has a key.</li>
<li>Someone tampered with your letterbox lock.</li>
</ul>

<h2>How it works</h2>
<ol>
<li>WhatsApp {PHONE} with your block and unit, and a photo of the letterbox.</li>
<li>We confirm the price and arrange a time — letterboxes don't need a midnight call-out, so we'll come at a time that suits you.</li>
<li>We check your proof of residence, open the letterbox and fit a new lock with new keys.</li>
</ol>

<div class="callout"><p><strong>Why we check ID:</strong> A letterbox holds bank letters and IDs. {ID_POLICY}</p></div>

<h2>Price</h2>
<p>Letterbox lock replacement starts from <strong>{P_LETTERBOX}</strong>, including a new lock and keys. {WARRANTY} See all <a href="~/prices/">prices</a>.</p>
<p>Need your main door or gate lock changed too? See <a href="~/lock-replacement/">lock replacement</a>.</p>
""",
 faqs=[
  ("I lost my HDB letterbox key. What should I do?", "WhatsApp us your block and a photo of the letterbox. We'll open it and fit a new lock with new keys after checking your proof of residence."),
  ("Do you make duplicate letterbox keys?", "No, we don't do key duplication. We replace the lock and give you a new set of keys."),
  ("How much does letterbox lock replacement cost?", "From {P_LETTERBOX}, including the new lock and keys."),
 ],
),
# ----------------------------------------------------------------------
dict(
 path="commercial-locksmith/", short="Commercial locksmith", icon="🏢",
 card="Offices, shops, warehouses and vessels — door, glass door, shutter, cabinet and safe locks.",
 title="Commercial Locksmith Singapore | Office & Shop Locks 24/7",
 title_exp="Commercial Locksmith Singapore 24/7 | Since 1998",
 desc="Commercial locksmith for offices, shops and warehouses in Singapore — lockouts, lock changes, digital access and safes, 24/7. Uncle Thomas, 9224 9224.",
 h1="Commercial Locksmith for Offices & Shops in Singapore",
 sub="Locked out of the office before opening time? Staff left with keys? Uncle Thomas and his team handle commercial lockouts, lock changes, digital access and safes — 24/7, with minimal disruption to your business.",
 badges=["24/7, incl. before opening hours", "Offices, shops & warehouses", "Safes & vessels"],
 body="""
<h2>Commercial locksmith services</h2>
<ul>
<li><strong>Office and shop lockouts</strong> — main doors, glass doors, back doors and roller shutters.</li>
<li><strong>Lock changes when staff leave</strong> or keys go missing.</li>
<li><strong>Digital and keypad locks</strong> for offices and small businesses — see <a href="~/digital-lock-installation/">digital lock installation</a>.</li>
<li><strong>Cabinet, drawer and locker locks</strong>.</li>
<li><strong>Safe opening</strong> for cash, drop and document safes — see <a href="~/safe-opening/">safe opening</a>.</li>
<li><strong>Ships and vessels</strong> — Uncle Thomas has opened safes and locks on ships and cruise liners.</li>
</ul>

<h2>Why businesses choose Uncle Thomas</h2>
<ul>
<li><strong>{YEARS}+ years' experience</strong> since {FOUNDED}, including work for multinational companies.</li>
<li><strong>24/7</strong> — we can come before you open or after you close, so business isn't disrupted.</li>
<li><strong>Clear quotes and proper invoices</strong> for your accounts.</li>
<li><strong>Authorisation checked</strong> before opening any business premises or safe.</li>
<li>{WARRANTY}</li>
</ul>

<h2>Price</h2>
<p>Commercial jobs are quoted upfront. WhatsApp {PHONE} photos of the lock or door and tell us what you need. See typical <a href="~/prices/">prices</a>.</p>
""",
 faqs=[
  ("Can you come before our office opens?", "Yes, we work 24/7, so we can come early in the morning or after closing time."),
  ("Do you change locks when staff leave?", "Yes. Replacing the lock is the safest option when keys can't be accounted for."),
  ("Do you provide invoices for companies?", "Yes, we provide proper invoices for business jobs."),
 ],
),
]

SERVICE_BY_PATH = {s["path"]: s for s in SERVICES}


def related_html(current_path):
    cards = []
    for s in SERVICES:
        if s["path"] == current_path:
            continue
        cards.append(f'<a class="card" href="~/{s["path"]}"><span class="ico" aria-hidden="true">{s["icon"]}</span>'
                     f'<h3>{s["short"]}</h3><p>{s["card"]}</p><span class="more">Learn more →</span></a>')
    return ('<section class="section section-alt"><div class="container"><h2 class="section-title">Other locksmith services</h2>'
            '<p class="section-lead">One call covers it all — 24/7, islandwide.</p>'
            f'<div class="grid g3">{"".join(cards[:6])}</div></div></section>')


def service_cards(with_price=True):
    out = []
    for s in SERVICES:
        pr = C.price(s["path"])
        tag = f'<span class="from">From {pr}</span>' if with_price and pr else '<span class="from">Quote on request</span>'
        out.append(f'<a class="card" href="~/{s["path"]}"><span class="ico" aria-hidden="true">{s["icon"]}</span>'
                   f'<h3>{s["short"]}</h3><p>{s["card"]}</p>{tag}</a>')
    return "".join(out)


def price_table():
    rows = []
    for label, path, pr, note in C.PRICES:
        lab = f'<a href="~/{path}">{label}</a>' if path else label
        val = f"S${pr}" if isinstance(pr, int) else pr
        rows.append(f"<tr><td>{lab}</td><td>{val}</td></tr>")
    return ('<div class="price-wrap"><table class="price-table"><thead><tr><th scope="col">Service</th><th scope="col">From</th></tr></thead>'
            f'<tbody>{"".join(rows)}</tbody></table></div>')


# ======================================================================
# HOME
# ======================================================================
HOME_FAQS = [
  ("Are you really available 24/7?", "Yes. Uncle Thomas Locksmith works 24 hours a day, 7 days a week, including weekends and public holidays, anywhere in Singapore."),
  ("How fast can you reach me?", "We set off as soon as you call. Arrival time depends on your location and traffic — we'll give you an honest estimate on the phone. Call or WhatsApp {PHONE}."),
  ("How much does a locksmith cost in Singapore?", "Our lockouts start from {P_LOCKOUT} (9am–6pm) and {P_AFTERHOURS} after hours, weekends and public holidays. Car lockouts start from {P_CAR} and digital lock opening from {P_DIGITAL_OPEN}. Your final price is always confirmed before any work begins. See our <a href=\"~/prices/\">full price list</a>."),
  ("Do you check that I live there before opening the door?", "Yes. " + ID_POLICY + " It's how we keep every home safe."),
  ("Which areas in Singapore do you cover?", "All of Singapore — Central, East, West, North and North-East. See <a href=\"~/areas/\">areas we serve</a>."),
  ("Is there a warranty?", WARRANTY),
  ("Do you do key duplication or lock repairs?", "No. We specialise in opening doors, digital locks and safes, and in lock replacement and installation. Faulty locks are replaced, not repaired."),
]


def reviews_html(C_):
    """Reviews section — only rendered when real reviews exist in config.REVIEWS."""
    revs = [r for r in C_.REVIEWS if r.get("text")][:3]
    if not revs:
        return "<!-- FILL: real Google reviews in _build/config.py -> REVIEWS. Section hidden until then. -->"
    cards = "".join(
        f'<figure class="card review"><div class="stars" aria-hidden="true">★★★★★</div>'
        f'<blockquote>“{r["text"]}”</blockquote><figcaption class="who">— {r["name"]}, {r["estate"]} · {r["month"]}</figcaption></figure>'
        for r in revs)
    return f"""<section class="section" id="reviews">
  <div class="container review-cta">
    <h2 class="section-title">What Our Customers Say</h2>
    <p class="section-lead">Real reviews from Singapore customers on Google.</p>
    <div class="grid g3 reviews-grid">{cards}</div>
    <a href="{C_.GOOGLE_PROFILE}" class="btn btn-outline" target="_blank" rel="noopener">⭐ Read all our Google reviews</a>
  </div>
</section>"""


def pick_title(s_or_titles):
    """Choose the title per config.TITLE_STYLE."""
    keep, exp = s_or_titles
    return exp if C.TITLE_STYLE.upper().startswith("LEAD") else keep


def build_home(x):
    C_ = x["C"]
    hero_photo = x["photo"]("hero", eager=True, cls="photo hero-photo")
    if hero_photo.startswith("<!--"):
        hero_art = (hero_photo + '<picture><source srcset="~/assets/img/logo-320.webp 320w, ~/assets/img/logo-640.webp 640w" sizes="340px" type="image/webp">'
                    '<img src="~/assets/img/logo-640.jpg" alt="Uncle Thomas Locksmith mascot holding a key" width="340" height="340" fetchpriority="high"></picture>')
    else:
        hero_art = hero_photo
    work = x["photo"]("home_work")
    work_section = "" if work.startswith("<!--") else f"""
<section class="section section-alt" id="work">
  <div class="container">
    <h2 class="section-title">Recent Jobs Across Singapore</h2>
    <p class="section-lead">Real photos from Uncle Thomas's recent jobs: doors, digital locks, safes and letterboxes.</p>
    <div class="work-grid">{work}</div>
  </div>
</section>
"""
    town_links = "".join(f'<a href="~/areas/{t["slug"]}/">{t["name"]}</a>' for t in x["areas"].TOWNS)
    guide_cards = "".join(f'<a class="card" href="~/guides/{g["slug"]}/"><h3>{g["h1"]}</h3><p>{g["card"]}</p><span class="more">Read the guide →</span></a>'
                          for g in x["guides"].GUIDES[:4])
    body = f"""
<section class="hero">
  <div class="container hero-inner">
    <div>
      <p class="eyebrow">🔑 Singapore's locksmith "Shifu" · Since {C_.FOUNDED}</p>
      <h1>24/7 Locksmith in Singapore — Locked Out? <span class="hl">Uncle Thomas</span> Is On The Way.</h1>
      <p class="hero-sub">Emergency lockouts, digital locks, safes and cars — opened damage-free wherever possible, anywhere on the island. Clear price before we start, from <strong>{{P_LOCKOUT}}</strong>.</p>
      {x["cta_buttons"]()}
      <ul class="badges"><li>24/7 incl. public holidays</li><li>Islandwide</li><li>US-trained safesmith</li><li>ID verified</li><li>No-expiry warranty</li></ul>
    </div>
    <div class="hero-art">{hero_art}</div>
  </div>
</section>

<section class="trust" aria-label="Key facts">
  <div class="container trust-inner">
    <div class="trust-item"><strong>Since {C_.FOUNDED}</strong><span>{C_.YEARS}+ years in the trade</span></div>
    <div class="trust-item"><strong>24/7</strong><span>Nights, weekends, PH</span></div>
    <div class="trust-item"><strong>Islandwide</strong><span>Every town in Singapore</span></div>
    <div class="trust-item"><strong>From {{P_LOCKOUT}}</strong><span>Price confirmed first</span></div>
  </div>
</section>

<section class="section" id="services">
  <div class="container">
    <h2 class="section-title">Locksmith Services in Singapore</h2>
    <p class="section-lead">Doors, digital locks, safes and cars — for HDB flats, condos, landed homes, offices and shops.</p>
    <div class="grid g4">{service_cards()}</div>
    <p class="note">We specialise in opening and replacing locks. We do <strong>not</strong> offer key duplication or lock repair.</p>
  </div>
</section>

<section class="section section-alt" id="how">
  <div class="container">
    <h2 class="section-title">How It Works</h2>
    <p class="section-lead">No surprises, no guesswork — just a locksmith who turns up and gets you back in.</p>
    <div class="grid g4 steps">
      <div class="card step"><h3>Call or WhatsApp</h3><p>Call {C_.PHONE} or WhatsApp a photo of your lock and your location.</p></div>
      <div class="card step"><h3>Get the price</h3><p>We tell you the price upfront, before we set off.</p></div>
      <div class="card step"><h3>We come right away</h3><p>Uncle Thomas or his team heads to you immediately, 24/7.</p></div>
      <div class="card step"><h3>ID check, then open</h3><p>We confirm it's your home, car or safe — then open it, damage-free wherever possible.</p></div>
    </div>
  </div>
</section>

<section class="section" id="pricing">
  <div class="container narrow">
    <h2 class="section-title">Upfront Locksmith Prices</h2>
    <p class="section-lead">Clear starting prices. Your final price is confirmed before any work begins.</p>
    {price_table()}
    <p class="price-foot">Prices depend on lock type and location. WhatsApp a photo to {C_.PHONE} for an exact quote · <a href="~/prices/">What affects the price?</a></p>
  </div>
</section>

<section class="section shifu" id="shifu">
  <div class="container">
    <h2 class="section-title">Led by Singapore's Locksmith "Shifu"</h2>
    <p class="section-lead">Uncle Thomas started as an apprentice under his uncle in {C_.FOUNDED}. Today other locksmiths call him "Shifu" — the master they turn to when a job gets difficult.</p>
    <div class="shifu-grid">
      <div class="shifu-item"><strong>Since {C_.FOUNDED}</strong><p>Learnt the trade the traditional way — one lock, one door at a time.</p></div>
      <div class="shifu-item"><strong>US-trained safesmith</strong><p>Spent a year in the United States training in safesmithing.</p></div>
      <div class="shifu-item"><strong>Ships &amp; overseas</strong><p>Opened safes on ships and cruise liners, and in Thailand, Malaysia, China and Hong Kong.</p></div>
      <div class="shifu-item"><strong>Digital lock specialist</strong><p>Developed his own damage-free ways to open faulty digital locks.</p></div>
    </div>
    <div class="cta-row center"><a href="~/about/" class="btn btn-light">Read Uncle Thomas's story</a></div>
  </div>
</section>

{work_section}
<section class="section" id="why">
  <div class="container">
    <h2 class="section-title">Why Singapore Chooses Uncle Thomas</h2>
    <p class="section-lead">What you get with every call.</p>
    <div class="grid g3">
      <div class="card"><span class="ico" aria-hidden="true">⏱️</span><h3>Immediate response</h3><p>We set off as soon as you call — day or night, weekends and public holidays.</p></div>
      <div class="card"><span class="ico" aria-hidden="true">💬</span><h3>Price before work</h3><p>Upfront starting prices, and your final price confirmed before we touch the lock.</p></div>
      <div class="card"><span class="ico" aria-hidden="true">🛡️</span><h3>Damage-free methods</h3><p>We open most doors, digital locks and cars without drilling or forcing.</p></div>
      <div class="card"><span class="ico" aria-hidden="true">🪪</span><h3>ID verified</h3><p>We check proof of residence or ownership — so no one can use a locksmith to get into your home.</p></div>
      <div class="card"><span class="ico" aria-hidden="true">✅</span><h3>No-expiry warranty</h3><p>Every lock replacement and installation is covered, with no expiry date.</p></div>
      <div class="card"><span class="ico" aria-hidden="true">🏆</span><h3>{C_.YEARS}+ years' experience</h3><p>From HDB gates to ship safes — there's very little Uncle Thomas hasn't opened.</p></div>
    </div>
  </div>
</section>

<section class="section section-alt" id="areas">
  <div class="container narrow" style="text-align:center">
    <h2 class="section-title">Locksmith Near You — Islandwide</h2>
    <p class="section-lead">Wherever you are in Singapore, Uncle Thomas can reach you. Find your town:</p>
    <div class="town-links" style="justify-content:center">{town_links}</div>
    <p style="margin-top:20px"><a href="~/areas/" class="btn btn-outline">See all areas we serve</a></p>
  </div>
</section>

{reviews_html(C_)}

<section class="section section-alt" id="guides">
  <div class="container">
    <h2 class="section-title">Helpful Guides</h2>
    <p class="section-lead">Quick answers for when something goes wrong with a lock.</p>
    <div class="grid g4">{guide_cards}</div>
    <p style="text-align:center;margin-top:24px"><a href="~/guides/" class="btn btn-outline">See all guides</a></p>
  </div>
</section>

<section class="section" id="faq">
  <div class="container narrow">{x["faq_html"](HOME_FAQS)}</div>
</section>
{x["cta_band"]()}
"""
    title = pick_title(("24/7 Locksmith Singapore from S$80 | Uncle Thomas Since 1998",
                        "24/7 Locksmith Singapore | Since 1998 · US-Trained Safesmith"))
    desc = "Locked out? Uncle Thomas is Singapore's 24/7 emergency locksmith since 1998. Doors, digital locks, safes & cars, islandwide. From S$80. Call 9224 9224."
    biz = x["business_node"](full=True)
    nodes = [
        {"@type": "WebSite", "@id": C_.SITE + "/#website", "url": C_.SITE + "/", "name": C_.NAME,
         "inLanguage": "en-SG", "publisher": {"@id": x["BUSINESS_ID"]}},
        {"@type": "WebPage", "@id": C_.SITE + "/#webpage", "url": C_.SITE + "/", "name": title, "description": desc,
         "isPartOf": {"@id": C_.SITE + "/#website"}, "about": {"@id": x["BUSINESS_ID"]}, "inLanguage": "en-SG",
         "primaryImageOfPage": {"@type": "ImageObject", "url": C_.SITE + "/assets/img/og.jpg"}},
        biz, x["person_node"](), x["faq_node"](HOME_FAQS),
    ]
    x["render"]("", title, desc, body, nodes, preload_img=None if hero_photo.startswith("<figure") else "assets/img/logo-320.webp",
                priority="1.0", alternates={"en-SG": "", "zh-SG": "zh/"})


# ======================================================================
# SERVICES HUB + SERVICE PAGES
# ======================================================================
def build_services(x):
    C_ = x["C"]
    crumbs = [("Home", ""), ("Services", "services/")]
    title = "Locksmith Services Singapore | Doors, Digital Locks & Safes"
    desc = "All Uncle Thomas Locksmith services: emergency lockouts, digital lock opening & installation, safes, cars, lock and letterbox replacement. 24/7, islandwide."
    body = (x["page_hero"](crumbs, "Locksmith Services in Singapore",
            "Everything Uncle Thomas and his team can help with — 24/7, islandwide. Tap a service for details and prices.",
            ["24/7 islandwide", "Price before work", "No-expiry warranty"]) +
            f'<section class="section"><div class="container"><div class="grid g4">{service_cards()}</div>'
            f'<p class="note">{NO_REPAIR}</p></div></section>' + x["cta_band"]())
    nodes = x["page_schema"]("services/", title, desc, crumbs, page_type="CollectionPage", extra=[
        {"@type": "ItemList", "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "url": C_.SITE + "/" + s["path"], "name": s["short"]}
            for i, s in enumerate(SERVICES)]}])
    x["render"]("services/", title, desc, body, nodes, priority="0.8")

    for s in SERVICES:
        crumbs = [("Home", ""), ("Services", "services/"), (s["short"], s["path"])]
        body = (x["page_hero"](crumbs, s["h1"], s["sub"], s["badges"]) +
                f'<section class="section"><div class="container narrow prose">{s["body"]}{x["photo"](s["path"])}</div></section>' +
                f'<section class="section section-alt"><div class="container narrow">{x["faq_html"](s["faqs"])}</div></section>' +
                x["cta_band"]() + related_html(s["path"]))
        pr = C_.price(s["path"])
        svc = {"@type": "Service", "@id": C_.SITE + "/" + s["path"] + "#service", "name": s["short"].capitalize() + " — Singapore",
               "serviceType": s["short"], "description": s["desc"], "provider": {"@id": x["BUSINESS_ID"]},
               "areaServed": {"@type": "Country", "name": "Singapore"}, "url": C_.SITE + "/" + s["path"],
               "hoursAvailable": {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], "opens": "00:00", "closes": "23:59"}}
        if pr:
            svc["offers"] = {"@type": "Offer", "priceCurrency": "SGD",
                             "priceSpecification": {"@type": "PriceSpecification", "minPrice": int(pr[2:]), "priceCurrency": "SGD"}}
        img = x["photos_schema"](s["path"])
        if img:
            svc["image"] = img if len(img) > 1 else img[0]
        title = pick_title((s["title"], s.get("title_exp", s["title"])))
        nodes = x["page_schema"](s["path"], title, s["desc"], crumbs, faqs=s["faqs"], extra=[svc])
        alts = {"en-SG": s["path"], "zh-SG": "zh/emergency-locksmith/"} if s["path"] == "emergency-locksmith/" else None
        x["render"](s["path"], title, s["desc"], body, nodes, priority="0.9", alternates=alts)


# ======================================================================
# PRICES
# ======================================================================
PRICE_FAQS = [
  ("Why do locksmith prices vary so much in Singapore?", "Mainly because of the lock type, the time of day, whether a part needs replacing, and how the price is quoted. Some locksmiths advertise a very low call-out fee and add charges at the door. We give you the price before we start."),
  ("Is there a call-out or transport fee?", "Our prices are quoted for the job at your location. We'll tell you the total before we set off, so you won't be surprised by extra fees."),
  ("Do you charge more after midnight or on public holidays?", "Lockouts start from {P_LOCKOUT} from 9am to 6pm and from {P_AFTERHOURS} after hours, weekends and public holidays."),
  ("What if you can't open the lock?", "We'll explain the options — such as replacing the lock — and the price, and only go ahead with your agreement."),
  ("How do I pay?", "OWNER TO CONFIRM: payment methods (e.g. PayNow, cash). We'll tell you when you call."),
]


def build_prices(x):
    C_ = x["C"]
    crumbs = [("Home", ""), ("Prices", "prices/")]
    title = "Locksmith Prices Singapore (2026) | Upfront Rates from S$60"
    desc = "How much does a locksmith cost in Singapore? Uncle Thomas's upfront 2026 prices for lockouts, digital locks, cars, lock and letterbox replacement and safes."
    faqs = [f for f in PRICE_FAQS if "OWNER TO CONFIRM" not in f[1]]
    body = (x["page_hero"](crumbs, "Locksmith Prices in Singapore (2026)",
            "Clear starting prices for every service — and your final price confirmed before any work begins. No surprise charges at the door.",
            ["Price confirmed first", "No hidden fees", "No-expiry warranty"]) +
            f'''<section class="section"><div class="container narrow">{price_table()}
<p class="price-foot">All prices in Singapore dollars. Last updated {{MONTH_YEAR}}.</p>
<div class="prose" style="margin-top:36px">
<h2>What affects the price?</h2>
<ul>
<li><strong>Type of lock</strong> — a standard HDB mortise lock is quicker to open than a high-security deadbolt or a digital lock with a dead battery.</li>
<li><strong>Time of day</strong> — lockouts from 9am to 6pm start from {{P_LOCKOUT}}; after hours, weekends and public holidays from {{P_AFTERHOURS}}.</li>
<li><strong>Parts</strong> — if a lock is broken and needs replacing, the new lock is added to the price. We show you the options first.</li>
<li><strong>Safes and commercial jobs</strong> — quoted individually because every safe and site is different.</li>
</ul>
<h2>How to get an exact price in one minute</h2>
<p>WhatsApp a photo of the lock (outside and inside if possible) and your location to <a href="{C_.WA_LINK}" target="_blank" rel="noopener">{C_.PHONE}</a>. We'll reply with a firm price — before anyone sets off.</p>
<h2>How to avoid being overcharged by a locksmith</h2>
<p>Most complaints about locksmiths in Singapore are about prices that change once the locksmith arrives. Always ask for the total price before work starts, and be careful of very low "from" prices in adverts. Read our guide: <a href="~/guides/how-to-choose-a-locksmith/">how to choose a locksmith in Singapore and avoid overcharging</a>.</p>
<div class="callout navy"><p><strong>Our promise:</strong> the price we agree is the price you pay. {WARRANTY}</p></div>
</div></div></section>
<section class="section section-alt"><div class="container narrow">{x["faq_html"](faqs, "Price Questions")}</div></section>''' +
            x["cta_band"]())
    nodes = x["page_schema"]("prices/", title, desc, crumbs, faqs=faqs, extra=[x["offer_catalog"]()])
    x["render"]("prices/", title, desc, body, nodes, priority="0.9")


# ======================================================================
# ABOUT
# ======================================================================
def build_about(x):
    C_ = x["C"]
    crumbs = [("Home", ""), ("About", "about/")]
    title = "About Uncle Thomas | Singapore Locksmith & Safesmith Since 1998"
    desc = "Meet Uncle Thomas, the locksmith Singapore calls 'Shifu'. An apprentice in 1998, US-trained in safesmithing, he has opened safes on ships and across Asia."
    body = (x["page_hero"](crumbs, 'Meet Uncle Thomas — The Locksmith Singapore Calls "Shifu"',
            f"From apprentice in {C_.FOUNDED} to US-trained safesmith — the story behind Uncle Thomas Locksmith.",
            [f"Since {C_.FOUNDED}", "US-trained safesmith", "Leads a small team"]) +
            f'''<section class="section"><div class="container narrow prose">
{x["photo"]("about_portrait")}
<h2>From apprentice to master locksmith</h2>
<p>Uncle Thomas started in {C_.FOUNDED} as an apprentice under his uncle, learning the trade the traditional way — one lock, one door, one customer at a time. Years of hands-on work across Singapore's HDB flats, condos, shophouses and offices built the foundation he still relies on today.</p>
<h2>Trained in safesmithing in the United States</h2>
<p>Wanting to master the hardest locks in the trade, he spent a year in the United States training in safesmithing — the specialist skill of opening and servicing safes and vaults. It's a skill few locksmiths in Singapore have. <a href="~/safe-opening/">See our safe opening service</a>.</p>
<h2>Trusted overseas — on land and at sea</h2>
<p>That expertise has taken Uncle Thomas far beyond Singapore. He has been called in to open safes for multinational companies and on board ships and cruise liners, with jobs in Thailand, Malaysia, China, Hong Kong and more.</p>
<h2>Keeping up with digital locks</h2>
<p>As homes moved from keys to keypads, Uncle Thomas kept learning. He has developed his own damage-free techniques for opening faulty and locked digital locks — so you get back in without needing to replace an expensive lock. <a href="~/digital-lock-opening/">See digital lock opening</a>.</p>
<h2>Why they call him "Shifu"</h2>
<p>In the trade, Uncle Thomas is known as the "Shifu" — the master other locksmiths turn to when a job gets difficult. Today he leads a small team of locksmiths, and he still personally handles the toughest jobs.</p>
<h2>How we work</h2>
<ul>
<li><strong>24/7, islandwide</strong> — we set off as soon as you call.</li>
<li><strong>Price before work</strong> — <a href="~/prices/">upfront starting prices</a>, and your final price confirmed before we begin.</li>
<li><strong>ID verified</strong> — {ID_POLICY}</li>
<li><strong>Warranty</strong> — {WARRANTY}</li>
<li><strong>Specialists</strong> — we focus on opening doors, digital locks and safes, and on lock replacement and installation. We don't do lock repairs or key duplication.</li>
</ul>
<p>See all our <a href="~/services/">locksmith services</a>.</p>
<div class="photo-grid">{x["photo"]("about_van")}{x["photo"]("about_tools")}</div>
</div></section>''' + x["cta_band"]("Talk to Uncle Thomas", "Locked out, or planning a lock change? Call or WhatsApp — 24/7, islandwide."))
    imgs = [x["photo_schema"](k) for k in ("about_portrait", "about_van", "about_tools")]
    nodes = x["page_schema"]("about/", title, desc, crumbs, page_type="AboutPage", extra=[x["person_node"]()] + imgs)
    nodes[0]["mainEntity"] = {"@id": x["PERSON_ID"]}
    x["render"]("about/", title, desc, body, nodes, priority="0.7")


def build(x):
    from datetime import date
    C.TOKENS["MONTH_YEAR"] = date.today().strftime("%B %Y")
    globals()["ID_POLICY"] = ID_POLICY
    # expand helper tokens used inside service bodies
    for s in SERVICES:
        s["body"] = (s["body"].replace("{ID_POLICY}", ID_POLICY).replace("{WARRANTY}", WARRANTY)
                     .replace("{NO_REPAIR}", NO_REPAIR))
    brand_links = "".join(f'<li><a href="~/digital-lock-opening/{b["slug"]}/">{b["name"]} digital lock</a></li>'
                          for b in x["brands"].BRANDS)
    for s in SERVICES:
        s["body"] = s["body"].replace("{BRAND_LINKS}",
            f'<h3>Brand guides: what to try first</h3><ul class="link-pills">{brand_links}</ul>' if brand_links else "")
    build_home(x)
    build_services(x)
    build_prices(x)
    build_about(x)
