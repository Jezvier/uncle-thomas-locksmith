"""
Safe brand pages: /safe-opening/<brand>/  (added 29 Oct 2026)

Built around how people search (Google SG autocomplete): "<brand> safe forgot
password / battery dead / won't open with correct code / override key / reset
code / manual", and Singapore's "safe box" wording.
Facts from the manufacturers' manuals and support pages in each `sources`.
Factory default codes are deliberately NOT published, even where manuals show them.
Independent: not affiliated with any brand.
"""
import config as C
import re as _re
import unicodedata as _u

DATA = {
"Yale": dict(
 about="Yale safe boxes are among the most common home safes in Singapore, from the YSS standard and value safes to fingerprint models such as the YSS/580/W1 and Yale fire safes.",
 battery="Yale's motorised home safes run on AA batteries behind the keypad or inside the door. On the Yale Fire Safe, if the batteries go flat, hold a 9V battery to the two terminals underneath the dial and touch the screen to wake it, then enter your code. Yale says a flat battery doesn't change your PIN.",
 key="Many Yale home safes come with emergency override keys, so keep them outside the safe. The Yale Fire Safe is the exception: Yale says it is not supplied with an override key, which makes the 9V terminals your only way in when the batteries die.",
 code="On Yale motorised safes, open the safe (with the key if needed), hold the Tick key and press 3 together, then enter your new code twice until the screen shows GOOD. On the Fire Safe, codes of 4 to 12 digits are set with the programming button inside, near the battery compartment.",
 forgot="If you forget the code on a Yale Fire Safe, Yale customer services can send a factory code once you give the serial number, proof of purchase and ID. Allow a few days. For other models, the override key opens the safe so you can set a new code.",
 quirk="A Yale safe that shows an error when you try to set a code usually needs Tick and 3 pressed at the same time: hold Tick first, then press 3.",
 sources=[("Yale Fire Safe FAQ", "https://yalehome.co.uk/support/product-support/safes/fire-safes/faq/"),
          ("Yale motorised safe troubleshooting", "https://yalehome.co.uk/support/product-support/safes/motorized-safes/troubleshooting/")],
 faqs=[("How do I open a Yale safe with a dead battery?", "Use the override key if your model has one. On the Yale Fire Safe, hold a 9V battery to the terminals under the dial, touch the screen and enter your code."),
       ("I forgot my Yale safe box code. What can I do?", "Open it with the override key and set a new code. For the Fire Safe, Yale can send a factory code with your serial number, receipt and ID. If you can't wait or don't have them, call us."),
       ("Does a Yale fire safe have an override key?", "No. Yale says its Fire Safe isn't supplied with one, so keep spare batteries and a 9V battery handy.")]),

"SentrySafe": dict(
 about="SentrySafe is an American brand whose fire-resistant and security safes are sold by Singapore hardware stores, including electronic models such as the X055, X105 and X125.",
 battery="On the X055/X105/X125, four AA alkaline batteries sit inside the door: take off the cover between the knob and keypad, then slide the battery cover on the back of the door. A red light when you press a key means the batteries are low.",
 key="The override key comes in a bag attached to the owner's manual. SentrySafe warns not to store it inside the safe. To use it, remove the cover between the knob and keypad, insert the key and turn it clockwise, then, while holding it, turn the knob to open.",
 code="With the door open, remove the battery cover and press the key button in the battery compartment. When the yellow light comes on, enter a new code of 2 to 8 digits and press #. If the light flashes with five beeps, the code wasn't saved: start again. Change the factory code as soon as you set the safe up.",
 forgot="Open the safe with the override key, then set a new code. If the key is lost too, SentrySafe can supply one for some models if you send the serial number (on a label on the outside of the safe) and proof of ownership, which takes time.",
 quirk="When a SentrySafe accepts the code but won't open, try fresh batteries first, then the override key. Don't force the knob.",
 sources=[("SentrySafe X055/X105/X125 user manual (Hardware City Singapore)", "https://hardwarecity.com.sg/uploads/product/1637635883_Sentrysafe X055 _ X105 _ X125 User Manual.pdf")],
 faqs=[("How do I open a SentrySafe without the code?", "Use the override key: remove the cover between the knob and keypad, insert the key, turn it clockwise and hold it while turning the knob."),
       ("How many batteries does a SentrySafe take?", "Electronic models like the X055, X105 and X125 take four AA alkaline batteries inside the door."),
       ("I lost my SentrySafe key and code. Can you open it?", "Yes, with proof of ownership. SentrySafe can also supply keys for some models, but that takes time.")]),

"Phoenix": dict(
 about="Phoenix Safe Company is a British safe maker whose electronic security and fire safes are sold internationally, including models such as the SS0300E.",
 battery="On the SS0300E, four AA alkaline batteries go in a compartment on the back of the door, held by a screw you undo with the supplied Allen key. A red light means they're low: replace them straight away.",
 key="The emergency key hides under the grey plastic plug at the bottom of the keypad. Insert it, turn it anticlockwise and hold it, then turn the handle to open.",
 code="With the door open, press * twice until the yellow light comes on, enter the current master code and #, then the new code and #, then the new code again and #. The light goes off when it's saved; five beeps mean it didn't work. Change the factory master code when you first set the safe up.",
 forgot="Open the safe with the emergency key, then set a new code with the door open.",
 quirk="Always test a new Phoenix code with the door open before closing it.",
 sources=[("Phoenix SS0300E manual (Safelincs)", "https://www.safelincs.co.uk/templates_safelincs/files/datasheets/4184_SS0300E-Manual-EnglishOnly.pdf")],
 faqs=[("Where is the emergency key slot on a Phoenix safe?", "On models like the SS0300E, under the grey plastic plug at the bottom of the keypad."),
       ("How do I change the code on a Phoenix safe?", "With the door open, press * twice, enter the current master code and #, then the new code and # twice. Five beeps mean it didn't save.")]),

"Honeywell": dict(
 about="Honeywell-branded safes are made under licence by LH Licensed Products and sold widely online, including to Singapore buyers, as digital security and fire safes.",
 battery="Digital Honeywell safes typically use four AA batteries, and a flashing red light warns when they're low. If you ignore it, the keypad can stop responding. Some commercial models can take temporary power from a 9V battery held to contacts on the keypad.",
 key="Most digital models have an emergency override key behind a small plastic cover near the keypad or handle. Keys are specific to the lock series, so keep yours outside the safe.",
 code="A small reset button inside the door clears the old code, after which you enter a new one of 3 to 8 digits. Follow your model's manual.",
 forgot="Open with the override key, then use the reset button inside to set a new code.",
 quirk="Three wrong codes in a row trigger a lockout of about five minutes. Wait it out rather than keep trying.",
 sources=[("How to open a Honeywell safe (overview)", "https://library.peoplespharmacy.com/open-honeywell-safe")],
 faqs=[("Why won't my Honeywell safe keypad respond?", "Usually low batteries: a flashing red light warns you first. Use the override key, then replace the four AA batteries."),
       ("My Honeywell safe locked me out after wrong codes. How long?", "About five minutes after three wrong codes. Wait, then enter the code once, slowly.")]),

"Godrej": dict(
 about="Godrej, from India's Godrej Enterprises Group, makes home and office safes and electronic lockers used across Asia, including by Singapore homes and businesses.",
 battery="Godrej says that if a locker's batteries are weak or dead, you can open it by connecting the external battery adapter (supplied as an accessory with the locker) or with the emergency override keys, then replace the internal batteries once it's open.",
 key="Godrej electronic lockers come with emergency override keys. Keep them somewhere safe outside the locker, along with the external battery adapter.",
 code="Codes are changed from inside the open locker following your model's manual.",
 forgot="Use the emergency override keys to open the locker, then set a new code.",
 quirk="If you can't find the external battery adapter or the override keys, don't try to force the door. Call us.",
 sources=[("Godrej support: batteries weak or dead", "https://www.godrejenterprises.com/support/locks-and-security/home-security/common-problems/what-can-i-do-if-the-batteries-are-weak-or-dead")],
 faqs=[("How do I open a Godrej safe with dead batteries?", "Connect the external battery adapter that came with the locker, or use the emergency override keys. Then replace the batteries."),
       ("I've lost my Godrej override keys. Can you open the safe?", "Yes. WhatsApp us photos of the safe and proof of ownership, and we'll quote before we come.")]),

"Diplomat": dict(
 about="Diplomat safes come from Diplomat Safe Ltd, a Busan, South Korea maker founded in 1982 that exports to about 70 countries. Its safes carry fire-test certifications from bodies including Sweden's SP, the US UL, Japan's JIS and Russia's GOST. (Burg-Wächter also sells a German safe range called Diplomat: check your safe's label.)",
 battery="Diplomat electronic safes run on batteries. When the keypad dims or stops responding, replace the batteries before assuming the code is wrong, and check your model's manual for its emergency power or key.",
 key="Many Diplomat electronic safes have a backup key or emergency entry. Find yours now, before you need it.",
 code="Codes are changed with the door open, following your model's manual.",
 forgot="Use the backup key if your model has one, then reset the code. If not, call a safe locksmith rather than forcing it.",
 quirk="Some Diplomat models, such as the mono5, lock the keypad after three wrong entries. Wait for it to clear before trying again.",
 sources=[("Busan city: Diplomat Safe Ltd", "https://www.busan.go.kr/eng/bsnews01/798190"),
          ("Diplomat Japan: Diplomat products", "https://mirumu.jp/en/blogs/media/diplomat-products")],
 faqs=[("Where are Diplomat safes made?", "Diplomat Safe Ltd is based in Busan, South Korea, and was founded in 1982. Burg-Wächter also sells a German range named Diplomat, so check your safe's label."),
       ("My Diplomat safe keypad locked after wrong codes. What now?", "Some models lock after three wrong entries. Wait for it to clear, then enter the code once, slowly.")]),

"Eagle": dict(
 about="Eagle Safes are made by Korea's Sun Safes Mfg. and sold across Asia, from traditional dial safes to electronic fire safes such as the YES-M020, which carries Sweden's SP 60-minute paper fire certification.",
 battery="Electronic Eagle safes like the YES-M020 take four 1.5V AA batteries. A dim or silent keypad usually means flat batteries, not a broken lock.",
 key="Check your Eagle model for an emergency key. Traditional Eagle safes use a dial and key rather than electronics.",
 code="The YES-M020's electronic lock supports two independent passcodes, which suits households where two people need access. Codes are changed with the door open, following the manual.",
 forgot="If you forget the code and your model has no emergency key, a safe locksmith can open it. Don't keep trying codes or force the handle.",
 quirk="On Eagle dial safes, a dial that turns stiffly or spins freely points to worn lock parts. Stop turning it and call for help.",
 sources=[("Korea JoongAng Daily: Korean safes (Sun Safes / Eagle)", "https://www.koreajoongangdaily.com/business/korean-safes-are-cracking-open-new-market/10061036"),
          ("Eagle YES-M020 specifications (Costco)", "https://www.costco.com.tw/Electronics/Security/Safe/Eagle-Fire-Resistant-Safe/p/117087")],
 faqs=[("Who makes Eagle safes?", "Eagle Safes are made by Sun Safes Mfg. in South Korea."),
       ("What batteries does an Eagle safe use?", "Electronic models such as the YES-M020 take four AA batteries.")]),

"Bumil": dict(
 about="Bumil (Bumilsafe Mfg.) is a South Korean safe maker whose fire safes hold UL (US), P-mark (Sweden), KS (Korea) and JIS (Japan) fire certifications. Bumil home safes are a common sight in Singapore flats.",
 battery="Bumil electronic safes run on batteries behind the keypad or inside the door. If the keypad goes dark, try fresh batteries first.",
 key="Check whether your Bumil model has an emergency key, and keep it outside the safe.",
 code="Codes are changed with the door open, following your model's manual.",
 forgot="If the code is forgotten and there's no emergency key, a safesmith can open the safe. When a Bumil keypad lock has failed, the lock can often be replaced so you keep the safe.",
 quirk="When an older Bumil keypad stops working even with new batteries, the keypad lock itself may have failed. We've opened Bumil safes like this and fitted a new electronic keypad lock, so the owner kept the same safe.",
 sources=[("Korea JoongAng Daily: Korean safes (Bumilsafe Mfg.)", "https://www.koreajoongangdaily.com/business/korean-safes-are-cracking-open-new-market/10061036")],
 faqs=[("My Bumil safe keypad is dead even with new batteries. Do I need a new safe?", "Usually not. The keypad lock can often be replaced after the safe is opened. See our photos on the safe combination change page."),
       ("Can you open a Bumil safe without the code?", "Yes, with proof of ownership. Send photos of the safe and we'll quote before we come.")]),

"Booil": dict(
 about="Booil Safes Co. is a South Korean safe maker founded in 1971 in Gimhae, making fire-resistant and anti-burglary safes and fire-resistant filing cabinets, sold in Singapore as home and office safes.",
 battery="Booil electronic safes run on batteries. A weak or silent keypad usually means the batteries need replacing.",
 key="Check whether your Booil model has an emergency key, and store it outside the safe.",
 code="Codes are changed with the door open, following your model's manual.",
 forgot="Without the code or an emergency key, call a safe locksmith. Don't try to pry the door: fire safes are built to resist it.",
 quirk="Fire-resistant filing cabinets are heavy and awkward to move. Open them where they stand rather than trying to shift them.",
 sources=[("Booil Safes Co. company profile", "https://www.ampliz.com/company/booil-safes-co-ltd/83610288")],
 faqs=[("Where are Booil safes made?", "Booil Safes Co. is based in Gimhae, South Korea, and was founded in 1971."),
       ("Can you open a Booil fire-resistant filing cabinet?", "Yes. We open safes and cabinets where they stand, after checking ownership or business authorisation.")]),

"Chubb": dict(
 about="Chubbsafes traces back to the Chubb brothers' lock workshop founded in 1818 in England. Since 2000 the Chubbsafes brand has been owned under licence by Sweden's Gunnebo Group. Older Chubb safes, often with a combination dial and a key lock, are still in use in Singapore offices and shophouses.",
 battery="Newer Chubbsafes models may have electronic locks that run on batteries. Older Chubb safes use mechanical dial and key locks with no batteries at all.",
 key="Many older Chubb safes need both a key and the combination. If the key is lost, the lock usually has to be opened by a safesmith and a new lock fitted.",
 code="Changing the combination on a mechanical Chubb dial lock needs a change key and care, because a mistake can lock you out. It's a safesmith's job.",
 forgot="Forgotten combinations on old Chubb dial safes are a classic safesmith job. Don't keep spinning the dial or force the handle.",
 quirk="Chubbsafes are graded for burglary resistance (grades I to VI for safes) by the European Certification Body, and certified for 30, 60 or 120 minutes of fire protection for paper or data.",
 sources=[("Chubbsafes (Wikipedia)", "https://en.wikipedia.org/wiki/Chubbsafes")],
 faqs=[("Can you open an old Chubb safe without the combination?", "Yes. Old Chubb dial safes are a safesmith's job. We check ownership first, then open it and can fit a new lock."),
       ("Who owns Chubb safes now?", "Since 2000, the Chubbsafes brand has been owned under licence by Gunnebo Group.")]),

"Burg-Wächter": dict(
 about="Burg-Wächter is a German security company whose safes include the Point Safe, Basic Safe, Smart Safe, Home Safe, Karat, Diplomat and Ranger ranges.",
 battery="On most Burg-Wächter electronic safes, the code is kept when you change the batteries; on the Basic Safe, Smart Safe and Uni-Safe it has to be reprogrammed after a battery change. If the keypad does nothing, Burg-Wächter suggests fresh batteries and clean contacts first.",
 key="Some ranges have emergency keys (Basic Safe, Smart Safe and Uni-Safe keep them in a bag in front of the door; the Point Safe in the protective cardboard). But Burg-Wächter says the Home Safe, Cityline, Combi Line, Karat, Diplomat and Ranger ranges have no mechanical emergency lock.",
 code="On Basic, Smart and Uni-Safe models, codes are reprogrammed with the door open using the inside button. Follow the manual for your range.",
 forgot="With an emergency key, open the safe and reprogram the code. On ranges without an emergency lock (Home Safe, Cityline, Combi Line, Karat, Diplomat, Ranger), Burg-Wächter directs owners to a dealer or its service line. That's where a safe locksmith comes in.",
 quirk="Because several Burg-Wächter ranges have no emergency key, a forgotten code on those safes can't be solved with a key at all.",
 sources=[("Burg-Wächter safe FAQs", "https://burg.biz/en/pages/faqs-safes")],
 faqs=[("Does my Burg-Wächter safe have an emergency key?", "Basic Safe, Smart Safe, Uni-Safe and Point Safe models do. Home Safe, Cityline, Combi Line, Karat, Diplomat and Ranger models have no mechanical emergency lock."),
       ("Do I lose my code when I change Burg-Wächter safe batteries?", "On most ranges the code is kept. On Basic Safe, Smart Safe and Uni-Safe models it must be reprogrammed.")]),
}

