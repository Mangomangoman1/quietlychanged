#!/usr/bin/env python3
"""Builds docs/ (GitHub Pages root). Inputs per day in reports/:
  DATE-summary.md   – intro/lede in light markdown (required)
  DATE-changes.json – optional list of {"service","page":"pricing|terms|privacy","what","who","url"}
"""
import json, pathlib, html, re, datetime
R = pathlib.Path(__file__).parent; D = R/"docs"; (D/"reports").mkdir(parents=True, exist_ok=True)
SITE = "https://quietlychanged.com"; TAG = "Daily, plain-English reports on what popular services quietly change in their prices, terms, and privacy policies."
E = html.escape
LABEL = {"pricing":"Pricing","terms":"Terms","privacy":"Privacy"}
CSS = """
:root{--ink:#1a1a1a;--muted:#5a5a5a;--rule:#d9d6cf;--paper:#fbfaf7;--card:#fff;--accent:#b3261e;--serif:Charter,"Bitstream Charter","Iowan Old Style","Sitka Text",Cambria,Georgia,serif;--sans:system-ui,-apple-system,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif}
*{box-sizing:border-box}html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--paper);color:var(--ink);font:1.0625rem/1.65 var(--serif)}
a{color:var(--accent);text-underline-offset:2px}a:hover{text-decoration-thickness:2px}
:focus-visible{outline:3px solid var(--accent);outline-offset:2px}
.skip{position:absolute;left:-999px}.skip:focus{left:1rem;top:1rem;background:#fff;padding:.5rem;z-index:9}
.wrap{max-width:46rem;margin:0 auto;padding:0 1.25rem}
header.mast{border-bottom:3px double var(--ink);background:var(--card)}
.mast .top{border-bottom:1px solid var(--rule);font:600 .75rem/1 var(--sans);letter-spacing:.08em;text-transform:uppercase;color:var(--muted);padding:.6rem 0}
.mast .top .wrap{display:flex;justify-content:space-between;gap:1rem}
.brand{display:block;text-align:center;padding:1.4rem 0 .4rem;text-decoration:none;color:var(--ink)}
.brand b{font:700 clamp(2rem,6vw,3.1rem)/1 var(--serif);letter-spacing:-.02em}.brand b i{color:var(--accent);font-style:normal}
.tagline{text-align:center;margin:.3rem auto 1rem;max-width:34rem;font:.95rem/1.45 var(--sans);color:var(--muted)}
nav.main ul{display:flex;justify-content:center;flex-wrap:wrap;gap:.7rem 1.4rem;list-style:none;margin:0;padding:.7rem 0;border-top:1px solid var(--rule);font:600 .85rem/1 var(--sans);text-transform:uppercase;letter-spacing:.06em}
nav.main a{display:inline-block;color:var(--ink);text-decoration:none;padding:.3rem 0}nav.main a[aria-current]{border-bottom:2px solid var(--accent)}
main{padding:2rem 0 3rem}
h1,h2,h3{font-family:var(--serif);line-height:1.2;letter-spacing:-.01em}
h1{font-size:clamp(1.7rem,4.5vw,2.3rem);margin:.2rem 0 .6rem}h2{font-size:1.4rem;margin:2.2rem 0 .8rem;padding-top:.6rem;border-top:1px solid var(--rule)}
.kicker{font:700 .75rem/1 var(--sans);letter-spacing:.1em;text-transform:uppercase;color:var(--accent)}
.meta{font:.85rem/1.4 var(--sans);color:var(--muted)}
.lede{font-size:1.15rem}
.cards{list-style:none;padding:0;margin:1rem 0;display:grid;gap:1rem}
.card{background:var(--card);border:1px solid var(--rule);border-left:4px solid var(--accent);padding:1rem 1.2rem;border-radius:2px}
.card h3{margin:.35rem 0 .5rem;font-size:1.2rem}
.card dl{margin:0;display:grid;grid-template-columns:auto 1fr;gap:.3rem .8rem;font:.92rem/1.5 var(--sans)}
.card dt{font-weight:700;color:var(--muted)}.card dd{margin:0}
.card .foot{display:flex;justify-content:space-between;flex-wrap:wrap;gap:.5rem;margin-top:.7rem;font:.82rem var(--sans);color:var(--muted)}
.tag{display:inline-block;font:700 .7rem/1 var(--sans);letter-spacing:.06em;text-transform:uppercase;padding:.3rem .5rem;border:1px solid currentColor;border-radius:2px;color:var(--ink);margin-right:.35rem}
.tag.pricing{color:#1d4f91}.tag.terms{color:#5b3a00}.tag.privacy{color:#6a1b9a}
.empty{background:var(--card);border:1px dashed var(--rule);padding:1rem 1.2rem;font-family:var(--sans)}
.filters{display:flex;flex-wrap:wrap;gap:.6rem;align-items:center;margin:1rem 0;font-family:var(--sans)}
.filters input{flex:1 1 14rem;font:1rem var(--sans);padding:.6rem .7rem;border:1px solid #8a8780;border-radius:2px;background:#fff}
.filters button{font:600 .8rem var(--sans);padding:.5rem .8rem;border:1px solid var(--ink);background:#fff;color:var(--ink);border-radius:2px;cursor:pointer}
.filters button[aria-pressed=true]{background:var(--ink);color:#fff}
table{width:100%;border-collapse:collapse;font:.92rem/1.45 var(--sans);background:var(--card)}
th,td{text-align:left;padding:.6rem .7rem;border-bottom:1px solid var(--rule);vertical-align:top}th{font-size:.75rem;text-transform:uppercase;letter-spacing:.06em;color:var(--muted)}
.archive{list-style:none;padding:0;font-family:var(--sans)}.archive li{display:flex;justify-content:space-between;gap:1rem;padding:.7rem 0;border-bottom:1px solid var(--rule)}
.archive .n{color:var(--muted);font-size:.85rem;white-space:nowrap}
footer{border-top:3px double var(--ink);background:var(--card);padding:1.6rem 0;font:.85rem/1.6 var(--sans);color:var(--muted)}
footer .wrap{display:grid;gap:.8rem}footer nav a{margin-right:1rem}
.sr{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0)}
@media(max-width:600px){body{font-size:1rem}.card dl{grid-template-columns:1fr}.card dt{margin-top:.3rem}th:nth-child(3),td:nth-child(3){display:none}.mast .top .wrap span:last-child{display:none}}
"""
FAV = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="8" fill="#1a1a1a"/><text x="32" y="45" font-family="Georgia,serif" font-size="38" font-weight="700" text-anchor="middle" fill="#fff">Q</text><rect x="14" y="50" width="36" height="4" fill="#b3261e"/></svg>'
NAV = [("index.html","Latest"),("archive.html","Archive"),("services.html","What we track"),("about.html","How it works")]

