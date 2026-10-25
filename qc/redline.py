"""Word-level blacklines: turn a before/after pair of strings into <del>/<ins> HTML,
and pull candidate excerpts out of the tracker's raw unified diffs."""
import difflib, html, re

_TOK = re.compile(r"\s+|[^\s]+")

def _toks(s):
    return _TOK.findall(s or "")

def _coalesce(a, ops, gap=2):
    """Merge edits separated by tiny unchanged runs (<= gap words) so a rewritten phrase
    reads as one strike + one insert instead of alternating single words."""
    out = []
    for op in ops:
        out.append(list(op))
    changed = True
    while changed:
        changed = False
        for k in range(1, len(out) - 1):
            if out[k][0] == "equal" and out[k-1][0] != "equal" and out[k+1][0] != "equal":
                if len("".join(a[out[k][1]:out[k][2]]).split()) <= gap:
                    out[k-1:k+2] = [["replace", out[k-1][1], out[k+1][2], out[k-1][3], out[k+1][4]]]
                    changed = True; break
    return [tuple(o) for o in out]

def blackline(before, after):
    """HTML for one excerpt. Unchanged words plain, removed words in <del>, added in <ins>.
    Screen readers get 'deleted:'/'inserted:' labels so meaning never rests on color."""
    a, b = _toks(before), _toks(after)
    sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
    out = []
    ops = _coalesce(a, sm.get_opcodes())
    same = sum(len("".join(a[i1:i2]).split()) for op, i1, i2, j1, j2 in ops if op == "equal")
    total = max(len(before.split()), len(after.split()), 1)
    if before.strip() and after.strip() and same / total < .45:
        return (f'<del><span class="sr">deleted: </span>{html.escape(before.strip())}</del> '
                f'<ins><span class="sr">inserted: </span>{html.escape(after.strip())}</ins>')
    for op, i1, i2, j1, j2 in ops:
        old, new = "".join(a[i1:i2]), "".join(b[j1:j2])
        if op == "equal":
            out.append(html.escape(old)); continue
        lead = ""
        # keep surrounding whitespace outside the marks so strikes don't run into spaces
        if op in ("delete", "replace") and old.strip():
            ws = old[len(old.rstrip()):]; lw = old[:len(old) - len(old.lstrip())]
            out.append(f'{lw}<del><span class="sr">deleted: </span>{html.escape(old.strip())}</del>')
            lead = " " if op == "replace" else ws
            if op == "delete": out.append(ws); continue
        elif op in ("delete", "replace"):
            out.append(html.escape(old))
        if op in ("insert", "replace") and new.strip():
            ws = new[len(new.rstrip()):]; lw = new[:len(new) - len(new.lstrip())]
            out.append(f'{lead if op=="replace" else lw}<ins><span class="sr">inserted: </span>{html.escape(new.strip())}</ins>{ws}')
        elif op in ("insert", "replace"):
            out.append(html.escape(new))
    return re.sub(r"  +", " ", "".join(out)).strip()

def changed_words(before, after):
    a, b = _toks(before), _toks(after)
    sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
    return sum(len("".join(a[i1:i2]).split()) + len("".join(b[j1:j2]).split()) for op, i1, i2, j1, j2 in sm.get_opcodes() if op != "equal")

# ---- raw diff parsing (reports/DATE-raw.md) ----
_SEC = re.compile(r"^## (.+?) — (pricing|terms|privacy) \(\+(\d+)/-(\d+)\)\n(\S+)\n```diff\n(.*?)\n```", re.M | re.S)

def raw_sections(text):
    """{(service, page): {"url":…, "diff": "...unified diff text...", "add": n, "rem": n}}"""
    out = {}
    for svc, page, add, rem, url, body in _SEC.findall(text or ""):
        out[(svc.strip(), page)] = {"url": url, "diff": body, "add": int(add), "rem": int(rem)}
    return out

def _trim(before, after, ctx=28):
    """Cut a long pair of lines down to the changed region plus ~ctx words either side."""
    a, b = before.split(" "), after.split(" ")
    sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
    ops = [o for o in sm.get_opcodes() if o[0] != "equal"]
    if not ops: return before, after
    i1, i2 = max(0, ops[0][1] - ctx), min(len(a), ops[-1][2] + ctx)
    j1, j2 = max(0, ops[0][3] - ctx), min(len(b), ops[-1][4] + ctx)
    pre = "…" if i1 > 0 else ""; post_a = "…" if i2 < len(a) else ""; post_b = "…" if j2 < len(b) else ""
    return pre + " ".join(a[i1:i2]) + post_a, ("…" if j1 > 0 else "") + " ".join(b[j1:j2]) + post_b

def candidates(diff_text, limit=4):
    """Best before/after pairs from a unified diff, most changed first."""
    pairs = []; rem, add = [], []
    def flush():
        if rem and add:
            used = set()
            for r in rem:
                best = max(((difflib.SequenceMatcher(None, r, x).ratio(), k) for k, x in enumerate(add) if k not in used), default=(0, None))
                if best[1] is not None and best[0] > 0.45:
                    used.add(best[1]); pairs.append(_trim(r, add[best[1]]))
            for k, x in enumerate(add):
                if k not in used and len(x.split()) >= 4: pairs.append(("", x))
        elif add:
            pairs.extend(("", x) for x in add if len(x.split()) >= 4)
        elif rem:
            pairs.extend((x, "") for x in rem if len(x.split()) >= 4)
        rem.clear(); add.clear()
    for line in diff_text.splitlines():
        if line.startswith("@@"): flush(); continue
        if line.startswith("-"): 
            if add: flush()
            rem.append(line[1:]); continue
        if line.startswith("+"): add.append(line[1:]); continue
        flush()
    flush()
    pairs.sort(key=lambda p: -changed_words(*p))
    return pairs[:limit]