SCENARIO = {
"Yale": "A family moves flat and packs their Yale safe box with the batteries still in. Weeks later the keypad is dead, the override key is somewhere in an unopened carton, and the passports they need for a trip are inside. We open the safe and they set a new code.",
"SentrySafe": "Someone stores the SentrySafe override key inside the safe \"for safekeeping\". Months later the batteries die. With the key locked in, there's no way in without a safe locksmith.",
"Phoenix": "An office's Phoenix safe has been opened by the same manager for years. After they leave, nobody knows the master code, and the emergency key went with them. We confirm the company's authorisation, open the safe, and the new manager sets a fresh code.",
"Honeywell": "A home owner tries several old codes on a Honeywell safe and triggers the five-minute lockout, again and again. When none of the codes are right, we open it for them.",
"Godrej": "A family's Godrej locker goes dead. The external battery adapter that came with it was thrown out with the packaging years ago, and the override keys can't be found. We open the locker and they replace the batteries.",
"Diplomat": "Someone enters the wrong code three times on a Diplomat safe and the keypad locks. They keep trying, and it keeps locking. Once it's clear the code itself is forgotten, we open it.",
"Eagle": "An older Eagle dial safe in a shophouse office has a dial that's started to spin freely. The owner keeps turning it, hoping it will catch. We stop that, open the safe and talk through the options.",
"Bumil": "A Bumil home safe's keypad stops working, even with brand-new batteries. The keypad lock has failed, so we open the safe and fit a new electronic keypad lock, and the owner keeps the same safe.",
"Booil": "An office moving premises finds its Booil fire-resistant filing cabinet locked, and nobody knows the code. We open it on site before the movers arrive.",
"Chubb": "A business takes over a shophouse and finds an old Chubb safe with a dial and a key lock. No combination, no key. With proof the business owns the premises and contents, we open it and fit a new lock.",
"Burg-Wächter": "An owner forgets the code on a Burg-Wächter Home Safe, then learns that model has no emergency key. We open the safe and talk through options for the lock.",
}

