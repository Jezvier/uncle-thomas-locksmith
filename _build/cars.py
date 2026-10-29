"""
Car brand pages: /car-locksmith/<brand>/

Only brands in config.CAR_BRAND_PAGES are built (Tesla is never listed — owner's
instruction). Brand details are written cautiously ("many models…") because key
types vary by model and year. We are independent and not affiliated with any brand.
"""
import unicodedata, re
import config as C


def slug(name):
    s = unicodedata.normalize("NFKD", name).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")


DATA = {
"Toyota": dict(
 models="Corolla Altis, Camry, Corolla Cross, C-HR, Prius, Alphard, Vellfire and Hiace vans",
 about="Toyota is one of the most common car brands on Singapore roads, from family Corolla Altis and Camry sedans to Alphard and Vellfire MPVs and Hiace vans used by businesses.",
 keys="Newer Toyotas mostly use a smart key: you keep it in your pocket, the doors unlock when you touch the handle, and you press a button to start. Older models use a remote key with a metal blade. Most Toyota smart keys hide a small mechanical key inside the fob for emergencies.",
 tips=["If your smart key battery is dying, many Toyotas still start if you hold the fob against the start button. Check your manual for your model.",
       "Slide out the hidden mechanical key now and learn where the hidden keyhole on the driver's door is, before you need it.",
       "Businesses running Hiace vans should keep a spare fob at the office, as one lost key can stop a delivery day."],
 faqs=[("Can you clone a Toyota smart key?", "Yes, for most Toyota models. Send us the model, year and a photo of the key for a quote."),
       ("My Toyota smart key battery is flat. How do I get in?", "Most Toyota smart keys hide a mechanical key inside. Use it in the driver's door. If that fails, call us.")]),
"Honda": dict(
 models="Vezel, HR-V, Civic, Jazz, Fit, Shuttle, Freed and Odyssey",
 about="Honda is a favourite in Singapore, especially the Vezel and Civic, along with practical cars like the Jazz, Shuttle and Freed that families and private-hire drivers rely on every day.",
 keys="Many newer Hondas use a smart entry key with push-button start. Older models use a remote key with a flip-out or fixed metal blade. Smart keys usually contain a hidden mechanical key for when the battery dies.",
 tips=["Private-hire drivers: a spare fob is cheap insurance, because a lost key means lost earnings while you wait.",
       "If the remote range is getting shorter, change the fob battery before it dies completely.",
       "Keep the spare fob at home, not in the glovebox."],
 faqs=[("Can you make a spare Honda Vezel key?", "Yes, we clone key fobs for most Honda models, including the Vezel. Send the year and a photo of your key for a quote."),
       ("I locked my keys inside my Honda. Can you open it without damage?", "Yes. We use non-destructive tools that don't damage the paint, seals or windows.")]),
"Mercedes-Benz": dict(
 models="A-Class, C-Class, E-Class, GLA, GLC and S-Class",
 about="Mercedes-Benz is one of Singapore's best-selling luxury brands, with the C-Class, E-Class and GLC especially common in condo carparks and company fleets.",
 keys="Many Mercedes-Benz models use a smart key, often with KEYLESS-GO so you can unlock and start without taking the key out. An emergency key blade usually slides out of the fob for the door lock.",
 tips=["Learn how to release the emergency key blade from your fob; on most models it slides out from the back.",
       "Keyless entry keys can drain faster if stored near the car. Keep the spare away from the garage.",
       "Company fleet managers: keep a spare fob for each car to avoid downtime."],
 faqs=[("Can you clone a Mercedes-Benz key fob?", "We clone key fobs for many Mercedes-Benz models. Send the model, year and a photo of the key and we'll confirm before you book."),
       ("My Mercedes won't unlock with the fob. What should I try?", "Use the emergency key blade in the driver's door. If the car still won't open, call us; we'll open it without damage.")]),
"BMW": dict(
 models="1 Series, 3 Series, 5 Series, X1, X3, X5 and iX",
 about="BMW is a common sight in Singapore, from 3 Series and 5 Series sedans to X1, X3 and X5 SUVs, owned by families and companies alike.",
 keys="BMWs use remote keys and, on many models, Comfort Access, which unlocks the car when you touch the handle. Some newer models use a display key. Most BMW keys hold a small emergency key blade.",
 tips=["Find the emergency key blade in your fob now; on many models it's released by a small button on the side.",
       "If the remote stops working, try holding the key against the marked spot on the steering column to start the car (check your manual).",
       "Keep a spare fob, because a BMW key from the dealer can take a while."],
 faqs=[("Can you make a spare BMW key?", "We clone key fobs for many BMW models. Send us the model, year and a photo of your key so we can confirm and quote."),
       ("Can you open a locked BMW without damaging it?", "Yes. Our tools open the door without damaging the paint, seals or windows.")]),
"Audi": dict(
 models="A3, A4, A6, Q3, Q5 and Q7",
 about="Audi models like the A4, A6, Q3 and Q5 are popular with Singapore professionals and families who want a quiet, well-built car.",
 keys="Audi uses remote flip keys on many models and an advanced (keyless) key on others. Most keyless Audi fobs contain an emergency key blade for the door.",
 tips=["Learn where the hidden keyhole is on your driver's door; on some models it sits under a small cover on the handle.",
       "If the fob only works up close, replace its battery before it fails.",
       "Keep the spare fob at home, not in the car."],
 faqs=[("Can you clone an Audi key fob?", "Yes, for many Audi models. Send us the model, year and a photo of the key for a quote."),
       ("My Audi is locked with the key inside. Can you help?", "Yes, 24/7 anywhere in Singapore, using non-destructive car entry tools.")]),
"Volkswagen": dict(
 models="Golf, Polo, Jetta, Passat, Tiguan and Touran",
 about="Volkswagen's Golf, Polo, Passat and Tiguan are well-loved in Singapore for being practical and fun to drive.",
 keys="Many Volkswagens use a flip key: a remote fob with a metal blade that folds out. Some newer models use keyless entry and start.",
 tips=["A worn flip-key hinge can snap; if yours feels loose, get a spare before it breaks.",
       "Keep the spare key at home rather than in the car.",
       "Replace the fob battery when the remote range starts to drop."],
 faqs=[("Can you copy a Volkswagen flip key?", "Yes, we clone key fobs for many Volkswagen models. Send a photo of the key and the model and year."),
       ("Can you open my Volkswagen if the keys are locked inside?", "Yes, using non-destructive tools, 24/7 islandwide.")]),
"Mazda": dict(
 models="Mazda2, Mazda3, Mazda6, CX-3, CX-30, CX-5 and CX-8",
 about="Mazda is popular in Singapore for good-looking, reliable cars, especially the Mazda3, CX-30 and CX-5.",
 keys="Mazdas use either a remote key with a blade or a smart key for keyless entry and push-button start. Smart keys usually hide an emergency key inside.",
 tips=["If your smart key battery is weak, many Mazdas start if you hold the key close to the start button. Check your manual.",
       "Find the hidden emergency key in your fob before you need it.",
       "A spare key avoids a long wait if one goes missing."],
 faqs=[("Can you clone a Mazda smart key?", "Yes, for most Mazda models. Send the model, year and a photo of the key for a quote."),
       ("Can you unlock a Mazda CX-5 with the key inside?", "Yes. We open it without damage, 24/7.")]),
"Lexus": dict(
 models="ES, IS, NX, RX, UX and LM",
 about="Lexus is a popular premium choice in Singapore, from the ES sedan to NX and RX SUVs.",
 keys="Lexus models use smart keys for keyless entry and push-button start, and some models come with a slim card key as well. A mechanical key is usually hidden inside the fob.",
 tips=["If your model came with a card key, keep it in your wallet as a backup.",
       "Learn where the hidden keyhole is on the driver's door.",
       "Replace the smart key battery as soon as the car warns you it's low."],
 faqs=[("Can you clone a Lexus key?", "Yes, for many Lexus models. Send the model, year and a photo of the key and we'll confirm."),
       ("My Lexus smart key isn't detected. What should I do?", "Try the hidden mechanical key, and hold the fob close to the start button. If you're still stuck, call us.")]),
"Land Rover": dict(
 models="Range Rover, Range Rover Sport, Range Rover Evoque, Range Rover Velar, Defender and Discovery",
 about="Land Rover and Range Rover models, including the Evoque, Velar, Defender and Discovery, have a loyal following in Singapore.",
 keys="Most Land Rover and Range Rover models use smart keys with keyless entry and start, with an emergency key blade inside the fob for the door.",
 tips=["Find the emergency key blade in your fob before you need it.",
       "Keyless keys can be affected by a weak battery; replace it when the car warns you.",
       "A spare fob is worth having, as dealer keys can take time."],
 faqs=[("Can you clone a Range Rover key fob?", "We clone key fobs for many Land Rover and Range Rover models. Send the model, year and a photo of the key for a quote."),
       ("Can you open a locked Range Rover?", "Yes, without damaging the paint, seals or windows, 24/7.")]),
"Hyundai": dict(
 models="Avante, Elantra, Ioniq, Kona, Tucson and Santa Fe",
 about="Hyundai's Avante, Ioniq and Kona are common in Singapore, including many private-hire and electric models.",
 keys="Hyundais use remote flip keys on many models and smart keys with push-button start on others. Smart keys usually contain a mechanical key for emergencies.",
 tips=["Private-hire drivers: keep a spare fob so a lost key doesn't cost you a day's work.",
       "Slide out the mechanical key and find the driver's door keyhole now.",
       "Change the fob battery when the remote range drops."],
 faqs=[("Can you make a spare Hyundai key fob?", "Yes, for most Hyundai models. Send the model, year and a photo of the key for a quote."),
       ("My Hyundai is locked with the key inside. Can you open it?", "Yes, using non-destructive tools, 24/7 islandwide.")]),
"Kia": dict(
 models="Cerato, Niro, Seltos, Sportage, Sorento, Carnival and EV6",
 about="Kia's Cerato, Niro, Sportage and EV6 are popular in Singapore with families and private-hire drivers.",
 keys="Kias use remote flip keys or smart keys depending on the model. Smart keys usually hide an emergency key inside.",
 tips=["Keep a spare fob at home in case the main one goes missing.",
       "Learn where the emergency key and hidden keyhole are on your model.",
       "Replace the fob battery before it dies."],
 faqs=[("Can you clone a Kia smart key?", "Yes, for most Kia models. Send the model, year and a photo of the key for a quote."),
       ("Can you open a Kia without damaging it?", "Yes. Our tools open the door without damaging the paint, seals or windows.")]),
"Nissan": dict(
 models="Sylphy, Qashqai, X-Trail, Kicks, Serena and Note",
 about="Nissan is a long-time favourite in Singapore, from the Sylphy and Qashqai to the Serena MPV and Kicks e-Power.",
 keys="Many Nissans use an Intelligent Key for keyless entry and push-button start, with an emergency key inside the fob. Older models use remote keys with a metal blade.",
 tips=["If your Intelligent Key battery is low, many Nissans start if you touch the key to the start button. Check your manual.",
       "Find the hidden mechanical key in the fob before you need it.",
       "Keep the spare key at home rather than in the car."],
 faqs=[("Can you clone a Nissan Intelligent Key?", "Yes, for most Nissan models. Send the model, year and a photo of the key for a quote."),
       ("Can you unlock a Nissan with the keys inside?", "Yes, 24/7 islandwide, without damage.")]),
"Porsche": dict(
 models="911, Cayenne, Macan, Panamera and Taycan",
 about="Porsche owners in Singapore, from the 911 to the Cayenne and Macan, expect careful, damage-free work, and that's how we work.",
 keys="Porsche keys are car-shaped remote fobs, and many models offer keyless entry and start. Most fobs contain an emergency key for the door.",
 tips=["Learn how to release the emergency key from your fob.",
       "Keep the spare fob somewhere safe at home.",
       "Replace the fob battery as soon as the car warns you."],
 faqs=[("Can you clone a Porsche key fob?", "We clone key fobs for many Porsche models. Send the model, year and a photo of the key and we'll confirm before you book."),
       ("Will opening my Porsche damage it?", "No. We use non-destructive tools that protect the paint, seals and windows.")]),
"Volvo": dict(
 models="XC40, XC60, XC90, S60, S90 and V60",
 about="Volvo's XC40, XC60 and XC90 are popular with Singapore families who put safety first.",
 keys="Volvos use remote keys and, on many models, keyless entry and start. Many keys contain a detachable emergency key blade.",
 tips=["Find the detachable key blade in your fob now.",
       "Replace the fob battery when the car warns you.",
       "Keep a spare fob at home."],
 faqs=[("Can you clone a Volvo key?", "Yes, for many Volvo models. Send the model, year and a photo of the key for a quote."),
       ("Can you open a locked Volvo XC60?", "Yes, without damage, 24/7 islandwide.")]),
"Mitsubishi": dict(
 models="Attrage, Outlander, Xpander, ASX and Lancer",
 about="Mitsubishi's Attrage, Outlander and Xpander are practical favourites in Singapore, including with private-hire drivers.",
 keys="Mitsubishis use remote keys with a metal blade on many models and keyless operation keys with push-button start on others.",
 tips=["A spare key avoids downtime if you drive for a living.",
       "Replace the fob battery when the remote range starts to drop.",
       "Keep the spare key at home rather than in the car."],
 faqs=[("Can you make a spare Mitsubishi key fob?", "Yes, for most Mitsubishi models. Send the model, year and a photo of the key for a quote."),
       ("Can you open my Mitsubishi with the keys locked inside?", "Yes, using non-destructive tools, 24/7.")]),
"Subaru": dict(
 models="Forester, XV, Crosstrek, Impreza, Outback and WRX",
 about="Subaru has a loyal following in Singapore, especially the Forester, XV and WRX.",
 keys="Subarus use remote keys with a blade on some models and a keyless access smart key on others, usually with an emergency key inside.",
 tips=["Find the emergency key in your smart key before you need it.",
       "Replace the fob battery when the car warns you.",
       "Keep the spare key at home."],
 faqs=[("Can you clone a Subaru key?", "Yes, for most Subaru models. Send the model, year and a photo of the key for a quote."),
       ("Can you unlock a Subaru with the key inside?", "Yes, 24/7 islandwide, without damage.")]),
}

