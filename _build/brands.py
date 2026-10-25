"""
Digital lock brand pages: /digital-lock-opening/<brand>/

Only brands listed in config.BRAND_PAGES are built. Brand details are written
cautiously ("many models…") because features vary by model — the owner should
always check the lock's manual. We are independent and not affiliated with any brand.
"""
import config as C

DATA = {
"Samsung": dict(
 about="Samsung digital door locks are among the most common locks on HDB main doors and gates in Singapore, from rim locks on metal gates to push-pull mortise locks on main doors. Many have been in service for years, so we see a mix of older models with tired keypads and newer models with fingerprint readers.",
 power="Many Samsung models have emergency power contacts on the outside of the lock, often at the bottom of the keypad, where you can hold a 9V battery to wake the lock and enter your PIN. Check your model's manual to confirm where yours is.",
 backup="Some Samsung models have a hidden mechanical key cylinder; others rely only on PIN, card, fingerprint and emergency power. If your model came with a backup key, keep it outside the home — with family, at work or in your car.",
 quirk="On older Samsung locks, a keypad that lights up but doesn't accept a correct code is often a sign of a weak battery or worn keypad contacts rather than a forgotten PIN.",
 faqs=[
  ("Where is the emergency battery point on a Samsung digital lock?", "On many models it's on the outside, often under the keypad. Hold a 9V battery to the contacts and enter your code. Models differ, so check your manual."),
  ("My Samsung lock beeps but won't open with the right PIN. Why?", "Often it's low battery power or a mechanical problem with the lock body. Try emergency power first; if it still won't open, call us."),
 ]),
"Yale": dict(
 about="Yale digital locks are widely sold in Singapore and fitted to HDB doors and gates, condos and landed homes. The range covers rim locks for gates, mortise locks for main doors and smart locks with app control.",
 power="Many Yale models have an emergency power point on the outside — on some it's a 9V battery terminal, on newer models it may be a USB port. Your manual will show which yours uses.",
 backup="Many Yale models include a mechanical override key hidden behind a cover. If you received one with your lock, store it somewhere you can reach when you're outside the home.",
 quirk="If a Yale lock has been set to privacy or double-lock mode from inside, it can refuse codes from outside — a common surprise when someone at home has switched it on.",
 faqs=[
  ("How do I open a Yale digital lock with a dead battery?", "Use the emergency power point (9V or USB on many models) to wake it, then enter your code. If your model has a mechanical key, that works without power."),
  ("My Yale lock won't accept my code. Is it locked from inside?", "It might be. Privacy or double-lock mode can block outside codes. Ask anyone inside to switch it off, or call us if no one is home."),
 ]),
"Philips": dict(
 about="Philips digital locks — sold in the EasyKey range — are popular for HDB main doors and condo doors in Singapore, especially push-pull models with fingerprint and app features.",
 power="Depending on the model, Philips locks may take emergency power through a USB port or a 9V terminal on the outside. Check your model's manual so you know which cable or battery to carry.",
 backup="Many Philips models include a mechanical backup key. Keep it outside the home — a backup key locked inside the flat can't help you.",
 quirk="Fingerprint readers can struggle when fingers are wet, very dry or cut. If the fingerprint fails, try your PIN or card before assuming the lock is faulty.",
 faqs=[
  ("Can I charge a Philips digital lock from outside?", "Many models accept emergency power from outside via USB or a 9V battery. This only wakes the lock so you can enter — replace the batteries once you're in."),
  ("My Philips fingerprint reader stopped working. Is the lock broken?", "Not necessarily. Try your PIN or card. Wet or dry fingers often cause failed reads. If nothing works, call us."),
 ]),
"Igloohome": dict(
 about="Igloohome is a Singapore-founded smart lock brand, popular with homeowners and landlords who want app control and the ability to share access codes. Its mortise and deadbolt smart locks are common on HDB and condo doors.",
 power="Smart locks still need battery power. Many smart lock models have an emergency power option and a mechanical backup key — check your model's manual for where they are.",
 backup="If you manage the lock through the app, you may be able to issue yourself or a family member a new access code from your phone. If the phone is inside, or the lock has no power, the backup key or a locksmith is the next step.",
 quirk="Landlords often use smart locks to issue codes to tenants or guests. If a code stops working, check the code's validity period in the app before calling — expired codes are a common cause.",
 faqs=[
  ("Can I let myself back in through the Igloohome app?", "If you still have access to the app and your account, you may be able to issue a new code. If not, try the backup key or call us."),
  ("A guest's code isn't working on my Igloohome lock. What should I check?", "Check whether the code has expired or was set for a different time window. If the lock itself isn't responding, check the battery."),
 ]),
"Gateman": dict(
 about="Gateman digital locks have been fitted to Singapore homes for many years, on both HDB main doors and gates. Many owners have older Gateman models that are still working but starting to show their age.",
 power="Many Gateman models have emergency power contacts on the outside for a 9V battery. Hold the battery to the contacts, then enter your code. Your manual will confirm where they are.",
 backup="Some Gateman models include a mechanical backup key and some don't. If yours came with one, keep it outside the home.",
 quirk="Older Gateman locks often start to show worn keypads or slower motors before they fail completely. If your lock is getting slow or unreliable, plan a replacement before it locks you out.",
 faqs=[
  ("My old Gateman lock is slow to open. Should I replace it?", "Slow motors and unreliable keypads are common warning signs on older locks. Replacing it before it fails avoids an emergency lockout."),
  ("How do I wake a Gateman lock with a flat battery?", "On many models, hold a 9V battery to the emergency contacts on the outside and enter your code. Check your manual for your model."),
 ]),
}

