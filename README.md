# Uncle Thomas Locksmith — Website

A fast, mobile-first, multi-page site for **Uncle Thomas Locksmith**, a 24/7 islandwide emergency locksmith in Singapore since 1998. Built for Google ranking on searches like *locksmith Singapore*, *emergency locksmith*, *locksmith near me*, *digital lock opening* and *safe opening Singapore*.

## ⚠️ How to edit (important — read this first, including Kiro)

The `.html` pages are **generated**. Don't edit them directly — your changes will be overwritten.

1. Edit the source files in `_build/`:
   | File | What's in it |
   |---|---|
   | `_build/config.py` | Phone, email, UEN, domain, **prices**, reviews, photos, recent jobs, GA4 ID, title style, brand pages |
   | `_build/content.py` | Homepage, service pages, prices page, About page text |
   | `_build/areas.py` | Areas hub + 25 town pages (add a town by adding an entry to `TOWNS`) |
   | `_build/brands.py` | Digital lock brand pages |
   | `_build/guides_a.py`, `guides_b.py`, `guides_extra.py` | Guide articles |
   | `_build/zh.py` | Chinese pages |
   | `_build/styles.css` | The design (colours, layout) — inlined into every page |
2. Run: `python3 _build/build.py`
3. Commit and push. GitHub Pages publishes automatically.

Folders starting with `_` are not published by GitHub Pages, so `_build/` stays private-ish (it's still visible in the repo).

## 📄 Pages (55)

- **Home** `/` — targets *locksmith Singapore*, *24 hour locksmith*
- **Services** `/services/` + 8 service pages: emergency lockout, digital lock opening, digital lock installation, safe opening, car lockout, lock replacement, letterbox lock, commercial locksmith
- **Prices** `/prices/`
- **Digital lock brands** `/digital-lock-opening/<brand>/` — Samsung, Yale, Philips, Igloohome, Gateman
- **Areas** `/areas/` + 25 town pages
- **Guides** `/guides/` + 9 guides
- **Chinese** `/zh/` and `/zh/emergency-locksmith/`
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

Everything below lives in `_build/config.py` (search for `FILL`). Empty settings are **hidden** on the live site, so customers never see placeholders.

- [ ] `EMAIL` — business email (none shown until set)
- [ ] `GOOGLE_MAPS_URL` — full Google Maps link (the short share link is used until then)
- [ ] `UEN` — ACRA UEN (footer + schema)
- [ ] `GA4_ID` — Google Analytics ID (analytics off until set; add a privacy note when you switch it on)
- [ ] `REVIEWS` — up to 3 real Google reviews (reviews section hidden until then)
- [ ] `PHOTOS` — real photos in `assets/photos/` (12 slots: hero, About ×3, each service page)
- [ ] `RECENT_JOBS` — real recent jobs per town (section hidden until then)
- [ ] `PRICES` — confirm Uncle Thomas honours every "from" price; confirm payment methods
- [ ] `BRAND_PAGES` — confirm the brands Uncle Thomas handles
- [ ] `LANGUAGES` — add Chinese/Malay etc. if spoken
- [ ] Guides: check every `<!-- FILL: verify -->` legal/regulatory statement (search the `_build/guides_*.py` files)
- [ ] Chinese pages: native speaker review (`_build/zh.py`)

Performance note: `_headers` sets cache rules for Netlify / Cloudflare Pages. GitHub Pages ignores it.

## 🌐 Live domain: singapore-locksmiths.com (Cloudflare Pages)

The site is hosted on **Cloudflare Pages** (project `singapore-locksmiths`, test URL https://singapore-locksmiths.pages.dev). Domain registered at Namecheap; nameservers point to Cloudflare.

- **Publishing:** every push to `main` runs `.github/workflows/deploy.yml`, which uploads the site to Cloudflare Pages (it leaves out `_build/`, `.kiro/`, `.github/` and this README). It needs the repo secrets `CLOUDFLARE_API_TOKEN` and `CLOUDFLARE_ACCOUNT_ID`. The committed HTML is published as-is, so always run `python3 _build/build.py` before pushing.
- `SITE` in `_build/config.py` is `https://singapore-locksmiths.com` (no www). `www.` redirects to it via a Cloudflare redirect rule.
- `_headers` sets caching (Cloudflare reads it).
- Google Search Console: verify the domain, submit `https://singapore-locksmiths.com/sitemap.xml`.
- Put the website link on the Google Business Profile.
- The old GitHub Pages copy (jezvier.github.io/uncle-thomas-locksmith) can be switched off in repo Settings → Pages once Cloudflare is live.

## 🚀 Preview locally

```
python3 _build/build.py
python3 -m http.server 8080
```
Open http://localhost:8080
