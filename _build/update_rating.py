"""
Fetch the business's current Google rating + review count and save them to
_build/rating.json (read by config.py). Run daily by .github/workflows/update-rating.yml.

Needs env PLACES_API_KEY (Google Maps Platform key with "Places API (New)" enabled).
Optional env PLACE_ID; if missing, the place is found by text search and matched
on the Maps CID below. Exits 0 without changes if anything is missing, so the
site never breaks because of this job.
"""
import json, os, sys, urllib.request, urllib.parse

CID = "4145225534861484330"          # from https://maps.google.com/?cid=...
QUERY = "Singapore Locksmith 238 Lorong 1 Toa Payoh Singapore"
OUT = os.path.join(os.path.dirname(__file__), "rating.json")


def call(url, key, fields, body=None):
    req = urllib.request.Request(url, data=json.dumps(body).encode() if body else None,
                                 method="POST" if body else "GET")
    req.add_header("X-Goog-Api-Key", key)
    req.add_header("X-Goog-FieldMask", fields)
    req.add_header("Content-Type", "application/json")
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def main():
    key = os.environ.get("PLACES_API_KEY")
    if not key:
        print("No PLACES_API_KEY set; skipping."); return
    # Google Place ID for the business (not a secret; found on the first run, 27 Oct 2026)
    pid = os.environ.get("PLACE_ID") or "ChIJW1IOQGYX2jERKiFMX6nMhjk"
    try:
        if pid:
            p = call(f"https://places.googleapis.com/v1/places/{pid}", key, "id,rating,userRatingCount")
        else:
            res = call("https://places.googleapis.com/v1/places:searchText", key,
                       "places.id,places.googleMapsUri,places.rating,places.userRatingCount",
                       {"textQuery": QUERY, "regionCode": "SG"})
            places = res.get("places", [])
            p = next((x for x in places if CID in x.get("googleMapsUri", "")), None)
            if not p:
                print("Business not found by search; set PLACE_ID secret."); return
            print("Place ID (save as PLACE_ID secret):", p["id"])
    except Exception as e:
        print("Google request failed:", e); return
    rating, count = p.get("rating"), p.get("userRatingCount")
    if not rating or not count:
        print("No rating returned; leaving as is."); return
    new = {"rating": round(float(rating), 1), "count": int(count)}
    old = json.load(open(OUT)) if os.path.exists(OUT) else {}
    if {k: old.get(k) for k in new} == new:
        print("Rating unchanged:", new); return
    json.dump(new, open(OUT, "w"))
    print("Rating updated:", old, "->", new)


if __name__ == "__main__":
    main()
