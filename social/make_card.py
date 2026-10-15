#!/usr/bin/env python3
"""Branded 1200x675 QuietlyChanged quote card. Usage: make_card.py out.png KICKER HEADLINE SUB"""
import sys
from PIL import Image, ImageDraw, ImageFont
F="/usr/share/fonts/truetype/sand-box/google/IBM Plex Serif/IBMPlexSerif-"
def font(w,s): return ImageFont.truetype(F+w+".ttf", s)
RED=(179,38,30); INK=(28,28,28); BG=(249,247,242); GREY=(95,95,95)
W,H=1200,675
def wrap(d,t,f,maxw):
    out=[];line=""
    for w in t.split():
        c=(line+" "+w).strip()
        if d.textlength(c,font=f)<=maxw: line=c
        else: out.append(line); line=w
    out.append(line); return out
def card(out,kicker,head,sub):
    im=Image.new("RGB",(W,H),BG); d=ImageDraw.Draw(im)
    d.rectangle([0,0,W,8],fill=RED); d.rectangle([0,H-8,W,H],fill=RED)
    wf=font("Bold",44); d.text((56,38),"Quietly",font=wf,fill=INK)
    d.text((56+d.textlength("Quietly",font=wf),38),"Changed",font=wf,fill=RED)
    x0,y0,x1,y1=56,122,W-56,H-100
    d.rounded_rectangle([x0+8,y0+8,x1+8,y1+8],12,fill=(224,221,214))
    d.rounded_rectangle([x0,y0,x1,y1],12,fill="white",outline=(222,220,214))
    d.rectangle([x0,y0,x0+11,y1],fill=RED)
    tx=x0+50; maxw=x1-tx-44; y=y0+40
    d.text((tx,y),kicker.upper(),font=font("SemiBold",26),fill=RED); y+=58
    for size in (58,52,46,40):
        hf=font("Bold",size); hl=wrap(d,head,hf,maxw)
        if len(hl)<=3: break
    for l in hl: d.text((tx,y),l,font=hf,fill=INK); y+=int(size*1.2)
    y+=14; d.line([tx,y,x1-44,y],fill=(222,222,222),width=2); y+=24
    sf=font("Regular",30)
    for l in wrap(d,sub,sf,maxw): d.text((tx,y),l,font=sf,fill=GREY); y+=42
    ff=font("Regular",26); t="quietlychanged.com"
    d.text(((W-d.textlength(t,font=ff))/2,H-68),t,font=ff,fill=GREY)
    im.save(out)
if __name__=="__main__": card(*sys.argv[1:5])
