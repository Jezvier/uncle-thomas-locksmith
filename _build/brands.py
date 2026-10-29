"""
Digital and smart lock brand pages: /digital-lock-opening/<brand>/

Rebuilt 29 Oct 2026 around how people in Singapore actually search (Google SG
autocomplete): "<brand> digital lock battery flat / battery replacement / change
password / reset / not working / manual / no battery how to open".

Facts come from the manufacturers' manuals and support pages listed in each
brand's `sources`. Where a fact was only confirmed for one model, the text names
that model. Features vary by model, so pages always tell owners to check theirs.
We are independent and not affiliated with any brand.
Only brands in config.BRAND_PAGES are built.
"""
import config as C

# kind: "digital" for keypad digital door locks, "smart" for app-first smart locks.
DATA = {
"Samsung": dict(kind="digital",
 about="Samsung digital door locks are among the most common locks on HDB main doors and gates in Singapore, from rim locks on metal gates to push-pull locks such as the SHS-P718, SHP-DP728 and SHP-DR708 on main doors. Samsung's digital door lock range is now sold under the Zigbang name (see our <a href=\"~/digital-lock-opening/zigbang/\">Zigbang page</a>), so many locks on Singapore doors are older Samsung-branded units.",
 power="Many Samsung models have emergency power contacts on the outside of the lock, usually at the bottom of the front unit, where you hold a 9V battery to wake the lock and then enter your PIN. Once you're in, replace the main batteries straight away.",
 battery="Samsung locks run on AA alkaline batteries in the battery compartment of the inside unit. The number depends on the model, so count the slots and replace every battery at the same time with fresh alkaline ones. Don't mix old and new.",
 key="Some Samsung models, such as the SHP-DP728 and SHP-DR708, come with a mechanical emergency key. Others, such as the keypad-only SHS-1321, have no key at all, so emergency power is the only way in when the batteries die.",
 pin="Codes are changed from inside the home, usually with a registration or setting button under the battery cover, then following the voice prompts. The exact steps differ by model, so find the model number (often on the inside unit or the battery cover) and follow that manual.",
 reset="A factory reset wipes every PIN, card and fingerprint and can only be done from inside, using the button under the battery cover. You never need it to get back in from outside.",
 lockout="Like most digital locks, Samsung locks block the keypad for a few minutes after several wrong attempts. Wait, then enter the code once, slowly.",
 quirk="On older Samsung locks, a keypad that lights up but doesn't accept a correct code is often a sign of a weak battery or worn keypad contacts rather than a forgotten PIN.",
 sources=[("Zigbang (previously Samsung) SHP-DP609 listing, JB Hi-Fi", "https://www.jbhifi.com.au/products/zigbang-previously-samsung-shp-dp609"),
          ("TheSmartLocal: digital locks in Singapore (key override by model)", "https://thesmartlocal.com/read/digital-locks-singapore/")],
 faqs=[("Where is the emergency battery point on a Samsung digital lock?", "On many models it's on the outside, at the bottom of the front unit. Hold a 9V battery to the contacts and enter your code. Models differ, so check your manual."),
       ("My Samsung lock beeps but won't open with the right PIN. Why?", "Often it's low battery power or a mechanical problem with the lock body. Try emergency power first; if it still won't open, call us."),
       ("Is Samsung digital lock now Zigbang?", "Yes. Samsung's digital door lock range is now sold under the Zigbang brand, and many models keep the same SHP model numbers.")]),

"Zigbang": dict(kind="digital",
 about="Zigbang is the name Samsung's digital door locks are now sold under. Models such as the SHP-DP609 push-pull lock are listed in Singapore as Zigbang, and retailers describe them as \"previously Samsung\". If your lock says Samsung on the front but your new one says Zigbang, it's the same family of locks.",
 power="If the batteries go completely flat, use the emergency power contacts on the outside of the lock to wake it, then enter your PIN or use your fingerprint. Check your model's manual for where the contacts are and whether they take a 9V battery.",
 battery="Zigbang locks run on AA alkaline batteries in the inside unit, with a battery-dead alarm to warn you. Replace them all at once, as soon as the warning starts.",
 key="Whether there's a mechanical key depends on the model. If yours came with one, keep it outside the home, not in a drawer inside.",
 pin="Many Zigbang locks are managed in the Zigbang app, which can delete and recreate passcodes if a phone is lost. Without the app, codes are changed from the inside unit following the model's manual.",
 reset="A factory reset wipes all codes, cards and fingerprints and is done from inside. Use it only if you're inside and want to start again.",
 lockout="After several wrong codes the keypad pauses for a few minutes. Wait it out rather than keep trying.",
 quirk="Wi-Fi and app features rely on your home network. If the app can't reach the lock, try the PIN or fingerprint at the door first: the lock itself can still work.",
 sources=[("Zigbang SHP-DP609, Harvey Norman Singapore", "https://www.harveynorman.com.sg/smart-tech-and-phones/smart-home/smart-security/zigbang-digital-door-mortise-lock-silver-shp-dp609.html"),
          ("Samsung digital key FAQ (Zigbang app pairing)", "https://www.samsung.com/hk_en/apps/samsung-lock/")],
 faqs=[("Is Zigbang the same as Samsung digital lock?", "Zigbang now sells the digital door lock range that used to carry the Samsung name, including models such as the SHP-DP609."),
       ("Can I unlock my Zigbang lock from my phone?", "On Wi-Fi and NFC models set up in the Zigbang app, yes. The lock still needs battery power, and you should keep a PIN or fingerprint set up too.")]),

"Yale": dict(kind="digital",
 about="Yale digital locks are widely sold in Singapore and fitted to HDB doors and gates, condos and landed homes. The range covers rim locks for gates, mortise locks for main doors such as the YDM4109 and YDM7220, and smart locks with app control.",
 power="On the YDM4109, pull down the emergency cover on the front unit and hold a 9V battery to the emergency terminal. Touch the keypad, enter your password, then remove the 9V battery once the motor has turned. The YDM7220 also takes a 9V battery on its external terminal. Some newer Yale models use a USB port instead, so check yours.",
 battery="The YDM4109 takes four 1.5V AA alkaline batteries, which Yale says last about a year at ten uses a day. The YDM7220 also takes four AA batteries. When the low-battery lamp lights up or the voice says \"Please replace batteries\", replace all four at once.",
 key="The YDM4109 has an emergency key slot behind the same front cover as the 9V terminal. Not every Yale lock has one: the YDR3110 RFID lock, for example, has no mechanical key.",
 pin="On the YDM4109, open the battery cover on the inside unit, press the Registration button once, press 1 then 2 as the voice guide asks, enter the current 6-digit Master Number and #, enter the new Master Number, then press Registration again. The factory Master Number is printed in the manual: change it on day one.",
 reset="A reset clears registered codes and fingerprints, so do it only from inside, with the manual for your model in hand. It's never needed to get in from outside.",
 lockout="On the YDM4109, five wrong passwords or fingerprints in a row trigger a 3-minute lock. Wait 3 minutes, or someone inside can release it by pressing the Registration button or turning the inside handle.",
 quirk="If someone inside has switched on the Inside Forced Lock (privacy) switch, the keypad refuses codes from outside. It's a common surprise when one person is home and another comes back late.",
 sources=[("Yale YDM4109 user manual (ASSA ABLOY)", "https://static-mpc.assaabloy.com/yalefile//Fetchfile.aspx?id=21691"),
          ("Shopee: best digital door locks Singapore (YDM7220 specs)", "https://shopee.sg/blog/best-digital-door-locks-singapore/")],
 faqs=[("How do I open a Yale digital lock with a dead battery?", "On models like the YDM4109, pull down the front emergency cover, hold a 9V battery to the terminal and enter your password. The emergency key slot is behind the same cover."),
       ("My Yale lock won't accept my code. Is it locked from inside?", "It might be. The Inside Forced Lock (privacy) switch blocks outside codes. Ask anyone inside to switch it off, or call us if no one is home."),
       ("How long do Yale digital lock batteries last?", "Yale says about a year for the YDM4109 at ten uses a day. Heat, humidity and heavy use shorten it.")]),

"Philips": dict(kind="digital",
 about="Philips digital locks, sold in the EasyKey range, are popular for HDB main doors and condo doors in Singapore, especially push-pull models such as the EasyKey 9300 with fingerprint, PIN, card and app features.",
 power="The Philips EasyKey manual we checked uses a Micro USB emergency power port: plug in a 5V power bank and the lock wakes up so you can unlock it. Newer models may use USB-C, so check which cable yours needs before you need it.",
 battery="That EasyKey manual specifies four 1.5V alkaline batteries, with room in the compartment for eight if you want longer life. When the red light flashes and the voice says \"Low battery. Please replace all batteries\", replace them all.",
 key="EasyKey locks come with two mechanical keys for emergencies such as a flat battery or a forgotten PIN.",
 pin="Press #, enter the master PIN and confirm, then press 1 to change the master PIN and enter the new code twice. The default master PIN is in the manual, and Philips says to change it right after installation.",
 reset="Remove the battery cover on the inside unit and double-press the RES button with a pointed object until you hear \"Restored to factory settings\". This deletes every user, so it's a last resort for when you're inside.",
 lockout="Five wrong attempts in a row with the same method (PIN, card or fingerprint) lock that method for 3 minutes.",
 quirk="Fingerprint readers can struggle when fingers are wet, very dry or cut. If the fingerprint fails, try your PIN or card before assuming the lock is faulty.",
 sources=[("Philips EasyKey user manual", "https://www.documents.philips.com/assets/20230824/865102c24cc2404da7afb068005a9334.pdf")],
 faqs=[("How do I charge a Philips digital lock from outside?", "Connect a 5V power bank to the emergency USB port (Micro USB on the EasyKey manual we checked). This only wakes the lock so you can get in: replace the batteries afterwards."),
       ("How do I factory reset a Philips EasyKey lock?", "From inside: remove the battery cover and double-press the RES button until you hear \"Restored to factory settings\". It deletes all users."),
       ("My Philips fingerprint reader stopped working. Is the lock broken?", "Not necessarily. Try your PIN or card. Wet or dry fingers often cause failed reads.")]),

"Igloohome": dict(kind="smart",
 about="Igloohome is a Singapore-founded smart lock brand, popular with homeowners and landlords who want app control and shareable access codes. Its Mortise 2+ and deadbolt models are common on HDB and condo doors.",
 power="The Mortise 2+ has a 9V jumpstart: press a 9V battery's terminals against the two silver plates on the front of the lock. When it beeps, it has power and you can enter your PIN.",
 battery="Igloohome lists the Mortise 2+ as taking 8 AA alkaline batteries, lasting up to 18 months. Replace all of them together when the lock or app warns you.",
 key="The Mortise 2+ comes with physical keys (five in the box). Igloohome recommends keeping at least one on you.",
 pin="Codes are managed in the igloohome app, where you can create permanent, time-limited or one-time PINs and remove old ones. Landlords can issue codes to tenants and guests without meeting them.",
 reset="Resetting removes the lock from your app account and wipes its access settings, so it's done from inside with the app. If you're locked out, use the 9V jumpstart or a key instead.",
 lockout="Repeated wrong codes trigger a temporary keypad lockout. Wait it out, then try once.",
 quirk="If a code stops working, check its validity period in the app before calling: expired guest or tenant codes are a common cause.",
 sources=[("igloohome support: batteries run out and locked outside", "https://support.igloohome.co/support/solutions/articles/35000169783-my-batteries-have-completely-run-out-and-i-am-locked-outside-my-house-what-can-i-do-"),
          ("igloohome Mortise 2+ specifications", "https://igloohome.co/products/mortise-2-plus")],
 faqs=[("How do I open an Igloohome lock with dead batteries?", "On the Mortise 2+, press a 9V battery against the two silver plates on the front, wait for the beep, then enter your PIN. Or use one of the physical keys."),
       ("How many batteries does an Igloohome Mortise 2+ take?", "Eight AA alkaline batteries, which igloohome says last up to 18 months."),
       ("A guest's code isn't working on my Igloohome lock. What should I check?", "Check whether the code has expired or was set for a different time window in the app. If the lock isn't responding at all, check the batteries.")]),

"Gateman": dict(kind="digital",
 about="Gateman digital locks, made by ASSA ABLOY's Korean business, have been fitted to Singapore homes for many years on HDB main doors and gates. Push-pull models such as the GP-700D run on 4 AA batteries. Many owners have older Gateman models that still work but are starting to show their age.",
 power="Many Gateman models have emergency power contacts on the outside for a 9V battery. Hold the battery to the contacts, then enter your code.",
 battery="Gateman locks take AA alkaline batteries in the inside unit: four on push-pull models such as the GP-700D. Replace them all at once at the first low-battery warning.",
 key="Some Gateman models include a mechanical backup key and some don't. If yours came with one, keep it outside the home.",
 pin="Codes are registered and changed from inside, using the registration button under the battery cover and the steps in your model's manual.",
 reset="Resetting deletes all registered codes and cards, and is done from inside only.",
 lockout="After several wrong codes the keypad pauses for a few minutes. Wait, then try once.",
 quirk="Older Gateman locks often show worn keypads or slower motors before they fail completely. If your lock is getting slow or unreliable, plan a replacement before it locks you out.",
 sources=[("Gateman GP-700D listing (4×AA)", "https://www.ebay.de/itm/256793967609")],
 faqs=[("My old Gateman lock is slow to open. Should I replace it?", "Slow motors and unreliable keypads are common warning signs on older locks. Replacing it before it fails avoids an emergency lockout."),
       ("How do I wake a Gateman lock with a flat battery?", "On many models, hold a 9V battery to the emergency contacts on the outside and enter your code. Check your manual for your model.")]),

"Kaadas": dict(kind="digital",
 about="Kaadas digital and smart locks are a common sight on Singapore HDB gates and main doors, often fitted as a matching gate-and-door set with fingerprint, PIN, card and app access.",
 power="Kaadas locks take emergency power through a USB port, typically on the bottom edge of the outside keypad. Plug in a power bank with the right cable (USB-C on models like the R8; some older models use Micro USB), wait for the keypad to light up, then unlock as normal.",
 battery="Most Kaadas models use non-rechargeable alkaline AA batteries: the R8 manual specifies four, and so do models like the K9-5W. Face-recognition models use a rechargeable lithium battery instead. Replace all the batteries together.",
 key="Kaadas says every Kaadas lock comes with physical mechanical keys that work without power. Keep one outside the home.",
 pin="On the R8, touch the keypad to wake it, enter #, the Master PIN and #, then choose option 1, \"Modify Master PIN code\". The default Master PIN is in the manual: change it straight away.",
 reset="Pressing the reset button restores factory settings and deletes every user credential, so it's done from inside only.",
 lockout="On the R8, five wrong PINs, cards or fingerprints lock the system for 3 minutes.",
 quirk="Gate and door sets mean two locks and two sets of batteries. If one lock in the pair starts acting up, check its batteries separately.",
 sources=[("Kaadas: battery dead, how to open a digital lock", "https://kaadas.com.my/?p=8314"),
          ("Kaadas R8 manual (ManualsLib)", "https://www.manualslib.com/manual/4083489/Kaadas-R8-5.html")],
 faqs=[("How do I open a Kaadas lock with a flat battery?", "Plug a power bank into the emergency USB port on the bottom of the outside keypad, wait for it to light up, then unlock. Or use the mechanical key."),
       ("What batteries does a Kaadas digital lock use?", "Most models use alkaline AA batteries (four on the R8 and K9-5W). Face-recognition models use a rechargeable lithium battery."),
       ("My Kaadas gate lock works but the door lock doesn't. Why?", "They run on separate batteries. Check the door lock's batteries first.")]),

"Solity": dict(kind="digital",
 about="Solity is a Korean-made digital lock brand found on many Singapore HDB and condo doors, with push-pull and gate models such as the GEA1000BK that use fingerprint, PIN, card and app access.",
 power="Models such as the GEA1000BK have an emergency port for a 9V battery on the outside. Hold the battery to it, then enter your PIN.",
 battery="The GEA1000BK takes eight 1.5V AA batteries. Replace them all at once at the first low-battery warning.",
 key="The GEA1000BK includes a mechanical key. Not every model does, so check yours.",
 pin="Codes are changed from the inside unit or, on Wi-Fi models, the Solity app. Follow the manual for your model number.",
 reset="A factory reset deletes all fingerprints, cards and codes and is done from inside only.",
 lockout="After several wrong codes the keypad pauses for a few minutes. Wait, then try once.",
 quirk="A Solity lock that beeps but won't turn the latch may have a weak battery or a mechanical problem in the lock body rather than a wrong code.",
 sources=[("Shopee: best digital door locks Singapore (Solity GEA1000BK specs)", "https://shopee.sg/blog/best-digital-door-locks-singapore/")],
 faqs=[("Where is the emergency power point on a Solity lock?", "On models like the GEA1000BK there's a 9V emergency port on the outside. Check your manual, or send us a photo."),
       ("My Solity lock accepts the code but won't open. What's wrong?", "Usually a low battery or a mechanical fault in the lock body. Don't force the handle. Call us and we'll open it.")]),

"Häfele": dict(kind="digital",
 about="Häfele digital and smart locks, such as the EL-series, are often fitted by interior designers and renovation contractors in Singapore condos and HDB flats.",
 power="Many Häfele models accept emergency power from outside through a USB port or battery contacts. Check your model's manual so you're prepared.",
 battery="Häfele digital locks run on AA alkaline batteries in the inside unit. Replace them all at the first low-battery warning.",
 key="Many Häfele models include a mechanical backup key (the EL9000 does). If your contractor handed one over, keep it outside the home.",
 pin="Codes are changed with the master PIN through the keypad menu or app. If your contractor set the lock up, ask them to hand over the master PIN and app account first.",
 reset="A factory reset deletes all users and is done from inside. Do it when you move in, so no previous owner or contractor code still works.",
 lockout="Several wrong codes pause the keypad for a few minutes.",
 quirk="If your lock was installed during a renovation, the admin PIN or app account may still be under the contractor's details. Ask them to hand it over so you can manage it yourself.",
 sources=[("TheSmartLocal: digital locks in Singapore (Häfele EL9000)", "https://thesmartlocal.com/read/digital-locks-singapore/")],
 faqs=[("My Häfele lock was installed by my contractor and I don't know the master PIN. Can you help?", "If you're locked out, yes, we'll open it. For the master PIN, ask your contractor or Häfele first."),
       ("How do I power a Häfele lock with flat batteries?", "Many models take emergency power through USB or battery contacts on the outside. Check your manual for your model.")]),

"Aqara": dict(kind="smart",
 about="Aqara smart locks such as the U100 are popular with Singapore homeowners who run a smart home, connecting to the Aqara app and smart home systems, with fingerprint, PIN, card and app unlocking.",
 power="If the batteries run out, plug a power bank into the U100's USB-C emergency power port on the outside keypad, then unlock with your PIN or fingerprint.",
 battery="The U100 takes four AA batteries (6V). Aqara recommends original or alkaline batteries, as others may leak.",
 key="The U100 comes with two mechanical keys: slide the keyhole cover aside and unlock with the key.",
 pin="PINs are managed in the Aqara Home app, where you can add, remove and schedule codes.",
 reset="Long-press the Reset button for 3 seconds and release after the voice prompt. This clears all users, so do it from inside only.",
 lockout="Repeated wrong attempts trigger a temporary keypad lockout.",
 quirk="If the app shows the lock offline, it may just be the hub or Wi-Fi rather than the lock. Try PIN or fingerprint at the door before assuming the lock has failed.",
 sources=[("Aqara Smart Lock U100 user manual", "https://www.seam.co/img/device-db/aqara/manuals/aqara_smart-lock-u100_user_manual.pdf")],
 faqs=[("Can I open my Aqara smart lock from the app if I'm locked out?", "If the lock has power and is online, often yes. If the batteries are flat, use the USB-C emergency port or the key."),
       ("How do I reset an Aqara U100?", "From inside, long-press the Reset button for 3 seconds and release after the voice prompt. All users are cleared."),
       ("My Aqara lock shows offline in the app. Is it broken?", "Not necessarily. Check your hub and Wi-Fi. The lock usually still works with PIN or fingerprint.")]),

"Xiaomi": dict(kind="smart",
 about="Xiaomi smart door locks, such as the Xiaomi Automatic Smart Door Lock sold in Singapore, are bought by many homeowners for their app control and price, and are often fitted to HDB and condo main doors.",
 power="The Xiaomi Automatic Smart Door Lock has a 5V USB-C emergency power port on the front panel. Connect a power bank and unlock as normal.",
 battery="It takes eight AA batteries (6V), loaded from the rear panel inside. A flashing battery light on the front panel means it's time to replace them.",
 key="Two emergency keys come in the box. On the front, press the * at the bottom of the key cover, pull the cover down and use the key. Inside, the emergency knob opens the door too.",
 pin="Codes and users are managed in the Xiaomi Home app after pairing over Bluetooth.",
 reset="A reset removes all users and unpairs the lock from the app. Do it only from inside, following Xiaomi's instructions for your model.",
 lockout="Repeated wrong attempts trigger a temporary keypad lockout.",
 quirk="Locks bought online sometimes don't suit the door's thickness or cut-outs, which leads to latch problems later. If your lock sticks, the fit may be the issue.",
 sources=[("Xiaomi Automatic Smart Door Lock specs (Singapore)", "https://www.mi.com/sg/product/xiaomi-automatic-smart-door-lock/specs/")],
 faqs=[("How do I wake a Xiaomi smart lock with flat batteries?", "Connect a power bank to the USB-C emergency port on the front panel, then unlock with your PIN or fingerprint."),
       ("How many batteries does the Xiaomi smart door lock take?", "The Xiaomi Automatic Smart Door Lock takes eight AA batteries."),
       ("I bought a Xiaomi smart lock online. Can you install it?", "Yes. Send us a photo of the lock and your door first, so we can confirm it will fit.")]),

"Lenovo": dict(kind="smart",
 about="Lenovo smart locks are found in a growing number of Singapore homes, typically with fingerprint, PIN and app access.",
 power="Like all smart locks, Lenovo models run on battery power. Many have an emergency USB port outside to wake the lock when the battery is flat. Check your model's manual so you know which cable to carry.",
 battery="Depending on the model, Lenovo locks use AA batteries or a rechargeable battery pack. If yours is rechargeable, charge it as soon as the lock warns you.",
 key="If your Lenovo lock came with a mechanical backup key, keep it outside the home.",
 pin="Codes are managed through the keypad's admin menu or the app, depending on the model.",
 reset="A factory reset wipes all users and is done from inside only.",
 lockout="Repeated wrong attempts trigger a temporary keypad lockout.",
 quirk="If your phone app can't reach the lock, try PIN or fingerprint at the door; the app connection and the lock itself are separate.",
 sources=[],
 faqs=[("Can you open a Lenovo smart lock?", "Yes. We open all digital and smart lock brands, including Lenovo, 24/7."),
       ("My Lenovo smart lock battery died. What do I do?", "Use the emergency USB port if your model has one, or the backup key. If that doesn't work, call us.")]),

"Schlage": dict(kind="digital",
 about="Schlage, part of Allegion, sells digital locks across Asia, and models such as the S-6800 push-pull lock and the keypad-only S-480 are fitted on Singapore doors.",
 power="On the S-6800, open the cover directly below the front handle and touch a 9V battery to the terminals (either way round). You can then use your PIN, card or fingerprint. Schlage's Asia FAQ confirms a 9V battery gives one-time access with your credentials.",
 battery="The S-6800 takes eight 1.5V AA alkaline batteries; Schlage says about a year at ten entries a day. Don't use rechargeable batteries, which may leak. To check the level, touch the keypad, press 9 then #, and watch the battery lamp.",
 key="The S-6800's override keyhole is behind the same cover as the 9V terminals, and three keys come in the box. Not every Schlage lock has one: the S-480 has no mechanical key.",
 pin="On the S-6800 in normal mode, open the battery cover, press 10KEY, enter a new 6 to 12-digit PIN and press *. In safety mode, codes are changed with the manager PIN. The factory PIN is in the manual: change it on day one.",
 reset="The S-6800 reset must be done in safety mode with the batteries partly removed and the manager code, and it deletes every code, card and fingerprint. Follow the manual exactly, from inside.",
 lockout="On the S-6800, three wrong PINs suspend the lock and sound a loud alarm for 3 minutes. Pressing the manual lock button inside stops the alarm.",
 quirk="The S-6800 has a privacy switch on the inside unit (red is on, green is off). With privacy on, the door won't open from outside even with a valid PIN or card, though the mechanical key still works.",
 sources=[("Schlage S-6800 manual (Allegion Singapore)", "https://dev-cs-allegion-comsg.allegion.com/content/dam/allegion-singapore/schlage-landing-page-and-products/brochures-and-instructions/S-6800_manual_English_Jun17.pdf"),
          ("Schlage Asia FAQ", "https://dev-cs-schlagelocks-asia.allegion.com/en/help-centre/faq.html")],
 faqs=[("How do I open a Schlage digital lock with a dead battery?", "On the S-6800, open the cover under the front handle and touch a 9V battery to the terminals, then use your PIN, card or fingerprint. The override key slot is behind the same cover."),
       ("Why is my Schlage lock alarming after wrong codes?", "On the S-6800, three wrong PINs trigger a 3-minute alarm and lockout. Press the manual lock button inside to stop it, or wait it out."),
       ("What batteries does a Schlage S-6800 take?", "Eight AA alkaline batteries. Schlage advises against rechargeables.")]),

"Eufy": dict(kind="smart",
 about="Eufy, from Anker, sells smart locks with fingerprint, keypad and app control, and some models add a built-in video doorbell. Singapore owners often buy them online.",
 power="If a eufy lock dies completely and you have no key, eufy says to connect a power bank to the emergency charging port on the bottom of the lock (Micro USB on older models such as the Smart Lock Touch & Wi-Fi; newer models use USB-C).",
 battery="Depending on the model, eufy locks use AA batteries or a rechargeable battery pack. eufy says its smart locks give low-battery warnings for weeks before they lose power, so act when the warnings start.",
 key="If your eufy model has a keyway, use the key to lock and unlock when the battery is dead.",
 pin="Codes are added and removed in the eufy Security app.",
 reset="A reset removes the lock from your eufy account and deletes its users. Do it from inside, following eufy's steps for your model.",
 lockout="Repeated wrong codes trigger a temporary keypad lockout.",
 quirk="Video models use more power than keypad-only locks, so check the battery level in the app regularly.",
 sources=[("eufy: what happens if the smart lock battery dies", "https://service.eufy.com/article-description/What-happens-if-the-eufy-smart-lock-battery-dies")],
 faqs=[("What happens if my eufy smart lock battery dies?", "Use the key if your model has one. If not, connect a power bank to the emergency charging port on the bottom of the lock."),
       ("Does eufy warn before the battery dies?", "Yes. eufy says its smart locks give low-battery warnings for weeks before they lose power.")]),

"Tapo": dict(kind="smart",
 about="Tapo is TP-Link's smart home brand. Its Tapo DL100 Wi-Fi smart lock offers keypad, app, Bluetooth and voice-assistant control, and appeals to Singapore owners who already use Tapo cameras and plugs.",
 power="The DL100 has a USB-C port on the outside unit. If the batteries die, power the lock from a power bank, or from a phone that can supply power out.",
 battery="The DL100 takes four AA (LR6) batteries. TP-Link quotes up to 7 months in Wi-Fi mode and up to 10 months in Bluetooth-only mode at 20 unlocks a day.",
 key="The DL100 comes with two backup keys.",
 pin="Up to 200 keypad codes can be added, changed and removed in the Tapo app.",
 reset="The reset button is on the inside unit. Resetting removes the lock from your Tapo account, so do it from inside only.",
 lockout="Repeated wrong codes trigger a temporary keypad lockout.",
 quirk="Wi-Fi drains batteries faster. If yours run down quickly, Bluetooth-only mode lasts longer.",
 sources=[("Tapo DL100 product page (TP-Link)", "https://www.tp-link.com/in/products/details/tapo-dl100.html")],
 faqs=[("How do I open a Tapo DL100 with dead batteries?", "Connect a power bank, or a phone that supports power output, to the USB-C port on the outside unit. Or use one of the two backup keys."),
       ("How long do Tapo smart lock batteries last?", "TP-Link quotes up to 7 months in Wi-Fi mode and up to 10 months in Bluetooth-only mode at 20 unlocks a day.")]),

"Prism+": dict(kind="digital",
 about="PRISM+ is a homegrown Singapore brand best known for TVs, and its Sentinel door locks and Sentry gate locks are designed for HDB main doors and metal gates, pairing door and gate through its DuoSync feature.",
 power="The Sentinel runs on a rechargeable battery that you charge over USB-C. Keep it charged, as the physical key is the backup if it ever runs flat.",
 battery="PRISM+ lists the Sentinel's battery as a rechargeable, replaceable 5,000 mAh Li-ion battery, good for up to about 2,500 unlocks or up to 6 months on standby depending on use.",
 key="Both the Sentinel and Sentinel Pro include a physical key, and so do the Sentry gate locks.",
 pin="Codes, fingerprints, cards and stickers are managed through the keypad menu and the PRISM+ app.",
 reset="A reset deletes all users and is done from inside only, following PRISM+'s instructions.",
 lockout="Repeated wrong attempts trigger a temporary keypad lockout.",
 quirk="Door and gate locks pair with each other but have their own batteries. Charge both, not just the one that warns you.",
 sources=[("PRISM+ Sentinel series (official)", "https://prismplus.sg/products/prism-sentinel-series"),
          ("Shopee: best digital door locks Singapore (PRISM+ USB-C charging)", "https://shopee.sg/blog/best-digital-door-locks-singapore/")],
 faqs=[("How do I charge a PRISM+ digital lock?", "The Sentinel's rechargeable Li-ion battery charges over USB-C. Charge it when the lock warns you, and keep the physical key as a backup."),
       ("How long does a PRISM+ Sentinel battery last?", "PRISM+ says up to about 2,500 unlocks or up to 6 months on standby, depending on use.")]),

"Ezviz": dict(kind="smart",
 about="EZVIZ, known for home cameras, makes smart locks such as the DL50FVS that combine a lock, a security camera and a video doorbell, with face ID, fingerprint, PIN and app unlocking.",
 power="The DL50FVS has a USB-C emergency charging port: if the battery dies, connect a power bank to wake the lock and unlock it.",
 battery="The DL50FVS uses a 5,000 mAh rechargeable lithium battery. EZVIZ quotes up to about four months between charges with typical face-ID and video use.",
 key="The DL50FVS has a mechanical emergency key.",
 pin="Passcodes and temporary visitor codes are managed in the EZVIZ app.",
 reset="A reset removes the lock from your EZVIZ account and deletes users. Do it from inside only.",
 lockout="Repeated wrong attempts trigger a temporary keypad lockout.",
 quirk="Camera and radar features use power. If the battery drains fast, check the motion and video settings in the app.",
 sources=[("EZVIZ DL50FVS datasheet", "https://mfs.ezvizlife.com/DL50FVS_Datasheet (5085).pdf")],
 faqs=[("How do I open an EZVIZ smart lock with a dead battery?", "Connect a power bank to the USB-C emergency port to wake it, or use the mechanical key."),
       ("How long does the EZVIZ DL50FVS battery last?", "EZVIZ quotes up to about four months between charges, depending on face-ID and video use.")]),

"Lockly": dict(kind="smart",
 about="Lockly smart locks, such as the Secure Pro, are known for their PIN Genie keypad, which scrambles the digits every time so nobody can guess your code from fingerprints on the screen.",
 power="If the batteries die completely, hold a 9V battery against the contact points on the 9V backup socket at the bottom of the outside unit until the door unlocks. The lock detects polarity automatically. Replace the main batteries straight after.",
 battery="The Secure Pro takes four AA alkaline batteries, lasting up to a year. When they're low, a battery icon lights up; it can still run up to 300 cycles in low-battery mode.",
 key="Two physical keys come in the box. Turn the cover on the outside handle to reveal the keyhole.",
 pin="Codes are added and deleted in Programming Mode (battery cover off, press the Program button), or in the Lockly app once paired. A code is changed by deleting the old one and adding a new one.",
 reset="The Reset button is on the inside back panel, next to the Program button. Have the Activation Code card ready. A reset deletes all stored data.",
 lockout="Three wrong codes within 5 minutes put the lock into Safe Mode: the keypad locks for 10 minutes, then 20, then 30. Enter the correct code twice, use a fingerprint, the app or the key to clear it.",
 quirk="With PIN Genie on, the digits move every time. Look for your digit on any button and press it; you don't press a fixed position.",
 sources=[("Lockly Secure Pro user manual", "https://www.seam.co/img/device-db/lockly/manuals/lockly_secure-pro_latch-smart-lock_user-manual.pdf")],
 faqs=[("How do I open a Lockly lock with a dead battery?", "Hold a 9V battery to the backup contacts at the bottom of the outside unit until it unlocks, or use a physical key."),
       ("Why is my Lockly keypad locked for 10 minutes?", "Three wrong codes within 5 minutes trigger Safe Mode. The lockout grows to 20 and 30 minutes with further failed attempts."),
       ("How do I reset a Lockly lock?", "From inside, press the Reset button next to the Program button on the back panel, with your Activation Code card ready. All data is deleted.")]),

"Yew": dict(kind="digital",
 about="Yew digital locks are sold in Singapore as door and gate sets, such as the F11 door lock with the U4 Pro gate lock, with face recognition, fingerprint, PIN, card and Wi-Fi app access.",
 power="The F11 has a USB-C emergency port: connect a power bank if the battery runs flat, then unlock as normal.",
 battery="The F11 runs on a rechargeable battery pack. Charge it as soon as the lock warns you.",
 key="Yew door locks include mechanical emergency keys. Keep one outside the home.",
 pin="Codes are managed through the keypad's admin menu or the app. Use the manual for your model number.",
 reset="A reset deletes all users and is done from inside only.",
 lockout="Repeated wrong attempts trigger a temporary keypad lockout.",
 quirk="With a door and gate set, each lock has its own battery. Charge both on the same day.",
 sources=[("Shopee: best digital door locks Singapore (Yew F11 + U4 Pro)", "https://shopee.sg/blog/best-digital-door-locks-singapore/")],
 faqs=[("How do I open a Yew digital lock with a flat battery?", "Connect a power bank to the USB-C emergency port, or use the mechanical emergency key."),
       ("Does a Yew digital lock use AA batteries?", "The F11 uses a rechargeable battery pack rather than AA batteries.")]),
}

