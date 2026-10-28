"""Tell Bing (and other IndexNow engines, which feed ChatGPT search and Copilot) about
changed pages right after a deploy. Submits pages whose content changed today
(per _build/lastmod.json), or every page with --all. Never fails the deploy."""
import json, os, sys, urllib.request
from datetime import date

KEY = "eb37cd71ff868ba077b9f23ed60997c6"   # public by design; the same value is served at /eb37cd71ff868ba077b9f23ed60997c6.txt
SITE = "https://singapore-locksmiths.com"
HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    lm = json.load(open(os.path.join(HERE, "lastmod.json")))
    today = date.today().isoformat()
    paths = list(lm) if "--all" in sys.argv else [p for p, v in lm.items() if v.get("date") == today]
    urls = [SITE + "/" + ("" if p == "/" else p) for p in paths]
    if not urls:
        print("IndexNow: nothing changed today"); return
    body = json.dumps({"host": "singapore-locksmiths.com", "key": KEY,
                       "keyLocation": f"{SITE}/{KEY}.txt", "urlList": urls[:10000]}).encode()
    req = urllib.request.Request("https://api.indexnow.org/indexnow", data=body, method="POST",
                                 headers={"Content-Type": "application/json; charset=utf-8"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            print("IndexNow:", r.status, "for", len(urls), "URLs")
    except Exception as e:
        print("IndexNow skipped:", e)


if __name__ == "__main__":
    main()
