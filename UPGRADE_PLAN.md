# QuietlyChanged upgrade plan

> **Status (Oct 25, 2026):** phases 0–4 are built on branch `claude/quietly-changed-upgrade-plan-9szdhg`, except the weekly email digest, which needs an email provider account. One change from the plan: the build stays standard-library Python (no Jinja2), so the daily run can't break on a missing package. Pages live in `qc/`, styles and scripts in `static/`. The writing rules for new fields are in `EDITORIAL.md`.

**Goal:** a visitor who lands on any page (usually from search or X, usually on a change article or a service page) should want to read the next thing, then the next. Today the site is a well-written daily blog. It should feel like a living record of corporate fine print, with a memory.

**Thesis:** *Show the change, don't describe it.* The repo already keeps a daily snapshot of every tracked page and a raw diff of every change (`snapshots/`, `reports/*-raw.md`). The site never shows them. The struck-through sentence is the most gripping thing this topic has, and it's the one thing nobody else publishes.

---

## 1. What's there now (audit, Oct 25 2026)

Build: one 364-line `build_site.py` that writes HTML from Python f-strings, CSS stored as a string, no JS beyond a services filter. Output to `docs/` for GitHub Pages. Fast, SEO-solid (JSON-LD, sitemap, IndexNow, FAQ schema). Keep all of that.

Design and UX problems, roughly in order of cost:

1. **The front page is just yesterday's report.** Whoever lands there gets whatever happened that day. Oct 24's front page is mostly one 5,500-character FCC paragraph inside a card. The 43 changes, 66 services and 15 price histories behind it are a line of links at the bottom.
2. **Walls of text.** `what` averages 1,400 characters and renders as one paragraph, on cards and on articles. The FCC piece already has "Change 1 / Change 2 / What you can do" inside it; the structure is there but not shown.
3. **No sense of weight.** "Figma notes you can connect multiple GitHub orgs" gets the same red-bordered card as "Oura locks your app unless you accept arbitration."
4. **Dead ends.** Every page ends in a "More" paragraph of links. Nothing says "here's the next thing you'll care about."
5. **Every page looks the same.** Report, article, service history, tracker hub and comparison all share one template: 225px masthead, kicker, H1, prose. A Netflix price history is a stack of three tables; it begs to be a chart.
6. **Generic surface.** Cream paper, serif, red accent, double rules: tasteful, but it's the default "newspaper" look. Every link is red and underlined, so card headlines, sources and footers all shout equally.
7. **No reason to come back.** No email, no "watch this service", no countdowns to dates that matter, no personal angle. RSS only.
8. Small things: the comparison table clips its last column on desktop; `screens/` is from day 0; no dark mode; category tags are tiny outlined boxes that all look alike.

## 2. The direction: "the blackline"

Lawyers compare contract versions with a *blackline*: deleted words struck in red, inserted words underlined. That's the native visual language of this subject, and it becomes the site's identity.

