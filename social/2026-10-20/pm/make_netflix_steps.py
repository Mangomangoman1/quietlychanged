import json, datetime as dt
import matplotlib
matplotlib.rcParams["text.usetex"]=False
matplotlib.rcParams["text.parse_math"]=False
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager
d = json.load(open("/workspace/quietlychanged/price_history.json"))["Netflix"]["plans"]
def parse(s):
    p = s.split("-"); return dt.date(int(p[0]), int(p[1]), int(p[2]) if len(p) > 2 else 1)
std = [(parse(a), b) for a, b in d["Standard"]]
ads = [(parse(a), b) for a, b in d["Standard with ads"]]
end = dt.date(2026, 10, 20)
fig = plt.figure(figsize=(12, 6.75), dpi=100)
fig.patch.set_facecolor("white")
ax = fig.add_axes([0.07, 0.11, 0.62, 0.62])
def steps(series, color, lw):
    xs, ys = [], []
    for i, (x, y) in enumerate(series):
        nx = series[i+1][0] if i+1 < len(series) else end
        xs += [x, nx]; ys += [y, y]
    ax.plot(xs, ys, color=color, lw=lw, solid_capstyle="butt")
steps(std, "#E50914", 6)
steps(ads, "#888888", 4)
for x, y in std:
    ax.scatter([x], [y], s=60, color="#E50914", zorder=3)
    ax.annotate(f"${y:.2f}", (x, y), textcoords="offset points", xytext=(0, 10), ha="center", fontsize=13, fontweight="bold", color="#111")
ax.annotate("plan with ads: $6.99 (2022) → $8.99", (ads[-1][0], ads[-1][1]), textcoords="offset points", xytext=(-250, -62), fontsize=13, color="#555", fontweight="bold")
ax.set_ylim(0, 23); ax.set_xlim(dt.date(2010, 9, 1), dt.date(2027, 1, 1))
for s in ["top", "right", "left"]: ax.spines[s].set_visible(False)
ax.set_yticks([]); ax.tick_params(axis="x", labelsize=13, colors="#444")
fig.text(0.07, 0.86, "Netflix's ad-free plan, 2011 to today", fontsize=34, fontweight="bold", color="#111")
fig.text(0.07, 0.79, "US Standard plan, monthly price at each change", fontsize=17, color="#555")
fig.text(0.74, 0.62, "8", fontsize=120, fontweight="bold", color="#E50914", va="center")
fig.text(0.74, 0.47, "price increases", fontsize=22, fontweight="bold", color="#111")
fig.text(0.74, 0.27, "0", fontsize=120, fontweight="bold", color="#111", va="center")
fig.text(0.74, 0.12, "price cuts", fontsize=22, fontweight="bold", color="#111")
fig.text(0.07, 0.03, "Sources: Netflix price changes as reported by Reuters (Mar 26, 2026) and earlier coverage  ·  @QuietlyChanged  ·  quietlychanged.com", fontsize=11, color="#777")
fig.savefig("/workspace/quietlychanged/social/2026-10-20/pm/netflix-8-up-0-down.png", dpi=100, facecolor="white")
