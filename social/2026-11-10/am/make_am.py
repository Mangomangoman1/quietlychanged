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
        d.text((380,y),b,font=sans("Regular",27),fill=RED if hl==i else INK)
        y+=60
    d.text((56,620),src,font=sans("Regular",18),fill=GREY)
    im.save(fn)
rows_card("r1-02-ps-store-refund-fine-print.png","PLAYSTATION STORE PRE-ORDER REFUNDS  \u00b7  THE FINE PRINT","Pre-load can end your GTA VI refund",
 [("Paid by Nov 4","Cancel any time before the Nov 19 release"),
  ("Paid Nov 5 or later","Cancel within 14 days of payment"),
  ("Either way","Only if the main download hasn't started"),
  ("Auto-downloads","Start the download for you"),
  ("PS5 pre-load","Opened midnight local, Nov 10"),
  ("How to cancel","Contact PlayStation Support"),
  ("Refund goes to","Original payment method (most cards)")],
 "Sources: playstation.com/support/store/cancel-ps-store-pre-order; GTA VI support page (checked Nov 10, 2026)",hl=2)
rows_card("r2-02-xbox-preorder-fine-print.png","MICROSOFT STORE / XBOX PRE-ORDERS  \u00b7  THE FINE PRINT","Cancel online until launch day",
 [("Cancel","\u201cYou can cancel any pre-order online\u201d"),
  ("Where","account.microsoft.com/orders \u2192 Cancel"),
  ("Microsoft balance","Charged right away at pre-order"),
  ("Card / other","May be charged up to 10 days before release"),
  ("Billed already?","Cancel before release = processed as refund"),
  ("No Cancel button?","Use the Request an Xbox refund webform"),
  ("GTA VI launch","Nov 19, 2026")],
 "Sources: support.microsoft.com 'Pre-orders for Microsoft Store'; Xbox Support cancel-order page (checked Nov 10, 2026)",hl=4)
