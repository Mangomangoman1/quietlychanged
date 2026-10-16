#!/usr/bin/env python3
"""QuietlyChanged tracker: fetch -> extract text -> snapshot -> diff -> report."""
import json, re, sys, difflib, datetime, pathlib, concurrent.futures as cf
import requests
from bs4 import BeautifulSoup
ROOT = pathlib.Path(__file__).parent
SNAP = ROOT / "snapshots"; REP = ROOT / "reports"
UA = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128 Safari/537.36",
      "Accept-Language": "en-US,en;q=0.9"}
NOISE = [re.compile(p, re.I) for p in [
    r"cookie", r"accept all", r"^\s*(last )?(updated|modified|effective)[: ].{0,40}$",
    r"^©|copyright \d{4}", r"\b\d{1,2}:\d{2}\b", r"javascript", r"^\W*$"]]
DATE = re.compile(r"\b(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)[a-z]*\.? \d{1,2},? \d{4}\b|\b\d{4}-\d{2}-\d{2}\b", re.I)

def slug(s): return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")

def extract(html):
    soup = BeautifulSoup(html, "html.parser")
    for t in soup(["script","style","noscript","svg","iframe","header","footer","nav","form","button"]): t.decompose()
    for t in soup.select('[id*="cookie" i],[class*="cookie" i],[id*="consent" i],[class*="consent" i],[class*="banner" i]'): t.decompose()
    main = soup.find("main") or soup.find("article") or soup.body or soup
    lines = []
    for ln in main.get_text("\n").splitlines():
        ln = re.sub(r"\s+", " ", ln).strip()
        if len(ln) < 3 or any(p.search(ln) for p in NOISE): continue
        lines.append(DATE.sub("<DATE>", ln))
    return "\n".join(lines)

def extract_pdf(data):
    """PDF -> text via poppler's pdftotext, with the same line filtering as HTML pages."""
    import subprocess, tempfile
    with tempfile.NamedTemporaryFile(suffix=".pdf") as f:
        f.write(data); f.flush()
        raw = subprocess.run(["pdftotext", "-q", f.name, "-"], capture_output=True, timeout=60).stdout.decode("utf-8", "ignore")
    lines = []
    for ln in raw.splitlines():
        ln = re.sub(r"\s+", " ", ln).strip()
        if len(ln) < 3 or any(p.search(ln) for p in NOISE) or re.fullmatch(r"\d{1,3}", ln): continue
        lines.append(DATE.sub("<DATE>", ln))
    return "\n".join(lines)

def fetch(job):
    svc, kind, url = job
    try:
        r = requests.get(url, headers=UA, timeout=25)
        if r.status_code != 200: return job, None, f"HTTP {r.status_code}"
        is_pdf = "pdf" in r.headers.get("content-type","") or r.content[:5] == b"%PDF-"
        txt = extract_pdf(r.content) if is_pdf else extract(r.text)
        if len(txt) < 300: return job, None, f"too little text ({len(txt)} chars; JS-rendered or bot wall)"
        return job, txt, None
    except Exception as e: return job, None, type(e).__name__

def latest_before(d, day):
    prev = sorted(p for p in d.glob("*.txt") if p.stem < day)
    return prev[-1] if prev else None

def run(day):
    svcs = json.loads((ROOT/"services.json").read_text())
    jobs = [(s,k,u) for s,v in svcs.items() for k,u in v.items()]
    ok, fail, changes = [], [], []
    with cf.ThreadPoolExecutor(12) as ex:
        for (s,k,u), txt, err in ex.map(fetch, jobs):
            if err: fail.append((s,k,u,err)); continue
            d = SNAP/slug(s)/k; d.mkdir(parents=True, exist_ok=True)
            prev = latest_before(d, day)
            (d/f"{day}.txt").write_text(txt); ok.append((s,k,u))
            if prev:
                a = prev.read_text().splitlines(); b = txt.splitlines()
                diff = [l for l in difflib.unified_diff(a,b,lineterm="",n=1) if not l.startswith(("---","+++"))]
                added = [l for l in diff if l.startswith("+")]; removed = [l for l in diff if l.startswith("-")]
                if added or removed:
                    changes.append({"service":s,"page":k,"url":u,"diff":"\n".join(diff[:200]),"added":len(added),"removed":len(removed)})
    REP.mkdir(exist_ok=True)
    json.dump({"date":day,"ok":ok,"failed":fail,"changes":changes}, open(REP/f"{day}.json","w"), indent=1)
    md = [f"# Raw changes for {day}", f"Fetched {len(ok)} pages; {len(fail)} failed; {len(changes)} changed.\n"]
    for c in changes:
        md += [f"## {c['service']} — {c['page']} (+{c['added']}/-{c['removed']})", c["url"], "```diff", c["diff"], "```"]
    md += ["\n## Fetch failures"] + [f"- {s} {k}: {e} ({u})" for s,k,u,e in fail]
    (REP/f"{day}-raw.md").write_text("\n".join(md))
    print(f"{day}: ok={len(ok)} failed={len(fail)} changed={len(changes)}")

if __name__ == "__main__":
    run(sys.argv[1] if len(sys.argv)>1 else datetime.date.today().isoformat())
