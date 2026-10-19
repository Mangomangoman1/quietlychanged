# Deep-dive images, Oct 19 2026 (USPS customs billing, Verizon Glance rewards). Run from this folder.
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

# 1) USPS: postage receipt now -> invoice later
im,d=base()
d.text((56,84),"USPS INTERNATIONAL MAIL RULE  \u00b7  EFFECTIVE OCT 19, 2026",font=font("SemiBold",23),fill=RED)
hf=font("Bold",44); y=118
for ln in wrap(d,"Mailed a gift abroad? USPS can now bill you later for the duties.",hf,1090):
    d.text((56,y),ln,font=hf,fill=INK); y+=54
# receipt (left)
rx0,ry0,rx1,ry1=56,244,400,574
d.rectangle([rx0+7,ry0+7,rx1+7,ry1+7],fill=LIGHT); d.rectangle([rx0,ry0,rx1,ry1],fill=PAPER,outline=RULE)
m=mono("Regular",21); mb=mono("SemiBold",21)
ly=ry0+22
d.text((rx0+24,ly),"AT THE COUNTER",font=mono("SemiBold",19),fill=GREY); ly+=40
for a,b in [("Package to","Germany"),("Contents","Gift"),("Postage","PAID")]:
    d.text((rx0+24,ly),a,font=m,fill=INK); d.text((rx1-24-d.textlength(b,font=mb),ly),b,font=mb,fill=GREEN if b=="PAID" else INK); ly+=38
d.line([rx0+24,ly+6,rx1-24,ly+6],fill=RULE,width=2); ly+=24
for ln in wrap(d,"Duties, taxes and import fees are not included in postage.",font("Italic",20),rx1-rx0-48):
    d.text((rx0+24,ly),ln,font=font("Italic",20),fill=GREY); ly+=28
# arrow
ax=430; ay=(ry0+ry1)//2
d.line([ax,ay,ax+62,ay],fill=RED,width=6); d.polygon([(ax+62,ay-14),(ax+86,ay),(ax+62,ay+14)],fill=RED)
d.text((ax-6,ay+22),"later",font=font("Italic",22),fill=RED)
# invoice (right)
ix0,iy0,ix1,iy1=536,244,1144,574
d.rectangle([ix0+7,iy0+7,ix1+7,iy1+7],fill=LIGHT); d.rectangle([ix0,iy0,ix1,iy1],fill=PAPER,outline=RED,width=3)
ly=iy0+18
d.text((ix0+26,ly),"INVOICE TO THE MAILER",font=mono("SemiBold",21),fill=RED); ly+=38
rows=[("Unpaid foreign duties, taxes, import fees","owed by you"),
      ("Disagree with the amount?","pay it anyway"),
      ("Delivered, lost, damaged or returned?","still owed"),
      ("Paid late?","6% interest + collection costs")]
fr=font("Regular",22); fb=font("Bold",22)
for a,b in rows:
    d.text((ix0+26,ly),a,font=fr,fill=INK); ly+=29
    tw=d.textlength(b,font=fb); d.rectangle([ix0+24,ly-2,ix0+32+tw,ly+28],fill=HL)
    d.text((ix0+28,ly),b,font=fb,fill=INK); ly+=38
# footer bar
d.rounded_rectangle([56,598,1144,646],8,fill=INK)
ft="Why now: the EU ended duty-free entry for most low-value goods on July 1."
f2=font("SemiBold",22); d.text(((W-d.textlength(ft,font=f2))/2,608),ft,font=f2,fill=(255,255,255))
im.save("usps-sender-billed-foreign-duties.png")

# 2) Verizon: $5/month for switching privacy protections off
im,d=base()
d.text((56,84),"VERIZON DOLLARS  \u00b7  GLANCE LOCK SCREEN REWARDS",font=font("SemiBold",23),fill=RED)
hf=font("Bold",44); y=118
for ln in wrap(d,"Verizon's $5-a-month deal: keep these privacy settings the way Glance wants.",hf,1090):
    d.text((56,y),ln,font=hf,fill=INK); y+=54
# settings card (left)
cx0,cy0,cx1,cy1=56,250,780,600
d.rectangle([cx0+7,cy0+7,cx1+7,cy1+7],fill=LIGHT); d.rounded_rectangle([cx0,cy0,cx1,cy1],14,fill=PAPER,outline=RULE,width=2)
rows=[("Do not sell or share my personal info",False),("Limit use of my sensitive personal info",False),
      ("Location access for Glance",True),("Enhanced browsing",True),("iPhone: \u201cAsk App Not to Track\u201d",False)]
sf=sans("Medium",25); ly=cy0+24
def toggle(x,y,on):
    w,h=78,40; col=GREEN if on else (200,196,188)
    d.rounded_rectangle([x,y,x+w,y+h],h//2,fill=col)
    kx=x+w-h+4 if on else x+4; d.ellipse([kx,y+4,kx+h-8,y+h-4],fill=(255,255,255))
for i,(lab,on) in enumerate(rows):
    if i: d.line([cx0+24,ly-12,cx1-24,ly-12],fill=RULE,width=1)
    d.text((cx0+26,ly+4),lab,font=sf,fill=INK)
    toggle(cx1-26-78-118,ly,on)
    req="must be ON" if on else ("can't pick it" if lab.startswith("iPhone") else "must be OFF")
    d.text((cx1-26-108,ly+8),req,font=sans("SemiBold",19),fill=RED)
    ly+=64
# big number (right)
bx=820
d.text((bx,262),"$5",font=font("Bold",150),fill=RED)
d.text((bx+4,440),"a month in Verizon Dollars",font=font("SemiBold",24),fill=INK)
for i,ln in enumerate(["for 60 minutes of active","Glance use each month.","Max $60 a year."]):
    d.text((bx+4,478+i*32),ln,font=font("Regular",23),fill=GREY)
d.text((56,616),"\u201cGlance requires you to share personal information, including sensitive personal information\u201d \u2014 Verizon terms \u00a710.2",font=font("Italic",19),fill=GREY)
im.save("verizon-glance-5-dollar-privacy-toggles.png")
print("ok")
