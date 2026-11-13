import re,html,subprocess,sys,concurrent.futures as cf
pat=re.compile(r'(?i)((?:effective|last (?:updated|revised|modified)|updated|revised)[^.\n]{0,40}?(?:(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)\.? \d{1,2},? 20\d\d|\d{1,2}/\d{1,2}/20\d\d|20\d\d-\d\d-\d\d))')
def f(u):
    try:
        r=subprocess.run(['curl','-sL','--compressed','-m','25','-A','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/130 Safari/537.36','-w','\n%{http_code}',u],capture_output=True,timeout=40)
        t=r.stdout.decode('utf-8','ignore'); code=t.rsplit('\n',1)[-1]
        t=re.sub(r'<script.*?</script>|<style.*?</style>','',t,flags=re.S)
        t=html.unescape(re.sub(r'<[^>]+>',' ',t)); t=re.sub(r'\s+',' ',t)
        ms=sorted(set(m.group(1) for m in pat.finditer(t)))
        hot=[m for m in ms if re.search(r'2026|2027',m)]
        return u,code,len(t),hot[:6]
    except Exception as e: return u,'ERR',0,[str(e)]
urls=[l.strip() for l in open('urls.txt') if l.strip()]
with cf.ThreadPoolExecutor(12) as ex:
    for u,c,n,h in ex.map(f,urls): print(c,n,u,'|',h)
