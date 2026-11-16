import json, io, cairosvg, urllib.request
from PIL import Image, ImageDraw, ImageFont
UA={'User-Agent':'QuietlyChangedBot/1.0'}
def get(u): return urllib.request.urlopen(urllib.request.Request(u,headers=UA)).read()
def url(f):
    d=json.loads(get('https://commons.wikimedia.org/w/api.php?action=query&titles=File:'+urllib.parse.quote(f)+'&prop=imageinfo&iiprop=url&format=json'))
    return list(d['query']['pages'].values())[0]['imageinfo'][0]['url']
import urllib.parse
B='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'; R='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
def logo_card(svgfile,out,bg,width=820):
    png=cairosvg.svg2png(bytestring=get(url(svgfile)),output_width=width)
    lg=Image.open(io.BytesIO(png)).convert('RGBA')
    if lg.height>500: lg=lg.resize((int(lg.width*500/lg.height),500))
    im=Image.new('RGB',(1200,675),bg); im.paste(lg,((1200-lg.width)//2,(675-lg.height)//2),lg); im.save(out); print(out,lg.size)
logo_card('Bureau of Labor Statistics logo.svg','r1-01-bls-logo.png','white')
# bar card: 2025 vs 2024 change by category, BLS CE release Oct 29, 2026 (Table 1)
rows=[('Rent (rented dwellings)','$5,660 → $6,272',10.8),('Meat, poultry, fish, eggs','$1,414 → $1,579',11.7),
      ('Health insurance','$4,055 → $4,310',6.3),('Pre-tax income','$104,207 → $110,847',6.4),
      ('CPI inflation (CPI-U)','',2.6),('Gasoline and other fuels','$2,645 → $2,503',-5.4)]
im=Image.new('RGB',(1200,675),(250,250,248)); d=ImageDraw.Draw(im)
A=(200,40,40); G=(40,120,70); INK=(20,20,20)
d.rectangle([0,0,1200,14],fill=A)
d.text((60,40),'2025: rent and meat outran inflation',font=ImageFont.truetype(B,44),fill=INK)
d.text((60,100),'Average US household (consumer unit), spending and income, change vs 2024',font=ImageFont.truetype(R,26),fill=(90,90,90))
y=165; x0=640; scale=34
for name,val,pct in rows:
    d.text((60,y),name,font=ImageFont.truetype(B,28),fill=INK)
    if val: d.text((60,y+36),val,font=ImageFont.truetype(R,22),fill=(90,90,90))
    col = (120,120,120) if 'CPI' in name else (G if pct<0 else A)
    w=int(abs(pct)*scale)
    if pct>=0: d.rectangle([x0,y+8,x0+w,y+48],fill=col); tx=x0+w+12
    else: d.rectangle([x0-w,y+8,x0,y+48],fill=col); tx=x0+12
    d.text((tx,y+10),('+' if pct>0 else '')+f'{pct}%',font=ImageFont.truetype(B,30),fill=col)
    y+=72
d.line([x0,160,x0,y],fill=(160,160,160),width=2)
d.text((60,625),'Source: BLS Consumer Expenditures 2025 (USDL-26-1619, Oct 29, 2026), Table 1 · QuietlyChanged',font=ImageFont.truetype(R,21),fill=(110,110,110))
im.save('r1-02-bls-card.png'); print('card')
