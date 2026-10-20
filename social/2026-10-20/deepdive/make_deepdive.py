# Deep-dive images, Oct 20 2026 (Pinterest Nov 12 arbitration + opt-out; IKEA Gift Registry shutdown). Run from this folder.
from PIL import Image, ImageDraw, ImageFont
G="/usr/share/fonts/truetype/sand-box/google/"
def font(w,s): return ImageFont.truetype(G+"IBM Plex Serif/IBMPlexSerif-"+w+".ttf", s)
def mono(w,s): return ImageFont.truetype(G+"IBM Plex Mono/IBMPlexMono-"+w+".ttf", s)
def sans(w,s):
    f=ImageFont.truetype(G+"IBM Plex Sans/IBMPlexSans-VariableFont_wdth,wght.ttf", s)
    try: f.set_variation_by_name(w)
    except Exception: pass
    return f
RED=(179,38,30); INK=(26,26,26); BG=(251,250,247); GREY=(95,95,95); GREEN=(26,110,60)
PAPER=(255,255,253); HL=(255,226,92); RULE=(220,214,200); LIGHT=(214,209,198)
W,H=1200,675
def base():
    im=Image.new("RGB",(W,H),BG); d=ImageDraw.Draw(im)
    d.rectangle([0,0,W,8],fill=RED); d.rectangle([0,H-8,W,H],fill=RED)
    wf=font("Bold",30); d.text((56,28),"Quietly",font=wf,fill=INK)
    d.text((56+d.textlength("Quietly",font=wf),28),"Changed",font=wf,fill=RED)
    ff=font("Regular",21); t="quietlychanged.com"
    d.text((W-56-d.textlength(t,font=ff),36),t,font=ff,fill=GREY)
    return im,d
def wrap(d,text,f,width):
    out,line=[],""
    for w in text.split():
        t=(line+" "+w).strip()
        if d.textlength(t,font=f)<=width: line=t
        else: out.append(line); line=w
    out.append(line); return out
def card(d,x0,y0,x1,y1,outline=RULE,width=2):
    d.rectangle([x0+7,y0+7,x1+7,y1+7],fill=LIGHT); d.rectangle([x0,y0,x1,y1],fill=PAPER,outline=outline,width=width)
