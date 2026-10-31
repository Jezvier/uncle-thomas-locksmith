"""
Page text for: home, services hub, each service page, prices, about.
Links use "~/" for the site root (converted to relative links at build time).
{PHONE}, {YEARS}, {P_LOCKOUT} etc. are replaced from config.TOKENS.
"""
import config as C
import icons

BRANDS = ", ".join(C.DIGITAL_LOCK_BRANDS)

ID_POLICY = ("For your security, we check ID before every job — your NRIC, Singpass or other ID proof — "
             "and proof of residence or ownership, for example NRIC with your address, a tenancy agreement or utility bill, or the car's log card.")
WARRANTY = "Every lock replacement and installation comes with our warranty — with no expiry date."
NO_REPAIR = ("We don't do lock repairs, key duplication or key cutting (the one exception is remote car key fobs, which we clone). "
             "If a lock is faulty, we open it and replace it, so the problem doesn't come back.")

# ======================================================================
# SERVICES
# ======================================================================
SERVICES = [
# ----------------------------------------------------------------------
dict(
 path="emergency-locksmith/", short="Emergency lockout", icon="door",
 card="Locked out of your HDB, condo, house or office? We get you back in — damage-free wherever possible.",
 title="Emergency Locksmith Singapore 24/7 | Trusted Since 1998",
 title_exp="Emergency Locksmith Singapore 24/7 | Trusted Since 1998",
 desc="Locked out? Uncle Thomas is Singapore's 24/7 emergency locksmith since 1998. HDB, condo, landed & office lockouts islandwide, damage-free first. Call 9224 9224.",
 h1="24/7 Emergency Locksmith in Singapore",
 sub="Locked out of your home or office? Call Uncle Thomas — day or night, weekends and public holidays. We set off as soon as you call and open your door damage-free wherever possible.",
 badges=["Since 1998", "24/7 islandwide", "We check ID before opening"],
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
<li><strong>HDB flats</strong> — main doors, metal gates, room doors and toilet doors locked from the inside. See <a href="~/guides/room-door-locked-from-inside/">room or toilet door locked from inside</a>.</li>
<li><strong>Condominiums</strong> — main doors, deadbolts and digital locks.</li>
<li><strong>Landed homes</strong> — main doors, gates and back doors.</li>
<li><strong>Offices and shops</strong> — office doors, glass doors, cabinets and roller shutters. See <a href="~/commercial-locksmith/">commercial locksmith</a>.</li>
<li><strong>Key snapped in the lock?</strong> See <a href="~/broken-key-extraction/">broken key extraction</a>.</li>
<li><strong>Digital lock or smart lock won't open?</strong> Flat battery, forgotten PIN or faulty keypad — see <a href="~/digital-lock-opening/">digital and smart lock opening</a>.</li>
<li><strong>Keys locked in the car, or need a spare key fob?</strong> See <a href="~/car-locksmith/">car locksmith</a>.</li>
</ul>

<h2>Damage-free first</h2>
<p>With {YEARS}+ years in the trade, Uncle Thomas opens most mechanical and digital locks without drilling or forcing the door. If a lock is badly worn or broken and can't be opened cleanly, we explain your options and the price <em>before</em> doing anything else. If the lock then needs changing, we can <a href="~/lock-replacement/">replace it on the spot</a> — and every replacement comes with our no-expiry warranty.</p>

<div class="callout"><p><strong>Why we ask for ID:</strong> {ID_POLICY} It protects you — a locksmith who opens any door without checking is a risk to everyone.</p></div>

<h2>How much does an emergency locksmith cost in Singapore?</h2>
<p>The price depends on the lock type, the time of day and whether a part needs replacing. We always confirm it with you before we start, and the price we agree is the price you pay. See the <a href="~/prices/">price list</a>.</p>

<h2>Islandwide, 24 hours a day</h2>
<p>We cover every part of Singapore, from <a href="~/areas/woodlands/">Woodlands</a> to <a href="~/areas/tampines/">Tampines</a> and <a href="~/areas/cbd-orchard/">Orchard</a> to <a href="~/areas/toa-payoh/">Toa Payoh</a>. See <a href="~/areas/">all the areas we serve</a>.</p>
<p>Not locked out yet but worried? Read our guide: <a href="~/guides/locked-out-of-hdb-flat/">locked out of your HDB flat — what to do</a>.</p>
""",
 faqs=[
  ("How fast can an emergency locksmith reach me?", "We set off as soon as you call, 24/7, and usually arrive within 25–30 minutes. Far areas and heavy traffic can take longer, and we'll give you an honest estimate on the phone."),
  ("Will you damage my door?", "We use damage-free methods wherever possible, and most lockouts are opened without any damage. If a lock can't be opened cleanly, we explain the options and price before doing anything."),
  ("What do I need to show before you open the door?", "Proof that you live there — for example your NRIC with the address, a tenancy agreement or a utility bill. This protects you and your home."),
  ("Do you charge more at night?", "Lockouts start from {P_LOCKOUT} from 9am to 6pm and from {P_AFTERHOURS} after hours, weekends and public holidays. You'll always know the price before we start."),
  ("Do you open locks for tenants?", "Yes — as long as you can show you live there, for example with a tenancy agreement or a letter with your name and the address."),
 ],
),
# ----------------------------------------------------------------------
dict(
 path="digital-lock-opening/", short="Digital & smart lock opening", icon="keypad",
 card="Flat battery, forgotten PIN or faulty keypad? We open all digital lock and smart lock brands, 24/7.",
 title="Digital & Smart Lock Opening Singapore 24/7 | All Brands",
 title_exp="Digital & Smart Lock Opening Singapore | All Brands Since 1998",
 desc="Locked out by your digital lock or smart lock? Flat battery, forgotten PIN or faulty keypad: Uncle Thomas opens all brands 24/7, damage-free. Call 9224 9224.",
 h1="Digital Lock or Smart Lock Won't Open? 24/7 Opening",
 sub="Flat battery, forgotten PIN, dead keypad, an app that won't connect, or a lock that just won't respond: Uncle Thomas has developed his own damage-free techniques for opening digital locks and smart locks of every brand.",
 badges=["All brands", "Damage-free first", "24/7 islandwide"],
 body="""
<h2>Common digital lock and smart lock problems we solve</h2>
<ul>
<li><strong>Battery went flat</strong> and the emergency power option didn't work.</li>
<li><strong>Forgotten PIN</strong> or fingerprint no longer recognised.</li>
<li><strong>Keypad dead or not lighting up</strong> — often after rain or a corridor wash.</li>
<li><strong>Lock jammed or motor not turning</strong>, even with the right code.</li>
<li><strong>Locked from the inside</strong> — privacy or double-lock mode left on.</li>
<li><strong>Lost the backup key</strong> for the mechanical override.</li>
<li><strong>Smart lock app offline</strong> or your phone is locked inside.</li>
<li><strong>Tenant moved out without handing over the code</strong>: landlords and agents call us to get back into the flat. We check proof of ownership first.</li>
</ul>
<p>Before you call, it's worth trying the quick checks in our guides: <a href="~/guides/digital-lock-battery-dead/">digital lock battery dead or not opening</a>, and <a href="~/guides/forgot-digital-lock-pin/">forgot your digital lock PIN</a>.</p>

<h2>Every digital and smart lock brand, including</h2>
<ul class="tags">""" + "".join(f"<li>{b}</li>" for b in C.DIGITAL_LOCK_BRANDS) + """<li>and more</li></ul>
<p>Main door locks, gate locks, rim locks and mortise digital locks — on HDB flats, condos, landed homes and offices.</p>
{BRAND_LINKS}

<h2>Uncle Thomas's own digital and smart lock techniques</h2>
<p>As Singapore homes moved from keys to keypads, Uncle Thomas kept learning. Over the years he has worked out his own damage-free ways to open faulty and locked digital locks, including lock picking the mechanical override — so in most cases you get back in <em>without</em> having to buy a new lock. Where a lock is truly beyond saving, we tell you honestly and can <a href="~/digital-lock-installation/">install a new one</a> on the spot.</p>

<div class="callout"><p>{NO_REPAIR} Searching for <strong>digital lock repair</strong>? Read <a href="~/guides/digital-lock-repair/">fix, replace or just get in</a> first.</p></div>

<h2>What it costs</h2>
<p>The price depends on the brand, model and fault. WhatsApp a photo of the lock (front and inside if possible) to {PHONE} and we'll give you a firm price before we come. See all <a href="~/prices/">prices</a>.</p>

<div class="callout"><p><strong>Security first:</strong> {ID_POLICY}</p></div>
""",
 faqs=[
  ("Can you open a digital lock without damaging it?", "In most cases, yes. Uncle Thomas has developed his own damage-free techniques. If a lock is completely broken we'll explain the options before doing anything."),
  ("Which digital lock and smart lock brands do you open?", "All brands — including " + ", ".join(C.DIGITAL_LOCK_BRANDS) + "."),
  ("My digital lock battery is flat. What should I do?", "Most digital locks have an emergency power point (often a 9V battery terminal) or a backup key. If those don't work, call or WhatsApp {PHONE} and we'll open it for you."),
  ("Do you repair digital locks?", "No — we don't do repairs. We open the lock, and if it's faulty we can replace it with a new one, covered by our no-expiry installation warranty."),
  ("Is a smart lock different from a digital lock?", "A smart lock is a digital lock that also connects to an app, Wi-Fi or a smart home hub. Both run on batteries and can lock you out in the same ways, and we open both."),
  ("How much does it cost to open a digital lock?", "From {P_DIGITAL_OPEN}. Send a photo on WhatsApp for an exact price before we come."),
 ],
),
# ----------------------------------------------------------------------
dict(
 path="digital-lock-installation/", short="Digital & smart lock installation", icon="wrench",
 card="Neat, correct digital and smart lock installation for HDB doors, gates, condos and offices, with a no-expiry warranty.",
 title="Digital & Smart Lock Installation Singapore | HDB & Condo",
 title_exp="Digital & Smart Lock Installation Singapore | No-Expiry Warranty",
 desc="Digital lock and smart lock installation for HDB doors & gates, condos and offices. All brands, set up with you, no-expiry warranty. Call 9224 9224.",
 h1="Digital Lock &amp; Smart Lock Installation in Singapore",
 sub="Thinking of going keyless? Uncle Thomas installs digital locks and smart locks of every brand on HDB main doors and gates, condo doors and offices — fitted properly, set up with you, and covered by a warranty that never expires.",
 badges=["Set up with you", "All brands", "No-expiry warranty"],
 body="""
<h2>Why installation matters</h2>
<p>Most digital lock problems we're called out for start with a poor installation — a misaligned strike plate, a cable pinched in the door, or a lock that doesn't suit the door. A digital lock is only as good as how it's fitted. With {YEARS}+ years of opening and fitting locks, Uncle Thomas knows exactly what makes a lock last in Singapore's humid weather.</p>

<h2>What we install</h2>
<ul>
<li><strong>HDB main door digital locks and smart locks</strong> — including replacing an old mechanical lock.</li>
<li><strong>HDB gate digital locks</strong> — rim and mortise types for metal gates.</li>
<li><strong>Condo and landed home locks</strong> — main doors, side doors and gates.</li>
<li><strong>Office and shop locks</strong> — keypad and card access for small businesses. See <a href="~/commercial-locksmith/">commercial locksmith</a>.</li>
</ul>
<p>We work with all brands, including """ + BRANDS + """. Bought your own lock online? We'll install it. Not sure which to get? Tell us your door and budget and we'll recommend one that fits.</p>

<h2>Fire-rated doors: the SCDF rule</h2>
<p>Many HDB main doors are fire-rated. Since 1 March 2024, <a href="https://scdf.gov.sg/home/fire-safety/digital-locksets-on-fire-rated-doors" target="_blank" rel="noopener">SCDF requires</a> any digital lock fitted on a fire door to be certified for fire resistance. Before you buy, check three things on the lock's Certificate of Conformity:</p>
<ul>
<li><strong>The exact brand and model</strong> you're buying is listed.</li>
<li><strong>Its fire rating is at least the door's</strong> (residential fire doors are usually 30 or 60 minutes).</li>
<li><strong>It has a mechanical fail-safe</strong>, so the door can still be opened if the battery dies.</li>
</ul>
<p>Not sure if your door is fire-rated? Look for a label near the hinges, or send us a photo and we'll help you check. Full details: <a href="~/guides/digital-lock-fire-rated-door-scdf/">digital locks on fire-rated doors</a>. Older locks fitted before March 2024 don't have to be replaced, but SCDF encourages switching to a certified one.</p>

<h2>How it works</h2>
<ol>
<li>WhatsApp {PHONE} a photo of your door (outside and inside edge) and the lock you want.</li>
<li>We confirm the lock fits and give you a fixed price.</li>
<li>We install, test every function, and set up your PIN, fingerprints and cards with you.</li>
<li>You get our <strong>no-expiry warranty</strong> on the installation.</li>
</ol>

<div class="callout navy"><p><strong>Our warranty:</strong> {WARRANTY}</p></div>

<h2>Price</h2>
<p>The total depends on the door, whether old locks need removing, and whether you supply the lock. See the full <a href="~/prices/">price list</a>.</p>
<p>Choosing a lock for your gate? Read <a href="~/guides/smart-lock-for-hdb-gate/">choosing a digital or smart lock for your HDB gate</a>. Locked out of a digital lock right now? Go to <a href="~/digital-lock-opening/">digital lock opening</a>.</p>
""",
 faqs=[
  ("Can I install a digital lock on my HDB main door?", "Yes. Digital locks are common on HDB main doors and gates. We check your door's thickness and existing cut-outs so the lock fits properly."),
  ("Does a digital lock on a fire-rated door need certification?", "Yes. Since 1 March 2024, SCDF requires digital locks on fire doors to be certified for fire resistance, rated at least as high as the door, with a mechanical fail-safe. Ask the seller for the Certificate of Conformity."),
  ("Can you install a lock I bought online?", "Yes. Send us a photo of the lock and your door first so we can confirm it will fit."),
  ("How long does installation take?", "Most installations are completed in one visit. We test every function and set up your codes and fingerprints before we leave."),
  ("Is there a warranty?", "Yes — every installation comes with our warranty, with no expiry date."),
  ("Do you repair digital locks?", "No, we don't do repairs. If an existing lock is faulty we can replace it with a new one."),
 ],
),
# ----------------------------------------------------------------------
dict(
 path="safe-opening/", short="Safe opening", icon="safe",
 card="Forgotten combination or faulty safe? Opened by a US-trained safesmith who has worked on ships and across Asia.",
 title="Safe Locksmith Singapore | Safe & Safe Box Opening 24/7",
 title_exp="Safe Locksmith Singapore | Safe Box Opening by a Safesmith",
 desc="Safe box forgot password, battery dead or lost key? A US-trained safe locksmith opens all safe types in Singapore, homes and businesses, 24/7. Call 9224 9224.",
 h1="Safe Locksmith Singapore: Safe and Safe Box Opening, 24/7",
 sub="Forgotten combination, lost key, dead keypad or a jammed bolt. Uncle Thomas trained in safesmithing in the United States and opens every type of safe, for homes, offices, pawnshops, banks and government agencies.",
 badges=["US-trained safesmith", "All safe types", "Discreet, 24/7"],
 body="""
<p><strong>The short answer:</strong> try fresh batteries and the override key first. If the safe still won't open, don't force it. Send photos of the safe to {PHONE}, and Uncle Thomas will tell you how he'd open it and the price before he comes. Some safes can be opened and stay fully usable. When a safe is faulty, it usually has to be drilled, precisely, at the right point, so the safe can often take a new lock afterwards.</p>

<h2>What is a safesmith?</h2>
<p>A <strong>safesmith</strong> is a locksmith who specialises in safes and vaults: opening locked safes, changing combinations, replacing safe locks and installing safes. Uncle Thomas Locksmith is a safesmith in Singapore: its founder, Uncle Thomas, trained in safesmithing in the United States and has opened safes since 1998 for homes, offices, pawnshops, banks and government agencies.</p>

<h2>Why a safesmith, not just a locksmith</h2>
<p>Opening a safe is a different skill from opening a door. Safes are built to resist forced entry, and many have hidden relockers that fire if the safe is attacked the wrong way. A wrong approach can make the job far harder or damage what's inside. Few locksmiths in Singapore have formal safe training. Uncle Thomas spent a year in the United States training in <strong>safesmithing</strong>, and has since opened safes for multinational companies, on board ships and cruise liners, and in Thailand, Malaysia, China and Hong Kong.</p>

<h2>Opening a safe without drilling</h2>
<p>Uncle Thomas is trained in <strong>safe manipulation</strong>: opening high-security Group 2M combination locks by feel and sound, with no drilling and no damage. A safe can take anywhere from 5 minutes to 5 hours, depending on the lock and its condition. When drilling is the only way in, it's done precisely, and about 90% of drilled safes can be repaired and used again.</p>

<h2>Who we open safes for</h2>
<ul>
<li><strong>Homes:</strong> HDB flats, condos and landed houses.</li>
<li><strong>Businesses:</strong> commercial offices, shops, pawnshops and banks. See <a href="~/commercial-safe-services/">commercial safe services</a>.</li>
<li><strong>Government ministries and agencies.</strong></li>
<li><strong>Ships and vessels</strong> in Singapore waters and overseas.</li>
</ul>

<h2>Safes we open</h2>
<p>Every type of safe, including:</p>
<ul>
<li><strong>Electronic keypad safes</strong>: the most common type in homes and hotels.</li>
<li><strong>Mechanical dial (combination) safes</strong>: older and higher-security safes.</li>
<li><strong>Key safes</strong>, including safes with lost or broken keys.</li>
<li><strong>Dual-control safes</strong> that need a code and a key, or two codes.</li>
<li><strong>Biometric (fingerprint) safes.</strong></li>
<li><strong>Hotel-style and wardrobe safes.</strong></li>
<li><strong>Cash, drop and deposit safes</strong> for shops and offices.</li>
<li><strong>Fire safes, filing safes and document safes.</strong></li>
<li><strong>Vault doors and strongroom doors.</strong></li>
<li><strong>Safes on ships.</strong></li>
</ul>

<h2>What's wrong with your safe?</h2>
<table class="price-table info-table"><thead><tr><th scope="col">What you see</th><th scope="col">Likely cause</th><th scope="col">Try this first</th></tr></thead><tbody>
<tr><td>Keypad is dead, no lights or beeps</td><td>Flat batteries, or a failed keypad</td><td>Change the batteries. Many safes have an external battery point under the keypad.</td></tr>
<tr><td>Keypad beeps and accepts the code, but the door won't open</td><td>Weak batteries, or a jammed bolt or motor</td><td>New batteries. Then gently ease the handle while entering the code. Don't force it.</td></tr>
<tr><td>Keypad flashes or locks you out after tries</td><td>Wrong-code lockout</td><td>Wait out the lockout (often several minutes), then try once, slowly.</td></tr>
<tr><td>Forgot the code or the dial combination</td><td>Code lost</td><td>Look for the override key and the paperwork. Check whether the maker can reset it with proof of ownership.</td></tr>
<tr><td>Lost the key or override key</td><td>Key missing</td><td>Check paperwork for a key number; some makers can supply a key with proof of ownership.</td></tr>
<tr><td>Dial turns stiffly, or spins freely</td><td>Worn or broken lock parts</td><td>Stop turning it. Forcing a dial can make the job much harder.</td></tr>
<tr><td>Inherited a safe and nobody knows the code</td><td>Code never passed on</td><td>Gather proof that you have the right to open it, such as being the executor or the property owner.</td></tr>
</tbody></table>
<p>For step-by-step help, read <a href="~/guides/forgot-safe-combination/">forgot your safe combination: what to do</a>.</p>

<h2>How we open your safe</h2>
<ol>
<li><strong>Send photos on WhatsApp</strong> to {PHONE}: the safe's front, the keypad or dial, the brand label, and roughly how big it is.</li>
<li><strong>Get the price first.</strong> We tell you the price and the likely method before we set off.</li>
<li><strong>Proof of ownership.</strong> We confirm the safe is yours, or that you're authorised by the business, before touching it.</li>
<li><strong>We open it the right way for that safe.</strong> Where the safe allows, it's opened without damage and stays usable. Where the lock has failed, we drill at a precise point, not through the door.</li>
<li><strong>Your options afterwards.</strong> A new code, a <a href="~/safe-combination-change/">replacement lock</a>, or advice on whether the safe is worth keeping.</li>
</ol>

<h2>Will my safe need to be drilled?</h2>
<p>It depends on the safe and what's wrong with it. A safe with a forgotten code or a lost key can often be opened and stays fully usable. A safe whose lock has <strong>failed</strong>, such as a dead keypad board, a broken motor or a jammed bolt, usually needs drilling, because the lock can no longer respond to any code. Professional drilling is precise: a small hole at a specific point to reach the lock, chosen to avoid the relockers. On many safes the lock can then be replaced, and the safe used again. We'll always explain this, and the price, before starting. Read more in <a href="~/guides/safe-drilling-explained/">does my safe need drilling?</a></p>

<h2 id="brands">Safe brands we open</h2>
<p>All makes. Brand guides with battery, override key and code-reset help:</p>
{SAFE_BRAND_PILLS}
<p>We also open """ + ", ".join(C.SAFE_BRANDS_MORE) + """ and every other make.</p>

<h2>Common safe box problems</h2>
<ul>
<li><a href="~/guides/forgot-safe-combination/">Safe box forgot password or combination</a></li>
<li><a href="~/guides/safe-box-battery-dead/">Safe box battery dead: how to open it</a></li>
<li><a href="~/guides/safe-wont-open-correct-code/">Safe won't open with the correct code</a></li>
<li><a href="~/guides/lost-safe-key/">Lost safe key or override key</a></li>
<li><a href="~/guides/safe-drilling-explained/">Does my safe need drilling?</a></li>
</ul>

<div class="callout"><p><strong>Proof of ownership:</strong> Before opening any safe we confirm it belongs to you or your business, for example a purchase receipt, company authorisation, or proof of residence where the safe is kept. A safesmith who opens any safe without checking is a risk to everyone. Jobs are handled discreetly.</p></div>

<h2>How much does safe opening cost?</h2>
<p>Safe opening is <strong>quoted per job</strong>, because it depends on the safe's make, size, lock type and fault. A small home keypad safe with a battery problem is a very different job from a heavy commercial safe with a failed dial lock. WhatsApp {PHONE} photos of the safe and we'll give you a price before we come. The price we agree is the price you pay. Businesses can get an invoice.</p>

<h2>More safe services</h2>
<ul>
<li><a href="~/safe-combination-change/">Safe combination change and safe lock replacement</a>.</li>
<li><a href="~/safe-installation/">Safe supply and installation</a>: we recommend, source and install the right safe.</li>
<li><a href="~/commercial-safe-services/">Commercial safe services</a> for offices, shops, pawnshops, banks and government agencies.</li>
<li>Guide: <a href="~/guides/how-to-choose-a-safe-singapore/">how to choose a safe in Singapore</a>.</li>
</ul>
<p>Read more about <a href="~/about/">Uncle Thomas's background</a>.</p>
""",
 faqs=[
  ("Can you open a safe without destroying it?", "Often, yes. Safes with a forgotten code or lost key can usually be opened and stay usable. When the lock has failed, the safe usually needs precise drilling, and the lock can often be replaced afterwards. We explain the method and price before we start."),
  ("I forgot my safe code. Can you help?", "Yes. Try fresh batteries and the override key first (see our guide). If that doesn't work, WhatsApp us photos of the safe and we'll quote you."),
  ("What types of safes do you open?", "All types: electronic keypad, mechanical dial, key, dual-control, biometric, hotel and wardrobe safes, cash and drop safes, fire and filing safes, vault and strongroom doors, and safes on ships."),
  ("Do you open safes for businesses?", "Yes. Uncle Thomas has worked for commercial offices, pawnshops, banks and government ministries. We need authorisation from the business, and we issue invoices."),
  ("Do I need to bring the safe to you?", "No. We come to you, anywhere in Singapore, 24/7. Most safes are opened where they stand."),
  ("Can you change the combination after opening?", "Yes. We can set a new code, or fit a new lock if the old one has failed."),
  ("Do you check that the safe is mine?", "Always. We ask for proof of ownership or business authorisation before opening any safe."),
  ("How much does safe opening cost?", "It's quoted per job, depending on the safe. Send photos on WhatsApp to {PHONE} for a price."),
 ],
),
# ----------------------------------------------------------------------
dict(
 path="car-locksmith/", short="Car locksmith & key fobs", icon="car",
 card="Keys locked in the car, or need a spare key fob? Car unlocking and key fob cloning for all major brands, 24/7.",
 title="Car Locksmith Singapore 24/7 | Unlocking & Key Fob Cloning",
 title_exp="Car Locksmith Singapore | Car Key Fob Cloning, All Brands",
 desc="Keys locked in the car or need a spare key fob? Uncle Thomas unlocks cars and clones key fobs for all major brands, 24/7 islandwide. Call 9224 9224.",
 h1="Car Locksmith Singapore: Car Unlocking &amp; Key Fob Cloning",
 sub="Keys locked inside, remote not working, or only one key fob left? Uncle Thomas opens cars of all major brands without damage, and clones car key fobs so you have a spare.",
 badges=["Non-destructive entry", "All major brands", "24/7 islandwide"],
 body="""
<h2>Two things we do for cars</h2>
<h3>1. Car unlocking (keys locked inside)</h3>
<ul>
<li>Keys locked inside the car or boot.</li>
<li>Remote key battery dead and the door won't open.</li>
<li>Car locked at a carpark, petrol station or roadside, anywhere in Singapore.</li>
<li>Cars, vans and light commercial vehicles.</li>
</ul>
<p>We use professional car entry tools that open the door without damaging the paintwork, rubber seals or windows. It's much cheaper than breaking a window, and safer than trying a coat hanger yourself, which can damage the door's wiring and airbag sensors.</p>

<h3>2. Car key fob cloning (spare key)</h3>
<p>Down to your last key fob? A spare from the dealer can take time and cost a lot. Uncle Thomas clones remote car key fobs, so you have a working spare. It's the one kind of key we copy. We don't clone smart (keyless) keys. Cloning costs S$100–S$1,000 depending on the car and takes from a few minutes to a few hours, so call or WhatsApp to check yours first. We don't cut or copy house keys.</p>
<ul>
<li>Spare key fob for your car, so one lost key doesn't leave you stranded.</li>
<li>Replacement fob for family members or a second driver.</li>
<li>Remote keys, flip keys and smart keys for push-start cars.</li>
</ul>
<p>More on how it works: <a href="~/car-key-duplicate/">car key duplicate and spare key fob cloning</a>.</p>
<p>WhatsApp {PHONE} your car's make, model and year, plus a photo of your key (front and back), and we'll confirm we can do it and the price before you book. Lost a key already? Read <a href="~/guides/lost-car-key-fob/">lost your car key fob: what to do next</a>. Key locked inside the car? Read <a href="~/guides/keys-locked-in-car/">keys locked in the car: what to do</a>.</p>

<h2>All car brands</h2>
<p>We work on all the major makes on Singapore roads. Tap your brand for tips and details:</p>
{CAR_BRAND_LINKS}
<p>Also: {CAR_BRANDS_MORE} and more. Not sure about your model? Call or WhatsApp {PHONE} to check.</p>

<div class="callout"><p><strong>Proof of ownership:</strong> Before unlocking a car or cloning a key, we check that the car is yours, for example your NRIC against the vehicle log card, or a rental or company car agreement.</p></div>

<h2>Price</h2>
<p>Car lockouts and key fob cloning are quoted per car, because it depends on the make, model and key type. WhatsApp {PHONE} your location, car model and a photo of the key, and we'll confirm the price before we set off. See all <a href="~/prices/">prices</a>.</p>
""",
 faqs=[
  ("Can you open my car without damaging it?", "Yes. We use non-destructive car entry tools that don't damage the paint, seals or windows."),
  ("Which cars can you open?", "All major makes and models, including Toyota, Honda, Mercedes-Benz, BMW, Audi, Volkswagen, Mazda, Lexus, Land Rover, Hyundai, Kia, Nissan, Porsche, Volvo, Mitsubishi and Subaru, plus vans and light commercial vehicles. Not sure about yours? Call or WhatsApp to check."),
  ("Can you make a spare car key fob?", "Yes, for remote key fobs on all major brands. We don't clone smart (keyless) keys. It costs S$100–S$1,000 depending on the car; send us the make, model, year and a photo of the key for a quote."),
  ("Do you cut house keys too?", "No. Car key fobs are the only keys we copy. We don't do house key cutting or duplication."),
  ("How much is a car lockout?", "From {P_CAR}. Key fob cloning is quoted per car. We'll confirm the price before we set off."),
 ],
),
# ----------------------------------------------------------------------
dict(
 path="lock-replacement/", short="Lock replacement", icon="lock",
 card="Main door, gate, room and toilet door locks replaced with quality hardware — warranty with no expiry.",
 title="Lock Change & Replacement Singapore | No-Expiry Warranty",
 title_exp="Lock Change & Replacement Singapore | No-Expiry Warranty",
 desc="Need to change a lock? Main door, HDB gate, room and toilet door lock change and replacement islandwide, with a no-expiry warranty. Call 9224 9224.",
 h1="Lock Change &amp; Replacement in Singapore: Doors and Gates",
 sub="Lost your keys, moved into a new home, or have a lock that's worn out? Uncle Thomas replaces main door, gate and room door locks with quality hardware — and every replacement has a warranty that never expires.",
 badges=["Price agreed first", "No-expiry warranty", "Same-visit replacement"],
 body="""
<h2>When to change your locks</h2>
<p>A lock change (lock replacement) means taking out the old lock and fitting a new one with new keys, so any old keys stop working.</p>
<ul>
<li><strong>You moved into a new home</strong> — you never know how many old keys are out there.</li>
<li><strong>Keys lost or stolen</strong>.</li>
<li><strong>A tenant or helper has moved out</strong>.</li>
<li><strong>The lock is stiff, loose or jams</strong> — a worn lock can fail and lock you out.</li>
<li><strong>After a break-in or attempted break-in</strong>. See <a href="~/guides/after-a-break-in/">what to do after a break-in</a>.</li>
<li><strong>Upgrading security</strong> — or switching to a <a href="~/digital-lock-installation/">digital lock</a>.</li>
</ul>

<h2>Locks we replace</h2>
<ul>
<li>HDB main door locks — mortise locks, cylinder locks, deadbolts and lever handles. See <a href="~/hdb-main-door-lock-replacement/">HDB main door lock replacement</a>.</li>
<li>HDB metal gate locks — hook bolts, padlocks and gate locksets. See <a href="~/hdb-gate-lock-replacement/">HDB gate lock replacement</a>.</li>
<li>Room, toilet and bedroom door locks and knobs.</li>
<li><a href="~/glass-door-lock/">Glass door and sliding door locks</a>, <a href="~/roller-shutter-lock/">roller shutter locks</a> and <a href="~/cabinet-lock/">cabinet, drawer and locker locks</a>.</li>
<li>Condo, landed and office door locks.</li>
<li><a href="~/letterbox-lock-replacement/">Letterbox and mailbox locks</a>.</li>
</ul>

<div class="callout navy"><p><strong>Our warranty:</strong> {WARRANTY}</p></div>

<h2>Replace, don't repair</h2>
<p>{NO_REPAIR} A new lock is usually more reliable, often not much more expensive than a repair, and comes with our warranty.</p>

<h2>Price</h2>
<p>Lock replacement includes supply and installation, and the price depends on the lock you choose. WhatsApp a photo of your current lock to {PHONE} for a fixed price. See all <a href="~/prices/">prices</a>.</p>
""",
 faqs=[
  ("Should I change my locks after moving into a new flat?", "Yes, it's a good idea. Previous owners, tenants or contractors may still have keys."),
  ("How much does a lock change cost in Singapore?", "With us, a main door or gate lock change starts from {P_REPLACE}, including the new lock and installation, with a no-expiry warranty. We confirm the price before we start."),
  ("Do you repair locks?", "No. We replace faulty locks with new ones, which are more reliable and come with our no-expiry warranty."),
  ("Can you replace my lock if I'm locked out?", "Yes — we open the door first, then replace the lock in the same visit if needed."),
  ("Is there a warranty on replacement locks?", "Yes. Every lock replacement comes with our warranty, with no expiry date."),
 ],
),
# ----------------------------------------------------------------------
dict(
 path="letterbox-lock-replacement/", short="Letterbox lock", icon="mailbox",
 card="Lost your letterbox key? We open and replace HDB and condo letterbox locks.",
 title="Letterbox Lock Replacement Singapore | HDB & Condo",
 title_exp="Letterbox Lock Replacement Singapore | Since 1998",
 desc="Lost your HDB or condo letterbox key? Uncle Thomas opens and replaces letterbox locks islandwide, with a no-expiry warranty. Call 9224 9224.",
 h1="Letterbox Lock Replacement in Singapore",
 sub="Lost the key to your HDB or condo letterbox, or the lock is broken? We open it and fit a new lock with new keys — quickly, with proof of residence checked first.",
 badges=["Price agreed first", "HDB & condo", "No-expiry warranty"],
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
<p>Letterbox lock replacement includes a new lock and keys. {WARRANTY} See all <a href="~/prices/">prices</a>.</p>
<p>Need your main door or gate lock changed too? See <a href="~/lock-replacement/">lock replacement</a>.</p>
""",
 faqs=[
  ("I lost my HDB letterbox key. What should I do?", "WhatsApp us your block and a photo of the letterbox. We'll open it and fit a new lock with new keys after checking your proof of residence."),
  ("Do you make duplicate letterbox keys?", "No, we don't do key duplication or key cutting. We replace the lock and give you a new set of keys."),
  ("How much does letterbox lock replacement cost?", "From {P_LETTERBOX}, including the new lock and keys."),
 ],
),
# ----------------------------------------------------------------------
dict(
 path="commercial-locksmith/", short="Commercial locksmith", icon="building",
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
<li><strong>Office and shop lockouts</strong> — main doors, back doors, <a href="~/glass-door-lock/">glass doors</a> and <a href="~/roller-shutter-lock/">roller shutters</a>.</li>
<li><strong>Lock changes when staff leave</strong> or keys go missing.</li>
<li><strong>Digital and keypad locks</strong> for offices and small businesses — see <a href="~/digital-lock-installation/">digital lock installation</a>.</li>
<li><strong>Cabinet, drawer and locker locks</strong> — see <a href="~/cabinet-lock/">cabinet and locker locks</a>.</li>
<li><strong>Padlocks and broken keys</strong> — see <a href="~/padlock-cutting/">padlock cutting</a> and <a href="~/broken-key-extraction/">broken key extraction</a>.</li>
<li><strong>Safes</strong>: opening, combination changes, new locks and new safes for cash, drop and document safes. Uncle Thomas has worked for commercial offices, pawnshops, banks and government ministries. See <a href="~/commercial-safe-services/">commercial safe services</a>.</li>
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
# Premium focus (owner, 1 Nov 2026): safes and cars first.
_ORDER = ["safe-opening/", "car-locksmith/", "emergency-locksmith/", "digital-lock-opening/", "digital-lock-installation/", "commercial-locksmith/", "lock-replacement/", "letterbox-lock-replacement/"]
SERVICES.sort(key=lambda s: _ORDER.index(s["path"]) if s["path"] in _ORDER else 99)

from safes import SAFE_SERVICES
import niche
NICHE_SERVICES = niche.NICHE_SERVICES
SAFE_PATHS = {"safe-opening/"} | {s["path"] for s in SAFE_SERVICES}
SERVICE_BY_PATH = {s["path"]: s for s in SERVICES + SAFE_SERVICES + NICHE_SERVICES}


def related_html(current_path):
    cards = []
    if current_path in niche.RELATED:
        pool = [SERVICE_BY_PATH[p] for p in niche.RELATED[current_path]]
        heading, lead = "Related services", "One call covers it all — 24/7, islandwide."
    elif current_path in SAFE_PATHS:
        pool = [SERVICE_BY_PATH["safe-opening/"]] + SAFE_SERVICES + [SERVICE_BY_PATH["commercial-locksmith/"], SERVICE_BY_PATH["emergency-locksmith/"]]
        heading, lead = "Other safe services", "From opening a locked safe to fitting a new one: one safesmith, 24/7, islandwide."
    else:
        pool = SERVICES
        heading, lead = "Other locksmith services", "One call covers it all — 24/7, islandwide."
    for s in pool:
        if s["path"] == current_path:
            continue
        cards.append(f'<a class="card svc" href="~/{s["path"]}"><span class="ico" aria-hidden="true">{icons.svg(s["icon"])}</span>'
                     f'<h3>{s["short"]}</h3><p>{s["card"]}</p><span class="more">Learn more →</span></a>')
    return (f'<section class="section section-alt"><div class="container"><h2 class="section-title">{heading}</h2>'
            f'<p class="section-lead">{lead}</p>'
            f'<div class="grid g3">{"".join(cards[:6])}</div></div></section>')


def service_cards(with_price=True):
    out = []
    for s in SERVICES:
        pr = C.price(s["path"])
        tag = '<span class="more">See details →</span>'
        out.append(f'<a class="card svc" href="~/{s["path"]}"><span class="ico" aria-hidden="true">{icons.svg(s["icon"])}</span>'
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
  ("Can you come now? How fast can you reach me?", "Yes, any time of day or night. We set off as soon as you call and usually arrive within 25–30 minutes, depending on where you are and traffic. Call or WhatsApp {PHONE}."),
  ("How do I pay?", "By PayNow, once the job is done. We issue an invoice for every job, for homes and companies."),
  ("How much does a locksmith cost in Singapore?", "Our lockouts start from {P_LOCKOUT} (9am–6pm) and {P_AFTERHOURS} after hours, weekends and public holidays. Car lockouts start from {P_CAR} and digital lock opening from {P_DIGITAL_OPEN}. Your final price is always confirmed before any work begins. See our <a href=\"~/prices/\">full price list</a>."),
  ("Do you check that I live there before opening the door?", "Yes. " + ID_POLICY + " It's how we keep every home safe."),
  ("Which areas in Singapore do you cover?", "All of Singapore — Central, East, West, North and North-East. See <a href=\"~/areas/\">areas we serve</a>."),
  ("Is there a warranty?", WARRANTY),
  ("Do you do key duplication or lock repairs?", "No key duplication, key cutting or lock repairs. That's the only work we turn down: the one exception is remote car key fobs, which we clone for all major car brands. Otherwise we specialise in opening doors, digital and smart locks, safes and cars, and in lock replacement and installation. Faulty locks are replaced, not repaired."),
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
    <a href="{C_.GOOGLE_PROFILE}" class="btn btn-outline" target="_blank" rel="noopener">{icons.svg("star", cls="bi bi-star", fill=True)} Read all our Google reviews</a>
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
    if C_.GOOGLE_RATING and C_.GOOGLE_REVIEW_COUNT:
        r = float(C_.GOOGLE_RATING)
        pct = max(0, min(100, r / 5 * 100))
        rating_html = (f'<a class="g-rating" href="{C_.GOOGLE_PROFILE}" target="_blank" rel="noopener">'
                       f'<span class="stars" style="--pct:{pct:.0f}%" aria-hidden="true">★★★★★</span>'
                       f'<span><strong>{r:.1f}</strong> on Google · {int(C_.GOOGLE_REVIEW_COUNT)} reviews</span></a>')
    else:
        rating_html = "<!-- Google rating badge: set GOOGLE_RATING and GOOGLE_REVIEW_COUNT in _build/config.py -->"
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
      <h1>24/7 Locksmith in Singapore</h1>
      <p class="hero-lead"><picture><source srcset="~/assets/img/uncle-thomas-face-112.webp 1x, ~/assets/img/uncle-thomas-face-224.webp 2x" type="image/webp"><img class="hero-face" src="~/assets/img/uncle-thomas-face-112.jpg" srcset="~/assets/img/uncle-thomas-face-224.jpg 2x" width="56" height="56" alt="Uncle Thomas at work on a safe" fetchpriority="high"></picture><span>Led by <strong>Uncle Thomas</strong>: safe and car specialist, locksmith since {C_.FOUNDED}.</span></p>
      {rating_html}
      <ul class="hero-tiles">
        <li><a href="~/safe-opening/"><span class="t-ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3.5" y="3.5" width="17" height="15" rx="2"/><circle cx="12" cy="11" r="3.5"/><path d="M12 7.5V9M12 13v1.5M8.5 11H10M14 11h1.5"/><path d="M6.5 18.5V21M17.5 18.5V21"/></svg></span><span class="t-txt"><strong>Safes</strong><span>All safes and bolts: combination dials and smart keypads</span></span><svg class="t-go" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M9 6l6 6-6 6"/></svg></a></li>
        <li><a href="~/car-locksmith/"><span class="t-ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 16.5V12l1.8-4.6A2 2 0 0 1 7.7 6h8.6a2 2 0 0 1 1.9 1.4L20 12v4.5"/><path d="M3 16.5h18"/><path d="M4.5 12h15"/><circle cx="7.5" cy="16.5" r="1.8"/><circle cx="16.5" cy="16.5" r="1.8"/></svg></span><span class="t-txt"><strong>Cars</strong><span>Car unlocking and key fob cloning, all major brands</span></span><svg class="t-go" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M9 6l6 6-6 6"/></svg></a></li>
        <li><a href="~/emergency-locksmith/"><span class="t-ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M6 21V4.5A1.5 1.5 0 0 1 7.5 3h9A1.5 1.5 0 0 1 18 4.5V21"/><path d="M3.5 21h17"/><path d="M14.5 12.5h.01"/></svg></span><span class="t-txt"><strong>Doors</strong><span>Any door: HDB, condo, landed, office, digital &amp; smart locks</span></span><svg class="t-go" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M9 6l6 6-6 6"/></svg></a></li>
      </ul>
      {x["cta_buttons"]()}
      <p class="hero-note">Price agreed before we start · No-expiry warranty</p>
    </div>
    <div class="hero-art">{hero_art}</div>
  </div>
</section>

<section class="trust" aria-label="Key facts">
  <div class="container trust-inner">
    <div class="trust-item"><strong>Since {C_.FOUNDED}</strong><span>{C_.YEARS}+ years in the trade</span></div>
    <div class="trust-item"><strong>24/7</strong><span>Nights, weekends, PH</span></div>
    <div class="trust-item"><strong>Islandwide</strong><span>Every town in Singapore</span></div>
    <div class="trust-item"><strong>No-expiry</strong><span>Warranty on every lock we fit</span></div>
  </div>
</section>

{reviews_html(C_)}
<section class="section section-alt" id="reviews">
  <div class="container">
    <h2 class="section-title">What Customers Say on Google</h2>
    <p class="section-lead"><span class="rv-score">{C_.GOOGLE_RATING:.1f}</span> <span class="rv-stars" aria-hidden="true">★★★★★</span> from {int(C_.GOOGLE_REVIEW_COUNT)} Google reviews</p>
    <div class="rv-list" id="g-reviews" data-place="{C_.PLACE_ID}" data-key="{C_.GOOGLE_BROWSER_KEY}" aria-live="polite"></div>
    <p class="rv-foot"><a href="{C_.GOOGLE_PROFILE}" target="_blank" rel="noopener">Read all reviews on Google</a> · <a href="{C_.GOOGLE_REVIEW_URL}" target="_blank" rel="noopener">Leave a review</a></p>
    <p class="rv-attr">Reviews from Google</p>
  </div>
</section>

<section class="section" id="services">
  <div class="container">
    <h2 class="section-title">Locksmith Services in Singapore</h2>
    <p class="section-lead">Doors, digital locks, safes and cars — for HDB flats, condos, landed homes, offices and shops.</p>
    <div class="grid g4">{service_cards()}</div>
    <p class="note">We specialise in opening and replacing locks. We do <strong>not</strong> offer key duplication, key cutting or lock repair. The one exception: we clone car key fobs.</p>
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
    <h2 class="section-title">The Price Is Agreed Before We Start</h2>
    <p class="section-lead">No call-out tricks and no surprises at the door. Send a photo of the lock, and Uncle Thomas gives you a firm price before anyone sets off. The price we agree is the price you pay.</p>
    <p class="price-foot">Every lock we replace or install comes with a warranty that never expires · <a href="~/prices/">See how pricing works</a></p>
    {x["quote_form"]("home")}
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
      <div class="card svc"><span class="ico" aria-hidden="true">{icons.svg("clock")}</span><h3>Immediate response</h3><p>We set off as soon as you call — day or night, weekends and public holidays.</p></div>
      <div class="card svc"><span class="ico" aria-hidden="true">{icons.svg("tag")}</span><h3>Price before work</h3><p>Upfront starting prices, and your final price confirmed before we touch the lock.</p></div>
      <div class="card svc"><span class="ico" aria-hidden="true">{icons.svg("shield")}</span><h3>Damage-free methods</h3><p>We open most doors, digital locks and cars without drilling or forcing.</p></div>
      <div class="card svc"><span class="ico" aria-hidden="true">{icons.svg("idcard")}</span><h3>We check ID before opening</h3><p>We check proof of residence or ownership — so no one can use a locksmith to get into your home.</p></div>
      <div class="card svc"><span class="ico" aria-hidden="true">{icons.svg("check")}</span><h3>No-expiry warranty</h3><p>Every lock replacement and installation is covered, with no expiry date.</p></div>
      <div class="card svc"><span class="ico" aria-hidden="true">{icons.svg("award")}</span><h3>{C_.YEARS}+ years' experience</h3><p>From HDB gates to ship safes — there's very little Uncle Thomas hasn't opened.</p></div>
    </div>
  </div>
</section>

<section class="section section-alt" id="areas">
  <div class="container narrow" style="text-align:center">
    <h2 class="section-title">Locksmith Near You — Islandwide</h2>
    <p class="section-lead">Wherever you are in Singapore, Uncle Thomas can reach you. Find your town:</p>
    <details class="m-fold towns-box" open><summary>Find your town ({len(x["areas"].TOWNS)} areas)</summary><div class="town-links" style="justify-content:center">{town_links}</div></details>
    <p style="margin-top:20px"><a href="~/areas/" class="btn btn-outline">See all areas we serve</a></p>
  </div>
</section>


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
    title = pick_title(("24/7 Locksmith Singapore | Since 1998 · US-Trained Safesmith",
                        "24/7 Locksmith Singapore | Since 1998 · US-Trained Safesmith"))
    desc = "Locked out? Uncle Thomas is Singapore's 24/7 emergency locksmith since 1998. Doors, digital locks, safes & cars, islandwide, 24/7. Call 9224 9224."
    biz = x["business_node"](full=True)
    nodes = [
        {"@type": "WebSite", "@id": C_.SITE + "/#website", "url": C_.SITE + "/", "name": C_.NAME,
         "inLanguage": "en-SG", "publisher": {"@id": x["BUSINESS_ID"]}},
        {"@type": "WebPage", "@id": C_.SITE + "/#webpage", "url": C_.SITE + "/", "name": title, "description": desc,
         "isPartOf": {"@id": C_.SITE + "/#website"}, "about": {"@id": x["BUSINESS_ID"]}, "inLanguage": "en-SG",
         "primaryImageOfPage": {"@type": "ImageObject", "url": C_.SITE + "/assets/img/og-2026.jpg"}},
        biz, x["person_node"](), x["faq_node"](HOME_FAQS),
    ]
    x["render"]("", title, desc, body, nodes, preload_img=None if hero_photo.startswith("<figure") else "assets/img/logo-320.webp",
                priority="1.0", alternates={"en-SG": "", "zh-SG": "zh/"})


# ======================================================================
# SERVICES HUB + SERVICE PAGES
# ======================================================================
def build_services(x):
    C_ = x["C"]
    lock_pills = "".join(f'<li><a href="~/digital-lock-opening/{b["slug"]}/">{b["name"]}</a></li>' for b in x["brands"].BRANDS)
    crumbs = [("Home", ""), ("Services", "services/")]
    title = "Locksmith Services Singapore | Doors, Digital Locks & Safes"
    desc = "All Uncle Thomas Locksmith services: emergency lockouts, digital lock opening & installation, safes, cars, lock and letterbox replacement. 24/7, islandwide."
    body = (x["page_hero"](crumbs, "Locksmith Services in Singapore",
            "Everything Uncle Thomas and his team can help with — 24/7, islandwide. Tap a service for details and prices.",
            ["24/7 islandwide", "Price before work", "No-expiry warranty"]) +
            f'<section class="section"><div class="container"><h2 class="section-title">All locksmith services</h2><div class="grid g4" style="margin-top:24px">{service_cards()}</div>'
            f'<p class="note">{NO_REPAIR}</p></div></section>' +
            f'''<section class="section section-alt"><div class="container narrow prose">
<h2>Which service do you need?</h2>
<table class="price-table info-table"><thead><tr><th scope="col">Your situation</th><th scope="col">Service</th></tr></thead><tbody>
<tr><td>Locked out of your flat, house or office</td><td><a href="~/emergency-locksmith/">Emergency lockout</a></td></tr>
<tr><td>Digital or smart lock won't open (flat battery, forgotten PIN, dead keypad)</td><td><a href="~/digital-lock-opening/">Digital &amp; smart lock opening</a></td></tr>
<tr><td>Want a keyless lock on your door or gate</td><td><a href="~/digital-lock-installation/">Digital &amp; smart lock installation</a></td></tr>
<tr><td>Lost keys, moved house, or a worn or broken lock</td><td><a href="~/lock-replacement/">Lock change &amp; replacement</a></td></tr>
<tr><td>New lock for your HDB main door</td><td><a href="~/hdb-main-door-lock-replacement/">HDB main door lock replacement</a></td></tr>
<tr><td>Rusty, stiff or broken HDB gate lock</td><td><a href="~/hdb-gate-lock-replacement/">HDB gate lock replacement</a></td></tr>
<tr><td>A spare car key fob</td><td><a href="~/car-key-duplicate/">Car key duplicate</a></td></tr>
<tr><td>Key broken or stuck in the lock</td><td><a href="~/broken-key-extraction/">Broken key extraction</a></td></tr>
<tr><td>Padlock key lost or code forgotten</td><td><a href="~/padlock-cutting/">Padlock cutting &amp; removal</a></td></tr>
<tr><td>Shop shutter won't unlock</td><td><a href="~/roller-shutter-lock/">Roller shutter locks</a></td></tr>
<tr><td>Glass door or sliding door lock</td><td><a href="~/glass-door-lock/">Glass &amp; sliding door locks</a></td></tr>
<tr><td>Cabinet, drawer or locker key lost</td><td><a href="~/cabinet-lock/">Cabinet, drawer &amp; locker locks</a></td></tr>
<tr><td>Forgot a safe combination or lost the safe key</td><td><a href="~/safe-opening/">Safe opening</a></td></tr>
<tr><td>Need a new safe code, or a faulty safe lock replaced</td><td><a href="~/safe-combination-change/">Safe combination &amp; lock change</a></td></tr>
<tr><td>Buying a safe, or need one installed</td><td><a href="~/safe-installation/">Safe supply &amp; installation</a></td></tr>
<tr><td>A safe at your office, shop, pawnshop or bank</td><td><a href="~/commercial-safe-services/">Commercial safe services</a></td></tr>
<tr><td>Keys locked in the car, or need a spare key fob</td><td><a href="~/car-locksmith/">Car locksmith &amp; key fobs</a></td></tr>
<tr><td>Lost your letterbox key</td><td><a href="~/letterbox-lock-replacement/">Letterbox lock</a></td></tr>
<tr><td>Office, shop, warehouse or vessel</td><td><a href="~/commercial-locksmith/">Commercial locksmith</a></td></tr>
</tbody></table>
<h2>Digital and smart lock brands</h2>
<p>We open and install every brand. Guides for the most common ones:</p>
<ul class="link-pills">{lock_pills}</ul>
<h2>Car brands</h2>
<p>Car unlocking and key fob cloning for all major makes:</p>
{x["cars"].links_html()}
<p>Not sure what you need? WhatsApp a photo to {C_.PHONE} and we'll tell you, with a price, before we set off.</p>
</div></section>''' + x["cta_band"]())
    nodes = x["page_schema"]("services/", title, desc, crumbs, page_type="CollectionPage", extra=[
        {"@type": "ItemList", "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "url": C_.SITE + "/" + s["path"], "name": s["short"]}
            for i, s in enumerate(SERVICES + SAFE_SERVICES + NICHE_SERVICES)]}])
    x["render"]("services/", title, desc, body, nodes, priority="0.8")

    for s in SERVICES + SAFE_SERVICES + NICHE_SERVICES:
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
        zh_set = {"emergency-locksmith/"} | set(x["zh_pages"])
        alts = {"en-SG": s["path"], "zh-SG": "zh/" + s["path"]} if s["path"] in zh_set else None
        x["render"](s["path"], title, s["desc"], body, nodes, priority="0.9", alternates=alts)


# ======================================================================
# PRICES
# ======================================================================
PRICE_FAQS = [
  ("Why do locksmith prices vary so much in Singapore?", "Mainly because of the lock type, the time of day, whether a part needs replacing, and how the price is quoted. Some locksmiths advertise a very low call-out fee and add charges at the door. We give you the price before we start."),
  ("Is there a call-out or transport fee?", "Our prices are quoted for the job at your location. We'll tell you the total before we set off, so you won't be surprised by extra fees."),
  ("Do you charge more after midnight or on public holidays?", "Lockouts start from {P_LOCKOUT} from 9am to 6pm and from {P_AFTERHOURS} after hours, weekends and public holidays."),
  ("What if you can't open the lock?", "We'll explain the options — such as replacing the lock — and the price, and only go ahead with your agreement."),
  ("How do I pay?", "By PayNow, once the job is done. We issue an invoice for every job."),
]


def build_prices(x):
    C_ = x["C"]
    crumbs = [("Home", ""), ("Prices", "prices/")]
    title = "Locksmith Prices Singapore (2026) | Confirmed Upfront"
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
    title = "About Uncle Thomas | Singapore Locksmith & Safesmith"
    desc = "Meet Uncle Thomas, the locksmith Singapore calls 'Shifu'. An apprentice in 1998, US-trained in safesmithing, he has opened safes on ships and across Asia."
    body = (x["page_hero"](crumbs, 'Meet Uncle Thomas — The Locksmith Singapore Calls "Shifu"',
            f"From apprentice in {C_.FOUNDED} to US-trained safesmith — the story behind Uncle Thomas Locksmith.",
            [f"Since {C_.FOUNDED}", "US-trained safesmith", "Team of four"]) +
            f'''<section class="section"><div class="container narrow prose">
{x["photo"]("about_portrait")}
<h2>From apprentice to master locksmith</h2>
<p>Uncle Thomas started in {C_.FOUNDED} as an apprentice under his uncle, learning the trade the traditional way — one lock, one door, one customer at a time. Years of hands-on work across Singapore's HDB flats, condos, shophouses and offices built the foundation he still relies on today.</p>
<h2>Trained in safesmithing in the United States</h2>
<p>Wanting to master the hardest locks in the trade, he spent a year in the United States training in safesmithing — the specialist skill of opening and servicing safes and vaults — and completed the Associated Locksmiths of America (ALOA) Fundamentals of Locksmithing course in 1999. It's a skill few locksmiths in Singapore have. <a href="~/safe-opening/">See our safe opening service</a>.</p>
<h2>Trusted overseas — on land and at sea</h2>
<p>That expertise has taken Uncle Thomas far beyond Singapore. He has been called in to open safes for multinational companies and on board ships and cruise liners, with jobs in Thailand, Malaysia, China, Hong Kong and more. In Singapore he has worked on safes for commercial offices, pawnshops, banks and government ministries.</p>
<h2>Keeping up with digital locks</h2>
<p>As homes moved from keys to keypads, Uncle Thomas kept learning. He has developed his own damage-free techniques, including lock picking, for opening faulty and locked digital locks — so you get back in without needing to replace an expensive lock. <a href="~/digital-lock-opening/">See digital lock opening</a>.</p>
<h2>Why they call him "Shifu"</h2>
<p>In the trade, Uncle Thomas is known as the "Shifu" — the master other locksmiths turn to when a job gets difficult. Today he leads a team of four locksmiths, Thomas, Ong, Melvin and Andrew, and he still personally handles the toughest jobs.</p>
<h2>How we work</h2>
<ul>
<li><strong>24/7, islandwide</strong> — we set off as soon as you call and usually arrive within 25–30 minutes, any distance, any time.</li>
<li><strong>Every job, day or night</strong> — the only work we turn down is key duplication and key cutting.</li>
<li><strong>Languages</strong> — English, Mandarin, Malay, Hokkien and Cantonese.</li>
<li><strong>Payment</strong> — PayNow, with an invoice for every job.</li>
<li><strong>Price before work</strong> — <a href="~/prices/">upfront starting prices</a>, and your final price confirmed before we begin.</li>
<li><strong>ID verified</strong> — {ID_POLICY}</li>
<li><strong>Warranty</strong> — {WARRANTY}</li>
<li><strong>Specialists</strong> — safes and cars first, then doors and digital locks, and lock replacement and installation. We don't do lock repairs, key duplication or key cutting, except cloning remote car key fobs.</li>
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
    car_more = ", ".join(C.CAR_BRANDS_MORE)
    for s in SERVICES + NICHE_SERVICES:
        s["body"] = (s["body"].replace("{CAR_BRAND_LINKS}", x["cars"].links_html())
                     .replace("{CAR_BRANDS_MORE}", car_more))
    import safe_brands
    for s in SERVICES:
        s["body"] = s["body"].replace("{SAFE_BRAND_PILLS}", safe_brands.pills_html())
    for s in SERVICES:
        s["body"] = s["body"].replace("{BRAND_LINKS}",
            f'<h3>Brand guides: what to try first</h3><ul class="link-pills">{brand_links}</ul>' if brand_links else "")
    build_home(x)
    build_services(x)
    build_prices(x)
    build_about(x)
