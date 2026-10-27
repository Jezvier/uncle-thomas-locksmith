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
"Kaadas": dict(
 about="Kaadas digital and smart locks have become a common sight on Singapore HDB gates and main doors, often fitted as a matching gate-and-door set with fingerprint, PIN and card access.",
 power="Many Kaadas models take emergency power from outside, commonly through a USB port near the bottom of the lock. Check your model's manual so you know which cable to carry.",
 backup="Many Kaadas models include a mechanical backup key behind a small cover. If yours came with one, keep it outside the home.",
 quirk="Gate and door sets mean two locks and two sets of batteries. If one lock in the pair starts acting up, check its batteries separately.",
 faqs=[
  ("How do I open a Kaadas lock with a flat battery?", "On many models, plug a power bank into the emergency USB port to wake the lock, then enter your code. If your model has a backup key, that works without power."),
  ("My Kaadas gate lock works but the door lock doesn't. Why?", "They usually run on separate batteries. Check the door lock's batteries first. If it still won't respond, call us."),
 ]),
"Solity": dict(
 about="Solity is a Korean digital lock brand found on many Singapore HDB and condo doors, with push-pull and gate models that use fingerprint, PIN and card access.",
 power="Many Solity models have an emergency power option on the outside, either a 9V battery terminal or a USB port depending on the model. Your manual will confirm which.",
 backup="Some Solity models include a mechanical override key and some don't. If yours did, keep it outside the home.",
 quirk="A Solity lock that beeps but won't turn the latch may have a weak battery or a mechanical problem in the lock body rather than a wrong code.",
 faqs=[
  ("Where is the emergency power point on a Solity lock?", "It depends on the model; many have a 9V terminal or USB port on the outside. Check your manual, or send us a photo."),
  ("My Solity lock accepts the code but won't open. What's wrong?", "Usually a low battery or a mechanical fault in the lock body. Don't force the handle. Call us and we'll open it."),
 ]),
"Häfele": dict(
 about="Häfele digital and smart locks are often fitted by interior designers and renovation contractors in Singapore condos and HDB flats, from simple keypad locks to app-connected smart locks.",
 power="Many Häfele models accept emergency power from outside through a USB port or battery contacts. Check your model's manual so you're prepared.",
 backup="Many Häfele models include a mechanical backup key. If your contractor handed one over at the end of the renovation, keep it outside the home.",
 quirk="If your lock was installed during a renovation, the admin PIN or app account may still be under the contractor's details. Ask them to hand it over so you can manage it yourself.",
 faqs=[
  ("My Häfele lock was installed by my contractor and I don't know the master PIN. Can you help?", "If you're locked out, yes, we'll open it. For resetting the master PIN, check the manual or ask your contractor or Häfele first."),
  ("How do I power a Häfele lock with flat batteries?", "Many models take emergency power through USB or battery contacts on the outside. Check your manual for your model."),
 ]),
"Aqara": dict(
 about="Aqara smart locks are popular with Singapore homeowners who run a smart home, as they connect to the Aqara app and smart home systems, with fingerprint, PIN, card and app unlocking.",
 power="Aqara smart locks run on batteries even when connected to Wi-Fi or a hub. Many models have an emergency USB power port outside for when the batteries die.",
 backup="Many Aqara models include a mechanical backup key. The app can't open the lock if the lock itself has no power, so keep the key handy.",
 quirk="If the app shows the lock offline, it may just be the hub or Wi-Fi rather than the lock. Try PIN or fingerprint at the door before assuming the lock has failed.",
 faqs=[
  ("Can I open my Aqara smart lock from the app if I'm locked out?", "If the lock has power and is online, often yes. If the batteries are flat or it's offline, use emergency USB power or the backup key, or call us."),
  ("My Aqara lock shows offline in the app. Is it broken?", "Not necessarily. Check your hub and Wi-Fi. The lock usually still works with PIN or fingerprint at the door."),
 ]),
"Xiaomi": dict(
 about="Xiaomi smart door locks are bought online by many Singapore homeowners for their app control and price, and are often fitted to HDB and condo main doors.",
 power="Many Xiaomi smart locks have an emergency USB-C port on the outside to wake the lock when the batteries are flat. Check your model's manual.",
 backup="Many Xiaomi models come with mechanical backup keys. Keep one outside the home in case the batteries die.",
 quirk="Locks bought online sometimes don't suit the door's thickness or cut-outs, which leads to latch problems later. If your lock sticks, the fit may be the issue.",
 faqs=[
  ("I bought a Xiaomi smart lock online. Can you install it?", "Yes. Send us a photo of the lock and your door first, so we can confirm it will fit before we come."),
  ("How do I wake a Xiaomi smart lock with flat batteries?", "On many models, connect a power bank to the emergency USB-C port outside, then unlock with your PIN or fingerprint."),
 ]),
