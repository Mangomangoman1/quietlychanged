UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
curl -sL --compressed -m 40 -A "$UA" -H "Accept-Language: en-US,en;q=0.9" -H "Accept: text/html,application/xhtml+xml" -o "$1.html" -w "$1 %{http_code} %{size_download} %{url_effective}\n" "$2"
python3 - "$1.html" <<'PY'
import sys,re,html
s=open(sys.argv[1],errors='ignore').read()
s=re.sub(r'(?is)<(script|style|noscript)[^>]*>.*?</\1>',' ',s)
s=re.sub(r'(?i)<br\s*/?>|</(p|div|li|h\d|tr|td|th|span)>','\n',s)
s=re.sub(r'<[^>]+>',' ',s); s=html.unescape(s)
lines=[re.sub(r'[ \t\xa0]+',' ',l).strip() for l in s.split('\n')]
out='\n'.join(l for l in lines if l)
open(sys.argv[1][:-5]+'.txt','w').write(out)
print('  txt',len(out), 'captcha' if 'captcha' in out.lower() else '')
PY
