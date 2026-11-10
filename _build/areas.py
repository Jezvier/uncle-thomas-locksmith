"""
Areas hub + individual town pages.

Each town has its own local text — estates, landmarks, MRT, the kinds of
buildings and locks found there, common jobs and practical access tips — so
pages are genuinely useful, not copy-paste "doorway" pages. Shared text is
kept short on purpose.

Add a town by appending to TOWNS. Add real recent jobs in config.RECENT_JOBS.
"""
import config as C

TOWNS = [
# ======================= CENTRAL =======================
dict(slug="toa-payoh", name="Toa Payoh", region="Central",
 intro="Toa Payoh is one of Singapore's oldest HDB towns, so many homes still have original main door and gate locks — and older locks are the ones most likely to jam, wear out or snap a key.",
 overview="Toa Payoh was among the first new towns built by HDB, and it shows: alongside the newer Bidadari estates you'll find decades-old blocks around Toa Payoh Central and the Lorongs, where the same family may have used the same lock for thirty years. We're called here for everything from stiff old mortise locks to brand-new digital locks, plus workshops and small businesses in the Lorong 8 industrial area.",
 estates=["Toa Payoh Central", "Lorong 1–8", "Kim Keat", "Boon Teck", "Bidadari", "Braddell", "Caldecott"],
 landmarks=["HDB Hub", "Toa Payoh Town Park", "Toa Payoh Sports Complex", "Lorong 8 Industrial Estate"],
 mrt=["Toa Payoh", "Braddell", "Caldecott", "Woodleigh"],
 buildings=[
  ("Mature HDB blocks", "Original timber main doors with mortise locks and hook-bolt gate locks are common. After years of use and corridor washing, cylinders get stiff and keys can break off inside — we extract the broken key and replace the cylinder if it's worn."),
  ("Bidadari and newer flats", "Many owners have fitted digital locks on the main door or gate. Flat batteries and forgotten PINs are the usual reasons for a call."),
  ("Workshops and shops", "Roller shutters, padlocks and office doors in the Lorong 8 area — usually early-morning lockouts before opening time."),
 ],
 jobs=["Worn HDB main door locks that jam or won't turn", "Broken key stuck in the gate lock", "Digital lock upgrades in older flats", "Toilet and bedroom doors locked from inside"],
 access="Tell us your block number and which lift lobby you're nearest — some older Toa Payoh blocks have several stacks and lift lobbies. If you're waiting downstairs, the void deck of your block is the easiest meeting point.",
 faqs=[
  ("My old HDB gate lock in Toa Payoh is stuck. Can you open it?", "Yes. Older hook-bolt and gate padlocks are among the most common jobs we do in Toa Payoh. We open it first, then advise whether the lock should be replaced."),
  ("Do you serve Bidadari?", "Yes — Bidadari is part of Toa Payoh town and we cover it 24/7, along with Braddell, Caldecott and Kim Keat."),
 ],
 nearby=["bishan", "novena"]),

dict(slug="bishan", name="Bishan", region="Central",
 intro="Bishan mixes HDB estates, private condominiums and landed homes towards Thomson, plus workshops around Sin Ming — so jobs here range from home lockouts to commercial locks and safes.",
 overview="Bishan sits in the middle of the island, which makes it one of the easiest towns for us to reach at any hour. The HDB blocks around Bishan Central and Junction 8 are popular with families, condos line Bishan and Sin Ming, and the streets towards Upper Thomson are mostly landed homes. The Sin Ming industrial area adds workshops, car workshops and small offices to the mix.",
 estates=["Bishan Central", "Bishan North", "Bishan East", "Sin Ming", "Marymount", "Upper Thomson"],
 landmarks=["Junction 8", "Bishan-Ang Mo Kio Park", "Bishan Stadium", "Sin Ming Industrial Estate"],
 mrt=["Bishan", "Marymount", "Bright Hill", "Upper Thomson"],
 buildings=[
  ("Condominiums", "Condo main doors often have a deadbolt plus a digital lock. We coordinate with the guardhouse so we can get to your unit quickly."),
  ("Landed homes", "Main gates, side gates and back doors — often with several locks per entrance. A locked side gate can be the only way into the house."),
  ("Sin Ming workshops", "Roller shutters, cabinet locks and small business safes."),
 ],
 jobs=["Condo main door and digital lock lockouts", "Landed home gate and side door locks", "Office and workshop lock changes in Sin Ming", "Home safe opening"],
 access="For condos, please let the guardhouse know a locksmith is coming, or meet us at the drop-off point. For landed homes near Thomson, a quick message with the gate you're locked out of saves time.",
 faqs=[
  ("Can you get past my condo guardhouse in Bishan?", "We'll need you or management to let the guard know we're coming. Most condos simply ask for the unit number and your name."),
  ("Do you open safes in Bishan homes?", "Yes. Uncle Thomas is a US-trained safesmith. WhatsApp a photo of the safe for a quote."),
 ],
 nearby=["toa-payoh", "ang-mo-kio"]),

dict(slug="novena", name="Novena & Balestier", region="Central",
 intro="Novena and Balestier combine hospitals and medical suites, Balestier's shophouses and quiet condos and landed homes — so our calls here are a mix of clinic, shop and home lockouts.",
 overview="Novena is best known for its hospitals and medical centres, and the offices and clinics that come with them. Along Balestier Road, rows of shophouses hold eateries, lighting shops and family businesses, many with roller shutters and older padlocks. Behind the main roads are condominiums, walk-up apartments and landed streets around Moulmein, Whitley and Thomson.",
 estates=["Novena", "Balestier", "Moulmein", "Whitley", "Thomson Road", "Goldhill"],
 landmarks=["Novena Square", "Velocity", "United Square", "Tan Tock Seng Hospital", "Balestier shophouses"],
 mrt=["Novena", "Newton", "Toa Payoh"],
 buildings=[
  ("Clinics and medical suites", "Suite doors, cabinet locks and drug cupboard locks. We work early or after hours so clinics can open on time."),
  ("Balestier shophouses", "Roller shutters, collapsible gates and back-lane doors — older padlocks and hasps wear out and rust."),
  ("Condos and walk-ups", "Digital locks on main doors, and older cylinder locks in walk-up apartments."),
 ],
 jobs=["Clinic and office lockouts before opening hours", "Shophouse shutter padlocks cut and replaced", "Condo digital lock lockouts", "Cabinet and document safe opening"],
 access="For medical buildings, let building security know a locksmith is coming. Shophouse owners — tell us whether you're locked out at the front shutter or the back lane.",
 faqs=[
  ("Can you open our clinic before patients arrive?", "Yes — we work 24/7, so we can come early in the morning. We'll need authorisation from the clinic owner or manager."),
  ("Do you handle shophouse roller shutters on Balestier Road?", "Yes, we open locked shutters and replace worn padlocks and shutter locks."),
 ],
 nearby=["toa-payoh", "cbd-orchard"]),

dict(slug="cbd-orchard", name="Orchard & CBD", region="Central",
 # Rewritten 9 Nov 2026 around the real Orchard and CBD jobs in config.JOBS. Targets "locksmith orchard",
 # "locksmith orchard road", "locksmith cbd", "locksmith raffles place". Facts only: prices from config.PRICES,
 # arrival from TOKENS["ARRIVAL"] (owner-confirmed), safe experience from CLAUDE.md (never name clients).
 title="Locksmith Orchard Road & CBD | 24/7 Lockouts and Safes",
 desc="24/7 locksmith for Orchard Road and the CBD: locked room doors, office safes, gates and digital locks. US-trained safesmith, real local jobs. Call 9224 9224.",
 h1="Locksmith in Orchard Road and the CBD, 24/7",
 intro="From Orchard Road apartments to Raffles Place offices, city calls tend to be urgent and awkward: a bedroom door that won't open, an office safe that rejects its code, a gate locked shut after hours. Uncle Thomas handles all three, day and night.",
 overview="The city is where Singapore lives and works on top of each other. Orchard Road and Somerset are lined with condos, serviced apartments, hotels and malls; a few minutes south, Raffles Place, Tanjong Pagar, Telok Ayer and Marina Bay fill with offices by day and empty out by night, with shophouses, restaurants and bars in between. That mix shapes the work: apartment room doors and high-end digital locks around Orchard, and office doors, cash safes, gates and shutters in the CBD.",
 feature="""
<h2>What our Orchard and CBD jobs actually look like</h2>
<p>Ask most people what a locksmith does and they picture a front door. In the city, the pattern is different. Every Orchard Road job we logged this autumn was an <strong>interior door</strong>: a worn knob that broke and trapped a resident out of her room, a cracked bedroom lock that needed replacing, and a painter locked out of a room. In the CBD, the calls were a <strong>Bumil keypad safe</strong> that refused to open and a <strong>metal gate</strong> held shut by its surface-mounted lock. Each one is listed, with photos, further down this page.</p>
<p>Why room doors? City apartments are full of knob and lever locksets with privacy buttons, and many are budget fittings that have seen years of tenants. Latches wear, knobs work loose, and one day the door closes and simply won't open again. The good news is that most of these open quickly and without damage. The fastest Orchard job so far took Uncle Thomas under a minute; another had the resident back in her room within 2 minutes. If the lock itself has broken, we fit a new lockset in the same visit.</p>

<h2>Locked out of a room in an Orchard apartment</h2>
<p>Before you call, check the outside of the knob or lever for a small hole or slot. Many privacy locks have an emergency release there, meant for exactly this moment. If there isn't one, or it doesn't work, don't force the door: a shoulder or a screwdriver usually damages the frame, and the repair costs more than the call-out. Our guide to <a href="~/guides/room-door-locked-from-inside/">a room door locked from the inside</a> walks through the safe things to try. Still stuck? WhatsApp a photo of the lock to {PHONE} and we'll tell you what it will take.</p>

<h2>Office safes, cash safes and hotel safes in the CBD</h2>
<p>Safes are where the city work gets serious. Uncle Thomas trained as a safesmith in the United States and has opened safes for offices, pawnshops, hotels and banks, including safe deposit boxes and vault doors. We never name clients, and we work after hours so your business isn't disrupted. Companies get a proper invoice.</p>
<p>Some safes can be opened and stay fully usable, like the Bumil keypad safe we opened through its override lock in the CBD this month. But when a safe's lock has failed, it usually has to be drilled, precisely and at the right point, and a new lock can often be fitted afterwards. We'll tell you which situation you're in, and the price, before we start. Safe opening starts from {P_SAFE}. See <a href="~/safe-opening/">safe opening</a>, <a href="~/commercial-safe-services/">commercial safe services</a> and <a href="~/hotel-safe-opening/">hotel safe opening</a>.</p>

<h2>Gates, shutters and back-of-house doors</h2>
<p>Shophouses around Telok Ayer, Chinatown and Tanjong Pagar often have a front shutter, a metal gate and a back door onto the lane, each with its own lock. When you call, tell us which one is stopping you: it changes what we bring and how long it takes. Gate locks exposed to rain and heat are the usual culprits. If a lock has seized or is past saving, we replace it in the same visit; see <a href="~/roller-shutter-lock/">roller shutter locks</a> and <a href="~/lock-replacement/">lock replacement</a>.</p>

<h2>Getting us in the building faster</h2>
<p>In the city, the lock is rarely the slowest part of the job. Getting to it is. A few minutes of preparation saves the most time:</p>
<ul>
<li><strong>Tell security or the guardhouse a locksmith is coming</strong>, with your name and unit. Many office towers need tenants to register contractors, especially after hours.</li>
<li><strong>Send us the building name, unit and nearest loading bay or carpark</strong> on WhatsApp, with a pinned location.</li>
<li><strong>Photograph the lock</strong> (or the safe's front and brand label) so we can bring the right parts and confirm the price.</li>
<li><strong>Have your proof ready.</strong> We check NRIC, Singpass or other ID before opening anything. For offices and shops we need authorisation from the business; for rentals and serviced apartments, from the landlord or management.</li>
</ul>
<p>The city is a short drive from our usual base around Toa Payoh, so we usually arrive within {ARRIVAL}, any hour. Daytime lockouts start from {P_LOCKOUT}, and nights, weekends and public holidays from {P_AFTERHOURS}. Full details are on our <a href="~/prices/">price list</a>.</p>
""",
 estates=["Orchard Road", "Somerset", "Dhoby Ghaut", "Raffles Place", "Tanjong Pagar", "Telok Ayer", "Marina Bay", "Shenton Way", "Chinatown", "Robertson Quay"],
 landmarks=["ION Orchard", "Ngee Ann City", "Raffles Place", "Marina Bay Sands", "Lau Pa Sat", "Chinatown"],
 mrt=["Orchard", "Somerset", "Dhoby Ghaut", "Raffles Place", "Tanjong Pagar", "Telok Ayer", "Downtown", "Chinatown", "Marina Bay"],
 buildings=[
  ("Orchard condos and serviced apartments", "Room doors with knob and lever locks, main doors with high-end digital locks and deadbolts. We check proof of residence, or authorisation from the landlord or management, before opening."),
  ("Office towers in Raffles Place, Marina Bay and Shenton Way", "Office doors, glass doors, cabinets and safes. Most buildings need the tenant to register us with security before we go up, especially after hours."),
  ("Shophouses, restaurants and bars", "Front shutters, metal gates, back-lane doors and cash safes, usually before opening or after closing time."),
  ("Hotels", 'Guest room safes and back-office safes, always through hotel management. See <a href="~/hotel-safe-opening/">hotel safe opening</a>.'),
 ],
 jobs=["Room doors locked in Orchard apartments", "Office, shop and hotel safes that won't open", "Metal gates and shophouse shutters", "Digital lock lockouts in city condos", "Lock changes when staff or tenants leave"],
 access="Parking in the city is limited, so tell us the building's loading bay or nearest carpark if you know it. For offices and condos, let security or the guardhouse know we're coming.",
 faqs=[
  ("How quickly can a locksmith reach Orchard Road?", "Orchard is a short drive from our usual base around Toa Payoh, so we usually arrive within {ARRIVAL}, day or night. Building access can add a few minutes, so let security know we're coming."),
  ("Can you open a locked bedroom door in an Orchard apartment without damage?", "Usually, yes. Most room door locks open without damage: this November Uncle Thomas had one open in under a minute. If the lock itself has broken, we fit a new lockset in the same visit."),
  ("Do you open office safes in Raffles Place, Tanjong Pagar and Marina Bay?", "Yes, after hours too. Uncle Thomas is a US-trained safesmith who has opened safes for offices, pawnshops, hotels and banks. We need authorisation from the business, and we issue an invoice."),
  ("Can you come to our CBD office at night or on weekends?", "Yes. We work 24/7, and after-hours visits mean no disruption to your business. Please arrange building access with security."),
 ],
 nearby=["river-valley", "tanglin", "newton", "novena", "paterson", "bukit-merah"]),

dict(
 slug="newton", name="Newton", region="Central",
 # Long-form rewrite 10 Nov 2026 (no real jobs yet: guidance only, facts from CLAUDE.md and config).
 title='Locksmith Newton | Condo Digital Locks, Safes and Cars 24/7',
 desc='24/7 locksmith in Newton, Cairnhill and Scotts Road: condo digital lock lockouts, home safes and cars in basement carparks. Safe specialist. Call 9224 9224.',
 h1='Locksmith in Newton, Cairnhill and Scotts Road, 24/7',
 intro="Newton is condo country, between Orchard and Novena — so most of our calls here are digital lock lockouts, home safes and cars in condo carparks.",
 overview="Newton sits just north of Orchard, around Newton Circus and the hawker centre that gives the area its name. Most homes are private condominiums and apartments along Newton Road, Scotts Road, Cairnhill and the streets off Bukit Timah Road, with a few landed pockets and older walk-up apartments. That means high-end digital locks, home safes in bedrooms and study rooms, and cars parked in basement carparks.",
 feature="""
<h2>Why Newton calls are different from the heartlands</h2>
<p>Newton is almost entirely private housing. Between Newton Circus, Cairnhill, Scotts Road and the streets off Bukit Timah Road, nearly every front door belongs to a condominium unit, and nearly every unit has a digital lock. The classic heartland call, an old mortise lock that has finally worn out, is rare here. What we see instead falls into three groups: a digital or smart lock that won't let the owner in, a home safe that won't open, and a car locked in a basement carpark with the key inside.</p>
<p>All three have something in common: the lock itself is usually fine. A dead battery, a forgotten code or a key left on the passenger seat is the real problem, so most Newton jobs end with nothing broken and nothing to replace.</p>

<h2>Digital lock lockouts in Newton condos</h2>
<p>Most condo digital locks give weeks of warning before the batteries die: a beep, a flashing icon, a voice prompt. In a busy household that warning is easy to ignore, and the lock fails on the one evening the backup key is sitting in a drawer inside. Before you call us, try these in order:</p>
<ol>
<li><strong>Look for the emergency power point.</strong> Many locks have a USB port, or two contacts for a 9V battery, under the keypad. A power bank can wake the lock long enough to enter your PIN.</li>
<li><strong>Find the key override.</strong> Most models hide a mechanical keyhole behind a small cover. It only helps if the key is outside the flat.</li>
<li><strong>Check the lock isn't in privacy or double-lock mode</strong>, which some brands use to block the keypad when someone inside has locked up for the night.</li>
</ol>
<p>If none of that works, WhatsApp us the brand and a photo of the keypad. We open digital and smart locks of every brand, usually without damage, and replace the batteries before we leave. Emergency digital lock opening starts from {P_DIGITAL_OPEN}. Our guide to <a href="~/guides/digital-lock-battery-dead/">a digital lock with a dead battery</a> has more detail, and the <a href="~/digital-lock-opening/">digital lock opening</a> page covers the brands we see most.</p>

<h2>Home safes: a forgotten code is not the same as a faulty safe</h2>
<p>Newton families tend to keep passports, jewellery and documents in a bedroom or wardrobe safe, and the call often comes a day or two before a flight. How we open it depends on what has gone wrong. If the code has simply been forgotten and the lock is healthy, there are often ways in that leave the safe as it was: the override key, a manufacturer reset with proof of ownership, or, on high-security combination locks, manipulation by feel and sound, a skill Uncle Thomas trained in. If the lock itself has failed, the honest answer is different: most faulty safes have to be drilled. Done properly, that means one small, precise hole, and about 90% of drilled safes can be repaired and used again.</p>
<p>Either way, we tell you which case you're in, and the price, before we start. Safe opening starts from {P_SAFE}. If the safe holds something you need for a trip, say so when you call. See <a href="~/safe-opening/">safe opening</a> and <a href="~/guides/forgot-safe-combination/">forgot your safe combination</a>.</p>

<h2>Cars in condo basements</h2>
<p>Newton's condo carparks are deep, and phone signal down there is often poor, so many owners call us from the lift lobby. Send the carpark level, lot number and car model, and let the guardhouse know a locksmith is coming. We open cars of all major brands with non-destructive tools, from {P_CAR}, after checking your NRIC against the log card. If one remote key is shared between two drivers, a cloned spare fob stops it happening again: see <a href="~/car-key-duplicate/">spare car key fob</a>.</p>

<h2>Getting in at night</h2>
<p>Newton is one of the closest areas to our usual base around Toa Payoh, a short run down Thomson Road or the CTE, so late-night jobs here move quickly. The slow part is usually the gate. Tell the guardhouse your unit and that a locksmith is expected, and have ID showing your address ready. Daytime lockouts start from {P_LOCKOUT}; nights, weekends and public holidays from {P_AFTERHOURS}.</p>
""",
 estates=["Newton Road", "Cairnhill", "Scotts Road", "Kampong Java", "Stevens Road", "Bukit Timah Road"],
 landmarks=["Newton Food Centre", "Newton Circus", "Cairnhill", "Scotts Road"],
 mrt=["Newton", "Stevens", "Orchard"],
 buildings=[
  ("Condominiums and apartments", "Digital and smart locks on main doors, often with a second deadbolt. The guardhouse will need to know we're coming, and we check proof of residence before opening."),
  ("Home safes", "Many Newton homes keep passports, jewellery and documents in a bedroom or wardrobe safe. Uncle Thomas opens home safes of every type and changes combinations."),
  ("Basement carparks", "Car lockouts in condo carparks are common here. Tell us the level and lot number, and the guardhouse can let us in."),
 ],
 jobs=["Digital lock lockouts in condos", "Home safes that won't open", "Car lockouts in condo carparks", "Main door lock changes after a tenancy"],
 access="Most Newton condos have a guardhouse, so let them know a locksmith is coming and give us the block and unit. For car lockouts, tell us the carpark level and lot number.",
 faqs=[
  ("Can you open a home safe in a Newton condo?", "Yes. Uncle Thomas opens home safes of every type. If the code is forgotten but the lock works, it can often be opened without damage; a faulty lock usually means drilling, and most drilled safes can be repaired. We check that the safe is yours first."),
  ("Do you come to Newton late at night?", "Yes, 24/7. Newton is central, so it's quick for us to reach, usually within 25–30 minutes."),
  ('My condo digital lock is dead and the backup key is inside. What now?', 'Try the emergency power point under the keypad with a power bank or a 9V battery. If that fails, WhatsApp us the brand and a photo. We open all digital and smart lock brands and replace the batteries on the spot.'),
  ('How much does it cost to open a safe in Newton?', "Safe opening starts from {P_SAFE}. Send a photo of the safe's front and brand label, and we'll confirm the price before we come."),
 ],
 nearby=["cbd-orchard", "novena", "paterson"],
),
dict(
 slug="paterson", name="Paterson", region="Central",
 # Long-form rewrite 10 Nov 2026 (no real jobs yet: guidance only, facts from CLAUDE.md and config).
 title='Locksmith Paterson & Orchard Boulevard | Safes, Smart Locks',
 desc='24/7 locksmith for Paterson Road, Paterson Hill and Orchard Boulevard: luxury smart locks, watch and home safes, lock changes between tenants. Call 9224 9224.',
 h1='Locksmith in Paterson and Orchard Boulevard, 24/7',
 intro="Paterson is a quiet, upmarket pocket just off Orchard Road — our calls here are mostly luxury condo digital locks, home safes and cars.",
 overview="Paterson Road and Paterson Hill run between Orchard Road and River Valley, a few minutes' walk from Orchard Boulevard. It's an area of luxury condominiums, serviced residences and a few landed homes, many of them owned by families who travel often or by owners who rent to expatriates. High-end digital and smart locks, home safes and cars in private carparks make up most of the work here.",
 feature="""
<h2>A district of owners who are often elsewhere</h2>
<p>Paterson is small, and its locksmith work follows an unusual pattern. Many of its luxury condos and serviced residences belong to owners who spend part of the year abroad, or who rent their units to professionals on two- or three-year postings. Homes sit empty for weeks, tenants come and go, and the person who set a lock's code is often not the person standing in front of it. That shapes almost every call we get here.</p>

<h2>Between tenancies: a landlord's lock checklist</h2>
<p>When a tenant moves out of a Paterson unit, the lock is easy to forget. It shouldn't be. A departing tenant may have added fingerprints, shared PINs with a helper or driver, or paired the lock to an app on a phone that has now left the country. Before the next tenant moves in:</p>
<ul>
<li><strong>Delete every user code, card and fingerprint</strong>, or factory-reset the lock and set it up again.</li>
<li><strong>Unpair the app</strong> from the old tenant's account. Most smart lock apps let only the admin account do this, which is where many landlords get stuck.</li>
<li><strong>Collect or replace the mechanical keys.</strong> If one is missing, replacing the cylinder costs less than wondering who has it.</li>
<li><strong>Open and reset any safe</strong> left in the unit, so the next occupant doesn't inherit a locked box with no code.</li>
</ul>
<p>If the tenant has already gone and the code went with them, we open the door without damage once you show proof of ownership, then reset or replace the lock. Our <a href="~/guides/landlord-tenant-lock-change/">landlord and tenant lock change guide</a> explains who can authorise what.</p>

<h2>Smart locks, concierges and lift cards</h2>
<p>High-end condos around Paterson Hill and Orchard Boulevard often pair a premium smart lock with a concierge desk and lift access cards. When something fails, it's rarely the lock alone: an app that has logged out, a phone left inside, a lift that won't take you to your floor without your card. We deal with the lock, but the concierge holds the keys to everything else. Let them know a locksmith is expected and that you'll need lift access, and the job usually takes minutes rather than an hour. We open smart and digital locks of every brand, from {P_DIGITAL_OPEN} for an emergency opening.</p>

<h2>Watch, jewellery and document safes</h2>
<p>The safes we're called to in Paterson tend to be small, well built and kept in a walk-in wardrobe or study: watch safes, jewellery safes and document safes. Owners who travel ask for two things most. One is opening a safe whose code nobody remembers after months away. The other is a <strong>combination change</strong>, because someone who knew the old code has left: a household member, a member of staff or a tenant. A combination change is quicker than an opening, and worth doing every time the people around a safe change. See <a href="~/safe-combination-change/">safe combination change</a>.</p>
<p>If a safe's lock has actually failed, most faulty safes need drilling, done precisely so that about 90% of them can be repaired and used again. We explain which situation you're in, and the price, before any work starts. Safe opening starts from {P_SAFE}.</p>

<h2>When you're overseas</h2>
<p>If you own a unit here and you're abroad when something goes wrong, the job can still be done. Someone on site, such as a tenant, a family member or your agent, needs to meet us with ID, and we need your written authorisation and proof that the unit is yours. Send everything on WhatsApp to {PHONE} before we set off, and we confirm the price in writing too. Companies and property managers receive a proper invoice, and we take PayNow.</p>
""",
 estates=["Paterson Road", "Paterson Hill", "Orchard Boulevard", "Grange Road", "Angullia Park", "River Valley"],
 landmarks=["Paterson Hill", "Orchard Boulevard", "Orchard Road", "Grange Road"],
 mrt=["Orchard Boulevard", "Orchard", "Somerset", "Great World"],
 buildings=[
  ("Luxury condominiums", "Premium digital and smart locks, sometimes with app access and a concierge. We work with the management office and check proof of residence before opening."),
  ("Serviced and rented residences", "Landlords and agents call us when a tenant has left without returning the code or keys. We check proof of ownership, open the door and can change the lock the same visit."),
  ("Home safes", "Safes in walk-in wardrobes and studies hold passports, watches and jewellery. Uncle Thomas opens them and can change the combination afterwards."),
 ],
 jobs=["Home safe opening and combination changes", "Smart lock lockouts in luxury condos", "Lock changes for landlords between tenants", "Car lockouts in private carparks"],
 access="Paterson condos usually have a concierge or guardhouse, so tell them a locksmith is coming. For safes, have proof that the safe is yours ready, such as ID with the address.",
 faqs=[
  ("Can you change a safe combination in Paterson?", "Yes. After checking the safe is yours, Uncle Thomas can open it and set a new combination, or replace the safe lock if it's faulty."),
  ("My tenant left and the digital lock code changed. Can you help?", "Yes. Show us proof that you own the unit and we'll open the door without damage, then reset or replace the lock."),
  ("I'm overseas. Can you open my Paterson unit for my agent or tenant?", 'Yes, with your written authorisation and proof that the unit is yours, sent on WhatsApp before we set off. Someone you trust needs to be there with ID.'),
  ('How often should I change my safe combination?', "Whenever someone who knew it moves on: a tenant, a member of staff or anyone else. It's a quick job compared with opening a safe whose code has been lost."),
 ],
 nearby=["cbd-orchard", "newton", "bukit-merah"],
),
dict(
 slug="tanglin", name="Tanglin", region="Central",
 # Long-form rewrite 10 Nov 2026 (no real jobs yet: guidance only, facts from CLAUDE.md and config).
 title='Locksmith Tanglin & Nassim | Safes, Gates and Rekeying 24/7',
 desc='Discreet 24/7 locksmith for Tanglin, Nassim, Cuscaden and Dempsey: home and watch safes, bungalow gates, whole-house rekeying and smart locks. Call 9224 9224.',
 h1='Locksmith in Tanglin, Nassim and Dempsey, 24/7',
 intro="Tanglin is one of Singapore's most exclusive addresses: embassies, good class bungalows and luxury condos, so our calls here are mostly home safes, high-end digital locks and cars.",
 overview="Tanglin stretches from the top of Orchard Road past Tanglin Mall and Dempsey Hill to the Singapore Botanic Gardens. Around Nassim Road, Napier Road and Cuscaden Road you'll find embassies, ambassadors' residences, large landed houses and some of the island's most expensive condominiums. Homes here often have a safe in the master bedroom or study, gated driveways with several locks, and more than one car.",
 feature="""
<h2>Large homes, many keys</h2>
<p>A Tanglin bungalow can have a dozen locks before you count the safes: a driveway gate, a pedestrian gate, a front door, a back door, a service entrance, store rooms and staff quarters. Over the years, those keys spread. Helpers, drivers, gardeners, renovation contractors and previous tenants may all have held one, and some will have been copied. For most of the homes we see around Nassim, Napier and Cuscaden, the security question isn't whether the locks are good. It's who still has a key.</p>

<h2>Rekeying the whole property in one visit</h2>
<p>You don't usually need new locks to solve that. Replacing the cylinders, the part the key goes into, makes every old key useless while keeping the lock bodies, handles and gate hardware you already have. On a large property we work through it methodically:</p>
<ol>
<li><strong>Walk the property with you</strong> and list every entrance, gate and internal lock that matters.</li>
<li><strong>Photograph each lock</strong> so the right cylinders and parts are on hand. Sending these on WhatsApp beforehand saves a second trip.</li>
<li><strong>Agree who gets which keys.</strong> Staff may need the service gate and kitchen door, but not the study or the front door.</li>
<li><strong>Replace and test</strong> each cylinder, then hand over the new keys with a simple record of what opens what.</li>
</ol>
<p>Main door and gate lock replacement starts from {P_REPLACE}, supplied and installed, with our no-expiry warranty. See <a href="~/lock-replacement/">lock replacement</a> and <a href="~/guides/change-locks-new-home/">changing locks in a new home</a>.</p>

<h2>Safes, staff changes and discretion</h2>
<p>Tanglin homes often keep more than one safe: a wall or floor safe in the master bedroom, a watch or jewellery safe in the dressing room, a document safe in the study. Most of our safe calls here come from one of two moments. Either nobody can remember a code, or the household has changed and a member of staff who knew the code has moved on. In the second case the safe still opens, and the fix is a <a href="~/safe-combination-change/">combination change</a> that only the family knows.</p>
<p>Uncle Thomas trained as a safesmith in the United States and has opened safes for banks, hotels and offices, as well as on ships. That experience matters with expensive safes, which often have relockers that fire if a safe is attacked the wrong way. When a code is lost but the lock works, there's often a way in that leaves the safe as it was. When the lock has failed, drilling is usually the answer, at a precise point, and about 90% of drilled safes can be repaired. He works quietly, can come alone, and never discusses clients or what was inside. Safe opening starts from {P_SAFE}.</p>

<h2>Gates and driveways</h2>
<p>Heavy driveway gates take daily wear, and rain and heat get into every lock exposed to them. Watch for a key that turns only partway, a bolt that needs the gate lifted before it slides, or rust staining around the keyhole. Replace a failing gate lock before it seizes with the car on the wrong side. We open seized gate locks and fit replacements made for outdoor use.</p>

<h2>Embassies, guardhouses and access</h2>
<p>Tanglin is home to many embassies and diplomatic residences, and plenty of private homes have their own guards or gate procedures. If security needs to clear contractors, register us before you call, as Uncle Thomas Locksmith, {PHONE}. We still ask for ID and proof that the property is yours, or written authorisation from whoever is responsible for it. That check protects you as much as anyone.</p>
""",
 estates=["Nassim", "Cuscaden", "Napier Road", "Tanglin Road", "Dempsey", "Grange Road"],
 landmarks=["Singapore Botanic Gardens", "Dempsey Hill", "Tanglin Mall", "Nassim Road"],
 mrt=["Botanic Gardens", "Napier", "Orchard Boulevard", "Orchard"],
 buildings=[
  ("Landed homes and bungalows", "Main gates, side gates, front doors and safes, each with its own lock. We confirm ownership before opening anything and can rekey the whole property by replacing the cylinders."),
  ("Luxury condominiums", "Premium digital and smart locks with app access, often managed through a concierge. We coordinate with management and check proof of residence."),
  ("Home safes and watch safes", "Safes holding passports, jewellery, watches and documents. Uncle Thomas is a safe specialist: he opens them and can change the combination afterwards."),
 ],
 jobs=["Home safe and watch safe opening", "Combination changes when household staff change", "Car lockouts in private driveways and condo carparks", "Gate and main door lock upgrades"],
 access="Many Tanglin homes are gated, so tell us the gate or guardhouse procedure. For embassy-area addresses, let security know a locksmith is expected.",
 faqs=[
  ("Can you open a home safe in Tanglin discreetly?", "Yes. Uncle Thomas works quietly and can come alone if you prefer. If the code is lost but the lock works, there is often a way in without damage, and he can set a new combination on the spot. We check the safe is yours first."),
  ("Should I change my safe combination when my helper or staff leave?", "It's a good idea. Anyone who has seen or been told the code can still open the safe. We change combinations on most safe types in one visit."),
  ('Can you rekey every lock on a Tanglin bungalow without changing the hardware?', "Usually, yes. We replace the cylinders so old keys stop working, keep your existing lock bodies and handles where they're in good shape, and give you a record of which key opens what."),
 ],
 nearby=["cbd-orchard", "paterson", "bukit-timah", "holland-village"],
),
dict(
 slug="bukit-timah", name="Bukit Timah", region="Central",
 # Long-form rewrite 10 Nov 2026 (no real jobs yet: guidance only, facts from CLAUDE.md and config).
 title='Locksmith Bukit Timah | Gates, Home Safes and Cars, 24/7',
 desc='24/7 locksmith in Bukit Timah, Sixth Avenue and King Albert Park: driveway gates, lock changes, inherited safes, school-run car lockouts. Call 9224 9224.',
 h1='Locksmith in Bukit Timah, 24/7: Gates, Safes and Cars',
 intro="Bukit Timah is landed-home country, with bungalows, semi-detached houses and quiet condos, so most of our work here is gates, home safes and cars.",
 overview="Bukit Timah runs along Bukit Timah Road and Dunearn Road from the Botanic Gardens out towards Beauty World and the nature reserve. It's home to many of Singapore's good class bungalows and landed estates around Sixth Avenue, King Albert Park, Coronation Road and Hillcrest, alongside low-rise condos and top schools. Large homes mean more locks: driveway gates, side gates, front doors, store rooms and safes.",
 feature="""
<h2>Bukit Timah's most common calls</h2>
<p>Behind the schools and shophouses of Bukit Timah Road lie streets of bungalows, semi-detached houses and low-rise condos, from Cluny and Coronation Road out past Sixth Avenue and King Albert Park to Hillcrest and Beauty World. The calls we get from them fall into clear patterns: families who have just moved into a landed home and want control of the keys, gates that fail at the worst possible moment, and safes nobody can open, often ones that came with the house or belonged to a parent who has passed away.</p>

<h2>Just moved into a landed home? Start with the locks</h2>
<p>When you buy a landed house, you inherit every key the previous owners ever handed out: to helpers, contractors, agents, the neighbour who watered the plants. There is no way to know where they all are. The fix is simple and worth doing in your first week: replace the cylinders on every external door and gate, so only your keys work. Bring a list of the entrances, or send photos on WhatsApp, and we confirm parts and price in advance. If the house came with a digital lock, delete every old user and fingerprint, or reset it to factory settings. Our <a href="~/guides/change-locks-new-home/">guide to changing locks in a new home</a> covers the details.</p>

<h2>When the driveway gate won't open</h2>
<p>A driveway gate gets used several times a day, and its lock lives outdoors in the rain and heat. The failure is almost always gradual: a key that needs wiggling, a bolt that needs the gate pushed or lifted, a lock that only works if you're gentle with it. Then one morning, usually a school day, it stops. If that happens, don't force the key. A snapped key turns a quick opening into an extraction job. Call us, and we open the gate and, if the lock body is worn, fit a sturdier replacement in the same visit, from {P_REPLACE}. If a key has already snapped, see <a href="~/broken-key-extraction/">broken key extraction</a>.</p>

<h2>The safe nobody can open</h2>
<p>Older Bukit Timah homes often hold older safes: a heavy dial safe built into a wardrobe, a cabinet safe in a study, sometimes one the previous owners left behind with no code and no paperwork. Others belonged to a parent who has died, with documents or valuables the family needs to settle the estate. These are delicate situations, so we go carefully. We need to see that the property is yours or, for a late family member's safe, documents that show you're entitled to deal with the estate. Our guide to <a href="~/guides/opening-a-deceased-persons-safe/">opening a late family member's safe</a> explains what Singapore's probate process expects.</p>
<p>On the safe itself: an old dial lock in working order can sometimes be opened by manipulation, by feel and sound, without leaving a mark. Uncle Thomas is trained in that technique for high-security combination locks, and a job can take anywhere from 5 minutes to 5 hours. If the lock has failed, drilling is usually needed, and about 90% of drilled safes can be repaired and used again. Safe opening starts from {P_SAFE}.</p>

<h2>School runs and car lockouts</h2>
<p>With so many schools along Bukit Timah and Dunearn Road, drop-off and pick-up are when car lockouts happen: keys left inside while a child is helped out, a smart key dropped into a bag that ends up in the boot. Tell us the school or carpark and the car model. We open cars of all major brands without damage, from {P_CAR}, after checking the log card. For families sharing one remote key between two drivers, a cloned spare fob is the lasting fix; see <a href="~/car-key-duplicate/">spare car key fob</a>.</p>
""",
 estates=["Sixth Avenue", "King Albert Park", "Coronation Road", "Hillcrest", "Swiss Club Road", "Cluny"],
 landmarks=["Bukit Timah Nature Reserve", "Beauty World", "Cluny Court", "Botanic Gardens"],
 mrt=["Botanic Gardens", "Tan Kah Kee", "Sixth Avenue", "King Albert Park", "Beauty World"],
 buildings=[
  ("Bungalows and landed homes", "Several locks per property and heavy driveway gates that take a lot of wear. We open, replace or rekey them so one set of keys works the way you want."),
  ("Home safes", "Bedroom, study and wardrobe safes are common here. Uncle Thomas opens every type of safe, and when drilling is needed, about 90% of drilled safes can be repaired and used again."),
  ("Family cars", "Car lockouts in driveways, school carparks and condo basements. We open cars without damage after checking the log card."),
 ],
 jobs=["Home safe opening and combination changes", "Driveway and side gate lock replacement", "Car lockouts at home and at school pick-up", "Rekeying a whole house after moving in"],
 access="Bukit Timah's landed streets can be hard to find at night, so a pinned location on WhatsApp helps. Tell us which gate to come to.",
 faqs=[
  ("We just bought a landed home in Bukit Timah. Should we change the locks?", "Yes. You don't know who still has keys from the previous owner, contractors or agents. We replace the cylinders on every gate and door so only your keys work."),
  ("Can you open an old safe left by the previous owner?", "Usually, yes. Show us that you own the property and the safe came with it, and Uncle Thomas will open it. If its lock still works it may open without damage; if the lock has failed, it will usually need drilling."),
  ("Can you open my late father's safe in Bukit Timah?", "Yes, once you show you're entitled to deal with his estate, for example a Grant of Probate or Letters of Administration, or with the executor's agreement. Our guide to opening a late family member's safe explains the documents in plain English."),
 ],
 nearby=["tanglin", "holland-village", "bukit-panjang"],
),
dict(
 slug="holland-village", name="Holland Village", region="Central",
 # Long-form rewrite 10 Nov 2026 (no real jobs yet: guidance only, facts from CLAUDE.md and config).
 title='Locksmith Holland Village | Safes, Lock Changes and Shutters',
 desc='24/7 locksmith in Holland Village, Chip Bee Gardens and Leedon: lock changes between tenancies, safes left behind, restaurant shutters and cars. Call 9224 9224.',
 h1='Locksmith in Holland Village and Chip Bee Gardens, 24/7',
 intro="Holland Village mixes landed estates, expat condos and its famous dining strip, so our calls are home safes, digital locks, cars and the odd shop shutter.",
 overview="Holland Village sits around Lorong Liput and Jalan Merah Saga, with the landed estates of Chip Bee Gardens, Holland Grove and Holland Hill around it and condos along Holland Road and Farrer Road. Many homes are rented to expatriate families, so lock changes between tenancies and safes left by previous occupants are common. The dining strip adds shophouse shutters and back doors.",
 feature="""
<h2>A neighbourhood that moves in and out</h2>
<p>Holland Village has long been a favourite with families on overseas postings, and that gives our work here a rhythm of its own. Every few months a household arrives, another leaves, and the locks, codes and safes pass from one set of hands to the next. Most Holland Village calls happen at those handover points, plus late-night lockouts on the dining strip and the occasional car locked near One Holland Village.</p>

<h2>Moving in: what to do with the locks</h2>
<p>New tenants often assume the landlord has changed the locks. Many haven't, so ask. If they haven't, there are two options: ask the landlord to arrange a cylinder change, or agree to do it yourself and hand over the new keys when you leave. Either way, get it in writing, because changing locks on a rented home normally needs the landlord's agreement. For a digital lock, have every old PIN, card and fingerprint removed and set your own. See <a href="~/guides/landlord-tenant-lock-change/">who can change the locks in a rental</a>.</p>

<h2>Moving out: open every safe, hand over every code</h2>
<p>The most avoidable call we get in Holland Village is the safe nobody can open on moving day. The person who set the code has packed, the movers are booked, and a wardrobe safe still holds something important. Before a relocation:</p>
<ul>
<li>Open every safe in the home, empty it, and leave it open, or reset it to the factory code if the landlord prefers.</li>
<li>Hand the landlord or agent every key, every card and the digital lock's admin code.</li>
<li>Mention any lock that has become stiff or unreliable, so it's fixed before the next family arrives.</li>
</ul>
<p>Already stuck? With the landlord's or agent's written authorisation, we open a safe or door left locked by a previous occupant. If the code has just been forgotten, check the paperwork for an override key first; our <a href="~/guides/lost-safe-key/">lost safe key</a> and <a href="~/guides/forgot-safe-combination/">forgotten combination</a> guides explain what to look for. If the lock has failed, most faulty safes need drilling, and about 90% of those can be repaired and reused. Safe opening starts from {P_SAFE}.</p>

<h2>Older landed homes in Chip Bee Gardens and Holland Grove</h2>
<p>Chip Bee Gardens was built as housing for British military families, and many of its houses, like others around Holland Grove and Holland Hill, have been renovated more than once. That leaves a patchwork of hardware: an original timber door with a newer deadbolt, a modern digital lock on an old frame, a gate lock replaced twice. With mixed hardware, the first job is to look properly, so we bring the right parts and don't damage a door that may be hard to match. Photos on WhatsApp before we come help a lot.</p>

<h2>Restaurants and shops on the strip</h2>
<p>For restaurants and shops along Lorong Liput, Lorong Mambong and Jalan Merah Saga, the late shift is when locks fail: a shutter padlock that won't close at 1am, a back door that jams after the last delivery. We work 24/7, cut seized padlocks and fit new ones, and open roller shutter locks. We need proof that you own or run the business, and companies receive an invoice. See <a href="~/roller-shutter-lock/">roller shutter locks</a> and <a href="~/padlock-cutting/">padlock cutting</a>.</p>
""",
 estates=["Chip Bee Gardens", "Holland Grove", "Holland Hill", "Leedon Park", "Farrer Road", "Jalan Merah Saga"],
 landmarks=["Holland Village", "Holland Road", "Farrer Road", "Lorong Liput"],
 mrt=["Holland Village", "Farrer Road", "Buona Vista"],
 buildings=[
  ("Landed and semi-detached homes", "Gates, front doors and safes. We open them without damage where possible and confirm ownership or tenancy first."),
  ("Expat condos and rentals", "Digital locks and deadbolts that need resetting or replacing between tenants. Landlords and agents can authorise the job in writing."),
  ("Restaurants and shops", "Roller shutter locks, padlocks and back-lane doors, often before opening or after closing."),
 ],
 jobs=["Home safe opening for families moving in or out", "Lock changes between tenancies", "Car lockouts around Holland Village", "Shop shutter and padlock jobs"],
 access="Parking near the dining strip is tight in the evenings, so tell us the nearest carpark. For condos, let the guardhouse know we're coming.",
 faqs=[
  ("Can you help a family relocating out of Holland Village?", "Yes. We open safes whose codes have been forgotten, and change or reset locks before you hand the home back, with the landlord's agreement."),
  ("Do you open shop shutters on the Holland Village strip?", "Yes, 24/7. We'll need proof that you own or run the business before opening."),
  ('Can a tenant in Holland Village ask you to change the locks?', "A tenant can call us for a lockout with proof of residence. Changing the lock on a rented home normally needs the landlord's agreement, so check your tenancy agreement first."),
  ('The previous tenant left a locked safe. Can you open it?', "Yes, with written authorisation from the landlord or agent. Send a photo of the safe and we'll confirm the price first."),
 ],
 nearby=["tanglin", "bukit-timah", "clementi"],
),
dict(
 slug="river-valley", name="River Valley", region="Central",
 # Long-form rewrite 10 Nov 2026 (no real jobs yet: guidance only, facts from CLAUDE.md and config).
 title='Locksmith River Valley & Robertson Quay | Smart Locks, Safes',
 desc='24/7 locksmith in River Valley, Robertson Quay and Killiney: smart lock and app failures, serviced apartment doors and safes, car lockouts. Call 9224 9224.',
 h1='Locksmith in River Valley and Robertson Quay, 24/7',
 intro="River Valley and Robertson Quay are packed with luxury condos and serviced apartments, so most calls here are smart lock lockouts, home safes and cars in basement carparks.",
 overview="River Valley runs between Orchard and the Singapore River, taking in Robertson Quay, Mohamed Sultan, Killiney, Kim Yam and Institution Hill. Almost every home is a condo or serviced apartment, many with premium digital locks, and residents are often busy professionals who travel. It's a short drive from Orchard Road, so we reach it quickly at any hour.",
 feature="""
<h2>Smart homes, short stays and late nights</h2>
<p>River Valley packs more serviced apartments and app-controlled smart locks into a few square kilometres than almost anywhere else in Singapore. Add Robertson Quay's restaurants and bars, which keep the riverside busy past midnight, and you get our River Valley pattern: smart locks that stop cooperating, serviced apartment doors and in-room safes, and residents coming home late to a door that won't open.</p>

<h2>Five ways a smart lock locks you out</h2>
<p>When a smart lock fails, knowing why helps you fix it yourself, or tells us what to bring.</p>
<ol>
<li><strong>Flat batteries.</strong> The most common cause by far. Most locks warn you for weeks first, and many have an emergency power point under the keypad that a power bank can use.</li>
<li><strong>The app has logged you out</strong>, or a phone update has broken the pairing. Try the keypad PIN or a card instead.</li>
<li><strong>Your phone is inside.</strong> If the app is your only way in, you're stuck. Always set up a PIN or card as a second method.</li>
<li><strong>The hub has dropped offline.</strong> Remote unlocking needs the lock's Wi-Fi bridge or hub to be online, and a power cut or new router can knock it off.</li>
<li><strong>Privacy or lockdown mode.</strong> Some locks block every outside method once someone inside has locked up for the night.</li>
</ol>
<p>Still locked out? WhatsApp us the brand and model. We open smart and digital locks of every brand, usually without damage, from {P_DIGITAL_OPEN}. See <a href="~/digital-lock-opening/">digital lock opening</a> and our guide to a <a href="~/guides/forgot-digital-lock-pin/">forgotten digital lock PIN</a>.</p>

<h2>Serviced apartments: who can let us in</h2>
<p>In a serviced apartment, the operator controls the door, not the guest. If you're locked out, call the front desk or duty manager first: a master card may solve it in minutes. If the lock itself has failed, or the operator needs a locksmith, they authorise the job and we confirm your identity before opening anything. The same goes for in-room safes. Operators and property managers receive a proper invoice. See <a href="~/hotel-safe-opening/">hotel and serviced apartment safes</a>.</p>

<h2>Home safes after a long trip</h2>
<p>Owners here often travel for work, and safes go untouched for weeks. Electronic keypad safes then fail in a predictable way: the batteries die, or leak and corrode the contacts, and the keypad goes dark. Many have a backup key or an external battery point; our guide to a <a href="~/guides/safe-box-battery-dead/">safe with a dead battery</a> shows where to look. If the safe still won't open, or its lock has failed, Uncle Thomas opens every type of safe. Most faulty ones need drilling, and about 90% of drilled safes can be repaired afterwards. Safe opening starts from {P_SAFE}.</p>

<h2>Late nights and tight basements</h2>
<p>River Valley sits between Orchard and the river, a short drive from our usual base, so we usually reach Robertson Quay, Mohamed Sultan or Killiney within {ARRIVAL}, whatever the hour. Basements here are tight, so for a car lockout send the carpark level and lot, and let the concierge know we're coming. Nights, weekends and public holidays start from {P_AFTERHOURS}; car lockouts from {P_CAR}.</p>
""",
 estates=["Robertson Quay", "Mohamed Sultan", "Killiney", "Kim Yam", "Institution Hill", "Great World"],
 landmarks=["Robertson Quay", "Great World", "Fort Canning Park", "Valley Point"],
 mrt=["Great World", "Havelock", "Fort Canning", "Somerset"],
 buildings=[
  ("Luxury condos", "Premium digital and smart locks, sometimes linked to an app. We open them damage-free and check proof of residence with the concierge."),
  ("Serviced apartments", "Doors and in-room safes. The operator authorises the job and we confirm the guest's identity."),
  ("Basement carparks", "Car lockouts in tight condo basements. Tell us the level and lot number."),
 ],
 jobs=["Smart lock lockouts after a flat battery or app failure", "Home and in-room safe opening", "Car lockouts in condo carparks", "Lock resets when owners change tenants"],
 access="Most River Valley condos have a guardhouse or concierge, so let them know a locksmith is coming. At night, we usually arrive within 25–30 minutes.",
 faqs=[
  ("My smart lock app stopped working and my phone is inside. Can you help?", "Yes. We open smart and digital locks without damage after checking you live there, then help you get the lock working again."),
  ("Can you open the safe in my serviced apartment?", "Yes, with the operator's authorisation. We open it without damaging the safe or the furniture around it."),
  ('Can you open a dead keypad safe in my River Valley condo?', "Usually. First look for a backup key or an external battery point. If it still won't open, Uncle Thomas opens every type of safe, and we confirm the price from a photo first."),
  ('Who authorises a locksmith in a serviced apartment?', 'The operator. Call the front desk first. If they need a locksmith, they authorise us, and we confirm your identity before opening.'),
 ],
 nearby=["cbd-orchard", "paterson", "bukit-merah"],
),
dict(
 slug="sentosa-cove", name="Sentosa Cove", region="Central",
 # Long-form rewrite 10 Nov 2026 (no real jobs yet: guidance only, facts from CLAUDE.md and config).
 title='Locksmith Sentosa Cove | Home and Boat Safes, Gates, Locks',
 desc='24/7 locksmith for Sentosa Cove bungalows, condos and the marina: home and boat safes, salt-corroded gate locks, smart locks after months away. Call 9224 9224.',
 h1='Locksmith in Sentosa Cove, 24/7: Homes, Safes and Boats',
 intro="Sentosa Cove is Singapore's only island waterfront address: bungalows, condos and yachts, so our calls here are home safes, high-end locks, cars and boats.",
 overview="Sentosa Cove sits on the eastern end of Sentosa, with waterfront bungalows on Ocean Drive, Cove Drive, Paradise Island and Treasure Island, condominiums around the village, and berths at the marina. Owners often spend time abroad, so safes go unopened for months and digital lock batteries quietly run down. Uncle Thomas has opened safes on ships and cruise liners, which helps with safes on boats as well as at home.",
 feature="""
<h2>Locks by the sea</h2>
<p>Sentosa Cove is unlike any other address in Singapore. Bungalows line the waterways of Ocean Drive, Cove Drive and the private islands, condos cluster around the village, and boats sit in the marina a few steps from the front door. It's beautiful, and it's hard on locks. Salt air, humidity and long stretches with nobody home cause most of the problems we see here.</p>

<h2>What salt air does to a lock</h2>
<p>Salt settles inside keyholes and on a lock's moving parts, draws in moisture and starts corrosion you can't see until the key begins to grit or stick. Gate locks, padlocks and anything else facing the water go first. Digital lock keypads and safe keypads suffer too, as contacts corrode and buttons stop responding. Signs to watch for:</p>
<ul>
<li>A key that feels rough, or needs a push or a jiggle to turn.</li>
<li>Brown or white staining around the keyhole or on a padlock shackle.</li>
<li>A digital keypad that misses presses, or a safe keypad that beeps but won't open.</li>
</ul>
<p>Caught at that stage, a replacement is a quick, planned job. Left alone, the lock seizes, usually with you on the wrong side. When we replace outdoor locks here, we recommend stainless steel or marine-grade hardware, which lasts far longer by the sea than standard locks. See <a href="~/lock-replacement/">lock replacement</a>.</p>

<h2>Coming home after months away</h2>
<p>Many Sentosa Cove owners split the year between Singapore and elsewhere. While a house or apartment sits empty, digital lock batteries run down, safe batteries leak, and a code set a year ago is hard to recall. Before a long trip, replace the batteries in every digital lock and safe, test the backup keys, and leave a spare key with someone you trust in Singapore. If you've already come home to a dead lock, we open it, usually without damage, and replace the batteries. If a property manager needs to let us in while you're abroad, send your written authorisation and proof of ownership on WhatsApp first.</p>

<h2>Safes at home and on board</h2>
<p>Uncle Thomas trained as a safesmith in the United States and has opened safes on ships and cruise liners, so a safe on a yacht is familiar ground. Marine safes bring their own complications: tight cabinetry, salt-damaged keypads and owners who may be abroad. We work carefully around the joinery, and we need proof that the boat and safe are yours, or the owner's written authorisation. At home or afloat, the same honest rule applies. If a code is lost but the lock works, there's often a way in without damage; if the lock has failed, the safe usually has to be drilled, and about 90% of drilled safes can be repaired. Safe opening starts from {P_SAFE}.</p>

<h2>Getting to you on the island</h2>
<p>We reach Sentosa Cove by road over the Sentosa Gateway. Estate security adds a step that doesn't exist elsewhere, so let the guardhouse or your condo's security know a locksmith is coming, and send a pinned location, especially for the island bungalows, which can be hard to find at night. For a boat, tell us the marina and berth, and let the marina office know. We work 24/7; nights, weekends and public holidays start from {P_AFTERHOURS}.</p>
""",
 estates=["Ocean Drive", "Cove Drive", "Paradise Island", "Treasure Island", "Coral Island", "Sentosa Cove Village"],
 landmarks=["Sentosa Cove Village", "ONE°15 Marina", "Ocean Drive", "Quayside Isle"],
 mrt=["HarbourFront (then by road to Sentosa)"],
 buildings=[
  ("Waterfront bungalows", "Gates, front doors, store rooms and safes. Sea air corrodes outdoor locks quickly, so we often replace gate locks with ones better suited to the coast."),
  ("Condominiums", "Premium digital locks, often with long gaps between visits. We open them and replace batteries or the lock if needed."),
  ("Yachts and boats", "Safes and locks on board. Uncle Thomas has opened safes on ships, so marine safes are familiar work."),
 ],
 jobs=["Home safe opening after a long trip abroad", "Safes on yachts and boats", "Gate lock replacement after sea-air corrosion", "Car lockouts at home or the marina"],
 access="Sentosa Cove is reached by road over the Sentosa Gateway. Tell the guardhouse or estate security we're coming, and send a pinned location for bungalows.",
 faqs=[
  ("Can you open a safe on a yacht at Sentosa Cove?", "Yes. Uncle Thomas has opened safes on ships and cruise liners. We need proof that the boat and safe are yours, or the owner's written authorisation."),
  ("Our home has been empty for months and the digital lock is dead. Can you help?", "Yes. We open it without damage, then replace the batteries or the lock. Before your next trip, change the batteries and keep the backup key with someone you trust."),
  ('My gate lock at Sentosa Cove has rusted shut. Can you replace it?', 'Yes. We open it, then fit a stainless steel or marine-grade lock that copes better with salt air.'),
 ],
 nearby=["bukit-merah", "cbd-orchard"],
),
dict(slug="queenstown", name="Queenstown", region="Central",
 intro="Queenstown was Singapore's first satellite estate, so it mixes some of the oldest HDB blocks on the island with tall new ones at Dawson — and business parks like one-north and Science Park.",
 overview="Queenstown covers Commonwealth, Dawson, Tanglin Halt, Mei Ling and Stirling, stretching out to Alexandra and the one-north business district. Older blocks here have seen several generations of locks, while redeveloped areas such as Dawson have newer flats where digital locks are common. Offices, labs and start-ups around one-north and Science Park make up a good share of our commercial work in the area.",
 estates=["Commonwealth", "Dawson", "Tanglin Halt", "Mei Ling", "Stirling", "Alexandra", "one-north"],
 landmarks=["Queensway Shopping Centre", "Alexandra Retail Centre", "one-north", "Singapore Science Park", "Queenstown Library"],
 mrt=["Queenstown", "Commonwealth", "Buona Vista", "one-north", "Kent Ridge"],
 buildings=[
  ("Older HDB blocks", "Original-style main doors and gates where locks are often worn after decades of use — a common cause of keys snapping."),
  ("Dawson and newer flats", "Digital locks on main doors and gates; flat batteries and forgotten PINs are frequent call-outs."),
  ("Business parks", "Office and lab doors, cabinets and document safes around one-north and Science Park."),
 ],
 jobs=["Snapped keys in old HDB locks", "Digital lock lockouts in Dawson", "Office and lab lockouts at one-north", "Rental room lock changes for tenants"],
 access="Queenstown's older estates have many low blocks spread out — sending your block number and street name helps us find you fastest.",
 faqs=[
  ("Do you serve one-north and Science Park offices?", "Yes. We handle office lockouts, lock changes and safes, and can come outside working hours."),
  ("Can you replace a worn lock in an old Queenstown flat?", "Yes. We replace main door and gate locks on the spot, with our no-expiry warranty."),
 ],
 nearby=["bukit-merah", "clementi"]),

dict(slug="bukit-merah", name="Bukit Merah & Tiong Bahru", region="Central",
 intro="From Tiong Bahru's heritage flats to Redhill, Telok Blangah and HarbourFront, Bukit Merah has some of Singapore's most varied housing — and the cruise terminal on its doorstep.",
 overview="Bukit Merah stretches from the heritage walk-up flats of Tiong Bahru through Redhill, Henderson and Bukit Merah Central down to Telok Blangah and HarbourFront. It mixes old and new HDB blocks, private condos, light industrial buildings around Bukit Merah Central and Alexandra, and the shops and offices around VivoCity. With the Singapore Cruise Centre at HarbourFront nearby, ship and vessel safes are familiar ground for Uncle Thomas, who has opened safes on board ships and cruise liners.",
 estates=["Tiong Bahru", "Redhill", "Henderson", "Bukit Merah Central", "Telok Blangah", "HarbourFront"],
 landmarks=["Tiong Bahru Market", "VivoCity", "HarbourFront Centre", "Mount Faber", "Henderson Waves"],
 mrt=["Tiong Bahru", "Redhill", "Telok Blangah", "HarbourFront", "Outram Park"],
 buildings=[
  ("Tiong Bahru walk-ups", "Older pre-war and post-war flats often have timber doors with traditional locks, and some owners have added digital locks."),
  ("HDB estates", "A mix of mature and newer blocks around Redhill, Henderson and Telok Blangah."),
  ("Industrial and harbour", "Workshops, warehouses and offices — plus vessel and ship safes."),
 ],
 jobs=["Old timber door locks in Tiong Bahru", "HDB lockouts around Redhill and Henderson", "Industrial unit lock changes", "Ship and vessel safe opening"],
 access="Tiong Bahru's walk-up flats have shared staircases — tell us the block and staircase. For HarbourFront offices, please arrange building access.",
 faqs=[
  ("Do you open safes on ships at HarbourFront?", "Yes. Uncle Thomas has opened safes on board ships and cruise liners. We'll need authorisation from the vessel's owner or operator."),
  ("Can you work on old Tiong Bahru doors without damaging them?", "We use damage-free methods wherever possible, which matters for older timber doors."),
 ],
 nearby=["queenstown", "cbd-orchard"]),

dict(slug="kallang-whampoa", name="Kallang & Whampoa", region="Central",
 intro="Kallang and Whampoa mix mature HDB estates, light industrial buildings and the busy Sports Hub area — so we're called for home lockouts and business locks in equal measure.",
 overview="This part of central Singapore takes in Whampoa, Boon Keng, Bendemeer, Kallang Bahru and Geylang Bahru, down to the Kallang Basin and the Sports Hub. Mature HDB blocks sit next to industrial buildings along Kallang Bahru and Kallang Way, where workshops and small factories need reliable locks and fast help when something fails.",
 estates=["Whampoa", "Boon Keng", "Bendemeer", "Kallang Bahru", "Geylang Bahru", "Kallang Basin"],
 landmarks=["Singapore Sports Hub", "Kallang Wave Mall", "Whampoa Market", "Kallang Riverside Park"],
 mrt=["Boon Keng", "Bendemeer", "Geylang Bahru", "Kallang", "Stadium", "Lavender"],
 buildings=[
  ("Mature HDB estates", "Older main door locks and gate locks around Whampoa and Boon Keng."),
  ("Industrial buildings", "Factory units, workshops and warehouses along Kallang Bahru and Kallang Way — shutters, padlocks and office doors."),
  ("Condos near the river", "Digital locks and deadbolts in newer condos around Kallang and Bendemeer."),
 ],
 jobs=["Factory and workshop lockouts", "HDB gate locks in Whampoa", "Digital lock lockouts in riverside condos", "Lock changes when staff leave"],
 access="Industrial buildings often have several entrances and loading bays — tell us the unit number and which side to come to.",
 faqs=[
  ("Can you open our factory unit in Kallang Bahru?", "Yes. We handle shutters, padlocks and office doors in industrial buildings, 24/7."),
  ("Do you cover Whampoa and Boon Keng?", "Yes, along with Bendemeer, Geylang Bahru and the rest of Kallang."),
 ],
 nearby=["geylang", "novena"]),

dict(slug="geylang", name="Geylang & Paya Lebar", region="Central",
 intro="Geylang and Paya Lebar are a mix of shophouses, walk-up apartments, HDB estates and the new Paya Lebar office district — busy day and night, and so are our call-outs here.",
 overview="Along Geylang Road and Sims Avenue, shophouses hold restaurants, shops and small businesses, often with walk-up apartments above. Around Aljunied, Eunos and MacPherson are HDB estates, while Paya Lebar Quarter and the area around Paya Lebar MRT have become a commercial hub with offices and retail. Geylang Serai, with its market and festive bazaars, is a landmark for the whole east.",
 estates=["Geylang Road", "Sims Avenue", "Aljunied", "Eunos", "MacPherson", "Paya Lebar", "Geylang Serai"],
 landmarks=["Paya Lebar Quarter", "Geylang Serai Market", "SingPost Centre", "Wisma Geylang Serai"],
 mrt=["Paya Lebar", "Aljunied", "Eunos", "Dakota", "MacPherson", "Mattar"],
 buildings=[
  ("Shophouses", "Front shutters, collapsible gates, back doors and upstairs apartment doors — older locks and padlocks are common."),
  ("Walk-up apartments", "Older timber doors and cylinder locks on shared staircases."),
  ("Offices at Paya Lebar", "Office suites, cabinets and safes."),
 ],
 jobs=["Shophouse shutter lockouts", "Walk-up apartment door lockouts", "HDB lockouts in Aljunied and Eunos", "Office lock changes at Paya Lebar"],
 access="Geylang's lorongs are numbered — tell us the lorong and the nearest cross street to save time.",
 faqs=[
  ("Do you open shophouse shutters in Geylang?", "Yes. We open locked shutters and gates and replace worn padlocks and locks."),
  ("Do you serve the Paya Lebar offices?", "Yes, including after-hours lockouts and lock changes."),
 ],
 nearby=["kallang-whampoa", "marine-parade"]),

dict(slug="marine-parade", name="Marine Parade & Katong", region="Central",
 intro="Marine Parade and Katong combine the classic HDB estate on reclaimed land, Peranakan shophouses in Katong and Joo Chiat, and condos stretching along East Coast Park.",
 overview="Marine Parade's HDB estate was built on reclaimed land in the 1970s, and many flats still have older main doors and gates. Inland, Katong and Joo Chiat are known for colourful shophouses and terrace houses, while Amber Road, Meyer Road and Marine Parade Road are lined with condominiums. The Thomson-East Coast Line has made the area easier to reach than ever.",
 estates=["Marine Parade", "Katong", "Joo Chiat", "Amber Road", "Meyer Road", "Tanjong Katong", "Mountbatten"],
 landmarks=["Parkway Parade", "East Coast Park", "i12 Katong", "Joo Chiat Road"],
 mrt=["Marine Parade", "Marine Terrace", "Katong Park", "Tanjong Katong", "Dakota", "Mountbatten"],
 buildings=[
  ("1970s HDB blocks", "Older timber main doors and gates where locks get stiff with sea air and age."),
  ("Shophouses and terraces", "Traditional timber doors and gates in Katong and Joo Chiat — we use damage-free methods to protect heritage doors."),
  ("Seafront condos", "Digital locks, deadbolts and guarded access along Amber Road and East Coast."),
 ],
 jobs=["Stiff or rusted locks in older Marine Parade flats", "Condo digital lock lockouts", "Terrace house gate locks", "Shop lockouts in Katong"],
 access="Condos along the coast usually need the guardhouse to be informed. For Katong terraces, tell us whether you're locked out at the gate or the front door.",
 faqs=[
  ("Does sea air affect locks in Marine Parade?", "It can. Salty, humid air speeds up rust in older locks and gates — a stiff lock is worth replacing before it fails."),
  ("Do you work on heritage shophouse doors in Katong?", "Yes, and we use damage-free methods wherever possible to protect old timber doors."),
 ],
 nearby=["geylang", "bedok"]),

# ======================= EAST =======================
dict(slug="tampines", name="Tampines", region="East",
 intro="Tampines is one of Singapore's biggest towns — from mature estates around Tampines Central to brand-new BTO flats in Tampines North — so we see the full range of locks here.",
 overview="Tampines is a regional centre with its own malls, offices and community hub, surrounded by large HDB estates in Tampines North, East, West and Central, plus condos near Simei. Newer BTO projects in Tampines North mean a lot of digital locks, while older blocks still have traditional mortise locks and gate hook bolts. Offices around the regional centre and Changi Business Park add commercial work.",
 estates=["Tampines Central", "Tampines North", "Tampines East", "Tampines West", "Simei"],
 landmarks=["Our Tampines Hub", "Tampines Mall", "Century Square", "Tampines Eco Green"],
 mrt=["Tampines", "Tampines East", "Tampines West", "Simei", "Upper Changi"],
 buildings=[
  ("New BTO estates", "Tampines North flats where many owners fit digital locks soon after key collection."),
  ("Mature HDB blocks", "Original mortise locks and gate hook bolts that wear over time."),
  ("Offices and business parks", "Office doors, cabinets and safes around the regional centre."),
 ],
 jobs=["HDB main door and gate lockouts", "Digital lock installation in new Tampines North flats", "Office lockouts in the regional centre", "Car lockouts at mall carparks"],
 access="Tampines has many similar-looking blocks — the street number (e.g. Tampines Street 81) plus block number gets us there fastest.",
 faqs=[
  ("Can you install a digital lock in my new Tampines North BTO?", "Yes. We'll check your door and recommend a lock that fits, then install it with our no-expiry warranty."),
  ("Do you do car lockouts at Tampines malls?", "Yes. Tell us the carpark and level, and your car model."),
 ],
 nearby=["pasir-ris", "bedok"]),

dict(slug="bedok", name="Bedok", region="East",
 intro="Bedok has a bit of everything — mature HDB estates, private condos, landed homes around Siglap, and industrial units in Kaki Bukit — so our work here covers homes, cars and businesses.",
 overview="Bedok is one of the east's most established towns, with HDB estates in Bedok North, Bedok South, Bedok Reservoir and Chai Chee. Landed homes in Siglap, Frankel and Opera Estate bring gates and multi-lock doors, while Kaki Bukit's industrial estate has warehouses and factories. East Coast Park is minutes away, which also means car lockouts at its carparks.",
 estates=["Bedok North", "Bedok South", "Bedok Reservoir", "Chai Chee", "Kaki Bukit", "Siglap", "Frankel", "Opera Estate"],
 landmarks=["Bedok Mall", "Bedok Reservoir Park", "East Coast Park", "Kaki Bukit Industrial Estate"],
 mrt=["Bedok", "Tanah Merah", "Kembangan", "Bedok North", "Bedok Reservoir", "Kaki Bukit", "Sungei Bedok"],
 buildings=[
  ("Landed homes", "Main gates, side gates and doors with several locks in Siglap, Frankel and Opera Estate."),
  ("Industrial units", "Warehouses and factories in Kaki Bukit — shutters, padlocks and office doors."),
  ("HDB estates", "Older and newer blocks across Bedok North and South."),
 ],
 jobs=["Landed home gate and door locks", "Warehouse and factory lock changes in Kaki Bukit", "HDB lockouts at night", "Car lockouts at East Coast Park"],
 access="For East Coast Park car lockouts, tell us the carpark letter (e.g. Carpark C) — it's the quickest way to find you.",
 faqs=[
  ("Keys locked in my car at East Coast Park — can you help?", "Yes. Send us the carpark number and your car model and we'll come with non-destructive tools."),
  ("Do you serve landed homes in Siglap and Opera Estate?", "Yes — gates, doors and side entrances."),
 ],
 nearby=["tampines", "marine-parade"]),

dict(slug="pasir-ris", name="Pasir Ris", region="East",
 intro="Pasir Ris is a family town by the sea — HDB estates, landed homes near Loyang, and holiday chalets and resorts by the beach — and lockouts happen in all of them.",
 overview="Pasir Ris is known for its beach park, resorts and holiday chalets, which bring a steady stream of families and gatherings. Most residents live in HDB estates around Pasir Ris Drives and Elias, with private and landed homes towards Loyang and Pasir Ris Park. Loyang's industrial estate adds factories and offices that need commercial lock work.",
 estates=["Pasir Ris Central", "Pasir Ris Drives", "Elias", "Loyang", "Pasir Ris West", "Pasir Ris Park"],
 landmarks=["Pasir Ris Park", "White Sands", "Downtown East", "Loyang Industrial Estate"],
 mrt=["Pasir Ris", "Tampines East"],
 buildings=[
  ("HDB estates", "A mix of older blocks and newer flats around the town centre and Elias."),
  ("Chalets and holiday stays", "Chalet doors, safes and lockers — holiday lockouts are common at weekends and school holidays."),
  ("Loyang industrial", "Factory and warehouse locks, shutters and office doors."),
 ],
 jobs=["Lockouts at chalets and holiday stays", "HDB main door lockouts", "Room safes that won't open", "Factory lock changes in Loyang"],
 access="For chalets, tell us the chalet name and unit, and let the front desk know we're coming. For HDB flats, the block and Drive number is enough.",
 faqs=[
  ("Locked out of a chalet in Pasir Ris — can you help?", "Yes. We'll check your booking details with you and the operator before opening the door."),
  ("Do you open room safes?", "Yes — Uncle Thomas is a US-trained safesmith. We'll confirm the safe is yours or that the operator authorises it."),
 ],
 nearby=["tampines"]),

# ======================= NORTH-EAST =======================
dict(slug="ang-mo-kio", name="Ang Mo Kio", region="North-East",
 intro="Ang Mo Kio is a large, mature estate where long-time residents and young families live side by side — so we see everything from decades-old mechanical locks to brand-new digital locks.",
 overview="Ang Mo Kio is one of Singapore's largest and most established towns, with HDB blocks along the Avenues and around AMK Hub, Teck Ghee, Cheng San and Kebun Baru. Private homes cluster near Yio Chu Kang, Mayflower and Lentor, where new condos have brought plenty of digital locks. The Ang Mo Kio industrial parks also bring factory and workshop jobs.",
 estates=["Ang Mo Kio Central", "AMK Avenues 1–10", "Teck Ghee", "Cheng San", "Kebun Baru", "Yio Chu Kang", "Mayflower", "Lentor"],
 landmarks=["AMK Hub", "Bishan-Ang Mo Kio Park", "Ang Mo Kio Town Garden", "Ang Mo Kio Industrial Park"],
 mrt=["Ang Mo Kio", "Yio Chu Kang", "Mayflower", "Lentor", "Bright Hill"],
 buildings=[
  ("Mature HDB blocks", "Original main door locks and gate hook bolts — often stiff after decades of use."),
  ("New condos at Lentor", "Modern digital locks; flat batteries and forgotten PINs are the usual calls."),
  ("Industrial parks", "Factory and workshop doors, shutters and cabinets."),
 ],
 jobs=["Elderly residents locked out after the door swung shut", "Digital lock batteries going flat", "Letterbox lock replacements", "Main door lock changes after moving in"],
 access="Ang Mo Kio's Avenues are long — the Avenue number plus block number helps us find you quickly, day or night.",
 faqs=[
  ("My elderly parent is locked out in Ang Mo Kio. Can you come quickly?", "Yes. Call us — we set off immediately. If anyone inside may be unwell, call 995 first."),
  ("Do you serve the new Lentor condos?", "Yes, including digital lock lockouts and installations."),
 ],
 nearby=["bishan", "yishun"]),

dict(slug="serangoon", name="Serangoon", region="North-East",
 intro="Serangoon combines busy HDB estates around Serangoon Central with the landed homes of Serangoon Gardens — two very different kinds of locks, both of which Uncle Thomas handles every week.",
 overview="Serangoon Central is built around NEX and the MRT interchange, with HDB estates in Serangoon North and along Upper Serangoon Road. Serangoon Gardens is a well-known landed estate with its own market and food centre, and condos line Lorong Chuan. It's a town where the same afternoon might bring an HDB lockout and a landed-home gate job.",
 estates=["Serangoon Central", "Serangoon North", "Serangoon Gardens", "Lorong Chuan", "Upper Serangoon"],
 landmarks=["NEX", "Serangoon Garden Market", "Chomp Chomp Food Centre", "Serangoon Stadium"],
 mrt=["Serangoon", "Lorong Chuan", "Kovan"],
 buildings=[
  ("Landed homes", "Main gates, side gates and front doors, often with several locks."),
  ("HDB estates", "Older and mid-age blocks around Serangoon North and Central."),
  ("Condos", "Digital locks and deadbolts along Lorong Chuan."),
 ],
 jobs=["Landed home main gate and door lockouts", "Digital lock installation on condo doors", "HDB gate lock replacements", "Car lockouts at NEX"],
 access="For Serangoon Gardens, the street name is enough. For NEX car lockouts, tell us the carpark level and lot.",
 faqs=[
  ("Can you open a locked main gate in Serangoon Gardens?", "Yes. We'll check proof of residence, then open the gate and advise if the lock needs replacing."),
  ("Do you do car lockouts at NEX?", "Yes — tell us the level and lot number."),
 ],
 nearby=["hougang", "ang-mo-kio"]),

dict(slug="hougang", name="Hougang", region="North-East",
 intro="Hougang is a mature, family-heavy town where many flats have been home to the same family for decades — with newer blocks and shophouses around Kovan and Buangkok.",
 overview="Hougang stretches from Kovan and Upper Serangoon Road through Hougang Central to Buangkok and Punggol Park. Many families have lived here for generations, so older locks are common, while newer blocks near Buangkok have more digital locks. Shophouses and condos around Kovan add shops and private homes to our work.",
 estates=["Hougang Central", "Hougang Avenues", "Kovan", "Buangkok", "Lorong Ah Soo", "Upper Serangoon Road"],
 landmarks=["Hougang Mall", "Heartland Mall Kovan", "Punggol Park", "Hougang Stadium"],
 mrt=["Hougang", "Kovan", "Buangkok"],
 buildings=[
  ("Mature HDB blocks", "Older main door and gate locks; snapped keys and stiff cylinders are common."),
  ("Newer flats near Buangkok", "Digital locks on doors and gates."),
  ("Kovan shophouses and condos", "Shop shutters, back doors and condo digital locks."),
 ],
 jobs=["Old main door locks replaced with new locks", "Digital lock lockouts in newer flats", "Shophouse and shop lockouts near Kovan", "Children locked in bedrooms or toilets"],
 access="Hougang Avenues run long — share the Avenue and block number. For Kovan shophouses, tell us front or back lane.",
 faqs=[
  ("My child locked the bedroom door from inside in Hougang. What should I do?", "Keep talking to them calmly and call us — interior door locks are usually quick to open without damage. If there's any danger, call 995."),
  ("Do you replace old HDB main door locks?", "Yes, with quality hardware and our no-expiry warranty."),
 ],
 nearby=["serangoon", "sengkang"]),

dict(slug="sengkang", name="Sengkang", region="North-East",
 intro="Sengkang is a younger town full of families in BTO flats — and many have digital locks on the main door or gate, so flat batteries and forgotten PINs are common calls.",
 overview="Sengkang's estates — Compassvale, Rivervale, Anchorvale and Fernvale — are linked by the LRT loops around Sengkang Central. Most homes are HDB flats built from the late 1990s onwards, with condos near the river and Sengkang Central. Digital locks are especially common here, and so are the problems that come with them.",
 estates=["Compassvale", "Rivervale", "Anchorvale", "Fernvale", "Sengkang Central", "Jalan Kayu"],
 landmarks=["Compass One", "Sengkang Riverside Park", "Sengkang Sports Centre", "Sengkang General Hospital"],
 mrt=["Sengkang", "Buangkok", "Sengkang LRT (East & West loops)"],
 buildings=[
  ("BTO and HDB flats", "Digital locks on main doors and gates — the most common Sengkang call-outs."),
  ("Condos", "Digital locks and deadbolts, often with guardhouse access."),
  ("Jalan Kayu", "Shophouses and eateries with shutters and back doors."),
 ],
 jobs=["Digital lock battery flat or keypad not responding", "Digital lock installation on BTO doors and gates", "Kids locked in rooms", "Letterbox lock replacements"],
 access="Tell us your LRT station or block number — Sengkang's estates are spread across East and West loops.",
 faqs=[
  ("My digital lock died in Sengkang. Can you open it without breaking it?", "In most cases, yes. Uncle Thomas has his own damage-free methods for digital locks of all brands."),
  ("Do you install gate digital locks on BTO flats?", "Yes — we'll confirm your gate and lock are compatible first."),
 ],
 nearby=["punggol", "hougang"]),

dict(slug="punggol", name="Punggol", region="North-East",
 intro="Punggol is Singapore's newest waterfront town, with modern BTO flats and condos — and a high share of digital locks, many fitted at key collection.",
 overview="Punggol has grown around its waterway, with estates at Waterway, Northshore, Sumang and Matilda, condos along the water, and the new Punggol Digital District bringing offices and a university campus. Most homes are new, so mechanical lock wear is rare — but digital lock problems are very common.",
 estates=["Punggol Waterway", "Northshore", "Sumang", "Matilda", "Punggol Point", "Punggol Digital District"],
 landmarks=["Waterway Point", "Punggol Waterway Park", "Coney Island", "Punggol Point Park"],
 mrt=["Punggol", "Punggol Coast", "Punggol LRT (East & West loops)"],
 buildings=[
  ("New BTO flats", "Digital locks on doors and gates — many fitted at key collection, some of them budget models."),
  ("Waterfront condos", "Smart locks with app control and guardhouse access."),
  ("Punggol Digital District", "Office suites and access-controlled doors."),
  ("Multi-storey carparks", "Car lockouts are common in Punggol's HDB and condo carparks. Tell us the carpark, level and lot number, and we'll come straight to the car."),
 ],
 jobs=["Digital lock lockouts and forgotten PINs", "Replacing or upgrading digital locks fitted at key collection", "Gate digital lock installation", "Office and shop locks in the Digital District", "Car lockouts in HDB and condo carparks"],
 access="Punggol's newest blocks can be hard to find on maps — your block number plus the nearest LRT station helps.",
 faqs=[
  ("The digital lock that came with my Punggol BTO keeps failing. Can you replace it?", "Yes. We open it if you're locked out, then recommend and install a reliable replacement with our no-expiry warranty."),
  ("Do you cover Punggol Point and Northshore?", "Yes, all of Punggol, 24/7."),
  ("I'm locked out of my car in a Punggol carpark. How fast can you come?", "Usually within 25–30 minutes, and on a recent Punggol job we arrived within 15. We check the log card before opening the car."),
 ],
 nearby=["sengkang", "hougang", "pasir-ris"]),

# ======================= NORTH =======================
dict(slug="woodlands", name="Woodlands", region="North",
 intro="Woodlands is a large northern town with mature estates around Marsiling and newer flats towards Woodlands North — and many residents who cross the Causeway at odd hours.",
 overview="Woodlands is the north's regional centre, with HDB estates in Woodlands Central, Marsiling, Admiralty and Woodlands North and South, plus industrial areas near the Causeway. Many residents work or shop across the border, so late-night returns and lost keys are part of life here.",
 estates=["Woodlands Central", "Marsiling", "Admiralty", "Woodlands North", "Woodlands South", "Woodgrove"],
 landmarks=["Causeway Point", "Woodlands Civic Centre", "Woodlands Waterfront Park", "Woodlands Checkpoint"],
 mrt=["Woodlands", "Marsiling", "Admiralty", "Woodlands North", "Woodlands South"],
 buildings=[
  ("Mature HDB estates", "Older locks around Marsiling and Woodlands Central."),
  ("Newer flats", "Digital locks in newer blocks towards Woodlands North."),
  ("Industrial units", "Factories and warehouses near the Causeway and Woodlands Avenue."),
 ],
 jobs=["Late-night lockouts after returning from Johor", "Digital lock battery and keypad problems", "HDB gate and main door lock replacement", "Industrial unit lock changes"],
 access="Woodlands is big — the Avenue/Drive name and block number help. We cover all of it, including Marsiling and Admiralty.",
 faqs=[
  ("I lost my keys in Johor and I'm back in Woodlands. Can you help tonight?", "Yes — we work 24/7. We'll check proof of residence, open the door and can replace the lock so the lost keys can't be used."),
  ("Do you serve Admiralty and Marsiling?", "Yes, all of Woodlands."),
 ],
 nearby=["sembawang", "yishun"]),

dict(slug="yishun", name="Yishun", region="North",
 intro="Yishun has grown fast, with new BTO estates alongside long-established blocks around Chong Pang and Nee Soon — a mix of digital locks and older mechanical locks.",
 overview="Yishun's town centre around Northpoint City is surrounded by HDB estates in Khatib, Chong Pang and Nee Soon, and many new BTO projects across the town. That mix means we handle both older worn locks and the digital locks that new owners fit.",
 estates=["Yishun Central", "Khatib", "Chong Pang", "Nee Soon", "Yishun Ring Road"],
 landmarks=["Northpoint City", "Yishun Park", "Yishun Pond Park", "Khoo Teck Puat Hospital"],
 mrt=["Yishun", "Khatib"],
 buildings=[
  ("New BTO estates", "Digital locks on main doors and gates."),
  ("Mature HDB blocks", "Older main door locks and gate hook bolts in Chong Pang and Nee Soon."),
  ("Shops", "Shop shutters and back doors around Yishun Central."),
 ],
 jobs=["Digital lock lockouts in new BTO flats", "Older main door locks jamming", "Letterbox lock replacements", "Bedroom and toilet doors locked from inside"],
 access="Yishun Ring Road loops around the town — share the street and block number and we'll find you.",
 faqs=[
  ("Can you change the locks in my new Yishun flat?", "Yes — main door, gate and letterbox locks, with our no-expiry warranty."),
  ("Do you serve Khatib and Chong Pang?", "Yes, all of Yishun."),
 ],
 nearby=["sembawang", "woodlands"]),

dict(slug="sembawang", name="Sembawang", region="North",
 intro="Sembawang combines newer HDB estates around Canberra and Sun Plaza with quiet landed homes and the old naval base houses near the coast.",
 overview="Sembawang's town centre at Sun Plaza is surrounded by HDB estates, with newer flats around Canberra. Towards the coast, the former naval base area has colonial-era houses and landed homes near Sembawang Park. It's a quieter corner of the north, but we cover it 24/7 just like everywhere else.",
 estates=["Sembawang Central", "Canberra", "Sembawang Drive", "Wellington", "Sembawang Park area"],
 landmarks=["Sun Plaza", "Canberra Plaza", "Sembawang Park", "Sembawang Hot Spring Park"],
 mrt=["Sembawang", "Canberra"],
 buildings=[
  ("Newer HDB flats", "Digital locks on doors and gates around Canberra."),
  ("Landed and heritage homes", "Older timber doors and gates near the coast — we use damage-free methods to protect them."),
  ("HDB estates", "Main door and gate locks around Sun Plaza."),
 ],
 jobs=["Digital lock lockouts in Canberra flats", "Landed home gate locks", "Main door lock replacements", "Car lockouts at Sembawang Park"],
 access="Near the coast, roads can be quiet and hard to find at night — a pinned location on WhatsApp is the fastest way to guide us.",
 faqs=[
  ("Do you come to Sembawang late at night?", "Yes, 24/7. Send your location on WhatsApp so we can find you quickly."),
  ("Can you open older timber doors without damage?", "We use damage-free methods wherever possible, especially on older doors."),
 ],
 nearby=["yishun", "woodlands"]),

# ======================= WEST =======================
dict(slug="clementi", name="Clementi", region="West",
 intro="Clementi is a mature western town full of families, students and renters — close to universities and polytechnics, with HDB estates, condos and landed homes around Sunset Way and West Coast.",
 overview="Clementi's town centre around Clementi Mall is ringed by mature HDB estates along the Clementi Avenues, with condos and landed homes towards Sunset Way, West Coast and Dover. With several universities and polytechnics nearby, many flats and rooms here are rented to students and young workers — which means plenty of lost keys, room door lockouts and lock changes between tenants.",
 estates=["Clementi Central", "Clementi Avenues", "West Coast", "Dover", "Sunset Way", "Clementi Woods"],
 landmarks=["Clementi Mall", "Clementi Woods Park", "West Coast Park", "Clementi Stadium"],
 mrt=["Clementi", "Dover"],
 buildings=[
  ("Mature HDB estates", "Older main door and gate locks along the Clementi Avenues."),
  ("Rented rooms and flats", "Room door locks and main door lock changes when tenants move in or out."),
  ("Condos and landed homes", "Digital locks, deadbolts and gates around Sunset Way and West Coast."),
 ],
 jobs=["Room door lockouts in rented flats", "Lock changes between tenants", "HDB main door lockouts", "Digital lock installation in condos"],
 access="If you're a tenant, have your tenancy agreement or a letter with your name and address ready — we need proof of residence before opening.",
 faqs=[
  ("I'm a tenant in Clementi and locked out of my room. Can you open it?", "Yes, if you can show you live there — for example your tenancy agreement. For a lock change, we'll usually need the landlord's agreement."),
  ("Do you change locks for landlords between tenants?", "Yes, main door, gate and room door locks, with our no-expiry warranty."),
 ],
 nearby=["jurong", "queenstown"]),

dict(slug="bukit-batok", name="Bukit Batok", region="West",
 intro="Bukit Batok is a green western town with HDB estates around its central area, newer flats towards Tengah, and condos and landed homes near Hillview.",
 overview="Bukit Batok's estates surround Bukit Batok Central and West Mall, with Bukit Gombak to the north and new estates on the western edge near Tengah. Private homes and condos sit around Hillview and the nature park. It's a mix of older blocks and new BTO flats, with all the lock types that come with each.",
 estates=["Bukit Batok Central", "Bukit Batok West", "Bukit Batok East", "Bukit Gombak", "Guilin", "Hillview"],
 landmarks=["West Mall", "Bukit Batok Nature Park", "Little Guilin", "Bukit Gombak Stadium"],
 mrt=["Bukit Batok", "Bukit Gombak", "Hillview"],
 buildings=[
  ("Mature HDB blocks", "Older main door locks and gate hook bolts."),
  ("New BTO flats", "Digital locks on doors and gates, especially towards the western edge."),
  ("Hillview condos and landed homes", "Digital locks, deadbolts and gate locks."),
 ],
 jobs=["HDB lockouts around Bukit Batok Central", "Digital lock problems in new flats", "Gate lock replacements", "Condo digital lock lockouts at Hillview"],
 access="Bukit Batok has hilly roads and several street names — share the street and block number, or pin your location on WhatsApp.",
 faqs=[
  ("Do you serve Bukit Gombak and Hillview?", "Yes, and the rest of Bukit Batok, 24/7."),
  ("Do you also cover Tengah?", "Yes. We cover new Tengah estates too — WhatsApp your block and we'll find you."),
 ],
 nearby=["bukit-panjang", "jurong"]),

dict(slug="bukit-panjang", name="Bukit Panjang", region="West",
 intro="Bukit Panjang is an HDB town wrapped around its own LRT loop, between nature reserves — with condos and landed homes along Upper Bukit Timah Road.",
 overview="Bukit Panjang's estates are linked by the Bukit Panjang LRT, with stops like Senja, Fajar, Pending, Petir and Segar giving their names to the neighbourhoods. Hillion Mall and Bukit Panjang Plaza form the town centre, and condos and landed homes run along Upper Bukit Timah Road towards Cashew and Hillview.",
 estates=["Bukit Panjang Ring Road", "Senja", "Fajar", "Pending", "Petir", "Segar", "Jelapang", "Cashew"],
 landmarks=["Hillion Mall", "Bukit Panjang Plaza", "Zhenghua Park", "Dairy Farm Nature Park"],
 mrt=["Bukit Panjang", "Cashew", "Bukit Panjang LRT"],
 buildings=[
  ("HDB estates", "A mix of older and newer blocks around the LRT loop."),
  ("Condos along Upper Bukit Timah", "Digital locks and deadbolts with guardhouse access."),
  ("Landed homes", "Gates and doors with multiple locks near Cashew."),
 ],
 jobs=["HDB lockouts around the LRT loop", "Condo digital lock lockouts", "Gate lock replacements", "Letterbox lock replacements"],
 access="Your nearest LRT station (e.g. Senja or Petir) plus block number is the quickest way to tell us where you are.",
 faqs=[
  ("Do you cover all the Bukit Panjang LRT estates?", "Yes — Senja, Fajar, Pending, Petir, Segar, Jelapang and the rest of Bukit Panjang."),
  ("Can you replace my digital lock in Bukit Panjang?", "Yes. We install all brands, with our no-expiry warranty."),
 ],
 nearby=["choa-chu-kang", "bukit-batok"]),

dict(slug="choa-chu-kang", name="Choa Chu Kang", region="West",
 intro="Choa Chu Kang is a north-western family town with HDB estates around Lot One and Yew Tee, served by its own LRT — and close to the new Tengah town.",
 overview="Choa Chu Kang's town centre at Lot One is surrounded by estates in Keat Hong, Teck Whye and Yew Tee, with landed homes and farms further out. Many flats were built in the 1990s, so locks are reaching the age where they start to stiffen and fail, while new estates nearby bring plenty of digital locks.",
 estates=["Choa Chu Kang Central", "Yew Tee", "Keat Hong", "Teck Whye", "Limbang"],
 landmarks=["Lot One", "Yew Tee Point", "Choa Chu Kang Park", "Choa Chu Kang Stadium"],
 mrt=["Choa Chu Kang", "Yew Tee", "Bukit Panjang LRT (Choa Chu Kang, Keat Hong, Teck Whye)"],
 buildings=[
  ("1990s HDB blocks", "Locks reaching the age where cylinders stiffen and keys snap."),
  ("Newer flats", "Digital locks on doors and gates."),
  ("Landed homes and farmland", "Gates and padlocks further out towards Lim Chu Kang."),
 ],
 jobs=["Stiff or failing main door locks", "Digital lock lockouts", "Gate padlocks cut and replaced", "Letterbox lock replacements"],
 access="Yew Tee and Keat Hong blocks are numbered by street — share your street and block number, or send a pin on WhatsApp.",
 faqs=[
  ("My main door lock in Choa Chu Kang is getting stiff. Should I replace it?", "A stiff lock often fails at the worst time. We can replace it on the spot with quality hardware and our no-expiry warranty."),
  ("Do you cover Yew Tee and Tengah?", "Yes, both — and the rest of Choa Chu Kang."),
 ],
 nearby=["bukit-panjang", "bukit-batok"]),
]

