from PIL import Image, ImageDraw
exec(open("../../2026-10-29/pm/helpers.py").read())
def rows_card(fn,kicker,title,rows,src,hl=None):
    im,d=base()
    d.text((56,84),kicker,font=font("SemiBold",22),fill=RED)
    d.text((56,116),title,font=font("Bold",40),fill=INK)
    y=196
    for i,(a,b) in enumerate(rows):
        if hl==i: d.rectangle((48,y-6,1152,y+44),fill=(255,243,176))
        d.text((56,y),a,font=sans("Bold",27),fill=INK)
        d.text((360,y),b,font=sans("Regular",27),fill=RED if hl==i else INK)
        y+=60
    d.text((56,620),src,font=sans("Regular",18),fill=GREY)
    im.save(fn)
rows_card("r2-02-xfinity-boost-fine-print.png","XFINITY GTA VI SPEED BOOST  \u00b7  THE FINE PRINT","The 15-day clock starts when you claim it",
 [("How to claim","Xfinity app or xfinity.com/membership"),
  ("Claim window","Nov 9 to Dec 3, 2026"),
  ("How long","Up to 15 days from activation"),
  ("Claim on Dec 3","Boost lasts until Dec 18"),
  ("Option missing?","Xfinity says contact Customer Service"),
  ("Older plans","1.2TB/month cap; then $10 per 50GB, max $100"),
  ("GTA VI pre-load","Up to 212GB, about 18% of a 1.2TB cap")],
 "Sources: Xfinity press release, Business Wire (Nov 9, 2026); xfinity.com/learn/internet-service/data; PlayStation support",hl=2)
rows_card("r1-02-gta6-preload-card.png","GTA VI PRE-LOAD  \u00b7  PER ROCKSTAR / PLAYSTATION SUPPORT","Before you hit download tonight",
 [("Free space","Up to 212GB, depending on console"),
  ("Xbox Series X|S","Live now (midnight GMT Nov 10)"),
  ("PS5","Midnight local time, Nov 10"),
  ("Physical edition","Download code in the box. No disc."),
  ("Price","Standard $79.99  \u00b7  Ultimate $99.99"),
  ("Launch","Nov 19, 2026"),
  ("To auto pre-load","Auto-downloads on; console on or in sleep")],
 "Sources: playstation.com GTA VI support page; The Verge; PCWorld (checked Nov 9, 2026)",hl=3)
im,d=base()
d.text((56,84),"GOOGLE GEMINI APPS PRIVACY HUB  \u00b7  SUPPORT.GOOGLE.COM",font=font("SemiBold",22),fill=RED)
d.text((56,116),"Editing the summary isn\u2019t deleting the chat",font=font("Bold",40),fill=INK)
qs=["\u201cTo stop Gemini from personalizing your experience using info from a past chat, delete that chat.\u201d",
    "Chats reviewed by human reviewers \u201care not deleted when you delete your activity. Instead, they are retained for up to three years.\u201d",
    "Auto-delete default: 18 months. You can change it to 3 months, 36 months, or indefinite."]
y=196
for i,q in enumerate(qs):
    ls=wrap(d,q,sans("SemiBold",28),1060)
    if i<2: d.rectangle((48,y-8,1152,y+len(ls)*40),fill=(255,243,176))
    for l in ls: d.text((64,y),l,font=sans("SemiBold" if i<2 else "Regular",28),fill=INK); y+=40
    y+=30
d.text((56,620),"Source: support.google.com/gemini/answer/13594961 (Privacy Hub, updated Oct 26, 2026), checked Nov 9, 2026",font=sans("Regular",18),fill=GREY)
im.save("r3-02-gemini-memory-fine-print.png")