# Added 29 Oct 2026: BYD (Singapore's best-selling brand in 2025), MG, Mini, Skoda, Peugeot, Suzuki.
DATA.update({
"BYD": dict(
 models="Atto 3, Dolphin, Seal, Sealion 7, M6 and Atto 2",
 about="BYD was Singapore's best-selling car brand in 2025 for the second year running, with 11,184 new cars registered, so its electric Atto 3, Dolphin, Seal and Sealion models are now everywhere from HDB carparks to private-hire fleets.",
 keys="BYD cars lean on digital keys: a smart key fob, and on many models an NFC card key and a phone digital key in the BYD app. An NFC card needs no battery, which makes it the best backup to carry.",
 tips=["Keep the NFC card key in your wallet, not in the car: it's the backup that works when the fob battery or your phone dies.",
       "A phone digital key is only as good as your phone's battery. Carry the card or fob too.",
       "Replace the fob battery at the first low-battery warning on the dashboard."],
 faqs=[("Can you open a BYD with the key locked inside?", "Yes. We open BYD cars without damaging the paint, seals or windows, 24/7 islandwide."),
       ("Can you make a spare BYD key?", "It depends on the model and key system. WhatsApp {PHONE} the model, year and a photo of your key or card, and we'll confirm before you book.")]),
"MG": dict(
 models="MG4, MG ZS EV, MG5 and HS",
 about="MG, owned by China's SAIC Motor, sells electric and petrol models such as the MG4 and MG ZS EV in Singapore, popular with families and private-hire drivers who want an affordable EV.",
 keys="Many MG models use a smart key with keyless entry and push-button start. Check whether your fob holds a mechanical key for the door.",
 tips=["Replace the fob battery as soon as the car says the key isn't detected or the range drops.",
       "Know where your model's key detection spot is; some MG owners find a weak fob is read more easily in the marked spot in the centre console.",
       "Keep a spare key at home, not in the glovebox."],
 faqs=[("Can you unlock an MG with the keys inside?", "Yes. We open MG cars without damage, 24/7 islandwide."),
       ("Can you clone an MG key fob?", "For many models, yes. Send the model, year and a photo of the key so we can confirm first.")]),
"Mini": dict(
 models="Cooper, Countryman, Clubman and Aceman",
 about="MINI, part of the BMW Group, is a favourite city car in Singapore, from the three-door Cooper to the Countryman.",
 keys="MINI keys hold an integrated mechanical key for the door, and many models have Comfort Access keyless entry. MINI's own advice for a weak key is emergency detection on the steering column.",
 tips=["Learn how to release the integrated key from your MINI fob now.",
       "If the car says the key isn't recognised, try the steering column emergency detection before calling.",
       "Keep the spare key away from the car to avoid relay theft on keyless models."],
 faqs=[("Can you open a MINI with the key locked inside?", "Yes, without damage, 24/7 islandwide."),
       ("Can you make a spare MINI key?", "For many MINI models, yes. Send the model, year and a photo of the key and we'll confirm.")]),
"Skoda": dict(
 models="Octavia, Superb, Kodiaq, Karoq, Kamiq and Enyaq",
 about="Škoda, part of the Volkswagen Group, is known in Singapore for roomy, practical cars like the Octavia and Superb, plus the Kodiaq SUV and electric Enyaq.",
 keys="Many Škodas use KESSY keyless entry and start, with an emergency key blade inside the fob.",
 tips=["Slide out the emergency key and find the driver's door keyhole before you need it.",
       "On a weak fob, the back of the fob against the Start/Stop button usually works.",
       "Replace the fob battery at the first dashboard warning."],
 faqs=[("How do I start a Škoda with a dead key fob?", "Press the Start/Stop button with the back of the fob while braking. On the Enyaq and Octavia, you can also place the fob in the cup holder nearest the driver, buttons up."),
       ("Can you unlock a Škoda with the keys inside?", "Yes, without damage, 24/7 islandwide.")]),
"Peugeot": dict(
 models="208, 2008, 308, 3008, 5008 and e-208",
 about="Peugeot, part of Stellantis, sells hatchbacks and SUVs such as the 208, 2008, 3008 and 5008 in Singapore, plus electric versions.",
 keys="Newer Peugeots often have Keyless Entry and Starting; others use a remote flip key with a folding blade.",
 tips=["Find out how your key's integrated blade releases, and where the driver's keyhole is.",
       "Read the handbook's 'key not detected' section once, so you know your model's backup start method.",
       "Keep a spare key at home."],
 faqs=[("Can you open a Peugeot with the keys inside?", "Yes, without damage, 24/7 islandwide."),
       ("Can you make a spare Peugeot key?", "For many models, yes. Send the model, year and a photo of the key and we'll confirm.")]),
"Suzuki": dict(
 models="Swift, Jimny, Vitara and S-Cross",
 about="Suzuki's Swift and Jimny are long-time Singapore favourites: small, economical and easy to park.",
 keys="Keyless Suzukis hide a mechanical key in the fob, and older models use a regular ignition key.",
 tips=["Slide the release on the back of the fob to free the mechanical key, and practise once.",
       "The driver's keyhole is at the back of the door handle on Suzuki models.",
       "A spare key is cheap insurance for an older car."],
 faqs=[("How do I start a Suzuki with a dead key fob?", "On push-button models, press the start button with the back of the fob while stepping on the brake."),
       ("Can you unlock a Suzuki with the keys inside?", "Yes, without damage, 24/7 islandwide.")]),
})

