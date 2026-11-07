# Nov 7 AM X session images. Starlink logo: Wikimedia Commons Starlink_Logo.svg (from Oct 30 assets), rendered undistorted.
import cairosvg
from PIL import Image, ImageDraw
exec(open("../../2026-10-29/pm/helpers.py").read())
# O1 image 1: Starlink logo
cairosvg.svg2png(url="Starlink_Logo.svg",write_to="starlink.png",output_width=640)
lg=Image.open("starlink.png").convert("RGBA")
im=Image.new("RGB",(W,H),(255,255,255)); im.paste(lg,((W-lg.width)//2,(H-lg.height)//2),lg); im.save("o1-01-starlink-logo.png")
# O1 image 2: same plan, five prices
im,d=base()
d.text((56,84),"STARLINK RESIDENTIAL MAX  \u00b7  US, FROM BILLS ON/AFTER NOV 30",font=font("SemiBold",22),fill=RED)
d.text((56,120),"Same plan. Price now depends on your address.",font=font("Bold",40),fill=INK)
rows=[("20% above list","$156",156,RED),("10% above list","$143",143,RED),("List price","$130",130,INK),("10% below list","$117",117,GREEN),("20% below list","$104",104,GREEN)]
y=205; maxw=760
for lab,p,v,c in rows:
    d.text((56,y+8),lab,font=sans("SemiBold",26),fill=GREY)
    w=int(maxw*v/156); d.rectangle([300,y,300+w,y+52],fill=c)
    d.text((300+w+16,y+4),p,font=font("Bold",38),fill=c); y+=72
d.text((56,572),"$104 vs $156 for the same plan = $624 a year apart. Starlink says it will review prices \u201croughly quarterly.\u201d",font=sans("Regular",20),fill=INK)
d.text((56,612),"Sources: Starlink customer emails (Nov 2026); starlink.com local prices as reported by PCMag, Notebookcheck",font=sans("Regular",18),fill=GREY)
im.save("o1-02-price-ladder.png")
# O1 image 3: the email fine print
im,d=base()
d.text((56,84),"FROM STARLINK'S \u201cSERVICE PRICE ADJUSTMENTS\u201d EMAIL",font=font("SemiBold",22),fill=RED)
d.text((56,120),"Why it's up, and why downgrading won't dodge it",font=font("Bold",40),fill=INK)
card(d,56,196,1144,520,outline=RED,width=3)
y=222
for q,k in [("\u201cAs more people in your area use Starlink, less network capacity is available and service pricing may change from time to time.\u201d","less network capacity"),
            ("\u201cPlease note that the pricing for all Residential service plans in your area are increasing. If you switch plans before 30 days, the price you see in your account will be increased by 10% in 30 days.\u201d","increased by 10% in 30 days"),
            ("\u201cYou can change or cancel your service without penalty at any time from your account.\u201d","without penalty")]:
    y=hlpara(d,84,y,q,mono("Regular",21),1030,(k,))+18
d.text((56,612),"Text as shared by a customer on X, Nov 7, 2026 (version announcing a 10% increase)",font=sans("Regular",18),fill=GREY)
im.save("o1-03-email-fine-print.png")
# R1 road trip card
im,d=base()
d.text((56,84),"THE \u201cOPTIMAL\u201d US ROAD TRIP  \u00b7  13,949 MILES, 49 STOPS",font=font("SemiBold",22),fill=RED)
d.text((56,120),"Same loop, same car. Only the gas changed.",font=font("Bold",40),fill=INK)
for i,(yr,price,gal,v,c) in enumerate([("2015","$1,300","$2.37/gal",1300,GREY),("Oct 2026","$2,350","$4.29/gal",2350,RED)]):
    y=220+i*130; d.text((56,y+18),yr,font=sans("SemiBold",30),fill=INK)
    w=int(640*v/2350); d.rectangle([240,y,240+w,y+80],fill=c)
    d.text((240+w+18,y+2),price,font=font("Bold",44),fill=c); d.text((240+w+18,y+52),gal,font=sans("Regular",22),fill=GREY)
y=hlpara(d,56,490,"Priced state by state: ~$2,395. California's ~860 miles alone: ~$208 at $6.17/gal.",sans("Regular",24),1090,("~$2,395",))
d.text((56,612),"Source: Yahoo Finance (AAA Oct 19 avg; EPA 25.5 mpg, 2024 new gas car); route: optimalroadtrips.com",font=sans("Regular",18),fill=GREY)
im.save("r1-01-roadtrip-card.png")
# R2 ACR card
im,d=base()
d.text((56,84),"NORTHEASTERN \u201cWATCHING THE WATCHERS\u201d  \u00b7  12 SMART TVS TESTED",font=font("SemiBold",22),fill=RED)
d.text((56,120),"Did the \u201cstop tracking\u201d switch actually work?",font=font("Bold",40),fill=INK)
card(d,56,196,580,480,outline=GREEN,width=3); card(d,620,196,1144,480,outline=RED,width=3)
d.text((80,212),"OPT-OUT HELD",font=sans("Bold",24),fill=GREEN)
y=256
for l in ["LG webOS","Sony (Google TV)","Fire TV","VIDAA (Hisense etc.)"]: d.ellipse([80,y+12,96,y+28],fill=GREEN); d.text((108,y),l,font=sans("Regular",28),fill=INK); y+=52
d.text((644,212),"TRAFFIC KEPT FLOWING",font=sans("Bold",24),fill=RED)
y=256
for l in ["Samsung: 30/30 runs on its own channels","Vizio: no decrease at all","Roku: still on The Roku Channel"]:
    d.ellipse([644,y+10,660,y+26],fill=RED); y=hlpara(d,672,y,l,sans("Regular",24),440,())+10
d.text((56,500),"Where to switch it off:",font=sans("SemiBold",22),fill=GREY)
d.text((56,534),"Samsung: Viewing Information Services \u00b7 Vizio: Viewing Data \u00b7 LG: Live Plus",font=sans("Regular",24),fill=INK)
d.text((56,612),"Researchers note traffic was encrypted, so it's \u201cconsistent with ACR,\u201d not confirmed. Via The Verge, TechRadar.",font=sans("Regular",18),fill=GREY)
im.save("r2-01-acr-optout-card.png")