TOWN_BY_SLUG = {t["slug"]: t for t in TOWNS}

# Places covered without their own page yet (listed on the hub so every searcher sees coverage)
OTHER_TOWNS = {
 "Central": ["Potong Pasir"],
 "East": ["Changi", "Simei", "Loyang"],
 "West": ["Jurong East", "Jurong West", "Tengah", "Tuas"],
 "North": ["Admiralty", "Kranji", "Mandai"],
 "North-East": ["Seletar Hills", "Buangkok"],
}

def build(x):
    content = x["content"]
    regions = ["Central", "East", "West", "North", "North-East"]

    # ---- hub ----
    crumbs = [("Home", ""), ("Areas", "areas/")]
    title = "Locksmith Near Me Singapore | Every Town, 24/7"
    desc = "Need a locksmith near you? Uncle Thomas covers every town in Singapore 24/7 — Toa Payoh, Ang Mo Kio, Tampines, Jurong, Woodlands and more. Call 9224 9224."
    cards = []
    for r in regions:
        linked = "".join(f'<a href="~/areas/{t["slug"]}/">{t["name"]}</a>' for t in TOWNS if t["region"] == r)
        other = "".join(f"<span>{n}</span>" for n in OTHER_TOWNS.get(r, []))
        cards.append(f'<div class="card area-card"><h3>{r}</h3><div class="town-links">{linked}{other}</div></div>')
    body = (x["page_hero"](crumbs, "Locksmith Near Me — Every Town in Singapore",
            "Wherever you are on the island, Uncle Thomas and his team can reach you — 24 hours a day, including weekends and public holidays.",
            ["24/7 islandwide", "We set off immediately", "Since 1998"]) +
            f'''<section class="section"><div class="container"><h2 class="section-title">Areas We Serve</h2>
<p class="section-lead">Tap your town for local details. Don't see your area? We still cover it — every part of Singapore.</p>
<div class="grid g3">{"".join(cards)}</div>
<div class="prose" style="max-width:820px;margin:40px auto 0">
<h2>Why "near me" matters less for a mobile locksmith</h2>
<p>A locksmith doesn't need a shop next to you — what matters is that someone sets off the moment you call. Uncle Thomas's team works on the move across the island, so whether you're in an HDB flat in the heartlands, a condo in town or an industrial unit in the west, we come to you. Call or WhatsApp <a href="{x["C"].WA_LINK}" target="_blank" rel="noopener">{x["C"].PHONE}</a> with your location and we'll give you an honest arrival estimate and the price before we leave.</p>
</div></div></section>''' + x["cta_band"]())
    nodes = x["page_schema"]("areas/", title, desc, crumbs, page_type="CollectionPage", extra=[
        {"@type": "ItemList", "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "url": x["C"].SITE + f"/areas/{t['slug']}/", "name": "Locksmith " + t["name"]}
            for i, t in enumerate(TOWNS)]}])
    x["render"]("areas/", title, desc, body, nodes, priority="0.8")

    svc_pills = "".join(f'<li><a href="~/{s["path"]}">{s["short"]}</a></li>' for s in content.SERVICES)

    # ---- town pages ----
    for t in TOWNS:
        path = f"areas/{t['slug']}/"
        n = t["name"]
        crumbs = [("Home", ""), ("Areas", "areas/"), (n, path)]
        title = t.get("title") or f"Locksmith {n} 24/7 | Safes, Cars & Digital Locks"
        if len(title) > 60:
            title = f"Locksmith {n} 24/7 | Uncle Thomas Locksmith"
        if len(title) > 60:
            title = f"Locksmith {n} 24/7 | Uncle Thomas"
        desc = t.get("desc") or f"24/7 locksmith in {n}: safe opening, car lockouts, digital locks and door lockouts. Uncle Thomas sets off as soon as you call. Since 1998. Call 9224 9224."
        if len(desc) > 158 and not t.get("desc"):
            desc = f"24/7 locksmith in {n}: safes, cars, digital locks & lockouts. We set off as soon as you call. Since 1998. Call 9224 9224."
        facts = (f'<div class="facts"><div class="fact"><strong>Estates we cover</strong>{", ".join(t["estates"])}</div>'
                 f'<div class="fact"><strong>Landmarks</strong>{", ".join(t["landmarks"])}</div>'
                 f'<div class="fact"><strong>MRT / LRT</strong>{", ".join(t["mrt"])}</div>'
                 f'<div class="fact"><strong>Region</strong>{t["region"]} Singapore · 24/7 coverage</div></div>')
        bld = "".join(f"<h3>{h}</h3><p>{p}</p>" for h, p in t["buildings"])
        jobs = "".join(f"<li>{j}</li>" for j in t["jobs"])
        recent = C.RECENT_JOBS.get(t["slug"], [])
        _ph = x["photo"](f"areas/{t['slug']}/") if f"areas/{t['slug']}/" in C.PHOTOS else ""
        recent_html = (f'<h2>Recent jobs in {n}</h2><ul class="jobs">' + "".join(f"<li>{j}</li>" for j in recent) + "</ul>" + _ph
                       if recent else f'<!-- FILL: real recent jobs in {n} → _build/config.py RECENT_JOBS["{t["slug"]}"]. Section hidden until then. -->')
        near = [TOWN_BY_SLUG[s] for s in t["nearby"] if s in TOWN_BY_SLUG]
        near_html = " and ".join(f'<a href="~/areas/{m["slug"]}/">{m["name"]}</a>' for m in near)
        faqs = list(t["faqs"]) + ([EXTRA_FAQS[t["slug"]]] if t["slug"] in EXTRA_FAQS else []) + [
            (f"How much does a locksmith in {n} cost?", "The same as anywhere in Singapore: it depends on the lock and the time of day, and we confirm the price before we start. See our <a href=\"~/prices/\">price list</a>."),
        ]
        body = (x["page_hero"](crumbs, t.get("h1") or f"Locksmith in {n} — 24/7 Emergency Service",
                f"Locked out in {n}? {t['intro']}", ["24/7 incl. public holidays", "Since 1998", "We check ID before opening"]) +
                f'''<section class="section"><div class="container narrow prose">
<h2>Locksmith work in {n}</h2>
<p>{t["overview"]}</p>
{facts}
{t.get("feature", "")}
<h2>Locks and buildings in {n}</h2>
{bld}
<h2>Lock tips for {n} homes and businesses</h2>
<p>{LOCAL_NOTES.get(t["slug"], "")}</p>
<h2>A typical call in {n}</h2>
<p>{TYPICAL.get(t["slug"], "")}</p>
<h2>Jobs we often do in {n}</h2>
<ul>{jobs}</ul>
{recent_html}
<h2>Getting to you in {n}</h2>
<p>{t["access"]} Locked out right now? Here's <a href="~/guides/locked-out-of-hdb-flat/">what to do while you wait</a>.</p>
<h2>Services in {n}</h2>
<ul class="link-pills">{svc_pills}</ul>
{"<p>Also nearby: " + near_html + ".</p>" if near_html else ""}
</div></section>
<section class="section section-alt"><div class="container narrow">{x["faq_html"](faqs, f"{n} Locksmith FAQs")}</div></section>''' +
                x["cta_band"](f"Need a Locksmith in {n} Now?"))
        svc = {"@type": "Service", "@id": x["C"].SITE + "/" + path + "#service", "name": f"Locksmith in {n}",
               "serviceType": "Locksmith", "provider": {"@id": x["BUSINESS_ID"]},
               "areaServed": [{"@type": "Place", "name": f"{e}, Singapore"} for e in [n] + t["estates"][:5]],
               "url": x["C"].SITE + "/" + path,
               "hoursAvailable": {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], "opens": "00:00", "closes": "23:59"}}
        nodes = x["page_schema"](path, title, desc, crumbs, faqs=faqs, extra=[svc])
        x["render"](path, title, desc, body, nodes, priority="0.7")


