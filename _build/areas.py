"""
Areas hub + individual town pages.

Each town has its own local text — estates, landmarks, MRT, the kinds of
buildings and locks found there, common jobs and practical access tips — so
pages are genuinely useful, not copy-paste "doorway" pages. Shared text is
kept short on purpose.

Add a town by appending to TOWNS. Add real recent jobs in config.RECENT_JOBS.
"""
import config as C

TOWNS = [
# ======================= CENTRAL =======================
dict(slug="toa-payoh", name="Toa Payoh", region="Central",
 intro="Toa Payoh is one of Singapore's oldest HDB towns, so many homes still have original main door and gate locks — and older locks are the ones most likely to jam, wear out or snap a key.",
 overview="Toa Payoh was among the first new towns built by HDB, and it shows: alongside the newer Bidadari estates you'll find decades-old blocks around Toa Payoh Central and the Lorongs, where the same family may have used the same lock for thirty years. We're called here for everything from stiff old mortise locks to brand-new digital locks, plus workshops and small businesses in the Lorong 8 industrial area.",
 estates=["Toa Payoh Central", "Lorong 1–8", "Kim Keat", "Boon Teck", "Bidadari", "Braddell", "Caldecott"],
 landmarks=["HDB Hub", "Toa Payoh Town Park", "Toa Payoh Sports Complex", "Lorong 8 Industrial Estate"],
 mrt=["Toa Payoh", "Braddell", "Caldecott", "Woodleigh"],
 buildings=[
  ("Mature HDB blocks", "Original timber main doors with mortise locks and hook-bolt gate locks are common. After years of use and corridor washing, cylinders get stiff and keys can break off inside — we extract the broken key and replace the cylinder if it's worn."),
  ("Bidadari and newer flats", "Many owners have fitted digital locks on the main door or gate. Flat batteries and forgotten PINs are the usual reasons for a call."),
  ("Workshops and shops", "Roller shutters, padlocks and office doors in the Lorong 8 area — usually early-morning lockouts before opening time."),
 ],
 jobs=["Worn HDB main door locks that jam or won't turn", "Broken key stuck in the gate lock", "Digital lock upgrades in older flats", "Toilet and bedroom doors locked from inside"],
 access="Tell us your block number and which lift lobby you're nearest — some older Toa Payoh blocks have several stacks and lift lobbies. If you're waiting downstairs, the void deck of your block is the easiest meeting point.",
 faqs=[
  ("My old HDB gate lock in Toa Payoh is stuck. Can you open it?", "Yes. Older hook-bolt and gate padlocks are among the most common jobs we do in Toa Payoh. We open it first, then advise whether the lock should be replaced."),
  ("Do you serve Bidadari?", "Yes — Bidadari is part of Toa Payoh town and we cover it 24/7, along with Braddell, Caldecott and Kim Keat."),
 ],
 nearby=["bishan", "novena"]),

dict(slug="bishan", name="Bishan", region="Central",
 intro="Bishan mixes HDB estates, private condominiums and landed homes towards Thomson, plus workshops around Sin Ming — so jobs here range from home lockouts to commercial locks and safes.",
 overview="Bishan sits in the middle of the island, which makes it one of the easiest towns for us to reach at any hour. The HDB blocks around Bishan Central and Junction 8 are popular with families, condos line Bishan and Sin Ming, and the streets towards Upper Thomson are mostly landed homes. The Sin Ming industrial area adds workshops, car workshops and small offices to the mix.",
 estates=["Bishan Central", "Bishan North", "Bishan East", "Sin Ming", "Marymount", "Upper Thomson"],
 landmarks=["Junction 8", "Bishan-Ang Mo Kio Park", "Bishan Stadium", "Sin Ming Industrial Estate"],
 mrt=["Bishan", "Marymount", "Bright Hill", "Upper Thomson"],
 buildings=[
  ("Condominiums", "Condo main doors often have a deadbolt plus a digital lock. We coordinate with the guardhouse so we can get to your unit quickly."),
  ("Landed homes", "Main gates, side gates and back doors — often with several locks per entrance. A locked side gate can be the only way into the house."),
  ("Sin Ming workshops", "Roller shutters, cabinet locks and small business safes."),
 ],
 jobs=["Condo main door and digital lock lockouts", "Landed home gate and side door locks", "Office and workshop lock changes in Sin Ming", "Home safe opening"],
 access="For condos, please let the guardhouse know a locksmith is coming, or meet us at the drop-off point. For landed homes near Thomson, a quick message with the gate you're locked out of saves time.",
 faqs=[
  ("Can you get past my condo guardhouse in Bishan?", "We'll need you or management to let the guard know we're coming. Most condos simply ask for the unit number and your name."),
  ("Do you open safes in Bishan homes?", "Yes. Uncle Thomas is a US-trained safesmith. WhatsApp a photo of the safe for a quote."),
 ],
 nearby=["toa-payoh", "ang-mo-kio"]),

dict(slug="novena", name="Novena & Balestier", region="Central",
 intro="Novena and Balestier combine hospitals and medical suites, Balestier's shophouses and quiet condos and landed homes — so our calls here are a mix of clinic, shop and home lockouts.",
 overview="Novena is best known for its hospitals and medical centres, and the offices and clinics that come with them. Along Balestier Road, rows of shophouses hold eateries, lighting shops and family businesses, many with roller shutters and older padlocks. Behind the main roads are condominiums, walk-up apartments and landed streets around Moulmein, Whitley and Thomson.",
 estates=["Novena", "Balestier", "Moulmein", "Whitley", "Thomson Road", "Goldhill"],
 landmarks=["Novena Square", "Velocity", "United Square", "Tan Tock Seng Hospital", "Balestier shophouses"],
 mrt=["Novena", "Newton", "Toa Payoh"],
 buildings=[
  ("Clinics and medical suites", "Suite doors, cabinet locks and drug cupboard locks. We work early or after hours so clinics can open on time."),
  ("Balestier shophouses", "Roller shutters, collapsible gates and back-lane doors — older padlocks and hasps wear out and rust."),
  ("Condos and walk-ups", "Digital locks on main doors, and older cylinder locks in walk-up apartments."),
 ],
 jobs=["Clinic and office lockouts before opening hours", "Shophouse shutter padlocks cut and replaced", "Condo digital lock lockouts", "Cabinet and document safe opening"],
 access="For medical buildings, let building security know a locksmith is coming. Shophouse owners — tell us whether you're locked out at the front shutter or the back lane.",
 faqs=[
  ("Can you open our clinic before patients arrive?", "Yes — we work 24/7, so we can come early in the morning. We'll need authorisation from the clinic owner or manager."),
  ("Do you handle shophouse roller shutters on Balestier Road?", "Yes, we open locked shutters and replace worn padlocks and shutter locks."),
 ],
 nearby=["toa-payoh", "cbd-orchard"]),

dict(slug="cbd-orchard", name="CBD & Orchard", region="Central",
 intro="Offices, shops, hotels, serviced apartments and city condos — in the CBD and Orchard, most of our calls are about getting businesses and residents back in fast, often outside office hours.",
 overview="Singapore's city centre runs from Raffles Place, Tanjong Pagar and Marina Bay through Chinatown and River Valley to Orchard Road and Tanglin. During the day it's offices and retail; at night it's condos, serviced apartments and hotels. Locks here range from office glass doors and access-controlled suites to safes in shops and high-end digital locks in city apartments.",
 estates=["Raffles Place", "Tanjong Pagar", "Marina Bay", "Chinatown", "River Valley", "Robertson Quay", "Orchard", "Tanglin"],
 landmarks=["Raffles Place", "Marina Bay", "Chinatown", "Orchard Road", "Clarke Quay"],
 mrt=["Raffles Place", "Tanjong Pagar", "Downtown", "Chinatown", "Clarke Quay", "Somerset", "Orchard", "Great World"],
 buildings=[
  ("Office towers", "Office doors, glass doors and cabinet locks. Most buildings need the tenant to register us with security before we go up."),
  ("Retail and F&B", "Shop shutters, back-of-house doors and cash safes — usually before opening or after closing."),
  ("City condos and serviced apartments", "High-end digital locks and deadbolts. We'll check proof of residence or authorisation from the management."),
 ],
 jobs=["Office lockouts outside working hours", "Shop and restaurant safes that won't open", "Digital lock lockouts in city condos", "Lock changes when staff leave"],
 access="Parking in the city is limited, so tell us the building's loading bay or nearest carpark if you know it. For offices, please arrange building access with security in advance.",
 faqs=[
  ("Can you come to our CBD office at night or on weekends?", "Yes. We work 24/7, and after-hours visits mean no disruption to your business. Please arrange building access with security."),
  ("Do you open shop safes in Orchard and the CBD?", "Yes — Uncle Thomas trained in safesmithing in the United States. We'll need authorisation from the business before opening any safe."),
 ],
 nearby=["novena", "bukit-merah"]),

dict(slug="queenstown", name="Queenstown", region="Central",
 intro="Queenstown was Singapore's first satellite estate, so it mixes some of the oldest HDB blocks on the island with tall new ones at Dawson — and business parks like one-north and Science Park.",
 overview="Queenstown covers Commonwealth, Dawson, Tanglin Halt, Mei Ling and Stirling, stretching out to Alexandra and the one-north business district. Older blocks here have seen several generations of locks, while redeveloped areas such as Dawson have newer flats where digital locks are common. Offices, labs and start-ups around one-north and Science Park make up a good share of our commercial work in the area.",
 estates=["Commonwealth", "Dawson", "Tanglin Halt", "Mei Ling", "Stirling", "Alexandra", "one-north"],
 landmarks=["Queensway Shopping Centre", "Alexandra Retail Centre", "one-north", "Singapore Science Park", "Queenstown Library"],
 mrt=["Queenstown", "Commonwealth", "Buona Vista", "one-north", "Kent Ridge"],
 buildings=[
  ("Older HDB blocks", "Original-style main doors and gates where locks are often worn after decades of use — a common cause of keys snapping."),
  ("Dawson and newer flats", "Digital locks on main doors and gates; flat batteries and forgotten PINs are frequent call-outs."),
  ("Business parks", "Office and lab doors, cabinets and document safes around one-north and Science Park."),
 ],
 jobs=["Snapped keys in old HDB locks", "Digital lock lockouts in Dawson", "Office and lab lockouts at one-north", "Rental room lock changes for tenants"],
 access="Queenstown's older estates have many low blocks spread out — sending your block number and street name helps us find you fastest.",
 faqs=[
  ("Do you serve one-north and Science Park offices?", "Yes. We handle office lockouts, lock changes and safes, and can come outside working hours."),
  ("Can you replace a worn lock in an old Queenstown flat?", "Yes. We replace main door and gate locks on the spot, with our no-expiry warranty."),
 ],
 nearby=["bukit-merah", "clementi"]),

dict(slug="bukit-merah", name="Bukit Merah & Tiong Bahru", region="Central",
 intro="From Tiong Bahru's heritage flats to Redhill, Telok Blangah and HarbourFront, Bukit Merah has some of Singapore's most varied housing — and the cruise terminal on its doorstep.",
 overview="Bukit Merah stretches from the heritage walk-up flats of Tiong Bahru through Redhill, Henderson and Bukit Merah Central down to Telok Blangah and HarbourFront. It mixes old and new HDB blocks, private condos, light industrial buildings around Bukit Merah Central and Alexandra, and the shops and offices around VivoCity. With the Singapore Cruise Centre at HarbourFront nearby, ship and vessel safes are familiar ground for Uncle Thomas, who has opened safes on board ships and cruise liners.",
 estates=["Tiong Bahru", "Redhill", "Henderson", "Bukit Merah Central", "Telok Blangah", "HarbourFront"],
 landmarks=["Tiong Bahru Market", "VivoCity", "HarbourFront Centre", "Mount Faber", "Henderson Waves"],
 mrt=["Tiong Bahru", "Redhill", "Telok Blangah", "HarbourFront", "Outram Park"],
 buildings=[
  ("Tiong Bahru walk-ups", "Older pre-war and post-war flats often have timber doors with traditional locks, and some owners have added digital locks."),
  ("HDB estates", "A mix of mature and newer blocks around Redhill, Henderson and Telok Blangah."),
  ("Industrial and harbour", "Workshops, warehouses and offices — plus vessel and ship safes."),
 ],
 jobs=["Old timber door locks in Tiong Bahru", "HDB lockouts around Redhill and Henderson", "Industrial unit lock changes", "Ship and vessel safe opening"],
 access="Tiong Bahru's walk-up flats have shared staircases — tell us the block and staircase. For HarbourFront offices, please arrange building access.",
 faqs=[
  ("Do you open safes on ships at HarbourFront?", "Yes. Uncle Thomas has opened safes on board ships and cruise liners. We'll need authorisation from the vessel's owner or operator."),
  ("Can you work on old Tiong Bahru doors without damaging them?", "We use damage-free methods wherever possible, which matters for older timber doors."),
 ],
 nearby=["queenstown", "cbd-orchard"]),

dict(slug="kallang-whampoa", name="Kallang & Whampoa", region="Central",
 intro="Kallang and Whampoa mix mature HDB estates, light industrial buildings and the busy Sports Hub area — so we're called for home lockouts and business locks in equal measure.",
 overview="This part of central Singapore takes in Whampoa, Boon Keng, Bendemeer, Kallang Bahru and Geylang Bahru, down to the Kallang Basin and the Sports Hub. Mature HDB blocks sit next to industrial buildings along Kallang Bahru and Kallang Way, where workshops and small factories need reliable locks and fast help when something fails.",
 estates=["Whampoa", "Boon Keng", "Bendemeer", "Kallang Bahru", "Geylang Bahru", "Kallang Basin"],
 landmarks=["Singapore Sports Hub", "Kallang Wave Mall", "Whampoa Market", "Kallang Riverside Park"],
 mrt=["Boon Keng", "Bendemeer", "Geylang Bahru", "Kallang", "Stadium", "Lavender"],
 buildings=[
  ("Mature HDB estates", "Older main door locks and gate locks around Whampoa and Boon Keng."),
  ("Industrial buildings", "Factory units, workshops and warehouses along Kallang Bahru and Kallang Way — shutters, padlocks and office doors."),
  ("Condos near the river", "Digital locks and deadbolts in newer condos around Kallang and Bendemeer."),
 ],
 jobs=["Factory and workshop lockouts", "HDB gate locks in Whampoa", "Digital lock lockouts in riverside condos", "Lock changes when staff leave"],
 access="Industrial buildings often have several entrances and loading bays — tell us the unit number and which side to come to.",
 faqs=[
  ("Can you open our factory unit in Kallang Bahru?", "Yes. We handle shutters, padlocks and office doors in industrial buildings, 24/7."),
  ("Do you cover Whampoa and Boon Keng?", "Yes, along with Bendemeer, Geylang Bahru and the rest of Kallang."),
 ],
 nearby=["geylang", "novena"]),

dict(slug="geylang", name="Geylang & Paya Lebar", region="Central",
 intro="Geylang and Paya Lebar are a mix of shophouses, walk-up apartments, HDB estates and the new Paya Lebar office district — busy day and night, and so are our call-outs here.",
 overview="Along Geylang Road and Sims Avenue, shophouses hold restaurants, shops and small businesses, often with walk-up apartments above. Around Aljunied, Eunos and MacPherson are HDB estates, while Paya Lebar Quarter and the area around Paya Lebar MRT have become a commercial hub with offices and retail. Geylang Serai, with its market and festive bazaars, is a landmark for the whole east.",
 estates=["Geylang Road", "Sims Avenue", "Aljunied", "Eunos", "MacPherson", "Paya Lebar", "Geylang Serai"],
 landmarks=["Paya Lebar Quarter", "Geylang Serai Market", "SingPost Centre", "Wisma Geylang Serai"],
 mrt=["Paya Lebar", "Aljunied", "Eunos", "Dakota", "MacPherson", "Mattar"],
 buildings=[
  ("Shophouses", "Front shutters, collapsible gates, back doors and upstairs apartment doors — older locks and padlocks are common."),
  ("Walk-up apartments", "Older timber doors and cylinder locks on shared staircases."),
  ("Offices at Paya Lebar", "Office suites, cabinets and safes."),
 ],
 jobs=["Shophouse shutter lockouts", "Walk-up apartment door lockouts", "HDB lockouts in Aljunied and Eunos", "Office lock changes at Paya Lebar"],
 access="Geylang's lorongs are numbered — tell us the lorong and the nearest cross street to save time.",
 faqs=[
  ("Do you open shophouse shutters in Geylang?", "Yes. We open locked shutters and gates and replace worn padlocks and locks."),
  ("Do you serve the Paya Lebar offices?", "Yes, including after-hours lockouts and lock changes."),
 ],
 nearby=["kallang-whampoa", "marine-parade"]),

dict(slug="marine-parade", name="Marine Parade & Katong", region="Central",
 intro="Marine Parade and Katong combine the classic HDB estate on reclaimed land, Peranakan shophouses in Katong and Joo Chiat, and condos stretching along East Coast Park.",
 overview="Marine Parade's HDB estate was built on reclaimed land in the 1970s, and many flats still have older main doors and gates. Inland, Katong and Joo Chiat are known for colourful shophouses and terrace houses, while Amber Road, Meyer Road and Marine Parade Road are lined with condominiums. The Thomson-East Coast Line has made the area easier to reach than ever.",
 estates=["Marine Parade", "Katong", "Joo Chiat", "Amber Road", "Meyer Road", "Tanjong Katong", "Mountbatten"],
 landmarks=["Parkway Parade", "East Coast Park", "i12 Katong", "Joo Chiat Road"],
 mrt=["Marine Parade", "Marine Terrace", "Katong Park", "Tanjong Katong", "Dakota", "Mountbatten"],
 buildings=[
  ("1970s HDB blocks", "Older timber main doors and gates where locks get stiff with sea air and age."),
  ("Shophouses and terraces", "Traditional timber doors and gates in Katong and Joo Chiat — we use damage-free methods to protect heritage doors."),
  ("Seafront condos", "Digital locks, deadbolts and guarded access along Amber Road and East Coast."),
 ],
 jobs=["Stiff or rusted locks in older Marine Parade flats", "Condo digital lock lockouts", "Terrace house gate locks", "Shop lockouts in Katong"],
 access="Condos along the coast usually need the guardhouse to be informed. For Katong terraces, tell us whether you're locked out at the gate or the front door.",
 faqs=[
  ("Does sea air affect locks in Marine Parade?", "It can. Salty, humid air speeds up rust in older locks and gates — a stiff lock is worth replacing before it fails."),
  ("Do you work on heritage shophouse doors in Katong?", "Yes, and we use damage-free methods wherever possible to protect old timber doors."),
 ],
 nearby=["geylang", "bedok"]),

# ======================= EAST =======================
dict(slug="tampines", name="Tampines", region="East",
 intro="Tampines is one of Singapore's biggest towns — from mature estates around Tampines Central to brand-new BTO flats in Tampines North — so we see the full range of locks here.",
 overview="Tampines is a regional centre with its own malls, offices and community hub, surrounded by large HDB estates in Tampines North, East, West and Central, plus condos near Simei. Newer BTO projects in Tampines North mean a lot of digital locks, while older blocks still have traditional mortise locks and gate hook bolts. Offices around the regional centre and Changi Business Park add commercial work.",
 estates=["Tampines Central", "Tampines North", "Tampines East", "Tampines West", "Simei"],
 landmarks=["Our Tampines Hub", "Tampines Mall", "Century Square", "Tampines Eco Green"],
 mrt=["Tampines", "Tampines East", "Tampines West", "Simei", "Upper Changi"],
 buildings=[
  ("New BTO estates", "Tampines North flats where many owners fit digital locks soon after key collection."),
  ("Mature HDB blocks", "Original mortise locks and gate hook bolts that wear over time."),
  ("Offices and business parks", "Office doors, cabinets and safes around the regional centre."),
 ],
 jobs=["HDB main door and gate lockouts", "Digital lock installation in new Tampines North flats", "Office lockouts in the regional centre", "Car lockouts at mall carparks"],
 access="Tampines has many similar-looking blocks — the street number (e.g. Tampines Street 81) plus block number gets us there fastest.",
 faqs=[
  ("Can you install a digital lock in my new Tampines North BTO?", "Yes. We'll check your door and recommend a lock that fits, then install it with our no-expiry warranty."),
  ("Do you do car lockouts at Tampines malls?", "Yes. Tell us the carpark and level, and your car model."),
 ],
 nearby=["pasir-ris", "bedok"]),

dict(slug="bedok", name="Bedok", region="East",
 intro="Bedok has a bit of everything — mature HDB estates, private condos, landed homes around Siglap, and industrial units in Kaki Bukit — so our work here covers homes, cars and businesses.",
 overview="Bedok is one of the east's most established towns, with HDB estates in Bedok North, Bedok South, Bedok Reservoir and Chai Chee. Landed homes in Siglap, Frankel and Opera Estate bring gates and multi-lock doors, while Kaki Bukit's industrial estate has warehouses and factories. East Coast Park is minutes away, which also means car lockouts at its carparks.",
 estates=["Bedok North", "Bedok South", "Bedok Reservoir", "Chai Chee", "Kaki Bukit", "Siglap", "Frankel", "Opera Estate"],
 landmarks=["Bedok Mall", "Bedok Reservoir Park", "East Coast Park", "Kaki Bukit Industrial Estate"],
 mrt=["Bedok", "Tanah Merah", "Kembangan", "Bedok North", "Bedok Reservoir", "Kaki Bukit", "Sungei Bedok"],
 buildings=[
  ("Landed homes", "Main gates, side gates and doors with several locks in Siglap, Frankel and Opera Estate."),
  ("Industrial units", "Warehouses and factories in Kaki Bukit — shutters, padlocks and office doors."),
  ("HDB estates", "Older and newer blocks across Bedok North and South."),
 ],
 jobs=["Landed home gate and door locks", "Warehouse and factory lock changes in Kaki Bukit", "HDB lockouts at night", "Car lockouts at East Coast Park"],
 access="For East Coast Park car lockouts, tell us the carpark letter (e.g. Carpark C) — it's the quickest way to find you.",
 faqs=[
  ("Keys locked in my car at East Coast Park — can you help?", "Yes. Send us the carpark number and your car model and we'll come with non-destructive tools."),
  ("Do you serve landed homes in Siglap and Opera Estate?", "Yes — gates, doors and side entrances."),
 ],
 nearby=["tampines", "marine-parade"]),

dict(slug="pasir-ris", name="Pasir Ris", region="East",
 intro="Pasir Ris is a family town by the sea — HDB estates, landed homes near Loyang, and holiday chalets and resorts by the beach — and lockouts happen in all of them.",
 overview="Pasir Ris is known for its beach park, resorts and holiday chalets, which bring a steady stream of families and gatherings. Most residents live in HDB estates around Pasir Ris Drives and Elias, with private and landed homes towards Loyang and Pasir Ris Park. Loyang's industrial estate adds factories and offices that need commercial lock work.",
 estates=["Pasir Ris Central", "Pasir Ris Drives", "Elias", "Loyang", "Pasir Ris West", "Pasir Ris Park"],
 landmarks=["Pasir Ris Park", "White Sands", "Downtown East", "Loyang Industrial Estate"],
 mrt=["Pasir Ris", "Tampines East"],
 buildings=[
  ("HDB estates", "A mix of older blocks and newer flats around the town centre and Elias."),
  ("Chalets and holiday stays", "Chalet doors, safes and lockers — holiday lockouts are common at weekends and school holidays."),
  ("Loyang industrial", "Factory and warehouse locks, shutters and office doors."),
 ],
 jobs=["Lockouts at chalets and holiday stays", "HDB main door lockouts", "Room safes that won't open", "Factory lock changes in Loyang"],
 access="For chalets, tell us the chalet name and unit, and let the front desk know we're coming. For HDB flats, the block and Drive number is enough.",
 faqs=[
  ("Locked out of a chalet in Pasir Ris — can you help?", "Yes. We'll check your booking details with you and the operator before opening the door."),
  ("Do you open room safes?", "Yes — Uncle Thomas is a US-trained safesmith. We'll confirm the safe is yours or that the operator authorises it."),
 ],
 nearby=["tampines"]),

# ======================= NORTH-EAST =======================
dict(slug="ang-mo-kio", name="Ang Mo Kio", region="North-East",
 intro="Ang Mo Kio is a large, mature estate where long-time residents and young families live side by side — so we see everything from decades-old mechanical locks to brand-new digital locks.",
 overview="Ang Mo Kio is one of Singapore's largest and most established towns, with HDB blocks along the Avenues and around AMK Hub, Teck Ghee, Cheng San and Kebun Baru. Private homes cluster near Yio Chu Kang, Mayflower and Lentor, where new condos have brought plenty of digital locks. The Ang Mo Kio industrial parks also bring factory and workshop jobs.",
 estates=["Ang Mo Kio Central", "AMK Avenues 1–10", "Teck Ghee", "Cheng San", "Kebun Baru", "Yio Chu Kang", "Mayflower", "Lentor"],
 landmarks=["AMK Hub", "Bishan-Ang Mo Kio Park", "Ang Mo Kio Town Garden", "Ang Mo Kio Industrial Park"],
 mrt=["Ang Mo Kio", "Yio Chu Kang", "Mayflower", "Lentor", "Bright Hill"],
 buildings=[
  ("Mature HDB blocks", "Original main door locks and gate hook bolts — often stiff after decades of use."),
  ("New condos at Lentor", "Modern digital locks; flat batteries and forgotten PINs are the usual calls."),
  ("Industrial parks", "Factory and workshop doors, shutters and cabinets."),
 ],
 jobs=["Elderly residents locked out after the door swung shut", "Digital lock batteries going flat", "Letterbox lock replacements", "Main door lock changes after moving in"],
 access="Ang Mo Kio's Avenues are long — the Avenue number plus block number helps us find you quickly, day or night.",
 faqs=[
  ("My elderly parent is locked out in Ang Mo Kio. Can you come quickly?", "Yes. Call us — we set off immediately. If anyone inside may be unwell, call 995 first."),
  ("Do you serve the new Lentor condos?", "Yes, including digital lock lockouts and installations."),
 ],
 nearby=["bishan", "yishun"]),

dict(slug="serangoon", name="Serangoon", region="North-East",
 intro="Serangoon combines busy HDB estates around Serangoon Central with the landed homes of Serangoon Gardens — two very different kinds of locks, both of which Uncle Thomas handles every week.",
 overview="Serangoon Central is built around NEX and the MRT interchange, with HDB estates in Serangoon North and along Upper Serangoon Road. Serangoon Gardens is a well-known landed estate with its own market and food centre, and condos line Lorong Chuan. It's a town where the same afternoon might bring an HDB lockout and a landed-home gate job.",
 estates=["Serangoon Central", "Serangoon North", "Serangoon Gardens", "Lorong Chuan", "Upper Serangoon"],
 landmarks=["NEX", "Serangoon Garden Market", "Chomp Chomp Food Centre", "Serangoon Stadium"],
 mrt=["Serangoon", "Lorong Chuan", "Kovan"],
 buildings=[
  ("Landed homes", "Main gates, side gates and front doors, often with several locks."),
  ("HDB estates", "Older and mid-age blocks around Serangoon North and Central."),
  ("Condos", "Digital locks and deadbolts along Lorong Chuan."),
 ],
 jobs=["Landed home main gate and door lockouts", "Digital lock installation on condo doors", "HDB gate lock replacements", "Car lockouts at NEX"],
 access="For Serangoon Gardens, the street name is enough. For NEX car lockouts, tell us the carpark level and lot.",
 faqs=[
  ("Can you open a locked main gate in Serangoon Gardens?", "Yes. We'll check proof of residence, then open the gate and advise if the lock needs replacing."),
  ("Do you do car lockouts at NEX?", "Yes — tell us the level and lot number."),
 ],
 nearby=["hougang", "ang-mo-kio"]),

dict(slug="hougang", name="Hougang", region="North-East",
 intro="Hougang is a mature, family-heavy town where many flats have been home to the same family for decades — with newer blocks and shophouses around Kovan and Buangkok.",
 overview="Hougang stretches from Kovan and Upper Serangoon Road through Hougang Central to Buangkok and Punggol Park. Many families have lived here for generations, so older locks are common, while newer blocks near Buangkok have more digital locks. Shophouses and condos around Kovan add shops and private homes to our work.",
 estates=["Hougang Central", "Hougang Avenues", "Kovan", "Buangkok", "Lorong Ah Soo", "Upper Serangoon Road"],
 landmarks=["Hougang Mall", "Heartland Mall Kovan", "Punggol Park", "Hougang Stadium"],
 mrt=["Hougang", "Kovan", "Buangkok"],
 buildings=[
  ("Mature HDB blocks", "Older main door and gate locks; snapped keys and stiff cylinders are common."),
  ("Newer flats near Buangkok", "Digital locks on doors and gates."),
  ("Kovan shophouses and condos", "Shop shutters, back doors and condo digital locks."),
 ],
 jobs=["Old main door locks replaced with new locks", "Digital lock lockouts in newer flats", "Shophouse and shop lockouts near Kovan", "Children locked in bedrooms or toilets"],
 access="Hougang Avenues run long — share the Avenue and block number. For Kovan shophouses, tell us front or back lane.",
 faqs=[
  ("My child locked the bedroom door from inside in Hougang. What should I do?", "Keep talking to them calmly and call us — interior door locks are usually quick to open without damage. If there's any danger, call 995."),
  ("Do you replace old HDB main door locks?", "Yes, with quality hardware and our no-expiry warranty."),
 ],
 nearby=["serangoon", "sengkang"]),

dict(slug="sengkang", name="Sengkang", region="North-East",
 intro="Sengkang is a younger town full of families in BTO flats — and many have digital locks on the main door or gate, so flat batteries and forgotten PINs are common calls.",
 overview="Sengkang's estates — Compassvale, Rivervale, Anchorvale and Fernvale — are linked by the LRT loops around Sengkang Central. Most homes are HDB flats built from the late 1990s onwards, with condos near the river and Sengkang Central. Digital locks are especially common here, and so are the problems that come with them.",
 estates=["Compassvale", "Rivervale", "Anchorvale", "Fernvale", "Sengkang Central", "Jalan Kayu"],
 landmarks=["Compass One", "Sengkang Riverside Park", "Sengkang Sports Centre", "Sengkang General Hospital"],
 mrt=["Sengkang", "Buangkok", "Sengkang LRT (East & West loops)"],
 buildings=[
  ("BTO and HDB flats", "Digital locks on main doors and gates — the most common Sengkang call-outs."),
  ("Condos", "Digital locks and deadbolts, often with guardhouse access."),
  ("Jalan Kayu", "Shophouses and eateries with shutters and back doors."),
 ],
 jobs=["Digital lock battery flat or keypad not responding", "Digital lock installation on BTO doors and gates", "Kids locked in rooms", "Letterbox lock replacements"],
 access="Tell us your LRT station or block number — Sengkang's estates are spread across East and West loops.",
 faqs=[
  ("My digital lock died in Sengkang. Can you open it without breaking it?", "In most cases, yes. Uncle Thomas has his own damage-free methods for digital locks of all brands."),
  ("Do you install gate digital locks on BTO flats?", "Yes — we'll confirm your gate and lock are compatible first."),
 ],
 nearby=["punggol", "hougang"]),

dict(slug="punggol", name="Punggol", region="North-East",
 intro="Punggol is Singapore's newest waterfront town, with modern BTO flats and condos — and a high share of digital locks, many fitted at key collection.",
 overview="Punggol has grown around its waterway, with estates at Waterway, Northshore, Sumang and Matilda, condos along the water, and the new Punggol Digital District bringing offices and a university campus. Most homes are new, so mechanical lock wear is rare — but digital lock problems are very common.",
 estates=["Punggol Waterway", "Northshore", "Sumang", "Matilda", "Punggol Point", "Punggol Digital District"],
 landmarks=["Waterway Point", "Punggol Waterway Park", "Coney Island", "Punggol Point Park"],
 mrt=["Punggol", "Punggol Coast", "Punggol LRT (East & West loops)"],
 buildings=[
  ("New BTO flats", "Digital locks on doors and gates — many fitted at key collection, some of them budget models."),
  ("Waterfront condos", "Smart locks with app control and guardhouse access."),
  ("Punggol Digital District", "Office suites and access-controlled doors."),
 ],
 jobs=["Digital lock lockouts and forgotten PINs", "Replacing or upgrading digital locks fitted at key collection", "Gate digital lock installation", "Office and shop locks in the Digital District"],
 access="Punggol's newest blocks can be hard to find on maps — your block number plus the nearest LRT station helps.",
 faqs=[
  ("The digital lock that came with my Punggol BTO keeps failing. Can you replace it?", "Yes. We open it if you're locked out, then recommend and install a reliable replacement with our no-expiry warranty."),
  ("Do you cover Punggol Point and Northshore?", "Yes, all of Punggol, 24/7."),
 ],
 nearby=["sengkang"]),

# ======================= NORTH =======================
dict(slug="woodlands", name="Woodlands", region="North",
 intro="Woodlands is a large northern town with mature estates around Marsiling and newer flats towards Woodlands North — and many residents who cross the Causeway at odd hours.",
 overview="Woodlands is the north's regional centre, with HDB estates in Woodlands Central, Marsiling, Admiralty and Woodlands North and South, plus industrial areas near the Causeway. Many residents work or shop across the border, so late-night returns and lost keys are part of life here.",
 estates=["Woodlands Central", "Marsiling", "Admiralty", "Woodlands North", "Woodlands South", "Woodgrove"],
 landmarks=["Causeway Point", "Woodlands Civic Centre", "Woodlands Waterfront Park", "Woodlands Checkpoint"],
 mrt=["Woodlands", "Marsiling", "Admiralty", "Woodlands North", "Woodlands South"],
 buildings=[
  ("Mature HDB estates", "Older locks around Marsiling and Woodlands Central."),
  ("Newer flats", "Digital locks in newer blocks towards Woodlands North."),
  ("Industrial units", "Factories and warehouses near the Causeway and Woodlands Avenue."),
 ],
 jobs=["Late-night lockouts after returning from Johor", "Digital lock battery and keypad problems", "HDB gate and main door lock replacement", "Industrial unit lock changes"],
 access="Woodlands is big — the Avenue/Drive name and block number help. We cover all of it, including Marsiling and Admiralty.",
 faqs=[
  ("I lost my keys in Johor and I'm back in Woodlands. Can you help tonight?", "Yes — we work 24/7. We'll check proof of residence, open the door and can replace the lock so the lost keys can't be used."),
  ("Do you serve Admiralty and Marsiling?", "Yes, all of Woodlands."),
 ],
 nearby=["sembawang", "yishun"]),

dict(slug="yishun", name="Yishun", region="North",
 intro="Yishun has grown fast, with new BTO estates alongside long-established blocks around Chong Pang and Nee Soon — a mix of digital locks and older mechanical locks.",
 overview="Yishun's town centre around Northpoint City is surrounded by HDB estates in Khatib, Chong Pang and Nee Soon, and many new BTO projects across the town. That mix means we handle both older worn locks and the digital locks that new owners fit.",
 estates=["Yishun Central", "Khatib", "Chong Pang", "Nee Soon", "Yishun Ring Road"],
 landmarks=["Northpoint City", "Yishun Park", "Yishun Pond Park", "Khoo Teck Puat Hospital"],
 mrt=["Yishun", "Khatib"],
 buildings=[
  ("New BTO estates", "Digital locks on main doors and gates."),
  ("Mature HDB blocks", "Older main door locks and gate hook bolts in Chong Pang and Nee Soon."),
  ("Shops", "Shop shutters and back doors around Yishun Central."),
 ],
 jobs=["Digital lock lockouts in new BTO flats", "Older main door locks jamming", "Letterbox lock replacements", "Bedroom and toilet doors locked from inside"],
 access="Yishun Ring Road loops around the town — share the street and block number and we'll find you.",
 faqs=[
  ("Can you change the locks in my new Yishun flat?", "Yes — main door, gate and letterbox locks, with our no-expiry warranty."),
  ("Do you serve Khatib and Chong Pang?", "Yes, all of Yishun."),
 ],
 nearby=["sembawang", "woodlands"]),

dict(slug="sembawang", name="Sembawang", region="North",
 intro="Sembawang combines newer HDB estates around Canberra and Sun Plaza with quiet landed homes and the old naval base houses near the coast.",
 overview="Sembawang's town centre at Sun Plaza is surrounded by HDB estates, with newer flats around Canberra. Towards the coast, the former naval base area has colonial-era houses and landed homes near Sembawang Park. It's a quieter corner of the north, but we cover it 24/7 just like everywhere else.",
 estates=["Sembawang Central", "Canberra", "Sembawang Drive", "Wellington", "Sembawang Park area"],
 landmarks=["Sun Plaza", "Canberra Plaza", "Sembawang Park", "Sembawang Hot Spring Park"],
 mrt=["Sembawang", "Canberra"],
 buildings=[
  ("Newer HDB flats", "Digital locks on doors and gates around Canberra."),
  ("Landed and heritage homes", "Older timber doors and gates near the coast — we use damage-free methods to protect them."),
  ("HDB estates", "Main door and gate locks around Sun Plaza."),
 ],
 jobs=["Digital lock lockouts in Canberra flats", "Landed home gate locks", "Main door lock replacements", "Car lockouts at Sembawang Park"],
 access="Near the coast, roads can be quiet and hard to find at night — a pinned location on WhatsApp is the fastest way to guide us.",
 faqs=[
  ("Do you come to Sembawang late at night?", "Yes, 24/7. Send your location on WhatsApp so we can find you quickly."),
  ("Can you open older timber doors without damage?", "We use damage-free methods wherever possible, especially on older doors."),
 ],
 nearby=["yishun", "woodlands"]),

# ======================= WEST =======================
dict(slug="jurong", name="Jurong East & Jurong West", region="West",
 intro="Jurong covers the busy Jurong Gateway district, the large HDB estates of Jurong West and Singapore's biggest industrial zone — where safes and commercial locks are a regular part of our work.",
 overview="Jurong East is home to Jurong Gateway's malls and offices and estates like Teban Gardens, Yuhua and Toh Guan. Jurong West stretches through Boon Lay, Pioneer, Hong Kah and Taman Jurong. Beyond them lie the Jurong industrial estates, with factories, warehouses and offices that need everything from padlocks to safe opening.",
 estates=["Jurong Gateway", "Teban Gardens", "Yuhua", "Toh Guan", "Boon Lay", "Pioneer", "Hong Kah", "Taman Jurong"],
 landmarks=["JEM", "Westgate", "IMM", "Jurong Point", "Jurong Lake Gardens"],
 mrt=["Jurong East", "Chinese Garden", "Lakeside", "Boon Lay", "Pioneer", "Joo Koon"],
 buildings=[
  ("HDB estates", "Large estates across Jurong West with a mix of older and newer locks."),
  ("Offices at Jurong Gateway", "Office suites, cabinets and access-controlled doors."),
  ("Industrial estates", "Factories, warehouses and safes."),
 ],
 jobs=["HDB lockouts in Jurong West", "Office lockouts around Jurong Gateway", "Factory, warehouse and safe opening in the industrial estates", "Car lockouts at mall and industrial carparks"],
 access="Jurong is spread out — share your street and block number, or the factory's address and gate number.",
 faqs=[
  ("Can you open a safe at our Jurong factory?", "Yes. We'll need authorisation from the company. WhatsApp a photo of the safe for a quote."),
  ("Do you cover Boon Lay and Pioneer?", "Yes, all of Jurong East and Jurong West."),
 ],
 nearby=["clementi", "bukit-batok"]),

dict(slug="clementi", name="Clementi", region="West",
 intro="Clementi is a mature western town full of families, students and renters — close to universities and polytechnics, with HDB estates, condos and landed homes around Sunset Way and West Coast.",
 overview="Clementi's town centre around Clementi Mall is ringed by mature HDB estates along the Clementi Avenues, with condos and landed homes towards Sunset Way, West Coast and Dover. With several universities and polytechnics nearby, many flats and rooms here are rented to students and young workers — which means plenty of lost keys, room door lockouts and lock changes between tenants.",
 estates=["Clementi Central", "Clementi Avenues", "West Coast", "Dover", "Sunset Way", "Clementi Woods"],
 landmarks=["Clementi Mall", "Clementi Woods Park", "West Coast Park", "Clementi Stadium"],
 mrt=["Clementi", "Dover"],
 buildings=[
  ("Mature HDB estates", "Older main door and gate locks along the Clementi Avenues."),
  ("Rented rooms and flats", "Room door locks and main door lock changes when tenants move in or out."),
  ("Condos and landed homes", "Digital locks, deadbolts and gates around Sunset Way and West Coast."),
 ],
 jobs=["Room door lockouts in rented flats", "Lock changes between tenants", "HDB main door lockouts", "Digital lock installation in condos"],
 access="If you're a tenant, have your tenancy agreement or a letter with your name and address ready — we need proof of residence before opening.",
 faqs=[
  ("I'm a tenant in Clementi and locked out of my room. Can you open it?", "Yes, if you can show you live there — for example your tenancy agreement. For a lock change, we'll usually need the landlord's agreement."),
  ("Do you change locks for landlords between tenants?", "Yes, main door, gate and room door locks, with our no-expiry warranty."),
 ],
 nearby=["jurong", "queenstown"]),

dict(slug="bukit-batok", name="Bukit Batok", region="West",
 intro="Bukit Batok is a green western town with HDB estates around its central area, newer flats towards Tengah, and condos and landed homes near Hillview.",
 overview="Bukit Batok's estates surround Bukit Batok Central and West Mall, with Bukit Gombak to the north and new estates on the western edge near Tengah. Private homes and condos sit around Hillview and the nature park. It's a mix of older blocks and new BTO flats, with all the lock types that come with each.",
 estates=["Bukit Batok Central", "Bukit Batok West", "Bukit Batok East", "Bukit Gombak", "Guilin", "Hillview"],
 landmarks=["West Mall", "Bukit Batok Nature Park", "Little Guilin", "Bukit Gombak Stadium"],
 mrt=["Bukit Batok", "Bukit Gombak", "Hillview"],
 buildings=[
  ("Mature HDB blocks", "Older main door locks and gate hook bolts."),
  ("New BTO flats", "Digital locks on doors and gates, especially towards the western edge."),
  ("Hillview condos and landed homes", "Digital locks, deadbolts and gate locks."),
 ],
 jobs=["HDB lockouts around Bukit Batok Central", "Digital lock problems in new flats", "Gate lock replacements", "Condo digital lock lockouts at Hillview"],
 access="Bukit Batok has hilly roads and several street names — share the street and block number, or pin your location on WhatsApp.",
 faqs=[
  ("Do you serve Bukit Gombak and Hillview?", "Yes, and the rest of Bukit Batok, 24/7."),
  ("Do you also cover Tengah?", "Yes. We cover new Tengah estates too — WhatsApp your block and we'll find you."),
 ],
 nearby=["bukit-panjang", "jurong"]),

dict(slug="bukit-panjang", name="Bukit Panjang", region="West",
 intro="Bukit Panjang is an HDB town wrapped around its own LRT loop, between nature reserves — with condos and landed homes along Upper Bukit Timah Road.",
 overview="Bukit Panjang's estates are linked by the Bukit Panjang LRT, with stops like Senja, Fajar, Pending, Petir and Segar giving their names to the neighbourhoods. Hillion Mall and Bukit Panjang Plaza form the town centre, and condos and landed homes run along Upper Bukit Timah Road towards Cashew and Hillview.",
 estates=["Bukit Panjang Ring Road", "Senja", "Fajar", "Pending", "Petir", "Segar", "Jelapang", "Cashew"],
 landmarks=["Hillion Mall", "Bukit Panjang Plaza", "Zhenghua Park", "Dairy Farm Nature Park"],
 mrt=["Bukit Panjang", "Cashew", "Bukit Panjang LRT"],
 buildings=[
  ("HDB estates", "A mix of older and newer blocks around the LRT loop."),
  ("Condos along Upper Bukit Timah", "Digital locks and deadbolts with guardhouse access."),
  ("Landed homes", "Gates and doors with multiple locks near Cashew."),
 ],
 jobs=["HDB lockouts around the LRT loop", "Condo digital lock lockouts", "Gate lock replacements", "Letterbox lock replacements"],
 access="Your nearest LRT station (e.g. Senja or Petir) plus block number is the quickest way to tell us where you are.",
 faqs=[
  ("Do you cover all the Bukit Panjang LRT estates?", "Yes — Senja, Fajar, Pending, Petir, Segar, Jelapang and the rest of Bukit Panjang."),
  ("Can you replace my digital lock in Bukit Panjang?", "Yes. We install all brands, with our no-expiry warranty."),
 ],
 nearby=["choa-chu-kang", "bukit-batok"]),

dict(slug="choa-chu-kang", name="Choa Chu Kang", region="West",
 intro="Choa Chu Kang is a north-western family town with HDB estates around Lot One and Yew Tee, served by its own LRT — and close to the new Tengah town.",
 overview="Choa Chu Kang's town centre at Lot One is surrounded by estates in Keat Hong, Teck Whye and Yew Tee, with landed homes and farms further out. Many flats were built in the 1990s, so locks are reaching the age where they start to stiffen and fail, while new estates nearby bring plenty of digital locks.",
 estates=["Choa Chu Kang Central", "Yew Tee", "Keat Hong", "Teck Whye", "Limbang"],
 landmarks=["Lot One", "Yew Tee Point", "Choa Chu Kang Park", "Choa Chu Kang Stadium"],
 mrt=["Choa Chu Kang", "Yew Tee", "Bukit Panjang LRT (Choa Chu Kang, Keat Hong, Teck Whye)"],
 buildings=[
  ("1990s HDB blocks", "Locks reaching the age where cylinders stiffen and keys snap."),
  ("Newer flats", "Digital locks on doors and gates."),
  ("Landed homes and farmland", "Gates and padlocks further out towards Lim Chu Kang."),
 ],
 jobs=["Stiff or failing main door locks", "Digital lock lockouts", "Gate padlocks cut and replaced", "Letterbox lock replacements"],
 access="Yew Tee and Keat Hong blocks are numbered by street — share your street and block number, or send a pin on WhatsApp.",
 faqs=[
  ("My main door lock in Choa Chu Kang is getting stiff. Should I replace it?", "A stiff lock often fails at the worst time. We can replace it on the spot with quality hardware and our no-expiry warranty."),
  ("Do you cover Yew Tee and Tengah?", "Yes, both — and the rest of Choa Chu Kang."),
 ],
 nearby=["bukit-panjang", "bukit-batok"]),
]

