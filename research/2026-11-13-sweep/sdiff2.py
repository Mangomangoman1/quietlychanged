import re,sys,difflib
def sents(p):
    t=open(p).read(); t=re.sub(r'\s+',' ',t)
    return [s.strip() for s in re.split(r'(?<=[.;:!?])\s+(?=[A-Z0-9(“"])',t) if s.strip()]
a,b=sents(sys.argv[1]),sents(sys.argv[2])
def norm(s): return re.sub(r'\b(the|these)\b','',s.lower())
for op,i1,i2,j1,j2 in difflib.SequenceMatcher(None,a,b,autojunk=False).get_opcodes():
    if op=='equal': continue
    A=' '.join(a[i1:i2]); B=' '.join(b[j1:j2])
    if norm(A)==norm(B): continue
    # word diff
    wa,wb=A.split(),B.split()
    out=[]
    for o,x1,x2,y1,y2 in difflib.SequenceMatcher(None,wa,wb,autojunk=False).get_opcodes():
        if o=='equal':
            seg=wa[x1:x2]; out.append(' '.join(seg) if len(seg)<16 else ' '.join(seg[:6])+' … '+' '.join(seg[-6:]))
        else:
            if x2>x1: out.append('[-'+' '.join(wa[x1:x2])+'-]')
            if y2>y1: out.append('{+'+' '.join(wb[y1:y2])+'+}')
    print('=====',' '.join(out)); print()
