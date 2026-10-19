# Distribution image, Oct 19 2026: carrier comparison for the USPS unpaid-duties rule. Run from this folder.
from PIL import Image, ImageDraw, ImageFont
G="/usr/share/fonts/truetype/sand-box/google/"
def font(w,s): return ImageFont.truetype(G+"IBM Plex Serif/IBMPlexSerif-"+w+".ttf", s)
def mono(w,s): return ImageFont.truetype(G+"IBM Plex Mono/IBMPlexMono-"+w+".ttf", s)
RED=(179,38,30); INK=(26,26,26); BG=(251,250,247); GREY=(95,95,95)
PAPER=(255,255,253); HL=(255,226,92); RULE=(220,214,200); LIGHT=(214,209,198)
W,H=1200,675
im=Image.new("RGB",(W,H),BG); d=ImageDraw.Draw(im)
d.rectangle([0,0,W,8],fill=RED); d.rectangle([0,H-8,W,H],fill=RED)
wf=font("Bold",30); d.text((56,28),"Quietly",font=wf,fill=INK)
d.text((56+d.textlength("Quietly",font=wf),28),"Changed",font=wf,fill=RED)
ff=font("Regular",21); t="quietlychanged.com"; d.text((W-56-d.textlength(t,font=ff),36),t,font=ff,fill=GREY)
d.text((56,84),"RECIPIENT DIDN'T PAY THE DUTIES. WHO GETS THE BILL?",font=font("SemiBold",23),fill=RED)
d.text((56,118),"FedEx, UPS and DHL bill the sender. USPS now goes further.",font=font("Bold",38),fill=INK)
rows=[("FedEx","\u201cthe original shipper will be billed for duties and taxes\u201d","duties-and-taxes page"),
      ("UPS","\u201cUPS may recover the outstanding amounts from you\u201d","Understanding Customs page"),
      ("DHL","shipper \u201cshall pay or reimburse DHL ... if Consignee has failed to pay\u201d","Terms of Carriage")]
y=196; lab=mono("SemiBold",26); q=font("Italic",23); s=font("Regular",16)
for name,quote,src in rows:
    d.rectangle([56,y,1144,y+70],fill=PAPER,outline=RULE)
    d.text((80,y+19),name,font=lab,fill=INK)
    d.text((220,y+12),quote,font=q,fill=INK)
    d.text((220,y+44),src,font=s,fill=GREY)
    y+=82
# USPS row (highlighted)
d.rectangle([63,y+7,1151,y+7+148],fill=LIGHT)
d.rectangle([56,y,1144,y+148],fill=PAPER,outline=RED,width=3)
d.text((80,y+16),"USPS",font=lab,fill=RED)
d.text((220,y+12),"New IMM 424, effective Oct 19, 2026: invoice to the mailer, and",font=font("Regular",23),fill=INK)
chips=["pay \u201ceven if the mailer disputes\u201d","owed if lost or returned","6% interest + collection costs"]
cx=220; cy=y+54; fb=font("Bold",19)
for c in chips:
    tw=d.textlength(c,font=fb)
    if cx+tw+24>1130: cx=220; cy+=42
    d.rectangle([cx,cy,cx+tw+14,cy+30],fill=HL); d.text((cx+7,cy+3),c,font=fb,fill=INK); cx+=tw+24
d.text((220,y+104),"Disputes with USPS: accounting errors only. Comments due Nov 18, 2026.",font=font("Regular",17),fill=GREY)
d.rounded_rectangle([56,600,1144,648],8,fill=INK)
ft="Where it's offered, prepay duties with USPS Delivered Duty Paid (counter or Click-N-Ship)."
f2=font("SemiBold",22); d.text(((W-d.textlength(ft,font=f2))/2,611),ft,font=f2,fill=(255,255,255))
im.save("usps-duties-carrier-comparison.png")
