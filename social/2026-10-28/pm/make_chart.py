import json, matplotlib; matplotlib.use("Agg"); matplotlib.rcParams["text.usetex"]=False; matplotlib.rcParams["text.parse_math"]=False
import matplotlib.pyplot as plt
from datetime import date
d=json.load(open("/workspace/quietlychanged/price_history.json"))["YouTube"]["plans"]
def pd(s):
    p=s.split("-"); return date(int(p[0]),int(p[1]),int(p[2]) if len(p)>2 else 1)
fig,ax=plt.subplots(figsize=(12,6.75),dpi=100)
end=date(2026,10,28)
for plan,col in (("Individual","#FF0000"),("Family","#282828")):
    pts=[(pd(a),b) for a,b in d[plan]]
    xs=[p[0] for p in pts]+[end]; ys=[p[1] for p in pts]+[pts[-1][1]]
    ax.step(xs,ys,where="post",color=col,lw=4,label=plan)
    for x,y in pts: ax.annotate(f"${y:.2f}",(x,y),xytext=(4,8),textcoords="offset points",fontsize=15,fontweight="bold",color=col)
ax.set_title("YouTube Premium monthly price (US): it only goes one way",fontsize=22,fontweight="bold",loc="left",pad=16)
ax.set_ylim(0,31); ax.set_yticks([0,10,20,30]); ax.set_yticklabels(["$0","$10","$20","$30"],fontsize=14)
ax.tick_params(axis="x",labelsize=14); ax.grid(axis="y",alpha=.3)
for s in ("top","right"): ax.spines[s].set_visible(False)
ax.legend(fontsize=16,frameon=False,loc="upper left")
fig.text(0.01,0.015,"Individual: $9.99 (YouTube Red, Oct 2015), $11.99 (Jun 2018), $13.99 (Jul 2023), $15.99 (Apr 10, 2026)\nFamily: $17.99 (Jun 2018), $22.99 (Oct 2022), $26.99 (Apr 10, 2026).  Sources: quietlychanged.com/services/youtube/ ",fontsize=11,color="#555")
plt.tight_layout(rect=(0,0.07,1,1)); plt.savefig("r1-02-youtube-price-history.png")
