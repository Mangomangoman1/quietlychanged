# Deep-dive images, Oct 22 2026 (Fitbit Web API turn-off Oct 30: reconnect apps in Google Health). Run from this folder.
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


# Fitbit Web API turn-off: timeline + Google quote + affected / not affected
im,d=base()
d.text((56,84),"FITBIT WEB API  \u00b7  TURNED OFF OCT 30, 2026",font=font("SemiBold",23),fill=RED)
hf=font("Bold",40); y=116
for ln in wrap(d,"Apps linked to your Fitbit stop syncing Oct 30 unless you reconnect them.",hf,1090):
    d.text((56,y),ln,font=hf,fill=INK); y+=50
# timeline
ty=262; x0,x1=90,1110
d.line([x0,ty,x1,ty],fill=RULE,width=6)
pts=[(x0,"SEP 30","End of support",GREY,False),(600,"OCT 30","API turned off",RED,True),(x1,"NOV 30","Late-reconnect option until*",GREY,False)]
for x,dt,lab,c,big in pts:
    r=16 if big else 10
    d.ellipse([x-r,ty-r,x+r,ty+r],fill=c)
    f=mono("SemiBold",26 if big else 20); w=d.textlength(dt,font=f)
    ax=min(max(x-w/2,56),W-56-w); d.text((ax,ty+22),dt,font=f,fill=c)
    f2=sans("Medium" if not big else "Bold",19 if not big else 21); w2=d.textlength(lab,font=f2)
    bx=min(max(x-w2/2,56),W-56-w2); d.text((bx,ty+56),lab,font=f2,fill=INK if big else GREY)
# quote card
qx0,qy0,qx1,qy1=56,372,700,612
card(d,qx0,qy0,qx1,qy1)
d.text((qx0+22,qy0+14),"GOOGLE HEALTH HELP",font=mono("SemiBold",18),fill=RED)
segs=[("\u201cGoogle Health Support",True),("can\u2019t restore or fix your broken connection",True),("once Fitbit connections retired on October 30, 2026. Reconnection must be enabled by the partner app\u2019s developer.\u201d",False)]
body=font("Regular",21); bold=font("Bold",21)
words=[(w,h) for t,h in segs for w in t.split()]
lx=qx0+22; ly=qy0+50; lh=33
for w,h in words:
    f=bold if h else body; ww=d.textlength(w,font=f); sp=d.textlength(" ",font=body)
    if lx+ww>qx1-22: lx=qx0+22; ly+=lh
    if h: d.rectangle([lx-2,ly-1,lx+ww+sp,ly+29],fill=HL)
    d.text((lx,ly),w,font=f,fill=INK); lx+=ww+sp
d.text((qx0+22,qy1-30),"support.google.com/googlehealth/answer/14236613",font=mono("Regular",14),fill=GREY)
# affected / not affected
rx=736
d.text((rx,374),"NEEDS RECONNECTING",font=mono("SemiBold",18),fill=RED)
for i,t in enumerate(["Calorie & diet apps","Employer wellness points","Training apps","Research studies"]):
    yy=404+i*34; d.rectangle([rx,yy+8,rx+12,yy+20],fill=RED); d.text((rx+24,yy),t,font=sans("Medium",21),fill=INK)
d.text((rx,548),"NOT AFFECTED",font=mono("SemiBold",18),fill=GREEN)
d.text((rx,576),"Health Connect \u00b7 Apple Health",font=sans("Medium",21),fill=INK)
d.text((56,630),"*Per Fitabase, the reconnect option stays in Google Health through Nov 30. Already-synced history isn\u2019t deleted.",font=sans("Regular",16),fill=GREY)
im.save("fitbit-api-off-oct30.png"); print("saved")