TIPS = {'Samsung': ["Keep a 9V battery in your bag or car if your model uses 9V emergency power — it's the quickest way back in.", 'Older Samsung keypads can wear out; if some buttons need a hard press, plan a replacement.', 'Gate rim locks take the most weather — wipe the keypad dry after heavy rain or corridor washing.', 'Register a second fingerprint or card for a family member in case yours fails.'], 'Yale': ["Learn where your model's emergency power point is — 9V on many models, USB on some newer ones.", 'If your lock has a privacy or double-lock mode, make sure everyone at home knows how it works.', "Smart Yale models with app control still need batteries — the app can't open a lock with no power.", 'Keep the override key outside the home, not in a drawer inside.'], 'Philips': ['Check whether your model takes USB or 9V emergency power, and keep the right cable or battery handy.', 'Enrol two fingers per person — if one is cut or dry, the other usually still works.', 'Push-pull handles take a lot of force; if the handle feels loose, get it checked before it fails.', 'Use good-quality batteries; cheap ones can drain quickly in a busy household.'], 'Igloohome': ['Keep your app login details somewhere you can reach from another device.', 'For rentals, set guest codes with clear start and end times, and check them before guests arrive.', 'Keep the mechanical backup key (if your model has one) outside the property.', "Replace batteries as soon as the app or lock warns you — don't wait for it to die."], 'Gateman': ['If your Gateman is more than a few years old, test the emergency power point now so you know it still works.', 'A lock that opens more slowly than it used to may be close to failing — plan a replacement.', 'Keep a 9V battery handy if your model uses 9V emergency power.', 'Check that gate-mounted models are protected from direct rain where possible.']}

BRANDS = [dict(name=b, slug=b.lower(), tips=TIPS.get(b, []), **DATA[b]) for b in C.BRAND_PAGES if b in DATA]


