"""
Outside sources for the guides, shown as a "Sources:" note after each guide and as the Article's
schema `citation`. Added 17 Nov 2026 (an external audit found 20 of 30 guides cited none).

GUIDE_SOURCES[slug] = [(label, url), ...]

Rules: official or primary sources only (Singapore government and statutory boards, standards bodies,
the maker's own manual or support page). No blogs, forums, marketplaces, manual-copy sites or other
locksmiths. Every URL is opened and checked to support the guide's claim before it goes in. Never link
a document that prints factory default codes.
"""

_SCDF_995 = ("SCDF: emergency medical services (call 995)", "https://www.scdf.gov.sg/home/about-scdf/emergency-medical-services")
_HDB_WORKS = ("HDB renovation guidelines: building works (doors and gates)", "https://www.hdb.gov.sg/managing-my-home/renovation-and-maintenance/renovation/renovation-guidelines/building-works")
_MND_FIRE_DOOR = ("MND: fire-rated entrance doors for HDB flats (written answer, 2017)", "https://www.mnd.gov.sg/newsroom/parliament-matters/q-as/view/written-answer-by-ministry-of-national-development-on-fire-rated-entrance-door-for-hdb-flats")
_SCDF_DDL = ("SCDF: digital locksets on fire-rated doors", "https://www.scdf.gov.sg/fire-safety-services-listing/permits-and-certifications/digital-locksets-on-fire-rated-doors")
_PHILIPS = ("Philips EasyKey Alpha user manual", "https://www.documents.philips.com/assets/20230823/5ecb017a31234c5c83bfb06700df2cf8.pdf")
_LTA = ("LTA: vehicle log cards are no longer issued on paper", "https://vrl.lta.gov.sg/lta/vrl/html/genInfo/aa/LTA_main04.html")
_SAVTA = ("SAVTA: about the Safe & Vault Technicians Association", "https://www.savta.org/about.html")
_ALOA = ("ALOA: history", "https://www.aloa.org/history")
_SG_LOCKS = ("Sargent & Greenleaf: mechanical safe lock guide", "https://ftp.sargentandgreenleaf.com/pdf/book_mech_locks.pdf")
_PHOENIX_FAQ = ("Phoenix Safe: FAQs", "https://phoenixsafe.co.uk/faqs/")
_YALE_FIRE = ("Yale Fire Safe FAQ", "https://yalehome.co.uk/support/product-support/safes/fire-safes/faq/")
_HONEYWELL_5100 = ("Honeywell 5100 series digital safe manual", "https://cdn.shopify.com/s/files/1/0569/0969/3080/files/M5103S-5107S_5103-5108_5112DOJ_5112-5113_5103GS-5107GS_5103G-5108G_5112G-DOJ_5112G-5113G_E_V2_R1_D0.pdf")

GUIDE_SOURCES = {
    # Home, HDB and doors
    "locked-out-of-hdb-flat": [_SCDF_995, _HDB_WORKS, _MND_FIRE_DOOR],
    "change-locks-new-home": [_SCDF_DDL, _HDB_WORKS],
    "lost-house-key": [("Singapore Police Force: lodge a police report online", "https://www.police.gov.sg/e-services/lodge-police-report")],
    "main-door-lock-types": [_HDB_WORKS, _SCDF_DDL],
    "room-door-locked-from-inside": [
        ("MHA: SCDF powers to force entry to save lives (2019)", "https://www.mha.gov.sg/media-room/newsroom/commencement-of-civil-defence-and-other-matters-amendment-act/"),
        _SCDF_995,
        ("Schlage: privacy levers and the outside emergency release", "https://www.schlage.com/en/home/products/levers/bed-and-bath-door-levers.html")],
    "door-lock-jammed": [_MND_FIRE_DOOR],
    # Digital locks, cars and cost
    "digital-lock-battery-dead": [
        ("Samsung SDS smart door lock catalogue (9V backup)", "https://image.samsungsds.com/global/en/support/resources/__icsFiles/afieldfile/2019/03/27/DoorLock_Cata_ENG_32p_190102-Final.pdf"),
        ("Yale Singapore: YDR50GA gate lock (9V emergency power)", "https://www.yalehome.com/sg/en/products/smart-door-locks/metal-gate-smart-locks/ydr50ga"),
        _PHILIPS],
    "digital-lock-repair": [
        ("Yale YDD724A user manual: warranty exclusions", "https://www.yalehome.com/my/en/product-assets/smart-lock/yale-access-app-smart-lock/ydd724a/assets/documents/user-manual/Yale%20YDD724A%20User%20Manual.pdf"),
        _SCDF_DDL],
    "forgot-digital-lock-pin": [("igloohome: permanent PINs", "https://support.igloohome.co/support/solutions/articles/35000183358-permanent-pins"), _PHILIPS],
    "smart-lock-for-hdb-gate": [_HDB_WORKS],
    "car-key-fob-not-working": [
        ("Panasonic CR2025 specifications", "https://energy.panasonic.com/ap/business/products/lithium/coin-cr-standard/models/CR2025"),
        ("Panasonic CR2032 specifications", "https://energy.panasonic.com/ap/business/products/lithium/coin-cr-standard/models/CR2032"),
        ("Toyota owner's manual: if the electronic key does not operate properly", "https://www.toyota.com/content/dam/toyotaowners/digital-owners-manual-v2/en/om02688u/chapter/ch07se020409.html")],
    "lost-car-key-fob": [_LTA],
    "locksmith-cost-singapore": [
        ("CASE: submit a complaint", "https://www.case.org.sg/submit-a-complaint/"),
        ("Singapore Courts: file a small claim", "https://www.judiciary.gov.sg/civil/file-small-claim")],
    # Safes
    "forgot-safe-combination": [_SAVTA, _ALOA, _PHOENIX_FAQ, _YALE_FIRE],
    "how-to-choose-a-safe-locksmith": [_SAVTA, _ALOA, _SG_LOCKS],
    "lost-safe-key": [("SentrySafe: replacement keys (identity verification)", "https://replacements-ca.sentrysafe.com/products/lost-key"), _PHOENIX_FAQ],
    "safe-box-battery-dead": [
        _YALE_FIRE,
        ("SentrySafe X125 manual", "https://cdn.masterlock.com/sentrysafe/resources/pdf/manuals/7000-0885.pdf"),
        ("Godrej: what to do if the batteries are weak or dead", "https://www.godrejenterprises.com/support/locks-and-security/home-security/common-problems/what-can-i-do-if-the-batteries-are-weak-or-dead"),
        ("Burg-Wächter: safe FAQs", "https://burg.biz/en/pages/faqs-safes")],
    "safe-drilling-explained": [_SG_LOCKS],
    "safe-wont-open-correct-code": [
        _HONEYWELL_5100,
        ("Honeywell 2605 fire safe manual", "https://cdn.shopify.com/s/files/1/0569/0969/3080/files/M2605_2607_2609_E_V3_R0_D4.pdf")],
}
