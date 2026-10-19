from PIL import Image, ImageDraw, ImageFont
G="/usr/share/fonts/truetype/sand-box/google/"
def sans(w,s): return ImageFont.truetype(G+"Fira Sans/FiraSans-"+w+".ttf",s)
def mono(w,s): return ImageFont.truetype(G+"IBM Plex Mono/IBMPlexMono-"+w+".ttf",s)
W,H=1080,1350
im=Image.new("RGB",(W,H),"#F4EFE6"); d=ImageDraw.Draw(im)
d.text((70,60),"FINE PRINT WITH A DEADLINE",font=mono("Bold",34),fill="#B3261E")
d.text((70,110),"Changes kicking in over",font=sans("Black",72),fill="#111")
d.text((70,190),"the next 32 days",font=sans("Black",72),fill="#111")
rows=[("OCT","19","Bank of America","Won't investigate most errors on","transfers from linked outside banks"),
("NOV","1","Verizon","Regulatory Charge goes","$0.21 → $0.26 per voice line"),
("NOV","2","Rocket Money","Bill negotiation only on","$15/mo Premium+; auto-renegotiation ends"),
("NOV","4","Oura","Accept new terms in the app","or you can't use it (no opt-out)"),
("NOV","18","Robinhood","Auto-enrolled in class-action claims;","it keeps 20% of your payout")]
y=320; lx=70
d.line((lx+70,y+40,lx+70,y+5*190-80),fill="#C9BFAE",width=6)
for mo,day,svc,l1,l2 in rows:
    # calendar tile
    d.rounded_rectangle((lx,y,lx+140,y+150),radius=16,fill="#FFFFFF",outline="#111",width=4)
    d.rounded_rectangle((lx,y,lx+140,y+44),radius=16,fill="#B3261E")
    d.rectangle((lx,y+28,lx+140,y+44),fill="#B3261E")
    d.text((lx+70,y+22),mo,font=mono("Bold",28),fill="#fff",anchor="mm")
    d.text((lx+70,y+98),day,font=sans("Black",70),fill="#111",anchor="mm")
    tx=lx+180
    d.text((tx,y+4),svc,font=sans("Bold",44),fill="#111")
    d.text((tx,y+62),l1,font=sans("Regular",33),fill="#333")
    d.text((tx,y+104),l2,font=sans("Regular",33),fill="#333")
    y+=190
d.text((70,H-70),"Sources: each company's own terms and pricing pages · quietlychanged.com",font=mono("Regular",22),fill="#6B6255")
im.save("deadline-calendar.png"); print(im.size)
