# Deep-dive images, Oct 27 2026 (Xero terms: ID + biometric face scan, US arbitration terms, Dec 28). Run from this folder.
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

def hlpara(d,x,y,text,f,width,hl_words=()):
    for l in wrap(d,text,f,width):
        w=d.textlength(l,font=f)
        if any(h in l for h in hl_words): d.rectangle([x-2,y-2,x+2+w,y+32],fill=HL)
        d.text((x,y),l,font=f,fill=INK); y+=38
    return y

# 1) Logo first: Xero logo (Wikipedia file), centered, undistorted
im=Image.new("RGB",(W,H),(255,255,255))
lg=Image.open("logo.png").convert("RGBA"); s=470
lg=lg.resize((s,round(s*lg.height/lg.width)),Image.LANCZOS)
im.paste(lg,((W-lg.width)//2,(H-lg.height)//2),lg)
im.save("01-xero-logo.png")

# 2) The new ID / face-scan clause
im,d=base()
d.text((56,84),"XERO TERMS OF USE  \u00b7  UPDATED OCT 26, 2026  \u00b7  NEW SECTION 12",font=font("SemiBold",23),fill=RED)
d.text((56,122),"Pass an ID and face check, or lose access",font=font("Bold",44),fill=INK)
card(d,56,196,1144,530)
mf=mono("Regular",23); y=222
y=hlpara(d,80,y,"\u201cwe may ask you to provide things like government-issued identification documents and a biometric facial scan so we can confirm the document belongs to you.\u201d",mf,1030,())
y+=14
y=hlpara(d,80,y,"\u201cif we can't verify you, or you choose not to provide the information we ask for within that time, we may decline to activate your subscription or restrict or terminate access to some or all of our services.\u201d",mf,1030,())
d.text((80,y+14),"Plus: automated risk checks \u201con an ongoing basis\u201d can suspend access while Xero looks into it.",font=sans("Regular",21),fill=GREY)
d.text((56,560),"New customers now; current customers from Dec 28, 2026.  Source: xero.com/us/legal/terms",font=sans("Regular",19),fill=GREY)
im.save("02-face-scan-clause.png")

# 3) US arbitration terms, big number
im,d=base()
d.text((56,84),"XERO US ARBITRATION TERMS  \u00b7  FROM DEC 28, 2026",font=font("SemiBold",23),fill=RED)
bf=font("Bold",110); d.text((56,112),"1 YEAR",font=bf,fill=RED)
d.text((56+d.textlength("1 YEAR",font=bf)+30,150),"to bring any claim",font=font("Bold",44),fill=INK)
d.text((56+d.textlength("1 YEAR",font=bf)+30,206),"from when you knew (or should have known)",font=sans("Regular",24),fill=GREY)
items=["Notice of Claim first, then a required video or phone meeting within 60 days",
       "Individual AAA arbitration or small claims only. No class actions",
       "Proceedings, evidence and the final decision stay confidential",
       "25+ similar claims get batched; test cases go first, the rest wait",
       "Claim found frivolous? You reimburse Xero's fees and arbitrator costs"]
yy=290
for it in items:
    d.ellipse([60,yy+10,74,yy+24],fill=RED); d.text((90,yy),it,font=sans("Regular",26),fill=INK); yy+=56
d.text((56,612),"We found no opt-out.  Source: xero.com/us/legal/terms/arbitration-terms",font=sans("Regular",19),fill=GREY)
im.save("03-one-year-arbitration.png")
