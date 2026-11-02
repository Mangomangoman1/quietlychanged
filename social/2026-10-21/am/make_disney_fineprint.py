# Highlighted real screenshot: Disney+ US Subscriber Agreement section 2(k), captured live Oct 21, 2026 via headless Chrome (shot3.mjs)
import json
from PIL import Image, ImageDraw, ImageFont
W,H=1080,1350
F='/usr/share/fonts/truetype/sand-box/google/Inter/Inter-VariableFont_opsz,wght.ttf'
def font(sz,w=700):
    f=ImageFont.truetype(F,sz)
    try: f.set_variation_by_axes([min(sz,32),w])
    except Exception: pass
    return f
rects=json.load(open('rects_m.json')); clip=json.load(open('clips_m.json'))['clip']
S=4
para=Image.open('para_m.png').convert('RGB')
d=ImageDraw.Draw(para)
# boxes
last_y=0
for b in rects['boxes']:
    for r in b['rects']:
        if r['w']<6: continue
        x0=(r['x']-clip['x'])*S-8; y0=(r['y']-clip['y'])*S-4
        x1=x0+r['w']*S+16; y1=y0+r['h']*S+12
        d.rounded_rectangle([x0,y0,x1,y1],radius=10,outline=(255,59,48),width=9)
        last_y=max(last_y,y1)
para=para.crop((0,0,para.width,int(last_y+12)))
img=Image.new('RGB',(W,H),(255,255,255))
dr=ImageDraw.Draw(img)
# headline band
dr.rectangle([0,0,W,290],fill=(255,59,48))
dr.text((56,48),'Paying for "no ads"?',font=font(78,800),fill='white')
dr.text((56,150),'Disney+ fine print, US terms, live today:',font=font(40,600),fill='white')
dr.text((56,205),'"generally" ad-free.',font=font(52,800),fill='white')
# head crop
head=Image.open('head_m.png').convert('RGB')
c2=json.load(open('clips_m.json'))['clip2']; u=rects['updated']
head=head.crop((0,0,head.width,int((u['y']+u['h']-c2['y'])*S+40)))
pw=W-80
head=head.resize((pw,int(head.height*pw/head.width)),Image.LANCZOS)
para=para.resize((pw,int(para.height*pw/para.width)),Image.LANCZOS)
avail=(H-150)-330
tot=head.height+40+para.height
if tot>avail:
    k=avail/tot
    head=head.resize((int(head.width*k),int(head.height*k)),Image.LANCZOS)
    para=para.resize((int(para.width*k),int(para.height*k)),Image.LANCZOS)
pw2=head.width; x0=(W-pw2)//2
y=330
dr.rectangle([x0,y,x0+pw2,y+head.height+40+para.height],fill=(4,8,20))
img.paste(head,(x0,y)); y+=head.height
dr.text((x0+30,y-6),'[ ... ]',font=font(30,500),fill=(150,150,160)); y+=40
img.paste(para,(x0,y)); y+=para.height
print('content bottom',y)
# footer
dr.text((56,H-120),'disneyplus.com/legal/subscriber-agreement, section 2(k)',font=font(30,500),fill=(60,60,60))
dr.text((56,H-72),'Screenshot Oct 21, 2026  ·  QuietlyChanged',font=font(30,700),fill=(20,20,20))
img.save('disney-no-ads-fine-print-us.png')
