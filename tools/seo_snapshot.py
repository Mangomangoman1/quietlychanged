#!/usr/bin/env python3
"""Snapshot the SEO-relevant parts of every built page in docs/ (URL, title, description,
canonical, OG tags, JSON-LD) so a rebuild can be compared against it.
  python3 tools/seo_snapshot.py > before.json
  python3 tools/seo_snapshot.py --compare before.json   # exits 1 if a page disappeared
"""
import json, pathlib, re, sys, html
D = pathlib.Path(__file__).resolve().parent.parent / "docs"
def grab(t, pat):
    m = re.search(pat, t, re.S); return html.unescape(m.group(1)) if m else None
def snap():
    out = {}
    for f in sorted(D.rglob("*.html")):
        t = f.read_text()
        out[str(f.relative_to(D))] = {
            "title": grab(t, r"<title>(.*?)</title>"),
            "desc": grab(t, r'<meta name="description" content="(.*?)">'),
            "canonical": grab(t, r'<link rel="canonical" href="(.*?)">'),
            "og_title": grab(t, r'<meta property="og:title" content="(.*?)">'),
            "og_type": grab(t, r'<meta property="og:type" content="(.*?)">'),
            "ld": sorted(json.dumps(json.loads(x), sort_keys=True) for x in re.findall(r'<script type="application/ld\+json">(.*?)</script>', t, re.S)),
        }
    return out
if __name__ == "__main__":
    if len(sys.argv) > 2 and sys.argv[1] == "--compare":
        old = json.loads(pathlib.Path(sys.argv[2]).read_text()); new = snap()
        gone = [p for p in old if p not in new]
        strict = "--strict" in sys.argv
        changed = [(p, k) for p in old if p in new for k in old[p] if k != "ld" and old[p][k] != new[p][k]]
        ldchg = [p for p in old if p in new and old[p]["ld"] != new[p]["ld"]]
        for p in gone: print("MISSING PAGE:", p)
        for p, k in changed: print(f"CHANGED {k}: {p}\n   was: {old[p][k]}\n   now: {new[p][k]}")
        for p in ldchg: print("CHANGED structured data:", p)
        print(f"{len(old)} pages before, {len(new)} now; {len(gone)} missing, {len(changed)} field changes, {len(ldchg)} JSON-LD changes")
        sys.exit(1 if gone or (strict and (changed or ldchg)) else 0)
    print(json.dumps(snap(), indent=1))
