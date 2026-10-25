"""Small shared helpers: escaping, slugs, dates, light markdown."""
import datetime, html, re

E = html.escape
LABEL = {"pricing": "Pricing", "terms": "Terms", "privacy": "Privacy"}
IMPACT = {1: "Minor", 2: "Notable", 3: "Major"}

def slug(x): return re.sub(r"[^a-z0-9]+", "-", x.lower().replace("+", "-plus")).strip("-")
def slug_tr(x): return re.sub(r"[^a-z0-9]+", "-", x.lower()).strip("-")
def art_slug(d, c): return f"{d}-{slug(c['service'])}-{slug(c.get('headline') or c.get('page', 'update'))}"[:90].strip("-")
def date(s): return datetime.date.fromisoformat(s)
def nice(d): return date(d).strftime("%B %-d, %Y")
def short(d): return date(d).strftime("%b %-d")
def short_y(d): return date(d).strftime("%b %-d, %Y")
def weekday(d): return date(d).strftime("%A, %B %-d, %Y")
def days_until(d, today): return (date(d) - date(today)).days

def monogram(name):
    m = re.search(r"[A-Za-z0-9]", name)
    return (m.group(0) if m else "?").upper()

def md(t):
    """The light markdown the daily summaries use: # / ## headings, - lists, **bold**, [links](url)."""
    out = []; inl = False
    for l in t.splitlines():
        e = E(l); e = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", e); e = re.sub(r"\[(.+?)\]\((.+?)\)", r'<a href="\2">\1</a>', e)
        if l.startswith("- "):
            if not inl: out.append("<ul>"); inl = True
            out.append(f"<li>{e[2:]}</li>"); continue
        if inl: out.append("</ul>"); inl = False
        if l.startswith("## "): out.append(f"<h2>{e[3:]}</h2>")
        elif l.startswith("# "): out.append(f"<h1>{e[2:]}</h1>")
        elif l.strip(): out.append(f"<p>{e}</p>")
    if inl: out.append("</ul>")
    return "\n".join(out)

def plural(n, word, pl=None): return f"{n} {word if n == 1 else (pl or word + 's')}"
