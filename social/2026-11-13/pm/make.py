from PIL import Image, ImageDraw, ImageFont
B='/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf'; R='/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf'
def f(p,s): return ImageFont.truetype(p,s)
W,H=1200,675
im=Image.new('RGB',(W,H),'#0f172a'); d=ImageDraw.Draw(im)
d.text((60,42),"Flight canceled by the ground stop?",font=f(B,52),fill='white')
d.text((60,108),"US DOT refund rule (14 CFR 260.6)",font=f(R,30),fill='#94a3b8')
rows=[("Canceled flight","Full cash refund if you turn down the rebooking or voucher"),
      ("Delayed 3+ hrs","Same right if you'll land 3+ hrs late (6+ hrs international)"),
      ("What's included","Fare + taxes + paid extras like bag & seat fees"),
      ("How fast","Credit card: within 7 business days. Other payment: 20 days"),
      ("The trap","Accept a voucher or the new flight and the cash right is gone")]
y=180
for i,(a,b) in enumerate(rows):
    col='#fbbf24' if i==4 else '#38bdf8'
    d.rounded_rectangle((60,y,1140,y+78),14,fill='#1e293b')
    d.text((84,y+22),a,font=f(B,30),fill=col)
    d.text((370,y+24),b,font=f(R,27),fill='white')
    y+=90
d.text((60,H-36),"Applies to US flights no matter who caused it. Source: eCFR, 14 CFR 260.2 & 260.6.  quietlychanged.com",font=f(R,20),fill='#94a3b8')
im.save('r1-refund-rule-card.png')