# Town-specific advice paragraphs (rendered as "Lock tips for <town>").
LOCAL_NOTES = {
"tanglin": "In large Tanglin homes, keys tend to multiply: helpers, drivers, gardeners and contractors may all have had one at some point. If you've lost track, the simplest fix is to rekey every gate and door in one visit so old keys stop working. Do the same for safe combinations whenever household staff change.",
"bukit-timah": "Driveway gates in Bukit Timah take a beating from daily use, rain and heat. If a gate lock starts to stick, have it replaced before it fails with the car inside. For home safes, keep the combination written down somewhere secure away from the safe, because a forgotten code is the most common reason we're called.",
"holland-village": "Holland Village homes change hands and tenants often. If you're moving in, change the locks on day one; if you're moving out, make sure every safe is open and every code is handed over, so the next occupant doesn't inherit a locked safe with no code.",
"river-valley": "Smart locks in River Valley condos depend on batteries and apps. Change the batteries as soon as the lock warns you, keep the mechanical backup key outside the flat (with a friend or at the office), and don't rely only on your phone to get in.",
"sentosa-cove": "Salt air at Sentosa Cove is hard on locks and safe keypads. Before a long trip, replace safe and digital lock batteries, and check that gate locks still turn smoothly. Stainless or marine-grade gate locks last much longer here than standard ones.",
"newton": "Newton condos are full of digital locks that are rarely given a thought until the batteries die. Change them as soon as the lock starts warning you, and keep the mechanical backup key somewhere outside the flat, such as with a family member nearby. For home safes, write the combination down and keep it somewhere safe away from the safe itself: a forgotten code is the most common reason we're called to open one.",
"paterson": "Owners in Paterson often travel or rent their units out, so a lock can go unused for months. Before a long trip, change the digital lock batteries and check the backup key works. If you rent your unit out, change the code or cylinder between every tenancy, and keep a record of who has which code. For safes, change the combination whenever staff or tenants change.",
"toa-payoh": "In older Toa Payoh flats, the most common warning sign we see is a key that has to be jiggled or pulled slightly to turn. That usually means the cylinder pins are worn, and it's only a matter of time before the key snaps or the lock refuses to turn at all — often late at night. Replacing a worn cylinder costs far less than an emergency call-out with a broken key stuck inside. If your gate's hook-bolt lock has started to rust from corridor washing, a few drops of lock lubricant (not cooking oil) can help, but a rusted lock body is best replaced. Families with elderly parents living alone in Toa Payoh often ask us about digital locks so that children can let themselves in — it's a sensible upgrade for older blocks, provided the door is in good condition.",
"bishan": "Bishan homes often have more than one lock per entrance: a condo door with a deadbolt and a digital lock, or a landed home with a gate lock, a padlock and a front door lock. When you call, tell us exactly which lock is stopping you — it changes the tools we bring and the price. If you live in a condo, keep a spare card or key with a trusted neighbour or family member rather than in your car, because a car parked in the condo carpark doesn't help if the lift lobby needs a card too. For workshops in Sin Ming, we recommend replacing padlocks on shutters with closed-shackle padlocks, which are harder to cut and stand up better to the weather.",
"novena": "Clinics and medical suites in Novena often have strict rules about who can open a door or cabinet, so we'll always ask for authorisation from the clinic owner or practice manager before starting. If your clinic uses a key safe or drug cupboard, keep a record of who holds the keys, and change the lock when staff leave — it's cheaper than dealing with a missing key later. Shophouse owners along Balestier should check shutter padlocks every few months: rust on the shackle is the first sign that a padlock will seize, and a seized padlock means cutting it off. In older walk-up apartments, a door that has dropped on its hinges can put strain on the lock; if your key turns stiffly only when the door is closed, the door may need adjusting before the lock is replaced.",
"cbd-orchard": "In the city, the biggest delay in a lockout is usually building access rather than the lock itself. If you manage an office, save building security's after-hours number somewhere other than your office desk, and register a few people who are allowed to approve contractors. For shops and restaurants, keep the safe's manufacturer details and serial number on file — if the code is lost, it speeds up any manufacturer reset and helps us quote accurately. City condo and serviced-apartment residents should note that many high-end digital locks have an emergency power point and a backup key; keep the backup key somewhere outside the apartment, such as with a colleague or family member. We'll always ask for proof of residence or authorisation from management before opening a unit.",
"queenstown": "Queenstown has a high mix of rental flats and rooms near the universities and business parks, so we often help landlords change locks between tenants. If you're a landlord, changing the main door cylinder after each tenancy is a small cost compared with the risk of an old key being copied. Tenants, keep your tenancy agreement handy — we need proof that you live there before opening. In the older estates, a lot of the lockouts we see are caused by the door's latch slipping shut behind someone taking out the rubbish. If you often step out briefly, consider a lock that can be set on 'hold back' while you're in the corridor, or a digital lock with a keypad.",
"bukit-merah": "Tiong Bahru's heritage flats are much loved, and many still have timber doors that can be damaged by forced entry, so we always try damage-free methods first and explain the options before doing anything that could mark the door. In the industrial buildings around Bukit Merah Central and Alexandra, we recommend businesses keep a simple record of who holds which keys, and change locks when staff or contractors leave. For businesses with safes — including vessels — keep the safe's make, model and serial number on file, along with proof of ownership; it helps a safesmith quote accurately and work faster when you're locked out of something important.",
"kallang-whampoa": "Industrial units in Kallang Bahru and Kallang Way are often secured with a roller shutter and a padlock or two — and in Singapore's humidity, padlocks exposed to rain can seize within a few years. A seized padlock usually has to be cut, which is quick but means you'll need a new one, so we bring replacements. If your unit is in a multi-tenant industrial building, check with the management whether after-hours access needs approval before you call; it saves waiting at the gate. In Whampoa and Boon Keng's older HDB blocks, the same advice applies as in other mature estates: a stiff key is an early warning, and replacing the cylinder before it fails costs less than a lockout.",
"geylang": "Shophouses in Geylang are busy at all hours, and many have both a front shutter and a back door onto the lane. When you call, tell us which entrance you need to get through — sometimes the back door is quicker and causes less disruption to your shop. Upstairs walk-up apartments often share a staircase door as well as the unit door, so let us know if there's a shared gate we need to get past. For businesses around Paya Lebar Quarter, after-hours lockouts usually involve building security, so register your contractors in advance if you can. As always, we'll check proof of residence or authorisation before opening any door or shutter.",
"marine-parade": "Living near the sea is lovely, but salt in the air is hard on locks. In Marine Parade's older blocks and the terraces of Katong and Joo Chiat, we often see gate locks and padlocks that have corroded far faster than they would inland. If your key feels gritty or the lock needs force to turn, it's worth replacing it with a lock designed for outdoor use before it seizes. Seafront condo residents should check that their digital lock's batteries are changed regularly, since humidity and heavy use can shorten battery life. For heritage doors, we use damage-free techniques wherever possible, and we'll always talk you through the options before doing anything that could mark the door.",
"tampines": "Tampines North has thousands of new flats, and many owners install a digital lock within weeks of collecting their keys. If you're about to do the same, check your door's thickness and the existing lock cut-out before you buy — a lock that doesn't fit properly is the most common cause of later problems. In the older estates, the gate hook-bolt locks take the most wear, especially in corridors that are washed regularly. For businesses in the regional centre and Changi Business Park, keep a spare key or access card with a second person, and change locks when staff leave. Mall carpark car lockouts are common at weekends — tell us the carpark, level and lot number and we'll find you quickly.",
"bedok": "Landed homes in Siglap, Frankel and Opera Estate often have several layers of security — a main gate, a side gate, a front door and sometimes a back door, each with its own key. It's easy to lose track of which key opens what, so we suggest labelling keys discreetly (not with your address) and keeping a spare set with family. In Kaki Bukit's industrial estate, roller shutters and padlocks see heavy use; replacing worn padlocks before they seize saves an emergency call. Car lockouts near East Coast Park are among our most common Bedok jobs — keys left in the boot while unloading bicycles or picnic gear is a classic. Non-destructive car entry tools mean no broken windows.",
"pasir-ris": "Pasir Ris chalets and holiday stays get busy at weekends and during school holidays, and so do lockouts: a door swings shut while everyone is at the beach, or a room safe won't open on check-out day. If you're staying in a chalet, let the front desk or operator know if you're locked out — we'll need to confirm the booking before opening. Families in the HDB estates around Pasir Ris Drives and Elias often ask about child-proofing: interior doors with privacy locks can usually be opened from outside with the right tool, so it's worth asking us how your door's lock works before there's a problem. In Loyang's industrial estate, we handle shutters, padlocks and factory doors.",
"ang-mo-kio": "Ang Mo Kio has many elderly residents who have lived in the same flat for decades, and a door swinging shut behind them is one of the most common reasons we're called here. If an elderly family member lives alone, consider a digital lock with a PIN that trusted family members know, or keep a spare key with a neighbour. Older gate hook-bolt locks are often stiff after years of use; if it takes two hands to turn the key, it's time to replace the lock. In the newer condos around Lentor, the usual problems are digital lock batteries and forgotten PINs — change the batteries as soon as the lock warns you.",
"serangoon": "Serangoon Gardens homes tend to have heavy main gates with lock bodies that take a lot of wear from daily use and the weather. If your gate lock has started to stick or the key turns only partway, a replacement now is much cheaper than an emergency call-out later. For HDB residents in Serangoon North, gate padlocks and hook-bolt locks are the usual suspects. Condo residents along Lorong Chuan with digital locks should keep the backup key somewhere outside the unit — many people keep it inside, which doesn't help when the battery dies. Car lockouts at NEX are common on busy weekends; tell us the carpark level and lot so we can come straight to you.",
"hougang": "Hougang's long-time residents often still use the original locks their flats came with, and those locks are now reaching the end of their life. Worn keys and stiff cylinders are early warning signs. For families with young children, interior doors with push-button privacy locks are a frequent call-out: a child locks the bedroom or toilet door and can't unlock it. Most of these can be opened quickly without damage, but it helps to know how your doors' emergency release works. Around Kovan, shop owners with roller shutters should check padlocks regularly for rust, especially before the monsoon season.",
"sengkang": "Sengkang's BTO flats are packed with digital locks, so most of our calls here are about batteries, forgotten PINs and keypads that stop responding after rain. Most digital locks warn you for weeks before the batteries die — change them as soon as you hear the low-battery alert, and use good-quality batteries. If your lock has an emergency power terminal or a backup key, make sure you know where they are before you need them. Families with young children should also check whether the lock has a child-lock or privacy mode that could be switched on by accident. For older flats in Sengkang, gate locks and letterbox locks are the other common jobs.",
"punggol": "Many Punggol homeowners received digital locks at key collection or bought budget models online, and some of these are less reliable in Singapore's heat and humidity. If your lock regularly fails to read fingerprints, drains batteries quickly or jams, it may be cheaper in the long run to replace it with a better-quality model. Before buying, check that the lock suits your door's thickness and cut-out. Smart locks with app control are popular in the waterfront condos — keep the app updated and know how to use the backup key or emergency power if the phone or the lock fails. For offices in the Punggol Digital District, we handle access doors and lock changes.",
"woodlands": "Woodlands residents who travel across the Causeway often carry keys in bags that get searched, swapped or left behind, so lost keys are a common story here. If you lose keys anywhere outside your home, it's worth changing the main door cylinder afterwards, especially if anything with your address was lost at the same time. Late-night lockouts are part of our routine in Woodlands — we work 24/7 and will check proof of residence before opening. In the newer blocks towards Woodlands North, digital lock batteries and keypads are the usual problems. Industrial unit owners near the Causeway should replace padlocks before they seize in the humidity.",
"yishun": "Yishun's mix of old and new flats means our calls here are split between worn mechanical locks and new digital locks. In Chong Pang and Nee Soon's older blocks, stiff cylinders and snapped keys are common — replacing a worn lock early is cheaper than a late-night lockout. In newer BTO estates, many homeowners add a digital lock soon after moving in; if you're planning to, check that your gate and door are compatible first. Letterbox locks are another frequent job in Yishun, as letterbox keys are small and easily lost. We'll check proof of residence before opening any letterbox or door.",
"sembawang": "Sembawang is quieter than many towns, which makes it easy for us to reach at night — but roads near the coast and Sembawang Park can be hard to find in the dark, so a pinned location on WhatsApp helps. The area's older colonial-era houses and landed homes often have traditional timber doors and gates that deserve careful, damage-free handling. In the newer Canberra estates, digital locks are common, and the advice is the same as elsewhere: change batteries at the first warning and know where your backup key is. If you lose your keys, consider changing the main door cylinder, especially if anything with your address went missing too.",
"jurong": "Jurong's industrial estates mean we do more commercial work here than in most towns: factory doors, warehouse shutters, cabinets and safes. For businesses, we recommend keeping a simple key register and changing locks when staff leave — it's the cheapest security upgrade there is. If your factory has a safe, keep the make, model and serial number on file, along with proof of ownership; it helps us quote accurately. In the large HDB estates of Jurong West, the usual jobs are lockouts, worn gate locks and digital lock problems. Mall carparks at Jurong Gateway and Jurong Point see regular car lockouts — tell us the carpark and level.",
"clementi": "Because so many Clementi flats and rooms are rented, we're often asked who can authorise a lockout or a lock change. Tenants can usually get help with a lockout by showing their tenancy agreement or a letter with their name and the address. Changing the lock on a rented flat, though, normally needs the landlord's agreement, so check your tenancy agreement first. Landlords: replacing the main door cylinder between tenants is a small cost compared with the risk of old keys still being in circulation. For students in rented rooms, a small key safe or a trusted friend holding a spare key can save an expensive call-out.",
"bukit-batok": "Bukit Batok's hilly streets and spread-out estates can make addresses hard to find, especially at night — a pinned location on WhatsApp is the fastest way to guide us. In the mature estates around Bukit Batok Central and Bukit Gombak, worn gate locks and stiff main door cylinders are the usual call-outs. The newer flats on the western edge of town and in nearby Tengah have more digital locks; if you're choosing one, check that it suits your door before buying. Condo residents around Hillview should keep their digital lock's backup key somewhere outside the unit, not in a drawer inside.",
"bukit-panjang": "The Bukit Panjang LRT stations make handy landmarks — telling us you're near Senja, Petir or Fajar narrows things down quickly. Many Bukit Panjang flats are now old enough that their original locks are wearing out, so stiff keys and jammed cylinders are a common call. Families living near the nature reserves sometimes find that humidity and damp affect gate locks and padlocks more than elsewhere; a lock designed for outdoor use lasts longer. For condo residents along Upper Bukit Timah Road, the usual issues are digital lock batteries and forgotten PINs. We install and replace digital locks of all brands, with our no-expiry warranty.",
"choa-chu-kang": "Many Choa Chu Kang flats were built in the 1990s, which means their original locks have now seen decades of daily use. If your key has to be pushed, pulled or jiggled, the cylinder is worn and is likely to fail — replacing it now avoids a late-night lockout. Families in Yew Tee and Keat Hong often ask about digital locks so that children can come home without a key; if that's you, choose a lock with a mechanical backup and a low-battery warning. Further out towards the farms and landed homes, gates and padlocks are the common jobs. Send a pinned location on WhatsApp if you're somewhere hard to find.",
}

