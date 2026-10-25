"""Share images (Open Graph, 1200x630) that show each change's blackline.

Rendered with headless Chrome/Chromium when one is available (set QC_CHROME to its path, or have
google-chrome / chromium on PATH). Images are cached in docs/og/ with a manifest of input hashes,
so only new or edited changes are re-rendered. Without a browser, existing images are reused and
new changes fall back to the site-wide og.png."""
import hashlib, html, json, os, pathlib, shutil, subprocess, tempfile
from .redline import blackline, _trim

def _cut(t, n):
    w = t.split(" ")
    return t if len(w) <= n else " ".join(w[:n]) + "…"
from .util import LABEL, IMPACT, short_y

SITE = "https://quietlychanged.com"
VERSION = "3"   # bump to force every image to re-render after a template change

def chrome():
    for c in [os.environ.get("QC_CHROME"), shutil.which("google-chrome"), shutil.which("chromium"), shutil.which("chromium-browser"),
              shutil.which("google-chrome-stable"), "/opt/pw-browsers/chromium"]:
        if c and os.path.exists(c): return c
    return None

def _css(R):
    f = (R / "static" / "fonts").resolve().as_uri()
    return (R / "static" / "fonts.css").read_text().replace("url(fonts/", f"url({f}/") + """
*{box-sizing:border-box;margin:0}html,body{width:1200px;height:630px;overflow:hidden}
body{background:#EEF0EC;color:#15181D;font-family:Newsreader,Georgia,serif;padding:56px 64px 0;display:flex;flex-direction:column;position:relative}
.top{display:flex;align-items:center;gap:22px;font:600 19px/1 'IBM Plex Mono',monospace;letter-spacing:.09em;text-transform:uppercase;color:#737A84}
.brand{font:600 30px/1 Newsreader,serif;letter-spacing:-.02em;text-transform:none;color:#15181D;margin-right:auto}.brand i{font-style:normal;color:#BA2A1F}
.k{display:flex;align-items:center;gap:9px}.k:before{content:"";width:12px;height:12px;border-radius:50%;background:currentColor}
.pricing{color:#8A5B00}.terms{color:#2C6150}.privacy{color:#6B3FA3}
h1{font-weight:500;font-size:var(--fs,58px);line-height:1.06;letter-spacing:-.025em;margin-top:34px;max-width:1060px;display:-webkit-box;-webkit-line-clamp:3;-webkit-box-orient:vertical;overflow:hidden}
.ex{margin-top:auto;margin-bottom:96px;background:#FAFBF8;border:1.5px solid #D3D7D3;border-radius:4px;padding:24px 28px;font:400 25px/1.6 'IBM Plex Mono',monospace;color:#464D57;display:-webkit-box;-webkit-line-clamp:4;-webkit-box-orient:vertical;overflow:hidden}
.ex.tl{font:400 30px/1.42 Newsreader,serif;color:#464D57;background:none;border:0;padding:0;-webkit-line-clamp:3}
del{color:#9E2118;text-decoration:line-through;text-decoration-color:#BA2A1F;text-decoration-thickness:2.5px}
ins{color:#1D4DA6;text-decoration:underline;text-decoration-thickness:2.5px;text-underline-offset:5px;background:rgba(29,77,166,.08)}
.sr{display:none}
.foot{position:absolute;left:0;right:0;bottom:0;height:64px;background:#15181D;color:#FAFBF8;display:flex;align-items:center;justify-content:space-between;padding:0 64px;font:500 19px/1 'IBM Plex Mono',monospace;letter-spacing:.04em}
.imp{display:flex;align-items:center;gap:6px}.imp i{width:26px;height:9px;border-radius:2px;background:#4B525C}.imp i.on{background:#E0493C}.imp b{font-weight:500;margin-left:10px;text-transform:uppercase;letter-spacing:.08em}
"""

