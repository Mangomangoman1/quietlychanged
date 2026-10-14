# QuietlyChanged growth log
Goal: 500 Google impressions/day by 2026-11-13.

## 2026-10-13: SEO foundation
- Shipped: sitemap.xml (absolute https://quietlychanged.com URLs) and robots.txt pointing to it; JSON-LD (Organization on every page, WebSite on home, NewsArticle on daily reports, WebPage on service pages); unique titles and meta descriptions; 1200×630 og.png and summary_large_image cards.
- Shipped: 54 evergreen service-history pages (/services/<slug>/), e.g. "Netflix price, terms & privacy policy changes (history)", linked from the services table and to each other; their changelogs fill in automatically from reports/DATE-changes.json.
- Baseline: 0 impressions (site just launched). Next: verify in Google Search Console, submit the sitemap, then track impressions here daily.

## 2026-10-14: standalone change articles
- Shipped: every detected change now gets its own article at /changes/<date>-<service>-<headline>/ with an SEO title/description (optional seo_title/seo_desc fields in reports/DATE-changes.json), NewsArticle JSON-LD, and links to the service history and daily report. Report cards, the home page, and service changelogs link to them; they're in the sitemap. Built automatically by build_site.py from now on.
- First two: "Cash App can now auto-sell your bitcoin to cover ACH debits (terms update)" and "Squarespace pricing now lists AI credits by plan, and Basic's 2% store fee".
