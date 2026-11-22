import sys,re,html
def clean(s):
    s=re.sub(r'(?is)<(script|style|noscript)[^>]*>.*?</\1>',' ',s)
    for _ in range(2):
        s=s.replace('\\"','"').replace('\\r\\n','\n').replace('\\n','\n').replace('\\/','/')
        s=re.sub(r'\\u([0-9a-fA-F]{4})',lambda m:chr(int(m.group(1),16)),s)
        s=html.unescape(s)
    s=re.sub(r'(?i)<br\s*/?>|</(p|div|li|h\d|tr|td|th|a|b|ul|table)>','\n',s)
    s=re.sub(r'<[^>]*>',' ',s)
    s=re.sub(r'"[,}\]]*"?[a-zA-Z]*"?:?(null|"[^"\n]{0,40}")?[,}]*',' ',s) if False else s
    lines=[re.sub(r'\s+',' ',l).strip() for l in s.split('\n')]
    out=[];seen=set()
    for l in lines:
        if not l or l in seen and len(l)<60: continue
        if re.match(r'^(🏀|🏈|🏒|Get Essentials for|Get Sling|Get Select)',l): continue
        seen.add(l); out.append(l)
    return '\n'.join(out)
for n in sys.argv[1:]:
    t=clean(open(n+'.html').read()); open(n+'.txt','w').write(t); print(n,len(t))
