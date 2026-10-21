# Streaming price-since-launch bar chart, data from price_history.json (flagship plan, US)
import json
from PIL import Image, ImageDraw, ImageFont
G="/usr/share/fonts/truetype/sand-box/google/"
def black(s): return ImageFont.truetype(G+"Archivo Black/ArchivoBlack-Regular.ttf",s)
def inter(s,w="Bold"):
    f=ImageFont.truetype(G+"Inter/Inter-VariableFont_opsz,wght.ttf",s)
    try: f.set_variation_by_name(w)
    except Exception: pass
    return f
d0=json.load(open("/workspace/quietlychanged/price_history.json"))
names={"YouTube":"YouTube Premium","Amazon Prime":"Amazon Prime"}
rows=[]
for k,v in d0.items():
    if k.startswith("_") or v.get("compare",True) is False: continue
    p=v["plans"][v["flagship"]]; a,b=p[0],p[-1]
    rows.append((names.get(k,k),a[0][:4],a[1],b[1],round((b[1]/a[1]-1)*100),k=="Amazon Prime"))
rows.sort(key=lambda r:-r[4])
W,H=1080,1350; BG=(14,14,16); INK=(245,242,235); MUT=(150,146,140); RED=(235,64,52); DIM=(70,40,38)
im=Image.new("RGB",(W,H),BG); d=ImageDraw.Draw(im)
d.text((60,56),"US STREAMING PRICES",font=inter(30,"SemiBold"),fill=MUT)
d.text((60,96),"Launch price",font=black(76),fill=INK)
d.text((60,186),"vs. today",font=black(76),fill=RED)
top=300; rowh=82; x0=60; barx=380; barmax=W-60-barx
mx=max(r[4] for r in rows)
for i,(n,yr,a,b,pct,annual) in enumerate(rows):
    y=top+i*rowh
    d.text((x0,y+4),n,font=inter(30,"Bold"),fill=INK)
    fmt=(lambda v:f"${v:.0f}") if annual else (lambda v:f"${v:.2f}")
    sub=f"{fmt(a)} ({yr}) → {fmt(b)}"+("/yr" if annual else "")
    d.text((x0,y+42),sub,font=inter(22,"Medium"),fill=MUT)
    bw=int(barmax*pct/mx)
    col=RED if pct>=150 else (200,120,110)
    d.rounded_rectangle([barx,y+10,barx+max(bw,8),y+62],8,fill=col)
    t=f"+{pct}%"; f=black(34); tw=d.textlength(t,font=f)
    if bw>tw+30: d.text((barx+bw-tw-16,y+15),t,font=f,fill=BG if col==RED else BG)
    else: d.text((barx+bw+14,y+15),t,font=f,fill=INK)
fy=top+len(rows)*rowh+20
d.line([60,fy,W-60,fy],fill=(50,50,54),width=2)
d.text((60,fy+20),"Main plan for each service (Disney+, Hulu, Netflix ad-free; Peacock Premium).",font=inter(21,"Regular"),fill=MUT)
d.text((60,fy+50),"Netflix: first streaming-only price (2011). Prime: annual membership.",font=inter(21,"Regular"),fill=MUT)
d.text((60,fy+80),"Prices checked Oct 17–19, 2026. Sources on our price-history page.",font=inter(21,"Regular"),fill=MUT)
d.text((60,H-72),"Quietly",font=black(34),fill=INK)
d.text((60+d.textlength("Quietly",font=black(34)),H-72),"Changed",font=black(34),fill=RED)
t="quietlychanged.com/subscription-price-history"; f=inter(22,"Medium")
d.text((W-60-d.textlength(t,font=f),H-64),t,font=f,fill=MUT)
im.save("streaming-launch-vs-today.png"); print(rows)
