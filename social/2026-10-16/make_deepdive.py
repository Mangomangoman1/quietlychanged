# Deep-dive images, Oct 16 2026 (Robinhood, DoorDash, Proton). Run from this folder.
from PIL import Image, ImageDraw, ImageFont
F="/usr/share/fonts/truetype/sand-box/google/IBM Plex Serif/IBMPlexSerif-"
M="/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"
def font(w,s): return ImageFont.truetype(F+w+".ttf", s)
RED=(179,38,30); INK=(28,28,28); BG=(249,247,242); GREY=(95,95,95); GREEN=(26,110,60)
PAPER=(255,255,253); HL=(255,226,92); RULE=(220,214,200)
W,H=1200,675
def base(bg=BG):
    im=Image.new("RGB",(W,H),bg); d=ImageDraw.Draw(im)
    d.rectangle([0,0,W,8],fill=RED); d.rectangle([0,H-8,W,H],fill=RED)
    wf=font("Bold",36); d.text((56,30),"Quietly",font=wf,fill=INK)
    d.text((56+d.textlength("Quietly",font=wf),30),"Changed",font=wf,fill=RED)
    ff=font("Regular",22); t="quietlychanged.com"
    d.text((W-56-d.textlength(t,font=ff),42),t,font=ff,fill=GREY)
    return im,d
def wrap(d,text,f,width):
    out,line=[], ""
    for w in text.split():
        t=(line+" "+w).strip()
        if d.textlength(t,font=f)<=width: line=t
        else: out.append(line); line=w
    out.append(line); return out

# 1) Robinhood: big number + payout bar
im,d=base()
d.text((56,100),"ROBINHOOD CUSTOMER AGREEMENT, SECTION 36A",font=font("SemiBold",26),fill=RED)
big=font("Bold",210); d.text((48,128),"20%",font=big,fill=INK)
y=372
for ln in wrap(d,"of any class-action payout Robinhood files for you. Accounts are auto-enrolled starting Nov 18, 2026.",font("SemiBold",29),550):
    d.text((60,y),ln,font=font("SemiBold",29),fill=INK); y+=40
x0,y0,x1=640,150,1144; bw=x1-x0
d.text((x0,y0),"A $100 settlement check:",font=font("Regular",28),fill=GREY)
y=y0+48; d.rounded_rectangle([x0,y,x1,y+90],12,fill=(230,244,234))
cut=x0+int(bw*0.8)
d.rounded_rectangle([cut,y,x1,y+90],12,fill=RED); d.rectangle([cut,y,cut+14,y+90],fill=RED)
d.text((x0+22,y+22),"$80 to you",font=font("Bold",38),fill=GREEN)
d.text((cut+16,y+26),"$20",font=font("Bold",32),fill=(255,255,255))
yy=y+116
for ln in wrap(d,"\u201cYour Account is automatically enrolled ... unless you unenroll\u201d",font("Italic",25),x1-x0):
    d.text((x0,yy),ln,font=font("Italic",25),fill=INK); yy+=34
yy+=14
for ln in wrap(d,"And once a claim is filed for you, you can't separately sue that defendant.",font("Regular",25),x1-x0):
    d.text((x0,yy),ln,font=font("Regular",25),fill=GREY); yy+=34
d.rounded_rectangle([56,560,W-56,628],10,fill=INK)
t="Opt out anytime in the app or via Customer Service. Filing your own claim is usually free."
d.text(((W-d.textlength(t,font=font("SemiBold",25)))/2,578),t,font=font("SemiBold",25),fill=(255,255,255))
im.save("robinhood-class-action-20.png")

