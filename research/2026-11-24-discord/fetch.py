import sys,re,html,time,requests
UA={"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128 Safari/537.36","Accept-Language":"en-US,en;q=0.9"}
def clean(s):
    s=re.sub(r'(?is)<(script|style|noscript)[^>]*>.*?</\1>',' ',s)
    s=re.sub(r'(?i)<br\s*/?>|</(p|div|li|h\d|tr|td|th|span|a)>','\n',s)
    s=re.sub(r'<[^>]+>',' ',s); s=html.unescape(s)
    lines=[re.sub(r'\s+',' ',l).strip() for l in s.split('\n')]
    return '\n'.join(l for l in lines if l)
args=sys.argv[1:]
for i in range(0,len(args),2):
    name,url=args[i],args[i+1]
    try:
        r=requests.get(url,headers=UA,timeout=30)
        r.encoding='utf-8' if b'charset=utf-8' in r.content[:5000].lower() or 'utf' in (r.encoding or '').lower() or True else r.encoding
        open(name+'.html','w').write(r.text); t=clean(r.text); open(name+'.txt','w').write(t)
        print(name,r.status_code,len(t),r.url,'CAPTCHA' if 'captcha' in t.lower() else '')
    except Exception as e: print(name,'ERR',e)
    time.sleep(float(__import__('os').environ.get('SLEEP','1')))
