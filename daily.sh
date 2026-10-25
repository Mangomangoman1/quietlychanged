#!/usr/bin/env bash
# QuietlyChanged daily run
set -euo pipefail
cd /workspace/quietlychanged
DAY=$(date +%F)
python3 tracker.py "$DAY"   # 1) fetch + snapshot + diff -> reports/$DAY.json, reports/$DAY-raw.md
# 2) Agent step: read reports/$DAY-raw.md; write reports/$DAY-summary.md (short "# headline" + lede) and
#    reports/$DAY-changes.json: [{"service","page":"pricing|terms|privacy","headline","what","who","url",
#      "tldr","impact":1-3,"redline":[{"before","after","label","note","src":"raw|quoted"}],
#      "effective":"YYYY-MM-DD","deadline","themes":[...],"actions":[...]}]
#    (headline per real change: what changed, who's affected, link; skip noise; "No changes today" if none)
#    Field-by-field rules: EDITORIAL.md. Threads live in themes.json.
[ -f "reports/$DAY-summary.md" ] || { echo "Write reports/$DAY-summary.md, then rerun: ./daily.sh publish"; [ "${1:-}" = publish ] || exit 0; }
python3 tools/seo_snapshot.py > /tmp/qc-seo-before.json
python3 build_site.py       # 3) rebuild docs/
python3 tools/seo_snapshot.py --compare /tmp/qc-seo-before.json | tail -1 || { echo "A published page disappeared from docs/; not publishing."; exit 1; }
git add -A && git commit -qm "Report $DAY" && git push -q origin main   # 4) publish
