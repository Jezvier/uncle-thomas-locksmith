# Uncle Thomas Locksmith — Website

A fast, mobile-first, multi-page site for **Uncle Thomas Locksmith**, a 24/7 islandwide emergency locksmith in Singapore since 1998. Built for Google ranking on searches like *locksmith Singapore*, *emergency locksmith*, *locksmith near me*, *digital lock opening* and *safe opening Singapore*.

## ⚠️ How to edit (important — read this first, including Kiro)

The `.html` pages are **generated**. Don't edit them directly — your changes will be overwritten.

1. Edit the source files in `_build/`:
   | File | What's in it |
   |---|---|
   | `_build/config.py` | Phone, email, domain, **prices**, digital lock brands, Google profile link |
   | `_build/content.py` | Homepage, service pages, prices page, About page text |
   | `_build/areas.py` | Areas hub + town pages (add a town by adding an entry to `TOWNS`) |
   | `_build/guides.py` | Guide articles |
   | `_build/styles.css` | The design (colours, layout) |
2. Run: `python3 _build/build.py`
3. Commit and push. GitHub Pages publishes automatically.

Folders starting with `_` are not published by GitHub Pages, so `_build/` stays private-ish (it's still visible in the repo).

## 📄 Pages (30)

- **Home** `/` — targets *locksmith Singapore*, *24 hour locksmith*
- **Services** `/services/` + 8 service pages: emergency lockout, digital lock opening, digital lock installation, safe opening, car lockout, lock replacement, letterbox lock, commercial locksmith
- **Prices** `/prices/`
- **Areas** `/areas/` + 12 town pages (Toa Payoh, Ang Mo Kio, Bishan, Serangoon, Hougang, Sengkang, Punggol, Tampines, Bedok, Jurong, Woodlands, Yishun)
- **Guides** `/guides/` + 4 guides
- **About** `/about/`
- `404.html`, `sitemap.xml`, `robots.txt`, `llms.txt`, `site.webmanifest`

## ✅ SEO built in

- Unique title + description on every page (≤60 / ≤160 chars), one H1 each
- Structured data (JSON-LD) on every page: Locksmith business, Service, OfferCatalog with prices, FAQPage, BreadcrumbList, Article (guides), Person (Uncle Thomas)
- Internal linking: every service ↔ prices ↔ areas ↔ guides, footer links
- Self-hosted fonts, WebP images, no render-blocking third parties → Lighthouse 97–100
- Accessibility 100 (contrast, landmarks, skip link, labelled menu)
- Mobile: sticky Call / WhatsApp bar, call + WhatsApp buttons in the first screen of every page

## 🔑 Facts the site states (keep these true)

24/7 islandwide · since 1998 · Uncle Thomas leads a small team · US-trained safesmith · ID/proof of residence checked before opening · warranty on every lock replacement and installation with no expiry · all digital lock brands · **no** key duplication or lock repair.

## 📝 Still to do (owner)

- [ ] **Confirm prices** in `_build/config.py` → `PRICES` (Uncle Thomas must honour every "from" price)
- [ ] **Add 3–6 real Google reviews** to the homepage (search `OWNER TO FILL` in `_build/content.py`)
- [ ] **Add a real photo of Uncle Thomas** (About page — search `OWNER TO FILL`)
- [ ] Confirm spoken languages (`LANGUAGES` in config) and payment methods
- [ ] Add Facebook / Carousell / directory links to `SAME_AS` in config as you create them

## 🌐 Going live on thomaslocksmith.sg

1. Buy the domain.
2. In `_build/config.py` set `BASE_PATH = "/"` (SITE is already `https://thomaslocksmith.sg`).
3. Add a file named `CNAME` in the repo root containing `thomaslocksmith.sg`, rebuild, push.
4. GitHub → repo Settings → Pages → Custom domain → `thomaslocksmith.sg`, add the DNS records it shows, tick **Enforce HTTPS**.
5. Google Search Console: verify the domain, submit `https://thomaslocksmith.sg/sitemap.xml`.
6. Put the website link on the Google Business Profile.

## 🚀 Preview locally

```
python3 _build/build.py
python3 -m http.server 8080
```
Open http://localhost:8080
