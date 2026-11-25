import re,sys,html
for f in sys.argv[1:]:
    t=open(f,errors='ignore').read()
    t=re.sub(r'<script.*?</script>|<style.*?</style>|<svg.*?</svg>','',t,flags=re.S)
    t=re.sub(r'<(br|/p|/li|/h\d|/div|/tr|/td|/th)[^>]*>','\n',t)
    t=re.sub(r'<[^>]+>','',t); t=html.unescape(t)
    t=re.sub(r'[ \t\xa0]+',' ',t); t=re.sub(r'\n\s*\n+','\n',t)
    open(f.replace('.html','.txt'),'w').write(t)