def _card(c, d):
    k = c.get("page", "terms"); n = int(c.get("impact") or 1)
    rl = next((r for r in c.get("redline", []) if r.get("before") and r.get("after")), None) or next(iter(c.get("redline", [])), None)
    if rl:
        b, a = rl.get("before", ""), rl.get("after", "")
        if b and a: b, a = _trim(b, a, ctx=12)
        else: b, a = _cut(b, 48), _cut(a, 48)
        inner = blackline(b, a) if b and a else f"<ins>{html.escape(a)}</ins>" if a else f"<del>{html.escape(b)}</del>"
        ex = f'<div class="ex">{inner}</div>'
    else:
        ex = f'<div class="ex tl">{html.escape(c.get("tldr") or c["what"][:220])}</div>'
    t = f'{c["service"]}: {c.get("headline", "")}'
    fs = 62 if len(t) < 70 else 54 if len(t) < 110 else 46
    pips = "".join(f'<i class="{"on" if i < n else ""}"></i>' for i in range(3))
    return (f'<div class="top"><span class="brand">Quietly<i>Changed</i></span><span class="k {k}">{LABEL.get(k, k)}</span><span>{short_y(d)}</span></div>'
            f'<h1 style="--fs:{fs}px">{html.escape(t)}</h1>{ex}'
            f'<div class="foot"><span>quietlychanged.com</span><span class="imp">{pips}<b>{IMPACT[n]}</b></span></div>')

def _render(exe, html_doc, out):
    # One browser at a time, default profile: a fresh --user-data-dir makes Chrome try first-run
    # network calls, which hang in sandboxes without internet access.
    with tempfile.TemporaryDirectory() as td:
        src = pathlib.Path(td) / "card.html"; src.write_text(html_doc)
        try:
            r = subprocess.run([exe, "--headless=new", "--no-sandbox", "--disable-gpu", "--hide-scrollbars", "--force-device-scale-factor=1",
                            "--no-first-run", "--no-default-browser-check", "--disable-background-networking", "--disable-component-update",
                            "--disable-sync", "--disable-features=Translate,OptimizationHints,MediaRouter", "--metrics-recording-only",
                            "--window-size=1200,630", "--virtual-time-budget=4000", f"--screenshot={out}", src.as_uri()],
                           capture_output=True, timeout=30)
        except subprocess.TimeoutExpired:
            return False
        return r.returncode == 0 and pathlib.Path(out).exists()

def build_all(D, R, ALL, today):
    outdir = D / "og"; outdir.mkdir(parents=True, exist_ok=True)
    man_p = outdir / "manifest.json"
    man = json.loads(man_p.read_text()) if man_p.exists() else {}
    css = _css(R); exe = chrome(); jobs = []
    result = {}
    for d, c in ALL:
        a = c["_art"]; doc = f"<!doctype html><meta charset=utf-8><style>{css}</style>{_card(c, d)}"
        h = hashlib.sha256((VERSION + doc).encode()).hexdigest()[:16]
        png = outdir / f"{a}.png"
        if png.exists() and man.get(a) == h:
            result[a] = f"{SITE}/og/{a}.png"; continue
        if exe: jobs.append((a, doc, png, h))
        elif png.exists(): result[a] = f"{SITE}/og/{a}.png"
    if jobs:
        for a, doc, png, h in jobs:
            if _render(exe, doc, str(png)): man[a] = h; result[a] = f"{SITE}/og/{a}.png"
            elif png.exists(): result[a] = f"{SITE}/og/{a}.png"
        print(f"Share images: rendered {sum(1 for j in jobs if j[0] in result)} of {len(jobs)}")
    elif not exe:
        print("Share images: no Chrome/Chromium found (set QC_CHROME); using existing images")
    man_p.write_text(json.dumps(man, indent=0, sort_keys=True))
    return result

def site_image(D, R):
    """The site-wide fallback og.png, in the same style."""
    exe = chrome()
    if not exe: return
    css = _css(R)
    doc = (f"<!doctype html><meta charset=utf-8><style>{css}h1.big{{font-size:118px;font-weight:400;letter-spacing:-.045em;margin-top:120px;line-height:.95}}h1.big i{{color:#BA2A1F}}"
           f".sub{{font:400 34px/1.4 Newsreader,serif;color:#464D57;margin-top:26px;max-width:900px}}</style>"
           '<div class="top"><span class="brand" style="visibility:hidden">.</span><span>Prices · Terms · Privacy</span></div>'
           '<h1 class="big">Quietly<i>Changed</i></h1><p class="sub">What popular services <del>quietly</del> <ins>actually</ins> change in their prices, terms and privacy policies. Every day, word for word.</p>'
           '<div class="foot"><span>quietlychanged.com</span><span>The fine-print watchdog</span></div>')
    h = hashlib.sha256((VERSION + doc).encode()).hexdigest()[:16]
    mark = D / "og" / "site.hash"
    if (D / "og.png").exists() and mark.exists() and mark.read_text() == h: return
    if _render(exe, doc, str(D / "og.png")): mark.write_text(h)
