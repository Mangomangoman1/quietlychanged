from PIL import Image, ImageDraw, ImageFont
F="/usr/share/fonts/truetype/sand-box/google/IBM Plex Serif/IBMPlexSerif-"
S="/usr/share/fonts/truetype/dejavu/DejaVuSans"
def f(w,s): return ImageFont.truetype(F+w+".ttf",s)
W,H=1200,675
im=Image.new("RGB",(W,H),"white"); d=ImageDraw.Draw(im)
d.rectangle([0,0,W,190],fill="#202124")
d.text((56,28),"GOOGLE PRIVACY POLICY  ·  EFFECTIVE OCT 16, 2026",font=ImageFont.truetype(S+"-Bold.ttf",22),fill="#f28b82")
hf=f("Bold",46)
d.text((56,64),'The "no ads from your Gmail" promise',font=hf,fill="white")
d.text((56,120),'just got an 18-word exception.',font=hf,fill="white")
# body
segs=[("We don’t show you personalized ads based on your content from Drive, Gmail, or","n"),("Photos.","del"),("Google Photos,","n"),
("unless you choose to make data from these services available to other Google services that support personalized ads.","ins")]
fn={"n":f("Regular",34),"del":f("Regular",34),"ins":f("Bold",34)}
x0,x,y,lh,maxx=88,88,225,52,1145
d.rectangle([56,215,62,422],fill="#d93025")
for txt,st in segs:
  for w in txt.split(" "):
    fo=fn[st]; tw=d.textlength(w+" ",fo); ww=d.textlength(w,fo)
    if x+ww>maxx: x=x0; y+=lh
    if st=="ins":
      d.rectangle([x-3,y+2,x+tw-2,y+46],fill="#fce8e6"); d.text((x,y),w,font=fo,fill="#c5221f"); d.rectangle([x-3,y+44,x+tw-2,y+48],fill="#d93025")
    elif st=="del":
      d.text((x,y),w,font=fo,fill="#9aa0a6"); d.line([x,y+25,x+ww,y+25],fill="#9aa0a6",width=3)
    else: d.text((x,y),w,font=fo,fill="#202124")
    x+=tw
sf=ImageFont.truetype(S+".ttf",21)
d.text((56,618),"Source: policies.google.com/privacy (red = added)",font=sf,fill="#5f6368")
b=ImageFont.truetype(S+"-Bold.ttf",21); t="QuietlyChanged flagged it Oct 17"
d.text((W-56-d.textlength(t,b),618),t,font=b,fill="#202124")
pf=f("SemiBold",29); pi=f("Regular",29)
d.text((56,468),"In plain English:",font=pf,fill="#202124")
d.text((56,510),"Connect Gmail, Photos or Drive to Search or Gemini",font=pi,fill="#202124")
d.text((56,550),"(Personal Intelligence), and that content may shape your ads.",font=pi,fill="#202124")
im.save("google-gmail-ads-18-words.png")
