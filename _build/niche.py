"""
Niche service pages (added 29 Oct 2026), built from Google SG autocomplete research:
"hdb main door lock replacement (price)", "hdb gate lock replacement (price)",
"car key duplicate singapore", "car key replacement singapore", "key fob duplicate".
Uses only owner-confirmed facts: lock replacement from P_REPLACE incl. lock and
installation, no-expiry warranty, no repairs, car key fob cloning for all major
brands (never Tesla) from a working key, NRIC checked against the log card.
"""

NICHE_SERVICES = [
# ----------------------------------------------------------------------
dict(
 path="hdb-main-door-lock-replacement/", short="HDB main door lock replacement", icon="lock",
 card="New lock for your HDB main door, from {P_REPLACE} including the lock and installation, with a no-expiry warranty.",
 title="HDB Main Door Lock Replacement Singapore | From S$100",
 title_exp="HDB Main Door Lock Replacement | Price Agreed First",
 desc="Change your HDB main door lock: lost keys, new flat, worn or jammed lock. From S$100 including lock and installation, no-expiry warranty. Call 9224 9224.",
 h1="HDB Main Door Lock Replacement",
 sub="Lost keys, a new flat, a tenant moving out, or a lock that's stiff and jamming: Uncle Thomas replaces HDB main door locks across Singapore, with the price agreed first and a warranty that never expires.",
 badges=["From {P_REPLACE}", "No-expiry warranty", "Price agreed first"],
 body="""
<p><strong>The short answer:</strong> an HDB main door lock change starts from {P_REPLACE}, including the new lock and installation. WhatsApp {PHONE} photos of your lock from both sides and the door edge, and we'll confirm the exact price before we come. Every lock we fit comes with our warranty, with no expiry date.</p>

<h2>When to change your HDB main door lock</h2>
<ul>
<li><strong>You've moved into a resale flat</strong>, or your renovation is finished. Previous owners, agents and contractors may still have keys. See <a href="~/guides/change-locks-new-home/">changing locks when you move in</a>.</li>
<li><strong>Keys lost or stolen</strong>, especially with anything showing your address. See <a href="~/guides/lost-house-key/">lost your house key</a>.</li>
<li><strong>A tenant or helper has moved out.</strong></li>
<li><strong>The lock is stiff, the key catches, or the latch sticks.</strong> A worn lock is a lockout waiting to happen. See <a href="~/guides/door-lock-jammed/">door lock jammed</a>.</li>
<li><strong>After a break-in or attempted break-in.</strong></li>
</ul>

<h2>HDB main door locks we replace</h2>
<ul>
<li><strong>Mortise locksets with lever handles</strong>, where the lock body sits inside the door edge. Very common on HDB main doors.</li>
<li><strong>Cylinder and rim locks</strong> on older doors.</li>
<li><strong>Deadbolts</strong>, added for extra security.</li>
<li><strong>Digital and smart locks</strong>: see <a href="~/digital-lock-installation/">digital lock installation</a>.</li>
</ul>
<p>Not sure which lock you have? Read <a href="~/guides/main-door-lock-types/">main door lock types explained</a>, or just send us a photo.</p>

<h2>Fire-rated doors: keep the door intact</h2>
<p>HDB says its fire-rated entrance doors are fitted with a door closer, a self-closing device that keeps the door shut in a fire, and that you shouldn't remove it. When we change a lock, we choose one that suits your door's existing cut-out, so we don't weaken the door. If the old lock left extra holes, a stainless cover plate hides them neatly. Fitting a digital lock on a fire-rated door? Since 1 March 2024, SCDF requires it to be certified: see <a href="~/guides/digital-lock-fire-rated-door-scdf/">digital locks on fire-rated doors</a>.</p>

<h2>How it works</h2>
<ol>
<li><strong>WhatsApp photos</strong> of the lock (outside, inside and the door edge) to {PHONE}.</li>
<li><strong>Get the price first</strong>, including the lock and installation.</li>
<li><strong>We come to you</strong> and fit the new lock.</li>
<li><strong>We test it with you</strong> and hand over the new keys. Every old key stops working.</li>
</ol>

<div class="callout navy"><p><strong>Our warranty:</strong> every lock replacement and installation comes with our warranty, with no expiry date.</p></div>

<h2>Locked out with a broken lock?</h2>
<p>We open the door first, then replace the lock in the same visit if it needs it. We don't repair locks: a faulty lock is replaced, so the problem doesn't come back. See <a href="~/emergency-locksmith/">emergency locksmith</a>.</p>
""",
 faqs=[
  ("How much does it cost to change an HDB main door lock?", "From {P_REPLACE}, including the new lock and installation, with a no-expiry warranty. The price depends on the lock you choose, and we confirm it before we come."),
  ("Will a new lock fit my HDB door's existing holes?", "We choose a lock that suits your door's cut-out. If the old lock left extra holes, a stainless cover plate hides them neatly."),
  ("Can you change the lock on a fire-rated HDB main door?", "Yes. We keep the door intact and leave the door closer in place. For digital locks on fire-rated doors, the lock must be SCDF-certified."),
  ("Do you repair HDB door locks?", "No. We replace faulty locks with new ones, which are more reliable and come with our no-expiry warranty."),
  ("Can you change the lock the same day?", "Often, yes. WhatsApp photos of your lock to {PHONE} and we'll tell you when we can come."),
 ],
),
# ----------------------------------------------------------------------
dict(
 path="hdb-gate-lock-replacement/", short="HDB gate lock replacement", icon="lock",
 card="Rusty, stiff or broken HDB gate lock? New gate lock from {P_REPLACE}, supply and installation, no-expiry warranty.",
 title="HDB Gate Lock Replacement Singapore | From S$100",
 title_exp="HDB Gate Lock Replacement & Change | Price Agreed First",
 desc="Rusty, stiff or broken HDB gate lock, or lost the key? New gate lock from S$100 including installation, with a no-expiry warranty. Digital gate locks too.",
 h1="HDB Gate Lock Replacement",
 sub="HDB gate locks face rain, corridor washing and daily slamming, so they wear out faster than door locks. Uncle Thomas replaces HDB gate locks across Singapore, mechanical or digital, with the price agreed first.",
 badges=["From {P_REPLACE}", "Mechanical or digital", "No-expiry warranty"],
 body="""
<p><strong>The short answer:</strong> an HDB gate lock change starts from {P_REPLACE}, including the new lock and installation. Send photos of your gate lock from both sides to {PHONE} for the exact price before we come.</p>

<h2>Signs your gate lock needs replacing</h2>
<ul>
<li><strong>Rust</strong> on the lock body or keyhole, or a key that grinds.</li>
<li><strong>The bolt doesn't slot in or pull back smoothly</strong>, so you have to lift or slam the gate to lock it.</li>
<li><strong>The handle is loose</strong>, or the lock moves when you push it.</li>
<li><strong>Keys lost</strong>, or you've just moved in.</li>
<li><strong>A padlock you no longer trust</strong>, or a hasp that's bent.</li>
</ul>

<h2>HDB gate locks we fit</h2>
<ul>
<li><strong>Gate locksets and rim gate locks</strong> with a key outside and a knob or key inside.</li>
<li><strong>Hook bolts</strong>, which hook into the frame and resist the gate being lifted.</li>
<li><strong>Digital gate locks</strong>, opened with PIN, fingerprint or card, often matched to your door lock. See <a href="~/guides/smart-lock-for-hdb-gate/">choosing a smart lock for your HDB gate</a>.</li>
</ul>
<p>Comparing options? Read <a href="~/guides/hdb-gate-lock-types/">HDB gate lock types</a>.</p>

<h2>Built for Singapore's weather</h2>
<p>Gate locks sit in the corridor, so we look for locks and finishes that cope with rain and humidity. Wipe the keypad dry after heavy rain or corridor washing, and change digital gate lock batteries together with the door lock's.</p>

<h2>How it works</h2>
<ol>
<li><strong>WhatsApp photos</strong> of the gate lock from both sides to {PHONE}.</li>
<li><strong>Get the price first</strong>, including the lock and installation.</li>
<li><strong>We fit the new lock</strong>, check the bolt lines up with the frame, and hand over new keys.</li>
</ol>

<div class="callout navy"><p><strong>Our warranty:</strong> every lock replacement and installation comes with our warranty, with no expiry date.</p></div>

<p>Changing the main door lock too? See <a href="~/hdb-main-door-lock-replacement/">HDB main door lock replacement</a>.</p>
""",
 faqs=[
  ("How much does it cost to replace an HDB gate lock?", "From {P_REPLACE}, including the new lock and installation, with a no-expiry warranty. We confirm the price from photos before we come."),
  ("Can you put a digital lock on my HDB gate?", "Yes. We install digital gate locks of every brand, and can match them to your door lock."),
  ("My gate lock is rusty and hard to turn. Can you repair it?", "We don't repair locks. A rusty gate lock is best replaced, so it doesn't jam with you outside."),
  ("Why won't my HDB gate bolt slot in properly?", "Often the gate has dropped slightly on its hinges, so the bolt no longer lines up. If the lock itself is worn, replacing it fixes the problem."),
 ],
),
# ----------------------------------------------------------------------
dict(
 path="car-key-duplicate/", short="Car key duplicate", icon="car",
 card="Down to one car key? We clone a spare key fob for all major car brands from your working key.",
 title="Car Key Duplicate Singapore | Spare Key Fob Cloning",
 title_exp="Car Key Duplicate & Spare Key Fob Singapore | All Brands",
 desc="Need a spare or duplicate car key in Singapore? We clone key fobs for all major car brands from your working key, after checking ID against the log card.",
 h1="Car Key Duplicate: Spare Key Fob Cloning in Singapore",
 sub="Bought a used car with one key, or worried about losing your only fob? Uncle Thomas clones a spare key fob from your working key, for all major car brands, without a trip to the dealer.",
 badges=["All major brands", "From your working key", "ID checked"],
 body="""
<p><strong>The short answer:</strong> if you still have one working key, we can clone a spare key fob for all major car brands. WhatsApp {PHONE} the car's make, model, year and a photo of your key, and we'll confirm and quote before you book.</p>

<h2>Duplicate vs replacement: which do you need?</h2>
<table class="price-table info-table"><thead><tr><th scope="col">Your situation</th><th scope="col">What you need</th><th scope="col">Who can help</th></tr></thead><tbody>
<tr><td>You have one working key and want a spare</td><td>A duplicate (cloned) key fob</td><td>Us: we clone it from your working key.</td></tr>
<tr><td>Your key works but the remote buttons don't</td><td>Usually just a new battery</td><td>See <a href="~/guides/car-key-fob-not-working/">key fob not working</a>.</td></tr>
<tr><td>Every key is lost or dead</td><td>A replacement key programmed to the car</td><td>Usually the dealer. If you're locked out meanwhile, we can open the car.</td></tr>
</tbody></table>

<h2>Why get a spare now</h2>
<ul>
<li><strong>Used cars often come with one key.</strong> Losing it can mean days off the road.</li>
<li><strong>Private-hire and delivery drivers</strong> lose earnings for every day without the car.</li>
<li><strong>A spare costs far less while you still have a working key</strong> than replacing every key after they're lost.</li>
</ul>

<h2>What we need</h2>
<ol>
<li><strong>Your working key</strong> and the car.</li>
<li><strong>Your NRIC and the car's log card.</strong> We check they match before cloning any key: it protects you, and every car owner.</li>
<li><strong>The make, model and year</strong>, sent first on WhatsApp with a photo of the key, so we can confirm we can clone it.</li>
</ol>

<h2>Brands we clone</h2>
<p>All major car brands. Brand guides with key fob battery, spare key and lockout help:</p>
{CAR_BRAND_LINKS}

<h2>We don't cut house keys</h2>
<p>Car key fob cloning is the one key service we offer. We don't duplicate or cut house, gate or letterbox keys: if those are lost, we <a href="~/lock-replacement/">replace the lock</a> and give you new keys.</p>
""",
 faqs=[
  ("Can you duplicate a car key in Singapore without going to the dealer?", "Yes, if you have a working key. We clone key fobs for all major car brands after checking your NRIC against the log card."),
  ("How much is a spare car key in Singapore?", "It depends on the make, model and key type, so it's quoted per car. WhatsApp {PHONE} the details and a photo of the key."),
  ("I lost all my car keys. Can you make a new one?", "We clone from a working key. If every key is lost, the dealer is usually the route. If you're locked out meanwhile, we can open the car without damage."),
  ("Which car brands can you clone keys for?", "All major car brands. Send us the make, model, year and a photo of the key to confirm."),
  ("Do you cut house keys?", "No. Car key fob cloning is our only key service. For lost house keys, we replace the lock."),
 ],
),
]

