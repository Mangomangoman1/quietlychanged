from PIL import Image, ImageDraw, ImageFont
G="/usr/share/fonts/truetype/sand-box/google/"
import glob
def f(fam,size,pat="*"):
    c=sorted(glob.glob(G+fam+"/"+pat+".ttf"))
    return ImageFont.truetype(c[0],size)
W,H=1080,1350
Y="#FFD60A"; K="#111111"; R="#C1121F"
im=Image.new("RGB",(W,H),Y); d=ImageDraw.Draw(im)
anton=lambda s: f("Anton",s)
inter=lambda s,w="Bold": ImageFont.truetype(glob.glob(G+"Inter/*VariableFont*")[0] if False else G+"Inter/Inter-VariableFont_opsz,wght.ttf",s)
try:
    ib=ImageFont.truetype(G+"Inter/Inter-VariableFont_opsz,wght.ttf",40); ib.set_variation_by_name("Bold")
except Exception as e: print(e)
def IF(s,w="Bold"):
    ft=ImageFont.truetype(G+"Inter/Inter-VariableFont_opsz,wght.ttf",s)
    try: ft.set_variation_by_name(w)
    except Exception: pass
    return ft
M=64
d.text((M,60),"STARTING TOMORROW",font=IF(40,"Black"),fill=K)
d.text((M,100),"OCT 21",font=anton(250),fill=K)
d.text((M,410),"Disney+ and Hulu raise prices for people",font=IF(40,"Bold"),fill=K)
d.text((M,460),"who subscribed before Sep 23.",font=IF(40,"Bold"),fill=K)
d.text((M,515),"The new rate hits your first bill on or after Oct 21.",font=IF(32,"Medium"),fill=K)
rows=[("Disney+ or Hulu, with ads","$11.99","$12.49"),
("Disney+ Premium, no ads","$18.99","$21.49"),
("Hulu Premium, no ads","$18.99","$21.49"),
("Disney+, Hulu bundle, no ads","$19.99","$21.99"),
("+ HBO Max bundle, with ads","$19.99","$21.99"),
("+ HBO Max bundle, no ads","$32.99","$34.99"),
("Hulu + Live TV","$89.99","$99.99"),
("Hulu + Live TV, no ads","$99.99","$109.99")]
y=575
d.rectangle((M,y-10,W-M,y-6),fill=K)
for name,o,n in rows:
    y+=16
    d.text((M,y),name,font=IF(34,"SemiBold"),fill=K)
    fo=IF(32,"Medium"); fn=IF(38,"Black")
    nw=d.textlength(n,font=fn); ow=d.textlength(o,font=fo)
    xn=W-M-nw; xo=xn-40-ow-10
    d.text((xo,y+3),o,font=fo,fill="#5a4a00")
    d.line((xo-2,y+24,xo+ow+2,y+24),fill=R,width=4)
    d.text((xn,y-1),n,font=fn,fill=K)
    y+=54
    d.line((M,y,W-M,y),fill="#d4b200",width=2)
y+=34
d.text((M,y),"Monthly US prices. Annual plans move at renewal.",font=IF(28,"Medium"),fill=K)
d.text((M,y+40),"Not worth it? Cancel or downgrade before your billing date.",font=IF(28,"Bold"),fill=K)
d.rectangle((0,H-90,W,H),fill=K)
d.text((M,H-66),"Source: Hulu + Disney+ help centers, Oct 20",font=IF(26,"Medium"),fill=Y)
t="@QuietlyChanged"; ft=IF(28,"Bold"); d.text((W-M-d.textlength(t,font=ft),H-67),t,font=ft,fill=Y)
im.save("disney-hulu-oct21-bill.png"); print(y)
