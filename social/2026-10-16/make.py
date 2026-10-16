from PIL import Image, ImageDraw, ImageFont
F="/usr/share/fonts/truetype/sand-box/google/IBM Plex Serif/IBMPlexSerif-"
M="/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"
def font(w,s): return ImageFont.truetype(F+w+".ttf", s)
RED=(179,38,30); INK=(28,28,28); BG=(249,247,242); GREY=(95,95,95); GREEN=(26,110,60)
W,H=1200,675
def base():
    im=Image.new("RGB",(W,H),BG); d=ImageDraw.Draw(im)
    d.rectangle([0,0,W,8],fill=RED); d.rectangle([0,H-8,W,H],fill=RED)
    wf=font("Bold",40); d.text((56,34),"Quietly",font=wf,fill=INK)
    d.text((56+d.textlength("Quietly",font=wf),34),"Changed",font=wf,fill=RED)
    ff=font("Regular",24); t="quietlychanged.com"
    d.text((W-56-d.textlength(t,font=ff),46),t,font=ff,fill=GREY)
    return im,d
def ctext(d,y,t,f,fill):
    d.text(((W-d.textlength(t,font=f))/2,y),t,font=f,fill=fill)
# Audible: big-number graphic
im,d=base()
ctext(d,120,"AUDIBLE PREMIUM, ONE YEAR",font("SemiBold",30),RED)
big=font("Bold",230); t="$99"; tw=d.textlength(t,font=big)
d.text(((W-tw)/2-150,160),t,font=big,fill=INK)
old=font("Regular",96); o="$149.50"; ox=(W+tw)/2-150+60; oy=230
d.text((ox,oy),o,font=old,fill=GREY); ow=d.textlength(o,font=old)
d.line([ox-6,oy+62,ox+ow+6,oy+62],fill=RED,width=8)
d.text((ox,oy+120),"regular annual (12 credits)",font=font("Regular",28),fill=GREY)
ctext(d,470,"New \"limited time offer\" on Audible's plans page",font("Bold",40),INK)
ctext(d,530,"That's about $8.25 a month. Terms apply; no end date listed.",font("Regular",30),GREY)
im.save("audible-99-premium.png")
# Cloudflare: before/after line diff
im,d=base()
ctext(d,112,"CLOUDFLARE PLANS PAGE, PIPELINES PRICING",font("SemiBold",28),RED)
x0,x1=70,W-70
mf=ImageFont.truetype(M,30); lf=font("SemiBold",24)
d.text((x0,170),"OCT 15",font=lf,fill=GREY)
d.rounded_rectangle([x0,204,x1,284],10,fill=(253,235,233))
d.text((x0+24,226),"- Ingestion       TBD (free during beta)",font=mf,fill=RED)
d.text((x0,310),"OCT 16",font=lf,fill=GREY)
d.rounded_rectangle([x0,344,x1,560],10,fill=(230,244,234))
rows=["+ SQL transforms           $0.04 / GB",
      "+ Delivery, JSON           $0.03 / GB",
      "+ Delivery, Parquet/Iceberg $0.06 / GB",
      "+ Querying (Basin SQL)     $2.50 / TB"]
for i,r in enumerate(rows): d.text((x0+24,364+i*48),r,font=mf,fill=GREEN)
ctext(d,590,"The beta's over. Each paid line includes a monthly free tier first.",font("Regular",28),GREY)
im.save("cloudflare-basin-pricing.png")
