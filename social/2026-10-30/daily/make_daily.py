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



def hl(d,x,y,text,f,width,keys,lh=34):
    for l in wrap(d,text,f,width):
        if any(k in l for k in keys):
            d.rectangle([x-2,y-2,x+2+d.textlength(l,font=f),y+lh-6],fill=HL)
        d.text((x,y),l,font=f,fill=INK); y+=lh
    return y

# 1) Logo first
im=Image.new("RGB",(W,H),(255,255,255))
lg=Image.open("canva-logo.png").convert("RGBA")
im.paste(lg,((W-lg.width)//2,(H-lg.height)//2),lg)
im.save("01-canva-logo.png")

# 2) The fine print of Canva's new e-signature terms
im,d=base()
d.text((56,84),"CANVA ELECTRONIC SIGNATURE FEATURE TERMS  \u00b7  OCT 30, 2026",font=font("SemiBold",23),fill=RED)
d.text((56,122),"Canva now does e-signatures. The fine print:",font=font("Bold",42),fill=INK)
card(d,56,196,1144,590)
y=216; mf=mono("Regular",23)
for txt,keys in [
 ("\u201cCanva does not verify the identity, age, capacity, or authority of any sender or signer.\u201d",("does not verify",)),
 ("\u201cnot an archive or evidence preservation service\u201d",("not an archive",)),
 ("\u201cYou must not use Electronic Signature Feature for\u201d wills, trusts, powers of attorney and deeds.",("must not use",)),
 ("\u201cNames, emails, and signing records will be visible to anyone who has access to the document or signing link.\u201d",("visible to anyone",)),
]:
    y=hl(d,80,y,txt,mf,1030,keys,36)+16
d.text((56,610),"Source: canva.com/policies/signature-terms, last updated Oct 30, 2026",font=sans("Regular",19),fill=GREY)
im.save("02-esign-fine-print.png")

# 3) Terms of Use before/after
im,d=base()
d.text((56,84),"CANVA TERMS OF USE  \u00b7  OCT 29 vs OCT 30, 2026",font=font("SemiBold",23),fill=RED)
d.text((56,122),"New terms took effect today",font=font("Bold",44),fill=INK)
card(d,56,196,1144,330)
d.text((76,206),"BEFORE",font=sans("Bold",17),fill=GREY)
hl(d,76,236,"\u201cThese Terms of Use are effective as of 19 August 2026.\u201d  \u00b7  \u201c6. Use of AI Products\u201d",mono("Regular",22),1050,(),34)
card(d,56,352,1144,580,outline=RED,width=3)
d.text((76,362),"NOW",font=sans("Bold",17),fill=RED)
y=hl(d,76,392,"\u201cThese Terms of Use are effective as of 30 October 2026.\u201d",mono("Regular",23),1050,("30 October",),38)
y=hl(d,76,y+6,"\u201c6. Use of Products  Your use of certain Canva products and features may be subject to additional obligations and restrictions in the Feature Specific Terms\u201d",mono("Regular",23),1050,("Feature Specific",),38)
d.text((56,604),"Source: canva.com/policies/terms-of-use, snapshots Oct 29 and Oct 30, 2026",font=sans("Regular",19),fill=GREY)
im.save("03-terms-before-after.png")
