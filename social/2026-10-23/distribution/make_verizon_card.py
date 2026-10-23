#!/usr/bin/env python3
"""Big-number graphic: Verizon admin charge $3.78 -> $4.69 (Nov 15, 2026) with fee history bars."""
from PIL import Image, ImageDraw, ImageFont
F="/usr/share/fonts/truetype/sand-box/google/IBM Plex Serif/IBMPlexSerif-"
def f(w,s): return ImageFont.truetype(F+w+".ttf", s)
RED=(179,38,30); INK=(28,28,28); BG=(249,247,242); GREY=(95,95,95); LG=(205,200,190)
W,H=1200,675
im=Image.new("RGB",(W,H),BG); d=ImageDraw.Draw(im)
d.rectangle([0,0,W,8],fill=RED); d.rectangle([0,H-8,W,H],fill=RED)
d.text((56,34),"VERIZON ADMINISTRATIVE & TELCO RECOVERY CHARGE",font=f("SemiBold",26),fill=RED)
d.text((56,72),"per voice line, per month",font=f("Regular",26),fill=GREY)
# big numbers
d.text((56,120),"$3.78",font=f("Bold",120),fill=GREY)
x=56+d.textlength("$3.78",font=f("Bold",120))+30
d.text((x,150),"→",font=f("Bold",90),fill=INK)
x2=x+d.textlength("→",font=f("Bold",90))+30
d.text((x2,120),"$4.69",font=f("Bold",120),fill=RED)
d.text((56,275),"Nov 15, 2026  ·  +$0.91 (+24%)  ·  not a tax, Verizon keeps it",font=f("SemiBold",30),fill=INK)
d.text((56,318),"With the Regulatory Charge (Nov 1): $3.99 → $4.95 a line. Price locks don't cover it.",font=f("Regular",25),fill=GREY)
# bars
hist=[("2005",0.40),("2007",0.70),("2015",1.23),("2019",1.78),("2020",1.95),("2022",3.30),("2024",3.50),("2025",3.78),("Nov '26",4.69)]
bx0,by1,bw,gap=70,575,100,26; maxv=4.69; maxh=190
for i,(lab,v) in enumerate(hist):
    x=bx0+i*(bw+gap); h=int(v/maxv*maxh); c=RED if i==len(hist)-1 else LG
    d.rectangle([x,by1-h,x+bw,by1],fill=c)
    d.text((x+bw/2,by1-h-6),f"${v:.2f}",font=f("SemiBold",22),fill=RED if c==RED else INK,anchor="ms")
    d.text((x+bw/2,by1+28),lab,font=f("Regular",21),fill=GREY,anchor="ms")
d.text((W-56,H-22),"Source: verizon.com/support/important-plan-information  ·  QuietlyChanged",font=f("Regular",18),fill=GREY,anchor="rs")
im.save("verizon-admin-charge-4-69.png"); print("ok")
