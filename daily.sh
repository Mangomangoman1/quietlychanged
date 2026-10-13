#!/usr/bin/env bash
# QuietlyChanged daily run
set -euo pipefail
cd /workspace/quietlychanged
DAY=$(date +%F)
python3 tracker.py "$DAY"   # 1) fetch + snapshot + diff -> reports/$DAY.json, reports/$DAY-raw.md
# 2) Agent step: read reports/$DAY-raw.md and write plain-English reports/$DAY-summary.md
#    (headline per real change: what changed, who's affected, link; skip noise; "No changes today" if none)
[ -f "reports/$DAY-summary.md" ] || { echo "Write reports/$DAY-summary.md, then rerun: ./daily.sh publish"; [ "${1:-}" = publish ] || exit 0; }
python3 build_site.py       # 3) rebuild docs/
git add -A && git commit -qm "Report $DAY" && git push -q origin main   # 4) publish
