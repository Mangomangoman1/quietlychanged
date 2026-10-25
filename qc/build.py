"""Builds docs/ (GitHub Pages root).

Inputs per day in reports/:
  DATE-summary.md   – headline + lede in light markdown (required)
  DATE-changes.json – list of changes. Required keys: service, page (pricing|terms|privacy), headline, what, who, url.
                      Optional: tldr, impact (1-3), effective (YYYY-MM-DD), deadline (label), themes [slugs],
                      redline [{before, after, label, note, src}], actions [..], faq [[q,a],..], note, sources [[name,url],..],
                      seo_title, seo_desc, modified.
  DATE-raw.md       – the tracker's raw diffs (used for the "full diff" view)
Other inputs: services.json, price_history.json, service_seo.json, themes.json.
See EDITORIAL.md for how to write each field.
"""
import json, pathlib, re, datetime, os, shutil, random
from .util import E, LABEL, IMPACT, slug, slug_tr, art_slug, nice, short, short_y, weekday, days_until, md, plural, date
from .layout import page, PAGES, SITE, TAG, ORG
from .components import kind, impact, mono, stamp, exhibit, mini_bl, entry, clip, due_chip, follow_btn, countdown_text
from .redline import raw_sections
from .structure import structure, render as render_sections
from .charts import step_chart, seismograph, heatmap, bars, CPI_EST
from . import og

R = pathlib.Path(__file__).resolve().parent.parent
D = R / "docs"
HUB_FOR = {"pricing": ("price-changes/", "Price changes"), "terms": ("terms-of-service-changes/", "Terms of service changes"), "privacy": ("privacy-policy-changes/", "Privacy policy changes")}
FAV = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="14" fill="#15181D"/><text x="32" y="44" font-family="Georgia,serif" font-size="36" font-weight="600" text-anchor="middle" fill="#FAFBF8">Q</text><rect x="13" y="30" width="38" height="3.2" rx="1.6" fill="#E0493C"/></svg>'

def load_json(p, default):
    return json.loads(p.read_text()) if p.exists() else default

def write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True); path.write_text(text)

def ics_escape(s): return s.replace("\\", "\\\\").replace(";", "\\;").replace(",", "\\,").replace("\n", "\\n")
def ics_fold(line):
    out = []; b = line.encode()
    while len(b) > 74:
        cut = 74
        while (b[cut] & 0xC0) == 0x80: cut -= 1
        out.append(b[:cut].decode()); b = b" " + b[cut:]
    out.append(b.decode()); return "\r\n".join(out)
def ics_event(c, stamp_dt):
    eff = c["effective"].replace("-", ""); nxt = (date(c["effective"]) + datetime.timedelta(days=1)).isoformat().replace("-", "")
    url = f'{SITE}/changes/{c["_art"]}/'
    lines = ["BEGIN:VEVENT", f'UID:{c["_art"]}@quietlychanged.com', f"DTSTAMP:{stamp_dt}", f"DTSTART;VALUE=DATE:{eff}", f"DTEND;VALUE=DATE:{nxt}",
             "SUMMARY:" + ics_escape(f'{c["service"]}: {c.get("deadline") or "Takes effect"}'),
             "DESCRIPTION:" + ics_escape((c.get("tldr") or c.get("headline", "")) + "\n\n" + url), f"URL:{url}",
             "BEGIN:VALARM", "ACTION:DISPLAY", "TRIGGER:-P1D", "DESCRIPTION:" + ics_escape(f'Tomorrow: {c["service"]} — {c.get("deadline") or "takes effect"}'), "END:VALARM", "END:VEVENT"]
    return lines
def ics_cal(events, name):
    lines = ["BEGIN:VCALENDAR", "VERSION:2.0", "PRODID:-//QuietlyChanged//Deadlines//EN", "CALSCALE:GREGORIAN", "METHOD:PUBLISH", "X-WR-CALNAME:" + ics_escape(name)] + [l for e in events for l in e] + ["END:VCALENDAR"]
    return "\r\n".join(ics_fold(l) for l in lines) + "\r\n"

