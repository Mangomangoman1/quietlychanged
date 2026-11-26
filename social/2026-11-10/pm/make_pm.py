from PIL import Image, ImageDraw
exec(open("../../2026-10-29/pm/helpers.py").read())
# R1: Costco food court vs No Tip delivered price
im,d=base()
d.text((56,84),"COSTCO FOOD COURT, DELIVERED BY \u201cNO TIP\u201d (SOUTHERN CALIFORNIA)",font=font("SemiBold",22),fill=RED)
d.text((56,116),"Same food. Up to 12x the price.",font=font("Bold",44),fill=INK)
items=[("Hot dog + drink combo",1.50,18.00),("Whole pizza",9.95,30.00),("Chicken chef salad",7.99,28.00)]
y=210; maxv=40.0; x0=420; span=640
for name,a,b in items:
    d.text((56,y+8),name,font=sans("Bold",28),fill=INK)
    wa=max(6,int(span*a/maxv)); wb=int(span*b/maxv)
    d.rectangle((x0,y,x0+wa,y+38),fill=GREY); d.text((x0+wa+12,y+2),f"${a:.2f} at Costco",font=sans("Regular",26),fill=GREY)
    d.rectangle((x0,y+48,x0+wb,y+90),fill=RED); d.text((x0+wb+12,y+52),f"${b:.2f}",font=sans("Bold",30),fill=RED)
    d.text((x0+10,y+54),f"{b/a:.0f}x" if b/a>=10 else f"{b/a:.1f}x",font=sans("Bold",28),fill=(255,255,255))
    y+=130
d.text((56,600),"No Tip's prices are all-inclusive (no tips or fees); pitched mainly as office catering.",font=sans("Regular",20),fill=INK)
d.text((56,630),"Prices as reported by SFGate and The Independent, Nov 9, 2026.",font=sans("Regular",18),fill=GREY)
im.save("r1-01-costco-vs-notip-chart.png")
# R2: Apple status card
def rows_card(fn,kicker,title,rows,src,hl=None):
    im,d=base()
    d.text((56,84),kicker,font=font("SemiBold",22),fill=RED)
    d.text((56,116),title,font=font("Bold",40),fill=INK)
    y=196
    for i,(a,b) in enumerate(rows):
        if hl==i: d.rectangle((48,y-6,1152,y+44),fill=(255,243,176))
        d.text((56,y),a,font=sans("Bold",27),fill=INK)
        d.text((430,y),b,font=sans("Regular",27),fill=RED if hl==i else INK)
        y+=56
    d.text((56,620),src,font=sans("Regular",18),fill=GREY)
    im.save(fn)
rows_card("r2-02-apple-status-card.png","APPLE SYSTEM STATUS  \u00b7  NOV 10, 2026","What Apple says is down right now",
 [("iCloud Account & Sign In","Outage since 2:49 PM PT"),
  ("iCloud Mail","Outage"),("iCloud Calendar / Contacts","Outage"),
  ("Photos","Outage"),("iWork for iCloud","Outage"),("Game Center","Outage"),
  ("Find My","May be slow or unavailable (2:50 PM PT)")],
 "Source: apple.com/support/systemstatus (checked 5:17 PM MT / 4:17 PM PT). Apple: \u201cSome users are affected.\u201d",hl=0)
