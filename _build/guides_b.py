"""Guide articles, part B. Body text is HTML. ~/ = site root. {P_*} = prices from config."""

GUIDES_B = [
# ---------------------------------------------------------------------------
dict(
 slug="landlord-tenant-lock-change", short="Landlords & tenants: changing locks",
 title="Landlords and Tenants: Changing Locks in Singapore",
 desc="Can a tenant change the locks in Singapore? Can a landlord keep a key? A locksmith's practical guide to lock changes, lockouts and keys in rented homes.",
 h1="Landlords and Tenants: Changing Locks in Singapore",
 card="Who can change the locks in a rented flat, who keeps keys, and how lockouts work for tenants.",
 body="""
<p>Rented flats and rooms are a big part of Singapore's housing, and they raise practical questions every locksmith hears: Can a tenant change the locks? Should a landlord keep a key? Who pays for a lockout? This guide sets out how it usually works and what Uncle Thomas looks for before doing a job in a rented home.</p>
<p><em>This is general information, not legal advice. Your tenancy agreement is the main document that sets out your rights and responsibilities — read it first, and get legal advice if you're in a dispute.</em> <!-- FILL: verify --></p>

<h2>Start with the tenancy agreement</h2>
<p>Most tenancy agreements in Singapore cover locks and keys somewhere — often in clauses about alterations, fixtures, access and the return of keys at the end of the tenancy. Look for:</p>
<ul>
<li>whether the tenant may change or add locks, and whether the landlord's written consent is needed;</li>
<li>how many keys were handed over (this is often listed in the inventory);</li>
<li>whether the landlord may enter the property, and how much notice is needed;</li>
<li>who pays for lost keys, lockouts and lock replacements;</li>
<li>what must be returned at the end of the tenancy.</li>
</ul>
<p>If the agreement says nothing, the safest approach is to agree in writing — a simple WhatsApp message exchange is better than nothing. <!-- FILL: verify --></p>

<h2>For tenants</h2>
<h3>Can I change the locks?</h3>
<p>In most cases, a tenant should get the landlord's written agreement before changing the main door or gate lock, because the locks are part of the landlord's property. <!-- FILL: verify --> Many landlords are happy to agree — especially if you've lost keys, or the old lock is worn — as long as they receive a copy of the new key or the new lock is handed back at the end of the tenancy.</p>
<h3>I've lost my keys. What should I do?</h3>
<p>Tell your landlord or agent as soon as possible, especially if anything with the address was lost too. Changing the cylinder is the only way to be sure the lost keys can't be used. Check your agreement to see who pays — commonly it's the tenant if the keys were lost through the tenant's fault.</p>
<h3>I'm locked out. Can a locksmith help me?</h3>
<p>Yes, if you can show you live there. A tenancy agreement with your name and the address, or a letter or bill addressed to you there, is usually enough. If those documents are inside, tell the locksmith; we can usually check them with you once the door is open. If you rent a room, a room door lockout works the same way.</p>
<h3>Can I add a digital lock?</h3>
<p>Adding a digital lock is an alteration to the door, so get the landlord's agreement first. Some landlords welcome it, especially if you agree to leave it behind at the end of the tenancy. Read our guide to <a href="~/guides/digital-vs-traditional-lock-hdb/">digital vs traditional locks</a>.</p>

<h2>For landlords</h2>
<h3>Change the locks between tenants</h3>
<p>Previous tenants, agents, cleaners and contractors may all have had keys. Replacing the main door cylinder between tenancies is a small cost that protects both you and your new tenant. Many landlords also change the letterbox lock.</p>
<h3>Should I keep a key?</h3>
<p>Many landlords keep a spare key for emergencies, and many tenancy agreements allow the landlord to enter with notice. Make sure the agreement states this clearly, and never enter without following it. If the tenant changes the lock with your agreement, ask for a copy of the new key if the agreement allows it.</p>
<h3>Digital locks for rentals</h3>
<p>Digital and smart locks are popular with landlords because codes can be changed between tenants instead of cutting new keys. Some smart locks also let you issue time-limited codes for agents, cleaners or contractors. If you use a smart lock, keep the admin details safe and remove old codes when a tenancy ends.</p>
<h3>Lockouts and authorisation</h3>
<p>If your tenant calls a locksmith, we'll ask the tenant for proof of residence. If <em>you</em> call us to open a flat that's currently rented out, we'll need to be satisfied that you have the right to enter — for example, proof of ownership and confirmation that the tenancy allows it. We won't open a tenanted home simply because the owner asks.</p>

<h2>At the end of the tenancy</h2>
<ul>
<li>Tenants: return every key and card listed in the inventory, including letterbox keys.</li>
<li>If you changed a lock with permission, return the new keys — or reinstall the original lock if that's what you agreed.</li>
<li>Landlords: check that every key is returned, and change the cylinder before the next tenant moves in.</li>
</ul>

<h2>Disputes</h2>
<p>Lock disputes between landlords and tenants — for example, a landlord changing the locks to keep a tenant out — are serious and can have legal consequences. A locksmith is not the right person to settle them. If you're in a dispute, seek legal advice or mediation; Singapore has community mediation services and the Small Claims Tribunals for some disputes. <!-- FILL: verify which bodies handle tenancy disputes --> Uncle Thomas will not change locks to exclude someone who lives at the property.</p>

<h2>What it costs</h2>
<p>With Uncle Thomas, main door and gate lock replacement starts from <strong>{P_REPLACE}</strong> including supply and installation; letterbox lock replacement from <strong>{P_LETTERBOX}</strong>; and digital lock installation from <strong>{P_DIGITAL_INSTALL}</strong> for labour. Lockouts start from <strong>{P_LOCKOUT}</strong> (9am–6pm) and <strong>{P_AFTERHOURS}</strong> after hours. Every replacement and installation comes with our no-expiry warranty, and we provide receipts for your records. See the <a href="~/prices/">price list</a>.</p>

<h2>Quick checklist</h2>
<ol>
<li>Read the tenancy agreement's clauses on locks, keys and access.</li>
<li>Agree any lock change in writing.</li>
<li>Keep receipts for lock changes and lost-key replacements.</li>
<li>Change cylinders between tenants.</li>
<li>Return all keys at the end of the tenancy.</li>
</ol>

<div class="callout navy"><p><strong>Need a lock changed in a rented home?</strong> Call or WhatsApp {PHONE}. <a href="~/lock-replacement/">More about lock replacement</a>.</p></div>
""",
 faqs=[
  ("Can a tenant change the locks without telling the landlord?", "Generally it's best not to. Locks are usually part of the landlord's property, and most tenancy agreements require consent for alterations. Get agreement in writing first."),
  ("Can a locksmith open a rented flat for the landlord?", "Only if we're satisfied the landlord has the right to enter — for example under the tenancy agreement, with proper notice. We won't help exclude someone who lives there."),
  ("Who pays for a lockout in a rented flat?", "It depends on the tenancy agreement. Often the tenant pays if the lockout was their fault, such as lost keys."),
 ],
),
# ---------------------------------------------------------------------------
dict(
 slug="hdb-gate-lock-types", short="HDB gate lock types",
 title="HDB Gate Lock Types Explained: Which One Do You Have?",
 desc="Hook bolt, padlock, rim lock or digital gate lock? A Singapore locksmith explains the common HDB gate lock types, how they fail and when to replace them.",
 h1="HDB Gate Lock Types Explained",
 card="Hook bolts, padlocks, rim locks and digital gate locks — how they work and how they fail.",
 body="""
<p>Most HDB flats have a metal gate in front of the main door, and the lock on that gate takes a beating: it's exposed to rain, corridor washing, sun and daily use. Knowing which type of gate lock you have helps you look after it, explain a problem to a locksmith, and choose the right replacement. Here are the types Uncle Thomas sees most often.</p>

<h2>1. Mortise hook-bolt gate locks</h2>
<p>A very common HDB gate lock. The lock body sits inside a metal box welded to the gate, and a curved hook bolt swings out to catch the frame. You lock and unlock it with a key from outside and a key or thumb-turn from inside.</p>
<p><strong>How they fail:</strong> the cylinder wears and the key becomes stiff; the hook bolt rusts or jams; the lock body corrodes inside its box after years of water exposure. A key snapping in the cylinder is a common lockout.</p>
<p><strong>Tip:</strong> if the key feels gritty or needs force, the lock is telling you something. A cylinder or lock body replacement now is cheaper than a lockout later.</p>

<h2>2. Padlock and hasp</h2>
<p>Many older gates — and some newer ones as a second lock — use a padlock through a hasp or chain. Simple and cheap, but padlocks are the most exposed lock of all.</p>
<p><strong>How they fail:</strong> rust seizes the shackle or the cylinder; the key snaps; the padlock is lost or stolen. A seized padlock usually has to be cut.</p>
<p><strong>Tip:</strong> choose a weather-resistant padlock (often marketed for outdoor or marine use), and consider a closed-shackle design, which is harder to cut. Replace padlocks that show rust before they seize.</p>

<h2>3. Rim gate locks</h2>
<p>A rim lock is mounted on the surface of the gate rather than inside it. Some are key-operated; many digital gate locks are also rim-mounted.</p>
<p><strong>How they fail:</strong> the latch wears or misaligns with the strike plate as the gate sags; water gets into the lock body; screws loosen with vibration.</p>
<p><strong>Tip:</strong> if your gate needs lifting or pushing to lock, the gate has dropped on its hinges. Fixing the alignment protects the lock.</p>

<h2>4. Digital gate locks</h2>
<p>Digital locks on HDB gates have become very popular, especially in newer estates. They're convenient — no keys — but they live outdoors, which is hard on electronics.</p>
<p><strong>How they fail:</strong> keypads stop responding after rain or washing; batteries drain faster in heat; fingerprint readers struggle in humid conditions; cheap models corrode.</p>
<p><strong>Tip:</strong> choose a model designed for outdoor gate use, change batteries at the first warning, and keep the backup key outside the home. See <a href="~/guides/digital-lock-battery-dead/">digital lock battery dead</a>.</p>

<h2>5. Sliding and bi-fold gate locks</h2>
<p>Some flats have sliding or folding gates with their own locking mechanisms — a hook or latch built into the gate, usually with a key cylinder.</p>
<p><strong>How they fail:</strong> track debris stops the gate closing fully; the latch misaligns; the cylinder wears.</p>
<p><strong>Tip:</strong> keep the track clean, and don't force a gate that won't close — find out why first.</p>

<h2>How to tell which lock you have</h2>
<ul>
<li><strong>Lock hidden inside a metal box on the gate, curved bolt</strong> → mortise hook-bolt lock.</li>
<li><strong>Separate lock hanging through a loop</strong> → padlock and hasp.</li>
<li><strong>Lock box screwed to the surface of the gate</strong> → rim lock.</li>
<li><strong>Keypad or fingerprint reader</strong> → digital gate lock.</li>
</ul>
<p>If you're not sure, take a photo of the outside and inside of the lock and send it to us on WhatsApp — we'll tell you what it is.</p>

<h2>Looking after your gate lock</h2>
<ul>
<li>Avoid splashing water into the lock when washing the corridor.</li>
<li>Use a proper lock lubricant — not cooking oil, which attracts dirt — once or twice a year.</li>
<li>Don't use the key as a handle to pull the gate.</li>
<li>Fix a sagging gate before it damages the lock.</li>
<li>Replace stiff or rusty locks before they fail.</li>
</ul>

<h2>HDB rules on gates</h2>
<p>HDB has rules about gates and what can be installed in common corridors, and you may need to check the requirements before replacing a gate or making major changes. <!-- FILL: verify current HDB rules on gate installation and replacement --> Replacing the lock on an existing gate is generally a routine job.</p>

<h2>What it costs</h2>
<p>With Uncle Thomas, gate lock replacement starts from <strong>{P_REPLACE}</strong> including supply and installation, and every replacement has our no-expiry warranty. If you're locked out by a gate lock, lockouts start from <strong>{P_LOCKOUT}</strong> (9am–6pm) and <strong>{P_AFTERHOURS}</strong> after hours. Digital gate lock installation starts from <strong>{P_DIGITAL_INSTALL}</strong> for labour. See the full <a href="~/prices/">price list</a> and <a href="~/lock-replacement/">lock replacement</a>.</p>

<div class="callout navy"><p><strong>Gate lock stuck or worn?</strong> Send a photo to {PHONE} and we'll tell you what it is and what it'll cost.</p></div>
""",
 faqs=[
  ("What's the most common HDB gate lock?", "Mortise hook-bolt gate locks and padlocks are very common on HDB gates, with digital gate locks increasingly popular in newer flats."),
  ("Why does my gate lock keep jamming?", "Usually rust, a worn cylinder, or a gate that has sagged so the bolt no longer lines up. A locksmith can tell you which."),
  ("Can I put a digital lock on my HDB gate?", "Yes, many people do. Choose a model designed for outdoor use and make sure it suits your gate."),
 ],
),
# ---------------------------------------------------------------------------
dict(
 slug="digital-vs-traditional-lock-hdb", short="Digital vs traditional lock",
 title="Digital Lock vs Traditional Lock for HDB: Which to Choose?",
 desc="Digital lock or traditional key lock for your HDB flat? A locksmith compares security, cost, reliability and convenience to help you choose.",
 h1="Digital Lock vs Traditional Lock for HDB: Which Should You Choose?",
 card="Security, cost, reliability and convenience — an honest comparison from a locksmith.",
 body="""
<p>If you're moving into a new BTO, renovating, or replacing a worn lock, one of the first decisions is whether to go digital. Uncle Thomas opens and installs both every week, so here's an honest comparison — including the downsides that sellers don't always mention.</p>

<h2>The quick answer</h2>
<ul>
<li><strong>Choose digital</strong> if you want no keys, easy access for family or helpers, and you'll change batteries on time.</li>
<li><strong>Choose traditional</strong> if you want the simplest, most power-independent option, or your door isn't suitable for a digital lock.</li>
<li><strong>Many households do both:</strong> a digital lock on the main door and a key lock on the gate, or the other way round.</li>
</ul>

<h2>Convenience</h2>
<p><strong>Digital locks</strong> win easily. No keys to lose, forget or copy; you can give family a PIN, register fingerprints for children, and change codes when a helper or tenant leaves. Some smart locks add app control and temporary codes for visitors.</p>
<p><strong>Traditional locks</strong> mean carrying keys and cutting copies, and a lost key often means changing the lock.</p>

<h2>Reliability</h2>
<p><strong>Traditional locks</strong> have no electronics to fail. A good-quality mechanical lock, looked after, can last many years — although cylinders do wear, and keys snap in old locks.</p>
<p><strong>Digital locks</strong> rely on batteries, motors and electronics. Most lockouts we see with digital locks are flat batteries, wet keypads or failed motors. Quality varies a lot: well-known brands tend to cope better with Singapore's heat and humidity than the cheapest online models. Gate-mounted digital locks have the toughest life because they're outdoors.</p>

<h2>Security</h2>
<p>Both can be secure if you choose well and install properly. A cheap lock of either kind is a weak point.</p>
<ul>
<li><strong>Traditional:</strong> security depends on the cylinder quality and how many keys exist. Old cylinders may be easier to manipulate, and you never know how many copies of an old key are out there.</li>
<li><strong>Digital:</strong> no keys to copy, and codes can be changed. But PINs can be seen over your shoulder, smudges on keypads can give away digits, and some cheap models have weak mechanical overrides. Choose a reputable brand, use a scramble or "fake digits" feature if it has one, and wipe the keypad occasionally.</li>
</ul>

<h2>Cost</h2>
<p>Traditional locks are cheaper to buy and install. Digital locks cost more upfront — the lock itself plus installation — and need batteries. But digital locks can save money later: no key cutting, and no lock change just because a key was lost or a tenant moved out.</p>

<h2>Lockouts: what's it like when things go wrong?</h2>
<p>With a <strong>traditional lock</strong>, lockouts usually mean lost keys or a snapped key, and a locksmith can normally open the lock without damage.</p>
<p>With a <strong>digital lock</strong>, many lockouts can be solved by the owner — emergency power and the backup key. When they can't, opening a faulty digital lock is specialist work. Uncle Thomas has developed his own damage-free methods for this; see <a href="~/digital-lock-opening/">digital lock opening</a>.</p>

<h2>Is your HDB door suitable for a digital lock?</h2>
<p>Most HDB main doors can take a digital lock, but check:</p>
<ul>
<li><strong>Door thickness</strong> — each lock supports a range.</li>
<li><strong>Existing cut-outs</strong> — a lock that matches the existing mortise cut-out avoids extra cutting.</li>
<li><strong>Door condition</strong> — a door that has dropped or warped will strain any lock.</li>
<li><strong>Fire-rated main door</strong> — HDB main doors are generally fire-rated, and installation shouldn't compromise the door. <!-- FILL: verify HDB guidance on installing digital locks on fire-rated main doors --></li>
<li><strong>Gate type</strong> — gate locks need to suit the gate's frame and be designed for outdoor use.</li>
</ul>
<p>Send us a photo of your door's edge and both sides and we'll tell you what fits.</p>

<h2>Our recommendation by situation</h2>
<ul>
<li><strong>Families with children or elderly parents:</strong> digital on the main door, with PINs for trusted family and a mechanical backup key kept outside the home.</li>
<li><strong>Landlords:</strong> digital, so codes can be changed between tenants.</li>
<li><strong>People who travel often or forget to change batteries:</strong> consider a good mechanical lock, or a digital lock with a reliable low-battery warning and emergency power.</li>
<li><strong>Older flats with worn doors:</strong> fix the door alignment first, then choose.</li>
</ul>

<h2>What it costs</h2>
<p>With Uncle Thomas, digital lock installation starts from <strong>{P_DIGITAL_INSTALL}</strong> for labour (the lock is supplied by you or us), and traditional main door or gate lock replacement starts from <strong>{P_REPLACE}</strong> including supply and installation. Every installation and replacement has our no-expiry warranty. If you're locked out, digital lock opening starts from <strong>{P_DIGITAL_OPEN}</strong> and standard lockouts from <strong>{P_LOCKOUT}</strong>. See the full <a href="~/prices/">price list</a>, <a href="~/digital-lock-installation/">digital lock installation</a> and <a href="~/lock-replacement/">lock replacement</a>.</p>

<div class="callout navy"><p><strong>Not sure which to choose?</strong> WhatsApp a photo of your door to {PHONE} and Uncle Thomas will recommend options that fit.</p></div>
""",
 faqs=[
  ("Are digital locks safe for HDB flats?", "Yes, if you choose a reputable model and it's installed properly. Keep the backup key outside the home and change batteries on time."),
  ("Do digital locks work during a power cut?", "Yes — they run on their own batteries, not mains power."),
  ("Which lasts longer, digital or traditional?", "A good mechanical lock usually outlasts a digital lock, which has electronics and a motor. But a quality digital lock, looked after, gives years of service."),
 ],
),
# ---------------------------------------------------------------------------
dict(
 slug="locksmith-cost-singapore", short="Locksmith cost in Singapore",
 title="How Much Does a Locksmith Cost in Singapore? (2026 Guide)",
 desc="How much does a locksmith cost in Singapore in 2026? Typical prices for lockouts, digital locks, car lockouts, lock changes, letterboxes and safes.",
 h1="How Much Does a Locksmith Cost in Singapore? (2026)",
 card="Typical 2026 prices for every common locksmith job — and what makes a price go up.",
 body="""
<p>Locksmith prices in Singapore can seem confusing: one advert says "from $39", another "from $90", and the final bill can be very different from either. This guide explains what locksmith jobs typically cost in 2026, what changes the price, and how to make sure you pay a fair amount. For our exact rates, see our <a href="~/prices/">price list</a>.</p>

<h2>Uncle Thomas's prices at a glance</h2>
<ul>
<li>Home / office lockout (9am–6pm): from <strong>{P_LOCKOUT}</strong> — <a href="~/emergency-locksmith/">emergency lockout</a></li>
<li>Lockout after hours, weekends &amp; public holidays: from <strong>{P_AFTERHOURS}</strong></li>
<li>Digital lock emergency opening: from <strong>{P_DIGITAL_OPEN}</strong> — <a href="~/digital-lock-opening/">digital lock opening</a></li>
<li>Digital lock installation (labour): from <strong>{P_DIGITAL_INSTALL}</strong> — <a href="~/digital-lock-installation/">installation</a></li>
<li>Car lockout: from <strong>{P_CAR}</strong> — <a href="~/car-locksmith/">car locksmith</a></li>
<li>Main door / gate lock replacement (supply + install): from <strong>{P_REPLACE}</strong> — <a href="~/lock-replacement/">lock replacement</a></li>
<li>Letterbox lock replacement: from <strong>{P_LETTERBOX}</strong> — <a href="~/letterbox-lock-replacement/">letterbox locks</a></li>
<li>Safe opening: quoted per job — <a href="~/safe-opening/">safe opening</a></li>
</ul>
<p>These are starting prices. Your final price is confirmed before any work begins.</p>

<h2>What the wider market charges</h2>
<p>Published starting prices from Singapore locksmiths in 2026 generally put a standard daytime lockout somewhere around S$80–S$90, with after-hours lockouts higher. Some locksmiths advertise much lower "call-out" or "from" prices; these often don't include the actual work. Digital lock opening, safes and lock replacements typically cost more than a basic lockout. Prices change, so always confirm with the locksmith you call.</p>

<h2>What makes a locksmith price go up?</h2>
<h3>1. Time of day</h3>
<p>Most locksmiths charge more after office hours, late at night, on weekends and on public holidays. With us, that's the difference between {P_LOCKOUT} and {P_AFTERHOURS} for a lockout.</p>
<h3>2. Type of lock</h3>
<p>A standard HDB mortise lock is usually quicker to open than a high-security deadbolt, a double-locked door, or a faulty digital lock. Safes vary the most of all.</p>
<h3>3. Whether parts are needed</h3>
<p>If the lock is broken, badly worn, or a key has snapped and damaged the cylinder, the lock may need replacing. The new lock and fitting are added to the price — a good locksmith shows you the options and the cost first.</p>
<h3>4. Damage-free vs destructive entry</h3>
<p>Damage-free opening takes skill but saves you the cost of a new lock. Drilling is sometimes necessary, but then a replacement is almost always needed too.</p>
<h3>5. Location and access</h3>
<p>Most locksmiths cover the whole island at the same rates, but access issues — condo guardhouses, office buildings, carparks — can add time.</p>

<h2>Costs that catch people out</h2>
<ul>
<li><strong>Call-out fees</strong> quoted on their own, with the real work charged on top.</li>
<li><strong>"Special tool" charges</strong> added on site.</li>
<li><strong>Unnecessary drilling</strong> followed by an expensive replacement lock.</li>
<li><strong>Cheap replacement locks</strong> that fail again within months.</li>
</ul>
<p>Our guide on <a href="~/guides/how-to-choose-a-locksmith/">how to choose a locksmith and avoid overcharging</a> covers the warning signs.</p>

<h2>Is it cheaper to replace the lock or keep calling a locksmith?</h2>
<p>If a lock keeps jamming, or you've been locked out more than once by the same lock, replacing it is usually cheaper in the long run. A main door or gate lock replacement starts from {P_REPLACE} with us — often not much more than a second lockout — and comes with our no-expiry warranty.</p>

<h2>How to get an exact price in a minute</h2>
<ol>
<li>Take a photo of the lock — outside and inside if you can.</li>
<li>WhatsApp it to {PHONE} with your location.</li>
<li>Tell us what happened (lost keys, snapped key, dead battery, etc.).</li>
<li>We reply with a firm price before anyone sets off.</li>
</ol>

<h2>Does insurance cover locksmith costs?</h2>
<p>Some home insurance policies cover lock replacement after a break-in or theft of keys. <!-- FILL: verify --> Check your policy, and keep the locksmith's receipt in case you need to claim.</p>

<div class="callout navy"><p><strong>Our promise:</strong> the price we agree is the price you pay. Call or WhatsApp {PHONE}, 24/7. <a href="~/prices/">See the full price list</a>.</p></div>
""",
 faqs=[
  ("How much is a locksmith in Singapore for a lockout?", "Uncle Thomas charges from {P_LOCKOUT} for a daytime lockout and from {P_AFTERHOURS} after hours, weekends and public holidays. Published market prices generally start around S$80–S$90."),
  ("Why do locksmiths charge more at night?", "After-hours work means the locksmith is on call around the clock. Most locksmiths in Singapore charge a higher rate for nights, weekends and public holidays."),
  ("Is there a call-out fee?", "We quote the job at your location and tell you the total before we set off, so you won't be surprised by extra fees."),
  ("How much does it cost to change a lock in Singapore?", "With us, main door or gate lock replacement starts from {P_REPLACE} including supply and installation, with a no-expiry warranty."),
 ],
),
]
