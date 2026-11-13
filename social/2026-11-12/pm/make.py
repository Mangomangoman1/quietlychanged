import cairosvg, io
from PIL import Image, ImageDraw, ImageFont
W,H=1200,675
png=cairosvg.svg2png(url="ms.svg", output_width=860)
logo=Image.open(io.BytesIO(png)).convert("RGBA")
im=Image.new("RGB",(W,H),"white")
im.paste(logo,((W-logo.width)//2,(H-logo.height)//2-30),logo)
d=ImageDraw.Draw(im)
B="/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"; R="/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
f=ImageFont.truetype(B,40)
t="Microsoft 365 outage: the SLA fine print"
d.text(((W-d.textlength(t,font=f))/2,H-150),t,font=f,fill="#222")
im.save("r1-01-microsoft-logo.png")
# card
im=Image.new("RGB",(W,H),"#0f172a"); d=ImageDraw.Draw(im)
fb=lambda s:ImageFont.truetype(B,s); fr=lambda s:ImageFont.truetype(R,s)
d.text((60,45),"Exchange Online SLA (business plans)",font=fb(44),fill="white")
d.text((60,110),"Financially backed monthly uptime: 99.9%",font=fr(32),fill="#cbd5e1")
rows=[("Monthly uptime","Service credit"),("below 99.9%","25%"),("below 99%","50%"),("below 95%","100%")]
y=180
for i,(a,b) in enumerate(rows):
    col="#94a3b8" if i==0 else "white"; s=30 if i==0 else 46
    d.text((90,y),a,font=fb(s) if i else fr(s),fill=col); d.text((760,y),b,font=fb(s) if i else fr(s),fill="#facc15" if i else col)
    y+=60 if i==0 else 78
d.line((60,y+5,W-60,y+5),fill="#334155",width=3)
for line in ["Not automatic: your admin files a claim with the Service Health","incident ID. For a November outage, claim by Dec 31.","Uptime counts user-minutes, so a big multi-hour outage can cross it."]:
    d.text((60,y+25),line,font=fr(28),fill="#e2e8f0"); y+=42
d.text((60,H-45),"Source: Microsoft Service Level Agreement for Microsoft Online Services  |  QuietlyChanged",font=fr(20),fill="#64748b")
im.save("r1-02-sla-card.png")
