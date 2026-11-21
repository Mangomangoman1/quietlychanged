#!/bin/bash
# usage: hfetch.sh name url ...
while [ $# -gt 0 ]; do n=$1; u=$2; shift 2
timeout 60 google-chrome --headless=new --no-sandbox --disable-gpu --virtual-time-budget=15000 --user-agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128 Safari/537.36" --dump-dom "$u" > h_$n.html 2>/dev/null
python3 -c "
import sys;sys.argv=['x'];exec(open('fetch.py').read().split('args=')[0]);t=clean(open('h_$n.html').read());open('h_$n.txt','w').write(t);print('$n',len(t),t.split(chr(10))[0][:80])"
done