TIPS = {
 "Samsung": ["Keep a 9V battery in your bag or car if your model uses 9V emergency power. It's the quickest way back in.", "Older Samsung keypads can wear out; if some buttons need a hard press, plan a replacement.", "Gate rim locks take the most weather: wipe the keypad dry after heavy rain or corridor washing.", "Register a second fingerprint or card for a family member in case yours fails."],
 "Zigbang": ["Set up the Zigbang app and a PIN, so you have two ways in.", "Replace the AA batteries as soon as the battery-dead alarm sounds.", "Keep any mechanical key outside the home.", "If the app can't connect, try the keypad before calling."],
 "Yale": ["Learn where your model's emergency power point is: 9V on models like the YDM4109, USB on some newer ones.", "Make sure everyone at home knows what the privacy (Inside Forced Lock) switch does.", "Keep the emergency key outside the home, not in a drawer inside.", "Change the factory Master Number on day one."],
 "Philips": ["Check whether your model uses Micro USB or USB-C emergency power, and keep that cable in your bag.", "Enrol two fingers per person: if one is cut or dry, the other usually still works.", "Push-pull handles take a lot of force; if the handle feels loose, get it checked before it fails.", "Fit eight batteries if your compartment allows it, for longer life."],
 "Igloohome": ["Keep a 9V battery and one physical key where you can reach them from outside.", "For rentals, set guest codes with clear start and end times, and check them before guests arrive.", "Keep your app login details somewhere you can reach from another device.", "Replace all eight AA batteries together when warned."],
 "Gateman": ["If your Gateman is more than a few years old, test the emergency power point now so you know it still works.", "A lock that opens more slowly than it used to may be close to failing: plan a replacement.", "Keep a 9V battery handy if your model uses 9V emergency power.", "Protect gate-mounted models from direct rain where possible."],
 "Kaadas": ["Carry a small power bank and the right USB cable for your model.", "Change the batteries in the gate and door locks at the same time.", "Register a second fingerprint per person in case one fails.", "Keep the mechanical key outside the home."],
 "Solity": ["Find out whether your model uses 9V or USB emergency power before you need it.", "If the latch is getting stiff, get it checked before it jams.", "Replace all eight batteries as soon as the low-battery warning sounds.", "Keep the override key (if any) outside the home."],
 "Häfele": ["Get the master PIN and app account handed over from your contractor.", "Check whether your model uses USB or battery-contact emergency power.", "Keep the backup key outside the home.", "Reset the lock and set new codes when you move in."],
 "Aqara": ["Keep a USB-C cable and power bank for emergency power.", "Don't rely on the app alone; set up PIN and fingerprint too.", "Use alkaline batteries, as Aqara recommends.", "Keep one of the two keys outside the home."],
 "Xiaomi": ["Keep a USB-C cable and power bank handy for emergency power.", "Check the lock fits your door's thickness before buying.", "Store one emergency key outside the home.", "Set up a second unlocking method in case the app or fingerprint fails."],
 "Lenovo": ["Learn where your model's emergency power port is.", "Set up PIN as well as fingerprint and app access.", "Keep any backup key outside the home.", "Replace or charge the battery at the first warning."],
 "Schlage": ["Keep a 9V battery handy: on the S-6800 the terminals are under the front handle cover.", "Explain the privacy switch to everyone at home.", "Use alkaline AA batteries, not rechargeables.", "Store one of the three keys outside the home."],
 "Eufy": ["Know whether your model's emergency port is Micro USB or USB-C, and carry that cable.", "Don't ignore the weeks of low-battery warnings.", "Keep any key outside the home.", "Check video settings if the battery drains fast."],
 "Tapo": ["Use Bluetooth-only mode if you want longer battery life.", "Keep a USB-C cable and power bank for emergencies.", "Store one of the two backup keys outside the home.", "Review your 200-code list now and then and delete old codes."],
 "Prism+": ["Charge the door and gate locks on the same day.", "Keep the physical key outside the home.", "Set up at least two ways in: PIN and fingerprint.", "Charge as soon as the low-battery warning appears."],
 "Ezviz": ["Charge the battery before it runs out; video features use power.", "Keep a USB-C cable and power bank for emergencies.", "Store the mechanical key outside the home.", "Use temporary visitor codes instead of sharing your own."],
 "Lockly": ["Keep your Activation Code card somewhere safe: you need it to reset.", "Carry a key, as Lockly recommends, in case Safe Mode kicks in.", "Keep a 9V battery handy for emergencies.", "Leave PIN Genie on for privacy."],
 "Yew": ["Charge the door and gate locks together.", "Keep a USB-C cable and power bank for emergencies.", "Store a mechanical key outside the home.", "Register more than one fingerprint per person."],
}

