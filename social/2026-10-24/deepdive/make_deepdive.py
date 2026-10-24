# Deep-dive image, Oct 24 2026 (FCC robocall/robotext opt-out rule effective Nov 25). Run from this folder.
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
d.text((56,84),"FCC ROBOCALL & ROBOTEXT RULE  \u00b7  EFFECTIVE NOV 25, 2026",font=font("SemiBold",23),fill=RED)
hf=font("Bold",42); y=118
for ln in wrap(d,"Companies can now pick the only way you\u2019re allowed to say stop.",hf,1090):
    d.text((56,y),ln,font=hf,fill=INK); y+=52
# left: phone-style chat
px0,py0,px1,py1=56,236,540,598
card(d,px0,py0,px1,py1)
d.text((px0+22,py0+14),"YOUR REPLY TO A COMPANY THAT PICKED \u201cSTOP\u201d",font=mono("SemiBold",16),fill=GREY)
rows=[("Please stop texting me",False,"May not count"),("Take me off your list",False,"May not count"),("STOP",True,"Must be honored")]
by=py0+56; bf=sans("Medium",21)
for txt,ok,lab in rows:
    w=d.textlength(txt,font=bf); bx1=px1-28; bx0=bx1-w-32
    d.rounded_rectangle([bx0,by,bx1,by+48],radius=22,fill=(37,99,235) if ok else (150,150,150))
    d.text((bx0+18,by+9),txt,font=bf,fill=(255,255,255))
    c=GREEN if ok else RED; mk="\u2713" if ok else "\u2715"
    d.text((px0+22,by+10),mk,font=ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",21),fill=c); d.text((px0+50,by+10),lab,font=sans("Bold",21),fill=c)
    by+=82
d.text((px0+22,py1-58),"Also counts: QUIT, END, REVOKE, OPT OUT,",font=sans("Regular",17),fill=GREY)
d.text((px0+22,py1-34),"CANCEL, UNSUBSCRIBE",font=sans("Regular",17),fill=GREY)
# right: redline of the rule
rx0,ry0,rx1,ry1=574,236,1144,598
card(d,rx0,ry0,rx1,ry1)
d.text((rx0+22,ry0+14),"47 CFR 64.1200, THE RULE TEXT",font=mono("SemiBold",16),fill=RED)
d.text((rx0+22,ry0+46),"TODAY",font=mono("SemiBold",15),fill=GREY)
tf=font("Regular",20)
old="Callers \u2026 may not designate an exclusive means to request revocation of consent."
yy=ry0+70
for ln in wrap(d,old,tf,rx1-rx0-44):
    d.text((rx0+22,yy),ln,font=tf,fill=GREY); lw=d.textlength(ln,font=tf)
    d.line([rx0+22,yy+14,rx0+22+lw,yy+14],fill=RED,width=3); yy+=30
d.text((rx0+22,yy+14),"FROM NOV 25",font=mono("SemiBold",15),fill=GREEN)
new="\u201cCallers may designate any of the following methods as the exclusive means to revoke consent.\u201d A caller that does \u201cis not required to process revocation requests made by any other means.\u201d"
yy+=38; bt=font("Bold",20)
for ln in wrap(d,new,bt,rx1-rx0-44):
    lw=d.textlength(ln,font=bt); d.rectangle([rx0+20,yy-1,rx0+24+lw,yy+27],fill=HL)
    d.text((rx0+22,yy),ln,font=bt,fill=INK); yy+=31
d.text((56,622),"Also new: a STOP to one kind of alert (e.g. payment reminders) can leave the company\u2019s other alerts running.",font=sans("Regular",18),fill=GREY)
d.text((56,650-0),"",font=sans("Regular",10),fill=GREY)
im.save("fcc-robotext-opt-out-nov25.png"); print("saved")
