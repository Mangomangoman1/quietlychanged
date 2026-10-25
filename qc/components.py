"""Reusable HTML pieces."""
from .util import E, LABEL, IMPACT, short, short_y, nice, days_until, monogram
from .redline import blackline
from .layout import ICON_STAR

def kind(k): return f'<span class="kind {E(k)}">{LABEL.get(k, k.title())}</span>'

def impact(n):
    n = int(n or 1)
    return f'<span class="impact" title="Impact: {IMPACT[n]}"><i class="on"></i><i{" class=on" if n >= 2 else ""}></i><i{" class=on" if n >= 3 else ""}></i><b>{IMPACT[n]}</b></span>'

def mono(name, href=None, lg=False):
    cls = "mono-badge" + (" lg" if lg else "")
    m = E(monogram(name))
    return f'<a class="{cls}" href="{href}" aria-hidden="true" tabindex="-1">{m}</a>' if href else f'<span class="{cls}" aria-hidden="true">{m}</span>'

def countdown_text(n):
    return "today" if n == 0 else "tomorrow" if n == 1 else f"in {n} days" if n > 1 else "yesterday" if n == -1 else f"{-n} days ago"

def stamp(c, today):
    eff = c.get("effective")
    if not eff: return ""
    n = days_until(eff, today); label = c.get("deadline") or "Takes effect"
    past = n < 0
    return (f'<div class="stamp{" past" if past else ""}" role="note"><span>{E(label)} {E(short(eff) if eff[:4] == today[:4] else short_y(eff))}</span>'
            f'<span data-countdown="{eff}">{countdown_text(n)}</span></div>')

def exhibit(r, service, kind_label, when, idx=0):
    """One blackline excerpt. `when` is the provenance line in the header."""
    before, after = r.get("before", ""), r.get("after", "")
    if before and after: inner = blackline(before, after)
    elif after: inner = f'<ins><span class="sr">inserted: </span>{E(after)}</ins>'
    else: inner = f'<del><span class="sr">deleted: </span>{E(before)}</del>'
    note = r.get("note")
    label = r.get("label") or f"{service} · {kind_label}"
    src = "From our snapshot diff" if r.get("src") == "raw" else "Quoted from the documents"
    nh = f'<aside class="ex-note"><span class="who">What it means</span>{E(note)}</aside>' if note else ""
    return (f'<figure class="exhibit" aria-label="Wording change {idx+1}"><figcaption class="ex-head"><span><b>{E(label)}</b></span><span>{E(when)} · {src}</span></figcaption>'
            f'<div class="ex-body{" has-note" if note else ""}"><div class="ex-text bl">{inner}</div>{nh}</div></figure>')

def mini_bl(c, limit=240):
    for r in c.get("redline", []):
        b, a = r.get("before", ""), r.get("after", "")
        if len(b) + len(a) <= limit and (b or a):
            if b and a: inner = blackline(b, a)
            elif a: inner = f'<ins><span class="sr">inserted: </span>{E(a)}</ins>'
            else: inner = f'<del><span class="sr">deleted: </span>{E(b)}</del>'
            return f'<div class="mini-bl bl">{inner}</div>'
    return ""

def clip(t, n=240):
    t = (t or "").strip()
    return t if len(t) <= n else t[:n].rsplit(" ", 1)[0].rstrip(",;:") + "…"

def due_chip(c, today):
    eff = c.get("effective")
    if not eff: return ""
    n = days_until(eff, today)
    if n < 0: return ""
    return f'<span class="due-chip">{E(c.get("deadline") or "Takes effect")} {E(short(eff))} · <span data-countdown="{eff}">{countdown_text(n)}</span></span>'

def entry(c, d, root, today, title=None, svc_href=None, show_service=True, who=False, mini=True, h="h3"):
    """A change as a list item. root = relative path to site root."""
    url = f'{root}changes/{c["_art"]}/'
    t = title if title is not None else (c.get("headline") or "Page updated")
    svc = ""
    if show_service:
        svc = f'<a class="svc" href="{svc_href}">{E(c["service"])}</a>' if svc_href else f'<span class="svc">{E(c["service"])}</span>'
    body = c.get("tldr") or clip(c["what"])
    whoh = f'<p><strong style="font-weight:600;color:var(--ink)">Who it affects:</strong> {E(c.get("who","All users"))}</p>' if who else ""
    return (f'<article class="entry"><div class="metarow">{kind(c.get("page","terms"))}{svc}{impact(c.get("impact",1))}<time datetime="{d}">{E(short(d))}</time></div>'
            f'<{h}><a href="{url}">{E(t)}</a></{h}><p>{E(body)}</p>{mini_bl(c) if mini else ""}{whoh}'
            f'<div class="foot">{due_chip(c, today)}<a href="{url}">Read the change →</a><a href="{E(c["url"])}" rel="nofollow noopener">Source ↗<span class="sr"> for {E(c["service"])}</span></a></div></article>')

def follow_btn(service, small=False):
    if small:
        return f'<button class="star" type="button" data-follow="{E(service)}" aria-pressed="false" aria-label="Follow {E(service)}">{ICON_STAR}</button>'
    return f'<button class="btn" type="button" data-follow="{E(service)}" aria-pressed="false">{ICON_STAR}<span data-follow-label>Follow {E(service)}</span></button>'
