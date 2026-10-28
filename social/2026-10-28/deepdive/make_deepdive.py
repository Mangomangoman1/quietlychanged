# Deep-dive images, Oct 28 2026 (Grindr Oct 27 terms: AI summaries from chats, AI settings vs paid features). Run from this folder.
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


# 1) Logo first: Grindr logo (Wikimedia Commons "Grindr Logo Black.svg"), centered, undistorted
im=Image.new("RGB",(W,H),(255,255,255))
lg=Image.open("logo.png").convert("RGBA"); s=700
lg=lg.resize((s,round(s*lg.height/lg.width)),Image.LANCZOS)
im.paste(lg,((W-lg.width)//2,(H-lg.height)//2),lg)
im.save("01-grindr-logo.png")

# 2) Before / after: AI section
im,d=base()
d.text((56,84),"GRINDR TERMS OF SERVICE  \u00b7  EFFECTIVE OCT 27, 2026  \u00b7  \u00a77.5(b)",font=font("SemiBold",23),fill=RED)
d.text((56,122),"AI summaries about you, built from your chats",font=font("Bold",42),fill=INK)
mf=mono("Regular",19)
card(d,56,190,1144,290)
d.text((76,200),"BEFORE (Oct 6 version)",font=sans("Bold",17),fill=GREY)
hlpara(d,76,226,"\u201cassess and summarize past interactions to support reconnection and identify compatibility, and surface ... insights to You or other users\u201d",mf,1050,())
card(d,56,312,1144,560,outline=RED,width=3)
d.text((76,322),"NOW",font=sans("Bold",17),fill=RED)
y=348
def hl(x,y,text,f,width,keys):
    for l in wrap(d,text,f,width):
        if any(k in l for k in keys):
            d.rectangle([x-2,y-2,x+2+d.textlength(l,font=f),y+26],fill=HL)
        d.text((x,y),l,font=f,fill=INK); y+=31
    return y
y=hl(76,y,"\u201cWhether or not you use AI Technology features yourself, our systems may generate inferences, summaries, and other System-Generated Content about you (where permitted) from (i) your profile; (ii) your activity on the Services; and, (iii) , your interactions with other users including chats. We may share such content with users who use those features.\u201d",mono("Regular",21),1050,("Whether or not","including chats","We may share"))
d.text((56,590),"Source: trust.grindr.com/en-US/legal/2026-terms-of-service  \u00b7  previous version via Wayback Machine",font=sans("Regular",19),fill=GREY)
im.save("02-ai-chats-before-after.png")

# 3) New section 9.13: turn AI off, paid features stop, bill stays
im,d=base()
d.text((56,84),"GRINDR TERMS OF SERVICE  \u00b7  NEW SECTION 9.13",font=font("SemiBold",23),fill=RED)
d.text((56,122),"Turn AI off, lose paid features, same bill",font=font("Bold",44),fill=INK)
card(d,56,196,1144,520)
y=222
y=hl(80,y,"\u201cIf you turn off a setting that a Paid Feature depends on, that feature will stop working for you until you turn the setting back on. Your Subscription and its billing are not affected by your settings choices.\u201d",mono("Regular",23),1030,("billing are not affected",))
y+=16
y=hl(80,y,"\u201cTurning off a setting is your choice and is not a change we make to the Services under Section 11; no refund is due except where the law requires it.\u201d",mono("Regular",23),1030,("no refund is due",))
d.text((56,556),"Also new (\u00a79.1): \u201cthe Paid Features and prices you see may differ from those shown to other users.\u201d",font=sans("Regular",21),fill=GREY)
d.text((56,600),"Source: trust.grindr.com/en-US/legal/2026-terms-of-service",font=sans("Regular",19),fill=GREY)
im.save("03-ai-off-no-refund.png")
