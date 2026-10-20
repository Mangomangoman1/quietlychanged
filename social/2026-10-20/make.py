from PIL import Image, ImageDraw, ImageFont
G="/usr/share/fonts/truetype/sand-box/google/"
def serif(w,s): return ImageFont.truetype(G+"IBM Plex Serif/IBMPlexSerif-"+w+".ttf",s)
def mono(w,s): return ImageFont.truetype(G+"IBM Plex Mono/IBMPlexMono-"+w+".ttf",s)
W,H=1200,675; BG=(250,247,240); INK=(28,28,28); MUT=(110,104,96); RED=(179,38,30); CARD=(255,255,255); BOR=(220,213,200)
def wrap(d,text,font,maxw):
    out=[];line=""
    for w in text.split():
        t=(line+" "+w).strip()
        if d.textlength(t,font=font)<=maxw: line=t
        else: out.append(line); line=w
    out.append(line); return out
def footer(d):
    d.line([56,612,W-56,612],fill=BOR,width=2)
    d.text((56,624),"Quietly",font=serif("Bold",32),fill=INK)
    d.text((56+d.textlength("Quietly",font=serif("Bold",32)),624),"Changed",font=serif("Bold",32),fill=RED)
    t="quietlychanged.com"; d.text((W-56-d.textlength(t,font=mono("Medium",22)),632),t,font=mono("Medium",22),fill=MUT)

# 1) Proton before/after
im=Image.new("RGB",(W,H),BG); d=ImageDraw.Draw(im); d.rectangle([0,0,W,8],fill=RED)
d.text((56,32),"proton.me/legal/terms  ·  3. Inactive Accounts  ·  spotted Oct 20, 2026",font=mono("Medium",21),fill=MUT)
d.text((56,66),"Before Proton deletes an inactive free account:",font=serif("Bold",42),fill=INK)
def box(y,label,text,hl,strike_words=None):
    h=200
    d.rounded_rectangle([56,y,W-56,y+h],14,fill=CARD,outline=RED if hl else BOR,width=4 if hl else 2)
    d.text((84,y+16),label,font=mono("Medium",20),fill=RED if hl else MUT)
    f=serif("Regular",31); yy=y+52
    for ln in wrap(d,text,f,W-170):
        d.text((84,yy),ln,font=f,fill=INK if hl else MUT); 
        if not hl:
            tw=d.textlength(ln,font=f); d.line([84,yy+20,84+tw,yy+20],fill=(150,140,130),width=2)
        yy+=42
    return f
box(140,"UNTIL OCT 19","\u201cYou will receive notices 30, 15 and 7 days in advance before such action is taken on the recovery email associated with your Account.\u201d",False)
f=box(360,"NOW","\u201cAs a mere courtesy, the Company will aim to send notice to the recovery email associated with your Account 30, 15 and 7 days in advance\u2026\u201d",True)
# underline the key phrase in the NOW box
x0=84; ln1=wrap(d,"\u201cAs a mere courtesy, the Company will aim to send notice to the recovery email associated with your Account 30, 15 and 7 days in advance\u2026\u201d",f,W-170)[0]
p="\u201cAs a mere courtesy"; d.line([x0,412+38,x0+d.textlength(p,font=f),412+38],fill=RED,width=4)
q=", the Company "; xs=x0+d.textlength(p+q,font=f); d.line([xs,450,xs+d.textlength("will aim to",font=f),450],fill=RED,width=4)
d.text((56,572),"Page still says \u201cLast modified: October 09, 2026.\u201d",font=serif("Italic",24),fill=MUT)
footer(d); im.save("proton-inactive-deletion-notice.png")

# 2) Spotify big number
im=Image.new("RGB",(W,H),BG); d=ImageDraw.Draw(im); d.rectangle([0,0,W,8],fill=RED)
d.text((56,32),"spotify.com/us/premium  ·  Oct 20, 2026",font=mono("Medium",22),fill=MUT)
d.text((56,70),"Spotify Premium free trial, new US users",font=serif("Bold",44),fill=INK)
cy=170
d.rounded_rectangle([56,cy,520,cy+330],14,fill=CARD,outline=BOR,width=2)
d.text((84,cy+20),"UNTIL OCT 19",font=mono("Medium",20),fill=MUT)
f=serif("Bold",150); t="1"; d.text((84,cy+50),t,font=f,fill=MUT); d.text((84+d.textlength(t,font=f)+20,cy+130),"month",font=serif("Regular",44),fill=MUT)
d.text((84,cy+260),"free, then $12.99/mo",font=serif("Regular",28),fill=MUT)
d.text((540,cy+120),"\u2192",font=serif("Bold",80),fill=RED)
d.rounded_rectangle([640,cy,W-56,cy+330],14,fill=CARD,outline=RED,width=4)
d.text((668,cy+20),"NOW, UNTIL NOV 1",font=mono("Medium",20),fill=RED)
t="2"; d.text((668,cy+50),t,font=f,fill=RED); d.text((668+d.textlength(t,font=f)+20,cy+130),"months",font=serif("Regular",44),fill=INK)
d.text((668,cy+260),"free, then $12.99/mo",font=serif("Regular",28),fill=INK)
d.text((56,528),"Premium Individual only. Only if you\u2019ve never tried Premium before.",font=serif("Regular",27),fill=INK)
d.text((56,566),"Spotify\u2019s page: \u201cOffer ends November 1, 2026.\u201d",font=serif("Italic",24),fill=MUT)
footer(d); im.save("spotify-2-month-trial.png")