SCENARIO = {
"Samsung": "An elderly couple in an older HDB flat come home from a family dinner to find the Samsung gate lock completely dark. The batteries ran flat while they were out, and they don't know about the 9V emergency contacts. We get them in, then show them where the contacts are and which battery to keep in their bag.",
"Zigbang": "A family replaced their old Samsung lock with a Zigbang one and set up the app on one phone only. When that phone is left at the office, nobody else has a PIN registered. If no one can get the phone home, we open the door and they set up a PIN for everyone.",
"Yale": "Someone at home switches the Yale lock's privacy switch on before bed. The other half of the household comes home after a late shift, and the keypad refuses a code they know is right. If no one inside wakes up, we open it, and then explain how the switch works.",
"Philips": "A family back from a holiday finds their Philips push-pull lock dead after two weeks of draining batteries. Their model takes USB emergency power, but the power bank and cable are packed deep in a suitcase. If they can't find them, we open the lock and the batteries get replaced.",
"Igloohome": "A landlord set a tenant's access code to run until the end of the month. The tenant renewed, but nobody extended the code, and on the 1st it stops working. Usually the landlord can fix it in the app; when they can't be reached, we're the backup.",
"Gateman": "A Gateman lock that has served a flat for about ten years has been getting slower: the motor hums and hesitates. One evening it doesn't finish turning at all, with the owner outside. We open it, and the owner decides it's time for a new lock.",
"Kaadas": "A household with a matching Kaadas gate and door set finds the gate lock dead while the door lock still works. The two run on separate batteries, and the gate's ran out first. We get them through the gate, and they change both sets of batteries together from then on.",
"Solity": "Someone pushed hard on a Solity handle when the lock was slow to respond. Now the code is accepted and the motor runs, but the latch won't pull back. That's a mechanical fault rather than a battery one, so we open the door and talk through replacing the lock body or the whole lock.",
"Häfele": "A new condo owner moves in after a renovation and realises the contractor never handed over the Häfele master PIN or app account. Day to day the codes work, until a code needs changing. We open locks when people are locked out; for the master PIN, the contractor or Häfele is the first call.",
"Aqara": "After changing their home Wi-Fi router, a family's Aqara smart lock shows offline in the app. They've only ever used app unlocking. The lock still accepts PIN and fingerprint at the door; if those were never set up, we're the next step.",
"Xiaomi": "An owner bought a Xiaomi smart lock online and fitted it themselves. A few weeks later the latch catches on the strike plate and the door won't open from outside. We open it and check how the lock sits on the door.",
"Lenovo": "Only one person in a household set up fingerprints on the Lenovo smart lock, and the app lives on their phone. When they're overseas, the rest of the family has only the PIN, and when that's forgotten, they call us.",
"Schlage": "A teenager taps the wrong PIN three times on the family's Schlage S-6800 and the lock starts a 3-minute alarm. Nobody inside to press the stop button, and the neighbours are looking. Usually waiting it out and entering the code slowly works; when the code itself is forgotten, we're called.",
"Eufy": "A eufy owner ignores the low-battery warnings for a few weeks, then the lock dies while they're out. Their model has no keyway, and the power bank they carry has the wrong cable for the emergency port. We open the door, and they keep the right cable in their bag from then on.",
"Tapo": "A Tapo DL100 owner keeps the lock on Wi-Fi for remote access, and the batteries drain faster than expected. The lock dies one evening and both backup keys are inside. We get them in, and they switch to Bluetooth-only mode on weekdays.",
"Prism+": "A household's PRISM+ door lock is charged regularly, but the Sentry gate lock outside isn't, and it's the gate that dies first. The gate's physical key is on the key ring inside the flat. We open the gate, and they start charging both on the same day.",
"Ezviz": "An EZVIZ owner leaves motion video on high and the rechargeable battery runs flat sooner than expected. The power bank in the car has the wrong cable. We open the door, and they adjust the video settings in the app.",
"Lockly": "A guest tries the wrong code on a Lockly lock three times and Safe Mode locks the keypad for 10 minutes, then 20 after another try. The owner is overseas. If the owner can't unlock it from the app, we're called.",
"Yew": "A family charges their Yew F11 door lock but forgets the U4 Pro on the gate, and it dies late at night. The mechanical key is on the key ring inside. We open the gate, and they set a reminder to charge both together.",
}

