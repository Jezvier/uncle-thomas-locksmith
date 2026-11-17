"""
Extra brand-specific sections for the brand pages that were least original
(below the 55% unique-text target in the 13 Nov 2026 check).

EXTRA[group][brand] = dict(sections=[(h2, html), ...], sources=[(label, url), ...])
group is "car", "lock" or "safe". The templates in cars.py, brands.py and
safe_brands.py insert the sections before "A typical <brand> call" and add the
sources to the page's source line.

Rules (same as the rest of the site): facts only from the sources listed; where
sources disagree or don't cover a model, say "check your manual" instead of
guessing; never publish factory default codes. YEW and Booil have no manuals
online, so their sections are practical, clearly general advice.
"""

EXTRA = {
"car": {
"Mercedes-Benz": dict(sections=[
 ("Mercedes-Benz key battery: CR2032 or CR2025",
  "<p>The battery depends on the generation. The current <strong>GLC (X254)</strong> manual calls for a <strong>CR2032</strong>; the "
  "<strong>W205 C-Class</strong> (2015 on) takes a <strong>CR2025</strong>. Read the old cell before buying.</p>"
  "<p>The GLC manual's test for a weak battery: press a button, and if the key's indicator lamp doesn't light up, the battery is weak. "
  "A spare key you rarely use can have KEYLESS-GO switched off to save its battery, which is worth doing for the one kept at home.</p>"),
 ], sources=[
  ("Mercedes-Benz GLC (X254) operator's manual 2024 (Mercedes-Benz Canada)", "https://www.mercedes-benz.ca/content/dam/mb-nafta/ca/owners/operators-manual/2024/GLCSUV_254_ENG.pdf"),
  ("Mercedes-Benz C-Class (W205) operator's manual 2015 (Mercedes-Benz Canada)", "https://www.mercedes-benz.ca/content/dam/mb-nafta/ca/owners/operators-manual/2015/operators-manual/2015_C-Class_SHORT_P205000213_EdD.pdf")]),
"BMW": dict(sections=[
 ("BMW Digital Key: handy, but keep a physical spare",
  "<p>BMW says that with Digital Key Plus the car recognises your phone as you approach and unlocks, starts with the phone in your "
  "pocket, and locks itself when you walk away. Depending on the model and phone, up to 18 keys can be shared.</p>"
  "<p>That's convenient until the phone is flat or left inside the car. A physical key at home is still the simplest backup, and if "
  "you're down to one, we can clone it before it becomes urgent. BMW's handbooks are online by VIN, so look up your own model's "
  "emergency key and weak-key steps once, while everything works.</p>"),
 ], sources=[("BMW Digital Key (BMW Canada)", "https://www.bmw.ca/en/digital-services/bmw-digital-key.html")]),
"Volkswagen": dict(sections=[
 ("Volkswagen key battery: watch the indicator lamp",
  "<p>The Tiguan owner's manual doesn't name a battery type; it just calls it a button cell, so read the number on the old one before "
  "you buy. What it does give is a clear test: <strong>if the indicator lamp in the key doesn't flash when you press a button, the "
  "cell needs replacing</strong>.</p>"
  "<p>If you leave it too late, the flat-battery start above still works on Keyless Access cars: brake, press start, then hold the key "
  "to the right of the steering column trim.</p>"),
 ], sources=[("Volkswagen Tiguan owner's manual, edition 11.2021 (Volkswagen India)", "https://www.volkswagen.co.in/idhub/content/dam/onehub_pkw/importers/in/pdf/Tiguan-User-Manual.pdf")]),
"Land Rover": dict(sections=[
 ("Land Rover keys: CR2032, the Activity Key and keys locked in",
  "<p>Both the Discovery Sport and Defender handbooks call for a <strong>CR2032</strong>, and the instrument panel shows a warning when "
  "the smart key battery needs replacing.</p>"
  "<p>Two Land Rover features change how lockouts happen. The <strong>Activity Key</strong> is a wristband waterproof to 40 m for "
  "sport and the beach: once it's activated, <strong>any smart key left inside the car is disabled</strong>, so the car stays secure "
  "with your fob in the glovebox. And a smart key left inside when you close the luggage compartment with the alarm armed is "
  "deactivated too. If you're locked out with the key inside, we check the log card and open the car without damage.</p>"),
 ], sources=[
  ("Land Rover Discovery Sport (2023) handbook: smart key", "https://www.ownerinfo.landrover.com/document/3A/2023/1665395/proc/G2818154/G2904727"),
  ("Land Rover Defender (2024) handbook: smart key", "https://www.ownerinfo.landrover.com/document/3E/2024/1697590/proc/G3244912/G3359301")]),
"Toyota": dict(sections=[
 ("Toyota key battery: CR2450 or CR2032",
  "<p>Toyota's 2025 Corolla owner's manual lists two batteries: <strong>a CR2450 for smart keys</strong> (Smart Entry & Start) and "
  "<strong>a CR2032 for keys without it</strong>. Read the number on the old cell before you buy. The manual's first sign of a weak "
  "battery is a shorter range: you have to get closer to the car before it responds.</p>"
  "<p>One feature worth knowing: Toyota's <strong>battery-saving mode</strong> stops the key listening for the car's signal, which "
  "cuts battery drain if you keep the key near the front door at home.</p>"),
 ], sources=[
  ("Toyota 2025 Corolla owner's manual: key battery", "https://www.toyota.com/content/dam/toyotaowners/digital-owners-manual-v2/en/om02688u/chapter/ch06se030409.html"),
  ("Toyota 2025 Corolla owner's manual: if the key doesn't work", "https://www.toyota.com/content/dam/toyotaowners/digital-owners-manual-v2/en/om02688u/chapter/ch07se020409.html"),
  ("Toyota 2025 Corolla owner's manual: battery-saving mode", "https://www.toyota.com/content/dam/toyotaowners/digital-owners-manual-v2/en/om02688u/chapter/ch03se020403.html")]),
"Honda": dict(sections=[
 ("Honda keyless remote battery: CR2032",
  "<p>Honda's Civic e:HEV owner's manual specifies a <strong>CR2032</strong> lithium cell and puts its life at <strong>about two "
  "years</strong>. Its test is simple: if the remote's indicator light doesn't come on when you press a button, replace the battery. "
  "Until you do, the weak-battery start above still works.</p>"),
 ], sources=[
  ("Honda Civic e:HEV owner's manual: keyless remote battery", "https://manuals.honda.co.uk/civicehev/2026/HTMLtemplate/106962046-93568.html"),
  ("Honda Civic e:HEV owner's manual: if the remote battery is weak", "https://manuals.honda.co.uk/civicehev/2026/HTMLtemplate/106962046-18683.html"),
  ("Honda Civic e:HEV owner's manual: locking from outside", "https://manuals.honda.co.uk/civicehev/2026/HTMLtemplate/106962046-120103.html")]),
"Lexus": dict(sections=[
 ("Lexus key battery and the low-battery alarm",
  "<p>The 2025 ES owner's manual takes a <strong>CR2032</strong>, and Lexus's support site lists the same cell for the 2019 ES, NX "
  "and RX. Lexus also gives you a warning most brands don't: when the key battery gets low, <strong>an alarm sounds in the cabin "
  "when you switch the engine off</strong>.</p>"
  "<p>If your Lexus came with a card key, its battery is different: the manual says it's available only from Lexus dealers, so don't "
  "leave the card's battery to the last minute.</p>"),
 ], sources=[
  ("Lexus 2025 ES owner's manual: key battery", "https://www.lexus.com/content/dam/lexus/drivers/documents/digital-owners-manual-v2/en/om06308u/chapter/ch06se030409.html"),
  ("Lexus 2025 ES owner's manual: if the key doesn't work", "https://www.lexus.com/content/dam/lexus/drivers/documents/digital-owners-manual-v2/en/om06308u/chapter/ch07se020410.html"),
  ("Lexus support: key battery sizes by model", "https://support.lexus.com/s/article/What-size-battery-is-8347")]),
"Nissan": dict(sections=[
 ("Nissan Intelligent Key battery: CR2032",
  "<p>Nissan's 2024 X-Trail owner's manual specifies a <strong>CR2032</strong> (or equivalent). You get a warning before it dies: "
  "the dashboard shows a key battery low message while the key still works, which is the moment to change it.</p>"
  "<p>If the warning is ignored, the dead-battery steps above still get you started: touch the key to the switch, wait for the chime, "
  "and press within 10 seconds.</p>"),
 ], sources=[
  ("Nissan X-Trail (2024) owner's manual: Intelligent Key battery", "https://www.nissan.co.uk/owners/car-repair/car-owner-manual/manuals/iom/xtrail/0t33/e1/2024/intelligent-key-battery-1.shtml"),
  ("Nissan X-Trail (2024) owner's manual: if the key battery is discharged", "https://www.nissan.co.uk/owners/car-repair/car-owner-manual/manuals/iom/xtrail/0t33/e1/2024/intelligent-key-battery-discharge-1.shtml"),
  ("Nissan X-Trail (2024) owner's manual: mechanical key", "https://www.nissan.co.uk/owners/car-repair/car-owner-manual/manuals/iom/xtrail/0t33/e1/2024/mechanical-key-1.shtml")]),
"Hyundai": dict(sections=[
 ("Ioniq 5: flush handles and the NFC card key",
  "<p>The Ioniq 5's door handles sit flush with the body, so the keyhole isn't visible. Hyundai's manual says to <strong>press the "
  "front part of the handle</strong> so the rear part comes out, then use the mechanical key from the smart key. Once inside, press "
  "the start button directly with the smart key.</p>"
  "<p>Many Ioniq 5s also came with an <strong>NFC key card</strong>: hold it to the centre of the door handle to lock or unlock. "
  "Keep it in your wallet, and the smart key's <strong>CR2032</strong> battery stops being a single point of failure.</p>"),
 ], sources=[
  ("Hyundai Ioniq 5 (2022) owner's manual: convenience features", "https://manuals.hyundai.co.uk/umanuals/ioniq-5/ioniq-5-2022-convenience-features.pdf"),
  ("Hyundai Ioniq 5 quick reference guide: NFC key card", "https://owners.hyundaiusa.com/content/dam/hyundai/us/myhyundai/manuals/glovebox-manual/2022/ioniq5/2022-Ioniq-5-Quick-Reference-Guide.pdf"),
  ("Hyundai Elantra owner's manual (Hyundai India)", "https://www.hyundai.com/content/dam/hyundai/in/en/data/connect-to-service/owners-manual/elantra.pdf")]),
"Kia": dict(sections=[
 ("What Kia Singapore says to do when the key battery dies",
  "<p>Kia Singapore publishes the steps itself. To get in: take the mechanical key out of the smart key and use it to <strong>remove "
  "the keyhole cover on the driver's door handle</strong>, then unlock. On flush handles, press the front of the handle to expose the "
  "keyhole. To start: sit in the driver's seat, brake, and <strong>press ENGINE START/STOP directly with the smart key</strong>.</p>"
  "<p>The EV6 manual adds that the mechanical key opens the driver's door only, and that the key takes a <strong>CR2032</strong>.</p>"),
 ], sources=[
  ("Kia Singapore: unlocking your car when the smart key battery is dead", "https://www.kia.com/sg/owners/owner-resources/quick-tips/breakdowns-and-accidents/unlocking-your-car-when-smart-key-battery-is-dead.html"),
  ("Kia Singapore: starting your car when the smart key battery is dead", "https://www.kia.com/sg/owners/owner-resources/quick-tips/breakdowns-and-accidents/starting-your-car-when-smart-key-battery-is-dead.html"),
  ("Kia EV6 owner's manual: key battery", "https://ownersmanual.kia.com/full_webhelp/CV1/2023/en_GB/topics/t00145.html")]),
"BYD": dict(sections=[
 ("BYD Atto 3: card, phone and the no-power mode sign",
  "<p>The Atto 3 handbook lists the full key set: an electronic smart key with a mechanical key inside, plus (on equipped cars) a "
  "Bluetooth digital key and an NFC card. The card works at the <strong>NFC sign on the driver's side mirror</strong>, held within "
  "about 2 cm for a second or two, and inside the car it authorises starting.</p>"
  "<p>When the smart key's battery runs low, the car says so: <em>Smart key power is low. Please replace the battery as soon as "
  "possible.</em> BYD's manuals don't name the cell and send you to a BYD dealer to change it, so book that when the message appears.</p>"),
 ], sources=[
  ("BYD Atto 3 owner's manual (byd.com)", "https://www.byd.com/material/BYD%20ATTO3%202022%20Owner's%20Manual-20251004-EN.pdf"),
  ("BYD Atto 3 owner's handbook 2025 (BYD Australia)", "https://bydautomotive.com.au/brochures/BYD-ATTO-3-Owners-Handbook-2025.pdf"),
  ("BYD digital key (byd.com)", "https://www.byd.com/eu/ownership/byd-digital-key")]),
"MG": dict(sections=[
 ("MG4 and ZS EV: the backup key and the cup-holder start",
  "<p>MG's manuals are clear about the mechanical key: <strong>each smart key holds one, it opens the driver's door, and it can't "
  "start the car</strong>. The driver's lock hides under a trim cover that has to come off first. On the ZS EV, once you've unlocked "
  "with the mechanical key, power the car on within 15 seconds or the alarm goes off.</p>"
  "<p>To start with a weak key, MG's alternative starting procedure puts the key in a backup position with the buttons facing up. On "
  "the ZS EV that's <strong>the centre console cup holder</strong>. Both cars take a <strong>CR2032</strong>.</p>"),
 ], sources=[
  ("MG4 EV owner's manual (MG Europe)", "https://cdn.mgmotor.eu/manuals/EU-MG4-MY23_Owner-Manual-20230907_compressed.pdf"),
  ("MG ZS EV owner's manual (MG Europe)", "https://cdn.mgmotor.eu/manuals/1.-ZS-EV_Owners-Manual.pdf")]),
"Volvo": dict(sections=[
 ("Volvo key fob battery: a CR2430, not a CR2032",
  "<p>Most car keys on this site take a CR2032, but Volvo's own support pages list a <strong>CR2430, 3V</strong> cell for the remote key "
  "on models such as the XC60, S60 and V60 of the 2010s. A CR2430 is wider than a CR2032, so the more common cell won't sit properly. "
  "On the XC60, Volvo says to change it when the instrument panel shows <em>Low battery in remote control</em>, or when the locks "
  "keep ignoring the key within 20 metres of the car: do it then, before it fails at a carpark gantry.</p>"
  "<p>On those keys, slide the spring-loaded catch aside while pulling the key blade straight out, then put a 3 mm flat screwdriver in the "
  "hole behind the catch and gently prise the key open, buttons facing up so the cell doesn't drop out. "
  "Note which way up the old cell sits and fit the new one the same way. Volvo also advises not touching the new cell's flat faces with your "
  "fingers, and no re-pairing is needed afterwards. Newer Volvos, including the XC40, use a different key, so check your handbook before buying a cell.</p>"),
 ("Key locked in the boot of a Volvo?",
  "<p>Keyless locking plus a powered tailgate makes this the classic Volvo call: the key goes into a bag in the boot, the tailgate closes, "
  "and the car locks. Don't break a window. We open the door without damage and the key comes out of the boot once we're in. If there's a "
  "second key at home and someone can bring it quickly, that's often faster, and we'll say so when you call.</p>"),
 ], sources=[("Volvo Cars support: replacing the remote key battery (XC60)", "https://www.volvocars.com/us/support/car/xc60/13w46/article/a1caf043c4f29955c0a801e80048135e/"),
             ("Volvo Cars support: remote key battery (V40)", "https://volvocars.com/au/support/car/v40/article/28862da64e18587dc0a801e801ced2fa")]),
"Mini": dict(sections=[
 ("MINI key battery: check the cell before you buy",
  "<p>MINI's own FAQ says to replace the key battery with the same type that's already in it, and that this is usually a "
  "<strong>CR2032 or a CR2450</strong>. They're very different sizes (a CR2450 is wider and thicker), so open the key and read the number "
  "on the old cell first. On many MINI keys you press the release on the side, slide out the integrated mechanical key, then ease off the "
  "cover with a small flat screwdriver to reach the cell.</p>"
  "<p>The usual early sign of a weak MINI key is a remote that only works up close. Change the cell then. If the car stops detecting the key "
  "altogether, use the emergency detection spot on the steering column described above.</p>"),
 ("Spare MINI keys",
  "<p>A battery change never needs the key re-paired, but a brand-new MINI key has to be programmed to the car with specialist equipment. "
  "If you're down to one key, WhatsApp us the model, year and a photo of it: we'll tell you honestly whether it's a remote we can clone "
  "or one that needs MINI.</p>"),
 ], sources=[("MINI FAQ: key battery type", "https://faq.mini.com.au/s/article/MINI-vehicle-Vehicle-access-Key-recognition-Battery-type-wWHQB"),
             ("MINI FAQ: replacing the key battery", "https://faq.mini.com.au/s/article/MINI-vehicle-Vehicle-access-Key-recognition-Replace-battery-CYvAW")]),
"Peugeot": dict(sections=[
 ("Peugeot key battery: CR2032",
  "<p>Peugeot handbooks for models including the 508 and the 2008 list a <strong>CR2032 3V</strong> cell for the remote key, and the "
  "instrument panel shows a message when it's running low. The case unclips at a small notch: put a small flat screwdriver in the cut-out, "
  "lift the cover, and fit the new cell the same way up as the old one.</p>"
  "<p>The 508 handbook also has an <em>electronic key fault</em> procedure for when the car stops recognising the key. The steps differ "
  "between models and years, which is why the handbook is the first thing to check. Keep the paper copy in the glovebox, not only as a PDF "
  "on a phone that might be flat too.</p>"),
 ("Locked out of a Peugeot",
  "<p>The big boots of the 3008 and 5008 are easy places to leave a key while loading. If the car has locked with the key inside, don't try "
  "a wire hanger down the window seal: modern doors are full of wiring for the windows, mirrors and locks. We open the door with "
  "non-destructive tools, check the log card against your NRIC, and you're on your way.</p>"),
 ], sources=[("Peugeot 508 handbook: key battery", "https://www.manualslib.com/manual/1215410/Peugeot-508.html?page=259"),
             ("Peugeot 2008 handbook: remote control", "https://manualslib.com/manual/919944/Peugeot-2008.html?page=55")]),
"Mitsubishi": dict(sections=[
 ("Mitsubishi key battery",
  "<p>The smart key for the third-generation Outlander (2014 to 2021) takes a <strong>CR2032</strong>, as do many other Mitsubishi keyless "
  "operation keys, but some older Mitsubishi remotes use a smaller CR1620. Check the old cell before you buy. On keyless models, slide out "
  "the emergency key first: the slot it leaves is where you ease the case open.</p>"
  "<p>A Mitsubishi key that only works when you're standing right next to the car almost always has a weak cell. Change it then, before "
  "the car stops recognising it.</p>"),
 ("Fleets and private-hire Mitsubishis",
  "<p>Attrage and Xpander cars are often run by small companies and private-hire drivers, where one lost key means a day off the road. "
  "Keep one spare per car, label it by plate number (never by address), and keep the spares at the office rather than inside the cars.</p>"),
 ], sources=[("2014–2021 Outlander key battery guide", "https://paulstravelpictures.com/2014-2021-Mitsubishi-Outlander-Key-Fob-Battery-Replacement-Guide"),
             ("Mitsubishi remote key battery replacement (YOUCANIC)", "https://www.youcanic.com/change-battery-a-mitsubishis-key/")]),
"Skoda": dict(sections=[
 ("Škoda key battery: CR2032 or CR2025",
  "<p>Škoda's manuals say a replacement cell must match the original. Depending on the model and year, Škoda keys take a <strong>CR2032 or "
  "a CR2025</strong>: the same width, but the CR2032 is thicker. If the cover won't click shut after a swap, you have the wrong one. On newer "
  "keys such as the Karoq's, press the lower button on the cover while pulling out the emergency key, then lift the back cover with a small "
  "flat screwdriver.</p>"
  "<p>Still getting a key battery warning after a swap? Check the new cell is the right way up and genuinely fresh before assuming the key "
  "itself has failed.</p>"),
 ("Škoda shares its keys with Volkswagen",
  "<p>Škoda uses Volkswagen Group key hardware, so the remote and emergency-key layout will look familiar if you've owned a VW, and the same "
  "advice applies: on older folding keys the hinge is the wear point, so get a spare cloned while the old key still works. See our "
  "<a href=\"~/car-locksmith/volkswagen/\">Volkswagen page</a> too.</p>"),
 ], sources=[("Škoda Octavia manual: changing the remote battery", "https://www.manualslib.com/manual/1259664/Skoda-Octavia.html?page=301")]),
"Subaru": dict(sections=[
 ("Subaru key battery",
  "<p>Forester keys of the 2014 to 2018 generation take a <strong>CR2032</strong>, but other Subaru keys use a CR2025 or CR1620, so read "
  "the old cell first. On most recent Subaru keys, hold the release on the back and pull out the emergency key; that opens a gap where the "
  "case splits. Subaru dealers suggest wrapping the screwdriver tip in tape so you don't crack the plastic.</p>"
  "<p>New cell and it still won't work? After a Singapore downpour, water damage is the usual suspect, and a soaked key can fail for good. "
  "That's when a cloned spare earns its keep.</p>"),
 ("A Subaru habit worth building",
  "<p>Many Forester, XV and WRX owners have Keyless Access with push-button start, so the key rarely leaves a pocket or bag. Keep it in the "
  "same pocket every time, and never put it down in the boot or on a seat while loading: that's how most Subaru lockouts start.</p>"),
 ], sources=[("Subaru dealer guide: changing the key battery", "https://www.subarusouthtampa.com/service/service-and-parts-tips/how-to-change-battery-subaru-key-fob/")]),
"Porsche": dict(sections=[
 ("Porsche key battery: CR2032",
  "<p>The car-shaped Porsche key used on the Macan, Cayenne, Panamera and 911 takes a single <strong>CR2032</strong>. Turn the key over, "
  "release the emergency key and pull it partway out, then press it away from the key body to lift off the back cover. Fit the new cell "
  "+ side up; if the cover won't close, the cell is the wrong way round. If your key doesn't open this way, don't force it: check the handbook.</p>"),
 ("Locked out of a Porsche",
  "<p>Tight panel gaps and expensive paint are exactly why the wedge-and-rod tricks from online videos are a bad idea on a Porsche. We use "
  "non-destructive entry tools made for modern cars, and we check the log card and your NRIC before we start.</p>"),
 ], sources=[("Porsche key battery replacement guide (YOUCANIC)", "https://www.youcanic.com/porsche-key-fob-battery-replacement/")]),
"Audi": dict(sections=[
 ("Audi key battery: CR2032",
  "<p>On the 2017-and-later A4 and the 2018-and-later Q5, the key takes a <strong>CR2032</strong>; a few older Audi keys use a CR2025. "
  "Take the emergency key out first. On some 2015 to 2017 Q5 keys the back cover is held by a single small Torx (T8) screw rather than "
  "clipping off. Handle the new cell by its edges: skin oil on the contacts can shorten its life.</p>"
  "<p>On older A4s with a flip key, a flat battery only stops the remote buttons: the key blade still opens the door and turns the ignition.</p>"),
 ("Audi locked with the key inside",
  "<p>It still happens with advanced keys: a child presses the lock button, the key is in a bag in the boot, or the key's battery is too weak "
  "for the car to detect it. We open the door without damage: no broken glass, no wedges forced into the door frame.</p>"),
 ], sources=[("Audi dealer guide: changing the key battery", "https://www.audigreatneck.com/en/blogs/how-to-change-the-battery-in-your-audi-key-fob/"),
             ("Audi dealer guide: starting with a dead key", "https://www.audigreatneck.com/en/blogs/how-to-start-your-audi-with-a-dead-key-fob/")]),
"Mazda": dict(sections=[
 ("Mazda key battery: CR2025 or CR2032",
  "<p>Mazda's own CX-5 owner's manual lists two key types: <strong>Type A takes a CR2025</strong> and <strong>Type B takes a CR2032</strong>, "
  "and says to replace the cell only with the same type. Start by pressing the knob and drawing out the auxiliary key, which gives you a way "
  "into the case. Mazda recommends having the battery changed at an authorised repairer to avoid damaging the key, so if the case resists, "
  "don't force it.</p>"
  "<p>The manual's sign of a dead key battery: the buttons do nothing and the key's operation indicator light doesn't flash.</p>"),
 ("Mazda lockouts at the void deck",
  "<p>CX-5s and Mazda3s are family cars, and family drop-offs are where keys get left inside: the key goes on the seat while a pram comes "
  "out of the boot. We check the log card against your NRIC and open the door without damage.</p>"),
 ], sources=[("Mazda CX-5 owner's manual: key battery replacement", "https://www.mazdausa.com/static/manuals/2020/cx-5/contents/07031300.html")]),
"Suzuki": dict(sections=[
 ("Suzuki key battery",
  "<p>Most Swift keys of recent years take a <strong>CR2032</strong> coin cell, but key types vary by model and year, so read the number on "
  "the old cell before buying a new one. Take the emergency key out of the fob first, then ease the case apart at its seam with a small "
  "flat screwdriver and fit the new cell the same way up.</p>"
  "<p>On models with keyless start, whether the car will start from a weak key held close to the start button depends on the model, so "
  "check your handbook rather than relying on online tips.</p>"),
 ("Swift, Jimny and Vitara owners",
  "<p>Bought your Suzuki second-hand with only one key? A cloned spare costs far less than the day you lose "
  "the only one. WhatsApp us the model, year and a photo of your key and we'll confirm before you book.</p>"),
 ], sources=[]),
},

"lock": {
"Yew": dict(sections=[
 ("If your Yew lock is rechargeable",
  "<p>Rechargeable locks change the routine: instead of buying AA batteries, you bring the battery pack to a socket. A full charge lasts "
  "a long time, which makes it easy to forget, so tie it to something you already do, like charging the door and gate locks together on "
  "the first weekend of every other month, or the day either lock first warns you.</p>"
  "<p>Keep the right cable and a small power bank somewhere outside the flat: the car, your office drawer or a family member's place. With an "
  "emergency power port, that's the difference between getting in within two minutes and waiting for a locksmith.</p>"),
 ("Yew door and gate sets: two locks, two batteries",
  "<p>A matched set is still two separate locks, each with its own battery, users and settings. Add fingerprints and codes to both, not "
  "just the door lock, or a family member who can open the door may still be stuck at the gate. If only one of the pair stops responding, "
  "it's nearly always that lock's own battery rather than a fault with the set.</p>"),
 ("When someone moves out: clear both locks",
  "<p>A door-and-gate set means two lists of fingerprints and codes. When a tenant, a helper or a contractor stops needing access, "
  "delete their fingerprints and codes from <strong>both</strong> locks on the same day: it's easy to clear the door and forget the "
  "gate, which still lets them through the first barrier. If you don't know how to delete users on your model, the manual for your model "
  "number has the steps; if you can't find it, a reset from inside and re-enrolling everyone is the clean option.</p>"),
 ], sources=[]),
"Gateman": dict(sections=[
 ("Is your old Gateman worth keeping?",
  "<p>Many Gateman locks in Singapore are older units that have been on the same door for years. Older digital locks rarely fail without warning, "
  "and the signs are easy to spot: the motor hums before it turns, keypad buttons need a hard press, a fresh set of batteries runs down "
  "sooner than it used to, or the latch catches on the strike plate. One of these on its own may just need new batteries; two or more "
  "usually means the lock is near the end.</p>"
  "<p>Replacing it on a weekday costs the same as replacing it after it fails at night, minus the lockout. If you replace it, note what's "
  "on the door now: a new lock needs to fit the existing cut-out, or the door has to be modified. Send us a photo of the front and inside "
  "and we'll tell you which locks fit. See <a href=\"~/digital-lock-installation/\">digital lock installation</a>.</p>"),
 ], sources=[]),
"Ezviz": dict(sections=[
 ("EZVIZ DL50FVS face recognition in practice",
  "<p>EZVIZ says the DL50FVS stores up to 50 faces, recognises a face in under 1.5 seconds, and reads faces between about 1.2 and 2 metres "
  "off the ground, so young children may need a fingerprint or code instead. It's designed to reject photos and "
  "videos of a face.</p>"
  "<p>Wi-Fi and video cost battery: EZVIZ says a Wi-Fi connection may reduce battery life, and its support pages suggest turning on "
  "<em>Power-saving Mode</em> under the lock's Settings → Battery in the app if a charge isn't lasting.</p>"),
 ("Which DL50FVS do you have?",
  "<p>EZVIZ sells the DL50FVS with different lock bodies (for example the 5085 and 6068 versions) and as a <em>Plus</em> model, and the "
  "specifications differ between them. The lock body number matters if the lock ever needs replacing, so note it from the box when it's "
  "installed. The versions we checked all list a USB-C emergency port and a mechanical emergency key with a C-grade cylinder.</p>"),
 ], sources=[("EZVIZ DL50FVS (5085) product page", "https://www.ezviz.com/eu/product/DL50FVS-%285085%29/351275"),
             ("EZVIZ DL50FVS support and FAQ", "https://support.ezviz.com/product/dl50fvs/55733"),
             ("EZVIZ DL50FVS (6068) product page", "https://www.ezviz.com/eu/product/DL50FVS-%286068%29/351273"),
             ("EZVIZ DL50FVS Plus product page", "https://www.ezviz.com/product/DL50FVS-Plus/77729")]),
"Lenovo": dict(sections=[
 ("Which Lenovo smart lock is it?",
  "<p>Lenovo has sold several smart locks, and they don't all work the same way. The model name is "
  "usually on the inside unit or the battery cover. Note it down now: it's the first thing we, or Lenovo, will ask.</p>"
  ""),
 ("If your lock needs two methods together",
  "<p>Some smart locks can be set to need two methods together, such as fingerprint plus PIN, before the door opens. It's "
  "more secure, but it doubles the ways to get stuck: a cut finger or a forgotten PIN keeps you out. If you use it, enrol at least one other "
  "household member and keep the mechanical key somewhere outside the home.</p>"),
 ], sources=[]),
"Solity": dict(sections=[
 ("Using emergency power on a Solity lock",
  "<p>If your model has a 9V terminal, hold a fresh battery to it and, while it's "
  "touching, enter your password. Use a fresh <strong>alkaline</strong> 9V; a tired or rechargeable one may not have enough power to drive "
  "the motor. Where the terminal sits depends on the model, so find yours before you need it.</p>"
  "<p>Once you're in, the 9V has done its job. Replace all the main batteries from inside straight away, or the lock will be dead again the "
  "next time you step out.</p>"),
 ("A Solity on the door, another on the gate?",
  "<p>Many Singapore homes pair a push-pull lock on the main door with a rim lock on the gate. They're separate locks with separate "
  "batteries: when one warns you, check the other on the same day, and keep a spare 9V where you can reach it from outside.</p>"),
 ], sources=[]),
},

"safe": {
"Godrej": dict(sections=[
 ("Godrej's own advice on keys and batteries",
  "<p>Godrej says the emergency keys are for two situations only, a forgotten user code or completely drained batteries, and should be "
  "kept hidden somewhere else in your home, never inside the locker. For a locker with dead batteries, Godrej's support page gives two ways "
  "in: connect the external battery adapter (sold as an accessory for some models) or use the emergency override keys.</p>"
  "<p>On some Godrej models the codes are stored in memory that survives a flat battery, so new batteries alone may bring the locker back "
  "with your old code. Godrej also recommends a fresh alkaline battery of the type your model specifies: some take a 9V, others AA cells.</p>"),
 ("Forgotten code and lost key",
  "<p>If both the code and the override key are gone, Godrej asks owners to contact its service team with the product details. In "
  "Singapore, where many Godrej lockers were bought overseas or second-hand, the quicker route is usually a safe locksmith. We open it, "
  "and if the lock can be reset you keep using the locker.</p>"),
 ], sources=[("Godrej support: weak or dead batteries", "https://www.godrejenterprises.com/support/locks-and-security/home-security/common-problems/what-can-i-do-if-the-batteries-are-weak-or-dead"),
             ("Godrej support: where to keep the keys", "https://www.godrejenterprises.com/support/locks-and-security/home-security/common-problems/where-do-i-keep-my-keys-after-i-have-installed-the-locker"),
             ("Godrej support: forgotten password and lost key", "https://www.godrejenterprises.com/support/locks-and-security/home-security/common-problems/i-have-forgotten-my-password-and-i-lost-the-mechanical-key-how-do-i-open-the-locker")]),
"Booil": dict(sections=[
 ("Booil fire safes and fire-resistant cabinets",
  "<p>Fire-resistant safes are built differently from burglary safes: the walls are packed with insulating material that keeps the "
  "inside cool in a fire, and the door closes tight against its seals. That's why a jammed fire safe can't simply be pried open, and why "
  "drilling one is careful work. The hole has to go in the right spot and be sealed afterwards so the fire protection isn't lost. Many "
  "fire-resistant filing cabinets have one lock at the top that secures every drawer together.</p>"),
 ("Battery first, override key second",
  "<p>On many digital safes the override key lock hides behind a small cover near the keypad. So the order matters: try fresh alkaline "
  "batteries if the compartment is on the outside, then the override key, then call us. Keep the override key outside the safe: a key "
  "locked inside is the most common way a simple battery problem turns into a drilling job.</p>"),
 ], sources=[]),
"Phoenix": dict(sections=[
 ("Other Phoenix models",
  "<p>Phoenix makes many electronic safes, and the details change from model to model. On the SS0935E series, the mechanical override "
  "sits under the brass Phoenix nameplate. On models such as the DS2503K, two AA batteries sit in an internal compartment, so the low-battery "
  "beep is your warning to change them while you can still open the door. And on some Phoenix locks, removing the batteries deletes the user "
  "codes, so be ready to set your code again after a battery change.</p>"
  "<p>Some Phoenix models also have a <em>super code</em> that resets the lock to factory settings. If yours has one, it's in the paperwork "
  "that came with the safe. Keep that paperwork anywhere except inside the safe.</p>"),
 ("Lost the Phoenix override key?",
  "<p>Phoenix supplies replacement keys through its support team and dealers, usually against the safe's serial number, so note the serial "
  "now while the safe is open. If it's already locked and the key is gone, we can open it.</p>"),
 ], sources=[("Phoenix SS0935E series manual", "https://manuals.online/phoenix/safe/ss0935e-series/user-manual/t4lg"),
             ("Phoenix DS2503K manual", "https://www.notice-facile.com/en/manual/1568643/phoenix+ds2503k"),
             ("Phoenix DS4651E manual", "https://www.notice-facile.com/en/manual/1568595/phoenix+ds4651e")]),
},
}


def sections_html(group, name):
    e = EXTRA.get(group, {}).get(name)
    if not e:
        return ""
    return "".join(f"<h2>{h}</h2>\n{body}\n" for h, body in e["sections"])


def sources(group, name):
    e = EXTRA.get(group, {}).get(name)
    return list(e["sources"]) if e else []
