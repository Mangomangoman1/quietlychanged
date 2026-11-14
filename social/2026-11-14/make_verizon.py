from PIL import Image, ImageDraw, ImageFont
W,H=1200,675
im=Image.new("RGB",(W,H),"#faf7f0"); d=ImageDraw.Draw(im)
DJ="/usr/share/fonts/truetype/dejavu/"
B=lambda s:ImageFont.truetype(DJ+"DejaVuSans-Bold.ttf",s)
R=lambda s:ImageFont.truetype(DJ+"DejaVuSans.ttf",s)
SE=lambda s:ImageFont.truetype(DJ+"DejaVuSerif.ttf",s)
d.rectangle([0,0,W,8],fill="#c0392b")
d.text((60,30),"VERIZON DOLLARS TERMS · NEW SECTION 7.4, SPOTTED NOV 14, 2026",font=B(20),fill="#555")
d.text((60,62),"Opt out of Verizon Dollars and you lose:",font=B(42),fill="#111")
def hl(x,y,text,font,maxw=1040,lh=31):
    for w in text.split(" "):
        tw=d.textlength(w+" ",font=font)
        if x+tw>80+maxw: x=80; y+=lh
        ww=d.textlength(w,font=font); d.rectangle([x-2,y-1,x+tw,y+26],fill="#fde68a"); d.text((x,y),w,font=font,fill="#111")
        x+=tw
    return y
items=[("1","All accumulated Verizon Dollars will be immediately forfeited, with the exception of Verizon Dollars earned by Verizon Visa Card holders for eligible Verizon Visa Card spend."),
("2","Verizon purchases (e.g., accessories, devices) made with Verizon Dollars will be ineligible for a refund."),
("3","You will lose access to waived fees for mobile device activations and/or upgrades.")]
y=140
d.rectangle([60,y,1140,y+392],fill="#ffffff",outline="#ddd")
d.text((80,y+12),"7.4 Opt-Out: \"If you choose to opt out of Verizon Dollars, you agree:\"",font=B(18),fill="#777")
yy=y+52
for n,t in items:
    d.ellipse([80,yy,112,yy+32],fill="#c0392b"); d.text((90,yy+3),n,font=B(20),fill="#fff")
    end=hl(128,yy+2,t,SE(22),maxw=1000)
    yy=end+48
d.text((80,y+350),"Verizon's own launch post put activation and upgrade fees at \"up to $40 in fees per device.\"",font=R(18),fill="#444")
d.text((60,560),"Before you leave: spend your balance and make any returns first.",font=B(26),fill="#c0392b")
d.text((60,632),"Highlighted: new text, exact wording from Verizon's terms (Nov 13 vs Nov 14 snapshots).",font=R(17),fill="#666")
d.text((900,626),"quietlychanged.com",font=B(22),fill="#c0392b")
im.save("verizon-dollars-opt-out-forfeit.png")
