"""
Safe pages beyond safe opening (added 29 Oct 2026).
Owner-confirmed facts (29 Oct 2026): Uncle Thomas opens all safe types; some safes
can be opened and stay usable, but most faulty safes need drilling; he changes
combinations, installs safes, and recommends or procures safes on request; he has
worked for commercial offices, pawnshops, banks and government ministries; he
issues invoices to companies. Don't add claims beyond these without owner input.
"""
import config as C

SAFE_CLUSTER_NOTE = "safe"

_MORE_SAFE = """
<h2>Other safe services</h2>
<ul>
<li><a href="~/safe-opening/">Safe opening</a>: forgotten combination, lost key, dead keypad or jammed bolt.</li>
<li><a href="~/safe-combination-change/">Safe combination change and safe lock replacement</a>.</li>
<li><a href="~/safe-installation/">Safe supply and installation</a>: we recommend, source and install the right safe.</li>
<li><a href="~/commercial-safe-services/">Commercial safe services</a> for offices, shops, pawnshops, banks and government agencies.</li>
</ul>
"""

SAFE_SERVICES = [
# ----------------------------------------------------------------------
dict(
 path="safe-combination-change/", short="Safe combination & lock change", icon="keypad",
 card="Staff left, moved house or bought a used safe? New combination or a new safe lock, set by a safesmith.",
 title="Safe Combination Change & Safe Lock Replacement Singapore",
 title_exp="Safe Combination Change Singapore | Safe Lock Replacement",
 desc="Change your safe combination or replace a faulty safe lock in Singapore. Dial, keypad and key safes, homes and businesses. US-trained safesmith. Call 9224 9224.",
 h1="Safe Combination Change and Safe Lock Replacement",
 sub="Someone who knew the code has left, you've bought a second-hand safe, or the keypad is failing. Uncle Thomas, a US-trained safesmith, changes combinations and replaces safe locks on all types of safe.",
 badges=["All safe types", "Homes & businesses", "Invoices for companies"],
 body="""
<p><strong>The short answer:</strong> a safe's combination should change whenever you can't be sure who knows it. On an electronic safe that's usually quick. On a mechanical dial safe it's a precise job, because a mistake can lock you out of your own safe. If the lock itself is faulty, the better fix is a new lock.</p>

<h2>When to change your safe combination</h2>
<ul>
<li><strong>A staff member who knew the code has left</strong>, or a manager has changed.</li>
<li><strong>You've bought or inherited a safe</strong>, or moved into a home or office that came with one.</li>
<li><strong>The code has been shared</strong> with a contractor, a helper or family members who no longer need it.</li>
<li><strong>The safe still uses the factory code.</strong> Many owners never change it.</li>
<li><strong>After a break-in or a lost override key</strong>, even if the safe wasn't opened.</li>
<li><strong>As routine for business safes</strong>, for example once a year or when your audit policy says so.</li>
</ul>

<h2>Combination changes by safe type</h2>
<table class="price-table info-table"><thead><tr><th scope="col">Safe type</th><th scope="col">What a combination change involves</th></tr></thead><tbody>
<tr><td>Electronic keypad safe</td><td>Usually set from the keypad with the current code or a manager code. We also check the batteries and the override key, so the new code doesn't fail you next month.</td></tr>
<tr><td>Mechanical dial safe</td><td>The lock's wheels are reset to new numbers with a change key, then tested several times with the door open. Done wrongly, this is how people lock themselves out, so it's a safesmith's job.</td></tr>
<tr><td>Key safe</td><td>Keys can't be "re-coded". If keys are missing, the lock is replaced and you get new keys.</td></tr>
<tr><td>Dual-control safe (code plus key, or two codes)</td><td>Each code holder sets their own part. Common in offices and shops, so no single person can open the safe alone.</td></tr>
</tbody></table>

<h2>Safe lock replacement</h2>
<p>If a keypad is failing, a dial is stiff, or the safe had to be opened because the lock broke, the answer is usually a <strong>new lock</strong>, not a new safe. The photos below are from a real job: a home safe whose original keypad lock failed. Uncle Thomas opened it, removed the faulty lock and fitted a new electronic keypad lock, so the owner kept the same safe.</p>
<p>Not every safe is worth a new lock. A small, light safe can cost less to replace than to refit. We'll tell you honestly which makes sense before any work starts.</p>

<h2>How it works</h2>
<ol>
<li><strong>WhatsApp {PHONE} photos</strong> of the safe's front, the keypad or dial, and the brand label.</li>
<li><strong>We confirm the price</strong> before we come.</li>
<li><strong>We check ownership or authorisation</strong>, then change the combination or replace the lock.</li>
<li><strong>We test it with you</strong>, several times, with the door open, before closing the safe.</li>
</ol>

<div class="callout"><p><strong>Keep the new code safe.</strong> Write it down and store it somewhere secure <em>outside</em> the safe. For a business, decide who holds it and record the date it was changed.</p></div>
""" + _MORE_SAFE,
 faqs=[
  ("How often should I change my safe combination?", "Whenever someone who knew it no longer needs it: a staff member leaving, a move, or a shared code. Businesses often also change it on a fixed schedule, such as once a year."),
  ("Can I change a dial safe combination myself?", "It's possible with the change key and the manufacturer's instructions, but a mistake can lock you out of the safe. If you're not confident, ask a safesmith to do it with the door open."),
  ("My safe keypad is faulty. Do I need a new safe?", "Usually not. The faulty keypad or lock can often be replaced, so you keep the safe. For small, light safes, a new safe can sometimes cost less, and we'll tell you if so."),
  ("Do you change combinations for business safes?", "Yes, for offices, shops and other businesses. We need authorisation from the business, and we can issue an invoice to the company."),
  ("How much does a safe combination change cost?", "It depends on the safe and lock type, so it's quoted per job. WhatsApp a photo to {PHONE} for a price before we come."),
 ],
),
# ----------------------------------------------------------------------
dict(
 path="safe-installation/", short="Safe supply & installation", icon="wrench",
 card="Not sure which safe to buy? We recommend the right one, source it if needed, and install it properly.",
 title="Safe Installation Singapore | Advice, Supply & Bolt-Down",
 title_exp="Safe Installation Singapore | We Recommend, Supply & Install",
 desc="Buying a safe in Singapore? A US-trained safesmith recommends the right safe, sources it if needed and installs it properly, for homes and businesses.",
 h1="Safe Supply and Installation in Singapore",
 sub="Uncle Thomas has opened safes of every type for {YEARS}+ years, so he knows which ones hold up. He'll recommend the right safe for what you're protecting, source it if you need one, and install it properly.",
 badges=["Independent advice", "Homes & businesses", "Installed properly"],
 body="""
<p><strong>The short answer:</strong> choose a safe for what you're protecting (cash, jewellery, documents or data), how much it's worth, and where it will stand. Then make sure it's fixed down. A safe that isn't anchored can be carried away and opened somewhere else.</p>

<h2>What we do</h2>
<ul>
<li><strong>Recommend:</strong> we ask what you'll keep in it, its value, and where the safe will go, then suggest the right type and size.</li>
<li><strong>Source:</strong> if you don't have a safe yet, we can procure one for you.</li>
<li><strong>Install:</strong> we position the safe and fix it down where the safe and the floor allow, then set your code and check the lock with you.</li>
<li><strong>Already bought one?</strong> We can install a safe you've bought yourself. Send us the model first so we can check it can be fixed down.</li>
</ul>

<h2>Five things that decide the right safe</h2>
<ol>
<li><strong>What you're protecting.</strong> Cash and jewellery need burglary resistance. Documents need fire resistance. Hard drives and USB sticks need a data-rated fire safe, because a safe built for paper can still get too hot inside for electronics.</li>
<li><strong>The value inside.</strong> Higher-value contents call for a higher security grade. Ask your insurer what they expect for the amount you're keeping at home or at work.</li>
<li><strong>The lock.</strong> Electronic keypads are quick and the code is easy to change. Mechanical dials need no batteries. Dual-control locks suit businesses where two people should be present to open the safe.</li>
<li><strong>Weight and fixing.</strong> European safe standards expect burglary-resistant safes under 1,000 kg to be anchored. Most home and office safes are far lighter, so fixing them down matters.</li>
<li><strong>Where it will stand.</strong> Floor type, access, lifts and stairs all matter. In a condo or rented home, check with management or your landlord before drilling into the floor.</li>
</ol>
<p>For more detail, read our guide to <a href="~/guides/how-to-choose-a-safe-singapore/">choosing a safe in Singapore</a>.</p>

<h2>Where we install safes</h2>
<ul>
<li>HDB flats, condos and landed homes.</li>
<li>Offices, shops and retail counters.</li>
<li>Pawnshops, jewellers and other businesses handling cash or valuables.</li>
</ul>

<div class="callout"><p><strong>Discreet by default.</strong> We don't publish where we install safes, and we keep your details private.</p></div>
""" + _MORE_SAFE,
 faqs=[
  ("Can you recommend a safe for my home?", "Yes. Tell us what you'll keep in it, roughly what it's worth and where it will stand, and we'll suggest the right type and size."),
  ("Can you supply the safe?", "Yes. If you don't have one yet, we can procure a suitable safe and install it."),
  ("Should a home safe be bolted down?", "Yes, wherever the safe and floor allow. European standards expect burglary-resistant safes under 1,000 kg to be anchored, and an unanchored small safe can simply be carried away."),
  ("Is a fireproof safe good for hard drives?", "Only if it's rated for data or digital media. Safes rated for paper can still get too hot inside for electronics."),
  ("Can you install a safe I bought online?", "Usually, yes. Send us the model and photos of where it will go, and we'll confirm before we come."),
 ],
),
# ----------------------------------------------------------------------
dict(
 path="commercial-safe-services/", short="Commercial safe services", icon="building",
 card="Safes for offices, shops, pawnshops, banks and government agencies: opening, code changes, new locks, new safes.",
 title="Commercial Safe Services Singapore | Offices, Banks & Shops",
 title_exp="Commercial Safe Locksmith Singapore | Offices, Banks, Shops",
 desc="Safe opening, code changes, new locks and safe installation for Singapore offices, shops, pawnshops, banks and government agencies. Invoices issued.",
 h1="Safe Services for Businesses in Singapore",
 sub="Uncle Thomas has worked on safes for commercial offices, pawnshops, banks and government ministries. One safesmith for opening, combination changes, new locks and new safes, with invoices for your accounts team.",
 badges=["Offices, banks & pawnshops", "Invoices issued", "24/7, discreet"],
 body="""
<p><strong>The short answer:</strong> when a business safe won't open, the cost is usually the downtime: cash you can't bank, documents you can't reach, a counter you can't open. Uncle Thomas is a US-trained safesmith who has worked for commercial offices, pawnshops, banks and government ministries, and he's available 24/7, including before opening hours and after closing.</p>

<h2>Who we work with</h2>
<ul>
<li><strong>Commercial offices:</strong> cash safes, document and filing safes, and key cabinets.</li>
<li><strong>Pawnshops and jewellers:</strong> safes holding pledges, gold and jewellery.</li>
<li><strong>Banks and financial businesses.</strong></li>
<li><strong>Government ministries and agencies.</strong></li>
<li><strong>Shops, restaurants and retail counters:</strong> drop safes and cash safes.</li>
<li><strong>Ships and vessels:</strong> Uncle Thomas has opened safes on board ships and cruise liners.</li>
</ul>

<h2>Business safe services</h2>
<table class="price-table info-table"><thead><tr><th scope="col">You need</th><th scope="col">What we do</th></tr></thead><tbody>
<tr><td>A safe opened now</td><td>Forgotten code, lost key, dead keypad or a jammed bolt. See <a href="~/safe-opening/">safe opening</a>.</td></tr>
<tr><td>A new code after staff changes</td><td>Combination changed and tested with you. See <a href="~/safe-combination-change/">combination change</a>.</td></tr>
<tr><td>A faulty lock fixed for good</td><td>Old lock out, new lock in, so you keep the safe.</td></tr>
<tr><td>A new or extra safe</td><td>We recommend, source and install it. See <a href="~/safe-installation/">safe installation</a>.</td></tr>
<tr><td>Doors, shutters and office locks too</td><td>See <a href="~/commercial-locksmith/">commercial locksmith</a>.</td></tr>
</tbody></table>

<h2>How we work with businesses</h2>
<ul>
<li><strong>Authorisation first.</strong> Before opening any business safe, we confirm the request comes from someone authorised by the business, such as a letter on company letterhead or confirmation from a director or manager.</li>
<li><strong>Price agreed before work starts</strong>, from photos of the safe.</li>
<li><strong>Invoices issued</strong> to the company for your records.</li>
<li><strong>Timed around your business:</strong> early mornings, after closing, weekends and public holidays.</li>
<li><strong>Discreet:</strong> we don't name our business clients or publish where their safes are.</li>
</ul>

<h2>Pawnshops and jewellers</h2>
<p>Pawnbrokers in Singapore must keep their pledges secure and insured against theft under the <a href="https://rop.mlaw.gov.sg/information-for-pawnbrokers/" target="_blank" rel="noopener">Registry of Pawnbrokers' licence conditions</a>. A safe that won't open at the start of the day means pledges customers can't redeem. Call {PHONE} any time, and keep a note of the safe's brand and model so we can bring the right equipment.</p>

<h2>Keep business safes trouble-free</h2>
<ul>
<li>Change the code whenever a key holder leaves, and record the date.</li>
<li>Replace keypad batteries on a schedule, not when they die.</li>
<li>Keep override keys off-site or in a separate secure place, never inside the safe.</li>
<li>Don't let staff force a sticking dial or handle. Call us before it jams completely.</li>
</ul>
""" + _MORE_SAFE,
 faqs=[
  ("Do you open safes for banks and government agencies?", "Uncle Thomas has worked on safes for commercial offices, pawnshops, banks and government ministries. We need authorisation from the organisation before opening."),
  ("Can you issue an invoice to our company?", "Yes. We issue invoices for business jobs."),
  ("Can you come before our shop opens?", "Yes. We work 24/7, including early mornings, late nights, weekends and public holidays."),
  ("Our safe needs drilling. Will it still be usable?", "It depends on the safe. Some can be opened and stay usable; most faulty safes need drilling. We explain the options and price before starting, and the lock can often be replaced afterwards."),
  ("How do you confirm we're authorised?", "Typically a letter on company letterhead or confirmation from a director or manager, plus ID of the person meeting us."),
 ],
),
]
