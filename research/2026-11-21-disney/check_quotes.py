import json,re,glob,unicodedata
def norm(s):
    s=unicodedata.normalize('NFKC',s)
    for a,b in [('\u2019',"'"),('\u2018',"'"),('\u201c','"'),('\u201d','"'),('\u00a0',' ')]: s=s.replace(a,b)
    return re.sub(r'\s+',' ',s).strip().lower()
corpus={f:norm(open(f,errors='replace').read()) for f in glob.glob('*.txt')}
g=json.load(open('../../guides/disney-plus-plans-and-prices-2026-every-price-increase.json'))
texts=[g['dek']]
def walk(x):
    if isinstance(x,str): texts.append(x)
    elif isinstance(x,list): [walk(i) for i in x]
    elif isinstance(x,dict): [walk(v) for v in x.values()]
walk(g['body'])
qs=[]
for t in texts:
    qs+=re.findall(r'"([^"]{6,})"',t)
ok=bad=0
for q in qs:
    n=norm(q).rstrip('.,')
    hit=[f for f,c in corpus.items() if n in c]
    if hit: ok+=1
    else: bad+=1; print('MISSING:',q)
print(ok,'/',ok+bad,'quotes found')
