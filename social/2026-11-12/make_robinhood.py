from PIL import Image, ImageDraw, ImageFont
W,H=1200,675
im=Image.new("RGB",(W,H),"#faf7f0"); d=ImageDraw.Draw(im)
DJ="/usr/share/fonts/truetype/dejavu/"
B=lambda s:ImageFont.truetype(DJ+"DejaVuSans-Bold.ttf",s)
R=lambda s:ImageFont.truetype(DJ+"DejaVuSans.ttf",s)
M=lambda s:ImageFont.truetype(DJ+"DejaVuSansMono.ttf",s)
d.rectangle([0,0,W,8],fill="#c0392b")
d.text((60,36),"ROBINHOOD FEE SCHEDULE · KPI BINARY OPTIONS",font=B(22),fill="#555")
d.text((60,72),"Free through Dec 31. From Jan 1, 2027:",font=B(40),fill="#111")
d.text((60,124),"the cheaper the bet, the bigger the fee bite",font=B(40),fill="#c0392b")
d.text((60,190),"Fees as a share of what you pay: contract fee (10%, or 5% with Gold) + exchange fee (2%), each × p(1−p)",font=R(19),fill="#444")
prices=[0.10,0.30,0.50,0.70,0.90]
base=560; top=250; maxpct=12.0
bw=150; gap=60; x0=110
for i,p in enumerate(prices):
    pct=12*(1-p); g=7*(1-p)
    x=x0+i*(bw+gap)
    h=(base-top)*pct/maxpct; hg=(base-top)*g/maxpct
    d.rectangle([x,base-h,x+bw//2-4,base],fill="#c0392b")
    d.rectangle([x+bw//2+4,base-hg,x+bw,base],fill="#e8a49b")
    d.text((x-2,base-h-32),f"{pct:.1f}%",font=B(24),fill="#c0392b")
    d.text((x+bw//2+6,base-hg-26),f"{g:.1f}%",font=B(18),fill="#a0645c")
    d.text((x+bw//2-30,base+10),f"{int(p*100)}¢",font=B(26),fill="#111")
d.line([90,base,1130,base],fill="#333",width=2)
d.text((60,base+42),"Contract price (pays $1 if the company metric hits the strike)",font=R(20),fill="#444")
d.rectangle([800,250,824,268],fill="#c0392b"); d.text((832,246),"no Gold",font=R(20),fill="#222")
d.rectangle([800,280,824,298],fill="#e8a49b"); d.text((832,276),"with Gold",font=R(20),fill="#222")
d.text((60,636),"Before regulatory fees. Formula from Robinhood's Nov 10 fee schedule.",font=R(18),fill="#666")
d.text((900,626),"quietlychanged.com",font=B(22),fill="#c0392b")
im.save("robinhood-kpi-fees.png")
