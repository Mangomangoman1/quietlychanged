from PIL import Image, ImageDraw, ImageFont
W,H=1200,675
im=Image.new("RGB",(W,H),"#faf7f0"); d=ImageDraw.Draw(im)
DJ="/usr/share/fonts/truetype/dejavu/"
B=lambda s:ImageFont.truetype(DJ+"DejaVuSans-Bold.ttf",s)
R=lambda s:ImageFont.truetype(DJ+"DejaVuSans.ttf",s)
M=lambda s:ImageFont.truetype(DJ+"DejaVuSansMono.ttf",s)
d.rectangle([0,0,W,8],fill="#c0392b")
d.text((60,40),"SLACK BUSINESS+ · PRICING PAGE",font=B(24),fill="#555")
d.text((60,80),"Slackbot AI now capped at",font=B(46),fill="#111")
d.text((60,140),"15 messages per user a week",font=B(62),fill="#c0392b")
y=250
d.text((60,y),"BEFORE (Nov 10)",font=B(20),fill="#777")
d.rectangle([60,y+30,1140,y+110],fill="#fde2e2")
d.text((80,y+42),"\"Your personal AI agent that understands conversations,",font=M(22),fill="#7a1f1f")
d.text((80,y+74),"files, and projects in Slack. Plan limits apply.\"",font=M(22),fill="#7a1f1f")
y=380
d.text((60,y),"AFTER (Nov 11)",font=B(20),fill="#777")
d.rectangle([60,y+30,1140,y+110],fill="#dff3e3")
d.text((80,y+42),"\"Find answers, summarize channels, and work across your apps.",font=M(22),fill="#1d5a2c")
d.text((80,y+74),"15 messages per user each week. Contact sales to add more.\"",font=M(22),fill="#1d5a2c")
d.text((60,530),"Unlimited Slackbot is now an Enterprise+ feature, listed at",font=R(26),fill="#222")
d.text((60,566),"$45/user/month (annual). Business+ is $15.",font=R(26),fill="#222")
d.text((60,625),"quietlychanged.com",font=B(22),fill="#c0392b")
im.save("slack-slackbot-cap.png")
