#!/usr/bin/env python3
"""Builds docs/ (GitHub Pages root). Inputs per day in reports/:
  DATE-summary.md   – intro/lede in light markdown (required)
  DATE-changes.json – optional list of {"service","page":"pricing|terms|privacy","what","who","url","note?"}
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
.note{background:#fff8e8;border:1px solid #d4a017;border-left:4px solid #b3261e;padding:.9rem 1rem;margin:1.2rem 0;font:.95rem/1.55 var(--sans);border-radius:2px}.note strong{display:block;font:700 .75rem/1 var(--sans);letter-spacing:.08em;text-transform:uppercase;color:#b3261e;margin-bottom:.45rem}
.filters{display:flex;flex-wrap:wrap;gap:.6rem;align-items:center;margin:1rem 0;font-family:var(--sans)}
.filters input{flex:1 1 14rem;font:1rem var(--sans);padding:.6rem .7rem;border:1px solid #8a8780;border-radius:2px;background:#fff}
.filters button{font:600 .8rem var(--sans);padding:.5rem .8rem;border:1px solid var(--ink);background:#fff;color:var(--ink);border-radius:2px;cursor:pointer}
.filters button[aria-pressed=true]{background:var(--ink);color:#fff}
.tablewrap{overflow-x:auto;-webkit-overflow-scrolling:touch}
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
PAGES = []
ORG = {"@context":"https://schema.org","@type":"Organization","name":"QuietlyChanged","url":SITE+"/","logo":SITE+"/og.png"}
HUB_FOR = {"pricing":("price-changes/","Price changes"),"terms":("terms-of-service-changes/","Terms of service changes"),"privacy":("privacy-policy-changes/","Privacy policy changes")}
NAV = [("index.html","Latest"),("archive.html","Archive"),("services.html","What we track"),("about.html","How it works")]

def slug(x): return re.sub(r"[^a-z0-9]+","-",x.lower().replace("+","-plus")).strip("-")
def slug_tr(x): return re.sub(r"[^a-z0-9]+","-",x.lower()).strip("-")
def art_slug(d,c): return f"{d}-{slug(c['service'])}-{slug(c.get('headline') or c.get('page','update'))}"[:90].strip("-")
def nice(d): return datetime.date.fromisoformat(d).strftime("%B %-d, %Y")
def page(fn, title, body, desc=TAG, depth=0, ld=None, otype="website", lastmod=None, crumbs=None):
    p = "../"*depth; url = f"{SITE}/{fn}".replace("/index.html","/")
    PAGES.append((url, lastmod))
    lds = [ORG] + (ld if isinstance(ld,list) else [ld] if ld else [])
    if crumbs: lds.append({"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":i+1,"name":n,"item":u} for i,(n,u) in enumerate(crumbs+[(title,url)])]})
    ldh = "".join(f'<script type="application/ld+json">{json.dumps(x)}</script>' for x in lds)
    nav = "".join(f'<li><a href="{p}{h}"{" aria-current=page" if fn==h else ""}>{t}</a></li>' for h,t in NAV)
    full = "QuietlyChanged: daily pricing, terms & privacy policy changes" if fn=="index.html" else f"{title} · QuietlyChanged"
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{E(full)}</title><meta name="description" content="{E(desc)}"><link rel="canonical" href="{url}">
<meta property="og:type" content="{otype}"><meta property="og:site_name" content="QuietlyChanged"><meta property="og:title" content="{E(full)}"><meta property="og:description" content="{E(desc)}"><meta property="og:url" content="{url}"><meta property="og:image" content="{SITE}/og.png"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta name="twitter:card" content="summary_large_image">{ldh}
<link rel="icon" href="{p}favicon.svg" type="image/svg+xml"><meta name="theme-color" content="#1a1a1a"><link rel="stylesheet" href="{p}style.css"><link rel="alternate" type="application/atom+xml" href="{p}feed.xml" title="QuietlyChanged"></head>
<body><a class="skip" href="#main">Skip to content</a>
<header class="mast"><div class="top"><div class="wrap"><span>The fine-print watchdog</span><span>{nice(TODAY)}</span></div></div>
<div class="wrap"><a class="brand" href="{p}index.html"><b>Quietly<i>Changed</i></b></a><p class="tagline">{TAG}</p>
<nav class="main" aria-label="Main"><ul>{nav}</ul></nav></div></header>
<main id="main"><div class="wrap">{body}</div></main>
<footer><div class="wrap"><nav aria-label="Footer"><a href="{p}about.html">How it works</a><a href="{p}archive.html">Archive</a><a href="{p}services.html">Tracked services</a><a href="{p}price-changes/">Price changes</a><a href="{p}subscription-price-history/">Price history</a><a href="{p}terms-of-service-changes/">Terms changes</a><a href="{p}privacy-policy-changes/">Privacy changes</a><a href="{p}feed.xml">Feed</a></nav>
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
        li.append(f'''<li><article class="card"><div>{tag(k)}</div><h3><a href="../changes/{art_slug(d,c)}/">{E(c["service"])}: {E(c.get("headline") or LABEL.get(k,k)+" page updated")}</a></h3>
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
    svs = sorted({c["service"] for c in items})
    desc = (f"{len(items)} changes on {nice(d)}: " + ", ".join(svs[:6]) + ". Plain-English summaries with source links.") if items else f"QuietlyChanged daily report for {nice(d)}: what popular services changed in their pricing, terms, and privacy pages."
    if d == days[0] and not items: desc = f"Day 0: QuietlyChanged starts tracking {len(json.loads((R/'services.json').read_text()))} popular services' pricing, terms of service, and privacy policies."
    hl = (R/"reports"/f"{d}-summary.md").read_text().splitlines()[0].lstrip("# ").strip() or f"Report, {nice(d)}"
    ld = {"@context":"https://schema.org","@type":"NewsArticle","headline":hl[:110],"datePublished":d+"T06:00:00-06:00","dateModified":d+"T06:00:00-06:00","url":f"{SITE}/reports/{d}.html","image":[SITE+"/og.png"],"author":{"@type":"Organization","name":"QuietlyChanged","url":SITE+"/"},"publisher":ORG,"description":desc}
    (D/"reports"/f"{d}.html").write_text(page(f"reports/{d}.html", f"{hl} ({nice(d)})", day_body(d, R/"reports"/f"{d}-summary.md", items), desc=desc, depth=1, ld=ld, otype="article", lastmod=d, crumbs=[("Home",SITE+"/"),("Archive",SITE+"/archive.html")]))
if days:
    L = days[-1]
    WEB = {"@context":"https://schema.org","@type":"WebSite","name":"QuietlyChanged","url":SITE+"/","description":TAG}
    (D/"index.html").write_text(page("index.html","Latest", ld=WEB, lastmod=L, body= day_body(L, R/"reports"/f"{L}-summary.md", data[L]).replace('href="../','href="') + f'<p class="meta"><a href="reports/{L}.html">Permalink</a> · <a href="archive.html">Earlier reports</a></p><h2>Browse by type</h2><p><a href="price-changes/">Price increases and pricing changes</a> · <a href="subscription-price-history/">Streaming and subscription price history compared</a> · <a href="terms-of-service-changes/">Terms of service changes</a> · <a href="privacy-policy-changes/">Privacy policy changes</a></p>'))
arch = "".join(f'<li><a href="reports/{d}.html">{nice(d)}</a><span class="n">{len(data[d])} change{"s"*(len(data[d])!=1)}</span></li>' for d in reversed(days))
(D/"archive.html").write_text(page("archive.html","Archive", lastmod=(days or [TODAY])[-1], desc="Archive of every QuietlyChanged daily report on pricing, terms of service, and privacy policy changes, by date.", body= f'<p class="kicker">Archive</p><h1>Every report, by date</h1><ul class="archive">{arch}</ul>'))
s = json.loads((R/"services.json").read_text())
TRACKED_SLUGS = {slug(k) for k in s}
rows = "".join(f'<tr data-k="{" ".join(v)}"><td><strong><a href="services/{slug(k)}/">{E(k)}</a></strong></td><td>{"".join(tag(p) for p in v)}</td><td>{" · ".join(f"<a href=\"{E(u)}\">{LABEL[p]}</a>" for p,u in v.items())}</td></tr>' for k,v in sorted(s.items(), key=lambda x:x[0].lower()))
btn = "".join(f'<button type="button" data-f="{k}" aria-pressed="false">{v}</button>' for k,v in LABEL.items())
(D/"services.html").write_text(page("services.html","What we track", desc=f"Search the {len(s)} services QuietlyChanged monitors daily for pricing, terms of service, and privacy policy changes.", body=f'''<p class="kicker">Coverage</p><h1>What we track</h1><p>{len(s)} services and {sum(map(len,s.values()))} pages, checked every day.</p>
<div class="filters" role="search"><label class="sr" for="q">Search services</label><input id="q" type="search" placeholder="Search services…" autocomplete="off">{btn}</div>
<p class="meta" id="count" aria-live="polite"></p>
<table><thead><tr><th scope="col">Service</th><th scope="col">Pages</th><th scope="col">Sources</th></tr></thead><tbody id="rows">{rows}</tbody></table>
<script>(()=>{{const q=document.getElementById("q"),rs=[...document.querySelectorAll("#rows tr")],bs=[...document.querySelectorAll("[data-f]")],c=document.getElementById("count");let f=null;
function go(){{const t=q.value.toLowerCase();let n=0;rs.forEach(r=>{{const ok=r.cells[0].textContent.toLowerCase().includes(t)&&(!f||r.dataset.k.split(" ").includes(f));r.hidden=!ok;n+=ok}});c.textContent=n+" of "+rs.length+" services shown"}}
q.addEventListener("input",go);bs.forEach(b=>b.addEventListener("click",()=>{{f=f===b.dataset.f?null:b.dataset.f;bs.forEach(x=>x.setAttribute("aria-pressed",x.dataset.f===f));go()}}));go()}})()</script>'''))
(D/"about.html").write_text(page("about.html","How it works", desc="How QuietlyChanged snapshots, compares, and explains daily changes to popular services' pricing pages, terms, and privacy policies.", body=f'''<p class="kicker">About</p><h1>How it works</h1>
<p class="lede">Companies revise their prices, plan limits, terms of service, and privacy policies all the time, usually without announcement. QuietlyChanged keeps a public, dated record of those changes.</p>
<h2>Our method</h2><ol><li><strong>Snapshot.</strong> Every morning we fetch the public pricing, terms, and privacy pages of every <a href="services.html">tracked service</a> and save the main text.</li>
<li><strong>Compare.</strong> Each snapshot is compared line by line with the previous day's. We filter out noise such as cookie banners, scripts, timestamps, and copyright lines.</li>
<li><strong>Explain.</strong> Meaningful differences are summarized in plain English: what changed, who it affects, and a link to the source.</li>
<li><strong>Publish.</strong> The day's report goes on the front page and into the <a href="archive.html">archive</a>.</li></ol>
<h2>Categories</h2><p>{tag("pricing")} prices, plans, limits, and fees. {tag("terms")} terms of service, user agreements, and contracts of carriage. {tag("privacy")} privacy policies and data-use notices.</p>
<h2>Limits</h2><p>Some sites block automated readers or load their text with scripts; we only track pages we can read reliably. Summaries are not legal advice. Always check the linked source.</p>'''))
(D/"style.css").write_text(CSS); (D/"favicon.svg").write_text(FAV)
(D/"og.svg").write_text('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 630"><rect width="1200" height="630" fill="#fbfaf7"/><rect y="600" width="1200" height="30" fill="#b3261e"/><text x="600" y="300" font-family="Georgia,serif" font-size="110" font-weight="700" text-anchor="middle" fill="#1a1a1a">Quietly<tspan fill="#b3261e">Changed</tspan></text><text x="600" y="390" font-family="Arial,sans-serif" font-size="34" text-anchor="middle" fill="#5a5a5a">What popular services quietly change in their fine print</text></svg>')
# Atom feed built after change articles (see below)
(D/".nojekyll").write_text("")
if not (D/"CNAME").exists(): (D/"CNAME").write_text("quietlychanged.com\n")

# ---- standalone change articles ----
ARTS=[]
_PHK = {k for k in json.loads((R/"price_history.json").read_text()) if not k.startswith("_")} if (R/"price_history.json").exists() else set()
for d in days:
    for c in data[d]:
        a=art_slug(d,c); c["_art"]=a; (D/"changes"/a).mkdir(parents=True, exist_ok=True)
        t=c.get("seo_title") or f'{c["service"]}: {c.get("headline") or "page updated"}'
        ds=c.get("seo_desc") or (c["what"][:155])
        k=c.get("page","terms"); sl=slug(c["service"]); has_svc = sl in TRACKED_SLUGS
        ld={"@context":"https://schema.org","@type":"NewsArticle","headline":t[:110],"datePublished":d+"T06:00:00-06:00","dateModified":c.get("modified",d)+"T06:00:00-06:00","url":f"{SITE}/changes/{a}/","image":[SITE+"/og.png"],"author":{"@type":"Organization","name":"QuietlyChanged","url":SITE+"/"},"publisher":ORG,"description":ds,"about":{"@type":"Organization","name":c["service"]}}
        note_html = f'<aside class="note" role="note"><strong>Update</strong>{E(c["note"])}</aside>' if c.get("note") else ""
        more_svc = (f'<a href="../../services/{sl}/#price-history">{E(c["service"])} price history: every increase, with dates</a> · ' if has_svc and c["service"] in _PHK else "") + (f'<a href="../../services/{sl}/">Full {E(c["service"])} change history</a> · ' if has_svc else "")
        body=f'''<p class="kicker">{tag(k)} {E(c["service"])}</p><h1>{E(t)}</h1><p class="meta"><time datetime="{d}">{nice(d)}</time> · Detected by QuietlyChanged's daily check</p>
<p class="lede">{E(c["what"])}</p>{note_html}<h2>Who it affects</h2><p>{E(c.get("who","All users"))}</p>
<h2>Source</h2><p>Detected on the {E(c["service"])} {LABEL.get(k,k).lower()} page: <a href="{E(c["url"])}">{E(c["url"])}</a>. Always check the source; this summary is not legal or financial advice.</p>
<h2>More</h2><p>{more_svc}<a href="../../{HUB_FOR[k][0]}">All {HUB_FOR[k][1].lower()}</a> · <a href="../../reports/{d}.html">Report for {nice(d)}</a> · <a href="../../archive.html">All reports</a></p>'''
        crumbs=[("Home",SITE+"/"),(HUB_FOR.get(k,("",""))[1] or "Changes",f"{SITE}/{HUB_FOR.get(k,('archive.html',''))[0]}")]
        if has_svc: crumbs.append((c["service"],f"{SITE}/services/{sl}/"))
        (D/"changes"/a/"index.html").write_text(page(f"changes/{a}/index.html", t, body, desc=ds, depth=2, ld=ld, otype="article", lastmod=c.get("modified",d), crumbs=crumbs))
        ARTS.append((d,c,t))

# ---- evergreen category hubs (price / terms / privacy changes) ----
# ---- sourced US price histories (price_history.json) ----
PH = {k:v for k,v in json.loads((R/"price_history.json").read_text()).items() if not k.startswith("_")} if (R/"price_history.json").exists() else {}
def _pd(x): return x if len(x)==4 else datetime.date.fromisoformat(x).strftime("%b %-d, %Y") if len(x)==10 else datetime.date.fromisoformat(x+"-01").strftime("%b %Y")
def _cur(rows): return rows[-1][1]
def _chg(p,q):
    dlt=p-q; sg="+" if dlt>=0 else "−"; return f"{sg}${abs(dlt):.2f} ({sg}{abs(p/q-1)*100:.0f}%)"
def _u(h,pl): return h.get("units",{}).get(pl,"month")
def _amt(h,pl,p): return f"${p:.2f}/{_u(h,pl)}" if p!=int(p) or _u(h,pl)=="month" else f"${p:.0f}/{_u(h,pl)}"
def ph_section(k, h):
    k = h.get("name", k); tk = h.get("title_name", k)
    first_year = min(r[0][:4] for rows in h["plans"].values() for r in rows)
    tabs = ""
    for plan, rows in h["plans"].items():
        tr = "".join(f'<tr><td><time datetime="{r[0]}">{_pd(r[0])}</time></td><td>{_amt(h,plan,r[1]).split("/")[0]}</td><td>{E(r[2]) if len(r)>2 else "Launch" if i==0 else _chg(r[1],rows[i-1][1])}</td></tr>' for i,r in enumerate(rows))
        tabs += f'<h3>{E(k)} {E(plan)}</h3><table><thead><tr><th scope="col">Effective</th><th scope="col">Price / {_u(h,plan)}</th><th scope="col">Change</th></tr></thead><tbody>{tr}</tbody></table>'
    now = "".join(f'<li><strong>{E(pl)}</strong>: {_amt(h,pl,_cur(r))}</li>' for pl,r in h["plans"].items() if "discontinued" not in pl)
    L = h["latest"]; fl = h["plans"][h["flagship"]]
    notes = "".join(f"<li>{E(n)}</li>" for n in h.get("notes",[]))
    srcs = "".join(f'<li><a href="{E(u)}">{E(n)}</a></li>' for n,u in h["sources"])
    html_ = (f'<h2 id="price-history">{E(tk)} price history (US, {first_year} to {h["verified"][:4]})</h2><p>{E(h["intro"])}</p>'
             f'<h3>What {E(k)} costs now</h3><ul>{now}</ul><p class="note"><strong>Latest change</strong>On {_pd(L["date"])}, {E(L["what"])} (<a href="{E(L["source"])}">{E(L["source_name"])}</a>)</p>'
             f'{tabs}' + (f'<ul class="meta">{notes}</ul>' if notes else "") +
             f'<p class="meta">{E(h["basis"].format(verified=nice(h["verified"]))) if h.get("basis") else "US list prices for new monthly subscribers, before tax, in nominal dollars. Compiled from the sources below and last verified " + nice(h["verified"]) + "."} Spotted an error? The sources are linked so you can check.</p><h3>Sources</h3><ul class="meta">{srcs}</ul><p><a href="../../subscription-price-history/">' + (f'Compare {E(k)} with other streaming and subscription price increases' if h.get("compare",True) else 'Compare streaming and subscription price increases') + '</a> · <a href="../../price-changes/">All price changes we track</a></p>')
    pct = (fl[-1][1]/fl[0][1]-1)*100
    faq = [(f"How much does {k} cost per month in the US?", "As of " + nice(h["verified"]) + ", " + "; ".join(f"{pl} is {_amt(h,pl,_cur(r))}" for pl,r in h["plans"].items() if "discontinued" not in pl) + "."),
           (f"When did {k} last raise prices?", f"On {_pd(L['date'])}: {L['what']}"),
           (f"How much has {k} gone up?", f"{k} {h['flagship']} went from {_amt(h,h['flagship'],fl[0][1])} {"on" if len(fl[0][0])==10 else "in"} {_pd(fl[0][0])} to {_amt(h,h['flagship'],fl[-1][1])}, an increase of {pct:.0f}% across {len(fl)-1} price change{"s"*(len(fl)!=2)}.")]
    html_ += '<h3>Quick answers</h3>' + "".join(f"<p><strong>{E(q)}</strong><br>{E(a)}</p>" for q,a in faq)
    ld = {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faq]}
    return html_, ld, pct, fl
HUBS = {
 "pricing": ("Subscription price increases & pricing changes in {Y} (tracker)", "Every price increase, new fee, plan limit, and pricing-page change QuietlyChanged has detected at popular subscriptions and apps in {Y}, dated and linked to the source.",
             "Price hikes rarely come with a press release. They show up as a new number on a pricing page, a fee line on a support page, or a plan that quietly loses a feature. This page collects every pricing change our daily check has caught, newest first, with the date we saw it and a link to the source."),
 "terms": ("Terms of service changes in {Y}: dated tracker", "A dated list of every terms of service, user agreement, and contract change QuietlyChanged has detected at popular apps, banks, and services in {Y}, with plain-English summaries.",
           "Terms of service updates decide what you can dispute, what a company can do with your money, and how disagreements get settled. This page lists every terms change our daily check has caught, newest first, in plain English with a link to the source text."),
 "privacy": ("Privacy policy changes in {Y}: dated tracker", "A dated list of every privacy policy change QuietlyChanged detects at popular apps and services in {Y}: new data uses, sharing, AI training, and retention changes.",
             "Privacy policies change more often than most people realize, and the edits that matter (new data sharing, AI training, longer retention) are usually buried in long documents. This page lists every privacy policy change our daily check catches, newest first, with a link to the source."),
}
for k,(tt,dd,lede) in HUBS.items():
    fn, short = HUB_FOR[k]; Y = TODAY[:4]; tt=tt.format(Y=Y); dd=dd.format(Y=Y)
    items = [(d,c) for d in reversed(days) for c in data[d] if c.get("page","terms")==k]
    by_month = {}
    for d,c in items: by_month.setdefault(d[:7], []).append((d,c))
    sec = ""
    for m, its in by_month.items():
        mname = datetime.date.fromisoformat(m+"-01").strftime("%B %Y")
        def _hist(c,d):
            slc=slug(c["service"])
            foot=f'<a href="../services/{slc}/">{E(c["service"])} history →</a>' if slc in TRACKED_SLUGS else ""
            return f'<li><article class="card"><div>{tag(k)} <strong>{E(c["service"])}</strong></div><h3><a href="../changes/{c["_art"]}/">{E(c.get("seo_title") or c.get("headline") or "Page updated")}</a></h3><p>{E(c["what"])}</p><div class="foot"><time datetime="{d}">{nice(d)}</time>{foot}</div></article></li>'
        li = "".join(_hist(c,d) for d,c in its)
        sec += f'<h2>{mname}</h2><ul class="cards">{li}</ul>'
    if not sec: sec = f'<p class="empty">No {short.lower()} detected yet since tracking began. This page updates automatically the day one is found.</p>'
    tracked = sorted([n for n,v in s.items() if k in v], key=str.lower)
    tl = " · ".join(f'<a href="../services/{slug(n)}/">{E(n)}</a>' for n in tracked)
    other = " · ".join(f'<a href="../{HUB_FOR[o][0]}">{HUB_FOR[o][1]}</a>' for o in HUBS if o!=k)
    lm = max([c.get("modified",d) for d,c in items] or [(days or [TODAY])[-1]])
    url = f"{SITE}/{fn}"
    ld = {"@context":"https://schema.org","@type":"CollectionPage","name":tt,"url":url,"description":dd,"dateModified":lm,"publisher":ORG,
          "mainEntity":{"@type":"ItemList","numberOfItems":len(items),"itemListElement":[{"@type":"ListItem","position":i+1,"url":f'{SITE}/changes/{c["_art"]}/',"name":c.get("seo_title") or c.get("headline") or c["service"]} for i,(d,c) in enumerate(items)]}}
    nlog = f'{len(items)} change{"s"*(len(items)!=1)} logged'
    body = (f'<p class="kicker">{tag(k)} Tracker</p><h1>{E(tt)}</h1><p class="meta">{nlog} · Updated <time datetime="{lm}">{nice(lm)}</time></p>'
            f'<p class="lede">{E(lede)}</p>{sec}'
            + (f'<h2>Price history by service</h2><p>Full US price histories, every increase with dates and sources: ' + ' · '.join(f'<a href="../services/{slug(n)}/#price-history">{E(PH[n].get("name",n))} price history</a>' for n in PH) + ' · <a href="../subscription-price-history/">All services compared</a></p>' if k=='pricing' and PH else '') + f'<h2>Services we check for {short.lower()}</h2><p>{len(tracked)} services, checked every morning: {tl}</p>'
            f'<h2>More trackers</h2><p>{other} · <a href="../archive.html">Daily reports</a> · <a href="../about.html">How we detect changes</a></p>')
    (D/fn).mkdir(parents=True, exist_ok=True)
    (D/fn/"index.html").write_text(page(fn+"index.html", tt, body, desc=dd, depth=1, ld=ld, lastmod=lm, crumbs=[("Home",SITE+"/")]))
# ---- comparison page: every sourced price history side by side ----
if PH:
    rows=[]
    for n,h in PH.items():
        if not h.get("compare",True): continue
        nm=h.get("name",n); fl=h["plans"][h["flagship"]]; pct=(fl[-1][1]/fl[0][1]-1)*100
        yrs=max(1,int(h["verified"][:4])-int(fl[0][0][:4]))
        rows.append((pct,n,nm,h,fl,yrs))
    rows.sort(key=lambda r:-r[0])
    tr="".join(f'<tr><th scope="row"><a href="../services/{slug(n)}/#price-history">{E(nm)}</a></th><td>{E(h["flagship"])}</td><td>{_amt(h,h["flagship"],fl[0][1])} ({fl[0][0][:4]})</td><td>{_amt(h,h["flagship"],fl[-1][1])}</td><td>+{pct:.0f}%</td><td>{len(fl)-1}</td><td><time datetime="{h["latest"]["date"]}">{_pd(h["latest"]["date"])}</time></td></tr>' for pct,n,nm,h,fl,yrs in rows)
    lm=max(r[3]["verified"] for r in rows)
    top=rows[0]; recent=sorted(rows,key=lambda r:r[3]["latest"]["date"],reverse=True)
    tt=f"Streaming & subscription price history compared ({lm[:4]}): {', '.join(r[2] for r in rows[:4])} and more"
    dd=f"Every US price increase at {len(rows)} major subscriptions side by side: launch price, today's price, total increase and the date of the last hike. {top[2]} {top[3]['flagship']} is up {top[0]:.0f}% since {top[4][0][0][:4]}. Sourced and dated."
    lede=(f"How much have streaming and subscription prices gone up? This table compares the main US plan at {len(rows)} big subscriptions, from launch price to today, using the same sourced, dated price histories that sit on each service page. "
          f"The biggest total increase is {top[2]} {top[3]['flagship']}, up {top[0]:.0f}% since {top[4][0][0][:4]}. The most recent increase was {recent[0][2]} on {_pd(recent[0][3]['latest']['date'])}.")
    lastn="".join(f'<li><strong>{E(r[2])}</strong>, {_pd(r[3]["latest"]["date"])}: {E(r[3]["latest"]["what"])} (<a href="{E(r[3]["latest"]["source"])}">{E(r[3]["latest"]["source_name"])}</a>)</li>' for r in recent)
    faq=[("Which streaming service has raised prices the most?", f"Of the services compared here, {top[2]} {top[3]['flagship']} has gone up the most: from {_amt(top[3],top[3]['flagship'],top[4][0][1])} in {top[4][0][0][:4]} to {_amt(top[3],top[3]['flagship'],top[4][-1][1])}, a {top[0]:.0f}% increase."),
         ("Which subscription raised prices most recently?", f"{recent[0][2]}, on {_pd(recent[0][3]['latest']['date'])}. Before that, {recent[1][2]} on {_pd(recent[1][3]['latest']['date'])}."),
         ("How often do streaming prices go up?", "Most of these services have raised their main plan every one to two years since 2022, often in the summer or fall. Amazon Prime has been the exception, with increases about every four years.")]
    body=(f'<p class="kicker">Price history</p><h1>{E(tt)}</h1><p class="meta">{len(rows)} services · Last verified <time datetime="{lm}">{nice(lm)}</time></p><p class="lede">{E(lede)}</p>'
          f'<h2>Price increases compared (US, main plan)</h2><div class="tablewrap"><table><thead><tr><th scope="col">Service</th><th scope="col">Plan</th><th scope="col">Launch price</th><th scope="col">Price now</th><th scope="col">Total increase</th><th scope="col">Increases</th><th scope="col">Last increase</th></tr></thead><tbody>{tr}</tbody></table></div>'
          f'<p class="meta">US list prices for new subscribers, before tax, not adjusted for inflation. Click a service for every plan, every dated change, and the sources.</p>'
          f'<h2>Latest increase at each service</h2><ul>{lastn}</ul><h2>Quick answers</h2>' + "".join(f"<p><strong>{E(q)}</strong><br>{E(a)}</p>" for q,a in faq) +
          f'<h2>More</h2><p><a href="../price-changes/">Every pricing change we detect, as it happens</a> · <a href="../services.html">All tracked services</a> · <a href="../about.html">How we detect changes</a></p>')
    ld=[{"@context":"https://schema.org","@type":"WebPage","name":tt,"url":f"{SITE}/subscription-price-history/","description":dd,"dateModified":lm,"publisher":ORG},
        {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faq]}]
    (D/"subscription-price-history").mkdir(parents=True, exist_ok=True)
    (D/"subscription-price-history"/"index.html").write_text(page("subscription-price-history/index.html", tt, body, desc=dd, depth=1, ld=ld, lastmod=lm, crumbs=[("Home",SITE+"/"),("Price changes",SITE+"/price-changes/")]))
# ---- Atom feed: daily reports + change articles (newest first) ----
entries = []
for d in days:
    entries.append((d, f'<entry><title>Report, {nice(d)}</title><link href="{SITE}/reports/{d}.html"/><id>{SITE}/reports/{d}.html</id><updated>{d}T12:00:00Z</updated></entry>'))
for d, c, t in ARTS:
    a = c["_art"]; url = f"{SITE}/changes/{a}/"
    entries.append((d, f'<entry><title>{E(t)}</title><link href="{url}"/><id>{url}</id><updated>{d}T12:00:00Z</updated><summary>{E(c.get("what",""))}</summary></entry>'))
entries.sort(key=lambda x: x[0], reverse=True)
feed = "".join(e for _, e in entries)
(D/"feed.xml").write_text(f'<?xml version="1.0" encoding="utf-8"?><feed xmlns="http://www.w3.org/2005/Atom"><title>QuietlyChanged</title><link href="{SITE}/"/><link rel="self" href="{SITE}/feed.xml"/><id>{SITE}/</id><updated>{(days or [TODAY])[-1]}T12:00:00Z</updated>{feed}</feed>')
# ---- evergreen per-service pages ----
def svc_name(k): return k
for k, v in s.items():
    sl = slug(k); (D/"services"/sl).mkdir(parents=True, exist_ok=True)
    snaps = [f.stem for p in v for f in (R/"snapshots"/slug_tr(k)/p).glob("*.txt")] if (R/"snapshots").exists() else []
    last = max(snaps) if snaps else TODAY; first = min(snaps) if snaps else TODAY
    log = [(d, c) for d in reversed(days) for c in data[d] if c["service"] == k]
    _w = [{"pricing":"price","terms":"terms","privacy":"privacy policy"}[p] for p in v]
    kinds = _w[0] if len(_w)==1 else ", ".join(_w[:-1]) + " & " + _w[-1]
    title = f"{k} {kinds} changes (history)"
    phtml, phld, phpct, phfl = ph_section(k, PH[k]) if k in PH else ("", None, 0, None)
    if k in PH:
        title = PH[k].get("title") or f"{PH[k].get('title_name',PH[k].get('name',k))} price history (US, {phfl[0][0][:4]}–{PH[k]['verified'][:4]}): every increase"
    srcs = "".join(f'<li>{tag(p)} <a href="{E(u)}">{E(u)}</a></li>' for p,u in v.items())
    cl = "".join(f'<li><article class="card"><div>{tag(c.get("page","terms"))}</div><h3><a href="../../changes/{c['_art']}/">{E(c.get("headline") or "Page updated")}</a></h3><p>{E(c["what"])}</p><div class="foot"><time datetime="{d}">{nice(d)}</time><a href="{E(c["url"])}">Source →</a></div></article></li>' for d,c in log)
    cl = f'<ul class="cards">{cl}</ul>' if cl else f'<p class="empty">No changes detected since tracking began on {nice(first)}. This page updates automatically when {E(k)} changes a tracked page.</p>'
    others = sorted(s, key=str.lower); i = others.index(k); nb = [others[(i+j)%len(others)] for j in (-1,1)]
    desc = f"A dated history of every change {k} makes to its {kinds} pages, checked daily by QuietlyChanged. Last checked {nice(last)}."
    if k in PH: desc = f"Every {PH[k].get('title_name',PH[k].get('name',k))} US price increase since {phfl[0][0][:4]}: {PH[k]['flagship']} went from {_amt(PH[k],PH[k]['flagship'],phfl[0][1])} to {_amt(PH[k],PH[k]['flagship'],phfl[-1][1])} (+{phpct:.0f}%). Dated tables for each plan, sources, plus daily {kinds} change tracking."
    ld = {"@context":"https://schema.org","@type":"WebPage","name":title,"url":f"{SITE}/services/{sl}/","dateModified":last,"publisher":ORG,"about":{"@type":"Organization","name":k}}
    body = f'''<p class="kicker">Service history</p><h1>{E(title)}</h1><p class="meta">Tracked since <time datetime="{first}">{nice(first)}</time> · Last snapshot <time datetime="{last}">{nice(last)}</time></p>
<p class="lede">QuietlyChanged checks {E(k)}'s public {kinds} pages every day and records what changes, in plain English.</p>
{phtml}<h2>Pages we monitor</h2><ul>{srcs}</ul><h2>Changelog</h2>{cl}
<h2>Related</h2><p><a href="../{slug(nb[0])}/">{E(nb[0])}</a> · <a href="../{slug(nb[1])}/">{E(nb[1])}</a> · <a href="../../services.html">All tracked services</a> · <a href="../../about.html">How it works</a></p>'''
    (D/"services"/sl/"index.html").write_text(page(f"services/{sl}/index.html", title, body, desc=desc, depth=2, ld=([ld, phld] if phld else ld), lastmod=max([last]+[c.get("modified",d) for d,c in log]+([PH[k]["verified"]] if k in PH else [])), crumbs=[("Home",SITE+"/"),("What we track",SITE+"/services.html")]))
# ---- sitemap / robots ----
(D/"sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' + "".join(f"<url><loc>{u}</loc><lastmod>{m}</lastmod></url>" for u,m in {u:(m or TODAY) for u,m in PAGES}.items()) + "</urlset>")
(D/"robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n")
import subprocess, shutil

# ---- IndexNow (Bing/Yandex): key file + ping new/changed URLs ----
INDEXNOW_KEY = (R/"indexnow.key").read_text().strip() if (R/"indexnow.key").exists() else ""
if INDEXNOW_KEY:
    (D/f"{INDEXNOW_KEY}.txt").write_text(INDEXNOW_KEY)
    import os
    if os.environ.get("QC_NO_INDEXNOW"): print("IndexNow ping skipped (QC_NO_INDEXNOW set; ping after deploy)")
    else:
     try:
         import urllib.request
         urls = list(dict.fromkeys(u for u,_ in PAGES))  # unique, order preserved
         # Prefer change articles + latest report + feed/sitemap
         ping = [u for u in urls if "/changes/" in u][-20:]
         if days:
             ping.append(f"{SITE}/reports/{days[-1]}.html")
             ping.append(f"{SITE}/")
         ping.append(f"{SITE}/feed.xml")
         ping += [f"{SITE}/{h[0]}" for h in HUB_FOR.values()]
         ping += [f"{SITE}/services/{slug(n)}/" for n in PH] + ([f"{SITE}/subscription-price-history/"] if PH else [])
         ping = list(dict.fromkeys(ping))
         body = json.dumps({"host":"quietlychanged.com","key":INDEXNOW_KEY,"keyLocation":f"{SITE}/{INDEXNOW_KEY}.txt","urlList":ping}).encode()
         req = urllib.request.Request("https://api.indexnow.org/indexnow", data=body, headers={"Content-Type":"application/json; charset=utf-8"}, method="POST")
         with urllib.request.urlopen(req, timeout=15) as resp:
             print(f"IndexNow: {resp.status} for {len(ping)} URLs")
     except Exception as ex:
         print(f"IndexNow ping skipped: {ex}")

if not (D/"og.png").exists() and shutil.which("google-chrome"):
    subprocess.run(["google-chrome","--headless=new","--no-sandbox","--hide-scrollbars","--window-size=1200,630",f"--screenshot={D/'og.png'}",(D/"og.svg").resolve().as_uri()],capture_output=True)
