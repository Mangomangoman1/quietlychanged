from PIL import Image, ImageDraw, ImageFont
F="/usr/share/fonts/truetype/sand-box/google/IBM Plex Serif/IBMPlexSerif-"
def font(w,s): return ImageFont.truetype(F+w+".ttf", s)
RED=(179,38,30); INK=(28,28,28); BG=(249,247,242); GREY=(95,95,95); HL=(255,226,92)
W,H=1200,675
im=Image.new("RGB",(W,H),BG); d=ImageDraw.Draw(im)
d.rectangle([0,0,W,8],fill=RED); d.rectangle([0,H-8,W,H],fill=RED)
wf=font("Bold",40); d.text((56,34),"Quietly",font=wf,fill=INK)
d.text((56+d.textlength("Quietly",font=wf),34),"Changed",font=wf,fill=RED)
ff=font("Regular",24); t="quietlychanged.com"; d.text((W-56-d.textlength(t,font=ff),46),t,font=ff,fill=GREY)
d.text((56,104),"GOOGLE PRIVACY POLICY  ·  EFFECTIVE OCT 16, 2026",font=font("SemiBold",28),fill=RED)
lf=font("SemiBold",22); bf=font("Regular",30); sb=font("SemiBold",30)
# before
d.text((70,158),"BEFORE",font=lf,fill=GREY)
d.rounded_rectangle([70,188,W-70,268],10,fill=(255,255,255),outline=(220,215,205))
s="We don't show you personalized ads based on your content from"
d.text((94,200),s,font=bf,fill=INK); d.text((94,234),"Drive, Gmail, or Photos.",font=bf,fill=INK)
# after
d.text((70,292),"NOW",font=lf,fill=RED)
d.rounded_rectangle([70,322,W-70,500],10,fill=(255,255,255),outline=(220,215,205))
d.text((94,334),"We don't show you personalized ads based on your content from",font=bf,fill=INK)
x=94; y=372; a="Drive, Gmail, or Google Photos, "
d.text((x,y),a,font=bf,fill=INK); x+=d.textlength(a,font=bf)
lines=[(x,y,"unless you choose to make data from"),(94,410,"these services available to other Google services that"),(94,448,"support personalized ads.")]
for lx,ly,lt in lines:
    w=d.textlength(lt,font=sb); d.rectangle([lx-4,ly+2,lx+w+4,ly+38],fill=HL); d.text((lx,ly),lt,font=sb,fill=INK)
def ctext(y,t,f,fill): d.text(((W-d.textlength(t,font=f))/2,y),t,font=f,fill=fill)
ctext(528,"New: let Search or Gemini access your Gmail, Photos or Drive, and that data",font("Regular",26),RED)
ctext(562,"can \"personalize content, including ads.\" It's opt-in.",font("Regular",26),RED)
ctext(606,"Google's no-ads-from-your-Gmail line now has an exception.",font("Bold",34),INK)
im.save("google-privacy-gmail-ads.png")