- **Redline** (deleted, struck, brand red) and **insert** (underlined, ink blue) are the two brand colors. A highlighter yellow marks "the part that matters."
- **Paper** shifts from warm cream to a cool, slightly blue legal-bond white. Night mode is a dark "carbon copy" palette.
- **Type:** Newsreader (display and reading, optical sizes), IBM Plex Sans (UI), IBM Plex Mono (the record's voice: dates, § numbers, quoted policy text). Self-hosted woff2.
- **Document details as content:** section symbols, "Effective" date stamps, margin notes like a reviewer's comment, line numbers on quoted text.

## 3. Five hooks that pull people deeper

| Hook | What it is | Why it pulls |
|---|---|---|
| **The redline** | Every change opens with the exact before/after sentence, rendered as a blackline, with a margin note explaining it. | Instantly legible, shareable, and only this site has it. |
| **Due soon** | Countdown chips for every change with a date: "Fitbit · 5 days", "Oura · accept by Nov 4". Add-to-calendar (.ics). | Urgency and usefulness. Right now: Fitbit Oct 30, Roblox Nov 1, Rocket Money Nov 2, Oura Nov 4, IPL Nov 9, Pinterest Nov 12, Google Play Nov 17, FCC Nov 25, Evernote Dec 1, IKEA Dec 27. |
| **Threads** | Cross-company stories: *Forced arbitration*, *AI and your data*, *Accept or lose access*, *Shutdowns and deletions*, *Junk fees*, *Who you can complain to*. | This is the binge path. One Oura article leads to DoorDash, Pinterest and Evernote doing the same thing. |
| **Dossiers** | Each service page becomes a profile: monogram, activity strip, price chart, latest redline, "pages we watch, last changed N days ago". | Turns 66 thin pages into destinations, and these are what rank. |
| **Your stack** | Tap the services you use; the site filters to them and says "3 changes affect you this month." Stored in the browser; later, email alerts. | Personal relevance is the strongest pull there is. |

## 4. Page by page

**Change article** (the real front door; most search traffic lands here)
1. Kicker: kind + service monogram + impact meter (Minor / Notable / Major).
2. Headline, then a one-sentence TL;DR in large type.
3. Effective-date stamp with countdown, if there is a date.
4. **The blackline**: 1 to 3 before/after excerpts, with margin notes. Animates the strike once on first view (respecting reduced motion).
5. "What changed", broken into short sections, and "What you can do" as a checklist box.
6. Quick answers (existing FAQ), sources, and a **provenance box**: "First seen in our Oct 17 snapshot · compared against Oct 16 · view full diff."
7. **Keep reading rail**: next in this thread, more from this service, and "Show me another quiet change."
8. Per-change share image (OG) that shows the redline itself, generated at build time with headless Chrome (already used for `og.png`).

**Front page** (an edition, not a blog post)
- Hero: the most consequential live change, with its redline.
- *Due soon* rail of countdown chips.
- *This week*: a compact grid of the week's changes, sized by impact.
- *Threads* row.
- *The seismograph*: a strip of every day since Oct 13 with a tick per change, colored by kind, tall by impact. Click a day to open it.
- *Price leaderboard*: the comparison table as a small bar chart ("Disney+ +207% since 2019").
- Your stack prompt.

**Service dossier**: header with monogram, tracked-since, change count, pages watched. Price-history step chart (inline SVG made at build time) with an optional inflation line ("Netflix +150%; inflation over the same years about +46%"). Timeline of every change, latest redline, related services.

**Threads**: an essay-length intro plus a dated timeline of every change in the thread across companies.

**Archive**: a calendar heatmap instead of a list of dates.

**What we track**: a grid of monograms with "last changed" and activity, filters kept, sources moved to the dossier.

**Everywhere**: a compact sticky top bar (56px) instead of the 225px masthead after the front page; `/` or ⌘K search over everything (client-side JSON index); dark mode; links styled by role, not all red.

## 5. Data the writing step needs to add

Added to each item in `reports/DATE-changes.json`. All optional, so old items still build. Backfill the 43 existing changes once.

```json
{
  "tldr": "Oura's app stops working Nov 4 unless you accept terms that add a jury waiver and batch mass claims.",
  "impact": 3,
  "effective": "2026-11-04",
  "deadline_label": "Accept in app by",
  "themes": ["forced-arbitration", "accept-or-lose-access"],
  "redline": [
    {"before": "…train generalized/non-personalized artificial intelligence…",
     "after":  "…train artificial intelligence…",
     "note":   "The qualifier is gone, so the promise now covers personalized models too."}
  ],
  "sections": [["Change 1: the company picks your opt-out", "…"], ["What stays the same", "…"]],
  "actions": ["Read the opt-out line in each automated text and use exactly that word."]
}
```

A small `themes.json` holds each thread's title and intro. `daily.sh` instructions get updated so the agent writes these fields. The redline excerpts come straight from `reports/DATE-raw.md`, which already has them.

## 6. Build changes

- Keep a Python static generator (fast, free hosting, no framework needed), but split it up:
  `build/` (data loading, helpers), `templates/` (Jinja2 HTML), `static/` (CSS, JS, fonts). One new dependency: Jinja2. This makes design work safe to iterate on instead of editing HTML inside Python strings.
- Charts are inline SVG generated at build time: zero chart libraries, readable by search engines, works without JS. A ~10 KB vanilla JS file adds hover, search, countdowns and Your stack.
- **SEO guardrails:** every current URL, title, description and JSON-LD block stays. Add a check that compares the built URL set and `<title>`s before and after, and fails the build if any disappear.
- Accessibility: redlines use real `<del>`/`<ins>` with screen-reader labels, not just color; contrast checked in both themes; reduced-motion respected.
- Refresh `screens/` automatically after each build (desktop + phone) so it stops going stale.

## 7. Order of work

| Phase | Ships | Size |
|---|---|---|
| **0. Foundation** | Split build into templates/static; new tokens, fonts, compact masthead, dark mode; URL/title regression check; fix comparison table overflow. Visually: same pages, new skin. | M |
| **1. The change page** | Blackline component, TL;DR, impact, deadline stamp, sections + action box, provenance box, keep-reading rail, redline OG images. Backfill 43 changes. | L |
| **2. Front page as an edition** | Hero, Due soon, This week grid, seismograph, price leaderboard. | M |
| **3. Depth** | Threads pages, service dossiers with SVG price charts + inflation line, archive heatmap, search, "Show me another". | L |
| **4. Coming back** | Your stack, .ics deadlines, email digest (Buttondown or similar, works with a static site), "watch this service". | M |

Phase 1 comes before the front page on purpose: the article page is where search visitors arrive, so that's where the pull has to start.

## 8. Things to avoid

- No pop-ups, no fake urgency, no autoplay, no infinite scroll. A site that calls out dark patterns can't use them.
- No client-side framework. The speed and crawlability are assets.
- No changing URLs or titles that already rank.