FEATURE = {
"Samsung": "Samsung's range in Singapore spans rim gate locks and push-pull mortise main door locks, from older keypad-only models to newer ones with fingerprint and card. Some have a mechanical key and some don't, which decides your options when the batteries die.",
"Zigbang": "Zigbang carries on Samsung's digital lock range with app features: Wi-Fi remote unlocking, NFC phone keys on supported models, one-time visitor codes and access logs.",
"Yale": "Many Yale models have an Inside Forced Lock (privacy) switch that blocks outside codes, a 9V emergency terminal and a hidden emergency key. That mix is why most Yale lockouts have a simple cause.",
"Philips": "Philips EasyKey push-pull locks are popular on HDB and condo main doors. The push-pull handle takes a lot of daily force, so a loose or stiff handle is an early warning sign worth acting on.",
"Igloohome": "Igloohome is a Singapore-founded smart lock brand built around app access and time-limited codes, which makes it popular with landlords. Most lockouts we see are about code settings rather than a broken lock.",
"Gateman": "Gateman locks have been fitted in Singapore for many years, so many are now older units. Ageing motors and keypads tend to give warning signs, slower opening or buttons that need a hard press, before they fail.",
"Kaadas": "Kaadas is often sold as a matching gate-and-door set with fingerprint, PIN and card access, and takes USB emergency power. Two locks means two sets of batteries to keep an eye on.",
"Solity": "Solity is a Korean-made brand found on many Singapore HDB and condo doors. Emergency power and override options vary by model, so knowing your model number saves time when something goes wrong.",
"Häfele": "Häfele locks are often chosen and installed by renovation contractors and interior designers. That's why the most common Häfele problem isn't the lock but who holds the master PIN and app account.",
"Aqara": "Aqara smart locks are built for smart homes, with app, hub and automation features. The lock and the network are separate, so an offline app doesn't mean a dead lock.",
"Xiaomi": "Xiaomi smart locks are often bought online for their price and app features, and many are self-installed. Fit matters: door thickness and cut-outs decide whether the latch works smoothly.",
"Lenovo": "Lenovo smart locks combine fingerprint, PIN and app access. They're most reliable when every household member has their own fingerprint and PIN, not just the person who set up the app.",
"Schlage": "Schlage's S-6800 is unusual in two ways: it sounds a loud 3-minute alarm after only three wrong PINs, and it has a privacy switch that blocks every outside credential except the mechanical key.",
"Eufy": "Eufy locks are app-first and some include a video doorbell. The emergency port differs between older and newer models, so the right cable matters.",
"Tapo": "Tapo locks fit into TP-Link's smart home app with cameras and plugs, and can be controlled by voice assistants. Wi-Fi convenience costs battery life.",
"Prism+": "PRISM+ is a Singapore brand, and its locks use rechargeable Li-ion batteries rather than AA cells, with matching door and gate locks that talk to each other.",
"Ezviz": "EZVIZ's DL50FVS is a lock, camera and video doorbell in one, running on a large rechargeable battery that powers all three.",
"Lockly": "Lockly's PIN Genie keypad scrambles the digits each time, and its Safe Mode lockout gets longer with each failed attempt: 10, 20, then 30 minutes.",
"Yew": "Yew sells door and gate sets on rechargeable batteries with USB-C emergency power, so charging habits matter more than buying batteries.",
}