TOWN_BY_SLUG = {t["slug"]: t for t in TOWNS}

# Places covered without their own page yet (listed on the hub so every searcher sees coverage)
OTHER_TOWNS = {
 "Central": ["Bukit Timah", "Holland", "Potong Pasir"],
 "East": ["Changi", "Simei", "Loyang"],
 "West": ["Tengah", "Tuas"],
 "North": ["Admiralty", "Kranji", "Mandai"],
 "North-East": ["Seletar Hills", "Buangkok"],
}

def build(x):
    content = x["content"]
    regions = ["Central", "East", "West", "North", "North-East"]

    # ---- hub ----
    crumbs = [("Home", ""), ("Areas", "areas/")]
    title = "Locksmith Near Me Singapore | Every Town, 24/7 | Uncle Thomas"
    desc = "Need a locksmith near you? Uncle Thomas covers every town in Singapore 24/7 — Toa Payoh, Ang Mo Kio, Tampines, Jurong, Woodlands and more. Call 9224 9224."
    cards = []
    for r in regions:
        linked = "".join(f'<a href="~/areas/{t["slug"]}/">{t["name"]}</a>' for t in TOWNS if t["region"] == r)
        other = "".join(f"<span>{n}</span>" for n in OTHER_TOWNS.get(r, []))
        cards.append(f'<div class="card area-card"><h3>{r}</h3><div class="town-links">{linked}{other}</div></div>')
    body = (x["page_hero"](crumbs, "Locksmith Near Me — Every Town in Singapore",
            "Wherever you are on the island, Uncle Thomas and his team can reach you — 24 hours a day, including weekends and public holidays.",
            ["24/7 islandwide", "We set off immediately", "Since 1998"]) +
            f'''<section class="section"><div class="container"><h2 class="section-title">Areas We Serve</h2>
<p class="section-lead">Tap your town for local details. Don't see your area? We still cover it — every part of Singapore.</p>
<div class="grid g3">{"".join(cards)}</div>
<div class="prose" style="max-width:820px;margin:40px auto 0">
<h2>Why "near me" matters less for a mobile locksmith</h2>
<p>A locksmith doesn't need a shop next to you — what matters is that someone sets off the moment you call. Uncle Thomas's team works on the move across the island, so whether you're in an HDB flat in the heartlands, a condo in town or an industrial unit in the west, we come to you. Call or WhatsApp <a href="{x["C"].WA_LINK}" target="_blank" rel="noopener">{x["C"].PHONE}</a> with your location and we'll give you an honest arrival estimate and the price before we leave.</p>
</div></div></section>''' + x["cta_band"]())
    nodes = x["page_schema"]("areas/", title, desc, crumbs, page_type="CollectionPage", extra=[
        {"@type": "ItemList", "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "url": x["C"].SITE + f"/areas/{t['slug']}/", "name": "Locksmith " + t["name"]}
            for i, t in enumerate(TOWNS)]}])
    x["render"]("areas/", title, desc, body, nodes, priority="0.8")

    svc_pills = "".join(f'<li><a href="~/{s["path"]}">{s["short"]}</a></li>' for s in content.SERVICES)

    # ---- town pages ----
    for t in TOWNS:
        path = f"areas/{t['slug']}/"
        n = t["name"]
        crumbs = [("Home", ""), ("Areas", "areas/"), (n, path)]
        title = f"Locksmith {n} 24/7 | Doors, Digital Locks & Safes"
        if len(title) > 60:
            title = f"Locksmith {n} 24/7 | Uncle Thomas Locksmith"
        if len(title) > 60:
            title = f"Locksmith {n} 24/7 | Uncle Thomas"
        desc = f"24/7 locksmith in {n} — door lockouts, digital locks, safes and car lockouts. Uncle Thomas sets off as soon as you call. Since 1998. Call 9224 9224."
        if len(desc) > 158:
            desc = f"24/7 locksmith in {n}: lockouts, digital locks, safes & cars. We set off as soon as you call. Since 1998. Call 9224 9224."
        facts = (f'<div class="facts"><div class="fact"><strong>Estates we cover</strong>{", ".join(t["estates"])}</div>'
                 f'<div class="fact"><strong>Landmarks</strong>{", ".join(t["landmarks"])}</div>'
                 f'<div class="fact"><strong>MRT / LRT</strong>{", ".join(t["mrt"])}</div>'
                 f'<div class="fact"><strong>Region</strong>{t["region"]} Singapore · 24/7 coverage</div></div>')
        bld = "".join(f"<h3>{h}</h3><p>{p}</p>" for h, p in t["buildings"])
        jobs = "".join(f"<li>{j}</li>" for j in t["jobs"])
        recent = C.RECENT_JOBS.get(t["slug"], [])
        recent_html = (f'<h2>Recent jobs in {n}</h2><ul class="jobs">' + "".join(f"<li>{j}</li>" for j in recent) + "</ul>"
                       if recent else f'<!-- FILL: real recent jobs in {n} → _build/config.py RECENT_JOBS["{t["slug"]}"]. Section hidden until then. -->')
        near = [TOWN_BY_SLUG[s] for s in t["nearby"] if s in TOWN_BY_SLUG]
        near_html = " and ".join(f'<a href="~/areas/{m["slug"]}/">{m["name"]}</a>' for m in near)
        faqs = list(t["faqs"]) + ([EXTRA_FAQS[t["slug"]]] if t["slug"] in EXTRA_FAQS else []) + [
            (f"How much does a locksmith in {n} cost?", "The same as anywhere in Singapore: it depends on the lock and the time of day, and we confirm the price before we start. See our <a href=\"~/prices/\">price list</a>."),
        ]
        body = (x["page_hero"](crumbs, f"Locksmith in {n} — 24/7 Emergency Service",
                f"Locked out in {n}? {t['intro']}", ["24/7 incl. public holidays", "Since 1998", "We check ID before opening"]) +
                f'''<section class="section"><div class="container narrow prose">
<h2>Locksmith work in {n}</h2>
<p>{t["overview"]}</p>
{facts}
<h2>Locks and buildings in {n}</h2>
{bld}
<h2>Lock tips for {n} homes and businesses</h2>
<p>{LOCAL_NOTES.get(t["slug"], "")}</p>
<h2>A typical call in {n}</h2>
<p>{TYPICAL.get(t["slug"], "")}</p>
<h2>Jobs we often do in {n}</h2>
<ul>{jobs}</ul>
{recent_html}
<h2>Getting to you in {n}</h2>
<p>{t["access"]} Locked out right now? Here's <a href="~/guides/locked-out-of-hdb-flat/">what to do while you wait</a>.</p>
<h2>Services in {n}</h2>
<ul class="link-pills">{svc_pills}</ul>
{"<p>Also nearby: " + near_html + ".</p>" if near_html else ""}
</div></section>
<section class="section section-alt"><div class="container narrow">{x["faq_html"](faqs, f"{n} Locksmith FAQs")}</div></section>''' +
                x["cta_band"](f"Need a Locksmith in {n} Now?"))
        svc = {"@type": "Service", "@id": x["C"].SITE + "/" + path + "#service", "name": f"Locksmith in {n}",
               "serviceType": "Locksmith", "provider": {"@id": x["BUSINESS_ID"]},
               "areaServed": [{"@type": "Place", "name": f"{e}, Singapore"} for e in [n] + t["estates"][:5]],
               "url": x["C"].SITE + "/" + path,
               "hoursAvailable": {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], "opens": "00:00", "closes": "23:59"}}
        nodes = x["page_schema"](path, title, desc, crumbs, faqs=faqs, extra=[svc])
        x["render"](path, title, desc, body, nodes, priority="0.7")


