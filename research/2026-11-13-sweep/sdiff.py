import re,sys,difflib
def sents(p):
    t=open(p).read()
    t=re.sub(r'\s+',' ',t)
    return [s.strip() for s in re.split(r'(?<=[.;:!?])\s+(?=[A-Z0-9(“"])',t) if s.strip()]
a,b=sents(sys.argv[1]),sents(sys.argv[2])
for op,i1,i2,j1,j2 in difflib.SequenceMatcher(None,a,b,autojunk=False).get_opcodes():
    if op=='equal': continue
    print('=====',op)
    for s in a[i1:i2]: print('- ',s)
    for s in b[j1:j2]: print('+ ',s)
