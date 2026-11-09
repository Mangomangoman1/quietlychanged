from PIL import Image, ImageDraw
exec(open("../../2026-10-29/pm/helpers.py").read())
# R1: PS5 Pro checkout card
im,d=base()
d.text((56,84),"PS5 PRO  \u00b7  PER SONY / PLAYSTATION.BLOG / PS DIRECT",font=font("SemiBold",22),fill=RED)
d.text((56,118),"What the $899 Pro does and doesn\u2019t include",font=font("Bold",40),fill=INK)
x=56;y=200
for i,(lab,p) in enumerate([("Launch, Nov 2024","$699.99"),("Aug 2025","$749.99"),("Apr 2, 2026","$899.99")]):
    col=RED if i==2 else INK
    d.text((x,y),lab,font=sans("Regular",22),fill=GREY)
    d.text((x,y+32),p,font=sans("Bold",50),fill=col)
    if i<2: d.text((x+235,y+38),"\u2192",font=sans("Bold",40),fill=GREY)
    x+=320
rows=[("No disc drive in the box.","Sony\u2019s add-on Disc Drive is $79 on PS Direct."),
      ("Discs end for new games.","From Jan 2028, new PlayStation games are digital only;"),
      ("","discs for games released before then still play.")]
y=350
for a,b in rows:
    if a: d.text((56,y),a,font=sans("Bold",30),fill=INK); y+=42
    d.text((56,y),b,font=sans("Regular",26),fill=INK); y+=48
d.text((56,612),"Sources: blog.playstation.com (Mar 27, 2026; Jul 1, 2026); direct.playstation.com disc drive page",font=sans("Regular",18),fill=GREY)
im.save("r1-02-ps5-pro-checkout.png")
# R2: SKIMS returns fine print
im,d=base()
d.text((56,84),"SKIMS US RETURNS PAGE  \u00b7  SKIMS.COM/PAGES/RETURNS",font=font("SemiBold",22),fill=RED)
d.text((56,118),"Refund or store credit? Read this line first",font=font("Bold",40),fill=INK)
d.rectangle((56,205,1144,365),fill=(255,243,176))
q=["\u201cDisclaimer: When a Klarna customer selects Store Credit",
   "as a refund method, the Klarna payment plan will remain",
   "active and must still be paid off.\u201d"]
y=222
for l in q: d.text((80,y),l,font=sans("SemiBold",30),fill=INK); y+=44
d.text((56,400),"Same page: refunds go \u201cto the original method of payment only.\u201d",font=sans("Regular",26),fill=INK)
d.text((56,446),"Store credit only spends at SKIMS.",font=sans("Regular",26),fill=INK)
d.text((56,612),"Source: skims.com/pages/returns, checked Nov 9, 2026",font=sans("Regular",18),fill=GREY)
im.save("r2-02-skims-klarna-fine-print.png")
