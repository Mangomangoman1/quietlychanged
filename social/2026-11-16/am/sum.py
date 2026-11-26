import json,sys,datetime as dt
import re
s=open(sys.argv[1]).read()
m=re.search(r'Full text: (\S+?\.txt)',s)
if m: s=open(m.group(1)).read()
s=s.replace("\n","")
i=s.find('{"data"'); 
if i<0: i=s.find('{')
d,_=json.JSONDecoder(strict=False).raw_decode(s[i:])
users={u['id']:u['username'] for u in d.get('includes',{}).get('users',[])}
now=dt.datetime.now(dt.timezone.utc)
rows=[]
for p in d.get('data',[]):
  m=p['public_metrics'];t=dt.datetime.fromisoformat(p['created_at'].replace('Z','+00:00'))
  age=int((now-t).total_seconds()/60)
  rows.append((m.get('impression_count',0),age,users.get(p.get('author_id'),''),m['reply_count'],m['like_count'],p['id'],p['text'][:150].replace('\n',' ')))
for r in sorted(rows,reverse=True): print(*r,sep=' | ')
