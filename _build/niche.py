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