BRANDS = [dict(name=b, slug=slug(b), **DATA[b]) for b in C.CAR_BRAND_PAGES if b in DATA]


def links_html():
    pills = "".join(f'<li><a href="~/car-locksmith/{b["slug"]}/">{b["name"]}</a></li>' for b in BRANDS)
    return f'<ul class="link-pills">{pills}</ul>'


def build(x):
    for b in BRANDS:
        n = b["name"]
        path = f"car-locksmith/{b['slug']}/"
        crumbs = [("Home", ""), ("Services", "services/"), ("Car locksmith", "car-locksmith/"), (n, path)]
        title = next(t for t in (f"{n} Key Fob Battery, Spare Key & Locked Keys in Car",
                                 f"{n} Key Fob, Spare Key & Locked Keys | Singapore",
                                 f"{n} Key Fob & Car Lockout Help Singapore") if len(t) <= 60)
        desc = (f"{n} key fob battery dead or not working, need a spare key, or keys locked in the car? What to try, "
                f"plus 24/7 unlocking and key fob cloning in Singapore.")
        if len(desc) > 158:
            desc = f"{n} locksmith in Singapore: car unlocking without damage and {n} key fob cloning, 24/7 islandwide. Call 9224 9224."
        faqs = b["faqs"] + [
            (f"My {n} key fob battery is dead. How do I start the car?", DEADFOB[n]["start"]),
            (f"How much does it cost to unlock a {n}?", "Car lockouts start from {P_CAR}. We confirm the price before we set off."),
            (f"How much is a spare {n} key fob?", "It depends on the model and key type. WhatsApp {PHONE} the model, year and a photo of your key for a price."),
        ]
        jobs = getattr(C, "BRAND_JOBS", {}).get(n, [])
        recent = "".join(f'<div class="callout"><p><strong>Recent job:</strong> {j}</p></div>' for j in jobs)
        rel = RELATED.get(n, [])
        others = " · ".join(f'<a href="~/car-locksmith/{o["slug"]}/">{o["name"]}</a>' for o in BRANDS if o["name"] in rel)
        body = (x["page_hero"](crumbs, f"{n} Key Fob Battery Dead, Spare Key or Keys Locked in the Car?",
                f"Keys locked inside your {n}, or down to your last key fob? Uncle Thomas opens {n} cars without damage and clones {n} key fobs, 24/7 anywhere in Singapore.",
                ["Non-destructive entry", "Key fob cloning", "24/7 islandwide"]) +
                f'''<section class="section"><div class="container narrow prose">
<h2>{n} cars in Singapore</h2>
<p>{b["about"]} We work on {n} models including the {b["models"]}.</p>
{recent}<h2>A typical {n} call</h2>
<p>This is the kind of {n} call we often get: {SCENARIO.get(n, "")}</p>
<h2>What's different about {n} keys</h2>
<p>{FEATURE.get(n, "")} {b["keys"]}</p>
<h2>{n} key fob battery dead? How to get in and start</h2>
<ol><li><strong>Get in:</strong> {DEADFOB[n]["open"]}</li><li><strong>Start the car:</strong> {DEADFOB[n]["start"]}</li></ol>
<p>Details vary by year, so check your manual. Still stuck? Call us. Key locked inside instead? See <a href="~/guides/keys-locked-in-car/">keys locked in the car</a>.</p>
<h2>{n} key fob battery replacement</h2>
<p>Most {n} fobs take a 3V coin cell (often CR2032 or CR2025): copy the type printed on the old one and fit the new cell the same way up. Not working after the swap? See <a href="~/guides/car-key-fob-not-working/">key fob not working after a battery change</a>; if the backup start above works, the {n} fob itself is fine.</p>
<h2>{n} spare key</h2>
<p>Down to one {n} key? We clone {n} fobs from a working key, after checking your NRIC against the log card. WhatsApp {{PHONE}} the model, year and a key photo to confirm first.</p>
<h2>Tips for {n} owners</h2>
<ul>{"".join(f"<li>{t}</li>" for t in b["tips"])}</ul>
<p>Independent locksmith, not affiliated with {n}. <a href="~/prices/">All prices</a>.</p>
<p>Related: {others} · <a href="~/car-locksmith/">all car brands</a></p>
</div></section>
<section class="section section-alt"><div class="container narrow">{x["faq_html"](faqs, f"{n} Locksmith FAQs")}</div></section>''' +
                x["cta_band"](f"Locked Out of Your {n}?"))
        svc = {"@type": "Service", "@id": C.SITE + "/" + path + "#service",
               "name": f"{n} car locksmith: unlocking and key fob cloning, Singapore", "serviceType": "Car locksmith",
               "description": desc, "provider": {"@id": x["BUSINESS_ID"]},
               "areaServed": {"@type": "Country", "name": "Singapore"}, "url": C.SITE + "/" + path,
               "brand": {"@type": "Brand", "name": n},
               "offers": {"@type": "Offer", "priceCurrency": "SGD",
                          "priceSpecification": {"@type": "PriceSpecification", "minPrice": 100, "priceCurrency": "SGD"}}}
        nodes = x["page_schema"](path, title, desc, crumbs, faqs=faqs, extra=[svc])
        x["render"](path, title, desc, body, nodes, priority="0.7")


