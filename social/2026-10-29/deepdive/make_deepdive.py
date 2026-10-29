# Deep-dive images, Oct 29 2026 (SSA Client Data System, SORN 60-0392, FR Doc 2026-22173). Run from this folder.
# Seal: Wikimedia Commons "US-SocialSecurityAdmin-Seal.svg" (public domain), rendered with cairosvg to logo.png.
from PIL import Image, ImageDraw, ImageFont
G="/usr/share/fonts/truetype/sand-box/google/"
def font(w,s): return ImageFont.truetype(G+"IBM Plex Serif/IBMPlexSerif-"+w+".ttf", s)
def mono(w,s): return ImageFont.truetype(G+"IBM Plex Mono/IBMPlexMono-"+w+".ttf", s)
def sans(w,s):
    f=ImageFont.truetype(G+"IBM Plex Sans/IBMPlexSans-VariableFont_wdth,wght.ttf", s)
    try: f.set_variation_by_name(w)
    except Exception: pass
    return f
RED=(179,38,30); INK=(26,26,26); BG=(251,250,247); GREY=(95,95,95)
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
def hl(d,x,y,text,f,width,keys,lh=31):
    for l in wrap(d,text,f,width):
        if any(k in l for k in keys): d.rectangle([x-2,y-2,x+2+d.textlength(l,font=f),y+lh-5],fill=HL)
        d.text((x,y),l,font=f,fill=INK); y+=lh
    return y

# 1) Logo first: SSA seal, centered, undistorted, plain white background
im=Image.new("RGB",(W,H),(255,255,255))
lg=Image.open("logo.png").convert("RGBA"); s=520
lg=lg.resize((round(s*lg.width/lg.height),s),Image.LANCZOS)
im.paste(lg,((W-lg.width)//2,(H-lg.height)//2),lg)
im.save("01-ssa-seal.png")

# 2) What goes in the one file
im,d=base()
d.text((56,84),"SSA CLIENT DATA SYSTEM (60-0392)  \u00b7  NEW SYSTEM OF RECORDS  \u00b7  OCT 30, 2026",font=font("SemiBold",22),fill=RED)
d.text((56,120),"One profile per Social Security number",font=font("Bold",44),fill=INK)
d.text((56,180),"Pulled from 12 existing SSA record systems, plus contractors and other agencies",font=sans("Regular",24),fill=GREY)
items=["Name, SSN, sex, birth date, parents, place of birth","Country of citizenship","Earnings by year","Benefit and SSI payment amounts","Marriages: spouse SSN, \u201creason for marriage end\u201d","Call and office notes \u201centered by technicians\u201d","\u201cHigh-risk\u201d and special warning flags","Payee, representative and fee agreements","Accommodation needs","Wounded Warrior and VA 100% disability flags"]
card(d,56,228,1144,600)
f=sans("Medium",25); y0=250
for i,t in enumerate(items):
    x=84 if i<5 else 616; y=y0+(i%5)*68
    d.rectangle([x,y+10,x+12,y+22],fill=RED)
    for j,l in enumerate(wrap(d,t,f,480)): d.text((x+26,y+j*30),l,font=f,fill=INK)
d.text((56,622),"Covers \u201cindividuals who have been issued a Social Security number.\u201d Source: Federal Register, FR Doc. 2026-22173",font=sans("Regular",19),fill=GREY)
im.save("02-whats-in-the-file.png")

# 3) Quotes: who's covered + new email outreach use, deadline
im,d=base()
d.text((56,84),"SSA CLIENT DATA SYSTEM  \u00b7  THE NOTICE\u2019S OWN WORDS",font=font("SemiBold",22),fill=RED)
d.text((56,120),"Everyone with an SSN, and your email for surveys",font=font("Bold",42),fill=INK)
card(d,56,190,1144,300)
d.text((76,200),"WHO\u2019S COVERED",font=sans("Bold",17),fill=GREY)
hl(d,76,226,"\u201cThis system maintains information on individuals who have been issued a Social Security number (SSN)\u2026\u201d",mono("Regular",22),1040,("issued a Social Security number",))
card(d,56,322,1144,462,outline=RED,width=3)
d.text((76,332),"NEW USE OF YOUR CONTACT INFO",font=sans("Bold",17),fill=RED)
hl(d,76,358,"\u201cWe may also use contact information (e.g., email addresses) provided by individuals who conduct business with SSA for program outreach (e.g., notification about our programs, online services, SSA events, and surveys)\u201d",mono("Regular",22),1040,("email addresses","surveys"))
d.text((56,500),"30 sharing rules (mostly carried over from other SSA systems) take effect Nov 29, 2026.",font=sans("Medium",23),fill=INK)
d.text((56,540),"Comment by Nov 29 at regulations.gov, docket SSA-2025-0030.",font=sans("Medium",23),fill=INK)
d.text((56,612),"Source: Federal Register public inspection, FR Doc. 2026-22173 (publishes Oct 30, 2026)",font=sans("Regular",19),fill=GREY)
im.save("03-notice-quotes.png")
