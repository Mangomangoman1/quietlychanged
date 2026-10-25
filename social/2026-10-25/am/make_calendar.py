from PIL import Image, ImageDraw, ImageFont
W,H=1080,1350
img=Image.new('RGB',(W,H),'#FFF8E7'); d=ImageDraw.Draw(img)
B='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'; R='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
f=lambda p,s: ImageFont.truetype(p,s)
d.rectangle([0,0,W,190],fill='#111111')
d.text((50,32),"FINE-PRINT DEADLINES",font=f(B,62),fill='#FFD400')
d.text((50,112),"Oct 30 to Nov 25, 2026. Mark your calendar.",font=f(R,34),fill='white')
rows=[("OCT 30","Fitbit","Linked apps stop getting your data unless you reconnect"),
("NOV 1","Verizon","Regulatory Charge $0.21 → $0.26 per line"),
("NOV 1","Roblox","Under 18s need a parent to accept new terms"),
("NOV 4","Oura","App locks unless you accept arbitration terms"),
("NOV 9","ipl.org","Site goes offline for good, nothing migrated"),
("NOV 12","Pinterest","Mass claims to one arbitrator, 30-day opt-out"),
("NOV 15","Verizon","Admin charge $3.78 → $4.69 per line"),
("NOV 17","Google Play","Broken purchase? Go to the developer, not Google"),
("NOV 18","Robinhood","Auto-files class claims for you, keeps 20%"),
("NOV 25","FCC rule","Companies pick the only way you can opt out of texts")]
y=215; rh=106
for i,(dt,svc,txt) in enumerate(rows):
    if i%2==0: d.rectangle([0,y-8,W,y+rh-14],fill='#FFEFC2')
    d.rounded_rectangle([40,y,210,y+76],radius=12,fill='#D7261E')
    tw=d.textlength(dt,font=f(B,32)); d.text((125-tw/2,y+20),dt,font=f(B,32),fill='white')
    d.text((235,y-2),svc,font=f(B,36),fill='#111111')
    d.text((235,y+44),txt,font=f(R,27),fill='#333333')
    y+=rh
d.text((50,H-95),"Sources: each company's own terms, pricing and Federal Register pages",font=f(R,24),fill='#555555')
d.text((W-300,H-62),"",font=f(R,24))
d.text((50,H-58),"quietlychanged.com",font=f(B,30),fill='#D7261E')
img.save('nov-fine-print-deadlines.png'); print('ok')
