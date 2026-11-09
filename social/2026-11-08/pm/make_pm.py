from PIL import Image, ImageDraw
exec(open("../../2026-10-29/pm/helpers.py").read())
# R1: PS5 US list prices, Sony's own announcements
im,d=base()
d.text((56,84),"PS5 US LIST PRICES  \u00b7  PER SONY / PLAYSTATION.BLOG",font=font("SemiBold",22),fill=RED)
d.text((56,118),"Memory got secured. Prices didn\u2019t come down.",font=font("Bold",40),fill=INK)
rows=[("PS5 (disc)",[("Launch 2020","$499.99"),("Aug 2025","$549.99"),("Apr 2, 2026","$649.99")]),
      ("PS5 Pro",[("Launch 2024","$699.99"),("Aug 2025","$749.99"),("Apr 2, 2026","$899.99")])]
y=200
for name,steps in rows:
    d.text((56,y+30),name,font=sans("Bold",34),fill=INK)
    x=320
    for i,(lab,p) in enumerate(steps):
        col=RED if i==2 else INK
        d.text((x,y),lab,font=sans("Regular",22),fill=GREY)
        d.text((x,y+32),p,font=sans("Bold",46),fill=col)
        if i<2: d.text((x+215,y+38),"\u2192",font=sans("Bold",40),fill=GREY)
        x+=280
    y+=170
d.text((56,540),"Sony cited \u201cglobal economic\u201d pressures; Reuters tied the April hike to memory-chip costs.",font=sans("Regular",20),fill=INK)
d.text((56,612),"Sources: blog.playstation.com (Mar 27, 2026; Aug 2025); Reuters, Mar 27, 2026",font=sans("Regular",18),fill=GREY)
im.save("r1-02-ps5-price-ladder.png")
# R2: EIA electricity
im,d=base()
d.text((56,84),"EIA ELECTRIC POWER MONTHLY  \u00b7  AUGUST 2026 vs AUGUST 2025",font=font("SemiBold",22),fill=RED)
d.text((56,118),"What a kilowatt-hour cost, by who\u2019s buying",font=font("Bold",40),fill=INK)
data=[("Homes",18.16,"+3.4%"),("Businesses",14.47,"+4.3%"),("Industry",9.64,"+7.3%")]
y=215
for lab,v,ch in data:
    d.text((56,y+8),lab,font=sans("Bold",32),fill=INK)
    w=int(640*v/18.16); d.rectangle([300,y,300+w,y+60],fill=(150,150,150) if lab!="Homes" else RED)
    d.text((300+w+16,y+6),f"{v:.2f}\u00a2",font=sans("Bold",36),fill=INK)
    d.text((300+w+150,y+12),ch,font=sans("Bold",30),fill=RED)
    y+=105
d.text((56,540),"Homes also used 7.9% more power. Biggest all-sector jumps: Hawaii +25.6%, Georgia +17.3%.",font=sans("Regular",20),fill=INK)
d.text((56,612),"Source: eia.gov Electricity Monthly Update, End Use: August 2026 (released Oct 23, 2026). Average revenue per kWh.",font=sans("Regular",18),fill=GREY)
im.save("r2-02-eia-electricity.png")
