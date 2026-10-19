from PIL import Image, ImageDraw, ImageFont
G="/usr/share/fonts/truetype/sand-box/google/"
def mono(w,s): return ImageFont.truetype(G+"IBM Plex Mono/IBMPlexMono-"+w+".ttf",s)
def sans(w,s): return ImageFont.truetype(G+"Fira Sans/FiraSans-"+w+".ttf",s)
def serif(w,s): return ImageFont.truetype(G+"IBM Plex Serif/IBMPlexSerif-"+w+".ttf",s)

# ---------- Post A: GitHub pricing as a git diff (dark) ----------
W,H=1200,675
BG=(13,17,23); PANEL=(22,27,34); BORDER=(48,54,61); TXT=(230,237,243); MUTED=(139,148,158)
DELBG=(73,2,11); DELTX=(255,161,152); ADDBG=(4,60,31); ADDTX=(126,231,135); YEL=(255,214,10)
im=Image.new("RGB",(W,H),BG); d=ImageDraw.Draw(im)
d.text((48,36),"github.com/pricing",font=mono("SemiBold",30),fill=MUTED)
d.text((48,78),"Secret Protection, changed Oct 17, 2026",font=sans("Bold",44),fill=TXT)
x0,y0,x1=48,150,W-48
d.rounded_rectangle([x0,y0,x1,y0+68+5*72+8],12,fill=PANEL,outline=BORDER,width=2)
d.rectangle([x0+2,y0+2,x1-2,y0+50],fill=(30,36,44))
d.text((x0+20,y0+10),"pricing.txt   Oct 16 → Oct 17",font=mono("Medium",24),fill=MUTED)
rows=[("-","Copilot secret scanning",DELBG,DELTX,False),
      ("+","AI detection for alerts",ADDBG,ADDTX,False),
      ("+","AI detection for push protection",ADDBG,ADDTX,False),
      ("+","   Usage-based",ADDBG,ADDTX,True),
      ("+","   …and block pushes that contain them",ADDBG,ADDTX,False)]
y=y0+68; f=mono("Medium",36)
for sign,txt,bg,fg,hl in rows:
    d.rectangle([x0+2,y,x1-2,y+62],fill=bg)
    d.text((x0+22,y+10),sign,font=f,fill=fg)
    if hl:
        tw=d.textlength("Usage-based",font=mono("Bold",36))
        d.rectangle([x0+70+d.textlength("   ",font=f)-8,y+8,x0+70+d.textlength("   ",font=f)+tw+8,y+56],fill=YEL)
        d.text((x0+70,y+10),"   ",font=f,fill=fg)
        d.text((x0+70+d.textlength("   ",font=f),y+10),"Usage-based",font=mono("Bold",36),fill=(20,20,20))
    else:
        d.text((x0+70,y+10),txt,font=f,fill=fg)
    y+=72
d.text((48,600),"AI password detection that blocks pushes is billed by usage,",font=sans("SemiBold",27),fill=TXT)
d.text((48,633),"not included in the plan price.",font=sans("SemiBold",27),fill=TXT)
t="quietlychanged.com"; d.text((W-48-d.textlength(t,font=mono("Medium",24)),636),t,font=mono("Medium",24),fill=MUTED)
im.save("github-usage-based-diff.png")

# ---------- Post B: fine print of the week (tall receipts) ----------
W,H=1080,1350
BG=(24,24,24); PAPER=(250,248,240); INK=(30,30,30); RED=(200,40,30); HL=(255,226,92); GREY=(110,110,110)
im=Image.new("RGB",(W,H),BG); d=ImageDraw.Draw(im)
d.text((60,50),"FINE PRINT",font=sans("Bold",92),fill=(255,255,255))
d.text((60,150),"that changed this week",font=sans("Regular",50),fill=(220,220,220))
cards=[("ROBINHOOD · Customer Agreement §36A",[("You agree that you ",0),("cannot separately bring a",1),("lawsuit",1),(", at any time, against any named defendant…",0)],"Auto-enrolled Nov 18. Service keeps 20% of payouts."),
       ("DOORDASH · Terms, effective Oct 16",[("Related Third Parties include… ",0),("Amplitude, Persona,",1),("Checkr, Blue Star, Stripe, Payfare",1)],"Its arbitration clause now covers those vendors too."),
       ("PROTON · Terms, updated Oct 9",[("…discontinue any of our Services… ",0),("with or",1),("without notice to you.",1)],"It will \"endeavor\" to warn you, but has no obligation."),
       ("GOOGLE · Privacy Policy, effective Oct 16",[("…ads based on your content from Drive, Gmail, or Google Photos, ",0),("unless you choose to make data from these services available",1),("…",0)],"Opt-in: applies if you let Search or Gemini use that data.")]
y=240; qf=serif("Regular",33); qb=serif("SemiBold",33)
for i,(hdr,parts,note) in enumerate(cards):
    def lay(cd,draw):
        x,yy=28,64; maxw=W-120-56
        for txt,hl in parts:
            f=qb if hl else qf
            for word in txt.split(" "):
                if word=="": continue
                w=cd.textlength(word+" ",font=f)
                if x+w>maxw+28: x=28; yy+=44
                if draw:
                    if hl: cd.rectangle([x-3,yy+4,x+cd.textlength(word,font=f)+3,yy+42],fill=HL)
                    cd.text((x,yy),word,font=f,fill=INK)
                x+=w
        return yy
    h=lay(d,False)+44+62
    ang=[-0.6,0.5,-0.4,0.6][i]
    card=Image.new("RGBA",(W-120,h),PAPER+(255,)); cd=ImageDraw.Draw(card)
    cd.text((28,20),hdr,font=sans("Bold",26),fill=RED)
    lay(cd,True)
    cd.text((28,h-46),note,font=sans("Medium",26),fill=GREY)
    card=card.rotate(ang,expand=True,resample=Image.BICUBIC)
    im.paste(card,(60-(card.width-(W-120))//2,y),card)
    y+=h+14
t="Old vs. new wording, sourced: quietlychanged.com"
d.text(((W-d.textlength(t,font=sans("SemiBold",30)))/2,H-62),t,font=sans("SemiBold",30),fill=(255,255,255))
im.save("fine-print-week.png")
