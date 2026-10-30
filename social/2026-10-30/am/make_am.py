# Oct 30 AM reply images. Logos: Wikimedia Commons (Steam_icon_logo.svg, DoorDash_Logo.svg, Instacart_logo_and_wordmark.svg), rendered undistorted.
import cairosvg
from PIL import Image, ImageDraw
exec(open("../../2026-10-29/pm/helpers.py").read())
def logo(svg, png, w):
    cairosvg.svg2png(url=svg, write_to=png, output_width=w); return Image.open(png).convert("RGBA")
# R1 Steam
im=Image.new("RGB",(W,H),(255,255,255)); lg=logo("Steam_icon_logo.svg","steam.png",380)
im.paste(lg,((W-lg.width)//2,(H-lg.height)//2),lg); im.save("01-steam-logo.png")
im,d=base()
d.text((56,84),"STEAMWORKS DOCUMENTATION  \u00b7  DISCOUNTING RULES",font=font("SemiBold",22),fill=RED)
d.text((56,120),"After a price increase, Steam blocks sales for 30 days",font=font("Bold",38),fill=INK)
card(d,56,196,1144,560,outline=RED,width=3)
d.text((84,214),"30-Day Price Increase Cooldown",font=sans("Bold",24),fill=RED)
y=hlpara(d,84,260,"\u201cA product cannot be discounted for 30 days following a price increase in any currency. There are no exceptions to this rule\u2026\u201d",mono("Regular",22),1020,("cannot be discounted for 30 days",))
y=hlpara(d,84,y+20,"\u201cAny product on a 30-day Release Cooldown or a 30-day Price Increase cooldown cannot join a Seasonal Sale.\u201d",mono("Regular",22),1020,("cannot join a Seasonal Sale",))
d.text((56,600),"Source: partner.steamgames.com/doc/marketing/discounts (read Oct 30, 2026)",font=sans("Regular",18),fill=GREY)
im.save("02-steam-cooldown-rule.png")
# R2 DoorDash + Instacart
im=Image.new("RGB",(W,H),(255,255,255)); dd=logo("DoorDash_Logo.svg","doordash.png",470); ic=logo("Instacart_logo_and_wordmark.svg","instacart.png",420)
im.paste(dd,(70,(H-dd.height)//2),dd); im.paste(ic,(W-70-ic.width,(H-ic.height)//2),ic)
d=ImageDraw.Draw(im); d.line([600,230,600,445],fill=(210,210,210),width=3); im.save("01-doordash-instacart-logos.png")
im,d=base()
d.text((56,84),"DOORDASH + INSTACART  \u00b7  THE OCT 29 ANNOUNCEMENT",font=font("SemiBold",22),fill=RED)
d.text((56,120),"One membership fee is coming. Not yet.",font=font("Bold",40),fill=INK)
card(d,56,190,700,580,outline=RED,width=3)
d.text((80,206),"WHAT IT SAYS",font=sans("Bold",20),fill=RED)
y=240
for q,k in [("\u201cDashPass and Instacart+ members would pay one membership fee instead of two\u201d","one membership fee"),
            ("Close \u201cexpected\u201d in \u201cthe end of 2027 or the first half of 2028\u201d","end of 2027"),
            ("\u201cUntil the transaction closes, DoorDash and Instacart will continue to operate as separate and independent companies.\u201d","separate")]:
    y=hlpara(d,80,y,q,mono("Regular",18),590,(k,))+14
card(d,724,190,1144,580)
d.text((748,206),"WHAT IT DOESN'T SAY",font=sans("Bold",20),fill=GREY)
y=244
for l in ["The combined plan's name","Its price","Which perks survive","Whether it needs regulators' OK first? Yes: it does"]:
    pass
for l in ["The combined plan's name","Its price","Which perks survive"]:
    d.text((748,y),"\u2022 "+l,font=sans("Regular",24),fill=INK); y+=46
y=hlpara(d,748,y+20,"Also needs Instacart shareholder and antitrust approval (US, Canada, Israel).",sans("Regular",20),370,())
d.text((56,612),"Source: about.doordash.com/en-us/news/doordash-to-acquire-instacart (Oct 29, 2026)",font=sans("Regular",18),fill=GREY)
im.save("02-what-it-says.png")