"Lenovo": dict(
 about="Lenovo smart locks are found in a growing number of Singapore homes, typically with fingerprint, PIN and app access.",
 power="Like all smart locks, Lenovo models run on batteries. Many have an emergency USB port outside to wake the lock when the batteries are flat. Check your manual.",
 backup="If your Lenovo lock came with a mechanical backup key, keep it outside the home.",
 quirk="If your phone app can't reach the lock, try PIN or fingerprint at the door; the app connection and the lock itself are separate.",
 faqs=[
  ("Can you open a Lenovo smart lock?", "Yes. We open all digital and smart lock brands, including Lenovo, 24/7."),
  ("My Lenovo smart lock battery died. What do I do?", "Use the emergency USB port if your model has one, or the backup key. If that doesn't work, call us."),
 ]),

}

TIPS = {'Samsung': ["Keep a 9V battery in your bag or car if your model uses 9V emergency power — it's the quickest way back in.", 'Older Samsung keypads can wear out; if some buttons need a hard press, plan a replacement.', 'Gate rim locks take the most weather — wipe the keypad dry after heavy rain or corridor washing.', 'Register a second fingerprint or card for a family member in case yours fails.'], 'Yale': ["Learn where your model's emergency power point is — 9V on many models, USB on some newer ones.", 'If your lock has a privacy or double-lock mode, make sure everyone at home knows how it works.', "Smart Yale models with app control still need batteries — the app can't open a lock with no power.", 'Keep the override key outside the home, not in a drawer inside.'], 'Philips': ['Check whether your model takes USB or 9V emergency power, and keep the right cable or battery handy.', 'Enrol two fingers per person — if one is cut or dry, the other usually still works.', 'Push-pull handles take a lot of force; if the handle feels loose, get it checked before it fails.', 'Use good-quality batteries; cheap ones can drain quickly in a busy household.'], 'Igloohome': ['Keep your app login details somewhere you can reach from another device.', 'For rentals, set guest codes with clear start and end times, and check them before guests arrive.', 'Keep the mechanical backup key (if your model has one) outside the property.', "Replace batteries as soon as the app or lock warns you — don't wait for it to die."], 'Gateman': ['If your Gateman is more than a few years old, test the emergency power point now so you know it still works.', 'A lock that opens more slowly than it used to may be close to failing — plan a replacement.', 'Keep a 9V battery handy if your model uses 9V emergency power.', 'Check that gate-mounted models are protected from direct rain where possible.']}

TIPS.update({
 "Kaadas": ["Carry a small power bank and USB cable if your model uses USB emergency power.", "Change the batteries in the gate and door locks at the same time.", "Register a second fingerprint per person in case one fails.", "Keep the backup key outside the home."],
 "Solity": ["Find out whether your model uses 9V or USB emergency power before you need it.", "If the latch is getting stiff, get it checked before it jams.", "Replace batteries as soon as the low-battery warning sounds.", "Keep the override key (if any) outside the home."],
 "Häfele": ["Get the master PIN and app account handed over from your contractor.", "Check whether your model uses USB or battery-contact emergency power.", "Keep the backup key outside the home.", "Replace batteries at the first low-battery warning."],
 "Aqara": ["Keep the backup key somewhere you can reach from outside.", "A power bank and USB cable can wake many models when the batteries die.", "Don't rely on the app alone; set up PIN and fingerprint too.", "Replace batteries when the app warns you, not after they die."],
 "Xiaomi": ["Keep a USB-C cable and power bank handy for emergency power.", "Check the lock fits your door's thickness before buying.", "Store a backup key outside the home.", "Set up a second unlocking method in case the app or fingerprint fails."],
 "Lenovo": ["Learn where your model's emergency power port is.", "Set up PIN as well as fingerprint and app access.", "Keep any backup key outside the home.", "Replace batteries at the first warning."],
})

import unicodedata as _u, re as _re
def _slug(n):
    return _re.sub(r'[^a-z0-9]+', '-', _u.normalize('NFKD', n).encode('ascii', 'ignore').decode().lower()).strip('-')

BRANDS = [dict(name=b, slug=_slug(b), tips=TIPS.get(b, []), **DATA[b]) for b in C.BRAND_PAGES if b in DATA]


