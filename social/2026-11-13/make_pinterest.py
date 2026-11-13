from PIL import Image, ImageDraw, ImageFont
import textwrap
W,H=1200,675
im=Image.new("RGB",(W,H),"#faf7f0"); d=ImageDraw.Draw(im)
DJ="/usr/share/fonts/truetype/dejavu/"
B=lambda s:ImageFont.truetype(DJ+"DejaVuSans-Bold.ttf",s)
R=lambda s:ImageFont.truetype(DJ+"DejaVuSans.ttf",s)
SE=lambda s:ImageFont.truetype(DJ+"DejaVuSerif.ttf",s)
d.rectangle([0,0,W,8],fill="#c0392b")
d.text((60,30),"PINTEREST · NEW TERMS + PRIVACY POLICY, LIVE SINCE NOV 12, 2026",font=B(20),fill="#555")
d.text((60,62),"Now in writing: your old Pins can train its gen AI.",font=B(40),fill="#111")
d.text((60,112),"And you're in forced arbitration unless you opt out.",font=B(34),fill="#c0392b")
# redline box
y=180
d.rectangle([60,y,1140,y+225],fill="#ffffff",outline="#ddd")
d.text((80,y+12),"Privacy Policy · How we use the info we collect",font=B(17),fill="#777")
def runs(x,y,parts,font,maxw=1040,lh=30):
    for txt,kind in parts:
        for w in txt.split(" "):
            if not w: continue
            tw=d.textlength(w+" ",font=font)
            if x+tw>80+maxw: x=80; y+=lh
            if kind=="del":
                d.text((x,y),w,font=font,fill="#999"); ww=d.textlength(w,font=font); d.line([x,y+12,x+ww,y+12],fill="#c0392b",width=2)
            elif kind=="ins":
                ww=d.textlength(w,font=font); d.rectangle([x-2,y-1,x+ww+2,y+25],fill="#fde68a"); d.text((x,y),w,font=font,fill="#111")
            else: d.text((x,y),w,font=font,fill="#333")
            x+=tw
    return y
f=SE(21)
y2=runs(80,y+44,[("For example, using information",""),("(such as Pins, regardless of when they were posted)","ins"),("to train, develop and improve our technology such as our machine learning models",""),(", regardless of when Pins were posted.","del"),("and our generative artificial intelligence models.","ins")],f)
d.text((80,y2+44),"Also new: \"voice transcripts\" feed inferences about you, and \"automated tools\" may",font=R(19),fill="#444")
d.text((80,y2+70),"\"scan and analyze your messages to detect harmful or unlawful content.\"",font=R(19),fill="#444")
# opt-out box
y=440
d.rectangle([60,y,1140,y+150],fill="#111")
d.text((84,y+16),"30 DAYS TO OPT OUT OF ARBITRATION",font=B(30),fill="#fde68a")
d.text((84,y+60),"Email litigation@pinterest.com with your name, account email",font=R(23),fill="#fff")
d.text((84,y+90),"and a statement that you're opting out of Section 11.",font=R(23),fill="#fff")
d.text((84,y+120),"Terms took effect Nov 12, so send it by Dec 12, 2026 (our count). Outside the EEA, Switzerland and UK.",font=R(17),fill="#bbb")
d.text((60,630),"Struck: removed. Highlighted: added. Exact wording from Pinterest's old vs live policy.",font=R(17),fill="#666")
d.text((900,624),"quietlychanged.com",font=B(22),fill="#c0392b")
im.save("pinterest-live-terms-ai-optout.png")
