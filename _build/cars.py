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

BRANDS = [dict(name=b, slug=slug(b), **DATA[b]) for b in C.CAR_BRAND_PAGES if b in DATA]


def links_html():
    pills = "".join(f'<li><a href="~/car-locksmith/{b["slug"]}/">{b["name"]}</a></li>' for b in BRANDS)
    return f'<ul class="link-pills">{pills}</ul>'


def build(x):
    for b in BRANDS:
        n = b["name"]
        path = f"car-locksmith/{b['slug']}/"
        crumbs = [("Home", ""), ("Services", "services/"), ("Car locksmith", "car-locksmith/"), (n, path)]
        title = f"{n} Locksmith Singapore | Unlocking & Key Fob Cloning"
        if len(title) > 60:
            title = f"{n} Locksmith Singapore | Car Key Fob & Lockout"
        desc = (f"{n} keys locked in the car, or need a spare key fob? Uncle Thomas unlocks {n} cars without damage and clones "
                f"{n} key fobs, 24/7 islandwide. Call 9224 9224.")
        if len(desc) > 158:
            desc = f"{n} locksmith in Singapore: car unlocking without damage and {n} key fob cloning, 24/7 islandwide. Call 9224 9224."
        faqs = b["faqs"] + [
            (f"How much does it cost to unlock a {n}?", "Car lockouts start from {P_CAR}. We confirm the price before we set off."),
            (f"How much is a spare {n} key fob?", "It depends on the model and key type. WhatsApp {PHONE} the model, year and a photo of your key for a price."),
        ]
        others = " · ".join(f'<a href="~/car-locksmith/{o["slug"]}/">{o["name"]}</a>' for o in BRANDS if o["slug"] != b["slug"])
        body = (x["page_hero"](crumbs, f"{n} Locksmith Singapore: Unlocking &amp; Key Fob Cloning",
                f"Keys locked inside your {n}, or down to your last key fob? Uncle Thomas opens {n} cars without damage and clones {n} key fobs, 24/7 anywhere in Singapore.",
                ["Lockouts from {P_CAR}", "Key fob cloning", "24/7 islandwide"]) +
                f'''<section class="section"><div class="container narrow prose">
<h2>{n} cars in Singapore</h2>
<p>{b["about"]} We work on {n} models including the {b["models"]}.</p>
<h2>Locked out of your {n}?</h2>
<p>Keys locked inside the car or boot, or a remote that won't respond? We open {n} cars with professional, non-destructive entry tools: no broken windows, no scratched paint, no damaged seals. Please don't try a coat hanger; it can damage the door wiring and airbag sensors.</p>
<h2>Spare {n} key fob</h2>
<p>{b["keys"]}</p>
<p>If you're down to one key, a spare saves a stressful day later. Uncle Thomas clones {n} key fobs, including remote and smart keys. WhatsApp {{PHONE}} your model, year and a photo of the key (front and back) and we'll confirm before you book.</p>
<h2>Tips for {n} owners</h2>
<ul>{"".join(f"<li>{t}</li>" for t in b["tips"])}</ul>
<h2>Price</h2>
<p>{n} lockouts start from <strong>{{P_CAR}}</strong>. Key fob cloning is quoted per car, depending on the model and key type. See all <a href="~/prices/">prices</a>.</p>
<div class="callout"><p><strong>Proof of ownership:</strong> before unlocking a car or cloning a key we check that it's yours, for example your NRIC against the vehicle log card. Uncle Thomas Locksmith is an independent locksmith and is not affiliated with {n}.</p></div>
<p>Other brands: {others} · <a href="~/car-locksmith/">all car brands</a></p>
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
