from PIL import Image,ImageDraw,ImageFont
B='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'; R='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
rows=[('Gasoline',34.2),('Airline fares',22.4),('Hotels, lodging',4.4),('All prices (CPI)',3.7)]
W,H=1200,675; im=Image.new('RGB',(W,H),(246,245,241)); d=ImageDraw.Draw(im)
d.text((60,40),'Getting there costs more this year',font=ImageFont.truetype(B,46),fill=(20,20,20))
d.text((60,104),'US prices, September 2026 vs September 2025',font=ImageFont.truetype(R,28),fill=(90,90,90))
x0,x1=440,990; y=185; mx=34.2
for name,p in rows:
    d.text((60,y+6),name,font=ImageFont.truetype(B,34),fill=(20,20,20))
    d.rectangle([x0,y,x1,y+56],fill=(232,230,224))
    col=(190,40,35) if p>10 else (120,120,120)
    d.rectangle([x0,y,x0+int((x1-x0)*p/mx),y+56],fill=col)
    d.text((x1+20,y+8),f'+{p}%',font=ImageFont.truetype(B,36),fill=col)
    y+=100
d.text((60,598),'Source: BLS CPI-U, not seasonally adjusted. Oct 2025 prices were not collected,',font=ImageFont.truetype(R,20),fill=(110,110,110))
d.text((60,624),'so September is the latest year-over-year comparison.  QuietlyChanged',font=ImageFont.truetype(R,20),fill=(110,110,110))
im.save('r1-02-travel-cpi-chart.png')
