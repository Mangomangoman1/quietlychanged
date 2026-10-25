"""Charts as plain SVG/HTML, generated at build time (no JS, readable by crawlers)."""
import datetime
from .util import E, short, LABEL

# CPI-U, U.S. city average, annual averages (BLS series CUUR0000SA0).
# 2025 and 2026 are estimates; update when BLS publishes the annual figures.
CPI = {2005: 195.3, 2006: 201.6, 2007: 207.3, 2008: 215.3, 2009: 214.5, 2010: 218.1, 2011: 224.9, 2012: 229.6,
       2013: 233.0, 2014: 236.7, 2015: 237.0, 2016: 240.0, 2017: 245.1, 2018: 251.1, 2019: 255.7, 2020: 258.8,
       2021: 271.0, 2022: 292.7, 2023: 304.7, 2024: 313.7, 2025: 322.2, 2026: 330.0}
CPI_EST = {2025, 2026}

def _fy(s):
    if len(s) == 4: return int(s) + .5
    d = datetime.date.fromisoformat(s if len(s) == 10 else s + "-15")
    return d.year + (d.timetuple().tm_yday - 1) / 365.25

def cpi_at(t):
    y = int(t); f = t - y
    a = CPI.get(y, CPI[max(CPI)]); b = CPI.get(y + 1, a)
    return a + (b - a) * max(0, f - .5) * 2 if f >= .5 else CPI.get(y - 1, a) + (a - CPI.get(y - 1, a)) * (f + .5)

def _nice_step(span):
    for s in (.25, .5, 1, 2, 5, 10, 20, 25, 50, 100, 200, 500):
        if span / s <= 5: return s
    return 1000

def step_chart(rows, unit="month", today=None, inflation=True, label=""):
    """rows: [[date, price, …], …] -> (svg, inflation_price or None)."""
    pts = [(_fy(r[0]), float(r[1])) for r in rows]
    if len(pts) < 2: return "", None
    end_t = _fy(today) if today else max(t for t, _ in pts) + .4
    end_t = max(end_t, pts[-1][0] + .15)
    t0 = int(pts[0][0]); t1 = int(end_t) + 1
    infl = None
    if inflation and t0 >= min(CPI):
        infl = pts[0][1] * cpi_at(min(end_t, max(CPI) + .99)) / cpi_at(pts[0][0])
    hi = max([p for _, p in pts] + ([infl] if infl else [])) * 1.12
    step = _nice_step(hi); hi = (int(hi / step) + 1) * step
    W, H, X0, X1, Y0, Y1 = 640, 270, 56, 624, 236, 18
    x = lambda t: X0 + (t - t0) / (t1 - t0) * (X1 - X0)
    y = lambda p: Y0 - p / hi * (Y0 - Y1)
    money = lambda p: f"${p:,.2f}" if p < 100 and p != int(p) else f"${p:,.0f}"
    o = []
    v = step
    while v < hi + 1e-9:
        o.append(f'<line class="grid" x1="{X0}" x2="{X1}" y1="{y(v):.1f}" y2="{y(v):.1f}"/><text class="ax" x="{X0-8}" y="{y(v)+4:.1f}" text-anchor="end">{money(v) if step < 1 else "$" + format(int(v), ",")}</text>')
        v += step
    span = t1 - t0; ystep = 1 if span <= 6 else 2 if span <= 14 else 3 if span <= 20 else 5
    for yr in range(t0 + (1 if span > 6 else 0), t1 + 1, ystep):
        if X0 + 10 < x(yr) < X1 - 4:
            o.append(f'<text class="ax" x="{x(yr):.1f}" y="{Y0+20}" text-anchor="middle">{yr}</text>')
    o.append(f'<line class="base" x1="{X0}" x2="{X1}" y1="{Y0}" y2="{Y0}"/>')
    if infl:
        ip = [(pts[0][0], pts[0][1])]
        t = int(pts[0][0]) + 1
        while t < end_t:
            ip.append((t, pts[0][1] * cpi_at(t) / cpi_at(pts[0][0]))); t += .5
        ip.append((end_t, infl))
        o.append('<polyline class="infl" points="' + " ".join(f"{x(a):.1f},{y(b):.1f}" for a, b in ip) + '"/>')
    d = [f"M{x(pts[0][0]):.1f},{y(pts[0][1]):.1f}"] + [f"H{x(t):.1f}V{y(p):.1f}" for t, p in pts[1:]] + [f"H{x(end_t):.1f}"]
    o.append(f'<path class="area" d="{" ".join(d)} V{Y0} H{x(pts[0][0]):.1f} Z"/><path class="step" d="{" ".join(d)}"/>')
    for (t, p), r in zip(pts, rows):
        o.append(f'<circle class="dot" cx="{x(t):.1f}" cy="{y(p):.1f}" r="3.3"><title>{E(r[0])}: {money(p)}</title></circle>')
    ex, ey = x(end_t), y(pts[-1][1])
    o.append(f'<circle class="end" cx="{ex:.1f}" cy="{ey:.1f}" r="5"/><text class="lbl strong" x="{ex-9:.1f}" y="{ey-11:.1f}" text-anchor="end">{money(pts[-1][1])} now</text>')
    first_lbl_y = y(pts[0][1]) - 11
    o.append(f'<text class="lbl" x="{x(pts[0][0])+2:.1f}" y="{first_lbl_y:.1f}">{money(pts[0][1])} · {int(pts[0][0])}</text>')
    if infl:
        iy = y(infl); ty = iy + 18 if abs(iy - ey) < 24 or iy > ey else iy - 9
        ty = min(ty, Y0 - 6)
        o.append(f'<text class="lbl muted" x="{ex-9:.1f}" y="{ty:.1f}" text-anchor="end">{money(pts[0][1])} + inflation ≈ {money(infl)}</text>')
    aria = f"{label} price per {unit} from {money(pts[0][1])} in {int(pts[0][0])} to {money(pts[-1][1])} now" + (f"; the first price adjusted for inflation would be about {money(infl)}" if infl else "")
    return f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="{E(aria)}">{"".join(o)}</svg>', infl

