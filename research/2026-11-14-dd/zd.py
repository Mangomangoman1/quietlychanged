import json,urllib.request,sys,concurrent.futures as cf
hosts=sys.argv[1:]
UA={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) Chrome/130 Safari/537.36','Accept':'application/json'}
def go(h):
    u=f"https://{h}/api/v2/help_center/en-us/articles.json?sort_by=edited_at&sort_order=desc&per_page=30"
    try:
        d=json.load(urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=20))
        out=[f"## {h} ({d.get('count')})"]
        for a in d['articles']:
            if a["edited_at"]>='2026-11-01': out.append(f"  {a["edited_at"][:10]} {a['title'][:110]} {a['html_url']}")
        return '\n'.join(out)
    except Exception as e: return f"## {h} ERR {str(e)[:60]}"
with cf.ThreadPoolExecutor(16) as ex:
    for r in ex.map(go,hosts): print(r)