# ---------------------------------------------------------------------------
# Brand-specific depth (added 27 Oct 2026 to make each page more original).
# SCENARIO = a realistic *typical* call, framed as typical on the page, never as
# a dated real job. Real jobs go in config.BRAND_JOBS and show as "Recent job".
SCENARIO = {
"Toyota": "A driver loads groceries into the boot of a Corolla Altis at an HDB multi-storey carpark, sets the key down on the shopping bags, and closes the boot. The car locks itself. We open the driver's door with non-destructive tools, the key comes out of the boot, and the driver decides it's time to get a spare fob cloned.",
"Honda": "A private-hire driver bought a used Vezel that came with only one key. Nothing has gone wrong yet, but losing that key would mean days off the road. They WhatsApp us a photo of the key and the car's year, we confirm we can clone it, and they get a spare the same day.",
"Mercedes-Benz": "A C-Class owner in a condo carpark presses the fob and nothing happens: the battery has finally died. The car is KEYLESS-GO, so they've never used the hidden key blade. We talk them through sliding it out over WhatsApp, and they're in within a minute, no call-out needed. They book a spare fob for later.",
"BMW": "At a petrol station, a 3 Series owner puts the key on the passenger seat while checking the tyres. Comfort Access locks the car when the doors close. The key is visible through the window but out of reach. We open it without damage and suggest a spare key kept at home.",
"Audi": "A family with a Q5 at a shopping mall carpark: a child presses the lock button inside while the key is still in the cup holder, and everyone steps out. We open the car without touching the paint or seals, and the family is on their way.",
"Volkswagen": "A Golf owner's flip key hinge has snapped and the blade only stays out with tape. It still works, for now. Before it fails completely they want a spare. We clone a new remote from the working key.",
"Mazda": "A CX-5 driver unloading kids and a pram at a void deck drop-off locks the key inside with the engine off. We arrive, check the log card against the driver's NRIC, and open the door without damage.",
"Lexus": "An ES owner loses the main smart key but still has the slim card key in their wallet. The car still works, but one key left is risky. We clone a new fob from the working key so they're back to two.",
"Land Rover": "A Range Rover Evoque owner's spare fob went through the washing machine and no longer works. With only one key left, they ask us for a new spare cloned from the working fob.",
"Hyundai": "A private-hire driver with an Ioniq has a fob that only works when it's held right next to the door. The battery is weak and the driver can't risk a dead key mid-shift. We sort out a cloned spare so there's always a backup in the car bag.",
"Kia": "A couple share one Niro and one key, and they keep passing it back and forth. When one of them needs the car while the other is at work, they decide a second fob is cheaper than the hassle. We clone it from their working key.",
"Nissan": "A family with a Serena MPV: a child locks the doors from inside while the Intelligent Key is on the seat, then climbs out the other side before the door shuts. Everyone is out, and the key is in. We open the car without damage.",
"Porsche": "A Macan owner wants a spare key but doesn't want to leave the car at the dealer. They send us the model year and a photo of the key, and we confirm before booking that we can clone it.",
"Volvo": "An XC60 owner loading luggage for a Changi drop-off closes the tailgate on the key. The car locks. We open it with non-destructive tools so the trip isn't missed.",
"Mitsubishi": "A small company runs several Attrage cars, each with only one key. One key going missing has already cost them a day. They ask us to clone a spare for each car.",
"Subaru": "A Forester owner's key was soaked in a heavy downpour and now works only some of the time. While it still works, they ask for a cloned spare as a backup.",
}

