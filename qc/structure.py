"""Turn a long single-paragraph `what` into readable sections.

Writers can be explicit: blank lines start new paragraphs and a line starting with "## "
is a subheading. Otherwise we split sentences and promote the lead-ins our write-ups
already use ("Change 1: …", "What you can do:", "How it compares (checked …):") to headings.
Coverage notes are pulled out so the page can show them in a quieter box."""
import re
from .util import E

_ABBR = {"U.S", "U.K", "Doc", "No", "Nos", "S.p.A", "e.g", "i.e", "vs", "Inc", "Co", "Corp", "Ltd", "Mr", "Ms", "Dr", "St",
         "Jan", "Feb", "Mar", "Apr", "Jun", "Jul", "Aug", "Sep", "Sept", "Oct", "Nov", "Dec", "a.m", "p.m", "approx", "est", "etc"}
_BOUND = re.compile(r'(?<=[.!?])(["”’)\]]*)\s+(?=["“(\[]?[A-Z0-9$€£])')

def sentences(text):
    out, start = [], 0
    for m in _BOUND.finditer(text):
        end = m.start()
        prev = text[start:end + 0]
        word = re.search(r"([A-Za-z.]+)\.$", prev)
        if word and (word.group(1) in _ABBR or re.fullmatch(r"[A-Z]", word.group(1)) or re.fullmatch(r"(?:[A-Za-z]\.)+[A-Za-z]", word.group(1))):
            continue
        out.append(text[start:m.end(1)].strip()); start = m.end()
    tail = text[start:].strip()
    if tail: out.append(tail)
    return out

_LEADS = r"(What you can do(?: before you mail)?|What to do(?: before you mail)?|What it means|What stays the same|What it replaces|What the apps are telling users|How it compares|How private carriers compare|How to comment|Some history|Other changes|Unchanged|Accounts|Your uploads|Public pages|Data|Billing|Defective purchases|Scope|Free trials|For comparison)"
_HEAD = re.compile(r"^" + _LEADS + r"(\s*\([^)]*\))?\s*:\s*(.*)$", re.S)
_CHANGE = re.compile(r"^(Change \d+)\s*:\s*(.+?)[.]?$", re.S)
_SOLO = {"More could change.", "Some changes favor customers.", "Mass claims are squeezed harder."}
_COVER = re.compile(r"^Coverage(?: so far| check)?\s*(\([^)]*\))?\s*[:,]?\s*(.*)$", re.S)

def structure(what, para_chars=430):
    """-> (sections, coverage). sections: [(heading or None, meta or None, [paragraph, …])]"""
    text = (what or "").strip()
    if not text: return [], None
    sections = [[None, None, []]]; coverage = []
    def add_sents(sents):
        para = []
        for s in sents:
            para.append(s)
            if sum(len(x) for x in para) > para_chars:
                sections[-1][2].append(" ".join(para)); para = []
        if para: sections[-1][2].append(" ".join(para))
    if "\n" in text:   # explicit structure from the writer
        for block in re.split(r"\n\s*\n", text):
            block = block.strip()
            if block.startswith("## "):
                head, _, rest = block[3:].partition("\n"); sections.append([head.strip(), None, []])
                if rest.strip(): sections[-1][2].append(rest.strip())
            elif block: sections[-1][2].append(block)
        return [tuple(s) for s in sections if s[0] or s[2]], None
    if len(text) < 650:
        return [(None, None, [text])], None
    buf = []; in_cover = False
    for s in sentences(text):
        m = _CHANGE.match(s); h = _HEAD.match(s); c = _COVER.match(s)
        if c and len(s) < 900:
            add_sents(buf); buf = []; in_cover = True
            coverage.append(((c.group(1) or "").strip("() "), c.group(2).strip())); continue
        if in_cover and not (m or h or s in _SOLO):
            coverage[-1] = (coverage[-1][0], coverage[-1][1] + " " + s); continue
        in_cover = False
        if m:
            add_sents(buf); buf = []
            sections.append([f"{m.group(1)}: {m.group(2)[0].lower() + m.group(2)[1:] if m.group(2)[:2] != m.group(2)[:2].upper() else m.group(2)}", None, []])
            continue
        if h:
            add_sents(buf); buf = []
            sections.append([h.group(1), (h.group(2) or "").strip(" ()") or None, []])
            rest = h.group(3).strip()
            if rest: buf.append(rest[0].upper() + rest[1:])
            continue
        if s in _SOLO:
            add_sents(buf); buf = []; sections.append([s.rstrip("."), None, []]); continue
        buf.append(s)
    add_sents(buf)
    cov = None
    if coverage:
        meta = next((m for m, _ in coverage if m), "")
        cov = (meta, " ".join(t for _, t in coverage))
    return [tuple(s) for s in sections if s[0] or s[2]], cov

def render(sections, h="h3"):
    out = []
    for head, meta, paras in sections:
        if head:
            out.append(f'<{h}>{E(head)}' + (f'<span class="part-meta">{E(meta)}</span>' if meta else "") + f'</{h}>')
        out += [f"<p>{E(p)}</p>" for p in paras]
    return "\n".join(out)
