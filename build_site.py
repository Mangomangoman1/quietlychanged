#!/usr/bin/env python3
"""Builds docs/ (GitHub Pages root) from reports/*-summary.md and services.json."""
import json, pathlib, html, re
R=pathlib.Path(__file__).parent; D=R/"docs"; (D/"reports").mkdir(parents=True,exist_ok=True)
CSS="body{font:17px/1.6 system-ui,sans-serif;max-width:720px;margin:2rem auto;padding:0 1rem;color:#222}a{color:#b5301f}h1 a{color:#222;text-decoration:none}nav a{margin-right:1rem}li{margin:.2rem 0}"
def page(title,body,depth=0):
    p="../"*depth
    return f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{html.escape(title)} · QuietlyChanged</title><style>{CSS}</style></head><body><h1><a href="{p}index.html">QuietlyChanged</a></h1><nav><a href="{p}index.html">Latest</a><a href="{p}archive.html">Archive</a><a href="{p}services.html">What we track</a></nav><hr>{body}<hr><small>Daily plain-English diffs of pricing pages, terms, and privacy policies.</small></body></html>'
def md(t):  # tiny markdown -> html
    out=[];inl=False
    for l in t.splitlines():
        e=html.escape(l); e=re.sub(r"\*\*(.+?)\*\*",r"<b>\1</b>",e); e=re.sub(r"\[(.+?)\]\((.+?)\)",r'<a href="\2">\1</a>',e)
        if l.startswith("- "):
            if not inl: out.append("<ul>");inl=True
            out.append(f"<li>{e[2:]}</li>");continue
        if inl: out.append("</ul>");inl=False
        if l.startswith("## "): out.append(f"<h3>{e[3:]}</h3>")
        elif l.startswith("# "): out.append(f"<h2>{e[2:]}</h2>")
        elif l.strip(): out.append(f"<p>{e}</p>")
    if inl: out.append("</ul>")
    return "\n".join(out)
days=sorted((p.name[:10],p) for p in (R/"reports").glob("*-summary.md"))
for d,p in days: (D/"reports"/f"{d}.html").write_text(page(d,md(p.read_text()),1))
(D/"archive.html").write_text(page("Archive","<h2>Archive</h2><ul>"+"".join(f'<li><a href="reports/{d}.html">{d}</a></li>' for d,_ in reversed(days))+"</ul>"))
s=json.loads((R/"services.json").read_text())
(D/"services.html").write_text(page("What we track",f"<h2>What we track ({len(s)} services)</h2><ul>"+"".join(f'<li><b>{html.escape(k)}</b>: '+", ".join(f'<a href="{html.escape(u)}">{p}</a>' for p,u in v.items())+"</li>" for k,v in s.items())+"</ul>"))
latest=days[-1] if days else None
(D/"index.html").write_text(page("Latest",md(latest[1].read_text())+f'<p><a href="reports/{latest[0]}.html">Permalink</a></p>' if latest else "<p>No reports yet.</p>"))
(D/".nojekyll").write_text("")
