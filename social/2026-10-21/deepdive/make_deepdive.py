# Deep-dive images, Oct 21 2026 (Shein Customer Support "courtesy" clause; IPL ipl.org shutdown Nov 9). Run from this folder.
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

# 1) Shein: support is "a courtesy" (highlighted fine-print crop + who's on the hook)
im,d=base()
d.text((56,84),"SHEIN U.S. TERMS OF USE  \u00b7  EFFECTIVE OCT 21, 2026",font=font("SemiBold",23),fill=RED)
hf=font("Bold",42); y=116
for ln in wrap(d,"Shein\u2019s new terms: help with your order is \u201ca courtesy.\u201d",hf,1090):
    d.text((56,y),ln,font=hf,fill=INK); y+=52
# fine-print card
x0,y0,x1,y1=56,236,750,522
card(d,x0,y0,x1,y1)
d.text((x0+24,y0+16),"NEW  \u00a717. CUSTOMER SUPPORT",font=mono("SemiBold",19),fill=RED)
body=font("Regular",18); bold=font("Bold",18)
segs=[("SHEIN may, in its discretion, assist with questions about the shipment, delivery, return, refund, or payment of an order. Unless a SHEIN policy expressly states otherwise,",False),
      ("any such assistance is a courtesy and does not create a contractual obligation",True),
      (" for SHEIN to resolve issues caused by carriers, banks, payment processors, Third-Party Sellers, or other third parties.",False),
      (" Where a third party\u2019s involvement is necessary to resolve your issue, ",False),
      ("we may refer you to that third party.",True)]
words=[]
for t,h in segs:
    for w in t.replace(" .",".").split(" "):
        if w: words.append((w,h))
lx=x0+24; ly=y0+50; maxx=x1-24; lh=28
for w,h in words:
    f=bold if h else body
    ww=d.textlength(w,font=f); sp=d.textlength(" ",font=body)
    if lx+ww>maxx: lx=x0+24; ly+=lh
    if h: d.rectangle([lx-2,ly-1,lx+ww+sp,ly+25],fill=HL)
    d.text((lx,ly),w,font=f,fill=INK); lx+=ww+sp
d.text((x0+24,y1-28),"us.shein.com/Terms-and-Conditions-a-399.html (excerpt)",font=mono("Regular",14),fill=GREY)
# right: problem -> who Shein may send you to
rx=786
d.text((rx,240),"IF THE PROBLEM IS\u2026",font=mono("SemiBold",19),fill=GREY)
rows=[("Lost or late package","the carrier"),("Payment declined or doubled","your bank"),("Marketplace seller item","the seller")]
for i,(a,b) in enumerate(rows):
    yy=274+i*82
    d.rounded_rectangle([rx,yy,1144,yy+68],8,fill=PAPER,outline=RULE,width=2)
    d.text((rx+16,yy+8),a,font=font("SemiBold",20),fill=INK)
    d.text((rx+16,yy+36),"\u2192 may be referred to "+b,font=font("Regular",17),fill=RED)
# bottom bar
d.rounded_rectangle([56,544,1144,626],10,fill=INK)
d.text((80,554),"STILL IN WRITING",font=mono("SemiBold",19),fill=HL)
d.text((80,584),"Lost/damaged package claims to Shein within 14 days. Credit card disputes: 60 days from the bill.",font=font("SemiBold",20),fill=(255,255,255))
im.save("shein-support-a-courtesy.png")

# 2) IPL: ipl.org goes dark Nov 9 (timeline)
im,d=base()
d.text((56,84),"IPL (IPL.ORG)  \u00b7  RETIRING",font=font("SemiBold",23),fill=RED)
hf=font("Bold",42); y=116
for ln in wrap(d,"ipl.org goes offline Nov 9. Nothing you uploaded is moved anywhere.",hf,1090):
    d.text((56,y),ln,font=hf,fill=INK); y+=52
# timeline
ty=330; d.line([90,ty,1110,ty],fill=RULE,width=6)
pts=[(120,"1995","Internet Public Library opens",GREY,False),(420,"2015","nonprofit library stops",GREY,False),
     (690,"~2020","domain reopens as an essay site",GREY,False),(1040,"NOV 9, 2026","site taken offline",RED,True)]
for x,yr,lab,c,big in pts:
    r=16 if big else 11
    d.ellipse([x-r,ty-r,x+r,ty+r],fill=c)
    yf=font("Bold",44 if big else 30)
    tw=d.textlength(yr,font=yf); xx=min(max(56,x-tw/2),1144-tw)
    d.text((xx,ty-(78 if big else 58)),yr,font=yf,fill=c)
    lf=font("Italic" if not big else "SemiBold",18)
    lw=d.textlength(lab,font=lf); lx=min(max(56,x-lw/2),1144-lw)
    d.text((lx,ty+26),lab,font=lf,fill=INK if big else GREY)
# what goes
items=["Logins disabled","Uploads unrecoverable","Public pages removed","Accounts & data deleted"]
bx=56; by=410
for i,t in enumerate(items):
    x=bx+i*276
    d.rounded_rectangle([x,by,x+258,by+60],8,fill=PAPER,outline=RED,width=2)
    f=font("SemiBold",20); d.text((x+(258-d.textlength(t,font=f))/2,by+17),t,font=f,fill=INK)
d.rounded_rectangle([56,500,1144,610],10,fill=INK)
q="\u201cWe are not migrating any content or product features from IPL to a new platform.\u201d"
qf=font("SemiBold",23); d.text(((W-d.textlength(q,font=qf))/2,516),q,font=qf,fill=HL)
s="Download your files before Nov 9. Subscribers with time left: watch for a prorated refund email."
sf=font("Regular",20); d.text(((W-d.textlength(s,font=sf))/2,562),s,font=sf,fill=(255,255,255))
im.save("ipl-org-offline-nov9.png")