def build(x):
    for b in BRANDS:
        n = b["name"]
        path = f"digital-lock-opening/{b['slug']}/"
        crumbs = [("Home", ""), ("Services", "services/"), ("Digital lock opening", "digital-lock-opening/"), (n, path)]
        title = f"{n} Digital & Smart Lock Opening Singapore 24/7"
        desc = (f"{n} digital or smart lock won't open? Flat battery, forgotten PIN, dead keypad or wrong-code lockout — what to try first, "
                f"and 24/7 help from S$150. Call 9224 9224.")
        if len(desc) > 158:
            desc = f"{n} digital lock won't open? What to try first for a flat battery, forgotten PIN or dead keypad — and 24/7 help from S$150."
        faqs = b["faqs"] + [
            (f"How much does it cost to open a {n} digital lock?", "Digital lock emergency opening starts from {P_DIGITAL_OPEN}. WhatsApp a photo of the lock (front and inside if possible) for an exact price."),
            (f"Do you repair {n} digital locks?", f"No — we don't do repairs. We open the lock, and if it's faulty we can replace it. For warranty repairs, contact {n} or your retailer."),
        ]
        jobs = getattr(x["C"], "BRAND_JOBS", {}).get(n, [])
        recent = "".join(f'<div class="callout"><p><strong>Recent job:</strong> {j}</p></div>' for j in jobs)
        others = " · ".join(f'<a href="~/digital-lock-opening/{o["slug"]}/">{o["name"]}</a>' for o in BRANDS if o["slug"] != b["slug"])
        body = (x["page_hero"](crumbs, f"{n} Digital Lock or Smart Lock Won't Open? 24/7 Help in Singapore",
                f"Flat battery, forgotten PIN, dead keypad or locked out after too many wrong tries — here's what to try first with your {n} lock, and how Uncle Thomas can open it, damage-free wherever possible.",
                ["From {P_DIGITAL_OPEN}", "24/7 islandwide", "Damage-free first"]) +
                f'''<section class="section"><div class="container narrow prose">
<h2>{n} digital locks and smart locks in Singapore</h2>
<p>{b["about"]}</p>
{recent}<h2>A typical {n} call</h2>
<p>This is the kind of {n} call we often get: {SCENARIO.get(n, "")}</p>
<h2>What's different about {n} locks</h2>
<p>{FEATURE.get(n, "")}</p>
<h2>Common {n} problems and what to try</h2>
<h3>Flat battery</h3>
<p>{b["power"]}</p>
<h3>Forgotten PIN or fingerprint not recognised</h3>
<p>{b["backup"]}</p>
<h3>Lock won't respond</h3>
<p>{b["quirk"]}</p>
<h2>Tips for {n} owners</h2>
<ul>{"".join(f"<li>{tip}</li>" for tip in b["tips"])}</ul>
<p><strong>Still locked out?</strong> Don't force the handle. Call or WhatsApp {{PHONE}}: {n} opening from {{P_DIGITAL_OPEN}}, price confirmed first, ID checked. Independent locksmith, not affiliated with {n}. General checks: <a href="~/guides/digital-lock-battery-dead/">digital lock battery dead</a> · <a href="~/guides/forgot-digital-lock-pin/">forgot your PIN</a>.</p>
<p>Other brands: {others} · <a href="~/digital-lock-opening/">all digital lock brands</a></p>
</div></section>
<section class="section section-alt"><div class="container narrow">{x["faq_html"](faqs, f"{n} Digital Lock FAQs")}</div></section>''' +
                x["cta_band"](f"Locked Out by Your {n} Lock?"))
        svc = {"@type": "Service", "@id": x["C"].SITE + "/" + path + "#service",
               "name": f"{n} digital lock and smart lock opening — Singapore", "serviceType": "Digital lock and smart lock opening",
               "description": desc, "provider": {"@id": x["BUSINESS_ID"]},
               "areaServed": {"@type": "Country", "name": "Singapore"}, "url": x["C"].SITE + "/" + path,
               "offers": {"@type": "Offer", "priceCurrency": "SGD",
                          "priceSpecification": {"@type": "PriceSpecification", "minPrice": 150, "priceCurrency": "SGD"}}}
        nodes = x["page_schema"](path, title, desc, crumbs, faqs=faqs, extra=[svc])
        x["render"](path, title, desc, body, nodes, priority="0.7")