FEATURE = {
"Toyota": "Many newer Toyotas have Smart Entry & Start, so the car can lock with the key nowhere near your hand. MPVs like the Alphard and Vellfire add power sliding doors, and a key left in a door pocket is easy to lock in.",
"Honda": "Some Honda models have a walk-away auto lock that locks the car when the smart key moves out of range. It's convenient, but if the key is still in the car with someone who then leaves, you can come back to a locked car.",
"Mercedes-Benz": "With KEYLESS-GO you rarely take the fob out, so many owners don't know where the emergency key blade is or where the hidden keyhole on the door handle sits. Learning both takes a minute and can save a call-out.",
"BMW": "Comfort Access unlocks the car when you touch the handle and locks it when you walk away. Some newer models also support a digital key on your phone. Both still depend on a working key or phone battery, so a physical spare matters.",
"Audi": "Many Audis with advanced keys lock and unlock by touch. On some models the emergency keyhole is hidden under a cap on the driver's door handle that you prise off with the key blade.",
"Volkswagen": "Volkswagen's flip keys are hard-wearing, but the folding hinge is a common weak point after years in a pocket. Models with Keyless Access behave like other smart-key cars.",
"Mazda": "Mazda's Advanced Keyless Entry lets you lock and unlock with a button on the door while the key stays in your pocket. A low key battery is the usual cause when that button stops responding.",
"Lexus": "Some Lexus models come with a card key that slips into a wallet. It's a useful built-in backup, but it isn't a full replacement for a lost main fob.",
"Land Rover": "Many Land Rover and Range Rover models use keyless entry, and some offer a wearable key for sports and the beach. Keep the main fob safe when you use it, because the main fob is what a cloned spare is made from.",
"Hyundai": "Newer Hyundais may also support a digital key on a phone or card. A fob is still the backup most owners rely on, especially private-hire drivers who can't afford downtime.",
"Kia": "Like Hyundai, some newer Kias support a phone-based digital key. A physical fob remains the simplest backup for sharing a car between drivers.",
"Nissan": "Nissan's Intelligent Key works from a pocket or bag, which makes it easy to forget where it is. MPVs like the Serena have several doors that can be locked from inside.",
"Porsche": "Porsche Entry & Drive works from your pocket on many models. The car-shaped fob still holds an emergency key for the driver's door.",
"Volvo": "Many Volvos have keyless locking and unlocking, and a tailgate that can be closed with a button. A key left in the boot is a common way to get locked out.",
"Mitsubishi": "Mitsubishi's Keyless Operation System is found on many models, while simpler models such as the Attrage often use a remote with a metal blade. For fleets, one spare per car avoids downtime.",
"Subaru": "Many Subarus use Keyless Access with push-button start, and the fob contains an emergency key. A key that works only some of the time is often a weak battery or water damage.",
}

