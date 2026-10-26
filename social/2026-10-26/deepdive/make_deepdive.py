# Deep-dive images, Oct 26 2026 (California sales tax on software/SaaS from Jan 1, 2027, SB 122). Run from this folder.
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




# 1) Logo first: Seal of California (Wikimedia Commons), centered, undistorted
im=Image.new("RGB",(W,H),(255,255,255))
seal=Image.open("seal.png").convert("RGBA"); s=560
seal=seal.resize((s,round(s*seal.height/seal.width)),Image.LANCZOS)
im.paste(seal,((W-seal.width)//2,(H-seal.height)//2),seal)
im.save("01-california-seal.png")

# 2) Before / after
im,d=base()
d.text((56,84),"CALIFORNIA SALES TAX  \u00b7  SB 122  \u00b7  STARTS JAN 1, 2027",font=font("SemiBold",23),fill=RED)
hf=font("Bold",44); y=122
for l in wrap(d,"Downloaded and cloud software stops being tax-free",hf,1090):
    d.text((56,y),l,font=hf,fill=INK); y+=54
y+=14
card(d,56,y,1144,y+170)
d.text((80,y+16),"NOW  \u00b7  CDTFA Regulation 1502",font=sans("SemiBold",20),fill=GREY)
mf=mono("Regular",23); yy=y+50
for l in wrap(d,"\u201cThe sale or lease of a prewritten program is not a taxable transaction if the program is transferred by remote telecommunications\u2026\u201d",mf,1030):
    d.text((80,yy),l,font=mf,fill=INK); w=d.textlength(l,font=mf)
    d.line([80,yy+15,80+w,yy+15],fill=RED,width=3); yy+=34
y2=y+196
card(d,56,y2,1144,y2+190,outline=GREEN,width=3)
d.text((80,y2+16),"FROM JAN 1, 2027  \u00b7  Rev. & Tax. Code \u00a76016, as amended",font=sans("SemiBold",20),fill=GREEN)
yy=y2+50
for l in wrap(d,"\u201cTangible personal property\u201d now includes \u201cA digital product and any copyright or patent interests associated therewith.\u201d",mf,1030):
    w=d.textlength(l,font=mf); d.rectangle([78,yy-2,82+w,yy+30],fill=HL); d.text((80,yy),l,font=mf,fill=INK); yy+=36
d.text((80,yy+6),"Digital product = prewritten software on media, downloaded, or accessed remotely (incl. SaaS)",font=sans("Regular",20),fill=GREY)
im.save("02-before-after.png")

# 3) Taxed vs not
im,d=base()
d.text((56,84),"FROM JAN 1, 2027, IN CALIFORNIA",font=font("SemiBold",23),fill=RED)
d.text((56,118),"7.25%+",font=font("Bold",86),fill=RED)
d.text((56+d.textlength("7.25%+",font=font("Bold",86))+24,146),"sales tax on software subscriptions",font=font("Bold",36),fill=INK)
d.text((56,226),"Statewide rate 7.25%; most areas add district taxes of 0.10% to 2.00%",font=sans("Regular",21),fill=GREY)
L=[(56,"TAXED",GREEN,["Prewritten (off-the-shelf) software","Downloaded software","Cloud software / SaaS","Software on a disk (already taxed)","Subscription periods from Jan 1, 2027*"]),
   (612,"NOT TAXED",RED,["Movies and video","Music, ringtones, audiobooks","E-books","Entertainment video games","Digital art, crypto, IaaS/PaaS"])]
for x,t,c,items in L:
    card(d,x,266,x+532,590,outline=c,width=3)
    d.text((x+24,282),t,font=sans("Bold",28),fill=c); yy=332
    for it in items:
        d.ellipse([x+26,yy+11,x+38,yy+23],fill=c); d.text((x+50,yy),it,font=sans("Regular",24),fill=INK); yy+=48
d.text((56,610),"*CDTFA draft emergency regulation, not final.  Sources: CDTFA digital products guide; SB 122 (Stats. 2026, ch. 23)",font=sans("Regular",18),fill=GREY)
im.save("03-taxed-vs-not.png")