def main():
    TODAY = os.environ.get("QC_TODAY") or datetime.date.today().isoformat()
    (D / "reports").mkdir(parents=True, exist_ok=True)
    days = sorted(p.name[:10] for p in (R / "reports").glob("*-summary.md"))
    data = {}
    for d in days:
        cj = R / "reports" / f"{d}-changes.json"
        data[d] = json.loads(cj.read_text()) if cj.exists() else []
    s = json.loads((R / "services.json").read_text())
    TRACKED = {slug(k) for k in s}
    PH = {k: v for k, v in load_json(R / "price_history.json", {}).items() if not k.startswith("_")}
    SVC_SEO = {k: v for k, v in load_json(R / "service_seo.json", {}).items() if not k.startswith("_")}
    THEMES = {k: v for k, v in load_json(R / "themes.json", {}).items() if not k.startswith("_")}
    RAW = {d: raw_sections((R / "reports" / f"{d}-raw.md").read_text()) if (R / "reports" / f"{d}-raw.md").exists() else {} for d in days}

    # every change, with its article slug, newest first
    ALL = []
    for d in days:
        for c in data[d]:
            c["_art"] = art_slug(d, c); c["_d"] = d
            c["impact"] = int(c.get("impact") or 1)
            ALL.append((d, c))
    ALL_NEW = list(reversed(ALL))
    svc_href = lambda name, root: f"{root}services/{slug(name)}/" if slug(name) in TRACKED else None
    report_title = {}
    for d in days:
        report_title[d] = (R / "reports" / f"{d}-summary.md").read_text().splitlines()[0].lstrip("# ").strip() or f"Report, {nice(d)}"
    OGIMG = og.build_all(D, R, ALL, TODAY)   # {art_slug: absolute url} for per-change share images

    # ---------- daily report pages ----------
    def report_body(d, root):
        sm = R / "reports" / f"{d}-summary.md"; txt = sm.read_text(); body = md(txt)
        if not txt.lstrip().startswith("# "): body = f"<h1>Report for {nice(d)}</h1>" + body
        first, _, rest = body.partition("</h1>")
        h1 = first.replace("<h1>", "")
        items = data[d]; n = days.index(d)
        head = (f'<header class="wrap page-head"><p class="label">Daily report · No. {n} · <time datetime="{d}">{weekday(d)}</time></p><h1>{h1}</h1>'
                f'<p class="meta">{plural(len(items), "change")} · checked {nice(d)}</p></header>')
        cards = ""
        if items or "Day 0" not in first:
            if items:
                li = "".join(f'<li>{entry(c, d, root, TODAY, title=c["service"] + ": " + (c.get("headline") or LABEL.get(c.get("page","terms")) + " page updated"), svc_href=svc_href(c["service"], root), who=True)}</li>' for c in sorted(items, key=lambda c: -c["impact"]))
                cards = f'<section class="wrap" aria-labelledby="wc"><div class="sec-title"><h2 id="wc">What changed</h2></div><ul class="entries">{li}</ul></section>'
            else:
                cards = '<section class="wrap"><div class="sec-title"><h2>What changed</h2></div><p class="coverage">No meaningful changes detected on tracked pages today.</p></section>'
        prose = f'<section class="wrap section prose" aria-label="Report notes">{rest}</section>' if rest.strip() else ""
        prev_d = days[n - 1] if n > 0 else None; next_d = days[n + 1] if n + 1 < len(days) else None
        dn = (f'<nav class="wrap daynav" aria-label="Other reports">' + (f'<a href="{root}reports/{prev_d}.html">← {E(short(prev_d))}: {E(report_title[prev_d][:60])}</a>' if prev_d else "<span></span>")
              + (f'<a href="{root}reports/{next_d}.html">{E(short(next_d))}: {E(report_title[next_d][:60])} →</a>' if next_d else f'<a href="{root}archive.html">All reports →</a>') + "</nav>")
        return head + cards + prose + dn

    for d in days:
        items = data[d]; svs = sorted({c["service"] for c in items})
        desc = (f"{len(items)} changes on {nice(d)}: " + ", ".join(svs[:6]) + ". Plain-English summaries with source links.") if items else f"QuietlyChanged daily report for {nice(d)}: what popular services changed in their pricing, terms, and privacy pages."
        if d == days[0] and not items: desc = f"Day 0: QuietlyChanged starts tracking {len(s)} popular services' pricing, terms of service, and privacy policies."
        hl = report_title[d]
        ld = {"@context": "https://schema.org", "@type": "NewsArticle", "headline": hl[:110], "datePublished": d + "T06:00:00-06:00", "dateModified": d + "T06:00:00-06:00", "url": f"{SITE}/reports/{d}.html", "image": [SITE + "/og.png"], "author": {"@type": "Organization", "name": "QuietlyChanged", "url": SITE + "/"}, "publisher": ORG, "description": desc}
        write(D / "reports" / f"{d}.html", page(f"reports/{d}.html", f"{hl} ({nice(d)})", report_body(d, "../"), TODAY, desc=desc, depth=1, ld=ld, otype="article", lastmod=d, crumbs=[("Home", SITE + "/"), ("Archive", SITE + "/archive.html")]))

    # ---------- change articles ----------
    def related(c, k=3):
        th = set(c.get("themes", []))
        scored = []
        for d2, o in ALL:
            if o is c: continue
            sc = 0; why = None
            shared = th & set(o.get("themes", []))
            if o["service"] == c["service"]: sc += 5; why = f"More from {o['service']}"
            if shared:
                sc += 3 * len(shared)
                if not why: why = "Same thread · " + THEMES.get(sorted(shared)[0], {}).get("title", "")
            if o.get("page") == c.get("page"): sc += .5
            gap = abs((date(d2) - date(c["_d"])).days)
            if gap <= 4: sc += 1; why = why or "Same week"
            sc += o["impact"] * .8
            scored.append((sc, -gap, o, why or "Also notable"))
        scored.sort(key=lambda x: (-x[0], x[1]))
        out, seen = [], set()
        for sc, _, o, why in scored:
            if o["_art"] in seen: continue
            seen.add(o["_art"]); out.append((o, why))
            if len(out) == k: break
        return out

    for d, c in ALL:
        a = c["_art"]
        t = c.get("seo_title") or f'{c["service"]}: {c.get("headline") or "page updated"}'
        ds = c.get("seo_desc") or (c["what"][:155])
        k = c.get("page", "terms"); sl = slug(c["service"]); has_svc = sl in TRACKED
        ld = {"@context": "https://schema.org", "@type": "NewsArticle", "headline": t[:110], "datePublished": d + "T06:00:00-06:00", "dateModified": c.get("modified", d) + "T06:00:00-06:00", "url": f"{SITE}/changes/{a}/", "image": [OGIMG.get(a, SITE + "/og.png")], "author": {"@type": "Organization", "name": "QuietlyChanged", "url": SITE + "/"}, "publisher": ORG, "description": ds, "about": {"@type": "Organization", "name": c["service"]}}
        if c.get("faq"): ld = [ld, {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": an}} for q, an in c["faq"]]}]
        root = "../../"
        sh = svc_href(c["service"], root)
        when = f"First seen {short(d)}"
        exhibits = "".join(exhibit(r, c["service"], LABEL.get(k, k), when, i) for i, r in enumerate(c.get("redline", [])))
        secs, cov = structure(c["what"])
        body_html = render_sections(secs)
        note_html = f'<aside class="update" role="note"><strong>Update</strong>{E(c["note"])}</aside>' if c.get("note") else ""
        faq_html = ('<h2>Quick answers</h2>' + "".join(f"<h3>{E(q)}</h3><p>{E(an)}</p>" for q, an in c["faq"])) if c.get("faq") else ""
        srcs_html = ("<p>Other sources:</p><ul>" + "".join(f'<li><a href="{E(u)}">{E(n)}</a></li>' for n, u in c["sources"]) + "</ul>") if c.get("sources") else ""
        cov_html = f'<div class="coverage"><span class="label">Who else has reported it{" · " + E(cov[0]) if cov[0] else ""}</span>{E(cov[1])}</div>' if cov else ""
        raw = RAW.get(d, {}).get((c["service"], k))
        diff_html = ""
        if raw:
            lines = raw["diff"].splitlines()
            shown = lines[:400]
            sp = "".join(f'<span class="{"a" if l.startswith("+") else "r" if l.startswith("-") else "h" if l.startswith("@@") else ""}">{E(l[1:] if l[:1] in "+- " and not l.startswith("@@") else ("· · ·" if l.startswith("@@") else l)) or " "}</span>' for l in shown)
            more = f'<span class="h">… {len(lines) - 400} more lines in the raw report</span>' if len(lines) > 400 else ""
            prev = days[days.index(d) - 1] if days.index(d) > 0 else None
            diff_html = (f'<details class="diff"><summary>Full diff from our snapshots <span class="mono muted" style="font-size:.75rem">+{raw["add"]} / −{raw["rem"]} lines</span></summary><pre class="diffview">{sp}{more}</pre></details>')
        prov = (f'<p class="prov">Provenance: detected in our {E(short(d))} snapshot of the {E(c["service"])} {LABEL.get(k,k).lower()} page' + (f', compared against {E(short(days[days.index(d)-1]))}' if raw and days.index(d) > 0 else "") +
                ('. Excerpts marked "Quoted from the documents" come from the sources linked above.' if any(r.get("src") == "quoted" for r in c.get("redline", [])) else ".") + "</p>")
        more_svc = (f'<a href="../../services/{sl}/#price-history">{E(c["service"])} price history: every increase, with dates</a> · ' if has_svc and c["service"] in PH else "") + (f'<a href="../../services/{sl}/">Full {E(c["service"])} change history</a> · ' if has_svc else "")
        rel = related(c)
        rail = "".join(f'<li><a class="rc" href="../../changes/{o["_art"]}/"><span class="why">{E(why)}</span><b>{E(o["service"])}: {E(o.get("headline",""))}</b><span class="metarow">{kind(o.get("page","terms"))}{impact(o["impact"])}</span></a></li>' for o, why in rel)
        acts = c.get("actions") or []
        aside = ""
        if acts: aside += '<section class="box"><h2>What you can do</h2><ul class="todo">' + "".join(f"<li>{E(x)}</li>" for x in acts) + "</ul></section>"
        tools = []
        if c.get("effective") and days_until(c["effective"], TODAY) >= 0:
            tools.append(f'<a class="btn" href="../../due-soon/{a}.ics">Add the date to your calendar</a>')
        if has_svc: tools.append(follow_btn(c["service"]))
        tools.append('<button class="btn" type="button" data-copy>Copy link</button>')
        aside += f'<section class="box"><h2>Keep track</h2><div class="btnrow">{"".join(tools)}</div></section>'
        if c.get("themes"):
            aside += '<section class="box"><h2>Part of</h2><ul class="chips">' + "".join(f'<li><a href="../../threads/{th}/">{E(THEMES[th]["title"])}</a></li>' for th in c["themes"] if th in THEMES) + "</ul></section>"
        head = (f'<header class="wide art-head"><div class="metarow">{mono(c["service"], sh)}{kind(k)}' + (f'<a class="svc" href="{sh}">{E(c["service"])}</a>' if sh else f'<span class="svc">{E(c["service"])}</span>') +
                f'{impact(c["impact"])}<time datetime="{d}">{E(short_y(d))}</time></div><h1>{E(t)}</h1>' + (f'<p class="lede">{E(c["tldr"])}</p>' if c.get("tldr") else "") + stamp(c, TODAY) + "</header>")
        main_col = (f'<div class="art-main">' + (f'<section aria-labelledby="w"><h2 class="sr" id="w">The wording</h2>{exhibits}<div class="legend-bl"><span class="bl"><del>struck</del></span> removed <span class="bl"><ins>underlined</ins></span> added</div></section>' if exhibits else "") +
                    f'<div class="prose" style="margin-top:{"2.2rem" if exhibits else "0"}">{note_html}' + ('<h2>What changed</h2>' if c.get("tldr") or exhibits else "") +
                    (body_html if c.get("tldr") or exhibits else f'<p class="lede">{E(c["what"])}</p>' if len(secs) <= 1 else body_html) +
                    f'<h2>Who it affects</h2><p>{E(c.get("who","All users"))}</p>{faq_html}{cov_html}'
                    f'<h2>Source</h2><p>Detected on the {E(c["service"])} {LABEL.get(k,k).lower()} page: <a href="{E(c["url"])}">{E(c["url"])}</a>. Always check the source; this summary is not legal or financial advice.</p>{srcs_html}{diff_html}{prov}</div></div>')
        body = (head + f'<div class="wide art-grid">{main_col}<aside class="art-aside" aria-label="Actions">{aside}</aside></div>'
                f'<section class="wide section" aria-labelledby="kr"><div class="sec-title"><h2 id="kr">Keep reading</h2><button class="btn" type="button" data-another>Show me another quiet change ↻</button></div><ul class="rail">{rail}</ul>'
                f'<p class="linkline" style="margin-top:1.4rem">{more_svc}<a href="../../{HUB_FOR[k][0]}">All {HUB_FOR[k][1].lower()}</a> · <a href="../../reports/{d}.html">Report for {nice(d)}</a> · <a href="../../archive.html">All reports</a></p></section>')
        crumbs = [("Home", SITE + "/"), (HUB_FOR.get(k, ("", ""))[1] or "Changes", f"{SITE}/{HUB_FOR.get(k, ('archive.html', ''))[0]}")]
        if has_svc: crumbs.append((c["service"], f"{SITE}/services/{sl}/"))
        write(D / "changes" / a / "index.html", page(f"changes/{a}/index.html", t, body, TODAY, desc=ds, depth=2, ld=ld, otype="article", lastmod=c.get("modified", d), crumbs=crumbs, image=OGIMG.get(a)))

    # ---------- deadlines ----------
    dated = [(d, c) for d, c in ALL if c.get("effective")]
    upcoming = sorted([x for x in dated if days_until(x[1]["effective"], TODAY) >= 0], key=lambda x: x[1]["effective"])
    recent_past = sorted([x for x in dated if -45 <= days_until(x[1]["effective"], TODAY) < 0], key=lambda x: x[1]["effective"], reverse=True)
    stamp_dt = datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    for d, c in dated:
        write(D / "due-soon" / f'{c["_art"]}.ics', ics_cal([ics_event(c, stamp_dt)], f'{c["service"]} · QuietlyChanged'))
    write(D / "due-soon" / "calendar.ics", ics_cal([ics_event(c, stamp_dt) for d, c in dated], "QuietlyChanged deadlines"))

    def due_card(c, root):
        n = days_until(c["effective"], TODAY)
        return (f'<a class="dc{" hot" if 0 <= n <= 7 else ""}" href="{root}changes/{c["_art"]}/"><span class="d">{E(short(c["effective"]))} · {E(c.get("deadline") or "Takes effect")}</span>'
                f'<span class="n" data-days="{c["effective"]}">{max(n,0)}<small>{"day" if n == 1 else "days"}</small></span><span class="s">{E(c["service"])}</span><p>{E(clip(c.get("tldr") or c.get("headline",""), 110))}</p></a>')

    def due_row(c, root, past=False):
        n = days_until(c["effective"], TODAY)
        num = f'{abs(n)}<small>{"day" if abs(n)==1 else "days"} {"ago" if past else "to go"}</small>' if n != 0 else '0<small>today</small>'
        btn = "" if past else f'<a class="btn" href="{root}due-soon/{c["_art"]}.ics">Add to calendar</a>'
        return (f'<li class="{"past" if past else "hot" if n <= 7 else ""}"><span class="n">{num}</span><div><div class="metarow">{kind(c.get("page","terms"))}<span class="svc">{E(c["service"])}</span><span class="when">{E(c.get("deadline") or "Takes effect")} {E(short_y(c["effective"]))}</span></div>'
                f'<h3><a href="{root}changes/{c["_art"]}/">{E(c.get("headline",""))}</a></h3><p>{E(c.get("tldr",""))}</p></div>{btn}</li>')
    body = (f'<header class="wide page-head"><p class="label">Due soon</p><h1>Dates that matter in the fine print</h1>'
            f'<p class="lede">Every deadline, start date and shutdown we have found in a change: when new terms take effect, when a feature disappears, when you have to act. Counted from today.</p>'
            f'<div class="btnrow" style="margin-top:1.2rem"><a class="btn solid" href="calendar.ics">Subscribe to every deadline (.ics)</a><a class="btn" href="../threads/">Browse threads</a></div></header>'
            f'<section class="wide section" style="margin-top:1rem"><div class="sec-title"><h2>Coming up</h2><span class="label">{plural(len(upcoming), "date")}</span></div>'
            + (f'<ul class="duelist">{"".join(due_row(c, "../") for d, c in upcoming)}</ul>' if upcoming else '<p class="coverage">Nothing scheduled right now.</p>') + "</section>"
            + (f'<section class="wide section"><div class="sec-title"><h2>Recently passed</h2></div><ul class="duelist">{"".join(due_row(c, "../", True) for d, c in recent_past)}</ul></section>' if recent_past else ""))
    write(D / "due-soon" / "index.html", page("due-soon/index.html", "Due soon: upcoming deadlines in terms, prices and privacy policies", body, TODAY, depth=1,
          desc="Upcoming dates from the changes QuietlyChanged has caught: new terms taking effect, price increases, shutdowns and opt-out windows, with calendar files.",
          ld={"@context": "https://schema.org", "@type": "CollectionPage", "name": "Due soon", "url": f"{SITE}/due-soon/", "publisher": ORG}, lastmod=TODAY, crumbs=[("Home", SITE + "/")]))

    # ---------- threads ----------
    by_theme = {th: [(d, c) for d, c in ALL_NEW if th in c.get("themes", [])] for th in THEMES}
    def thread_card(th, root, short_ver=False):
        v = THEMES[th]; its = by_theme[th]
        who = " · ".join(dict.fromkeys(c["service"] for _, c in its))
        return (f'<a class="th" href="{root}threads/{th}/"><span class="ct">{plural(len(its), "change")}</span><h3>{E(v["title"])}</h3><p>{E(v["dek"])}</p>'
                + (f'<span class="who">{E(clip(who, 80))}</span>' if who else "") + "</a>")
    for th, v in THEMES.items():
        its = by_theme[th]
        intro = "".join(f"<p>{E(p)}</p>" for p in v["intro"].split("\n\n"))
        li = "".join(f'<li class="i{c["impact"]}">{entry(c, d, "../../", TODAY, svc_href=svc_href(c["service"], "../../"))}</li>' for d, c in its)
        svcs = list(dict.fromkeys(c["service"] for _, c in its))
        others = "".join(thread_card(o, "../../") for o in THEMES if o != th)
        body = (f'<header class="wrap page-head"><p class="label">Thread · {plural(len(its), "change")}</p><h1>{E(v["title"])}</h1><p class="lede">{E(v["dek"])}</p></header>'
                f'<div class="wrap prose">{intro}</div>'
                + (f'<div class="wrap" style="margin-top:1.4rem"><ul class="chips">' + "".join(f'<li><a href="../../services/{slug(n)}/">{mono(n)}{E(n)}</a></li>' if slug(n) in TRACKED else f'<li><span class="chips-static">{E(n)}</span></li>' for n in svcs) + "</ul></div>" if svcs else "")
                + f'<section class="wrap section"><div class="sec-title"><h2>Every change in this thread</h2><span class="label">Newest first</span></div>'
                + (f'<ul class="timeline">{li}</ul>' if li else '<p class="coverage">Nothing yet. This page updates the day one is found.</p>') + "</section>"
                + f'<section class="wide section"><div class="sec-title"><h2>Other threads</h2></div><div class="threads">{others}</div></section>')
        lm = max([c.get("modified", d) for d, c in its] or [TODAY])
        ldd = {"@context": "https://schema.org", "@type": "CollectionPage", "name": v["title"], "url": f"{SITE}/threads/{th}/", "description": v["dek"], "publisher": ORG,
               "mainEntity": {"@type": "ItemList", "numberOfItems": len(its), "itemListElement": [{"@type": "ListItem", "position": i + 1, "url": f'{SITE}/changes/{c["_art"]}/'} for i, (d, c) in enumerate(its)]}}
        write(D / "threads" / th / "index.html", page(f"threads/{th}/index.html", f'{v["title"]}: every change we have tracked', body, TODAY, depth=2,
              desc=f'{v["dek"]} A dated, sourced list of {plural(len(its), "change")} across companies, from QuietlyChanged.', ld=ldd, lastmod=lm, crumbs=[("Home", SITE + "/"), ("Threads", SITE + "/threads/")]))
    body = (f'<header class="wide page-head"><p class="label">Threads</p><h1>The stories behind the changes</h1><p class="lede">One company changing its terms is news. Several doing the same thing is a pattern. Threads follow those patterns across every service we watch.</p></header>'
            f'<section class="wide" style="margin-top:1rem"><div class="threads">{"".join(thread_card(th, "../") for th in THEMES)}</div></section>')
    write(D / "threads" / "index.html", page("threads/index.html", "Threads: patterns across company terms and pricing changes", body, TODAY, depth=1,
          desc="Cross-company threads from QuietlyChanged: forced arbitration, AI and your data, ads and tracking, shutdowns, fees, and more.",
          ld={"@context": "https://schema.org", "@type": "CollectionPage", "name": "Threads", "url": f"{SITE}/threads/", "publisher": ORG}, lastmod=TODAY, crumbs=[("Home", SITE + "/")]))

    # ---------- price history helpers (shared by service pages, hubs, comparison) ----------
    def _pd(x): return x if len(x) == 4 else datetime.date.fromisoformat(x).strftime("%b %-d, %Y") if len(x) == 10 else datetime.date.fromisoformat(x + "-01").strftime("%b %Y")
    def _cur(rows): return rows[-1][1]
    def _chg(p, q):
        dlt = p - q; sg = "+" if dlt >= 0 else "−"; return f"{sg}${abs(dlt):.2f} ({sg}{abs(p/q-1)*100:.0f}%)"
    def _u(h, pl): return h.get("units", {}).get(pl, "month")
    def _amt(h, pl, p): return f"${p:.2f}/{_u(h,pl)}" if p != int(p) or _u(h, pl) == "month" else f"${p:.0f}/{_u(h,pl)}"
    def ph_section(k, h):
        k = h.get("name", k); tk = h.get("title_name", k)
        first_year = min(r[0][:4] for rows in h["plans"].values() for r in rows)
        tabs = ""
        for plan, rows in h["plans"].items():
            tr = "".join(f'<tr><td><time datetime="{r[0]}">{_pd(r[0])}</time></td><td class="num">{_amt(h,plan,r[1]).split("/")[0]}</td><td>{(_chg(r[1],rows[i-1][1]) + ". " + E(r[2]) if i>0 and r[1]!=rows[i-1][1] else E(r[2])) if len(r)>2 else "Launch" if i==0 else _chg(r[1],rows[i-1][1])}</td></tr>' for i, r in enumerate(rows))
            tabs += f'<h3>{E(k)} {E(plan)}</h3><div class="tablewrap"><table><thead><tr><th scope="col">Effective</th><th scope="col" class="num">Price / {_u(h,plan)}</th><th scope="col">Change</th></tr></thead><tbody>{tr}</tbody></table></div>'
        now = "".join(f'<li><span>{E(pl)}</span><b>{_amt(h,pl,_cur(r)).split("/")[0]}</b><small>per {_u(h,pl)}</small></li>' for pl, r in h["plans"].items() if "discontinued" not in pl)
        L = h["latest"]; fl = h["plans"][h["flagship"]]
        notes = "".join(f"<li>{E(n)}</li>" for n in h.get("notes", []))
        srcs = "".join(f'<li><a href="{E(u)}">{E(n)}</a></li>' for n, u in h["sources"])
        svg, infl = step_chart(fl, _u(h, h["flagship"]), TODAY, label=f'{k} {h["flagship"]}')
        chart = ""
        if svg:
            est = ", latest year estimated" if any(y in CPI_EST for y in range(int(fl[0][0][:4]), int(TODAY[:4]) + 1)) else ""
            chart = (f'<figure class="chart chartbox" style="margin-top:1.4rem">{svg}<figcaption>Solid line: {E(k)} {E(h["flagship"])}, US list price for new subscribers. Dashed line: the first price grown with U.S. consumer prices (CPI-U annual averages{est}). '
                     + (f'{E(k)} is up {(fl[-1][1]/fl[0][1]-1)*100:.0f}%; inflation over the same period is about {(infl/fl[0][1]-1)*100:.0f}%.' if infl else "") + '</figcaption></figure>')
        html_ = (f'<h2 id="price-history">{E(tk)} price history (US, {first_year} to {h["verified"][:4]})</h2><p>{E(h["intro"])}</p>{chart}'
                 f'<h3>What {E(k)} costs now</h3><ul class="plans">{now}</ul><div class="update"><strong>Latest change</strong>On {_pd(L["date"])}, {E(L["what"])} (<a href="{E(L["source"])}">{E(L["source_name"])}</a>)</div>'
                 f'{tabs}' + (f'<ul class="cap">{notes}</ul>' if notes else "") +
                 f'<p class="cap">{E(h["basis"].format(verified=nice(h["verified"]))) if h.get("basis") else "US list prices for new monthly subscribers, before tax, in nominal dollars. Compiled from the sources below and last verified " + nice(h["verified"]) + "."} Spotted an error? The sources are linked so you can check.</p><h3>Sources</h3><ul class="cap">{srcs}</ul><p><a href="../../subscription-price-history/">' + (f'Compare {E(k)} with other streaming and subscription price increases' if h.get("compare", True) else 'Compare streaming and subscription price increases') + '</a> · <a href="../../price-changes/">All price changes we track</a></p>')
        pct = (fl[-1][1] / fl[0][1] - 1) * 100
        faq = [(f"How much does {k} cost per month in the US?", "As of " + nice(h["verified"]) + ", " + "; ".join(f"{pl} is {_amt(h,pl,_cur(r))}" for pl, r in h["plans"].items() if "discontinued" not in pl) + "."),
               (f"When did {k} last raise prices?", h.get("faq_last") or f"On {_pd(L['date'])}: {L['what']}"),
               (f"How much has {k} gone up?", f"{k} {h['flagship']} went from {_amt(h,h['flagship'],fl[0][1])} {'on' if len(fl[0][0])==10 else 'in'} {_pd(fl[0][0])} to {_amt(h,h['flagship'],fl[-1][1])}, an increase of {pct:.0f}% across {len(fl)-1} price change{'s'*(len(fl)!=2)}." if not h.get("faq_up") else h["faq_up"])]
        html_ += '<h3>Quick answers</h3>' + "".join(f"<p><strong>{E(q)}</strong><br>{E(an)}</p>" for q, an in faq)
        ld = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": an}} for q, an in faq]}
        return html_, ld, pct, fl

    # ---------- evergreen category hubs ----------
    HUBS = {
     "pricing": ("Subscription price increases & pricing changes in {Y} (tracker)", "Every price increase, new fee, plan limit, and pricing-page change QuietlyChanged has detected at popular subscriptions and apps in {Y}, dated and linked to the source.",
                 "Price hikes rarely come with a press release. They show up as a new number on a pricing page, a fee line on a support page, or a plan that quietly loses a feature. This page collects every pricing change our daily check has caught, newest first, with the date we saw it and a link to the source."),
     "terms": ("Terms of service changes in {Y}: dated tracker", "A dated list of every terms of service, user agreement, and contract change QuietlyChanged has detected at popular apps, banks, and services in {Y}, with plain-English summaries.",
               "Terms of service updates decide what you can dispute, what a company can do with your money, and how disagreements get settled. This page lists every terms change our daily check has caught, newest first, in plain English with a link to the source text."),
     "privacy": ("Privacy policy changes in {Y}: dated tracker", "A dated list of every privacy policy change QuietlyChanged detects at popular apps and services in {Y}: new data uses, sharing, AI training, and retention changes.",
                 "Privacy policies change more often than most people realize, and the edits that matter (new data sharing, AI training, longer retention) are usually buried in long documents. This page lists every privacy policy change our daily check catches, newest first, with a link to the source."),
    }
    for k, (tt, dd, lede) in HUBS.items():
        fn, short_n = HUB_FOR[k]; Y = TODAY[:4]; tt = tt.format(Y=Y); dd = dd.format(Y=Y)
        items = [(d, c) for d in reversed(days) for c in data[d] if c.get("page", "terms") == k]
        by_month = {}
        for d, c in items: by_month.setdefault(d[:7], []).append((d, c))
        sec = ""
        for m, its in by_month.items():
            mname = datetime.date.fromisoformat(m + "-01").strftime("%B %Y")
            li = "".join(f'<li>{entry(c, d, "../", TODAY, title=c.get("seo_title") or c.get("headline") or "Page updated", svc_href=svc_href(c["service"], "../"))}</li>' for d, c in its)
            sec += f'<section class="wrap section" style="margin-top:2.4rem"><div class="sec-title"><h2>{mname}</h2><span class="label">{plural(len(its), "change")}</span></div><ul class="entries">{li}</ul></section>'
        if not sec: sec = f'<div class="wrap"><p class="coverage">No {short_n.lower()} detected yet since tracking began. This page updates automatically the day one is found.</p></div>'
        tracked = sorted([n for n, v in s.items() if k in v], key=str.lower)
        tl = "".join(f'<li><a href="../services/{slug(n)}/">{E(n)}</a></li>' for n in tracked)
        other = " · ".join(f'<a href="../{HUB_FOR[o][0]}">{HUB_FOR[o][1]}</a>' for o in HUBS if o != k)
        lm = max([c.get("modified", d) for d, c in items] or [(days or [TODAY])[-1]])
        url = f"{SITE}/{fn}"
        ld = {"@context": "https://schema.org", "@type": "CollectionPage", "name": tt, "url": url, "description": dd, "dateModified": lm, "publisher": ORG,
              "mainEntity": {"@type": "ItemList", "numberOfItems": len(items), "itemListElement": [{"@type": "ListItem", "position": i + 1, "url": f'{SITE}/changes/{c["_art"]}/', "name": c.get("seo_title") or c.get("headline") or c["service"]} for i, (d, c) in enumerate(items)]}}
        nlog = f'{len(items)} change{"s"*(len(items)!=1)} logged'
        body = (f'<header class="wrap page-head"><div class="metarow">{kind(k)}<span class="label">Tracker</span></div><h1>{E(tt)}</h1><p class="meta">{nlog} · Updated <time datetime="{lm}">{nice(lm)}</time></p><p class="lede">{E(lede)}</p></header>'
                f'{sec}'
                + (f'<section class="wrap section"><div class="sec-title"><h2>Price history by service</h2><a href="../subscription-price-history/">All services compared →</a></div><p class="linkline">Full US price histories, every increase with dates and sources: ' + ' · '.join(f'<a href="../services/{slug(n)}/#price-history">{E(PH[n].get("name",n))} price history</a>' for n in PH) + '</p></section>' if k == 'pricing' and PH else '')
                + f'<section class="wrap section"><div class="sec-title"><h2>Services we check for {short_n.lower()}</h2><span class="label">{len(tracked)} services</span></div><p class="linkline" style="margin-bottom:.8rem">Checked every morning:</p><ul class="chips">{tl}</ul></section>'
                f'<section class="wrap section"><div class="sec-title"><h2>More trackers</h2></div><p class="linkline">{other} · <a href="../threads/">Threads</a> · <a href="../archive.html">Daily reports</a> · <a href="../about.html">How we detect changes</a></p></section>')
        write(D / fn / "index.html", page(fn + "index.html", tt, body, TODAY, desc=dd, depth=1, ld=ld, lastmod=lm, crumbs=[("Home", SITE + "/")]))

    # ---------- comparison page ----------
    cmp_rows = []
    if PH:
        rows = []
        for n, h in PH.items():
            if not h.get("compare", True): continue
            nm = h.get("name", n); fl = h["plans"][h["flagship"]]; pct = (fl[-1][1] / fl[0][1] - 1) * 100
            yrs = max(1, int(h["verified"][:4]) - int(fl[0][0][:4]))
            h = dict(h, latest=h.get("last_up", h["latest"]), _ups=sum(1 for i in range(1, len(fl)) if fl[i][1] > fl[i - 1][1]))
            rows.append((pct, n, nm, h, fl, yrs))
        rows.sort(key=lambda r: -r[0]); cmp_rows = rows
        tr = "".join(f'<tr><th scope="row"><a href="../services/{slug(n)}/#price-history">{E(nm)}</a></th><td>{E(h["flagship"])}</td><td class="num">{_amt(h,h["flagship"],fl[0][1])} ({fl[0][0][:4]})</td><td class="num">{_amt(h,h["flagship"],fl[-1][1])}</td><td class="num up">+{pct:.0f}%</td><td class="num">{h["_ups"]}</td><td><time datetime="{h["latest"]["date"]}">{_pd(h["latest"]["date"])}</time></td></tr>' for pct, n, nm, h, fl, yrs in rows)
        lm = max(r[3]["verified"] for r in rows)
        top = rows[0]; recent = sorted(rows, key=lambda r: r[3]["latest"]["date"], reverse=True)
        tt = f"Streaming & subscription price history compared ({lm[:4]}): {', '.join(r[2] for r in rows[:4])} and more"
        dd = f"Every US price increase at {len(rows)} major subscriptions side by side: launch price, today's price, total increase and the date of the last hike. {top[2]} {top[3]['flagship']} is up {top[0]:.0f}% since {top[4][0][0][:4]}. Sourced and dated."
        lede = (f"How much have streaming and subscription prices gone up? This table compares the main US plan at {len(rows)} big subscriptions, from launch price to today, using the same sourced, dated price histories that sit on each service page. "
                f"The biggest total increase is {top[2]} {top[3]['flagship']}, up {top[0]:.0f}% since {top[4][0][0][:4]}. The most recent increase was {recent[0][2]} on {_pd(recent[0][3]['latest']['date'])}.")
        lastn = "".join(f'<li><strong>{E(r[2])}</strong>, {_pd(r[3]["latest"]["date"])}: {E(r[3]["latest"]["what"])} (<a href="{E(r[3]["latest"]["source"])}">{E(r[3]["latest"]["source_name"])}</a>)</li>' for r in recent)
        faq = [("Which streaming service has raised prices the most?", f"Of the services compared here, {top[2]} {top[3]['flagship']} has gone up the most: from {_amt(top[3],top[3]['flagship'],top[4][0][1])} in {top[4][0][0][:4]} to {_amt(top[3],top[3]['flagship'],top[4][-1][1])}, a {top[0]:.0f}% increase."),
               ("Which subscription raised prices most recently?", f"{recent[0][2]}, on {_pd(recent[0][3]['latest']['date'])}. Before that, {recent[1][2]} on {_pd(recent[1][3]['latest']['date'])}."),
               ("How often do streaming prices go up?", "Most of these services have raised their main plan every one to two years since 2022, often in the summer or fall. Amazon Prime has been the exception, with increases about every four years.")]
        barlist = bars([(f'{r[2]}', f'../services/{slug(r[1])}/#price-history', r[0]) for r in rows])
        body = (f'<header class="wrap page-head"><p class="label">Price history</p><h1>{E(tt)}</h1><p class="meta">{len(rows)} services · Last verified <time datetime="{lm}">{nice(lm)}</time></p><p class="lede">{E(lede)}</p></header>'
                f'<section class="wrap section" style="margin-top:1.6rem"><div class="sec-title"><h2>Total increase since launch</h2><span class="label">Main US plan</span></div>{barlist}</section>'
                f'<section class="wide section"><div class="wrap" style="padding:0;max-width:none"><div class="sec-title"><h2>Price increases compared (US, main plan)</h2></div></div><div class="tablewrap"><table><thead><tr><th scope="col">Service</th><th scope="col">Plan</th><th scope="col" class="num">Launch price</th><th scope="col" class="num">Price now</th><th scope="col" class="num">Total increase</th><th scope="col" class="num">Increases</th><th scope="col">Last increase</th></tr></thead><tbody>{tr}</tbody></table></div>'
                f'<p class="cap">US list prices for new subscribers, before tax, not adjusted for inflation. Click a service for every plan, every dated change, and the sources.</p></section>'
                f'<section class="wrap section prose"><h2>Latest increase at each service</h2><ul>{lastn}</ul><h2>Quick answers</h2>' + "".join(f"<p><strong>{E(q)}</strong><br>{E(an)}</p>" for q, an in faq) +
                f'<h2>More</h2><p><a href="../price-changes/">Every pricing change we detect, as it happens</a> · <a href="../services.html">All tracked services</a> · <a href="../about.html">How we detect changes</a></p></section>')
        ld = [{"@context": "https://schema.org", "@type": "WebPage", "name": tt, "url": f"{SITE}/subscription-price-history/", "description": dd, "dateModified": lm, "publisher": ORG},
              {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": an}} for q, an in faq]}]
        write(D / "subscription-price-history" / "index.html", page("subscription-price-history/index.html", tt, body, TODAY, desc=dd, depth=1, ld=ld, lastmod=lm, crumbs=[("Home", SITE + "/"), ("Price changes", SITE + "/price-changes/")]))

    # ---------- service dossiers ----------
    svc_stats = {}
    for k_, v in s.items():
        log = [(d, c) for d, c in ALL_NEW if c["service"] == k_]
        svc_stats[k_] = log
    for k, v in s.items():
        sl = slug(k)
        snaps = [f.stem for p in v for f in (R / "snapshots" / slug_tr(k) / p).glob("*.txt")] if (R / "snapshots").exists() else []
        last = max(snaps) if snaps else TODAY; first = min(snaps) if snaps else TODAY
        log = svc_stats[k]
        _w = [{"pricing": "price", "terms": "terms", "privacy": "privacy policy"}[p] for p in v]
        kinds = _w[0] if len(_w) == 1 else ", ".join(_w[:-1]) + " & " + _w[-1]
        title = f"{k} {kinds} changes (history)"
        phtml, phld, phpct, phfl = ph_section(k, PH[k]) if k in PH else ("", None, 0, None)
        if k in PH:
            title = PH[k].get("title") or f"{PH[k].get('title_name',PH[k].get('name',k))} price history (US, {phfl[0][0][:4]}–{PH[k]['verified'][:4]}): every increase"
        if k in SVC_SEO: title = SVC_SEO[k].get("title", title)
        last_by_kind = {}
        for d, c in log: last_by_kind.setdefault(c.get("page", "terms"), d)
        watch = "".join(f'<li>{kind(p)}<a href="{E(u)}" rel="nofollow noopener">{E(u)}</a><span class="when">' + (f'last changed {E(short_y(last_by_kind[p]))}' if p in last_by_kind else f'no change since {E(short(first))}') + '</span></li>' for p, u in v.items())
        cl = "".join(f'<li class="i{c["impact"]}">{entry(c, d, "../../", TODAY, show_service=False)}</li>' for d, c in log)
        cl = f'<ul class="timeline">{cl}</ul>' if cl else f'<p class="coverage">No changes detected since tracking began on {nice(first)}. This page updates automatically when {E(k)} changes a tracked page.</p>'
        others = sorted(s, key=str.lower); i = others.index(k); nb = [others[(i + j) % len(others)] for j in (-1, 1)]
        desc = f"A dated history of every change {k} makes to its {kinds} pages, checked daily by QuietlyChanged. Last checked {nice(last)}."
        if k in PH and PH[k].get("desc"): desc = PH[k]["desc"]
        if k in SVC_SEO and SVC_SEO[k].get("desc"): desc = SVC_SEO[k]["desc"]
        elif k in PH: desc = f"Every {PH[k].get('title_name',PH[k].get('name',k))} US price increase since {phfl[0][0][:4]}: {PH[k]['flagship']} went from {_amt(PH[k],PH[k]['flagship'],phfl[0][1])} to {_amt(PH[k],PH[k]['flagship'],phfl[-1][1])} (+{phpct:.0f}%). Dated tables for each plan, sources, plus daily {kinds} change tracking."
        ld = {"@context": "https://schema.org", "@type": "WebPage", "name": title, "url": f"{SITE}/services/{sl}/", "dateModified": last, "publisher": ORG, "about": {"@type": "Organization", "name": k}}
        _fqs = [(d, c) for d, c in log if c.get("faq")][:2]  # the two most recent changes with Quick answers
        svc_faq = "".join(f'<h2>What changed recently: {E(c_.get("headline",""))}</h2>' + "".join(f"<p><strong>{E(q)}</strong><br>{E(an)}</p>" for q, an in c_["faq"]) + f'<p><a href="../../changes/{c_["_art"]}/">Read the full breakdown, with sources</a></p>' for _, c_ in _fqs)
        latest_rl = next(((d, c) for d, c in log if c.get("redline")), None)
        latest_ex = ""
        if latest_rl:
            d0, c0 = latest_rl
            latest_ex = (f'<section class="section" aria-labelledby="lw"><div class="sec-title"><h2 id="lw">Latest change, word for word</h2><a href="../../changes/{c0["_art"]}/">Read it →</a></div>'
                         f'<p class="lede" style="font-size:1.15rem;margin-bottom:1rem"><a href="../../changes/{c0["_art"]}/" style="text-decoration:none">{E(c0.get("headline",""))}</a></p>{exhibit(c0["redline"][0], k, LABEL.get(c0.get("page","terms")), "First seen " + short(d0))}</section>')
        upcoming_svc = [(d, c) for d, c in log if c.get("effective") and days_until(c["effective"], TODAY) >= 0]
        due_html = "".join(f'<div style="margin-top:1rem"><a href="../../changes/{c["_art"]}/" style="text-decoration:none">{stamp(c, TODAY)}</a></div>' for d, c in upcoming_svc[:2])
        facts = [(nice(first).rsplit(",", 1)[0], "tracked since"), (str(len(log)), "changes logged"), (str(len(v)), "pages watched"), (short(log[0][0]) if log else "—", "last change")]
        if k in PH:
            h = PH[k]; fl = phfl
            ups = sum(1 for i2 in range(1, len(fl)) if fl[i2][1] > fl[i2 - 1][1])
            facts = [(_amt(h, h["flagship"], fl[-1][1]).split("/")[0], f'{h["flagship"]}, per {_u(h,h["flagship"])}'), (f"+{phpct:.0f}%", f"since {fl[0][0][:4]}"), (str(ups), "price increases"), (str(len(log)), "changes logged since Oct 13" if first == "2026-10-13" else "changes logged")]
        facts_html = '<div class="facts">' + "".join(f"<div><b>{E(a)}</b><span>{E(b)}</span></div>" for a, b in facts) + "</div>"
        body = (f'<header class="wide page-head"><div class="dossier-head">{mono(k, lg=True)}<div><p class="label">Service history · {E(" · ".join(LABEL[p] for p in v))}</p></div></div>'
                f'<h1>{E(title)}</h1><p class="meta">Tracked since <time datetime="{first}">{nice(first)}</time> · Last snapshot <time datetime="{last}">{nice(last)}</time></p>'
                f'<p class="lede">QuietlyChanged checks {E(k)}\'s public {kinds} pages every day and records what changes, in plain English.</p>{due_html}{facts_html}</header>'
                f'<div class="wide art-grid" style="margin-top:2rem"><div class="art-main"><div class="prose">{phtml}</div>{latest_ex}<div class="prose">{svc_faq}</div>'
                f'<section class="section" aria-labelledby="cl" style="margin-top:2.6rem"><div class="sec-title"><h2 id="cl">Changelog</h2><span class="label">{plural(len(log), "change")}</span></div>{cl}</section>'
                f'<section class="section" aria-labelledby="pw"><div class="sec-title"><h2 id="pw">Pages we monitor</h2></div><ul class="watch">{watch}</ul></section></div>'
                f'<aside class="art-aside" aria-label="About this service"><section class="box"><h2>Keep track</h2><div class="btnrow">{follow_btn(k)}<button class="btn" type="button" data-copy>Copy link</button></div></section>'
                + (f'<section class="box"><h2>In these threads</h2><ul class="chips">' + "".join(f'<li><a href="../../threads/{th}/">{E(THEMES[th]["title"])}</a></li>' for th in dict.fromkeys(t for _, c in log for t in c.get("themes", [])) if th in THEMES) + '</ul></section>' if any(c.get("themes") for _, c in log) else "")
                + f'<section class="box"><h2>Neighbors</h2><ul class="chips"><li><a href="../{slug(nb[0])}/">{E(nb[0])}</a></li><li><a href="../{slug(nb[1])}/">{E(nb[1])}</a></li><li><a href="../../services.html">All services</a></li><li><a href="../../about.html">How it works</a></li></ul></section></aside></div>')
        write(D / "services" / sl / "index.html", page(f"services/{sl}/index.html", title, body, TODAY, desc=desc, depth=2, ld=([ld, phld] if phld else ld), lastmod=max([last] + [c.get("modified", d) for d, c in log] + ([PH[k]["verified"]] if k in PH else [])), crumbs=[("Home", SITE + "/"), ("What we track", SITE + "/services.html")]))

    # ---------- services index ----------
    tiles = []
    for k_, v in sorted(s.items(), key=lambda x: x[0].lower()):
        log = svc_stats[k_]
        st = f'{plural(len(log), "change")} · last {short(log[0][0])}' if log else "No changes yet"
        hot = log and days_until(log[0][0], TODAY) >= -7
        tiles.append(f'<li data-k="{" ".join(v)}" data-n="{E(k_.lower())}" data-s="{E(k_)}"><a class="tile" href="services/{slug(k_)}/">{mono(k_)}<b>{E(k_)}</b><span class="k">{"".join(kind(p) for p in v)}</span><span class="st{" hot" if hot else ""}">{st}{" · price history" if k_ in PH else ""}</span></a>{follow_btn(k_, small=True)}</li>')
    btn = "".join(f'<li><button type="button" data-f="{k}" aria-pressed="false">{v}</button></li>' for k, v in LABEL.items()) + '<li><button type="button" data-f="followed" aria-pressed="false">Following</button></li>'
    write(D / "services.html", page("services.html", "What we track", today=TODAY, desc=f"Search the {len(s)} services QuietlyChanged monitors daily for pricing, terms of service, and privacy policy changes.", body=f'''<header class="wide page-head"><p class="label">Coverage</p><h1>What we track</h1><p class="lede">{len(s)} services and {sum(map(len,s.values()))} pages, checked every morning. Tap the star on the services you use and the front page will show what changed for you.</p></header>
<section class="wide"><div class="filters" role="search"><label class="sr" for="q">Search services</label><input id="q" type="search" placeholder="Search services…" autocomplete="off"><ul class="chips" style="list-style:none">{btn}</ul></div>
<p class="label" id="count" aria-live="polite" style="margin-bottom:.8rem">{len(s)} of {len(s)} services shown</p>
<ul class="tiles" id="rows">{"".join(tiles)}</ul></section>'''))

    # ---------- about ----------
    write(D / "about.html", page("about.html", "How it works", today=TODAY, desc="How QuietlyChanged snapshots, compares, and explains daily changes to popular services' pricing pages, terms, and privacy policies.", body=f'''<header class="wrap page-head"><p class="label">About</p><h1>How it works</h1>
<p class="lede">Companies revise their prices, plan limits, terms of service, and privacy policies all the time, usually without announcement. QuietlyChanged keeps a public, dated record of those changes.</p></header>
<div class="wrap prose"><h2>Our method</h2><ol><li><strong>Snapshot.</strong> Every morning we fetch the public pricing, terms, and privacy pages of every <a href="services.html">tracked service</a> and save the main text.</li>
<li><strong>Compare.</strong> Each snapshot is compared line by line with the previous day's. We filter out noise such as cookie banners, scripts, timestamps, and copyright lines.</li>
<li><strong>Explain.</strong> Meaningful differences are summarized in plain English: what changed, who it affects, and a link to the source.</li>
<li><strong>Publish.</strong> The day's report goes on the front page and into the <a href="archive.html">archive</a>.</li></ol>
<h2>Reading a blackline</h2><p>Lawyers compare two versions of a contract with a blackline, and so do we. Removed words are struck through in red; added words are underlined in blue. Text set in a typewriter face is the company's own wording, never ours.</p>
<figure class="exhibit" style="margin-top:1rem"><figcaption class="ex-head"><span><b>Example · Todoist privacy policy</b></span><span>Oct 24, 2026</span></figcaption><div class="ex-body"><div class="ex-text bl">…to develop, improve, or train <del><span class="sr">deleted: </span>generalized/non-personalized</del> artificial intelligence or machine learning models.</div></div></figure>
<p>Excerpts come from two places. "From our snapshot diff" means the words were taken directly from our before-and-after copies. "Quoted from the documents" means the change was confirmed in the company's own documents or announcements, which are linked from the article.</p>
<h2>Impact ratings</h2><p>{impact(3)} changes what you pay, what you can do, or what happens to your data, often with a deadline. {impact(2)} worth knowing if you use the service. {impact(1)} small edits: new features, relabeled plans, wording cleanups.</p>
<h2>Categories</h2><p>{kind("pricing")} prices, plans, limits, and fees. {kind("terms")} terms of service, user agreements, and contracts of carriage. {kind("privacy")} privacy policies and data-use notices.</p>
<h2>Threads and deadlines</h2><p><a href="threads/">Threads</a> connect the same kind of change across companies, like forced arbitration or AI training. <a href="due-soon/">Due soon</a> lists every date we find in a change, with calendar files you can add or subscribe to.</p>
<h2>Limits</h2><p>Some sites block automated readers or load their text with scripts; we only track pages we can read reliably. Summaries are not legal advice. Always check the linked source.</p></div>'''))

    # ---------- archive ----------
    def arch_row(d):
        its = data[d]; dots = "".join(f'<i class="dot-{p}"></i>' for p in sorted({c.get("page","terms") for c in its}))
        return f'<li><time datetime="{d}">{E(weekday(d))}</time><a href="reports/{d}.html">{E(report_title[d])}</a><span class="n">{dots}{plural(len(its), "change")}</span></li>'
    arch = "".join(arch_row(d) for d in reversed(days))
    hm = heatmap(days, data, lambda d: f"reports/{d}.html", TODAY)
    write(D / "archive.html", page("archive.html", "Archive", today=TODAY, lastmod=(days or [TODAY])[-1], desc="Archive of every QuietlyChanged daily report on pricing, terms of service, and privacy policy changes, by date.",
          body=f'<header class="wrap page-head"><p class="label">Archive</p><h1>Every report, by date</h1><p class="lede">{plural(len(days), "report")} and {plural(len(ALL), "change")} since {nice(days[0]) if days else ""}. Darker days had more, or bigger, changes.</p></header><section class="wrap">{hm}</section><section class="wrap section"><div class="sec-title"><h2>All reports</h2></div><ul class="archive">{arch}</ul></section>'))

    # ---------- front page ----------
    if days:
        L = days[-1]
        recent = [(d, c) for d, c in ALL_NEW if days_until(d, L) >= -6]
        lead = max(recent or ALL_NEW, key=lambda x: (x[1]["impact"], x[0], len(x[1].get("redline", []))))
        ld_, lc = lead
        lead_ex = exhibit(lc["redline"][0], lc["service"], LABEL.get(lc.get("page","terms")), "First seen " + short(ld_)) if lc.get("redline") else mini_bl(lc, 600)
        lead_html = (f'<section class="wide lead" aria-labelledby="lead-h"><div><div class="metarow">{mono(lc["service"], svc_href(lc["service"], ""))}{kind(lc.get("page","terms"))}<span class="svc">{E(lc["service"])}</span>{impact(lc["impact"])}<time datetime="{ld_}">{E(short(ld_))}</time></div>'
                     f'<h2 id="lead-h"><a href="changes/{lc["_art"]}/">{E(lc.get("headline",""))}</a></h2><p class="lede">{E(lc.get("tldr") or clip(lc["what"], 260))}</p>{stamp(lc, TODAY)}'
                     f'<div class="actions"><a class="btn solid" href="changes/{lc["_art"]}/">Read the change</a>' + (f'<a class="btn" href="due-soon/{lc["_art"]}.ics">Add to calendar</a>' if lc.get("effective") and days_until(lc["effective"], TODAY) >= 0 else "") + f'</div></div><div>{lead_ex}</div></section>')
        # latest report
        sm_txt = (R / "reports" / f"{L}-summary.md").read_text(); sm_body = md(sm_txt)
        _, _, sm_rest = sm_body.partition("</h1>")
        today_items = [c for c in data[L] if c is not lc]
        today_li = "".join(f'<li>{entry(c, L, "", TODAY, svc_href=svc_href(c["service"], ""))}</li>' for c in sorted(today_items, key=lambda c: -c["impact"]))
        latest_html = (f'<section class="wide section" aria-labelledby="latest-h"><div class="sec-title"><h2 id="latest-h"><span class="sym">§</span>The latest report</h2><a href="reports/{L}.html">Permalink · {E(short(L))}</a></div><div class="latest"><div>'
                       f'<p class="label" style="margin-bottom:.4rem">{E(weekday(L))} · {plural(len(data[L]), "change")}</p><h3 style="font-size:1.75rem;line-height:1.12"><a href="reports/{L}.html" style="text-decoration:none">{E(report_title[L])}</a></h3>'
                       f'<div class="prose" style="margin-top:1rem;font-size:1.05rem">{sm_rest}</div><p class="linkline" style="margin-top:1rem"><a href="reports/{L}.html">Permalink</a> · <a href="archive.html">Earlier reports</a></p></div>'
                       + (f'<div><ul class="entries">{today_li}</ul></div>' if today_li else "<div></div>") + '</div></section>')
        due_html = ""
        if upcoming:
            due_html = (f'<section class="wide section" aria-labelledby="due-h"><div class="sec-title"><h2 id="due-h"><span class="sym">§</span>Due soon</h2><a href="due-soon/">All dates and calendar →</a></div>'
                        f'<div class="due" tabindex="0" aria-label="Upcoming deadlines">{"".join(due_card(c, "") for d, c in upcoming[:12])}</div></section>')
        week = [(d, c) for d, c in ALL_NEW if days_until(d, L) >= -6 and c is not lc and d != L][:9]
        week_html = ""
        if week:
            wl = "".join(f'<li class="{"major" if c["impact"] == 3 and i < 2 else ""}">{entry(c, d, "", TODAY, svc_href=svc_href(c["service"], ""), mini=c["impact"] >= 2)}</li>' for i, (d, c) in enumerate(week))
            week_html = f'<section class="wide section" aria-labelledby="wk-h"><div class="sec-title"><h2 id="wk-h"><span class="sym">§</span>Earlier this week</h2><a href="archive.html">Archive →</a></div><ul class="grid-entries">{wl}</ul></section>'
        seis = seismograph(days, data, lambda d: f"reports/{d}.html", TODAY)
        seis_html = (f'<section class="wide section"><div class="two"><div><div class="sec-title"><h2><span class="sym">§</span>The seismograph</h2><a href="archive.html">Calendar →</a></div>{seis}'
                     f'<div class="legend">{kind("pricing")}{kind("terms")}{kind("privacy")}<span class="label">Taller block = bigger change · tap a day</span></div></div>'
                     f'<div><div class="sec-title"><h2><span class="sym">§</span>Price leaders</h2><a href="subscription-price-history/">Compare →</a></div>'
                     + bars([(r[2], f'services/{slug(r[1])}/#price-history', r[0]) for r in cmp_rows[:8]]) + '<p class="cap">Total increase on the main US plan since launch.</p></div></div></section>')
        threads_html = (f'<section class="wide section" aria-labelledby="th-h"><div class="sec-title"><h2 id="th-h"><span class="sym">§</span>Threads</h2><a href="threads/">All threads →</a></div>'
                        f'<div class="threads">{"".join(thread_card(th, "") for th in list(THEMES)[:8])}</div></section>')
        stack_html = (f'<section class="wide section" aria-labelledby="st-h"><div class="sec-title"><h2 id="st-h"><span class="sym">§</span>Your services</h2><a href="services.html">Follow more →</a></div>'
                      f'<div class="stack" data-stack><div><p class="lede" style="font-size:1.1rem">Tap the services you use. We\'ll keep a running list of what changed for you, saved in this browser.</p><ul class="chips pick" data-stack-pick style="margin-top:1rem"></ul></div>'
                      f'<div class="yours"><div class="top"><span class="label">Changes affecting you</span><div class="big" data-stack-count>Pick a few services</div></div><ul data-stack-list><li class="empty">Your list shows up here.</li></ul></div></div></section>')
        browse_html = ('<section class="wide section"><div class="sec-title"><h2>Browse by type</h2></div><p class="linkline"><a href="price-changes/">Price increases and pricing changes</a> · <a href="subscription-price-history/">Streaming and subscription price history compared</a> · <a href="terms-of-service-changes/">Terms of service changes</a> · <a href="privacy-policy-changes/">Privacy policy changes</a></p>'
                       + ('<h2 style="font-size:1.3rem;margin-top:1.6rem">Price histories</h2><p class="linkline">Every US price change, dated and sourced: ' + ' · '.join(f'<a href="services/{slug(n)}/#price-history">{E(v.get("name",n))}</a>' for n, v in PH.items()) + '</p>' if PH else "") + "</section>")
        nameplate = (f'<section class="nameplate"><div class="wide np"><div><h1>Quietly<i>Changed</i></h1><p class="tag">{E(TAG)}</p></div>'
                     f'<p class="edition"><b>{E(weekday(L))}</b><br>Report No. {len(days)-1} · {len(s)} services watched<br>{plural(len(ALL), "change")} on record</p></div></section>')
        body = nameplate + lead_html + due_html + latest_html + week_html + seis_html + threads_html + stack_html + browse_html
        WEB = {"@context": "https://schema.org", "@type": "WebSite", "name": "QuietlyChanged", "url": SITE + "/", "description": TAG}
        write(D / "index.html", page("index.html", "Latest", body, TODAY, ld=WEB, lastmod=L, front=True))

    # ---------- static assets ----------
    st = R / "static"
    fonts_css = (st / "fonts.css").read_text()
    write(D / "style.css", fonts_css + (st / "style.css").read_text())
    (D / "fonts").mkdir(exist_ok=True)
    for f in (st / "fonts").glob("*.woff2"): shutil.copy2(f, D / "fonts" / f.name)
    shutil.copy2(st / "app.js", D / "app.js")
    write(D / "favicon.svg", FAV)
    write(D / "og.svg", '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 630"><rect width="1200" height="630" fill="#EEF0EC"/><rect y="600" width="1200" height="30" fill="#BA2A1F"/><text x="600" y="300" font-family="Georgia,serif" font-size="110" font-weight="700" text-anchor="middle" fill="#15181D">Quietly<tspan fill="#BA2A1F">Changed</tspan></text><text x="600" y="390" font-family="Arial,sans-serif" font-size="34" text-anchor="middle" fill="#464D57">What popular services quietly change in their fine print</text></svg>')
    write(D / ".nojekyll", "")
    if not (D / "CNAME").exists(): write(D / "CNAME", "quietlychanged.com\n")

    # ---------- search index ----------
    idx = [{"t": c.get("headline", ""), "s": c["service"], "k": c.get("page", "terms"), "d": d, "u": f'changes/{c["_art"]}/', "x": c.get("tldr") or clip(c["what"], 160), "i": c["impact"], "e": c.get("effective", "")} for d, c in ALL_NEW]
    idx += [{"t": k_, "s": k_, "k": "service", "u": f"services/{slug(k_)}/", "x": f'{plural(len(svc_stats[k_]), "change")} logged', "p": list(v)} for k_, v in s.items()]
    idx += [{"t": v["title"], "s": "Thread", "k": "thread", "u": f"threads/{th}/", "x": v["dek"]} for th, v in THEMES.items()]
    write(D / "search.json", json.dumps(idx, ensure_ascii=False, separators=(",", ":")))

    # ---------- Atom feed: daily reports + change articles (newest first) ----------
    entries = []
    for d in days:
        entries.append((d, f'<entry><title>Report, {nice(d)}</title><link href="{SITE}/reports/{d}.html"/><id>{SITE}/reports/{d}.html</id><updated>{d}T12:00:00Z</updated></entry>'))
    for d, c in ALL:
        a = c["_art"]; url = f"{SITE}/changes/{a}/"; t = c.get("seo_title") or f'{c["service"]}: {c.get("headline") or "page updated"}'
        entries.append((d, f'<entry><title>{E(t)}</title><link href="{url}"/><id>{url}</id><updated>{d}T12:00:00Z</updated><summary>{E(c.get("what",""))}</summary></entry>'))
    entries.sort(key=lambda x: x[0], reverse=True)
    write(D / "feed.xml", f'<?xml version="1.0" encoding="utf-8"?><feed xmlns="http://www.w3.org/2005/Atom"><title>QuietlyChanged</title><link href="{SITE}/"/><link rel="self" href="{SITE}/feed.xml"/><id>{SITE}/</id><updated>{(days or [TODAY])[-1]}T12:00:00Z</updated>{"".join(e for _, e in entries)}</feed>')

    # ---------- sitemap / robots ----------
    write(D / "sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' + "".join(f"<url><loc>{u}</loc><lastmod>{m}</lastmod></url>" for u, m in {u: (m or TODAY) for u, m in PAGES}.items()) + "</urlset>")
    write(D / "robots.txt", f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n")

    # ---------- IndexNow (Bing/Yandex): key file + ping new/changed URLs ----------
    key = (R / "indexnow.key").read_text().strip() if (R / "indexnow.key").exists() else ""
    if key:
        write(D / f"{key}.txt", key)
        if os.environ.get("QC_NO_INDEXNOW"): print("IndexNow ping skipped (QC_NO_INDEXNOW set; ping after deploy)")
        else:
            try:
                import urllib.request
                urls = list(dict.fromkeys(u for u, _ in PAGES))
                ping = [u for u in urls if "/changes/" in u][-20:]
                if days: ping += [f"{SITE}/reports/{days[-1]}.html", f"{SITE}/"]
                ping.append(f"{SITE}/feed.xml")
                ping += [f"{SITE}/{h[0]}" for h in HUB_FOR.values()]
                ping += [f"{SITE}/services/{slug(n)}/" for n in PH] + ([f"{SITE}/subscription-price-history/"] if PH else [])
                ping += [f"{SITE}/due-soon/", f"{SITE}/threads/"] + [f"{SITE}/threads/{th}/" for th in THEMES]
                ping = list(dict.fromkeys(ping))
                body = json.dumps({"host": "quietlychanged.com", "key": key, "keyLocation": f"{SITE}/{key}.txt", "urlList": ping}).encode()
                req = urllib.request.Request("https://api.indexnow.org/indexnow", data=body, headers={"Content-Type": "application/json; charset=utf-8"}, method="POST")
                with urllib.request.urlopen(req, timeout=15) as resp: print(f"IndexNow: {resp.status} for {len(ping)} URLs")
            except Exception as ex: print(f"IndexNow ping skipped: {ex}")

    og.site_image(D, R)
    print(f"Built {len(PAGES)} pages · {len(ALL)} changes · {len(upcoming)} upcoming dates")
