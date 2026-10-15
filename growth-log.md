# QuietlyChanged growth log
Goal: 500 Google impressions/day by 2026-11-13.

## 2026-10-13: SEO foundation
- Shipped: sitemap.xml (absolute https://quietlychanged.com URLs) and robots.txt pointing to it; JSON-LD (Organization on every page, WebSite on home, NewsArticle on daily reports, WebPage on service pages); unique titles and meta descriptions; 1200×630 og.png and summary_large_image cards.
- Shipped: 54 evergreen service-history pages (/services/<slug>/), e.g. "Netflix price, terms & privacy policy changes (history)", linked from the services table and to each other; their changelogs fill in automatically from reports/DATE-changes.json.
- Baseline: 0 impressions (site just launched). Next: verify in Google Search Console, submit the sitemap, then track impressions here daily.

## 2026-10-14: standalone change articles
- Shipped: every detected change now gets its own article at /changes/<date>-<service>-<headline>/ with an SEO title/description (optional seo_title/seo_desc fields in reports/DATE-changes.json), NewsArticle JSON-LD, and links to the service history and daily report. Report cards, the home page, and service changelogs link to them; they're in the sitemap. Built automatically by build_site.py from now on.
- First two: "Cash App can now auto-sell your bitcoin to cover ACH debits (terms update)" and "Squarespace pricing now lists AI credits by plan, and Basic's 2% store fee".

## 2026-10-14: distribution session
**Best story:** Cash App terms, new section "(c) Automatic Bitcoin Sale to Support ACH Debits" (article: /changes/2026-10-14-cash-app-optional-auto-sell-of-bitcoin-to-fund-ach-debits/). Checked against the live ToS at 3:05 PM MT: the clause is there word for word. Corroboration: Block's Bitcoin Open Roadmap (block.xyz/bitcoin/roadmap, "Updated Sep 29, 2026") lists "Pay bills with bitcoin: In Progress," described as "Automatically sell bitcoin from your Cash App balance to cover monthly bills and ACH debits." The legal text has landed before any announced launch.
- News coverage: none found (WebSearch, X news). On X the only mentions are @grok replies quoting the roadmap item (x.com/grok/status/2109080968338305174). Nobody has reported the ToS clause yet, so we can be first.
- Squarespace (AI credits / Basic 2% fee): no current X/news buzz. Lower priority.

**Live checks (all HTTP 200):** home, both change articles, /reports/2026-10-14.html, /feed.xml (Atom), /sitemap.xml (contains both /changes/ URLs), /robots.txt (Sitemap line present). Home has an Atom `<link rel="alternate">`.
- Gap found: feed.xml only lists daily reports. It has no /changes/ articles and no summaries, which weakens RSS discovery and syndication. Fix in build_site.py (line ~155): add one entry per change article with a summary.
- Ping: Google's sitemap ping endpoint is retired, so there was nothing no-auth to call. IndexNow (Bing/Yandex) needs a key file hosted on the site, a repo change for a later session.

**Drafts prepared (for Samuel's approval, nothing sent):** X post, Bluesky post, LinkedIn post, r/CashApp text post (no self-promo link, because sub rules ban promotion), pitch emails to Bitcoin Magazine (editor@bitcoinmagazine.com, from their editorial-policy page) and The Crypto News (newsroom@thecrypto.news, from their contact page). Full text is in the session report.

**Opportunities (need Samuel's accounts):** FeedSpot publisher submit (feedspot.com/publisher); Show HN; Product Hunt / Indie Hackers launch posts; ask Open Terms Archive / ToS;DR / TOSTracker communities to cross-link. Comparable trackers to watch: tostracker.app, clerica.io, opentermsarchive.org, tosback.org.

**Next steps:** (1) Samuel approves and posts Cash App drafts today while the story is unreported. (2) Add change articles plus summaries to feed.xml. (3) Add an IndexNow key file and ping on each build. (4) Add a "Block roadmap context" line plus a link to the article (stronger E-E-A-T, more search terms: "cash app pay bills with bitcoin").

## 2026-10-15: SEO session
- Shipped: Atom feed now includes every change article (`/changes/<slug>/`) with title (seo_title or service+headline), absolute link/id, updated date, and an HTML-escaped `<summary>` from the `what` field. Daily report entries remain; all entries sorted newest-first. Regenerated `docs/feed.xml` (was 3 report-only entries → 3 reports + 7 change articles with summaries: Shopify, Slack, Anthropic Claude, Figma, Audible, Cash App, Squarespace).
- Shipped (stretch): IndexNow — `indexnow.key` + `docs/<key>.txt`; build pings Bing IndexNow for recent change URLs + home/feed (got HTTP 202 for 10 URLs).
- GSC (sc-domain:quietlychanged.com, last ~7 days via service account): 0 impressions / 0 clicks so far; no queries or pages yet. Sitemap https://quietlychanged.com/sitemap.xml last downloaded 2026-10-14 ~2:17 PM MT, 0 errors, 60 URLs submitted / 0 indexed.
- Expected effect: RSS readers and syndication partners can discover individual change stories (not just bare daily reports), with usable summaries; IndexNow should speed Bing/Yandex discovery of new change URLs.
- Next: wait for Google indexing of /changes/ URLs; consider Cash App "Block roadmap context" E-E-A-T line; keep daily change articles flowing so the feed stays fresh for subscribers.