# Dead-fob help: how owners of each brand usually get in and start with a flat
# key battery. Written cautiously ("many models") because it varies by model/year.
DEADFOB = {
"Toyota": dict(
 open="Toyota hides a mechanical key in the smart key: slide the release and it comes out. On some models the driver's keyhole is behind a cap at the end of the handle; lever it off gently with the key.",
 start="Hold the Toyota emblem side of the smart key against the POWER or ENGINE START STOP switch. A buzzer or light confirms it's been read, then press the switch again with your foot on the brake."),
"Honda": dict(
 open="There's a built-in key inside every Honda smart fob: slide the small knob on the back and it pulls free. It fits the driver's door lock.",
 start="Honda's trick is the H logo. Hold that face of the fob flat against the ENGINE START/STOP button, keep your foot on the brake, and press."),
"Mercedes-Benz": dict(
 open="Slide the catch on the back of the fob to release the emergency key blade. On many models the door keyhole is hidden under a cover on the driver's handle.",
 start="On models with a key slot, insert the fob as normal. On many newer models without a slot, place the fob in the spot marked with a key symbol (often in the centre console tray or a cup holder), then press start."),
"BMW": dict(
 open="Press the release on the fob and slide out the emergency key. The driver's door lock is often under a small cover at the end of the handle.",
 start="Hold the key against the marked area on the steering column, or place it in the marked spot in the centre console or cup holder on newer models, then press the start button."),
"Audi": dict(
 open="Press the release button on the fob and pull out the emergency key. On many Audis you prise off a small cap on the driver's door handle to reach the keyhole.",
 start="Hold the key at the spot marked with a key symbol, often in the centre console near the cup holders, then press the start button."),
"Volkswagen": dict(
 open="On a flip key, fold out the blade and use the driver's door keyhole. On Keyless Access models, pull the emergency key out of the fob and remove the cap on the driver's handle.",
 start="On flip-key models the ignition works with the blade as normal. On Keyless Access models, hold the fob next to the steering column near the start button, then press start."),
"Mazda": dict(
 open="Mazda calls it the auxiliary key. Push the knob on the smart key, draw the key out, and open the driver's door with it.",
 start="Mazda's push-button start can read a weak key at very close range. Bring the key right up to the button, then push it while braking."),
"Lexus": dict(
 open="Press the release and pull out the mechanical key, then unlock the driver's door. (A card key, if your model has one, is a backup for entry and doesn't replace a lost fob.)",
 start="Press the brake and touch the Lexus emblem side of the fob to the start button. When the car detects it, press the button to start."),
"Land Rover": dict(
 open="Slide the release and pull the emergency key blade out of the fob. The driver's door lock is often hidden behind a cover on the handle.",
 start="Many models have a backup reader for a flat fob, usually on the steering column cover or in a cup holder or console tray. Hold or place the fob there, then press start."),
"Hyundai": dict(
 open="A metal key hides in the back of most Hyundai smart keys; a press of the release frees it for the driver's door.",
 start="Use the fob itself as your finger: push the ENGINE START/STOP button with the end of the smart key. The car reads it at close range even with a weak battery."),
"Kia": dict(
 open="Free the mechanical key from the smart key with its release button and use the driver's door lock. On EVs like the Niro EV and EV6, total silence from the car usually points to a flat 12V battery rather than the fob.",
 start="Kia's backup method: press the start button using the smart key itself while braking. On EVs, wait for the READY light before driving off."),
"Nissan": dict(
 open="Nissan tucks a mechanical key inside the Intelligent Key. Release it and use it on the driver's door; on an MPV like the Serena, only the driver's door has a keyhole.",
 start="Touch the Intelligent Key to the push-button ignition and listen for the chime. That's the car confirming the key, so you can now start it."),
"Porsche": dict(
 open="Press the release on the car-shaped fob to free the emergency key, then use the driver's door lock.",
 start="On models with an ignition on the left of the steering wheel, insert the fob or the ignition handle as normal. On keyless models, your manual shows the backup spot to hold the fob before pressing start."),
"Volvo": dict(
 open="Slide the catch and remove the detachable key blade from the fob, then unlock the driver's door with it.",
 start="Place the fob in the backup reader, usually marked with a key symbol in the cup holder or tunnel console on newer models, then start as normal."),
"Mitsubishi": dict(
 open="Pull out the emergency key from the keyless operation key, or use the blade on a remote key, to unlock the driver's door.",
 start="On many push-button models, touch the start button with the key, or insert it into the key slot if your model has one. Your manual shows which applies."),
"Subaru": dict(
 open="Subaru's access key carries an emergency key; unclip it and it opens the driver's door.",
 start="Turn the access key over and press its back against the push-button ignition. Once the car recognises it, start as usual."),
}

