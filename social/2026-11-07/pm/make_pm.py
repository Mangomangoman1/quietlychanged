# Nov 7 PM X session images. Logos: Claude mark (claude.ai SVG, from Nov 1 assets), PlayStation logo (Wikimedia Commons SVG, from Nov 6 AM assets), rendered undistorted.
import cairosvg
from PIL import Image, ImageDraw
exec(open("../../2026-10-29/pm/helpers.py").read())
def logo(svg,out,width,bg=(255,255,255)):
    cairosvg.svg2png(url=svg,write_to="/tmp/_l.png",output_width=width)
    lg=Image.open("/tmp/_l.png").convert("RGBA")
    im=Image.new("RGB",(W,H),bg); im.paste(lg,((W-lg.width)//2,(H-lg.height)//2),lg); im.save(out)
logo("claude.svg","01-claude-logo.png",340,(245,240,232))
logo("playstation-logo.svg","01-playstation-logo.png",420)

# Q1: Anthropic consumer terms card
im,d=base()
d.text((56,84),"ANTHROPIC CONSUMER TERMS (CLAUDE FREE/PRO/MAX)  \u00b7  \u00a74 AND \u00a711",font=font("SemiBold",22),fill=RED)
d.text((56,120),"When Claude acts on your files, who carries the risk?",font=font("Bold",38),fill=INK)
card(d,56,190,1144,560,outline=RED,width=3)
y=214
for q,k in [("\u00a74: Claude can take \u201cactions on your behalf, such as software manipulation, data processing, and system interactions (we call these \u2018Actions\u2019)\u201d","Actions"),
            ("\u00a74: \u201cYou are responsible for all Inputs you submit to our Services and all Actions.\u201d","responsible for"),
            ("\u00a74: \u201cActions may not be error free or operate as you intended.\u201d","may not be error free"),
            ("\u00a711: liability capped at the greater of what you paid in the prior six months and $100.","greater of")]:
    y=hlpara(d,84,y,q,mono("Regular",20),1030,(k,))+14
d.text((56,580),"Not legal advice; consumer-protection laws can override some limits (\u201cto the extent permitted by applicable law\u201d).",font=sans("Regular",18),fill=GREY)
d.text((56,612),"Source: anthropic.com/legal/consumer-terms (checked Nov 7, 2026)",font=sans("Regular",18),fill=GREY)
im.save("q1-02-terms-card.png")

# R1: Claude Max pitch then vs pricing page now
im,d=base()
d.text((56,84),"KAHN v. ANTHROPIC, N.D. CAL. 26-CV-05763  \u00b7  ORDER NOV 6, 2026",font=font("SemiBold",22),fill=RED)
d.text((56,120),"The pitch the judge looked at vs. the pricing page now",font=font("Bold",38),fill=INK)
card(d,56,190,580,520,outline=RED,width=3); card(d,620,190,1144,520,outline=GREEN,width=3)
d.text((80,206),"THE PITCH IN THE LAWSUIT",font=sans("Bold",22),fill=RED)
y=250
for l in ["$100 Max 5x: \u201c5x more usage than Pro\u201d","$200 Max 20x: \u201c20x more usage than Pro\u201d","How it worked: 5x/20x per 5-hour session. Weekly, the complaint\u2019s math: ~3.5x and ~6x (Sonnet 4)."]:
    y=hlpara(d,80,y,l,sans("Regular",23),470,("~6x",))+12
d.text((644,206),"CLAUDE.COM/PRICING TODAY",font=sans("Bold",22),fill=GREEN)
y=250
for l in ["$100 Max: \u201c5x the usage of Pro, every 5 hours and every week\u201d","$200 is now \u201cUltra\u201d: \u201c10x Pro usage every week,\u201d no 5-hour limit (verified accounts)","Check yours: Settings \u2192 Usage"]:
    y=hlpara(d,644,y,l,sans("Regular",23),470,("10x Pro usage every week",))+12
hlpara(d,56,534,"Pleading stage only: contract, negligent-misrep and one CLRA claim survive; UCL/FAL dismissed with leave to amend (refile due Dec 2).",sans("Regular",19),1090,())
d.text((56,612),"Sources: Magistrate Judge Alex G. Tse order (Dkt. 50); claude.com/pricing and Claude Help Center, checked Nov 7, 2026",font=sans("Regular",18),fill=GREY)
im.save("r1-02-claude-pricing-card.png")

# R2: PlayStation Direct pre-order fine print
im,d=base()
d.text((56,84),"PULSE ELEVATE ($219.99)  \u00b7  WAS DUE NOV 12, NOW DELAYED, NO NEW DATE",font=font("SemiBold",22),fill=RED)
d.text((56,120),"Pre-ordered on PlayStation Direct? Read this first",font=font("Bold",38),fill=INK)
card(d,56,190,1144,540,outline=RED,width=3)
y=214
for q,k in [("\u201cyour credit card will not be charged until your item is ready to ship\u201d","not be charged"),
            ("\u201cA pre-authorization hold is temporary and does not cause your card to be charged.\u201d","does not cause your card to be charged"),
            ("\u201cyou may cancel your reservation up until the item enters the shipping process\u201d","cancel your reservation"),
            ("Sony, Nov 6: \u201cwe have identified a production issue \u2026 and have made the decision to delay the launch.\u201d No new date, no refund note.","No new date")]:
    y=hlpara(d,84,y,q,mono("Regular",20),1030,(k,))+14
d.text((56,570),"Bought at another store? Its own pre-order terms apply.",font=sans("Regular",20),fill=INK)
d.text((56,612),"Sources: direct.playstation.com Pre-Orders FAQ; PlayStation.Blog update, Nov 6, 2026",font=sans("Regular",18),fill=GREY)
im.save("r2-02-preorder-card.png")
