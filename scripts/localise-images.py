#!/usr/bin/env python3
"""Download every image hotlinked from static.wixstatic.com into /assets/img
and rewrite the HTML to use the local copies. Run once from the repo root:

    python3 scripts/localise-images.py

Then commit the assets/ folder and the updated HTML files. After that the
site no longer depends on the Wix account staying active.
"""
import glob, hashlib, os, re, urllib.request

OUT = "assets/img"
os.makedirs(OUT, exist_ok=True)
pattern = re.compile(r'https://static\.wixstatic\.com/media/[^"\'\s)]+')
files = glob.glob("*.html") + glob.glob("*.css")
urls = sorted({u for f in files for u in pattern.findall(open(f, encoding="utf-8").read())})
print(f"Found {len(urls)} Wix image URLs in {len(files)} files")

mapping, failed = {}, []
for url in urls:
    ext = ".png" if ".png" in url.lower() else ".jpg"
    name = hashlib.sha1(url.encode()).hexdigest()[:12] + ext
    dest = os.path.join(OUT, name)
    if not os.path.exists(dest):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=30) as r, open(dest, "wb") as fh:
                fh.write(r.read())
        except Exception as e:
            failed.append((url, e)); continue
    mapping[url] = "/" + dest.replace(os.sep, "/")

for f in files:
    s = open(f, encoding="utf-8").read()
    new = s
    for url, local in mapping.items():
        new = new.replace(url, local)
    new = new.replace('<link rel="preconnect" href="https://static.wixstatic.com" crossorigin>\n', "")
    if new != s:
        open(f, "w", encoding="utf-8").write(new)
        print("updated", f)

print(f"\nDone: {len(mapping)} images saved to {OUT}/")
for url, e in failed:
    print("FAILED:", url, "->", e)
