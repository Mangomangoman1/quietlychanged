import re,html,sys
t=open(sys.argv[1],errors='ignore').read()
t=re.sub(r'(?s)<(script|style|noscript)[^>]*>.*?</\1>',' ',t)
t=re.sub(r'(?i)<br\s*/?>|</(p|div|li|h\d|tr)>','\n',t)
t=html.unescape(re.sub(r'<[^>]+>',' ',t))
t=re.sub(r'[ \t\xa0]+',' ',t); t=re.sub(r'\n\s*\n+','\n',t)
open(sys.argv[2],'w').write(t)
