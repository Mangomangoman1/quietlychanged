# Deep-dive image, Oct 25 2026 (AT&T Nov 1 / Cricket Dec 1 small-claims 60-day wait). Run from this folder.
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



im,d=base()
d.text((56,84),"AT&T TERMS NOV 1  \u00b7  CRICKET WIRELESS TERMS DEC 1",font=font("SemiBold",23),fill=RED)
hf=font("Bold",42); y=118
for ln in wrap(d,"Want to take your carrier to small claims court? Soon you\u2019ll have to wait first.",hf,1090):
    d.text((56,y),ln,font=hf,fill=INK); y+=52
# left: big number
lx0,ly0,lx1,ly1=56,236,430,598
card(d,lx0,ly0,lx1,ly1,outline=RED,width=3)
d.text((lx0+26,ly0+16),"NEW WAITING PERIOD",font=mono("SemiBold",16),fill=RED)
bf=font("Bold",150); t="60"; tw=d.textlength(t,font=bf)
d.text(((lx0+lx1-tw)/2,ly0+38),t,font=bf,fill=INK)
t="DAYS"; f2=font("Bold",40); d.text(((lx0+lx1-d.textlength(t,font=f2))/2,ly0+210),t,font=f2,fill=INK)
sf=sans("Regular",19); yy=ly0+270
for ln in wrap(d,"after they receive your signed Notice of Dispute, before small claims court",sf,lx1-lx0-52):
    d.text(((lx0+lx1-d.textlength(ln,font=sf))/2,yy),ln,font=sf,fill=GREY); yy+=26
# right: redline
rx0,ry0,rx1,ry1=464,236,1144,598
card(d,rx0,ry0,rx1,ry1)
d.text((rx0+22,ry0+16),"SECTION 1.3, DISPUTE RESOLUTION",font=mono("SemiBold",16),fill=RED)
d.text((rx0+22,ry0+50),"BEFORE",font=mono("SemiBold",15),fill=GREY)
tf=font("Regular",21); yy=ry0+74
old="\u201cyou can choose to file your individual claim in small claims court or send us a Notice of Dispute\u201d"
for ln in wrap(d,old,tf,rx1-rx0-44):
    d.text((rx0+22,yy),ln,font=tf,fill=GREY); lw=d.textlength(ln,font=tf)
    d.line([rx0+22,yy+15,rx0+22+lw,yy+15],fill=RED,width=3); yy+=31
d.text((rx0+22,yy+16),"AFTER",font=mono("SemiBold",15),fill=GREEN)
yy+=42; bt=font("Bold",22)
new="\u201cAny arbitration or small claims court proceeding cannot begin until after the Informal Resolution Period has ended.\u201d"
for ln in wrap(d,new,bt,rx1-rx0-44):
    lw=d.textlength(ln,font=bt); d.rectangle([rx0+20,yy-1,rx0+24+lw,yy+29],fill=HL)
    d.text((rx0+22,yy),ln,font=bt,fill=INK); yy+=34
d.text((rx0+22,ry1-40),"Informal Resolution Period = at least 60 days after they get it",font=sans("Medium",18),fill=GREY)
d.text((56,618),"Cricket also drops online dispute notices (mail only). You can reject by mail within 30 days of the change notice.",font=sans("Regular",18),fill=GREY)
im.save("att-cricket-small-claims-60-days.png"); print("saved")
