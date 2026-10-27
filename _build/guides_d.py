"""Guides added 27 Oct 2026 (round 2): keys locked in a car, forgotten digital
lock PIN, and digital locks on fire-rated doors (SCDF rule).
Facts checked against SCDF, HDB and LTA/OneMotoring sources on 27 Oct 2026."""
import config as C
from cars import slug as car_slug
from brands import _slug as lock_slug

_CAR_LINKS = ", ".join(f'<a href="~/car-locksmith/{car_slug(b)}/">{b}</a>' for b in C.CAR_BRAND_PAGES)
_LOCK_LINKS = ", ".join(f'<a href="~/digital-lock-opening/{lock_slug(b)}/">{b}</a>' for b in C.BRAND_PAGES)

GUIDES_D = [
# ----------------------------------------------------------------------
dict(
 slug="keys-locked-in-car",
 short="Keys locked in car",
 title="Keys Locked in Car in Singapore? What to Do Now (2026)",
 desc="Locked your keys in the car in Singapore? What to check first, when to call 995, what not to try, and how a locksmith opens it without damage. From S$100.",
 h1="Locked Your Keys in the Car? What to Do in Singapore",
 card="Someone inside? Call 995. Everyone safe? Two quick checks, what never to try, and how to get back in without a scratch.",
 body="""
<p>It happens to careful people. You put the key down to lift the shopping into the boot, close the lid, and hear the doors lock. Or a child presses the lock button while the key sits in the cup holder. Many modern cars lock themselves automatically, so a key left inside is now one of the most common reasons drivers in Singapore call a locksmith.</p>
<p>Here's what to do, in the right order.</p>

<h2>1. Is anyone, or any pet, inside the car?</h2>
<p>If a child, an elderly person or a pet is locked inside, <strong>call 995 immediately</strong>. Don't wait for a locksmith or for someone to bring a spare key. A parked car in Singapore heats up fast, and children are far more vulnerable to heat than adults.</p>
<p>SCDF will break a window to get a child out if it has to. In June 2022, officers <a href="https://mustsharenews.com/boy-trapped-tiong-bahru/" target="_blank" rel="noopener">smashed a rear window in Tiong Bahru</a> to rescue a one-year-old boy after the car locked itself with the keys inside. A window can be replaced. While you wait, stay by the car where the child can see you, and try to shade it if you can.</p>

<h2>2. If everyone is safe: two quick checks</h2>
<ul>
<li><strong>Try every door and the boot.</strong> It sounds obvious, but in a hurry people try the driver's door twice and forget the others. On some cars, the boot or a rear door stays unlocked.</li>
<li><strong>Is there a spare key?</strong> If it's at home and someone can bring it, that may be the cheapest fix. If home is across the island, a locksmith is often faster.</li>
</ul>
<p>Some newer cars can be unlocked with a phone app or a digital key, but only if you set it up beforehand and your phone isn't the thing locked in the car.</p>

<h2>3. What not to try</h2>
<p>Online videos make it look easy with a wire hanger or a ruler. On a modern car it rarely is, and it's easy to cause damage that costs more than the call-out:</p>
<ul>
<li><strong>Bent hangers and rulers</strong> tear the rubber window seals and scratch the paint. Inside the door, they can snag wiring or the window mechanism.</li>
<li><strong>Prying the door frame</strong> can bend it, so it never seals properly again. That means wind noise, and water getting in during the next downpour.</li>
<li><strong>Breaking a window</strong> is a last resort for emergencies only. Side and rear glass is expensive and can take days to replace, and you can't leave the car unlocked overnight.</li>
</ul>

<h2>4. Who to call</h2>
<ul>
<li><strong>Your insurer's roadside assistance.</strong> Some motor policies include locksmith help, but <a href="https://www.singsaver.com.sg/car-insurance/blog/roadside-assistance" target="_blank" rel="noopener">coverage varies by provider</a>. Check your policy or call the hotline and ask.</li>
<li><strong>Your dealer.</strong> Useful if you've lost every key, but a dealer can't usually get you into a locked car tonight.</li>
<li><strong>A car locksmith.</strong> The quickest route for a simple lockout. Uncle Thomas opens cars of all major brands 24/7 with non-destructive tools, from <strong>{P_CAR}</strong>, with the price agreed before we set off.</li>
</ul>

<h2>5. Have these ready</h2>
<ul>
<li><strong>Where you are:</strong> the carpark name, deck or level, and lot number. In a basement, send your location on WhatsApp before you go back down, because the signal there is often weak.</li>
<li><strong>Your car:</strong> make, model and year.</li>
<li><strong>Proof the car is yours:</strong> your NRIC plus the vehicle registration details. If the papers are in the car, you can pull up the log card on your phone through <a href="https://www.motorist.sg/article/2951/the-motorist-guide-to-the-lta-log-card-2026-edition" target="_blank" rel="noopener">OneMotoring with Singpass</a>. We check this before we open any car. It protects you, because it means nobody can use a locksmith to get into your car.</li>
<li><strong>Company, rental or private-hire car:</strong> written permission from the company or owner, by WhatsApp or email.</li>
</ul>

<h2>6. How we open it</h2>
<p>We use specialist car-opening tools that work through the door's natural gaps without forcing the frame, cutting seals or touching the glass. You'll see exactly what we're doing, and once the door is open, we check the key works and the car locks and unlocks normally before we leave.</p>

<h2>7. Make sure it doesn't happen again</h2>
<ul>
<li><strong>Get a spare key.</strong> A spare fob kept at home turns the next lockout into a short trip. We clone spare fobs for all major brands; see <a href="~/guides/lost-car-key-fob/">lost car key fob</a>.</li>
<li><strong>Keep the key on you while loading the boot.</strong> A pocket or lanyard beats the boot floor.</li>
<li><strong>Learn your car's hidden key.</strong> Most smart keys hide a mechanical key that opens the driver's door if the fob battery dies. Each brand page has the steps.</li>
</ul>
<p>Brand guides: """ + _CAR_LINKS + """, and <a href="~/car-locksmith/">all car brands</a>.</p>

<div class="callout navy"><p><strong>Locked out of your car now?</strong> Call or WhatsApp {PHONE} with your carpark and car model. 24/7, islandwide, from {P_CAR}, and the price is agreed before we set off.</p></div>
""",
 faqs=[
  ("Can SCDF or the police unlock my car?", "If a child, a vulnerable adult or a pet is trapped inside, call 995: SCDF will get them out, even if it means breaking a window. If everyone is safe and only the key is inside, it's a job for a locksmith."),
  ("Will a locksmith damage my car?", "Not if they use the right tools. We open cars without forcing the frame, cutting seals or breaking glass, and we check that everything works before we leave."),
  ("What proof do I need to get my car opened?", "Your NRIC and the vehicle's registration details. If the papers are inside the car, show us the log card on your phone through OneMotoring. For company or rental cars, we need the owner's permission."),
  ("Does car insurance pay for a locksmith?", "Some motor policies include roadside assistance that covers locksmith help, but it varies by insurer. Call your insurer's hotline and ask before you pay anyone."),
  ("How much does it cost to unlock a car in Singapore?", "With Uncle Thomas, car lockouts start from {P_CAR}. We tell you the price before we set off."),
 ],
),
# ----------------------------------------------------------------------
dict(
 slug="forgot-digital-lock-pin",
 short="Forgot digital lock PIN",
 title="Forgot Your Digital Lock PIN? How to Get Back In (2026)",
 desc="Forgot your digital or smart lock PIN? The ways back in to try first, why you shouldn't keep guessing, how a reset works, and when to call a locksmith.",
 h1="Forgot Your Digital Lock PIN? How to Get Back In",
 card="Fingerprint, card, app or backup key: the ways back in to try first, why guessing makes it worse, and how resets really work.",
 body="""
<p>You come back from a long trip, or you changed the code last month, and now your fingers hover over the keypad with nothing. Forgetting a digital lock PIN is common, and the good news is that a PIN is rarely the only way into a digital or smart lock. Here's what to try, in order, before anything gets damaged.</p>

<h2>Stop guessing after two tries</h2>
<p>Most digital locks freeze the keypad for a few minutes after several wrong codes, and some sound an alarm. Keep guessing and you lose time and annoy the neighbours, without getting closer. If you have a likely code, try it once, carefully. Then move on to the other ways in.</p>

<h2>Other ways in to try first</h2>
<ul>
<li><strong>Fingerprint.</strong> If anyone in the household enrolled a fingerprint, it still works when the PIN is forgotten. Dry your finger first; wet or sweaty fingers fail more often.</li>
<li><strong>Card or key tag.</strong> Many locks came with RFID cards or tags. Check your wallet, your bag and your car.</li>
<li><strong>The app.</strong> App-based smart locks can often be opened from the phone over Bluetooth or Wi-Fi. With some brands, such as Igloohome, the owner can create a new PIN from the app.</li>
<li><strong>The mechanical backup key.</strong> Many digital locks hide a keyhole behind a small cover. The key only helps if it's outside the flat, so this is a good moment to plan where to keep it next time.</li>
<li><strong>Family members.</strong> Someone else may have their own PIN or fingerprint registered. A phone call can save a call-out.</li>
</ul>

<h2>How a PIN reset actually works</h2>
<p>You can't reset a digital lock from outside, and that's deliberate: if you could, so could a burglar. On most models, the registration or reset button is on the inside unit, often under the battery cover. So the order is always: get in first, then change the code.</p>
<p>Once you're inside, there are two options:</p>
<ul>
<li><strong>Change the PIN</strong> using the master or admin code, the app, or the registration button, following your lock's manual. This keeps your fingerprints and cards.</li>
<li><strong>Factory reset.</strong> This wipes everything (PINs, fingerprints, cards) back to the default settings. Use it if you've lost track of who has access, then register everyone again.</li>
</ul>
<p>The brand's service centre can also help, but they'll usually ask for proof of purchase and may not come the same day.</p>

<h2>When to call a locksmith</h2>
<p>If you've tried the other ways in and you're still outside, call or WhatsApp {PHONE}. Uncle Thomas opens digital and smart locks of every brand, 24/7, without damage wherever possible, from <strong>{P_DIGITAL_OPEN}</strong>. We check proof of residence before opening. If your ID is inside, tell us, and we'll verify it with you once the door is open. Once you're in, we can show you how to set a new PIN on your model.</p>

<h2>So it doesn't happen again</h2>
<ul>
<li><strong>Register at least two ways in</strong>: a PIN plus a fingerprint, or a PIN plus a card.</li>
<li><strong>Store the PIN somewhere safe</strong>, such as your phone's password manager. Not on a sticky note on the fridge, and not as your birthday.</li>
<li><strong>Add a second admin</strong>, like a spouse or adult child, so one forgotten code never locks the whole family out.</li>
<li><strong>Use the scramble feature</strong> if your lock has one. Many locks let you type extra random digits before or after the real PIN, so smudges on the keypad don't give it away.</li>
<li><strong>Keep the backup key outside the flat</strong>, with a trusted relative or neighbour.</li>
</ul>
<p>Brand guides: """ + _LOCK_LINKS + """. If your lock is dead rather than forgotten, see <a href="~/guides/digital-lock-battery-dead/">digital lock battery dead</a>.</p>
""",
 faqs=[
  ("Can I reset my digital lock PIN from outside?", "No. On almost every model, the reset button is on the inside unit, so nobody can reset the lock from the corridor. Get in using another method or a locksmith, then reset it."),
  ("Will a factory reset delete my fingerprints?", "Usually, yes. A factory reset returns the lock to its default settings and removes all PINs, fingerprints and cards, so you'll need to register them again."),
  ("How many wrong PIN attempts before my digital lock locks?", "It depends on the model, but many locks freeze the keypad for a few minutes after several wrong codes. Try once more, carefully, then use another way in."),
  ("Can a locksmith open my digital lock without breaking it?", "In most cases, yes. We open digital and smart locks of every brand without damage wherever possible, from {P_DIGITAL_OPEN}, after checking proof of residence."),
 ],
),
# ----------------------------------------------------------------------
dict(
 slug="digital-lock-fire-rated-door-scdf",
 short="Digital locks on fire-rated doors",
 title="Digital Locks on Fire-Rated Doors: SCDF Rule Explained",
 desc="Installing a digital lock on an HDB or condo fire-rated door? What SCDF has required since 1 March 2024, how to read the certificate, and a buyer's checklist.",
 h1="Digital Locks on Fire-Rated Doors: The SCDF Rule Explained",
 card="Since March 2024, digital locks on fire doors must be fire-certified. How to check your door, read the certificate, and buy the right lock.",
 body="""
<p><strong>The short answer:</strong> since 1 March 2024, any digital lock installed on a fire-rated door in Singapore must be certified for fire resistance. Its rating must be at least the door's, and it must have a mechanical fail-safe. Before you buy, ask the seller for the lock's Certificate of Conformity and check it covers the exact model. Here's what that means in practice.</p>

<h2>Is your main door fire-rated?</h2>
<p>Many are. A fire-rated door is built to hold back fire and smoke for a set time, usually 30 or 60 minutes in homes, so neighbours along the corridor have time to get out. HDB's <a href="https://www.hdb.gov.sg/cs/infoweb/residential/living-in-an-hdb-flat/renovation/guidelines/building-works" target="_blank" rel="noopener">renovation guidelines</a> say a main entrance door along a fire escape route must be half-hour fire-rated, with a self-closing device and an accreditor's label.</p>
<p>To check yours:</p>
<ul>
<li><strong>Look for the label</strong> on the door edge, usually near the hinges. It shows the rating and a serial number.</li>
<li><strong>Look for a door closer</strong>, the arm at the top that pulls the door shut. HDB fits one to fire-rated entrance doors, and <a href="https://www.hdb.gov.sg/cs/infoweb/residential/living-in-an-hdb-flat/home-maintenance/home-care-guide/gate-and-door" target="_blank" rel="noopener">it must not be removed</a>.</li>
<li><strong>Still unsure?</strong> HDB residents can check with HDB. Condo residents can ask the management office.</li>
</ul>

<h2>What SCDF requires</h2>
<p>According to <a href="https://scdf.gov.sg/home/fire-safety/digital-locksets-on-fire-rated-doors" target="_blank" rel="noopener">SCDF's guidance on digital locksets</a>, from 1 March 2024 a digital lock installed on a fire door must be certified for fire resistance. It can be certified together with a particular door, or on its own. If you're adding a lock to the door you already have, choose one that's certified on its own.</p>

<h2>How to read the Certificate of Conformity</h2>
<p>Ask the seller for the Certificate of Conformity (CoC) before you pay. Check four things:</p>
<ol>
<li><strong>Brand and model:</strong> the exact model you're buying must be listed. A certificate for a "similar" model doesn't count.</li>
<li><strong>Fire rating:</strong> at least the door's rating. A 30-minute door can take a lock rated 30, 60 or 120 minutes; a 60-minute door needs 60 or more.</li>
<li><strong>Mechanical fail-safe:</strong> the door can still be opened mechanically if the battery dies. That matters in a fire.</li>
<li><strong>Test standard:</strong> SS 332 or EN 1634-1.</li>
</ol>
<p>SCDF says only three certification bodies can issue these certificates, and its sample certificates come from Element Testing Services, Setsco Services and TÜV SÜD PSB.</p>

<h2>What about the lock I already have?</h2>
<p>If your digital lock was installed on a fire door before 1 March 2024 and isn't certified, SCDF doesn't require you to replace it. It does encourage homeowners to switch to a certified lock, and the natural time is when the old one needs replacing anyway.</p>

<h2>What about my gate?</h2>
<p>This rule is about digital locks on fire doors. HDB describes the metal gate as a safety barrier and the main door as the fire safety barrier, so the certification question is about your main door. For gates, see our guide to <a href="~/guides/smart-lock-for-hdb-gate/">choosing a smart lock for your HDB gate</a>.</p>

<h2>Buying and installing: practical tips</h2>
<ul>
<li><strong>Be careful with very cheap online locks.</strong> Ask for the CoC before buying. If the seller can't produce one for the exact model, buy elsewhere.</li>
<li><strong>Keep the door intact.</strong> Avoid a lock that needs extra holes or a much bigger cut-out in your fire door. A certified lock that suits your door's existing cut-out is the better choice.</li>
<li><strong>Keep the certificate</strong> with your home documents, in case management or a future buyer asks.</li>
<li><strong>Know your fail-safe.</strong> Once it's fitted, learn how the mechanical override works, and where the backup key and emergency power point are.</li>
</ul>

<h2>How we help</h2>
<p>Uncle Thomas installs digital and smart locks of every brand on HDB, condo and landed home doors, from <strong>{P_DIGITAL_INSTALL}</strong> labour, with a no-expiry installation warranty. If you've bought a lock already, WhatsApp {PHONE} a photo of your door edge, the door's label and the lock's certificate, and we'll tell you whether it fits before you book. See <a href="~/digital-lock-installation/">digital and smart lock installation</a>.</p>
<p><em>This guide summarises public guidance from SCDF and HDB as of October 2026. Rules can change, so check the linked SCDF page for the latest requirements.</em></p>
""",
 faqs=[
  ("Do digital locks on HDB doors need SCDF certification?", "If the door is a fire door, yes. Since 1 March 2024, SCDF requires digital locks installed on fire doors to be certified for fire resistance, with a rating at least equal to the door's and a mechanical fail-safe."),
  ("Do I have to replace a digital lock I installed before March 2024?", "No. SCDF doesn't require existing uncertified locks on residential fire doors to be replaced, but it encourages homeowners to switch to a certified one."),
  ("How do I know if my main door is fire-rated?", "Look for a label on the door edge near the hinges, and a door closer at the top. HDB residents can also check with HDB, and condo residents with management."),
  ("What test standards should a fire-rated digital lock meet?", "SCDF lists SS 332 or EN 1634-1. Check the standard on the lock's Certificate of Conformity."),
 ],
),
]