# ---------------------------------------------------------------------------
# Brand-specific depth (27 Oct 2026). SCENARIO = a realistic *typical* call,
# framed as typical on the page, never as a dated real job.
SCENARIO = {
"Samsung": "An elderly couple in an older HDB flat come home from a family dinner to find the Samsung gate lock completely dark. The batteries ran flat while they were out, and they don't know about the 9V emergency contacts. We get them in, then show them where the contacts are and which battery to keep in their bag.",
"Yale": "Someone at home switches the Yale lock to privacy mode before bed. The other half of the household comes home after a late shift, and the keypad refuses a code they know is right. If no one inside wakes up, we open it, and then explain how privacy mode works.",
"Philips": "A family back from a holiday finds their Philips push-pull lock dead after two weeks of draining batteries. Their model takes USB emergency power, but the power bank and cable are packed deep in a suitcase. If they can't find them, we open the lock and the batteries get replaced.",
"Igloohome": "A landlord set a tenant's access code to run until the end of the month. The tenant renewed, but nobody extended the code, and on the 1st it stops working. Usually the landlord can fix it in the app; when they can't be reached, we're the backup.",
"Gateman": "A Gateman lock that has served a flat for about ten years has been getting slower: the motor hums and hesitates. One evening it doesn't finish turning at all, with the owner outside. We open it, and the owner decides it's time for a new lock.",
"Kaadas": "A household with a matching Kaadas gate and door set finds the gate lock dead while the door lock still works. The two run on separate batteries, and the gate's ran out first. We get them through the gate, and they change both sets of batteries together from then on.",
"Solity": "Someone pushed hard on a Solity handle when the lock was slow to respond. Now the code is accepted and the motor runs, but the latch won't pull back. That's a mechanical fault rather than a battery one, so we open the door and talk through replacing the lock body or the whole lock.",
"Häfele": "A new condo owner moves in after a renovation and realises the contractor never handed over the Häfele master PIN or app account. Day to day the codes work, until a code needs changing. We open locks when people are locked out; for the master PIN, the contractor or Häfele is the first call.",
"Aqara": "After changing their home Wi-Fi router, a family's Aqara smart lock shows offline in the app. They've only ever used app unlocking. The lock still accepts PIN and fingerprint at the door; if those were never set up, we're the next step.",
"Xiaomi": "An owner bought a Xiaomi smart lock online and fitted it themselves. A few weeks later the latch catches on the strike plate and the door won't open from outside. We open it and check how the lock sits on the door.",
"Lenovo": "Only one person in a household set up fingerprints on the Lenovo smart lock, and the app lives on their phone. When they're overseas, the rest of the family has only the PIN, and when that's forgotten, they call us.",
}

FEATURE = {
"Samsung": "Samsung's range in Singapore spans rim gate locks and push-pull mortise main door locks, from older keypad-only models to newer ones with fingerprint and card. Older units are the ones we most often see with tired keypads.",
"Yale": "Many Yale models have a privacy or double-lock mode that blocks outside codes, and newer smart models add app control. That mix of mechanical override, privacy settings and app features is why Yale lockouts usually have a simple cause.",
"Philips": "Philips EasyKey push-pull locks are popular on HDB and condo main doors. The push-pull handle takes a lot of daily force, so a loose or stiff handle is an early warning sign worth acting on.",
"Igloohome": "Igloohome is a Singapore-founded smart lock brand built around app access and time-limited codes, which makes it popular with landlords. Most lockouts we see are about code settings rather than a broken lock.",
"Gateman": "Gateman locks have been fitted in Singapore for many years, so many are now older units. Ageing motors and keypads tend to give warning signs, slower opening or keys that need a hard press, before they fail.",
"Kaadas": "Kaadas is often sold as a matching gate-and-door set with fingerprint, PIN and card access, and many models take USB emergency power. Two locks means two sets of batteries to keep an eye on.",
"Solity": "Solity is a Korean brand found on many Singapore HDB and condo doors. Emergency power and override options vary by model, so knowing your model number saves time when something goes wrong.",
"Häfele": "Häfele locks are often chosen and installed by renovation contractors and interior designers. That's why the most common Häfele problem isn't the lock but who holds the master PIN and app account.",
"Aqara": "Aqara smart locks are built for smart homes, with app, hub and automation features. The lock and the network are separate, so an offline app doesn't mean a dead lock.",
"Xiaomi": "Xiaomi smart locks are often bought online for their price and app features, and many are self-installed. Fit matters: door thickness and cut-outs decide whether the latch works smoothly.",
"Lenovo": "Lenovo smart locks combine fingerprint, PIN and app access. They're most reliable when every household member has their own fingerprint and PIN, not just the person who set up the app.",
}