SAFE_BRAND_PAGES = list(DATA.keys())


def _slug(n):
    return _re.sub(r'[^a-z0-9]+', '-', _u.normalize('NFKD', n).encode('ascii', 'ignore').decode().lower()).strip('-')


BRANDS = [dict(name=b, slug=_slug(b), **DATA[b]) for b in SAFE_BRAND_PAGES]


def _fit(*options, limit=60):
    for o in options:
        if len(o) <= limit:
            return o
    return options[-1][:limit]


def _strip(s):
    return _re.sub(r"<[^>]+>", "", s)


def pills_html():
    return '<ul class="link-pills">' + "".join(f'<li><a href="~/safe-opening/{b["slug"]}/">{b["name"]}{"" if b["name"].lower().endswith("safe") else " safe"}</a></li>' for b in BRANDS) + '</ul>'


def build(x):
    C_ = x["C"]
    for b in BRANDS:
        n = b["name"]
        path = f"safe-opening/{b['slug']}/"
        title = _fit(f"{n} Safe Forgot Password, Battery Dead or Won't Open?",
                     f"{n} Safe: Forgot Code, Battery Dead, Won't Open",
                     f"{n} Safe Forgot Code or Won't Open?")
        h1 = f"{n} Safe Forgot Password, Battery Dead or Won't Open?"
        desc = _fit(f"{n} safe box forgot password, battery dead or won't open with the correct code? Override key, batteries and code reset explained, plus 24/7 safe opening in Singapore.",
                    f"{n} safe box forgot password, battery dead or won't open? Override key, batteries and code reset explained, plus 24/7 safe opening in Singapore.",
                    f"{n} safe won't open? Batteries, override key and code reset explained, plus 24/7 safe opening in Singapore.", limit=160)
        crumbs = [("Home", ""), ("Services", "services/"), ("Safe opening", "safe-opening/"), (n, path)]
        faqs = b["faqs"] + [
            (f"Can a locksmith open a {n} safe?", f"Yes. Uncle Thomas is a US-trained safesmith who opens every type of safe, including {n}. We check proof of ownership first, and agree the price before we come."),
            (f"How much does it cost to open a {n} safe in Singapore?", "It depends on the model, the lock and what's wrong, so it's quoted per job. WhatsApp photos of the safe's front, keypad or dial and brand label to {PHONE} for a price before we come."),
        ]
        i = [o["slug"] for o in BRANDS].index(b["slug"])
        near = (BRANDS[i + 1:] + BRANDS[:i])[:5]
        others = " · ".join(f'<a href="~/safe-opening/{o["slug"]}/">{o["name"]}</a>' for o in near)
        src = ""
        if b["sources"]:
            src = ('<p class="note"><strong>Sources:</strong> ' +
                   " · ".join(f'<a href="{u}" target="_blank" rel="noopener">{t}</a>' for t, u in b["sources"]) +
                   ". Checked October 2026. Features vary by model: check your safe's own manual. We never publish factory default codes.</p>")
        body = (x["page_hero"](crumbs, h1,
                f"Forgot the code, batteries dead, lost the override key, or the {n} safe box won't open even with the right code: what to try first, and how Uncle Thomas, a US-trained safesmith, can open it.",
                ["US-trained safesmith", "24/7 islandwide", "Ownership checked"]) +
                f'''<section class="section"><div class="container narrow prose">
<p><strong>The short answer:</strong> {_strip(b["battery"]).split(". ")[0]}. {_strip(b["key"]).split(". ")[0]}. If neither works, don't force the handle: call or WhatsApp {{PHONE}}.</p>
<h2>{n} safes in Singapore</h2>
<p>{b["about"]}</p>
<h2>{n} safe battery dead? How to open it</h2>
<p>{b["battery"]}</p>
<h2>{n} safe override key</h2>
<p>{b["key"]}</p>
<h2>Forgot the password on your {n} safe box?</h2>
<p>{b["forgot"]}</p>
<h2>How to change or reset the code on a {n} safe</h2>
<p>{b["code"]}</p>
<h2>{n} safe won't open with the correct code?</h2>
<p>{b["quirk"]} More causes: <a href="~/guides/safe-wont-open-correct-code/">safe won't open with the correct code</a>.</p>
<h2>A typical {n} call</h2>
<p>This is the kind of {n} call we often get: {SCENARIO.get(n, "")}</p>
<h2>When to call a safe locksmith</h2>
<p>If power and the key don't work, call or WhatsApp {{PHONE}}, 24/7. Uncle Thomas, a US-trained safesmith, opens {n} safes across Singapore after checking ownership, with the price agreed first. See <a href="~/safe-opening/">safe opening</a> · <a href="~/safe-combination-change/">safe lock replacement</a> · <a href="~/guides/safe-drilling-explained/">drilling explained</a>. Not affiliated with {n}.</p>
{src}
<p>Other safe brands: {others} · <a href="~/safe-opening/#brands">all safe brands</a></p>
</div></section>
<section class="section section-alt"><div class="container narrow">{x["faq_html"](faqs, f"{n} Safe FAQs")}</div></section>''' +
                x["cta_band"](f"{n} Safe Won't Open?"))
        svc = {"@type": "Service", "@id": C_.SITE + "/" + path + "#service",
               "name": f"{n} safe opening — Singapore", "serviceType": "Safe opening",
               "description": desc, "provider": {"@id": x["BUSINESS_ID"]},
               "areaServed": {"@type": "Country", "name": "Singapore"}, "url": C_.SITE + "/" + path}
        nodes = x["page_schema"](path, title, desc, crumbs, faqs=faqs, extra=[svc])
        x["render"](path, title, desc, body, nodes, priority="0.7")
