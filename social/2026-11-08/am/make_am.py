# Nov 8 AM X session images. Logos: OpenAI (Wikimedia Commons OpenAI_Logo.svg), PlayStation (Wikimedia SVG, from Nov 6/7 assets),
# JetBlue (from Nov 7 deep-dive asset), all rendered undistorted on 1200x675.
import cairosvg
from PIL import Image, ImageDraw
exec(open("../../2026-10-29/pm/helpers.py").read())
def logo(svg,out,width,bg=(255,255,255)):
    cairosvg.svg2png(url=svg,write_to="/tmp/_l.png",output_width=width)
    lg=Image.open("/tmp/_l.png").convert("RGBA")
    im=Image.new("RGB",(W,H),bg); im.paste(lg,((W-lg.width)//2,(H-lg.height)//2),lg); im.save(out)
logo("openai-logo.svg","01-openai-logo.png",620)
logo("playstation-logo.svg","01-playstation-logo.png",420)
jb=Image.open("../../2026-11-07/deepdive/01-jetblue-logo.png").convert("RGB")
jb=jb.resize((int(jb.width*1.1),int(jb.height*1.1)),Image.LANCZOS)
im=Image.new("RGB",(W,H),(255,255,255)); im.paste(jb,((W-jb.width)//2,(H-jb.height)//2)); im.save("01-jetblue-logo.png")

# Q1: OpenAI Pro multiples, post vs OpenAI's own pages
im,d=base()
d.text((56,84),"CHATGPT PRO 100 / 200 / 500  \u00b7  CHECKED NOV 8, 2026",font=font("SemiBold",22),fill=RED)
d.text((56,120),"\u201c10X / 20X / 50X\u201d: where it\u2019s written, and where it isn\u2019t",font=font("Bold",36),fill=INK)
card(d,56,190,580,540,outline=RED,width=3); card(d,620,190,1144,540,outline=GREEN,width=3)
d.text((80,206),"AN EMPLOYEE\u2019S X POST (NOV 8)",font=sans("Bold",22),fill=RED)
y=250
for l in ["\u201cPro 100 = 10X, Pro 200 = 20X, Pro 500 = 50X\u201d usage vs Plus","\u201call Pro plans have no 5-hour limits\u201d","Not on chatgpt.com/pricing (no multiples listed there today)"]:
    y=hlpara(d,80,y,l,sans("Regular",23),470,("Not on",))+12
d.text((644,206),"OPENAI HELP CENTER (UPDATED THIS WEEK)",font=sans("Bold",20),fill=GREEN)
y=250
for l in ["Pro plans \u201ccurrently have no five-hour usage limit in Work and Codex.\u201d","\u201cYour plan still has an included usage allowance.\u201d","Check yours: Settings \u2192 Usage (allowance + reset times)"]:
    y=hlpara(d,644,y,l,sans("Regular",23),470,("included usage allowance",))+12
hlpara(d,56,560,"Nov 6: a federal judge let \u201c20x more usage than Pro\u201d ad claims against Anthropic proceed (Kahn v. Anthropic).",sans("Regular",19),1090,())
d.text((56,612),"Sources: help.openai.com \u201cManaging usage with GPT-6 Astra\u2026\u201d; chatgpt.com/pricing; N.D. Cal. 26-cv-05763 Dkt. 50",font=sans("Regular",18),fill=GREY)
im.save("q1-02-openai-multiples-card.png")

# R1: PS Plus perks fine print
im,d=base()
d.text((56,84),"PLAYSTATION PLUS PERKS  \u00b7  ANNOUNCED NOV 6, 2026",font=font("SemiBold",22),fill=RED)
d.text((56,120),"The \u201cfree\u201d YouTube Premium trial, per Sony\u2019s own page",font=font("Bold",38),fill=INK)
card(d,56,190,1144,560,outline=RED,width=3)
y=214
for q,k in [("Perks need a PlayStation account \u201cbased in the United Kingdom, France or Germany.\u201d","United Kingdom, France or Germany"),
            ("YouTube trial: only for people who never subscribed to or trialled Premium, Music Premium or Premium Lite.","never subscribed"),
            ("\u201cAt the end of the trial period, you will be automatically charged \u2026 \u00a312.99/16,99 \u20ac/12,99 \u20ac on a monthly recurring basis.\u201d","automatically charged"),
            ("Cancel any time before the trial ends at no charge. Redeem by Nov 1, 2027.","Cancel any time")]:
    y=hlpara(d,84,y,q,mono("Regular",20),1030,(k,))+14
d.text((56,578),"Fine-print figures are from the UK page (France page matches). Not available to US accounts.",font=sans("Regular",19),fill=INK)
d.text((56,612),"Source: playstation.com/en-gb/ps-plus/perks (footnote 1), checked Nov 8, 2026",font=sans("Regular",18),fill=GREY)
im.save("r1-02-psplus-perks-card.png")

# R2: DDR5 chip spot price, DRAMeXchange then vs now
im,d=base()
d.text((56,84),"DRAMEXCHANGE (TRENDFORCE) SPOT PRICE  \u00b7  DDR5 16Gb CHIP, SESSION AVERAGE",font=font("SemiBold",20),fill=RED)
d.text((56,118),"The RAM chip in your next PC, then vs now",font=font("Bold",40),fill=INK)
pts=[("May 30, 2025",5.561),("Oct 13, 2025",8.867),("Nov 6, 2026",60.167)]
x0,base_y,top=180,560,215; bw=200; gap=150; mx=60.167
for i,(lab,v) in enumerate(pts):
    x=x0+i*(bw+gap); h=(base_y-top)*v/mx
    col=RED if i==2 else (150,150,150)
    d.rectangle([x,base_y-h,x+bw,base_y],fill=col)
    t=f"${v:.2f}"; f=sans("Bold",34); d.text((x+(bw-d.textlength(t,font=f))/2,base_y-h-46),t,font=f,fill=INK)
    f2=sans("Regular",22); d.text((x+(bw-d.textlength(lab,font=f2))/2,base_y+10),lab,font=f2,fill=INK)
d.line([150,base_y,1080,base_y],fill=INK,width=2)
hlpara(d,760,300,"~6.8x since Oct 2025",sans("Bold",30),360,("6.8x",))
d.text((56,612),"Sources: dramexchange.com (live Nov 6, 2026 update; Wayback captures May 30 and Oct 13, 2025). Chip spot, not retail kit prices.",font=sans("Regular",17),fill=GREY)
im.save("r2-02-ddr5-spot-card.png")

# O1: JetBlue fee ladder
im,d=base()
d.text((56,84),"JETBLUE CHECKED BAGS  \u00b7  U.S./LATIN AMERICA/CARIBBEAN/CANADA  \u00b7  BOOKINGS FROM NOV 3",font=font("SemiBold",19),fill=RED)
d.text((56,118),"Same bag, new price",font=font("Bold",40),fill=INK)
card(d,56,190,1144,540,outline=RED,width=3)
cols=[("",90),("Before (Oct 12)",470),("Now",760)]
hdr=sans("Bold",22)
for t,x in cols[1:]: d.text((x,210),t,font=hdr,fill=GREY if "Before" in t else RED)
rows=[("1st bag, off-peak, prepaid","$45","$50"),("1st bag, peak, prepaid","$49","$55"),("1st bag, peak, within 24h","$59","$70"),
      ("2nd bag, off-peak, prepaid","$59","$70"),("2nd bag, peak, prepaid","$69","$75"),("2nd bag, peak, within 24h","$79","$85")]
y=256; f=sans("Regular",24); fb=sans("Bold",26)
for a,b,c in rows:
    d.text((90,y),a,font=f,fill=INK); d.text((470,y),b,font=f,fill=GREY); d.text((760,y),c,font=fb,fill=RED)
    d.line([90,y+40,1110,y+40],fill=RULE,width=1); y+=46
d.text((56,560),"\u201cPrepaid\u201d = added more than 24h before departure. Booked before Nov 3? JetBlue says check Manage Trips.",font=sans("Regular",19),fill=INK)
d.text((56,612),"Source: jetblue.com/legal/fees (live, checked Nov 8, 2026) vs Wayback capture Oct 12, 2026",font=sans("Regular",18),fill=GREY)
im.save("o1-02-fee-ladder.png")

# O1: peak calendar
im,d=base()
d.text((56,84),"JETBLUE PEAK BAG-FEE DATES  \u00b7  FEES PAGE, OCT 12 vs NOV 8, 2026",font=font("SemiBold",21),fill=RED)
d.text((56,118),"December is now peak. All of it.",font=font("Bold",40),fill=INK)
# December strip
x0,y0,cw,ch=72,215,34,70
d.text((x0,y0-4),"DECEMBER 2026",font=sans("Bold",20),fill=INK)
for i in range(31):
    x=x0+i*cw; yy=y0+30
    old= i>=16
    d.rectangle([x,yy,x+cw-4,yy+ch/2-3],fill=(150,150,150) if old else (232,230,224))
    d.rectangle([x,yy+ch/2,x+cw-4,yy+ch-3],fill=RED)
    if i in (0,16,30):
        t=str(i+1); f=sans("Regular",16); d.text((x+(cw-4-d.textlength(t,font=f))/2,yy+ch+4),t,font=f,fill=INK)
d.text((x0+31*cw+10,y0+32),"before",font=sans("Regular",18),fill=GREY)
d.text((x0+31*cw+10,y0+66),"now",font=sans("Bold",18),fill=RED)
y=360
for l,k in [("Dec 1\u201316 used to be off-peak. Now peak.","Now peak"),("Nov 5\u201311 added as peak (Thanksgiving Nov 19\u201330 already was).","added"),
            ("Early-December round trip, 1 prepaid bag each way: $90 before \u2192 $110 now.","$110 now"),
            ("Bag fees are refundable only if the entire booking is cancelled before departure.","entire booking")]:
    y=hlpara(d,72,y,l,sans("Regular",24),1060,(k,))+8
d.text((56,612),"Source: jetblue.com/legal/fees peak-date table (live Nov 8, 2026) vs Wayback Oct 12, 2026",font=sans("Regular",18),fill=GREY)
im.save("o1-03-peak-december.png")