# One more town-specific question per page.
EXTRA_FAQS = {
"tanglin": ("Do you work at embassies and diplomatic residences in Tanglin?", "We work wherever we're authorised to. Security will need to clear us in advance, and we'll need written authorisation for any lock or safe."),
"bukit-timah": ("Can you replace all the locks on a bungalow in one visit?", "Usually, yes. Send photos of each gate and door lock on WhatsApp, and we'll confirm the parts and price before we come."),
"holland-village": ("Do you serve Chip Bee Gardens and Leedon Park?", "Yes. We cover all the landed estates and condos around Holland Village, 24/7."),
"river-valley": ("How quickly can you get to Robertson Quay at night?", "River Valley is close to the city, so we usually arrive within 25–30 minutes, any time."),
"sentosa-cove": ("Do you come to Sentosa Cove at night?", "Yes, 24/7. Let estate security know we're coming so we can get to you quickly."),
"newton": ("Can you open my car in a Newton condo carpark?", "Yes. Tell us the carpark level, lot number and car model, and let the guardhouse know. We open cars without damage after checking the log card."),
"paterson": ("Do you work with condo management in Paterson?", "Yes. We coordinate with the concierge or management office, and check proof of residence or ownership before opening anything."),
"toa-payoh": ("Can you replace the lock on an old timber door in Toa Payoh?", "Yes. Older timber doors often have mortise locks set into the door edge. We'll fit a replacement that suits the existing cut-out where possible, so the door doesn't need extra work."),
"bishan": ("Do you serve landed homes near Upper Thomson?", "Yes. We handle main gates, side gates and front doors on landed homes in Bishan and Thomson, including homes with several locks on one entrance."),
"novena": ("Can you change locks at our Balestier shop after a staff member leaves?", "Yes. We replace shutter padlocks, door locks and cabinet locks so former staff keys no longer work, usually in a single visit."),
"cbd-orchard": ("Do you open hotel or serviced apartment doors in the city?", "We work with the property's management. They'll need to authorise us, and we'll confirm the guest or resident's identity before opening."),
"queenstown": ("Can I change the lock on a flat I'm renting in Queenstown?", "Usually only with the landlord's agreement — check your tenancy agreement. We can help with a lockout if you can show you live there."),
"bukit-merah": ("Do you work in the industrial buildings around Bukit Merah Central and Alexandra?", "Yes — shutters, padlocks, office doors, cabinets and safes, 24/7. We'll need authorisation from the business before opening."),
"kallang-whampoa": ("How fast can you reach Kallang at night?", "Kallang is central, so it's one of the quickest areas for us to reach. We set off as soon as you call and give you an honest estimate."),
"geylang": ("Can you open the upstairs apartment door above a Geylang shophouse?", "Yes. Let us know if there's a shared staircase gate as well, and have proof of residence ready."),
"marine-parade": ("Can you replace a rusted gate lock in Marine Parade?", "Yes. We replace corroded gate locks and padlocks with ones better suited to outdoor use near the sea."),
"tampines": ("Do you serve Simei and Tampines West?", "Yes — all of Tampines, including Simei, Tampines West, East, North and Central."),
"bedok": ("Can you open a warehouse shutter in Kaki Bukit?", "Yes. We open locked shutters and cut seized padlocks, then fit a new padlock so you can lock up again."),
"pasir-ris": ("Do you serve Loyang and the landed homes near Pasir Ris Park?", "Yes. We cover all of Pasir Ris, including Loyang's industrial estate and the private homes near the park."),
"ang-mo-kio": ("Can you install a digital lock for my elderly parents in Ang Mo Kio?", "Yes. We'll recommend an easy-to-use model with a mechanical backup and install it with our no-expiry warranty."),
"serangoon": ("Can you replace an old landed-home gate lock in Serangoon Gardens?", "Yes. We'll match the lock to your gate and fit it with our no-expiry warranty."),
"hougang": ("Do you serve Kovan shophouses?", "Yes. We open shutters and doors and replace worn padlocks and locks for shops around Kovan and Upper Serangoon Road."),
"sengkang": ("My digital lock's keypad stopped working after rain. What can I do?", "Let it dry and try again after a while. If it still won't respond, try the backup key or emergency power — or call us and we'll open it."),
"punggol": ("Can you install a digital lock on my Punggol BTO gate?", "Yes. We check that your gate and the lock are compatible, then install it and set it up with you."),
"woodlands": ("Do you serve the Woodlands industrial areas?", "Yes. We handle factory and warehouse locks, shutters and office doors near the Causeway and across Woodlands."),
"yishun": ("Can you replace my Yishun letterbox lock?", "Yes. After checking your proof of residence, we open the letterbox and fit a new lock with new keys."),
"sembawang": ("Do you serve Canberra?", "Yes. Canberra is part of our Sembawang coverage, and we handle the digital locks common in the newer flats there."),
"jurong": ("Do you do car lockouts at Jurong Point and JEM?", "Yes. Tell us the carpark, level and lot number, plus your car model, and we'll come with non-destructive tools."),
"clementi": ("Do you serve Dover and West Coast?", "Yes — all of Clementi, including Dover, West Coast and the condos and landed homes around Sunset Way."),
"bukit-batok": ("Can you open a stuck gate lock in Bukit Batok?", "Yes. We open it first, then advise whether the lock can stay or should be replaced."),
"bukit-panjang": ("Do you serve the condos along Upper Bukit Timah Road?", "Yes. We'll coordinate with the guardhouse to reach your unit quickly."),
"choa-chu-kang": ("Do you serve landed homes and farms beyond Choa Chu Kang?", "Yes. We cover the whole north-west, including landed homes and farmland — send a pinned location on WhatsApp."),
}

