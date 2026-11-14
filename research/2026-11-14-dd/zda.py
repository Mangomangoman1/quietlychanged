import json,urllib.request,sys,re,html
h=sys.argv[1]
for aid in sys.argv[2:]:
    u=f"https://{h}/api/v2/help_center/en-us/articles/{aid}.json"
    a=json.load(urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0 Chrome/130'}),timeout=20))['article']
    b=a['body']; b=re.sub(r'(?i)<br\s*/?>|</(p|li|h\d|tr|div)>','\n',b); b=html.unescape(re.sub(r'<[^>]+>',' ',b)); b=re.sub(r'[ \t\xa0]+',' ',b); b=re.sub(r'\n\s*\n+','\n',b)
    txt=f"# {a['title']}\nURL: {a['html_url']}\ncreated {a['created_at']} edited {a['edited_at']} updated {a['updated_at']}\n\n{b}\n"
    open(f"zd-{aid}.txt","w").write(txt); print(txt[:4000]); print('-----')
