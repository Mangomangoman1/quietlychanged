from PIL import Image, ImageDraw, ImageFont
G="/usr/share/fonts/truetype/sand-box/google/"
def serif(w,s): return ImageFont.truetype(G+"IBM Plex Serif/IBMPlexSerif-"+w+".ttf",s)
def mono(w,s): return ImageFont.truetype(G+"IBM Plex Mono/IBMPlexMono-"+w+".ttf",s)
W,H=1200,675; BG=(250,247,240); INK=(28,28,28); MUT=(110,104,96); RED=(179,38,30); CARD=(255,255,255); BOR=(220,213,200)
im=Image.new("RGB",(W,H),BG); d=ImageDraw.Draw(im)
d.rectangle([0,0,W,8],fill=RED)
d.text((56,34),"shopify.com/pricing  ·  pay yearly  ·  Oct 19, 2026",font=mono("Medium",22),fill=MUT)
d.text((56,70),"Same page, same plans, two prices.",font=serif("Bold",50),fill=INK)
def card(x,label,share,grow,adv,hl):
    y=160; w=520; h=330
    d.rounded_rectangle([x,y,x+w,y+h],14,fill=CARD,outline=RED if hl else BOR,width=4 if hl else 2)
    d.text((x+28,y+22),label,font=serif("SemiBold",30),fill=RED if hl else INK)
    d.text((x+28,y+62),share,font=mono("Regular",20),fill=MUT)
    for i,(n,p) in enumerate([("Grow",grow),("Advanced",adv)]):
        yy=y+112+i*104
        d.text((x+28,yy+18),n,font=serif("Regular",34),fill=INK)
        f=serif("Bold",64); t=f"${p}"; tw=d.textlength(t,font=f)
        d.text((x+w-60-tw-d.textlength("/mo",font=serif("Regular",28)),yy),t,font=f,fill=RED if hl else INK)
        d.text((x+w-28-d.textlength("/mo",font=serif("Regular",28)),yy+32),"/mo",font=serif("Regular",28),fill=MUT)
card(56,"Version A","6 of 10 page loads","79","299",False)
card(624,"Version B","4 of 10 page loads","89","359",True)
d.text((56,512),"Monthly billing was $105 and $399 in both versions.",font=serif("Regular",28),fill=INK)
d.text((56,552),"Over a year, the gap is $120 on Grow and $720 on Advanced.",font=serif("Regular",28),fill=INK)
d.line([56,612,W-56,612],fill=BOR,width=2)
d.text((56,624),"Quietly",font=serif("Bold",32),fill=INK)
d.text((56+d.textlength("Quietly",font=serif("Bold",32)),624),"Changed",font=serif("Bold",32),fill=RED)
t="quietlychanged.com"; d.text((W-56-d.textlength(t,font=mono("Medium",22)),632),t,font=mono("Medium",22),fill=MUT)
im.save("shopify-two-yearly-prices.png")
