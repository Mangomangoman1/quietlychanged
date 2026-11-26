#!/bin/bash
# usage: shot.sh name  (renders name.html -> out png)
google-chrome --headless=new --no-sandbox --disable-gpu --hide-scrollbars --window-size=1200,675 --force-device-scale-factor=1 --screenshot="$2" "file://$PWD/$1.html" >/dev/null 2>&1