# More specific tips where the originals were generic.
DATA["Kia"]["tips"] = [
    "Sharing one car between two drivers? A second fob is simpler than passing one key around.",
    "On the Niro EV and EV6, a flat 12V battery can stop the doors unlocking even with a good fob. Tell us if nothing responds at all.",
    "Change the fob battery as soon as the range drops: Kia smart keys give little warning before they stop.",
]
DATA["Volvo"]["tips"] = [
    "Find the backup key reader in your manual now, so a flat fob never strands you.",
    "Take the key out of your pocket before loading the boot: a key left in the tailgate area is a common Volvo lockout.",
    "Keep the detachable blade with the fob; it's your way in if the battery dies.",
]
DATA["Subaru"]["tips"] = [
    "Keep the access key away from water. A soaked fob often works on and off before failing completely.",
    "If the remote range drops, replace the battery before it leaves you touching the start button to get going.",
    "Keep the spare key at home, not in the car.",
]

# Related brands linked from each page (same group, same market, or cars owners often compare).
RELATED = {
"Toyota": ["Lexus", "Honda", "Nissan"], "Lexus": ["Toyota", "Mercedes-Benz", "BMW"],
"Honda": ["Toyota", "Mazda", "Nissan"], "Nissan": ["Toyota", "Honda", "Mitsubishi"],
"Mazda": ["Honda", "Subaru", "Toyota"], "Subaru": ["Mazda", "Toyota", "Volvo"],
"Mitsubishi": ["Nissan", "Toyota", "Hyundai"], "Hyundai": ["Kia", "Toyota", "Mitsubishi"],
"Kia": ["Hyundai", "Toyota", "Mazda"], "Mercedes-Benz": ["BMW", "Audi", "Lexus"],
"BMW": ["Mercedes-Benz", "Audi", "Porsche"], "Audi": ["Volkswagen", "Porsche", "BMW"],
"Volkswagen": ["Audi", "Porsche", "Volvo"], "Porsche": ["Audi", "Volkswagen", "Mercedes-Benz"],
"Land Rover": ["Volvo", "BMW", "Porsche"], "Volvo": ["Land Rover", "Audi", "Subaru"],
}
DATA["Porsche"]["tips"] = [
    "Keyless cars can be targeted by relay theft. At home, keep fobs in a signal-blocking pouch, away from the front door.",
    "Want a spare without leaving the car at the dealer? Send us the model year and a photo of the fob first, and we'll confirm before you book.",
    "Replace the fob battery as soon as the dashboard warns you.",
]

