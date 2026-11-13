import cairosvg, io
from PIL import Image, ImageDraw, ImageFont
W,H=1200,675
B="/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"; R="/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
fb=lambda s:ImageFont.truetype(B,s); fr=lambda s:ImageFont.truetype(R,s)
def ctext(d,y,t,f,fill):
    d.text(((W-d.textlength(t,font=f))/2,y),t,font=f,fill=fill)
# Costco logo
png=cairosvg.svg2png(url="costco.svg", output_width=900)
logo=Image.open(io.BytesIO(png)).convert("RGBA")
im=Image.new("RGB",(W,H),"white"); im.paste(logo,((W-logo.width)//2,(H-logo.height)//2-50),logo)
d=ImageDraw.Draw(im); ctext(d,H-140,CAPTION,fb(42),"#222")
im.save("r1-01-costco-logo.png")
# Costco math card
im=Image.new("RGB",(W,H),"#0f172a"); d=ImageDraw.Draw(im)
d.text((60,40),"Does Costco Executive pay for itself?",font=fb(46),fill="white")
d.text((60,105),"Fee $120 → $130 on Sept 1, 2024 ($65 base + $65 upgrade)",font=fr(30),fill="#cbd5e1")
rows=[("You spend","2% Reward","vs $65 upgrade"),("$271/mo  ($3,252/yr)","$65","break-even"),("$542/mo  ($6,504/yr)","$130","+$65"),("$1,250/mo  ($15,000/yr)","$300","+$235"),("$62,500/yr","$1,250","cap")]
y=170
for i,(a,b,c) in enumerate(rows):
    f=fr(28) if i==0 else fb(38); col="#94a3b8" if i==0 else "white"
    d.text((70,y),a,font=f,fill=col); d.text((640,y),b,font=f,fill="#94a3b8" if i==0 else "#facc15"); d.text((860,y),c,font=f,fill=col)
    y+=50 if i==0 else 64
d.line((60,y+8,W-60,y+8),fill="#334155",width=3)
for line in ["Under break-even? Downgrade at the membership counter: Costco refunds","the $65 upgrade minus any 2% Reward already earned or issued."]:
    d.text((60,y+26),line,font=fr(28),fill="#e2e8f0"); y+=40
d.text((60,H-42),"Source: costco.com Executive Rewards page; Costco customer service fee-increase notice  |  QuietlyChanged",font=fr(19),fill="#64748b")
im.save("r1-02-costco-math-card.png")
# Costco policy quote card (for quote post)
im=Image.new("RGB",(W,H),"white"); d=ImageDraw.Draw(im)
d.rectangle((0,0,W,14),fill="#005DAA"); d.rectangle((0,H-14,W,H),fill="#E31837")
d.text((70,60),"Costco's own written policy, not a register trick:",font=fb(40),fill="#111")
d.text((70,140),"Risk-Free 100% Satisfaction Guarantee",font=fb(34),fill="#005DAA")
q=["“On Membership: We will cancel and refund","your membership fee at any time if you are","dissatisfied.”"]
y=210
for l in q: d.text((70,y),l,font=fb(44),fill="#111"); y+=64
d.text((70,y+30),"Any time in the year. No insider needed. Ask at the membership counter.",font=fr(30),fill="#333")
d.text((70,H-60),"Source: customerservice.costco.com, “What is Costco’s return policy?”  |  QuietlyChanged",font=fr(22),fill="#666")
im.save("q1-02-costco-policy-card.png")
# Xbox Ultimate price path chart
im=Image.new("RGB",(W,H),"#0b0f0b"); d=ImageDraw.Draw(im)
d.text((60,35),"Game Pass Ultimate already tried price hikes",font=fb(44),fill="white")
data=[("Jun 2019",14.99),("Jul 2023",16.99),("Sep 2024",19.99),("Oct 2025",29.99),("Apr 2026",22.99)]
base=590; top=150; mx=32; bw=150; gap=(W-120-5*bw)/4
for i,(lab,v) in enumerate(data):
    x=60+i*(bw+gap); h=(base-top)*v/mx
    col="#e11d48" if v==29.99 else ("#22c55e" if i==4 else "#107C10")
    d.rectangle((x,base-h,x+bw,base),fill=col)
    t=f"${v:.2f}"; d.text((x+(bw-d.textlength(t,font=fb(34)))/2,base-h-44),t,font=fb(34),fill="white")
    d.text((x+(bw-d.textlength(lab,font=fb(26)))/2,base+12),lab,font=fb(26),fill="#d1d5db")
d.text((60,H-40),"US monthly price, Game Pass Ultimate. Source: Xbox Wire / Microsoft Store, via QuietlyChanged price history",font=fr(19),fill="#9ca3af")
im.save("r3-02-gamepass-price-chart.png")