def nice(d): return datetime.date.fromisoformat(d).strftime("%B %-d, %Y")
def page(fn, title, body, desc=TAG, depth=0):
    p = "../"*depth; url = f"{SITE}/{fn}"
    nav = "".join(f'<li><a href="{p}{h}"{" aria-current=page" if fn==h else ""}>{t}</a></li>' for h,t in NAV)
    full = "QuietlyChanged" if fn=="index.html" else f"{title} · QuietlyChanged"
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{E(full)}</title><meta name="description" content="{E(desc)}"><link rel="canonical" href="{url}">
<meta property="og:type" content="website"><meta property="og:site_name" content="QuietlyChanged"><meta property="og:title" content="{E(full)}"><meta property="og:description" content="{E(desc)}"><meta property="og:url" content="{url}"><meta property="og:image" content="{SITE}/og.svg"><meta name="twitter:card" content="summary">
<link rel="icon" href="{p}favicon.svg" type="image/svg+xml"><meta name="theme-color" content="#1a1a1a"><link rel="stylesheet" href="{p}style.css"><link rel="alternate" type="application/atom+xml" href="{p}feed.xml" title="QuietlyChanged"></head>
<body><a class="skip" href="#main">Skip to content</a>
<header class="mast"><div class="top"><div class="wrap"><span>The fine-print watchdog</span><span>{nice(TODAY)}</span></div></div>
<div class="wrap"><a class="brand" href="{p}index.html"><b>Quietly<i>Changed</i></b></a><p class="tagline">{TAG}</p>
<nav class="main" aria-label="Main"><ul>{nav}</ul></nav></div></header>
<main id="main"><div class="wrap">{body}</div></main>
<footer><div class="wrap"><nav aria-label="Footer"><a href="{p}about.html">How it works</a><a href="{p}archive.html">Archive</a><a href="{p}services.html">Tracked services</a><a href="{p}feed.xml">Feed</a></nav>
<p>QuietlyChanged is an independent project. We snapshot public pages daily and summarize the differences. Always check the linked source; summaries are not legal advice.</p><p>© {TODAY[:4]} QuietlyChanged</p></div></footer></body></html>'''

def md(t):
    out=[]; inl=False
    for l in t.splitlines():
        e=E(l); e=re.sub(r"\*\*(.+?)\*\*",r"<strong>\1</strong>",e); e=re.sub(r"\[(.+?)\]\((.+?)\)",r'<a href="\2">\1</a>',e)
        if l.startswith("- "):
            if not inl: out.append("<ul>"); inl=True
            out.append(f"<li>{e[2:]}</li>"); continue
        if inl: out.append("</ul>"); inl=False
        if l.startswith("## "): out.append(f"<h2>{e[3:]}</h2>")
        elif l.startswith("# "): out.append(f"<h1>{e[2:]}</h1>")
        elif l.strip(): out.append(f"<p>{e}</p>")
    if inl: out.append("</ul>")
    return "\n".join(out)

def tag(k): return f'<span class="tag {k}">{LABEL.get(k,k.title())}</span>'
def cards(items, d):
    if not items: return '<p class="empty">No meaningful changes detected on tracked pages today.</p>'
    li=[]
    for c in items:
        k=c.get("page","terms")
        li.append(f'''<li><article class="card"><div>{tag(k)}</div><h3>{E(c["service"])}: {E(c.get("headline") or LABEL.get(k,k)+" page updated")}</h3>
