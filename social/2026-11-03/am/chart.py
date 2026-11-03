import json
from PIL import Image, ImageDraw, ImageFont
d=json.load(open('/workspace/quietlychanged/price_history.json'))
spec=[("Disney+","Disney+","Premium (no ads)"),("Hulu","Hulu","No Ads"),("Peacock","Peacock","Premium (with ads)"),
("Apple TV","Apple TV","Monthly"),("Netflix","Netflix","Standard"),("Spotify","Spotify","Individual"),
("HBO Max","HBO Max","Standard"),("Paramount+","Paramount+","Premium"),("YouTube Premium","YouTube","Individual")]
rows=[]
for label,key,plan in spec:
    p=d[key]['plans'][plan]
    before=[x for x in p if x[0]<'2022-01-01'][-1][1]
    inc=[x for x in p if x[0]>='2022-01-01' and x[2:] is not None]
    ups=0;prev=before
    for x in p:
        if x[0]>='2022-01-01':
            if x[1]>prev: ups+=1
            prev=x[1]
    now=p[-1][1]
    rows.append((label,ups,before,now))
rows.sort(key=lambda r:(-r[1],-(r[3]-r[2])/r[2]))
for r in rows: print(r)
json.dump(rows,open('chart-data.json','w'))
F="/usr/share/fonts/truetype/sand-box/google/Inter/Inter-VariableFont_opsz,wght.ttf"
def font(s,w=700):
    f=ImageFont.truetype(F,s)
    try: f.set_variation_by_axes([32 if s>30 else 14,w])
    except Exception as e: pass
    return f
W,H=1200,675
BG=(249,247,242);INK=(28,28,28);RED=(179,38,30);TRACK=(236,233,226);GREY=(110,110,110)
im=Image.new("RGB",(W,H),BG);dr=ImageDraw.Draw(im)
dr.text((50,28),"Times each service raised its price since 2022",font=font(46,800),fill=INK)
dr.text((50,86),"Main US plan, new-subscriber list price",font=font(26,500),fill=GREY)
x0=330;x1=840;y=140;rh=44;mx=max(r[1] for r in rows)
for label,n,b,nw in rows:
    dr.text((50,y+4),label,font=font(30,700),fill=INK)
    dr.rounded_rectangle([x0,y+4,x1,y+rh-6],6,fill=TRACK)
    w=(x1-x0)*n/mx
    dr.rounded_rectangle([x0,y+4,x0+w,y+rh-6],6,fill=RED)
    dr.text((x0+w-16-dr.textlength(str(n),font=font(30,800)),y+4),str(n),font=font(30,800),fill="white")
    fmt=lambda v: f"${v:.2f}"
    dr.text((x1+24,y+8),f"{fmt(b)} \u2192 {fmt(nw)}",font=font(26,600),fill=INK)
    y+=rh+6
dr.text((50,H-48),"Count of list-price raises since Jan 1, 2022: price at end of 2021 vs today. quietlychanged.com",font=font(19,500),fill=GREY)
im.save("01-raises-since-2022-chart.png")