# Short emergency-power method per brand, used in the troubleshooting table.
EM = {
 "Samsung": "hold a 9V battery to the contacts at the bottom of the front unit",
 "Zigbang": "use the emergency power contacts on the outside, per your model's manual",
 "Yale": "pull down the front emergency cover and hold a 9V battery to the terminal",
 "Philips": "plug a 5V power bank into the emergency USB port",
 "Igloohome": "press a 9V battery against the two silver plates on the front",
 "Gateman": "hold a 9V battery to the emergency contacts on the outside",
 "Kaadas": "plug a power bank into the USB port under the outside keypad",
 "Solity": "hold a 9V battery to the emergency port on the outside",
 "Häfele": "use the USB port or battery contacts on the outside",
 "Aqara": "plug a power bank into the USB-C port on the keypad",
 "Xiaomi": "plug a power bank into the USB-C port on the front panel",
 "Lenovo": "plug a power bank into the emergency USB port",
 "Schlage": "open the cover under the front handle and touch a 9V battery to the terminals",
 "Eufy": "plug a power bank into the charging port on the bottom of the lock",
 "Tapo": "power it from a power bank through the USB-C port outside",
 "Prism+": "use the physical key, then recharge the battery over USB-C",
 "Ezviz": "plug a power bank into the USB-C emergency port",
 "Lockly": "hold a 9V battery to the backup contacts at the bottom of the outside unit",
 "Yew": "plug a power bank into the USB-C emergency port",
}