<dl><dt>What changed</dt><dd>{E(c["what"])}</dd><dt>Who it affects</dt><dd>{E(c.get("who","All users"))}</dd></dl>
<div class="foot"><time datetime="{d}">{nice(d)}</time><a href="{E(c["url"])}">View source page<span class="sr"> for {E(c["service"])}</span> →</a></div></article></li>''')
    return f'<ul class="cards">{"".join(li)}</ul>'

def day_body(d, sm, items, h1=True):
    txt = sm.read_text(); body = md(txt)
    if not txt.lstrip().startswith("# "): body = f"<h1>Report for {nice(d)}</h1>"+body
    first,_,rest = body.partition("</h1>")
    head = f'<p class="kicker">Daily report</p>{first}</h1><p class="meta"><time datetime="{d}">{nice(d)}</time> · {len(items)} change{"s"*(len(items)!=1)}</p>'
    # changes section precedes any long lists in the summary
    return head + (f"<h2>What changed</h2>{cards(items,d)}" if items or "Day 0" not in first else "") + rest

TODAY = datetime.date.today().isoformat()
days = sorted(p.name[:10] for p in (R/"reports").glob("*-summary.md"))
data = {}
for d in days:
    cj = R/"reports"/f"{d}-changes.json"
    items = json.loads(cj.read_text()) if cj.exists() else []
    data[d] = items
    (D/"reports"/f"{d}.html").write_text(page(f"reports/{d}.html", f"Report, {nice(d)}", day_body(d, R/"reports"/f"{d}-summary.md", items), depth=1))
if days:
    L = days[-1]
    (D/"index.html").write_text(page("index.html","Latest", day_body(L, R/"reports"/f"{L}-summary.md", data[L]).replace('href="../','href="') + f'<p class="meta"><a href="reports/{L}.html">Permalink</a> · <a href="archive.html">Earlier reports</a></p>'))
arch = "".join(f'<li><a href="reports/{d}.html">{nice(d)}</a><span class="n">{len(data[d])} change{"s"*(len(data[d])!=1)}</span></li>' for d in reversed(days))
(D/"archive.html").write_text(page("archive.html","Archive", f'<p class="kicker">Archive</p><h1>Every report, by date</h1><ul class="archive">{arch}</ul>'))
s = json.loads((R/"services.json").read_text())
rows = "".join(f'<tr data-k="{" ".join(v)}"><td><strong>{E(k)}</strong></td><td>{"".join(tag(p) for p in v)}</td><td>{" · ".join(f"<a href=\"{E(u)}\">{LABEL[p]}</a>" for p,u in v.items())}</td></tr>' for k,v in sorted(s.items(), key=lambda x:x[0].lower()))
btn = "".join(f'<button type="button" data-f="{k}" aria-pressed="false">{v}</button>' for k,v in LABEL.items())
(D/"services.html").write_text(page("services.html","What we track", f'''<p class="kicker">Coverage</p><h1>What we track</h1><p>{len(s)} services and {sum(map(len,s.values()))} pages, checked every day.</p>
<div class="filters" role="search"><label class="sr" for="q">Search services</label><input id="q" type="search" placeholder="Search services…" autocomplete="off">{btn}</div>
<p class="meta" id="count" aria-live="polite"></p>
<table><thead><tr><th scope="col">Service</th><th scope="col">Pages</th><th scope="col">Sources</th></tr></thead><tbody id="rows">{rows}</tbody></table>
<script>(()=>{{const q=document.getElementById("q"),rs=[...document.querySelectorAll("#rows tr")],bs=[...document.querySelectorAll("[data-f]")],c=document.getElementById("count");let f=null;
function go(){{const t=q.value.toLowerCase();let n=0;rs.forEach(r=>{{const ok=r.cells[0].textContent.toLowerCase().includes(t)&&(!f||r.dataset.k.split(" ").includes(f));r.hidden=!ok;n+=ok}});c.textContent=n+" of "+rs.length+" services shown"}}
q.addEventListener("input",go);bs.forEach(b=>b.addEventListener("click",()=>{{f=f===b.dataset.f?null:b.dataset.f;bs.forEach(x=>x.setAttribute("aria-pressed",x.dataset.f===f));go()}}));go()}})()</script>'''))
(D/"about.html").write_text(page("about.html","How it works", f'''<p class="kicker">About</p><h1>How it works</h1>
<p class="lede">Companies revise their prices, plan limits, terms of service, and privacy policies all the time, usually without announcement. QuietlyChanged keeps a public, dated record of those changes.</p>
<h2>Our method</h2><ol><li><strong>Snapshot.</strong> Every morning we fetch the public pricing, terms, and privacy pages of every <a href="services.html">tracked service</a> and save the main text.</li>
<li><strong>Compare.</strong> Each snapshot is compared line by line with the previous day's. We filter out noise such as cookie banners, scripts, timestamps, and copyright lines.</li>
<li><strong>Explain.</strong> Meaningful differences are summarized in plain English: what changed, who it affects, and a link to the source.</li>
<li><strong>Publish.</strong> The day's report goes on the front page and into the <a href="archive.html">archive</a>.</li></ol>
<h2>Categories</h2><p>{tag("pricing")} prices, plans, limits, and fees. {tag("terms")} terms of service, user agreements, and contracts of carriage. {tag("privacy")} privacy policies and data-use notices.</p>
<h2>Limits</h2><p>Some sites block automated readers or load their text with scripts; we only track pages we can read reliably. Summaries are not legal advice. Always check the linked source.</p>'''))
(D/"style.css").write_text(CSS); (D/"favicon.svg").write_text(FAV)
(D/"og.svg").write_text('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 630"><rect width="1200" height="630" fill="#fbfaf7"/><rect y="600" width="1200" height="30" fill="#b3261e"/><text x="600" y="300" font-family="Georgia,serif" font-size="110" font-weight="700" text-anchor="middle" fill="#1a1a1a">Quietly<tspan fill="#b3261e">Changed</tspan></text><text x="600" y="390" font-family="Arial,sans-serif" font-size="34" text-anchor="middle" fill="#5a5a5a">What popular services quietly change in their fine print</text></svg>')
feed = "".join(f'<entry><title>Report, {nice(d)}</title><link href="{SITE}/reports/{d}.html"/><id>{SITE}/reports/{d}.html</id><updated>{d}T12:00:00Z</updated></entry>' for d in reversed(days))
(D/"feed.xml").write_text(f'<?xml version="1.0" encoding="utf-8"?><feed xmlns="http://www.w3.org/2005/Atom"><title>QuietlyChanged</title><link href="{SITE}/"/><id>{SITE}/</id><updated>{(days or [TODAY])[-1]}T12:00:00Z</updated>{feed}</feed>')
(D/".nojekyll").write_text("")
if not (D/"CNAME").exists(): (D/"CNAME").write_text("quietlychanged.com\n")