# Town-specific advice paragraphs (rendered as "Lock tips for <town>").
LOCAL_NOTES = {
"toa-payoh": "In older Toa Payoh flats, the most common warning sign we see is a key that has to be jiggled or pulled slightly to turn. That usually means the cylinder pins are worn, and it's only a matter of time before the key snaps or the lock refuses to turn at all — often late at night. Replacing a worn cylinder costs far less than an emergency call-out with a broken key stuck inside. If your gate's hook-bolt lock has started to rust from corridor washing, a few drops of lock lubricant (not cooking oil) can help, but a rusted lock body is best replaced. Families with elderly parents living alone in Toa Payoh often ask us about digital locks so that children can let themselves in — it's a sensible upgrade for older blocks, provided the door is in good condition.",
"bishan": "Bishan homes often have more than one lock per entrance: a condo door with a deadbolt and a digital lock, or a landed home with a gate lock, a padlock and a front door lock. When you call, tell us exactly which lock is stopping you — it changes the tools we bring and the price. If you live in a condo, keep a spare card or key with a trusted neighbour or family member rather than in your car, because a car parked in the condo carpark doesn't help if the lift lobby needs a card too. For workshops in Sin Ming, we recommend replacing padlocks on shutters with closed-shackle padlocks, which are harder to cut and stand up better to the weather.",
"novena": "Clinics and medical suites in Novena often have strict rules about who can open a door or cabinet, so we'll always ask for authorisation from the clinic owner or practice manager before starting. If your clinic uses a key safe or drug cupboard, keep a record of who holds the keys, and change the lock when staff leave — it's cheaper than dealing with a missing key later. Shophouse owners along Balestier should check shutter padlocks every few months: rust on the shackle is the first sign that a padlock will seize, and a seized padlock means cutting it off. In older walk-up apartments, a door that has dropped on its hinges can put strain on the lock; if your key turns stiffly only when the door is closed, the door may need adjusting before the lock is replaced.",
"cbd-orchard": "In the city, the biggest delay in a lockout is usually building access rather than the lock itself. If you manage an office, save building security's after-hours number somewhere other than your office desk, and register a few people who are allowed to approve contractors. For shops and restaurants, keep the safe's manufacturer details and serial number on file — if the code is lost, it speeds up any manufacturer reset and helps us quote accurately. City condo and serviced-apartment residents should note that many high-end digital locks have an emergency power point and a backup key; keep the backup key somewhere outside the apartment, such as with a colleague or family member. We'll always ask for proof of residence or authorisation from management before opening a unit.",
"queenstown": "Queenstown has a high mix of rental flats and rooms near the universities and business parks, so we often help landlords change locks between tenants. If you're a landlord, changing the main door cylinder after each tenancy is a small cost compared with the risk of an old key being copied. Tenants, keep your tenancy agreement handy — we need proof that you live there before opening. In the older estates, a lot of the lockouts we see are caused by the door's latch slipping shut behind someone taking out the rubbish. If you often step out briefly, consider a lock that can be set on 'hold back' while you're in the corridor, or a digital lock with a keypad.",
"bukit-merah": "Tiong Bahru's heritage flats are much loved, and many still have timber doors that can be damaged by forced entry, so we always try damage-free methods first and explain the options before doing anything that could mark the door. In the industrial buildings around Bukit Merah Central and Alexandra, we recommend businesses keep a simple record of who holds which keys, and change locks when staff or contractors leave. For businesses with safes — including vessels — keep the safe's make, model and serial number on file, along with proof of ownership; it helps a safesmith quote accurately and work faster when you're locked out of something important.",
"kallang-whampoa": "Industrial units in Kallang Bahru and Kallang Way are often secured with a roller shutter and a padlock or two — and in Singapore's humidity, padlocks exposed to rain can seize within a few years. A seized padlock usually has to be cut, which is quick but means you'll need a new one, so we bring replacements. If your unit is in a multi-tenant industrial building, check with the management whether after-hours access needs approval before you call; it saves waiting at the gate. In Whampoa and Boon Keng's older HDB blocks, the same advice applies as in other mature estates: a stiff key is an early warning, and replacing the cylinder before it fails costs less than a lockout.",
"geylang": "Shophouses in Geylang are busy at all hours, and many have both a front shutter and a back door onto the lane. When you call, tell us which entrance you need to get through — sometimes the back door is quicker and causes less disruption to your shop. Upstairs walk-up apartments often share a staircase door as well as the unit door, so let us know if there's a shared gate we need to get past. For businesses around Paya Lebar Quarter, after-hours lockouts usually involve building security, so register your contractors in advance if you can. As always, we'll check proof of residence or authorisation before opening any door or shutter.",
"marine-parade": "Living near the sea is lovely, but salt in the air is hard on locks. In Marine Parade's older blocks and the terraces of Katong and Joo Chiat, we often see gate locks and padlocks that have corroded far faster than they would inland. If your key feels gritty or the lock needs force to turn, it's worth replacing it with a lock designed for outdoor use before it seizes. Seafront condo residents should check that their digital lock's batteries are changed regularly, since humidity and heavy use can shorten battery life. For heritage doors, we use damage-free techniques wherever possible, and we'll always talk you through the options before doing anything that could mark the door.",
"tampines": "Tampines North has thousands of new flats, and many owners install a digital lock within weeks of collecting their keys. If you're about to do the same, check your door's thickness and the existing lock cut-out before you buy — a lock that doesn't fit properly is the most common cause of later problems. In the older estates, the gate hook-bolt locks take the most wear, especially in corridors that are washed regularly. For businesses in the regional centre and Changi Business Park, keep a spare key or access card with a second person, and change locks when staff leave. Mall carpark car lockouts are common at weekends — tell us the carpark, level and lot number and we'll find you quickly.",
"bedok": "Landed homes in Siglap, Frankel and Opera Estate often have several layers of security — a main gate, a side gate, a front door and sometimes a back door, each with its own key. It's easy to lose track of which key opens what, so we suggest labelling keys discreetly (not with your address) and keeping a spare set with family. In Kaki Bukit's industrial estate, roller shutters and padlocks see heavy use; replacing worn padlocks before they seize saves an emergency call. Car lockouts near East Coast Park are among our most common Bedok jobs — keys left in the boot while unloading bicycles or picnic gear is a classic. Non-destructive car entry tools mean no broken windows.",
"pasir-ris": "Pasir Ris chalets and holiday stays get busy at weekends and during school holidays, and so do lockouts: a door swings shut while everyone is at the beach, or a room safe won't open on check-out day. If you're staying in a chalet, let the front desk or operator know if you're locked out — we'll need to confirm the booking before opening. Families in the HDB estates around Pasir Ris Drives and Elias often ask about child-proofing: interior doors with privacy locks can usually be opened from outside with the right tool, so it's worth asking us how your door's lock works before there's a problem. In Loyang's industrial estate, we handle shutters, padlocks and factory doors.",
"ang-mo-kio": "Ang Mo Kio has many elderly residents who have lived in the same flat for decades, and a door swinging shut behind them is one of the most common reasons we're called here. If an elderly family member lives alone, consider a digital lock with a PIN that trusted family members know, or keep a spare key with a neighbour. Older gate hook-bolt locks are often stiff after years of use; if it takes two hands to turn the key, it's time to replace the lock. In the newer condos around Lentor, the usual problems are digital lock batteries and forgotten PINs — change the batteries as soon as the lock warns you.",
"serangoon": "Serangoon Gardens homes tend to have heavy main gates with lock bodies that take a lot of wear from daily use and the weather. If your gate lock has started to stick or the key turns only partway, a replacement now is much cheaper than an emergency call-out later. For HDB residents in Serangoon North, gate padlocks and hook-bolt locks are the usual suspects. Condo residents along Lorong Chuan with digital locks should keep the backup key somewhere outside the unit — many people keep it inside, which doesn't help when the battery dies. Car lockouts at NEX are common on busy weekends; tell us the carpark level and lot so we can come straight to you.",
"hougang": "Hougang's long-time residents often still use the original locks their flats came with, and those locks are now reaching the end of their life. Worn keys and stiff cylinders are early warning signs. For families with young children, interior doors with push-button privacy locks are a frequent call-out: a child locks the bedroom or toilet door and can't unlock it. Most of these can be opened quickly without damage, but it helps to know how your doors' emergency release works. Around Kovan, shop owners with roller shutters should check padlocks regularly for rust, especially before the monsoon season.",
"sengkang": "Sengkang's BTO flats are packed with digital locks, so most of our calls here are about batteries, forgotten PINs and keypads that stop responding after rain. Most digital locks warn you for weeks before the batteries die — change them as soon as you hear the low-battery alert, and use good-quality batteries. If your lock has an emergency power terminal or a backup key, make sure you know where they are before you need them. Families with young children should also check whether the lock has a child-lock or privacy mode that could be switched on by accident. For older flats in Sengkang, gate locks and letterbox locks are the other common jobs.",
"punggol": "Many Punggol homeowners received digital locks at key collection or bought budget models online, and some of these are less reliable in Singapore's heat and humidity. If your lock regularly fails to read fingerprints, drains batteries quickly or jams, it may be cheaper in the long run to replace it with a better-quality model. Before buying, check that the lock suits your door's thickness and cut-out. Smart locks with app control are popular in the waterfront condos — keep the app updated and know how to use the backup key or emergency power if the phone or the lock fails. For offices in the Punggol Digital District, we handle access doors and lock changes.",
"woodlands": "Woodlands residents who travel across the Causeway often carry keys in bags that get searched, swapped or left behind, so lost keys are a common story here. If you lose keys anywhere outside your home, it's worth changing the main door cylinder afterwards, especially if anything with your address was lost at the same time. Late-night lockouts are part of our routine in Woodlands — we work 24/7 and will check proof of residence before opening. In the newer blocks towards Woodlands North, digital lock batteries and keypads are the usual problems. Industrial unit owners near the Causeway should replace padlocks before they seize in the humidity.",
"yishun": "Yishun's mix of old and new flats means our calls here are split between worn mechanical locks and new digital locks. In Chong Pang and Nee Soon's older blocks, stiff cylinders and snapped keys are common — replacing a worn lock early is cheaper than a late-night lockout. In newer BTO estates, many homeowners add a digital lock soon after moving in; if you're planning to, check that your gate and door are compatible first. Letterbox locks are another frequent job in Yishun, as letterbox keys are small and easily lost. We'll check proof of residence before opening any letterbox or door.",
"sembawang": "Sembawang is quieter than many towns, which makes it easy for us to reach at night — but roads near the coast and Sembawang Park can be hard to find in the dark, so a pinned location on WhatsApp helps. The area's older colonial-era houses and landed homes often have traditional timber doors and gates that deserve careful, damage-free handling. In the newer Canberra estates, digital locks are common, and the advice is the same as elsewhere: change batteries at the first warning and know where your backup key is. If you lose your keys, consider changing the main door cylinder, especially if anything with your address went missing too.",
"jurong": "Jurong's industrial estates mean we do more commercial work here than in most towns: factory doors, warehouse shutters, cabinets and safes. For businesses, we recommend keeping a simple key register and changing locks when staff leave — it's the cheapest security upgrade there is. If your factory has a safe, keep the make, model and serial number on file, along with proof of ownership; it helps us quote accurately. In the large HDB estates of Jurong West, the usual jobs are lockouts, worn gate locks and digital lock problems. Mall carparks at Jurong Gateway and Jurong Point see regular car lockouts — tell us the carpark and level.",
"clementi": "Because so many Clementi flats and rooms are rented, we're often asked who can authorise a lockout or a lock change. Tenants can usually get help with a lockout by showing their tenancy agreement or a letter with their name and the address. Changing the lock on a rented flat, though, normally needs the landlord's agreement, so check your tenancy agreement first. Landlords: replacing the main door cylinder between tenants is a small cost compared with the risk of old keys still being in circulation. For students in rented rooms, a small key safe or a trusted friend holding a spare key can save an expensive call-out.",
"bukit-batok": "Bukit Batok's hilly streets and spread-out estates can make addresses hard to find, especially at night — a pinned location on WhatsApp is the fastest way to guide us. In the mature estates around Bukit Batok Central and Bukit Gombak, worn gate locks and stiff main door cylinders are the usual call-outs. The newer flats on the western edge of town and in nearby Tengah have more digital locks; if you're choosing one, check that it suits your door before buying. Condo residents around Hillview should keep their digital lock's backup key somewhere outside the unit, not in a drawer inside.",
"bukit-panjang": "The Bukit Panjang LRT stations make handy landmarks — telling us you're near Senja, Petir or Fajar narrows things down quickly. Many Bukit Panjang flats are now old enough that their original locks are wearing out, so stiff keys and jammed cylinders are a common call. Families living near the nature reserves sometimes find that humidity and damp affect gate locks and padlocks more than elsewhere; a lock designed for outdoor use lasts longer. For condo residents along Upper Bukit Timah Road, the usual issues are digital lock batteries and forgotten PINs. We install and replace digital locks of all brands, with our no-expiry warranty.",
"choa-chu-kang": "Many Choa Chu Kang flats were built in the 1990s, which means their original locks have now seen decades of daily use. If your key has to be pushed, pulled or jiggled, the cylinder is worn and is likely to fail — replacing it now avoids a late-night lockout. Families in Yew Tee and Keat Hong often ask about digital locks so that children can come home without a key; if that's you, choose a lock with a mechanical backup and a low-battery warning. Further out towards the farms and landed homes, gates and padlocks are the common jobs. Send a pinned location on WhatsApp if you're somewhere hard to find.",
}