SCENARIO.update({
"BYD": "A BYD owner uses the phone digital key every day and left the NFC card in the glovebox. At a mall carpark late at night, the phone dies and the fob is at home. We open the car without damage, and the card goes into their wallet.",
"MG": "An MG ZS EV owner ignores the key-not-detected messages for a week. One morning in an HDB carpark the fob is too weak to start the car. If the console spot doesn't help, they call us.",
"Mini": "A MINI Cooper owner with Comfort Access drops the key in the boot while loading shopping and shuts it. The car locks itself. We open it without damage.",
"Skoda": "A Škoda Octavia driver's fob battery dies at a petrol station. They don't know the emergency key or the Start/Stop trick, so they call. Often we can talk them through it on the phone.",
"Peugeot": "A Peugeot 3008 owner locks the key inside after the kids climb out and press the lock button. We open it without damage while the family waits in the shade.",
"Suzuki": "A Swift owner's remote stops working and they don't know the fob hides a key. We explain over WhatsApp where the release is and where the keyhole sits, and they're in.",
})
FEATURE.update({
"BYD": "BYD's electric cars use several key types at once (fob, NFC card and phone), which is great until the phone dies or the card is locked inside.",
"MG": "MG's smart keys rely on the car detecting the fob, so a weak battery shows up as 'key not detected' before it fails completely.",
"Mini": "MINI shares BMW Group key technology, including emergency key detection at the steering column and an integrated door key.",
"Skoda": "Škoda shares Volkswagen Group key systems, and has two well-known backup start methods: the back of the fob on Start/Stop, or the cup holder on some models.",
"Peugeot": "Peugeot's keyless system varies by model and year, so the handbook's backup procedure is the first thing to check.",
"Suzuki": "Suzuki keeps things simple: a hidden mechanical key in the fob and a keyhole behind the driver's door handle.",
})
DEADFOB.update({
"BYD": dict(open="If your BYD has an NFC card key, it needs no battery: tap it on the car's card reader (your manual shows where). Phone digital keys work if your phone has charge.",
            start="With a weak fob, follow the 'key not detected' steps in your BYD manual. If the car still won't detect a key or card, call us."),
"MG": dict(open="If your MG fob holds a mechanical key, use it in the driver's door.",
           start="Some MG ZS EV owners find placing the fob in the marked spot in the centre console cup holder helps the car read a weak key. Check your manual for your model."),
"Mini": dict(open="Release the integrated mechanical key from the fob and use it in the driver's door.",
             start="MINI says to press the back of the key against the marking on the steering column (emergency detection), then start as normal."),
"Skoda": dict(open="Slide the emergency key out of the fob and use it in the driver's door.",
              start="Press the Start/Stop button with the back of the fob while braking. On the Enyaq and Octavia, you can also put the fob in the cup holder nearest the driver, buttons up."),
"Peugeot": dict(open="Release the key blade from your remote and use it in the driver's door lock.",
                start="Follow the 'key not detected' backup procedure in your Peugeot handbook; it varies by model and year."),
"Suzuki": dict(open="Slide the button on the back of the fob, pull out the mechanical key, and use the keyhole at the back of the driver's door handle.",
               start="On push-button models, press the start button with the back of the fob while stepping on the brake. On older models, remove the cap over the key slot and use the key in the ignition."),
})
RELATED.update({"BYD": ["MG", "Hyundai", "Kia"], "MG": ["BYD", "Hyundai", "Kia"], "Mini": ["BMW", "Volkswagen", "Audi"],
                "Skoda": ["Volkswagen", "Audi", "Hyundai"], "Peugeot": ["Volkswagen", "Skoda", "Volvo"], "Suzuki": ["Toyota", "Honda", "Mazda"]})
