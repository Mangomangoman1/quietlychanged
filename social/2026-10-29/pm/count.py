import re,sys
def w(t):
    t=re.sub(r'https?://\S+','x'*23,t)
    n=0
    for ch in t:
        o=ord(ch)
        n+= 1 if (o<=0x10FF or 0x2000<=o<=0x200D or 0x2010<=o<=0x201F or 0x2032<=o<=0x2037) else 2
    return n
for f in sys.argv[1:]:
    t=open(f).read().rstrip('\n'); print(f, w(t))
