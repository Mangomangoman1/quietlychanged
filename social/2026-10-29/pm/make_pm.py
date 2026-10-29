# Oct 29 PM reply images: Meta AI glasses (logo + what you can / can't switch off). Run from this folder.
# Logo: Wikimedia Commons "Meta_Platforms_Inc._logo.svg", rendered with cairosvg, centered, undistorted.
import cairosvg
from PIL import Image, ImageDraw
exec(open("helpers.py").read())
cairosvg.svg2png(url="meta.svg", write_to="meta.png", output_width=760)
im=Image.new("RGB",(W,H),(255,255,255))
lg=Image.open("meta.png").convert("RGBA")
im.paste(lg,((W-lg.width)//2,(H-lg.height)//2),lg)
im.save("01-meta-logo.png")

im,d=base()
d.text((56,84),"META AI GLASSES  \u00b7  META'S OWN HELP PAGE AND VOICE PRIVACY NOTICE",font=font("SemiBold",22),fill=RED)
d.text((56,120),"What owners can switch off, and what they can't",font=font("Bold",40),fill=INK)
# left card: visual data
card(d,56,190,588,590,outline=RED,width=3)
d.text((80,204),"AI IMAGES (\u201cvisual data\u201d)",font=sans("Bold",20),fill=RED)
d.text((80,234),"You can turn this off",font=font("Bold",28),fill=INK)
sf=sans("Regular",21)
y=284
for i,l in enumerate(["Open the Meta AI app","Go to your glasses Settings","Tap Meta AI (Experiences)","Toggle off \u201cStore visual data","   from AI experiences\u201d"]):
    lab=(f"{i+1}. " if i<4 else "   ")+l.strip() if i<4 else "    "+l.strip()
    if i>=3: d.rectangle([78,y-2,82+d.textlength(lab,font=sf),y+28],fill=HL)
    d.text((80,y),lab,font=sf,fill=INK); y+=34
y+=14
hlpara(d,80,y,"\u201cYour visual data will not be used for training or other product improvement, and it will not be stored.\u201d",mono("Regular",17),480,())
# right card: voice
card(d,612,190,1144,590)
d.text((636,204),"VOICE RECORDINGS (US)",font=sans("Bold",20),fill=GREY)
d.text((636,234),"No off switch, delete only",font=font("Bold",28),fill=INK)
y=290
for q,k in [("\u201cText transcripts and audio recordings of your voice interactions are stored by default to help improve Meta\u2019s products.\u201d","stored by default"),
            ("\u201cstored for up to one year\u201d","one year"),
            ("\u201cYou can access and delete recordings and related transcripts in the Meta AI App.\u201d","")]:
    y=hlpara(d,636,y,q,mono("Regular",17),480,(k,) if k else ())+12
d.text((56,612),"Sources: meta.com/help/ai-glasses/1381548946634724  \u00b7  meta.com/legal/ai-glasses/voice-controls-privacy-notice (eff. July 22, 2025)",font=sans("Regular",16),fill=GREY)
im.save("02-meta-glasses-switches.png")