import unicodedata as _u, re as _re
def _slug(n):
    return _re.sub(r'[^a-z0-9]+', '-', _u.normalize('NFKD', n).encode('ascii', 'ignore').decode().lower()).strip('-')

BRANDS = [dict(name=b, slug=_slug(b), tips=TIPS.get(b, []), **DATA[b]) for b in C.BRAND_PAGES if b in DATA]


def _fit(*options, limit=60):
    for o in options:
        if len(o) <= limit:
            return o
    return options[-1][:limit]


def _titles(n, kind):
    K = "Digital Lock" if kind == "digital" else "Smart Lock"
    title = _fit(f"{n} {K} Battery Flat, Password & Reset Help | 24/7",
                 f"{n} {K} Battery Flat, Password & Reset Help",
                 f"{n} {K}: Battery Flat, Reset & Lockouts")
    h1 = f"{n} {K} Battery Flat, Forgot Password or Won't Open?"
    desc = _fit(f"{n} {K.lower()} battery flat, forgot the password or won't open? How to use emergency power, change batteries and reset it, plus 24/7 help in Singapore.",
                f"{n} {K.lower()} battery flat or won't open? Emergency power, battery replacement, password change and reset, plus 24/7 help in Singapore.",
                limit=160)
    return K, title, h1, desc


