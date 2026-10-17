from PIL import Image, ImageDraw, ImageFont
W,H=1200,675
im=Image.new("RGB",(W,H),"#0f1115"); d=ImageDraw.Draw(im)
def f(s,b=True):
    p="/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if b else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
    return ImageFont.truetype(p,s)
d.text((60,48),"Can you opt out of forced arbitration?",font=f(46),fill="#ffffff")
d.text((60,110),"Sleep / fitness trackers, U.S. terms checked Oct 17, 2026",font=f(26,False),fill="#9aa3b2")
rows=[("WHOOP","YES","30-day opt-out, and you can reject","updated terms by email in 30 days","#1f7a4a"),
      ("Eight Sleep","YES","30-day opt-out by writing to","legal@eightsleep.com","#1f7a4a"),
      ("Oura","NO","No opt-out. Accept in the app by Nov 4","or you can't use the app","#a32a2a")]
y=180
for name,ans,l1,l2,col in rows:
    d.rounded_rectangle((60,y,W-60,y+135),radius=18,fill="#1a1d24")
    d.text((90,y+42),name,font=f(38),fill="#ffffff")
    if name=="Oura": d.text((90,y+90),"new terms, Nov 4",font=f(22,False),fill="#9aa3b2")
    d.rounded_rectangle((470,y+30,600,y+105),radius=14,fill=col)
    tw=d.textlength(ans,font=f(40)); d.text((535-tw/2,y+44),ans,font=f(40),fill="#ffffff")
    d.text((630,y+38),l1,font=f(24,False),fill="#d8dce4"); d.text((630,y+72),l2,font=f(24,False),fill="#d8dce4")
    y+=155
d.text((60,H-48),"Sources: each company's Terms of Use   |   quietlychanged.com",font=f(22,False),fill="#9aa3b2")
im.save("social/2026-10-17/oura-optout-comparison.png")