RELATED = {
 "hdb-main-door-lock-replacement/": ["hdb-gate-lock-replacement/", "lock-replacement/", "digital-lock-installation/", "emergency-locksmith/", "letterbox-lock-replacement/", "digital-lock-opening/"],
 "hdb-gate-lock-replacement/": ["hdb-main-door-lock-replacement/", "lock-replacement/", "digital-lock-installation/", "emergency-locksmith/", "letterbox-lock-replacement/", "digital-lock-opening/"],
 "car-key-duplicate/": ["car-locksmith/", "emergency-locksmith/", "lock-replacement/", "digital-lock-opening/", "safe-opening/", "commercial-locksmith/"],
}

# ----------------------------------------------------------------------
# Added 29 Oct 2026 after the owner confirmed: broken key extraction, padlock
# opening/cutting, roller shutter locks, glass and sliding door locks, and
# cabinet, drawer and locker locks.
NICHE_SERVICES += [
dict(
 path="broken-key-extraction/", short="Broken key extraction", icon="key",
 card="Key snapped in the lock? We take the broken piece out and, if the lock is damaged, replace it.",
 title="Broken Key Extraction Singapore | Key Stuck or Snapped",
 title_exp="Key Broken or Stuck in Lock? Extraction Singapore 24/7",
 desc="Key broken or stuck in the lock? Uncle Thomas removes snapped keys from door, gate, letterbox, padlock and cabinet locks, 24/7 islandwide. Call 9224 9224.",
 h1="Key Broken or Stuck in the Lock? Broken Key Extraction",
 sub="A key that snaps inside the lock usually happens at the worst time: at the gate, late at night, in the rain. Uncle Thomas removes broken keys from door, gate, letterbox, padlock and cabinet locks, 24/7.",
 badges=["24/7 islandwide", "Door, gate & letterbox", "Price agreed first"],
 body="""
<p><strong>The short answer:</strong> stop using the lock, don't push the broken piece further in, and keep the other half of the key. Call or WhatsApp {PHONE}: we take the broken piece out, and if the lock was damaged, we replace it in the same visit.</p>

<h2>Key broken in the lock: what to do right now</h2>
<ol>
<li><strong>Stop turning and don't insert anything else.</strong> Pushing the spare key or another object in can drive the broken piece deeper.</li>
<li><strong>Keep the other half of the key.</strong> It shows what the key looked like.</li>
<li><strong>If a piece is sticking out</strong> and you can grip it with tweezers, try one gentle, straight pull. If it doesn't come, stop.</li>
<li><strong>Don't use glue.</strong> Superglue on a stick or the key stub usually ends up gluing the lock itself.</li>
<li><strong>Is the door locked or unlocked?</strong> If you're locked out, tell us: we'll open the door and remove the key in one visit.</li>
</ol>

<h2>Key stuck (not broken) in the lock?</h2>
<p>A key that goes in but won't turn or come out is often caught on a worn pin or a door that has dropped. Push the door firmly towards the frame, keep the key straight, and wiggle it gently while pulling. Don't use pliers: that's how keys snap. More causes in <a href="~/guides/door-lock-jammed/">door lock jammed</a>.</p>

<h2>Locks we extract broken keys from</h2>
<ul>
<li>HDB and condo <strong>main door locks</strong> and <strong>gate locks</strong>.</li>
<li><strong>Letterbox locks</strong>.</li>
<li><strong>Padlocks</strong> on gates, shutters and storerooms.</li>
<li><strong>Cabinet, drawer and locker locks</strong> in homes and offices.</li>
<li><strong>Office and shop locks</strong>, including shutter locks.</li>
</ul>

<h2>After the key is out</h2>
<p>If the lock still works, you're done. If the lock was worn enough to snap a key, or was damaged in the process, we replace it rather than repair it, so it doesn't happen again. Every replacement comes with our no-expiry warranty. See <a href="~/lock-replacement/">lock replacement</a>. We don't cut new keys: if you've no working key left, the lock is replaced and you get a new set.</p>

<h2>Why keys snap</h2>
<ul>
<li><strong>Worn keys</strong>, especially copies made from copies.</li>
<li><strong>Stiff locks</strong>: rust or dirt, common on gate locks exposed to rain.</li>
<li><strong>Forcing a key</strong> when the bolt is rubbing on the frame.</li>
</ul>
""",
 faqs=[
  ("How do I get a broken key out of a lock?", "If a piece sticks out, try one gentle, straight pull with tweezers. Otherwise stop: pushing anything else in drives it deeper. Call a locksmith to extract it."),
  ("Can I still use the lock after a key breaks in it?", "Not until the piece is out. If the lock is damaged or worn, it's best replaced."),
  ("Can you make a new key from the broken key?", "We don't cut keys. If you have no working key left, we replace the lock and give you a new set."),
  ("How much does broken key extraction cost?", "It depends on the lock and whether it needs replacing. WhatsApp a photo of the lock to {PHONE} and we'll confirm the price before we come."),
  ("My key broke in the lock and I'm locked out. Can you help?", "Yes, 24/7. We open the door, remove the broken key and replace the lock in the same visit if needed."),
 ],
),
dict(
 path="padlock-cutting/", short="Padlock cutting & removal", icon="lock",
 card="Lost the padlock key or forgot the combination? We open or cut padlocks on gates, shutters and storerooms.",
 title="Padlock Cutting & Removal Singapore | Lost Key or Code",
 title_exp="Padlock Cut or Opened in Singapore | Gates & Shutters",
 desc="Lost your padlock key or forgot the combination? We open or cut padlocks on HDB gates, shop shutters, storerooms and lockers, after checking ownership. 24/7.",
 h1="Padlock Cutting and Removal in Singapore",
 sub="Lost the key to the padlock on your gate, shop shutter or storeroom, or forgot the code? Uncle Thomas opens or cuts padlocks across Singapore, after checking that it's yours.",
 badges=["Gates, shutters & storerooms", "Ownership checked", "24/7 islandwide"],
 body="""
<p><strong>The short answer:</strong> WhatsApp {PHONE} a photo of the padlock and where it's fitted. We'll check it's yours, then open it or cut it off, and can fit a new padlock or lock if you need one.</p>

<h2>Padlocks we deal with</h2>
<ul>
<li><strong>HDB gate padlocks</strong> and padlocks on gate hasps.</li>
<li><strong>Shop shutter padlocks</strong>, often used at the base of roller shutters. See <a href="~/roller-shutter-lock/">roller shutter locks</a>.</li>
<li><strong>Storeroom, bomb shelter and service-yard padlocks.</strong></li>
<li><strong>Locker padlocks</strong> at offices, gyms and schools (with the owner's or management's permission).</li>
<li><strong>Combination padlocks</strong> with a forgotten code.</li>
</ul>

<h2>Open or cut?</h2>
<p>Where we can open a padlock without damage, we do. Some padlocks are built to resist cutting: closed-shackle (shrouded) and disc padlocks, and hardened steel shackles, take specialist tools. Either way, we agree the approach and the price before we start.</p>

<h2>Why we check ownership</h2>
<p>Padlocks protect gates, shops and storerooms, so we always confirm you're entitled to open the one in front of us: for example proof of residence for an HDB gate, or authorisation from the business or building management. A locksmith who cuts any padlock without asking is a risk to everyone.</p>

<h2>Replacing a padlock?</h2>
<p>For gates and shutters, a closed-shackle padlock is harder to cut than an open one. For HDB gates, a proper gate lock is often more convenient than a padlock: see <a href="~/hdb-gate-lock-replacement/">HDB gate lock replacement</a> and <a href="~/guides/hdb-gate-lock-types/">HDB gate lock types</a>.</p>
<p>Key snapped inside the padlock? See <a href="~/broken-key-extraction/">broken key extraction</a>.</p>
""",
 faqs=[
  ("Can you cut a padlock off my HDB gate?", "Yes, after checking proof that you live there. We open it without damage where we can, or cut it off."),
  ("I forgot my combination padlock code. Can you open it?", "Yes. We open or remove combination padlocks once we've confirmed they're yours."),
  ("Can every padlock be cut?", "Most can, but closed-shackle, disc and hardened padlocks need specialist tools. We agree the approach and price first."),
  ("How much does padlock cutting cost?", "It depends on the padlock and where it's fitted. Send a photo to {PHONE} for a price before we come."),
 ],
),
dict(
 path="roller-shutter-lock/", short="Roller shutter locks", icon="building",
 card="Shop shutter won't unlock, or the key is lost? We open roller shutter locks and fit new ones.",
 title="Roller Shutter Lock Singapore | Shop Shutter Opening 24/7",
 title_exp="Roller Shutter Lock Replacement & Opening | Singapore",
 desc="Shop roller shutter locked and the key lost, snapped or stuck? We open roller shutter locks and padlocks and fit new shutter locks, 24/7 islandwide.",
 h1="Roller Shutter Lock Opening and Replacement",
 sub="A shutter that won't unlock means a shop that can't open. Uncle Thomas opens roller shutter locks and padlocks, and fits new shutter locks, before opening hours or after closing.",
 badges=["24/7, before opening", "Shutter locks & padlocks", "Invoices for businesses"],
 body="""
<p><strong>The short answer:</strong> if your shop shutter is locked and the key is lost, snapped or won't turn, call or WhatsApp {PHONE}. We open the shutter lock or padlock and can fit a new lock in the same visit, with authorisation from the business checked first.</p>

<h2>Shutter lock problems we handle</h2>
<ul>
<li><strong>Lost shutter key</strong>, or a staff member left with it.</li>
<li><strong>Key snapped or stuck</strong> in the shutter lock. See <a href="~/broken-key-extraction/">broken key extraction</a>.</li>
<li><strong>Lock rusted or seized</strong>, common on shutters exposed to rain.</li>
<li><strong>Padlocks at the base of the shutter</strong> with a lost key. See <a href="~/padlock-cutting/">padlock cutting</a>.</li>
<li><strong>Changing the lock</strong> after a staff change or a break-in attempt.</li>
</ul>

<h2>Locks, not motors</h2>
<p>We deal with the <strong>locks</strong> on roller shutters: centre locks, side locks, bolts and padlocks. If the shutter itself is damaged, off its track or the motor has failed, you'll need a roller shutter company for that part. We can still get it unlocked first.</p>

<h2>For businesses</h2>
<ul>
<li><strong>Before opening hours or after closing:</strong> we work 24/7, including weekends and public holidays.</li>
<li><strong>Authorisation first:</strong> we confirm the request comes from the business or the unit's owner.</li>
<li><strong>Invoices issued</strong> to the company.</li>
<li><strong>Price agreed first</strong>, from photos of the lock.</li>
</ul>
<p>Office doors, glass doors and cabinets too? See <a href="~/commercial-locksmith/">commercial locksmith</a>.</p>
""",
 faqs=[
  ("Can you open a roller shutter if we lost the key?", "Yes. We open the shutter lock or padlock after confirming you're authorised, and can fit a new lock."),
  ("Do you repair roller shutter motors?", "No. We handle the locks on shutters. For motors, springs or a shutter off its track, you'll need a roller shutter company."),
  ("Can you come before our shop opens?", "Yes. We work 24/7, including early mornings, weekends and public holidays."),
  ("Do you issue invoices?", "Yes, for business jobs."),
 ],
),
dict(
 path="glass-door-lock/", short="Glass & sliding door locks", icon="door",
 card="Glass office door or sliding door won't lock or open? We open and replace glass door and sliding door locks.",
 title="Glass Door & Sliding Door Lock Singapore | Open & Replace",
 title_exp="Glass Door Lock & Sliding Door Lock Replacement Singapore",
 desc="Glass door or sliding door lock stuck, broken or key lost? We open and replace glass door locks for offices and shops, and sliding door locks for homes, 24/7.",
 h1="Glass Door and Sliding Door Locks: Opening and Replacement",
 sub="Frameless glass doors at offices and shops, and sliding doors at home, use their own kinds of locks. Uncle Thomas opens them when they're stuck and replaces them when they fail.",
 badges=["Offices, shops & homes", "Price agreed first", "No-expiry warranty"],
 body="""
<p><strong>The short answer:</strong> WhatsApp {PHONE} a photo of the lock and the door. We'll tell you how we'd open or replace it and the price before we come. Every replacement lock comes with our no-expiry warranty.</p>

<h2>Glass door locks</h2>
<p>Frameless glass doors at offices, shops and clinics usually lock in one of these ways:</p>
<ul>
<li><strong>Patch locks</strong> clamped to the bottom or top corner of the glass, locking into the floor or frame.</li>
<li><strong>Locks in the door rail</strong> on framed glass doors.</li>
<li><strong>Locking handles</strong> on double glass doors, which tie the two handles together.</li>
</ul>
<p>Common problems are a lost key, a staff member leaving with one, a key that won't turn, or a bolt that no longer lines up after the door has shifted. We open the door, and replace the lock if it's worn or the keys can't be accounted for.</p>

<h2>Sliding door locks</h2>
<p>Sliding doors to balconies, patios and shop fronts use hook locks and latches built into the frame. Over time they stop catching, the key stops turning, or the door locks and won't release. We open stuck sliding doors and replace the lock or latch.</p>

<h2>Why replace, not repair</h2>
<p>We don't repair locks. A worn glass door or sliding door lock is replaced with a new one, so the problem doesn't come back, with our no-expiry warranty.</p>

<h2>For businesses</h2>
<p>We work 24/7 so you can open on time, confirm authorisation from the business first, and issue invoices. See <a href="~/commercial-locksmith/">commercial locksmith</a>.</p>
""",
 faqs=[
  ("Can you change the lock on a glass office door?", "Yes. We replace glass door patch locks, rail locks and locking handles, after confirming authorisation from the business."),
  ("My sliding door won't lock any more. Can you fix it?", "We replace worn sliding door locks and latches rather than repair them, with our no-expiry warranty."),
  ("We lost the key to our glass shop door. Can you open it?", "Yes, 24/7. We open it and can replace the lock so the lost key no longer works."),
  ("How much does a glass door lock replacement cost?", "It depends on the lock type. WhatsApp a photo of the lock and door to {PHONE} for a price before we come."),
 ],
),
dict(
 path="cabinet-lock/", short="Cabinet, drawer & locker locks", icon="key",
 card="Lost the key to a cabinet, drawer or locker? We open it and fit a new lock with new keys.",
 title="Cabinet, Drawer & Locker Lock Singapore | Open & Replace",
 title_exp="Lost Cabinet or Locker Key? Lock Opening & Replacement SG",
 desc="Lost the key to a filing cabinet, drawer, wardrobe or locker? We open cabinet, drawer and locker locks and fit new ones with new keys, for homes and offices.",
 h1="Cabinet, Drawer and Locker Locks: Opening and Replacement",
 sub="A filing cabinet nobody can open, a desk drawer with the key gone, or a locker with a lost key: Uncle Thomas opens cabinet, drawer and locker locks and fits new locks with new keys.",
 badges=["Homes & offices", "New lock, new keys", "Price agreed first"],
 body="""
<p><strong>The short answer:</strong> WhatsApp {PHONE} a photo of the lock and the furniture. We open it with as little damage as possible and fit a new lock with new keys, so the lost key no longer works.</p>

<h2>Locks we open and replace</h2>
<ul>
<li><strong>Filing cabinets</strong> and office pedestals.</li>
<li><strong>Desk and drawer locks</strong>.</li>
<li><strong>Wardrobe and cupboard locks</strong>.</li>
<li><strong>Staff lockers</strong> at offices, gyms and schools, with management's permission.</li>
<li><strong>Display cabinets</strong> in shops.</li>
<li><strong>Key cabinets and cash drawers</strong>.</li>
</ul>
<p>Many of these use small cam locks or plunger locks, which can be swapped for a new lock with new keys. For a heavier cabinet that's really a safe, see <a href="~/safe-opening/">safe opening</a>.</p>

<h2>We don't cut keys</h2>
<p>We don't duplicate or cut keys. If a cabinet key is lost, we replace the lock and give you a new set, which is also more secure: the lost key stops working.</p>

<h2>For offices</h2>
<ul>
<li><strong>Staff turnover:</strong> change cabinet and locker locks when keys can't be accounted for.</li>
<li><strong>Several locks at once:</strong> send photos of each and we'll quote them together.</li>
<li><strong>Authorisation and invoices:</strong> we confirm the request comes from the business, and issue invoices.</li>
</ul>
<p>Key snapped in a cabinet lock? See <a href="~/broken-key-extraction/">broken key extraction</a>. Office doors too? See <a href="~/commercial-locksmith/">commercial locksmith</a>.</p>
""",
 faqs=[
  ("I lost my filing cabinet key. Can you open it?", "Yes. We open it and fit a new lock with new keys, after confirming it's yours or your company's."),
  ("Can you make a duplicate cabinet key?", "No, we don't cut keys. We replace the lock and give you a new set."),
  ("Can you open a locker without the key?", "Yes, with permission from the locker's owner or the building's management."),
  ("How much does it cost to replace a cabinet lock?", "It depends on the lock. WhatsApp photos to {PHONE}; for several locks we'll quote them together."),
 ],
),
]

RELATED.update({
 "broken-key-extraction/": ["emergency-locksmith/", "lock-replacement/", "hdb-gate-lock-replacement/", "padlock-cutting/", "cabinet-lock/", "letterbox-lock-replacement/"],
 "padlock-cutting/": ["hdb-gate-lock-replacement/", "roller-shutter-lock/", "broken-key-extraction/", "lock-replacement/", "commercial-locksmith/", "emergency-locksmith/"],
 "roller-shutter-lock/": ["commercial-locksmith/", "padlock-cutting/", "broken-key-extraction/", "glass-door-lock/", "commercial-safe-services/", "cabinet-lock/"],
 "glass-door-lock/": ["commercial-locksmith/", "roller-shutter-lock/", "lock-replacement/", "cabinet-lock/", "emergency-locksmith/", "digital-lock-installation/"],
 "cabinet-lock/": ["commercial-locksmith/", "broken-key-extraction/", "safe-opening/", "glass-door-lock/", "lock-replacement/", "padlock-cutting/"],
})
