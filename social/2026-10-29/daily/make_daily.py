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


# 1) Logo first: official GitHub mark (github.githubassets.com GitHub-Mark PNG), centered, undistorted
im=Image.new("RGB",(W,H),(255,255,255))
lg=Image.open("github-mark.png").convert("RGBA"); s=420
lg=lg.resize((s,s),Image.LANCZOS)
im.paste(lg,((W-s)//2,(H-s)//2),lg)
im.save("01-github-logo.png")

def hl(d,x,y,text,f,width,keys,lh=34):
    for l in wrap(d,text,f,width):
        if any(k in l for k in keys):
            d.rectangle([x-2,y-2,x+2+d.textlength(l,font=f),y+lh-6],fill=HL)
        d.text((x,y),l,font=f,fill=INK); y+=lh
    return y

# 2) Before/after of the pricing page's Enterprise box
im,d=base()
d.text((56,84),"GITHUB PRICING PAGE  \u00b7  ENTERPRISE PLAN  \u00b7  OCT 28 vs OCT 29, 2026",font=font("SemiBold",23),fill=RED)
d.text((56,122),"Copilot is now part of GitHub Enterprise",font=font("Bold",44),fill=INK)
card(d,56,196,1144,300)
d.text((76,206),"BEFORE",font=sans("Bold",17),fill=GREY)
hl(d,76,234,"\u201cSecurity, compliance, and flexible deployment\u201d  \u00b7  \u201cEverything included in Team, plus...\u201d",mono("Regular",22),1050,())
card(d,56,322,1144,560,outline=RED,width=3)
d.text((76,332),"NOW",font=sans("Bold",17),fill=RED)
y=362
y=hl(d,76,y,"\u201cAI-powered development, governed at enterprise scale\u201d",mono("Regular",24),1050,("AI-powered",),38)
y=hl(d,76,y+6,"\u201cGitHub Enterprise now includes access to GitHub Copilot.\u201d",mono("Regular",24),1050,("includes access",),38)
y=hl(d,76,y+6,"\u201cEverything from Team, plus: GitHub Copilot access, Agent governance ...\u201d",mono("Regular",24),1050,("Copilot access","Agent governance"),38)
d.text((56,596),"Source: github.com/pricing, snapshots Oct 28 and Oct 29, 2026",font=sans("Regular",19),fill=GREY)
im.save("02-enterprise-before-after.png")

# 3) The catch: no AI credits, metered from the first request
im,d=base()
d.text((56,84),"GITHUB CHANGELOG  \u00b7  OCT 28, 2026",font=font("SemiBold",23),fill=RED)
d.text((56,122),"Included seat, but AI usage bills from request #1",font=font("Bold",42),fill=INK)
card(d,56,196,1144,540)
y=220
y=hl(d,80,y,"\u201cdoes not include monthly AI credits per seat\u201d",mono("Regular",24),1030,("does not include",),38)
y=hl(d,80,y+10,"\u201cAI usage is metered from the first request against your enterprise budget ... There is no included usage allowance\u201d",mono("Regular",24),1030,("first request","no included usage allowance"),38)
y=hl(d,80,y+10,"\u201cCopilot Chat, Copilot code review, and Copilot in the cloud require available budget to use.\u201d",mono("Regular",24),1030,("require available budget",),38)
d.text((56,566),"Code completion keeps working with no budget left. Self-serve customers can't switch yet.",font=sans("Regular",21),fill=GREY)
d.text((56,604),"Source: github.blog/changelog/2026-10-28-github-enterprise-now-includes-access-to-github-copilot",font=sans("Regular",18),fill=GREY)
im.save("03-no-credits-metered.png")
