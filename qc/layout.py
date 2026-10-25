"""The page shell: <head> (SEO tags unchanged from the original build), header, footer."""
import json
from .util import E, nice

SITE = "https://quietlychanged.com"
TAG = "Daily, plain-English reports on what popular services quietly change in their prices, terms, and privacy policies."
ORG = {"@context": "https://schema.org", "@type": "Organization", "name": "QuietlyChanged", "url": SITE + "/", "logo": SITE + "/og.png"}
NAV = [("index.html", "Today"), ("due-soon/", "Due soon"), ("threads/", "Threads"), ("services.html", "Services"), ("archive.html", "Archive"), ("about.html", "How it works")]
PAGES = []   # (url, lastmod) for the sitemap

ICON_SEARCH = '<svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><circle cx="7" cy="7" r="4.6"/><path d="m10.4 10.4 3.6 3.6" stroke-linecap="round"/></svg>'
ICON_THEME = '<svg viewBox="0 0 16 16" aria-hidden="true"><circle cx="8" cy="8" r="6.2" fill="none" stroke="currentColor" stroke-width="1.5"/><path d="M8 1.8a6.2 6.2 0 0 1 0 12.4z" fill="currentColor"/></svg>'
ICON_STAR = '<svg viewBox="0 0 16 16" aria-hidden="true"><path d="M8 1.6l1.9 4 4.4.5-3.3 3 .9 4.4L8 11.3l-3.9 2.2.9-4.4-3.3-3 4.4-.5z" fill="currentColor"/></svg>'

def _current(fn, h):
    if fn == h: return True
    if h == "services.html" and fn.startswith("services/"): return True
    if h == "archive.html" and fn.startswith("reports/"): return True
    if h.endswith("/") and fn.startswith(h): return True
    return False

def page(fn, title, body=None, today=None, desc=TAG, depth=0, ld=None, otype="website", lastmod=None, crumbs=None, image=None, front=False):
    p = "../" * depth; url = f"{SITE}/{fn}".replace("/index.html", "/")
    PAGES.append((url, lastmod))
    lds = [ORG] + (ld if isinstance(ld, list) else [ld] if ld else [])
    if crumbs: lds.append({"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "item": u} for i, (n, u) in enumerate(crumbs + [(title, url)])]})
    ldh = "".join(f'<script type="application/ld+json">{json.dumps(x)}</script>' for x in lds)
    nav = "".join(f'<a href="{p}{h}"{" aria-current=page" if _current(fn, h) else ""}>{t}</a>' for h, t in NAV)
    full = "QuietlyChanged: daily pricing, terms & privacy policy changes" if fn == "index.html" else f"{title} · QuietlyChanged"
    img = image or f"{SITE}/og.png"
    vis_crumbs = ""
    if crumbs and not front:
        parts = []
        for n, u in crumbs:
            rel = p + (u.replace(SITE + "/", "") or "index.html")
            parts.append(f'<a href="{E(rel)}">{E(n)}</a><span aria-hidden="true">/</span>')
        vis_crumbs = f'<nav class="crumbs wide" aria-label="Breadcrumb" style="padding-top:1.2rem">{"".join(parts)}<span>{E(title if len(title) < 48 else title[:46].rsplit(" ",1)[0] + "…")}</span></nav>'
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{E(full)}</title><meta name="description" content="{E(desc)}"><link rel="canonical" href="{url}">
<meta property="og:type" content="{otype}"><meta property="og:site_name" content="QuietlyChanged"><meta property="og:title" content="{E(full)}"><meta property="og:description" content="{E(desc)}"><meta property="og:url" content="{url}"><meta property="og:image" content="{img}"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta name="twitter:card" content="summary_large_image">{ldh}
<link rel="icon" href="{p}favicon.svg" type="image/svg+xml"><meta name="theme-color" content="#EEF0EC" media="(prefers-color-scheme: light)"><meta name="theme-color" content="#0F1114" media="(prefers-color-scheme: dark)">
<link rel="preload" href="{p}fonts/newsreader-normal-latin.woff2" as="font" type="font/woff2" crossorigin>
<script>try{{var t=localStorage.getItem("qc-theme");if(t)document.documentElement.dataset.theme=t}}catch(e){{}}</script>
<link rel="stylesheet" href="{p}style.css"><link rel="alternate" type="application/atom+xml" href="{p}feed.xml" title="QuietlyChanged"><script src="{p}app.js" defer></script></head>
<body data-root="{p}"><a class="skip" href="#main">Skip to content</a>
<header class="site-head"><div class="wide bar"><a class="brand" href="{p}index.html" aria-label="QuietlyChanged home">Quietly<i>Changed</i></a>
<nav class="nav" aria-label="Main">{nav}</nav>
<div class="tools"><button class="iconbtn" type="button" data-search aria-label="Search">{ICON_SEARCH}<span class="t">Search</span><kbd>/</kbd></button><button class="iconbtn theme-btn" type="button" data-theme-toggle aria-label="Switch light or dark theme">{ICON_THEME}</button></div></div></header>
{vis_crumbs}<main id="main">{body}</main>
<footer class="site-foot"><div class="wide cols">
<div><a class="brand" href="{p}index.html">Quietly<i>Changed</i></a><p style="margin-top:.8rem">An independent record of what popular services change in their prices, terms and privacy policies. We snapshot public pages every morning and explain the differences. Always check the linked source; summaries are not legal advice.</p></div>
<div><h2>Read</h2><ul><li><a href="{p}index.html">Today</a></li><li><a href="{p}due-soon/">Due soon</a></li><li><a href="{p}threads/">Threads</a></li><li><a href="{p}archive.html">Archive</a></li></ul></div>
<div><h2>Trackers</h2><ul><li><a href="{p}price-changes/">Price changes</a></li><li><a href="{p}subscription-price-history/">Price history</a></li><li><a href="{p}terms-of-service-changes/">Terms changes</a></li><li><a href="{p}privacy-policy-changes/">Privacy changes</a></li></ul></div>
<div><h2>About</h2><ul><li><a href="{p}about.html">How it works</a></li><li><a href="{p}services.html">Tracked services</a></li><li><a href="{p}feed.xml">Feed</a></li><li><a href="{p}due-soon/calendar.ics">Deadline calendar</a></li></ul></div>
</div><div class="wide fine"><span>© {today[:4]} QuietlyChanged</span><span>Last checked {nice(today)}</span></div></footer></body></html>'''