# One more town-specific question per page.
EXTRA_FAQS = {
"toa-payoh": ("Can you replace the lock on an old timber door in Toa Payoh?", "Yes. Older timber doors often have mortise locks set into the door edge. We'll fit a replacement that suits the existing cut-out where possible, so the door doesn't need extra work."),
"bishan": ("Do you serve landed homes near Upper Thomson?", "Yes. We handle main gates, side gates and front doors on landed homes in Bishan and Thomson, including homes with several locks on one entrance."),
"novena": ("Can you change locks at our Balestier shop after a staff member leaves?", "Yes. We replace shutter padlocks, door locks and cabinet locks so former staff keys no longer work, usually in a single visit."),
"cbd-orchard": ("Do you open hotel or serviced apartment doors in the city?", "We work with the property's management. They'll need to authorise us, and we'll confirm the guest or resident's identity before opening."),
"queenstown": ("Can I change the lock on a flat I'm renting in Queenstown?", "Usually only with the landlord's agreement — check your tenancy agreement. We can help with a lockout if you can show you live there."),
"bukit-merah": ("Do you work in the industrial buildings around Bukit Merah Central and Alexandra?", "Yes — shutters, padlocks, office doors, cabinets and safes, 24/7. We'll need authorisation from the business before opening."),
"kallang-whampoa": ("How fast can you reach Kallang at night?", "Kallang is central, so it's one of the quickest areas for us to reach. We set off as soon as you call and give you an honest estimate."),
"geylang": ("Can you open the upstairs apartment door above a Geylang shophouse?", "Yes. Let us know if there's a shared staircase gate as well, and have proof of residence ready."),
"marine-parade": ("Can you replace a rusted gate lock in Marine Parade?", "Yes. We replace corroded gate locks and padlocks with ones better suited to outdoor use near the sea."),
"tampines": ("Do you serve Simei and Tampines West?", "Yes — all of Tampines, including Simei, Tampines West, East, North and Central."),
"bedok": ("Can you open a warehouse shutter in Kaki Bukit?", "Yes. We open locked shutters and cut seized padlocks, then fit a new padlock so you can lock up again."),
"pasir-ris": ("Do you serve Loyang and the landed homes near Pasir Ris Park?", "Yes. We cover all of Pasir Ris, including Loyang's industrial estate and the private homes near the park."),
"ang-mo-kio": ("Can you install a digital lock for my elderly parents in Ang Mo Kio?", "Yes. We'll recommend an easy-to-use model with a mechanical backup and install it with our no-expiry warranty."),
"serangoon": ("Can you replace an old landed-home gate lock in Serangoon Gardens?", "Yes. We'll match the lock to your gate and fit it with our no-expiry warranty."),
"hougang": ("Do you serve Kovan shophouses?", "Yes. We open shutters and doors and replace worn padlocks and locks for shops around Kovan and Upper Serangoon Road."),
"sengkang": ("My digital lock's keypad stopped working after rain. What can I do?", "Let it dry and try again after a while. If it still won't respond, try the backup key or emergency power — or call us and we'll open it."),
"punggol": ("Can you install a digital lock on my Punggol BTO gate?", "Yes. We check that your gate and the lock are compatible, then install it and set it up with you."),
"woodlands": ("Do you serve the Woodlands industrial areas?", "Yes. We handle factory and warehouse locks, shutters and office doors near the Causeway and across Woodlands."),
"yishun": ("Can you replace my Yishun letterbox lock?", "Yes. After checking your proof of residence, we open the letterbox and fit a new lock with new keys."),
"sembawang": ("Do you serve Canberra?", "Yes. Canberra is part of our Sembawang coverage, and we handle the digital locks common in the newer flats there."),
"jurong": ("Do you do car lockouts at Jurong Point and JEM?", "Yes. Tell us the carpark, level and lot number, plus your car model, and we'll come with non-destructive tools."),
"clementi": ("Do you serve Dover and West Coast?", "Yes — all of Clementi, including Dover, West Coast and the condos and landed homes around Sunset Way."),
"bukit-batok": ("Can you open a stuck gate lock in Bukit Batok?", "Yes. We open it first, then advise whether the lock can stay or should be replaced."),
"bukit-panjang": ("Do you serve the condos along Upper Bukit Timah Road?", "Yes. We'll coordinate with the guardhouse to reach your unit quickly."),
"choa-chu-kang": ("Do you serve landed homes and farms beyond Choa Chu Kang?", "Yes. We cover the whole north-west, including landed homes and farmland — send a pinned location on WhatsApp."),
}

