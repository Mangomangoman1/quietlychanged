# Oct 30 PM reply images: France data tax (Assemblée nationale amendment I-1358, PLF 2027), read Oct 30, 2026.
from PIL import Image, ImageDraw
exec(open("../../2026-10-29/pm/helpers.py").read())
SRC="Source: assemblee-nationale.fr, amendement n\u00b0 I-1358, projet de loi de finances 2027 (read Oct 30, 2026)"
# R1 card: what passed / what it isn't / what's next
im,d=base()
d.text((56,84),"FRANCE'S \u20ac0.055-PER-GB DATA TAX  \u00b7  OCT 30, 2026",font=font("SemiBold",22),fill=RED)
d.text((56,120),"What actually passed, and what it isn't",font=font("Bold",40),fill=INK)
cols=[("WHAT PASSED",RED,["Amendment I-1358 to the 2027 budget, adopted on the Assembly floor (1st reading)","\u20ac0.055 per GB sent to users in France, paid by senders like Google or Netflix","Capped: 15% of French or 2% of global revenue"]),
      ("WHAT IT ISN'T",GREY,["Not a charge on your internet bill: ISPs only count the GBs","Not content tracking: no record of content or destination allowed","Not law yet"]),
      ("WHAT'S NEXT",GREY,["The Senate reads the budget","It has to survive into the final 2027 budget","Backers' estimate: \u20ac10B a year"])]
x=56; w=352
for t,c,items in cols:
    card(d,x,190,x+w,580,outline=c,width=3 if c==RED else 2)
    d.text((x+22,206),t,font=sans("Bold",20),fill=c)
    y=246
    for it in items:
        y=hlpara(d,x+22,y,"\u2022 "+it,sans("Regular",19),w-44,())+16
    x+=w+20
d.text((56,612),SRC,font=sans("Regular",17),fill=GREY)
im.save("01-france-what-passed.png")
# R2: the amendment's own words, highlighted
im,d=base()
d.text((56,84),"THE AMENDMENT'S OWN WORDS  \u00b7  ART. 302 BIS ZQ & ZR",font=font("SemiBold",22),fill=RED)
d.text((56,120),"Who pays, how it's counted, and the ceiling",font=font("Bold",40),fill=INK)
card(d,56,190,1144,580,outline=RED,width=3)
y=214
for fr,en,k in [("\u00ab L\u2019\u00e9metteur est redevable d\u2019une taxe \u00e9gale au produit de la somme des volumes de donn\u00e9es [\u2026] exprim\u00e9s en gigaoctet et 0,055 euros. \u00bb","The sender owes \u20ac0.055 per gigabyte.","0,055 euros"),
                ("\u00ab \u2026un plafonnement correspondant au maximum \u00e0 15 % du chiffre d\u2019affaires r\u00e9alis\u00e9 en France par l\u2019\u00e9metteur ou \u00e0 2 % de son chiffre d\u2019affaires total. \u00bb","Capped at 15% of French revenue or 2% of total revenue.","15 %"),
                ("\u00ab Aucun relev\u00e9 relatif au contenu des donn\u00e9es ni \u00e0 leur destination ne peut \u00eatre exig\u00e9. \u00bb","ISPs report volumes only: no content, no destination.","Aucun relev\u00e9")]:
    y=hlpara(d,84,y,fr,mono("Regular",19),1030,(k,))+4
    d.text((84,y),en,font=sans("Bold",21),fill=INK); y+=44
d.text((56,612),SRC,font=sans("Regular",17),fill=GREY)
im.save("02-france-amendment-text.png")