def seismograph(days, data, art_url, today):
    """One column per day since tracking began; a block per change, colored by kind, tall by impact."""
    if not days: return ""
    d0 = datetime.date.fromisoformat(days[0]); d1 = datetime.date.fromisoformat(max(days[-1], today) if today else days[-1])
    n = (d1 - d0).days + 1
    W = 640; base = 150; unit = 9.5; gap = 2
    bw = W / n
    o = [f'<line class="base" x1="0" x2="{W}" y1="{base+.5}" y2="{base+.5}"/>']
    top = base
    for i in range(n):
        d = (d0 + datetime.timedelta(days=i)).isoformat()
        items = sorted(data.get(d, []), key=lambda c: -c.get("impact", 1))
        cx = i * bw; w = max(3, bw * .58); xx = cx + (bw - w) / 2
        y = base
        g = []
        for c in items:
            h = c.get("impact", 1) * unit; y -= h + gap
            g.append(f'<rect x="{xx:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="1.5" class="t-{c.get("page","terms")}"><title>{E(short(d))} · {E(c["service"])}: {E(c.get("headline",""))}</title></rect>')
        top = min(top, y)
        label = ""
        if n <= 31 or datetime.date.fromisoformat(d).day in (1, 8, 15, 22):
            label = f'<text class="day" x="{cx+bw/2:.1f}" y="{base+16}" text-anchor="middle">{datetime.date.fromisoformat(d).day}</text>'
        if i == 0 or datetime.date.fromisoformat(d).day == 1:
            label += f'<text class="mon" x="{cx+bw/2:.1f}" y="{base+30}" text-anchor="middle">{datetime.date.fromisoformat(d).strftime("%b").upper()}</text>'
        if items and d in days:
            o.append(f'<a href="{art_url(d)}" aria-label="{E(short(d))}: {len(items)} change{"s"*(len(items)!=1)}"><rect class="hit" x="{cx:.1f}" y="0" width="{bw:.1f}" height="{base}"/>{"".join(g)}</a>{label}')
        else:
            o.append(label)
    vb_top = min(0, top - 6)
    return f'<svg class="seis" viewBox="0 {vb_top:.0f} {W} {base+36-vb_top:.0f}" role="img" aria-label="Every change since {E(short(days[0]))}, one column per day, colored by type and stacked by impact">{"".join(o)}</svg>'

def heatmap(days, data, report_url, today):
    """Month calendars; each tracked day shaded by the sum of impact."""
    if not days: return ""
    d0 = datetime.date.fromisoformat(days[0]); d1 = datetime.date.fromisoformat(max(days[-1], today))
    months = []
    m = d0.replace(day=1)
    while m <= d1:
        months.append(m); m = (m.replace(day=28) + datetime.timedelta(days=4)).replace(day=1)
    out = []
    for m in reversed(months):
        nxt = (m.replace(day=28) + datetime.timedelta(days=4)).replace(day=1)
        cells = ['<span class="dow">' + x + '</span>' for x in "MTWTFSS"]
        cells += ['<span class="c x"></span>'] * m.weekday()
        d = m
        while d < nxt:
            ds = d.isoformat(); items = data.get(ds, [])
            score = sum(c.get("impact", 1) for c in items)
            lvl = 0 if not items else 1 if score <= 2 else 2 if score <= 5 else 3 if score <= 9 else 4
            cls = f"c l{lvl}" + (" today" if ds == today else "")
            if ds in days:
                cells.append(f'<a class="{cls}" href="{report_url(ds)}" title="{E(short(ds))}: {len(items)} change{"s"*(len(items)!=1)}">{d.day}</a>')
            else:
                cells.append(f'<span class="{cls}" style="opacity:.55">{d.day}</span>')
            d += datetime.timedelta(days=1)
        out.append(f'<div><h3>{m.strftime("%B %Y")}</h3><div class="days">{"".join(cells)}</div></div>')
    scale = '<div class="scale">Quiet <i style="background:var(--sunk)"></i><i class="l1" style="background:color-mix(in srgb,var(--red) 18%,var(--sheet))"></i><i style="background:color-mix(in srgb,var(--red) 40%,var(--sheet))"></i><i style="background:color-mix(in srgb,var(--red) 65%,var(--sheet))"></i><i style="background:var(--red)"></i> Busy</div>'
    return f'<div class="cal">{"".join(out)}</div>{scale}'

def bars(rows):
    """rows: [(label, href, value_pct)] -> horizontal bar list."""
    if not rows: return ""
    mx = max(v for _, _, v in rows) or 1
    li = "".join(f'<li><a href="{h}">{E(l)}</a><span class="track"><span class="fill" style="width:{max(2, v / mx * 100):.1f}%"></span></span><span class="v">+{v:.0f}%</span></li>' for l, h, v in rows)
    return f'<ul class="bars">{li}</ul>'
