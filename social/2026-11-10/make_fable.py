from PIL import Image, ImageDraw, ImageFont
W,H=1200,675
im=Image.new('RGB',(W,H),'#0f1115');d=ImageDraw.Draw(im)
B='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf';R='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
f=lambda p,s:ImageFont.truetype(p,s)
d.text((60,40),"Anthropic API pricing, per million tokens",font=f(R,28),fill='#9aa3b2')
d.text((60,80),"Fable 5.2: output and caching 20% cheaper",font=f(B,42),fill="#ffffff")
rows=[("Output",50,40,"$50","$40"),("Cache write",12.5,10,"$12.50","$10"),("Cache read",0.25,0.20,"$0.25","$0.20")]
y=190;maxw=760;x0=330
for name,a,b,sa,sb in rows:
  d.text((60,y+20),name,font=f(B,34),fill='#e6e8ec')
  wa=maxw; wb=int(maxw*b/a)
  d.rectangle([x0,y,x0+wa,y+40],fill='#3a3f4b'); d.text((x0+14,y+5),"5.1  "+sa,font=f(B,26),fill='#c9ced8')
  d.rectangle([x0,y+50,x0+wb,y+90],fill='#ffb020'); d.text((x0+14,y+55),"5.2  "+sb,font=f(B,26),fill='#111318')
  y+=140
d.text((60,H-60),"Source: anthropic.com/pricing, snapshot Nov 10, 2026",font=f(R,24),fill='#9aa3b2')
d.text((W-330,H-60),"quietlychanged.com",font=f(B,26),fill='#ffffff')
im.save('fable-5-2-pricing.png')
