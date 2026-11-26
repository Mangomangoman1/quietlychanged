
import subprocess, json, io, cairosvg
from PIL import Image, ImageDraw, ImageFont
UA={'User-Agent':'QuietlyChangedBot/1.0'}
import urllib.request
def get(u):
    return urllib.request.urlopen(urllib.request.Request(u,headers=UA)).read()
def url(f):
    d=json.loads(get('https://commons.wikimedia.org/w/api.php?action=query&titles=File:'+f+'&prop=imageinfo&iiprop=url&format=json'))
    return list(d['query']['pages'].values())[0]['imageinfo'][0]['url']
B='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'; R='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
def logo_card(svgfile, out, bg, width=760):
    png=cairosvg.svg2png(bytestring=get(url(svgfile)), output_width=width)
    lg=Image.open(io.BytesIO(png)).convert('RGBA')
    im=Image.new('RGB',(1200,675),bg); im.paste(lg,((1200-lg.width)//2,(675-lg.height)//2),lg); im.save(out); print(out, lg.size)
logo_card('VIZIO_logo.svg','r1-01-vizio-logo.png','white')
logo_card('Verizon_2024.svg','o1-01-verizon-logo.png','white')
def card(out, title, lines, foot, accent=(220,30,40)):
    im=Image.new('RGB',(1200,675),(250,250,248)); d=ImageDraw.Draw(im)
    d.rectangle([0,0,1200,14],fill=accent)
    d.text((60,50),title,font=ImageFont.truetype(B,50),fill=(20,20,20))
    y=150
    for big,small in lines:
        d.text((60,y),big,font=ImageFont.truetype(B,38),fill=accent); y+=52
        if small: d.text((60,y),small,font=ImageFont.truetype(R,30),fill=(40,40,40)); y+=50
        y+=22
    d.text((60,620),foot,font=ImageFont.truetype(R,22),fill=(110,110,110)); im.save(out); print(out)
card('r1-02-vizio-card.png','Before you set up a new VIZIO TV',
 [('Walmart account required','for apps and smart features (HDMI + antenna work without)'),
  ('Turn off Viewing Data (ACR)','All Settings > Privacy & Legal > Viewing Data > Off'),
  ('Older models','All Settings > Admin & Privacy > Viewing Data')],
 'Sources: vizio.com account FAQ and Walmart account data page · QuietlyChanged')
card('r2-02-gta-math-card.png','GTA VI pre-orders, per Sensor Tower',
 [('$1.18B ÷ 12.1M = ~$97.50','average revenue per pre-order'),
  ('Standard $79.99  ·  Ultimate $99.99','US PlayStation Store prices'),
  ('Average sits near Ultimate','(estimate; regional prices vary)')],
 'Sources: Sensor Tower via charlieINTEL; store.playstation.com GTA VI listings. QuietlyChanged', accent=(200,120,0))

