# QuietlyChanged
Daily tracker of pricing, terms, and privacy pages. `tracker.py` snapshots/diffs, an agent writes `reports/DATE-summary.md` and `reports/DATE-changes.json`, and `build_site.py` renders `docs/` for GitHub Pages (Settings → Pages → main branch, /docs).

- **How to write a change** (summary, impact, blackline excerpts, deadlines, threads): `EDITORIAL.md`
- **Site code**: `qc/` (standard library only), styles and scripts in `static/`
- **Threads**: `themes.json` · **Price histories**: `price_history.json`
- **SEO guard**: `tools/seo_snapshot.py` (used by `daily.sh` to stop a publish that drops a page)
- **Design rationale**: `UPGRADE_PLAN.md`