def build(x):
    for b in BRANDS:
        n = b["name"]
        path = f"digital-lock-opening/{b['slug']}/"
        crumbs = [("Home", ""), ("Services", "services/"), ("Digital lock opening", "digital-lock-opening/"), (n, path)]
        title = f"{n} Digital Lock Opening Singapore 24/7 | From S$150"
        desc = (f"{n} digital lock won't open? Flat battery, forgotten PIN, dead keypad or wrong-code lockout — what to try first, "
                f"and 24/7 help from S$150. Call 9224 9224.")
        if len(desc) > 158:
            desc = f"{n} digital lock won't open? What to try first for a flat battery, forgotten PIN or dead keypad — and 24/7 help from S$150."
        faqs = b["faqs"] + [
            (f"How much does it cost to open a {n} digital lock?", "Digital lock emergency opening starts from {P_DIGITAL_OPEN}. WhatsApp a photo of the lock (front and inside if possible) for an exact price."),
            (f"Do you repair {n} digital locks?", f"No — we don't do repairs. We open the lock, and if it's faulty we can replace it. For warranty repairs, contact {n} or your retailer."),
        ]
        others = " · ".join(f'<a href="~/digital-lock-opening/{o["slug"]}/">{o["name"]}</a>' for o in BRANDS if o["slug"] != b["slug"])
        body = (x["page_hero"](crumbs, f"{n} Digital Lock Won't Open? 24/7 Help in Singapore",
                f"Flat battery, forgotten PIN, dead keypad or locked out after too many wrong tries — here's what to try first with your {n} lock, and how Uncle Thomas can open it, damage-free wherever possible.",
                ["From {P_DIGITAL_OPEN}", "24/7 islandwide", "Damage-free first"]) +
                f'''<section class="section"><div class="container narrow prose">
<h2>{n} digital locks in Singapore</h2>
<p>{b["about"]}</p>
<h2>Common {n} digital lock problems</h2>
<h3>Flat battery</h3>
<p>{b["power"]}</p>
<h3>Forgotten PIN or fingerprint not recognised</h3>
<p>{b["backup"]}</p>
<h3>Keypad dead, or the lock won't respond</h3>
<p>{b["quirk"]} Rain and condensation can also stop a keypad responding — dry it gently and wait a few minutes.</p>
<h3>Locked out after too many wrong attempts</h3>
<p>Most locks freeze the keypad for a few minutes after repeated wrong codes. Wait for the time-out, then enter your code once, carefully.</p>
<h2>Tips for {n} owners</h2>
<ul>{"".join(f"<li>{tip}</li>" for tip in b["tips"])}</ul>
<p>More general checks are in our guide: <a href="~/guides/digital-lock-battery-dead/">digital lock battery dead or won't open</a>.</p>
<h2>When to call us</h2>
<p>If none of this works — or the lock responds but the door still won't open — call or WhatsApp us. Please don't force the handle; it can break the motor. Uncle Thomas has his own damage-free methods for faulty digital locks, and we explain the options and price before starting.</p>

<h2>Price</h2>
<p>{n} digital lock emergency opening starts from <strong>{{P_DIGITAL_OPEN}}</strong>. WhatsApp a photo of the lock to {{PHONE}} for an exact price before we come. If the lock is beyond saving, we can <a href="~/digital-lock-installation/">install a new digital lock</a> — every installation comes with our no-expiry warranty. See all <a href="~/prices/">prices</a>.</p>
<div class="callout"><p><strong>Security first:</strong> we check proof of residence before opening any door. Uncle Thomas Locksmith is an independent locksmith and is not affiliated with {n}.</p></div>
<p>Other brands: {others} · <a href="~/digital-lock-opening/">all digital lock brands</a></p>
</div></section>
<section class="section section-alt"><div class="container narrow">{x["faq_html"](faqs, f"{n} Digital Lock FAQs")}</div></section>''' +
                x["cta_band"](f"Locked Out by Your {n} Lock?"))
        svc = {"@type": "Service", "@id": x["C"].SITE + "/" + path + "#service",
               "name": f"{n} digital lock opening — Singapore", "serviceType": "Digital lock opening",
               "description": desc, "provider": {"@id": x["BUSINESS_ID"]},
               "areaServed": {"@type": "Country", "name": "Singapore"}, "url": x["C"].SITE + "/" + path,
               "offers": {"@type": "Offer", "priceCurrency": "SGD",
                          "priceSpecification": {"@type": "PriceSpecification", "minPrice": 150, "priceCurrency": "SGD"}}}
        nodes = x["page_schema"](path, title, desc, crumbs, faqs=faqs, extra=[svc])
        x["render"](path, title, desc, body, nodes, priority="0.7")
