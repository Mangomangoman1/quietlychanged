# Deep-dive images, Oct 17 2026 (Oura, Rocket Money). Run from this folder.
from PIL import Image, ImageDraw, ImageFont
F="/usr/share/fonts/truetype/sand-box/google/IBM Plex Serif/IBMPlexSerif-"
def font(w,s): return ImageFont.truetype(F+w+".ttf", s)
RED=(179,38,30); INK=(26,26,26); BG=(251,250,247); GREY=(95,95,95); GREEN=(26,110,60)
PAPER=(255,255,253); HL=(255,226,92); RULE=(220,214,200); LIGHT=(214,209,198)
W,H=1200,675
def base(bg=BG):
    im=Image.new("RGB",(W,H),bg); d=ImageDraw.Draw(im)
    d.rectangle([0,0,W,8],fill=RED); d.rectangle([0,H-8,W,H],fill=RED)
    wf=font("Bold",30); d.text((56,28),"Quietly",font=wf,fill=INK)
    d.text((56+d.textlength("Quietly",font=wf),28),"Changed",font=wf,fill=RED)
    ff=font("Regular",21); t="quietlychanged.com"
    d.text((W-56-d.textlength(t,font=ff),36),t,font=ff,fill=GREY)
    return im,d
def wrap(d,text,f,width):
    out,line=[], ""
    for w in text.split():
        t=(line+" "+w).strip()
        if d.textlength(t,font=f)<=width: line=t
        else: out.append(line); line=w
    out.append(line); return out
def center(d,y,t,f,fill):
    d.text(((W-d.textlength(t,font=f))/2,y),t,font=f,fill=fill)

# 1) Oura: forced acceptance + fine-print crop + mass-arbitration batch grid
im,d=base()
d.text((56,84),"OURA TERMS OF USE  \u00b7  EFFECTIVE NOV 4, 2026",font=font("SemiBold",23),fill=RED)
hf=font("Bold",46); y=118
for ln in wrap(d,"Accept Oura's new terms by Nov 4, or you can't use the app.",hf,1090):
    d.text((56,y),ln,font=hf,fill=INK); y+=56
# fine-print crop (left)
px0,py0,px1,py1=56,250,676,540
d.rectangle([px0+7,py0+7,px1+7,py1+7],fill=LIGHT); d.rectangle([px0,py0,px1,py1],fill=PAPER,outline=RULE)
fr=font("Regular",22); fb=font("Bold",22); lx=px0+26; ly=py0+20
d.text((lx,ly),"XVI. United States Mandatory Arbitration",font=font("Bold",23),fill=INK); ly+=40
segs=[("...binding individual arbitration. This provision also includes a ",False),("CLASS ACTION AND JURY TRIAL WAIVER.",True),
      (" Disputes will be resolved by arbitration ",False),("\u201cregardless of when it accrued.\u201d",True),
      (" Before filing, send a written Pre-Dispute Notice and negotiate for ",False),("30 days.",True),
      (" Claims of $50,000 or less: ",False),("documents only.",True)]
x=lx; maxx=px1-26
for text,hl in segs:
    f=fb if hl else fr
    for w in text.split(" "):
        if w=="": continue
        tw=d.textlength(w,font=f); sp=d.textlength(" ",font=f)
        if x+tw>maxx: x=lx; ly+=33
        if hl: d.rectangle([x-2,ly+2,x+tw+2,ly+29],fill=HL)
        d.text((x,ly),w,font=f,fill=INK if hl else (70,70,70)); x+=tw+sp
# batch grid (right)
gx0,gy0=720,258
d.text((gx0,gy0-12),"If 25+ people file similar claims:",font=font("SemiBold",23),fill=INK)
cell=30; r=11
for i in range(60):
    cx=gx0+14+(i%12)*cell; cy=gy0+34+(i//12)*cell
    col=RED if i<20 else LIGHT
    d.ellipse([cx-r+12,cy-r+12,cx+r+12,cy+r+12],fill=col)
ly2=gy0+34+5*cell+10
d.text((gx0,ly2),"20 random cases go first.",font=font("Bold",24),fill=RED)
d.text((gx0,ly2+32),"The rest wait for the next batch.",font=font("Regular",22),fill=GREY)
d.rounded_rectangle([56,566,W-56,628],10,fill=INK)
center(d,581,"Also: 30-day fee-notice promise dropped  \u00b7  liability cap now what you paid in 12 months",font("SemiBold",22),(255,255,255))
im.save("oura-accept-or-lose-app.png")

# 2) Rocket Money: before/after + cost comparison bars
im,d=base()
d.text((56,84),"ROCKET MONEY TERMS  \u00b7  EFFECTIVE NOV 2, 2026",font=font("SemiBold",23),fill=RED)
hf=font("Bold",46)
d.text((56,118),"Bill negotiation goes subscription-only.",font=hf,fill=INK)
# before / after cards
cw=530; cy0=196; cy1=394
d.rounded_rectangle([56,cy0,56+cw,cy1],12,fill=(236,233,226))
d.text((80,cy0+16),"UNTIL NOV 2",font=font("SemiBold",21),fill=GREY)
d.text((80,cy0+46),"Pay only if it works",font=font("Bold",32),fill=INK)
yy=cy0+92
for ln in wrap(d,"35\u201360% of the first year's savings, on any plan, including free.",font("Regular",24),cw-48):
    d.text((80,yy),ln,font=font("Regular",24),fill=(70,70,70)); yy+=32
bx=W-56-cw
d.rounded_rectangle([bx,cy0,W-56,cy1],12,fill=(253,235,233))
d.text((bx+24,cy0+16),"FROM NOV 2",font=font("SemiBold",21),fill=RED)
d.text((bx+24,cy0+46),"$15/month Premium+",font=font("Bold",32),fill=INK)
yy=cy0+92
for ln in wrap(d,"No success fee. One negotiation at a time. No pay-per-use option. Auto-renegotiations end.",font("Regular",24),cw-48):
    d.text((bx+24,yy),ln,font=font("Regular",24),fill=(70,70,70)); yy+=32
# bars
d.text((56,410),"Example: a bill lowered by $10/month ($120 saved in a year)",font=font("SemiBold",24),fill=INK)
scale=600/180; bx0=330
rows=[("Old fee at 35%",42,GREEN,"$42"),("Old fee at 60%",72,GREEN,"$72"),("Premium+ for a year",180,RED,"$180")]
yb=448
for lab,v,col,txt in rows:
    d.text((56,yb+4),lab,font=font("Regular",24),fill=GREY)
    d.rounded_rectangle([bx0,yb,bx0+int(v*scale),yb+36],6,fill=col)
    d.text((bx0+int(v*scale)+12,yb+2),txt,font=font("Bold",26),fill=INK); yb+=46
center(d,606,"Premium+ also includes Rowan and savings-account access, and bills monthly whether or not a bill comes down. Before tax.",font("Italic",19),GREY)
im.save("rocket-money-negotiation-premium-plus.png")