def dots(d,x,y,n,cols,r,gap,fill):
    for i in range(n):
        cx=x+(i%cols)*gap; cy=y+(i//cols)*gap
        d.ellipse([cx-r,cy-r,cx+r,cy+r],fill=fill)

# 1) Pinterest: mass claims to one arbitrator + 30-day opt-out
im,d=base()
d.text((56,84),"PINTEREST TERMS OF SERVICE  \u00b7  EFFECTIVE NOV 12, 2026",font=font("SemiBold",23),fill=RED)
hf=font("Bold",42); y=116
for ln in wrap(d,"Pinterest rewrote its arbitration clause. You get 30 days to opt out.",hf,1090):
    d.text((56,y),ln,font=hf,fill=INK); y+=52
# before card
bx0,by0,bx1,by1=56,236,560,470
card(d,bx0,by0,bx1,by1)
d.text((bx0+22,by0+16),"TODAY",font=mono("SemiBold",20),fill=GREY)
d.text((bx0+22,by0+44),"25+ similar claims are split into",font=font("Regular",21),fill=INK)
d.text((bx0+22,by0+72),"batches, one arbitrator per batch",font=font("Regular",21),fill=INK)
for k in range(3):
    gx=bx0+40+k*160
    dots(d,gx,by0+128,9,3,8,24,GREY)
    d.line([gx+24,by0+200,gx+24,by0+214],fill=GREY,width=3)
    d.text((gx-6,by0+214),"1 arbitrator",font=mono("Regular",15),fill=GREY)
# arrow
ax=578; ay=(by0+by1)//2
d.line([ax,ay,ax+40,ay],fill=RED,width=6); d.polygon([(ax+40,ay-13),(ax+62,ay),(ax+40,ay+13)],fill=RED)
# after card
cx0,cy0,cx1,cy1=652,236,1144,470
card(d,cx0,cy0,cx1,cy1,outline=RED,width=3)
d.text((cx0+22,cy0+16),"FROM NOV 12",font=mono("SemiBold",20),fill=RED)
fb=font("Bold",21)
t1="all of those Claims will be consolidated"; t2="into one arbitration before one arbitrator"
for i,t in enumerate([t1,t2]):
    tw=d.textlength(t,font=fb); yy=cy0+44+i*30
    d.rectangle([cx0+20,yy-1,cx0+26+tw,yy+27],fill=HL); d.text((cx0+23,yy),t,font=fb,fill=INK)
dots(d,cx0+40,cy0+128,27,9,8,24,INK)
d.line([cx0+136,cy0+200,cx0+136,cy0+214],fill=RED,width=3)
d.text((cx0+76,cy0+214),"1 arbitrator",font=mono("SemiBold",15),fill=RED)
d.text((cx0+262,cy0+118),"Also new:",font=font("SemiBold",17),fill=GREY)
for i,t in enumerate(["moves to JAMS","covers past claims","confidential","fees can shift to claimants"]):
    d.text((cx0+262,cy0+142+i*21),("\u2022 " if i<4 else "   ")+t,font=font("Regular",16),fill=INK)
# opt-out bar
d.rounded_rectangle([56,496,1144,582],10,fill=INK)
d.text((80,508),"NEW 30-DAY OPT-OUT",font=mono("SemiBold",20),fill=HL)
ot="Email litigation@pinterest.com: your name, account email, \u201cI\u2019m opting out of Section 11.\u201d"
d.text((80,540),ot,font=font("SemiBold",22),fill=(255,255,255))
ft="Safest window for existing users: Nov 12 \u2013 Dec 12, 2026. Same update adds connected-TV ads and household device matching."
f3=font("Italic",19); d.text(((W-d.textlength(ft,font=f3))/2,602),ft,font=f3,fill=GREY)
im.save("pinterest-arbitration-optout.png")

# 2) IKEA: Gift Registry deleted after Dec 27, 2026
im,d=base()
d.text((56,84),"IKEA GIFT REGISTRY  \u00b7  SHUTTING DOWN",font=font("SemiBold",23),fill=RED)
hf=font("Bold",44); y=118
for ln in wrap(d,"Got an IKEA registry for a 2027 wedding? It\u2019s about to vanish.",hf,1090):
    d.text((56,y),ln,font=hf,fill=INK); y+=54
# big date (left)
d.text((56,252),"AFTER",font=mono("SemiBold",26),fill=GREY)
bf=font("Bold",150); d.text((50,276),"DEC 27",font=bf,fill=RED)
d.text((60,452),"2026",font=font("Bold",64),fill=INK)
d.text((232,476),"registry accounts no longer accessible",font=font("Italic",22),fill=GREY)
# registry card (right)
rx0,ry0,rx1,ry1=640,244,1144,500
card(d,rx0,ry0,rx1,ry1)
d.text((rx0+24,ry0+18),"OUR WEDDING REGISTRY",font=mono("SemiBold",19),fill=GREY)
items=["Dinnerware set, 18 pc","Bed frame, queen","Duvet + covers","Bookcase","Glassware, 12 pc"]
fr=font("Regular",22)
for i,t in enumerate(items):
    yy=ry0+54+i*38
    d.rectangle([rx0+24,yy+4,rx0+42,yy+22],outline=GREY,width=2)
    d.text((rx0+56,yy),t,font=fr,fill=(150,150,150))
    d.line([rx0+52,yy+15,rx0+60+d.textlength(t,font=fr),yy+15],fill=RED,width=3)
d.text((rx1-d.textlength("illustration",font=font("Italic",15)),ry1+12),"illustration",font=font("Italic",15),fill=GREY)
# quote bar
d.rounded_rectangle([56,548,1144,636],10,fill=INK)
q="\u201cItems saved in your registry will be fully deleted.\u201d"
qf=font("SemiBold",26); tw=d.textlength(q,font=qf)
d.text(((W-tw)/2,558),q,font=qf,fill=HL)
s="Not transferred anywhere. Copy each item to a Favorites list and re-share the link before Dec 27."
sf=font("Regular",20); d.text(((W-d.textlength(s,font=sf))/2,600),s,font=sf,fill=(255,255,255))
im.save("ikea-gift-registry-deleted-dec27.png")
print("ok")