# "A typical call in <town>": a realistic, clearly *typical* situation for each town
# (never presented as a dated real job; real jobs go in config.RECENT_JOBS).
TYPICAL = {
"tanglin": "A family in a Tanglin bungalow can't open the study safe after a helper who knew the code has left. After confirming ownership, Uncle Thomas opens the safe and sets a new combination that only the family knows.",
"bukit-timah": "A Bukit Timah homeowner reverses out for the school run and the driveway gate lock jams with the car halfway out. We open the gate, replace the worn lock body with a sturdier one, and the family is on the road again.",
"holland-village": "An expat family leaving Singapore finds that nobody remembers the code to the wardrobe safe in their Holland Village rental. With the landlord's written authorisation, Uncle Thomas opens it the day before the movers arrive.",
"river-valley": "A Robertson Quay resident returns from an overseas trip and the condo's smart lock won't respond: the batteries died while they were away and the backup key is inside. After checking ID with the concierge, we open the lock without damage and replace the batteries.",
"sentosa-cove": "A boat owner at the Sentosa Cove marina can't open the small safe on board after a long season away. With proof of ownership, Uncle Thomas opens it without damaging the cabinetry around it.",
"newton": "A family in a Newton condo can't remember the combination of the bedroom safe holding their passports, two days before a flight. They send a photo of the safe, and after checking ID with their address, Uncle Thomas opens it and sets a new combination they'll remember.",
"paterson": "A landlord near Paterson Hill finds that a tenant has moved out and changed the digital lock code without passing it on. The new tenant arrives on Saturday. After checking proof of ownership, we open the door without damage and reset the lock so the landlord can set a new code.",
"toa-payoh": "An auntie in a Lorong 1 block takes the rubbish to the chute in her house slippers, and the main door's old latch clicks shut behind her. Her keys are on the dining table. A neighbour lends her a phone, she WhatsApps a photo of the door, and we agree the price before we set off. The lock opens without damage, and because the key had been sticking for months, she decides to replace the worn cylinder while we're there.",
"bishan": "A family in a Bishan condo comes home from Junction 8 to find the digital lock's screen dark. The batteries have died after weeks of low-battery beeps, and the backup key is in a kitchen drawer inside. The guardhouse lets us through once the owner confirms, we power up and open the lock, and the family leaves with fresh batteries in place and the backup key moved to a relative's home.",
"novena": "A clinic manager arrives at a Novena medical suite at 7.30am, half an hour before the first patient, and the suite door's key won't turn. Building security has to sign us in, so the manager calls them first. With authorisation confirmed, we open the door without marking it, and because the cylinder is worn, we replace it on the spot so the clinic opens on time with new keys for the staff.",
"cbd-orchard": "A restaurant manager near Tanjong Pagar closes up after midnight and realises the office safe holding the day's float won't accept the code. The owner is overseas but sends written authorisation by WhatsApp. We open the safe without drilling, and the manager resets the code with the owner on a video call before locking up for the night.",
"queenstown": "A landlord in Commonwealth has a tenant moving out on Friday and a new tenant moving in on Saturday. The old tenant has returned only two of the three keys. The landlord sends us a photo of the door lock and the gate lock, and we replace both cylinders that afternoon so the new tenant gets the only working keys.",
"bukit-merah": "A Tiong Bahru resident with a much-loved timber door is locked out after the latch slips shut. They're worried about the door being damaged, so we explain the damage-free options first and agree the price. The door opens cleanly, the frame is untouched, and the resident keeps a spare key with a friend nearby from then on.",
"kallang-whampoa": "A Kallang Bahru workshop owner arrives at 6am to start a delivery, but the padlock on the roller shutter has seized after months of rain. The key turns halfway and stops. We cut the seized padlock, fit a new closed-shackle padlock suited to outdoor use, and the van is out on time.",
"geylang": "A shop owner on Sims Avenue loses the bunch of keys for both the front shutter and the back-lane door. Anyone who finds them could open the shop, so after checking the business details, we open the front shutter, then change the padlocks and the back door lock so the lost keys no longer work.",
"marine-parade": "A Marine Parade resident's gate lock has been getting stiffer for months, and tonight the key won't turn at all. Sea air has corroded the lock body. We open the gate, show the owner the rust inside the old lock, and fit a replacement better suited to the salty air near East Coast Park.",
"tampines": "A couple collects the keys to their new Tampines North BTO flat and buys a digital lock online the same week. When it arrives, they aren't sure it fits their door. They WhatsApp us photos of the door edge and the lock box, we confirm the fit, and we install it, setting up their PINs and fingerprints with them before we leave.",
"bedok": "A family unloading bicycles at the East Coast Park carpark puts the car key on the boot floor, closes the boot and hears the car lock. The bicycles are out but the key is in. They send us the carpark, lot number and car model, and we open the car with non-destructive tools so the picnic can go ahead.",
"pasir-ris": "On check-out morning at a Pasir Ris chalet, the room's small safe won't open, and the family's passports are inside for a trip the next day. The operator confirms the booking and authorises us, and we open the safe without damaging it, with time to spare before check-out.",
"ang-mo-kio": "A son gets a call from his elderly father in Ang Mo Kio: the door has swung shut and his father is waiting in the corridor. We head over, confirm the father's identity with his NRIC once inside, and open the door without damage. The family then asks about a simple digital lock so this can't happen again, and we recommend one with a mechanical backup key.",
"serangoon": "A Serangoon Gardens homeowner's heavy main gate lock finally refuses to turn after years of daily use, with the car parked inside. We open the gate, check the lock body and replace it with a sturdier gate lock, so the family can lock up properly that night.",
"hougang": "A toddler in a Hougang flat pushes the button lock on the bathroom door and can't work out how to open it. The parent is on the other side, worried. We arrive, open the privacy lock from outside in under a minute without damage, and show the parent how the emergency release works on that type of door.",
"sengkang": "A Sengkang BTO owner comes home after a heavy downpour and the gate's digital lock keypad won't respond. The family has never used the backup key and isn't sure where it is. We open the lock, check that it has dried properly, and show them where the emergency power point and key override are.",
"punggol": "A Punggol homeowner's budget digital lock keeps failing to read fingerprints and drains its batteries every few weeks. Tonight it won't open at all. We get the family inside, then recommend a more reliable model suited to their door, and install it with our no-expiry warranty.",
"woodlands": "A Woodlands resident comes back from Johor Bahru late at night and realises the house keys were left behind across the Causeway. We check proof of residence, open the main door, and because the keys are with someone else for now, the resident decides to keep the old lock and pick the keys up the next day.",
"yishun": "A Yishun resident loses the tiny letterbox key and has a bank letter waiting inside. After checking proof of residence, we open the letterbox and fit a new lock with new keys, so the old key no longer matters.",
"sembawang": "A family staying in one of Sembawang's quiet landed streets near the park gets locked out of the side gate late at night. The road is dark and hard to find, so they send a pinned location on WhatsApp. We find the house first time and open the gate without damaging the old ironwork.",
"jurong": "A factory manager in Jurong needs the office safe opened before the morning shift: the staff member with the code has left the company. With written authorisation from the director and proof of ownership, we open the safe, and the company sets a new code and changes the office door lock the same day.",
"clementi": "A student renting a room near Clementi locks the room door with the key inside. We check the tenancy agreement on their phone and confirm with the landlord, then open the door without damage. The landlord later asks us to replace the room locks between tenants.",
"bukit-batok": "A Bukit Batok resident at the top of a hilly street is locked out late at night and isn't sure how to describe the way in. A pinned location on WhatsApp brings us straight to the block. The main door opens without damage, and the resident decides to replace a worn gate lock while we're there.",
"bukit-panjang": "A Bukit Panjang family near Petir LRT station finds their gate padlock rusted solid after weeks of wet weather. The key won't go in at all. We cut it off and fit a weather-resistant padlock, then check that the gate's own lock is still in good shape.",
"choa-chu-kang": "A Yew Tee family's original 1990s main door lock has been getting harder to turn, and tonight the key snaps off in the cylinder. We open the door without damage and replace the worn cylinder, so the family has a smooth lock and new keys before bedtime.",
}
