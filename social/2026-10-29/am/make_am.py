# Oct 29 AM reply images: Apple Live Listen (logo + Apple's own wording). Run from this folder.
import cairosvg, re
from PIL import Image, ImageDraw
src=open("/tmp/dd.py").read().split("# 1) Logo first")[0]
exec(src)
cairosvg.svg2png(url="apple.svg", write_to="apple.png", output_height=440)
im=Image.new("RGB",(W,H),(255,255,255))
lg=Image.open("apple.png").convert("RGBA")
im.paste(lg,((W-lg.width)//2,(H-lg.height)//2),lg)
im.save("01-apple-logo.png")

im,d=base()
d.text((56,84),"APPLE SUPPORT  \u00b7  IPHONE USER GUIDE  \u00b7  LIVE LISTEN",font=font("SemiBold",23),fill=RED)
d.text((56,122),"What \u201cRemote Control\u201d actually does",font=font("Bold",44),fill=INK)
card(d,56,196,1144,470,outline=RED,width=3)
q=("\u201cWhen you use Live Listen on your iPhone, you can remotely start, stop, or jump back in on a session "
   "from your paired Apple Watch or another nearby Apple device that is signed in to the same Apple Account\u2014like"
   " another iPhone or iPad. As your iPhone picks up audio, the text also appears on the other device in real time so you can follow along on either device.\u201d")
hlpara(d,80,214,q,mono("Regular",22),1040,("same Apple Account","signed in","Live Listen on your iPhone"))
sf=sans("Regular",24)
y=500
for l in ["Live Listen turns your iPhone into a mic for your AirPods or hearing aids. Remote control",
          "works from your own devices signed in to your Apple Account, on a session you start."]:
    d.text((56,y),l,font=sf,fill=INK); y+=34
d.text((56,H-48),"Source: support.apple.com/guide/iphone/iph8bf9386f5/ios",font=sans("Regular",18),fill=GREY)
im.save("02-apple-live-listen-wording.png")
