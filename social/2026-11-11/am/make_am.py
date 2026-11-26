from PIL import Image, ImageDraw
exec(open("../../2026-10-29/pm/helpers.py").read())
def logo(src,fn,w=900):
    lg=Image.open(src).convert("RGBA"); r=w/lg.width; lg=lg.resize((w,int(lg.height*r)),Image.LANCZOS)
    im=Image.new("RGB",(1200,675),(255,255,255)); im.paste(lg,((1200-lg.width)//2,(675-lg.height)//2),lg); im.save(fn)
logo("msi-logo-src.png","r1-01-msi-logo.png",820)
logo("Japan_Post_Service_Logo.svg.png","r2-01-japan-post-logo.png",960)
def rows_card(fn,kicker,title,rows,src,hl=None,col=430):
    im,d=base()
    d.text((56,84),kicker,font=font("SemiBold",22),fill=RED)
    d.text((56,116),title,font=font("Bold",40),fill=INK)
    y=196
    for i,(a,b) in enumerate(rows):
        if hl==i: d.rectangle((48,y-6,1152,y+44),fill=(255,243,176))
        d.text((56,y),a,font=sans("Bold",26),fill=INK)
        d.text((col,y),b,font=sans("Regular",26),fill=RED if hl==i else INK)
        y+=58
    d.text((56,620),src,font=sans("Regular",18),fill=GREY)
    im.save(fn)
rows_card("r1-02-msi-burn-in-warranty.png","MSI QD-OLED MONITORS  \u00b7  THE FINE PRINT","Burn-in is covered for 3 years",
 [("Warranty","3 years on the OLED panel"),
  ("Covers burn-in?","Yes: \u201cincluding safeguards against the OLED burn-in issue\u201d"),
  ("Region","\u201cSpecific terms may vary by region\u201d"),
  ("Panel Protect","Pixel refresh runs on standby / power-off"),
  ("Firmware","Refresh interval extended to every 24 hours")],
 "Sources: us.msi.com QD-OLED landing page; MSI news, \u201c3-Year Burn-in Warranty for MSI OLED Monitors\u201d (checked Nov 11, 2026)",hl=1,col=330)
rows_card("r2-02-japan-post-germany-fine-print.png","JAPAN POST NOTICE  \u00b7  EFFECTIVE NOV 9, 2026","Japan Post's rule, not a German ban",
 [("To Germany","Online-shop (B2C) mail: not accepted, all mail types"),
  ("Gifts / B2B","Not affected"),
  ("Other EU countries","Still accepted (payment-method limits vary)"),
  ("EU, B2C under \u20ac150","\u20ac3 duty (from Jul 1) + \u20ac2 handling fee (from Nov 1)"),
  ("Charged","Per item in the parcel"),
  ("Couriers","DHL / UPS still offered by shops; duties at the door")],
 "Sources: post.japanpost.jp notices 2026/1104_01 and 2026/1109_01; Aiyu Japan shipping notice, Nov 10 (checked Nov 11, 2026)",hl=0,col=330)