def build(x):
    C_ = x["C"]
    for b in BRANDS:
        n = b["name"]
        K, title, h1, desc = _titles(n, b["kind"])
        k = K.lower()
        path = f"digital-lock-opening/{b['slug']}/"
        crumbs = [("Home", ""), ("Services", "services/"), ("Digital lock opening", "digital-lock-opening/"), (n, path)]
        faqs = b["faqs"] + [
            (f"How do I change the password on a {n} {k}?", _strip(b["pin"])),
            (f"How much does it cost to open a {n} {k}?", "It depends on the model and what's wrong. We confirm the price before we come: WhatsApp a photo of the lock (front and inside if possible) to {PHONE}."),
            (f"Do you repair {n} {k}s?", f"No, we don't do repairs. We open the lock, and if it's faulty we can replace it. For warranty repairs, contact {n} or your retailer."),
        ]
        jobs = getattr(C_, "BRAND_JOBS", {}).get(n, [])
        recent = "".join(f'<div class="callout"><p><strong>Recent job:</strong> {j}</p></div>' for j in jobs)
        i = [o["slug"] for o in BRANDS].index(b["slug"])
        near = [o for o in BRANDS[i + 1:] + BRANDS[:i] if o["kind"] == b["kind"]][:4] + [o for o in BRANDS[i + 1:] + BRANDS[:i] if o["kind"] != b["kind"]][:1]
        others = " · ".join(f'<a href="~/digital-lock-opening/{o["slug"]}/">{o["name"]}</a>' for o in near)
        src = ""
        if b["sources"]:
            src = ('<p class="note"><strong>Sources:</strong> ' +
                   " · ".join(f'<a href="{u}" target="_blank" rel="noopener">{t}</a>' for t, u in b["sources"]) +
                   ". Checked October 2026. Features vary by model: always check your lock's own manual.</p>")
        e = EM.get(n, "use your lock's emergency power point")
        table = f'''<table class="price-table info-table"><thead><tr><th scope="col">Your {n} lock</th><th scope="col">Likely cause</th><th scope="col">What to do</th></tr></thead><tbody>
<tr><td>Keypad completely dark</td><td>Batteries flat</td><td>From outside, {e}. Then replace the batteries from inside.</td></tr>
<tr><td>Accepts the code but the latch won't turn</td><td>Weak batteries, or a mechanical fault in the lock body</td><td>Try emergency power once. Don't force the handle: that's how lock bodies break.</td></tr>
<tr><td>Refuses a code you know is right</td><td>Privacy mode set from inside, or the wrong-code lockout</td><td>{_first(b["lockout"])}</td></tr>
<tr><td>App shows offline or can't connect</td><td>Wi-Fi, hub or Bluetooth</td><td>Use the keypad or fingerprint at the door: the {n} lock works without the app.</td></tr>
</tbody></table>'''
        body = (x["page_hero"](crumbs, h1,
                f"Battery flat, forgotten password, dead keypad or locked out after too many wrong tries: what to do with your {n} lock, step by step, and how Uncle Thomas can open it, damage-free wherever possible.",
                ["Since 1998", "24/7 islandwide", "Damage-free first"]) +
                f'''<section class="section"><div class="container narrow prose">
<p><strong>The short answer:</strong> {_strip(b["power"])} If that doesn't work, call or WhatsApp {{PHONE}}, any time.</p>
<h2>{n} {k}s in Singapore</h2>
<p>{b["about"]}</p>
{recent}
<h2>{n} {k} battery flat? How to open it from outside</h2>
<p>{b["power"]}</p>
<p>{b["key"]}</p>
<h2>{n} {k} battery replacement</h2>
<p>{b["battery"]}</p>
<h2>How to change the password on a {n} {k}</h2>
<p>{b["pin"]}</p>
<h2>How to reset a {n} {k}</h2>
<p>{b["reset"]}</p>
<p>{b["lockout"]}</p>
<h2>{n} {k} not working? Common problems</h2>
{table}
<p>{b["quirk"]}</p>
<h2>A typical {n} call</h2>
<p>This is the kind of {n} call we often get: {SCENARIO.get(n, "")}</p>
<h2>What's different about {n} locks</h2>
<p>{FEATURE.get(n, "")}</p>
<h2>Tips for {n} owners</h2>
<ul>{"".join(f"<li>{tip}</li>" for tip in b["tips"])}</ul>
<h2>Still locked out?</h2>
<p>Call or WhatsApp {{PHONE}}, 24/7. We open {n} locks damage-free wherever possible, confirm the price first and check ID before opening. A failed {n} lock can be <a href="~/digital-lock-installation/">replaced</a>. Independent, not affiliated with {n}. See also: <a href="~/guides/digital-lock-battery-dead/">digital lock battery dead</a> · <a href="~/guides/forgot-digital-lock-pin/">forgot your PIN</a>.</p>
{src}
<p>Related brands: {others} · <a href="~/digital-lock-opening/">all digital and smart lock brands</a></p>
</div></section>
<section class="section section-alt"><div class="container narrow">{x["faq_html"](faqs, f"{n} {K} FAQs")}</div></section>''' +
                x["cta_band"](f"Locked Out by Your {n} Lock?"))
        svc = {"@type": "Service", "@id": C_.SITE + "/" + path + "#service",
               "name": f"{n} digital lock and smart lock opening — Singapore", "serviceType": "Digital lock and smart lock opening",
               "description": desc, "provider": {"@id": x["BUSINESS_ID"]},
               "areaServed": {"@type": "Country", "name": "Singapore"}, "url": C_.SITE + "/" + path}
        nodes = x["page_schema"](path, title, desc, crumbs, faqs=faqs, extra=[svc])
        x["render"](path, title, desc, body, nodes, priority="0.7")


def _first(s):
    return _strip(s).split(". ")[0].rstrip(".") + "."


def _strip(s):
    return _re.sub(r"<[^>]+>", "", s)