# "A typical call in <town>": a realistic, clearly *typical* situation for each town
# (never presented as a dated real job; real jobs go in config.RECENT_JOBS).
TYPICAL = {
"toa-payoh": "An auntie in a Lorong 1 block takes the rubbish to the chute in her house slippers, and the main door's old latch clicks shut behind her. Her keys are on the dining table. A neighbour lends her a phone, she WhatsApps a photo of the door, and we agree the price before we set off. The lock opens without damage, and because the key had been sticking for months, she decides to replace the worn cylinder while we're there.",
"bishan": "A family in a Bishan condo comes home from Junction 8 to find the digital lock's screen dark. The batteries have died after weeks of low-battery beeps, and the backup key is in a kitchen drawer inside. The guardhouse lets us through once the owner confirms, we power up and open the lock, and the family leaves with fresh batteries in place and the backup key moved to a relative's home.",
"novena": "A clinic manager arrives at a Novena medical suite at 7.30am, half an hour before the first patient, and the suite door's key won't turn. Building security has to sign us in, so the manager calls them first. With authorisation confirmed, we open the door without marking it, and because the cylinder is worn, we replace it on the spot so the clinic opens on time with new keys for the staff.",
"cbd-orchard": "A restaurant manager near Tanjong Pagar closes up after midnight and realises the office safe holding the day's float won't accept the code. The owner is overseas but sends written authorisation by WhatsApp. We open the safe without drilling, and the manager resets the code with the owner on a video call before locking up for the night.",
"queenstown": "A landlord in Commonwealth has a tenant moving out on Friday and a new tenant moving in on Saturday. The old tenant has returned only two of the three keys. The landlord sends us a photo of the door lock and the gate lock, and we replace both cylinders that afternoon so the new tenant gets the only working keys.",
"bukit-merah": "A Tiong Bahru resident with a much-loved timber door is locked out after the latch slips shut. They're worried about the door being damaged, so we explain the damage-free options first and agree the price. The door opens cleanly, the frame is untouched, and the resident keeps a spare key with a friend nearby from then on.",
"kallang-whampoa": "A Kallang Bahru workshop owner arrives at 6am to start a delivery, but the padlock on the roller shutter has seized after months of rain. The key turns halfway and stops. We cut the seized padlock, fit a new closed-shackle padlock suited to outdoor use, and the van is out on time.",
"geylang": "A shop owner on Sims Avenue loses the bunch of keys for both the front shutter and the back-lane door. Anyone who finds them could open the shop, so after checking the business details, we open the front shutter, then change the padlocks and the back door lock so the lost keys no longer work.",
"marine-parade": "A Marine Parade resident's gate lock has been getting stiffer for months, and tonight the key won't turn at all. Sea air has corroded the lock body. We open the gate, show the owner the rust inside the old lock, and fit a replacement better suited to the salty air near East Coast Park.",
"tampines": "A couple collects the keys to their new Tampines North BTO flat and buys a digital lock online the same week. When it arrives, they aren't sure it fits their door. They WhatsApp us photos of the door edge and the lock box, we confirm the fit, and we install it, setting up their PINs and fingerprints with them before we leave.",
"bedok": "A family unloading bicycles at the East Coast Park carpark puts the car key on the boot floor, closes the boot and hears the car lock. The bicycles are out but the key is in. They send us the carpark, lot number and car model, and we open the car with non-destructive tools so the picnic can go ahead.",
"pasir-ris": "On check-out morning at a Pasir Ris chalet, the room's small safe won't open, and the family's passports are inside for a trip the next day. The operator confirms the booking and authorises us, and we open the safe without damaging it, with time to spare before check-out.",
"ang-mo-kio": "A son gets a call from his elderly father in Ang Mo Kio: the door has swung shut and his father is waiting in the corridor. We head over, confirm the father's identity with his NRIC once inside, and open the door without damage. The family then asks about a simple digital lock so this can't happen again, and we recommend one with a mechanical backup key.",
"serangoon": "A Serangoon Gardens homeowner's heavy main gate lock finally refuses to turn after years of daily use, with the car parked inside. We open the gate, check the lock body and replace it with a sturdier gate lock, so the family can lock up properly that night.",
"hougang": "A toddler in a Hougang flat pushes the button lock on the bathroom door and can't work out how to open it. The parent is on the other side, worried. We arrive, open the privacy lock from outside in under a minute without damage, and show the parent how the emergency release works on that type of door.",
"sengkang": "A Sengkang BTO owner comes home after a heavy downpour and the gate's digital lock keypad won't respond. The family has never used the backup key and isn't sure where it is. We open the lock, check that it has dried properly, and show them where the emergency power point and key override are.",
"punggol": "A Punggol homeowner's budget digital lock keeps failing to read fingerprints and drains its batteries every few weeks. Tonight it won't open at all. We get the family inside, then recommend a more reliable model suited to their door, and install it with our no-expiry warranty.",
"woodlands": "A Woodlands resident comes back from Johor Bahru late at night and realises the house keys were left behind across the Causeway. We check proof of residence, open the main door, and because the keys are with someone else for now, the resident decides to keep the old lock and pick the keys up the next day.",
"yishun": "A Yishun resident loses the tiny letterbox key and has a bank letter waiting inside. After checking proof of residence, we open the letterbox and fit a new lock with new keys, so the old key no longer matters.",
"sembawang": "A family staying in one of Sembawang's quiet landed streets near the park gets locked out of the side gate late at night. The road is dark and hard to find, so they send a pinned location on WhatsApp. We find the house first time and open the gate without damaging the old ironwork.",
"jurong": "A factory manager in Jurong needs the office safe opened before the morning shift: the staff member with the code has left the company. With written authorisation from the director and proof of ownership, we open the safe, and the company sets a new code and changes the office door lock the same day.",
"clementi": "A student renting a room near Clementi locks the room door with the key inside. We check the tenancy agreement on their phone and confirm with the landlord, then open the door without damage. The landlord later asks us to replace the room locks between tenants.",
"bukit-batok": "A Bukit Batok resident at the top of a hilly street is locked out late at night and isn't sure how to describe the way in. A pinned location on WhatsApp brings us straight to the block. The main door opens without damage, and the resident decides to replace a worn gate lock while we're there.",
"bukit-panjang": "A Bukit Panjang family near Petir LRT station finds their gate padlock rusted solid after weeks of wet weather. The key won't go in at all. We cut it off and fit a weather-resistant padlock, then check that the gate's own lock is still in good shape.",
"choa-chu-kang": "A Yew Tee family's original 1990s main door lock has been getting harder to turn, and tonight the key snaps off in the cylinder. We open the door without damage and replace the worn cylinder, so the family has a smooth lock and new keys before bedtime.",
}
