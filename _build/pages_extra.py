"""
Contact page and privacy notice (added 27 Oct 2026).

The privacy notice is a plain-English PDPA-style notice. FILL: the owner should
confirm what records are actually kept (and for how long) and add a business
email for data requests once one exists.
"""
import config as C
import icons


def build(x):
    _contact(x)
    _privacy(x)


def _contact(x):
    path = "contact/"
    title = "Contact Uncle Thomas Locksmith | Call or WhatsApp 9224 9224"
    desc = ("Contact Uncle Thomas Locksmith, 24/7 islandwide Singapore. Call or WhatsApp 9224 9224 for lockouts, "
            "digital and smart locks, safes, cars and lock changes.")
    crumbs = [("Home", ""), ("Contact", path)]
    email_row = (f'<li>{icons.svg("mailbox", cls="bi")} <span><strong>Email:</strong> <a href="mailto:{C.EMAIL}">{C.EMAIL}</a> '
                 f'(for non-urgent questions)</span></li>') if C.EMAIL else ""
    uen = f"{C.LEGAL_NAME} (UEN {C.UEN}), registered in Singapore since {C.FOUNDED}" if C.UEN else f"Since {C.FOUNDED}"
    body = (x["page_hero"](crumbs, "Contact Uncle Thomas Locksmith",
            "The fastest way to reach us is a call or a WhatsApp message, 24 hours a day, including weekends and public holidays.",
            ["24/7", "Islandwide", "Price confirmed first"]) +
            f'''<section class="section"><div class="container narrow prose">
<h2>Call or WhatsApp</h2>
<ul class="contact-big">
<li>{icons.svg("phone", cls="bi")} <span><strong>Phone (24/7):</strong> <a href="tel:{C.PHONE_E164}" data-pos="contact">{C.PHONE}</a></span></li>
<li>{icons.svg("chat", cls="bi")} <span><strong>WhatsApp:</strong> <a href="{C.WA_LINK}" target="_blank" rel="noopener" data-pos="contact">{C.PHONE}</a></span></li>
{email_row}
<li>{icons.svg("star", cls="bi bi-star", fill=True)} <span><strong>Google:</strong> <a href="{C.GOOGLE_PROFILE}" target="_blank" rel="noopener">our Google Business Profile and reviews</a></span></li>
<li>{icons.svg("star", cls="bi bi-star", fill=True)} <span><strong>Had a job done with us?</strong> <a href="{C.GOOGLE_REVIEW_URL}" target="_blank" rel="noopener">Leave Uncle Thomas a Google review</a>. It takes a minute and helps other families find us.</span></li>
</ul>

<h2>Quick quote form</h2>
<p>Not urgent, or prefer to type? Pick what you need and we'll reply on WhatsApp with a price.</p>
{x["quote_form"]("contact")}

<h2>What to send on WhatsApp</h2>
<p>A quick message with these details lets us give you a price and set off sooner:</p>
<ol>
<li><strong>Where you are:</strong> block and street, or the carpark and level.</li>
<li><strong>What's locked:</strong> main door, gate, room, digital or smart lock, safe, car, or letterbox.</li>
<li><strong>A photo of the lock</strong> (front, and the inside edge for doors). For cars, the make, model and year, and a photo of the key if you need a spare.</li>
<li><strong>Is anyone at risk?</strong> A child, elderly person or someone unwell inside: tell us straight away, and call 995 if there's any danger.</li>
</ol>

<h2>Where we work</h2>
<p>Islandwide, 24 hours a day. Most jobs are around Toa Payoh and Ang Mo Kio, but we cover every town, from <a href="~/areas/woodlands/">Woodlands</a> to <a href="~/areas/tampines/">Tampines</a> and <a href="~/areas/jurong/">Jurong</a>. We come to you; there's no walk-in shop. See <a href="~/areas/">all areas</a>.</p>

<h2>Before we open anything</h2>
<p>We check proof of residence or ownership before opening any door, car or safe, for example your NRIC with your address, a tenancy agreement or the vehicle log card. It protects you and your home.</p>

<h2>Business details</h2>
<p>{uen}. Trading as {C.NAME}.</p>
</div></section>''' + x["cta_band"]())
    nodes = x["page_schema"](path, title, desc, crumbs, page_type="ContactPage")
    x["render"](path, title, desc, body, nodes, priority="0.6")


def _privacy(x):
    path = "privacy/"
    title = "Privacy Notice | Uncle Thomas Locksmith"
    desc = "How Uncle Thomas Locksmith collects, uses and protects your personal data when you call, message or use this website."
    crumbs = [("Home", ""), ("Privacy", path)]
    contact = f'<a href="mailto:{C.EMAIL}">{C.EMAIL}</a> or ' if C.EMAIL else ""
    analytics = ("<p>This website uses Google Analytics to understand which pages are useful. It uses cookies and collects "
                 "anonymous usage information such as pages visited and the type of device. You can block cookies in your browser.</p>"
                 if C.GA4_ID else
                 "<p>This website does not use advertising cookies. If we add website analytics, we'll update this notice.</p>")
    body = (x["page_hero"](crumbs, "Privacy Notice", f"How {C.NAME} handles your personal data. Last updated {{MONTH_YEAR}}.") +
            f'''<section class="section"><div class="container narrow prose">
<h2>What we collect</h2>
<p>When you call, WhatsApp or book a job, we collect only what we need to help you: your name, phone number, the address or location of the job, photos you choose to send, and details of the lock, safe or car.</p>
<p>Before every job we check your ID (NRIC, Singpass or other ID proof) and proof of residence or ownership, such as your NRIC with your address, a tenancy agreement, a utility bill or a vehicle log card.</p>

<h2>Why we use it</h2>
<ul>
<li>To quote, travel to you and do the job.</li>
<li>To confirm you live at the address or own the car or safe, so no one can use a locksmith to get into someone else's property.</li>
<li>To honour our warranty on lock replacements and installations.</li>
<li>To reply to your messages and, if you agree, ask for a review afterwards.</li>
</ul>

<h2>Who we share it with</h2>
<p>We don't sell your personal data. We share it only where the law requires it, for example with the police on request, or with service providers we rely on to run the business, such as our phone and messaging apps.</p>

<h2>How long we keep it</h2>
<p>The only records we keep are the invoice for the job and our WhatsApp messages with you about it. We keep them for our warranty and our legal and accounting obligations, and no longer than we need to.</p>

<h2>This website</h2>
{analytics}

<h2>Your rights</h2>
<p>Under Singapore's Personal Data Protection Act (PDPA), you can ask what personal data we hold about you, ask us to correct it, or withdraw consent for how we use it. Email <a href="mailto:thomaslocksmith@hotmail.com">thomaslocksmith@hotmail.com</a> or call {C.PHONE}.</p>
</div></section>''')
    nodes = x["page_schema"](path, title, desc, crumbs)
    x["render"](path, title, desc, body, nodes, priority="0.2")