# 2) DoorDash: fine-print crop with highlighter on the vendor names
im,d=base((236,232,222))
d.text((56,96),"DOORDASH CONSUMER TERMS  \u00b7  EFFECTIVE OCT 16, 2026",font=font("SemiBold",26),fill=RED)
px0,py0,px1,py1=70,134,W-70,514
d.rectangle([px0+8,py0+8,px1+8,py1+8],fill=(205,198,184)); d.rectangle([px0,py0,px1,py1],fill=PAPER,outline=RULE)
fb=font("Bold",28); fr=font("Regular",28); lx=px0+40; ly=py0+24
d.text((lx,ly),"(x) Related Third Parties.",font=fb,fill=INK); ly+=50
para=("This Arbitration Agreement extends to disputes between you and DoorDash's Related Third Parties ... "
      "\"Related Third Parties\" includes a party's affiliates, subsidiaries, successors, related entities, agents, employees, contractors, subcontractors, insurers, licensees, assignees, vendors, and suppliers.")
for ln in wrap(d,para,fr,px1-px0-80): d.text((lx,ly),ln,font=fr,fill=(70,70,70)); ly+=40
ly+=8
pre="DoorDash's Related Third Parties include but are not limited to "
names=["Amplitude,","Persona,","Checkr,","Blue Star,","Stripe,","Payfare"]
x=lx; d.text((x,ly),pre,font=fr,fill=INK); x+=d.textlength(pre,font=fr)
for n in names:
    w=d.textlength(n,font=fb)
    if x+w>px1-40: x=lx; ly+=44
    d.rectangle([x-4,ly+2,x+w+4,ly+38],fill=HL); d.text((x,ly),n,font=fb,fill=INK); x+=w+d.textlength(" ",font=fb)
t1="Also new: all U.S. cases move to JAMS  \u00b7  \u201cautonomous vehicles\u201d may deliver your order"
d.text(((W-d.textlength(t1,font=font("SemiBold",24)))/2,534),t1,font=font("SemiBold",24),fill=RED)
t="A claim against one of DoorDash's vendors? It goes to arbitration too."
d.text(((W-d.textlength(t,font=font("Bold",30)))/2,578),t,font=font("Bold",30),fill=INK)
im.save("doordash-arbitration-vendors.png")

# 3) Proton: before / after strike-through
im,d=base()
d.text((56,100),"PROTON TERMS OF SERVICE, SECTION 4",font=font("SemiBold",26),fill=RED)
mf=font("Regular",27); lf=font("SemiBold",22)
d.text((70,150),"JUNE 23, 2026 VERSION",font=lf,fill=GREY)
d.rounded_rectangle([70,182,W-70,300],10,fill=(253,235,233))
old="The Company does not make any warranty about the reliability of the Services or the security of user data, despite best efforts. The Service is provided \u201cas is\u201d and \u201cas available\u201d..."
y=196
for ln in wrap(d,old,mf,W-190):
    d.text((94,y),ln,font=mf,fill=(140,60,55)); lw=d.textlength(ln,font=mf); d.line([94,y+19,94+lw,y+19],fill=RED,width=3); y+=34
d.text((70,322),"OCT 9, 2026 VERSION",font=lf,fill=GREY)
d.rounded_rectangle([70,354,W-70,540],10,fill=(230,244,234))
new1="The Company reserves the right, at its sole discretion, to modify, suspend, or discontinue any of our Services, or any feature or component thereof, "
y=372
lines=wrap(d,new1+"with or without notice to you.",font("Regular",29),W-190)
for ln in lines:
    f=font("Regular",29)
    if "without notice" in ln:
        i=ln.find("with or without"); a=ln[:i]; b=ln[i:]
        d.text((94,y),a,font=f,fill=INK); xa=94+d.textlength(a,font=f); fb=font("Bold",29)
        d.rectangle([xa-3,y+3,xa+d.textlength(b,font=fb)+3,y+37],fill=HL); d.text((xa,y),b,font=fb,fill=INK)
    else: d.text((94,y),ln,font=f,fill=INK)
    y+=40
d.text((94,y+6),"...the Company has no obligation to provide such notice.",font=font("Italic",27),fill=GREEN)
t="Covers Proton Mail, Drive, VPN, Pass, Calendar, Meet and Docs."
d.text(((W-d.textlength(t,font=font("SemiBold",28)))/2,580),t,font=font("SemiBold",28),fill=INK)
im.save("proton-discontinue-without-notice.png")
