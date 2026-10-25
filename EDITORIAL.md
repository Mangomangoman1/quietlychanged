# QuietlyChanged editorial guide

How to write a change so the site can show it well. This is the brief for whoever (or whatever agent) writes `reports/DATE-changes.json` each day. The build is `python3 build_site.py`; it needs only the Python standard library.

## The idea in one line

**Show the change, don't just describe it.** Every change opens with the exact words that were removed and added (the *blackline*), a one-sentence summary, how much it matters, and any date the reader has to act by. The long write-up comes after.

## A change, field by field

Required, as before: `service`, `page` (`pricing` | `terms` | `privacy`), `headline`, `what`, `who`, `url`.

Strongly recommended for every new change:

| Field | What to write | Rules |
|---|---|---|
| `tldr` | One or two plain sentences: what changed and what it means for a person. Shown under the headline, on cards, in search and in share previews. | Under ~180 characters. No jargon. Say the consequence ("…BofA no longer investigates…"), not the mechanism. |
| `impact` | `1` Minor, `2` Notable, `3` Major. | **3** = changes what people pay, what they can do, or what happens to their data, often with a deadline (Oura's lock-out, Robinhood's 20% cut, the FCC opt-out rule). **2** = worth knowing if you use the service (Proton's "courtesy" warnings, a new fee). **1** = small edits (feature rows, relabeled plans, renamed policies). Be strict: if everything is Major, nothing is. |
| `redline` | 1–3 excerpts: `{"before": "...", "after": "...", "label": "...", "note": "...", "src": "raw" or "quoted"}` | See below. |
| `effective` | `YYYY-MM-DD` of the date that matters to readers. | Only real dates from the documents: when terms take effect, when a feature ends, an opt-out or comment deadline. |
| `deadline` | Short label shown before the date: "Accept in the app by", "Takes effect", "Shuts down", "Offer ends", "Comments close", "Reconnect apps by", "Took effect". | 2–5 words. |
| `themes` | 0–3 thread slugs from `themes.json`. | Only when the change really is an example of the thread. `plan-shuffles` is the home for minor pricing-page edits. |
| `actions` | 1–3 concrete steps a reader can take. Shown as a checklist beside the article. | Start with a verb. Include exact emails, menu paths and dates. Leave out if there's nothing a reader can do. |

Still supported, unchanged: `faq`, `note`, `sources`, `seo_title`, `seo_desc`, `modified`.

### Writing the redline

The excerpt is the hook of every page, so it's worth getting right.

- **Use the company's exact words, never a paraphrase.** Text in the typewriter face is always the company's.
- **Best source: `reports/DATE-raw.md`.** Copy the `-` line into `before` and the matching `+` line into `after`, then trim both to the sentence (or clause) that changed, keeping 10–30 words of context. Mark it `"src": "raw"`. The build works out which words were struck and added, so don't add any markup.
- **New text only:** leave `before` empty (`""`). **Removed text only:** leave `after` empty.
- **When the change was found through research** (a help page, a Federal Register notice, an older version we didn't snapshot), use exact quotes that appear in your `what` text and mark it `"src": "quoted"`. If you only have the old wording as a fragment, quote just the fragment (`"before": "$100"`, `"after": "the amount paid to Oura in the prior twelve (12) months"`).
- **`label`** names where the words live: `"Terms of Use · Liability cap"`, `"Pricing · Grow, billed yearly"`.
- **`note`** (optional, one sentence) says what it means, the way a reviewer writes in the margin: "A fixed 30-day email promise becomes 'whatever the law requires.'"
- If several sentences changed, pick the 1–3 that matter most. The full diff is shown separately on the page.

### Writing `what`

`what` is still the full explanation. Two things make it read better on the page:

- Lead-ins our write-ups already use become subheadings automatically: `Change 1: …`, `What you can do: …`, `What stays the same: …`, `How it compares (checked Oct 17): …`, `What it replaces …`, `Other changes: …`.
- A sentence starting `Coverage (checked …):` is moved into a separate "Who else has reported it" box.
- To control the structure yourself, use real line breaks: a blank line starts a new paragraph, and a line starting `## ` is a subheading.

## Threads (`themes.json`)

Threads connect the same kind of change across companies; they're the main way readers go from one article to the next. Current threads: `forced-arbitration`, `ai-and-your-data`, `ads-and-tracking`, `shutdowns`, `price-creep`, `accept-or-else`, `not-our-problem`, `plan-shuffles`.

Add a new thread only when at least three changes fit it. Each needs a `title`, a one-line `dek`, and a two-paragraph `intro`.

## What the build makes from this

- **Change pages** open with the blackline, the summary, impact and a deadline stamp with a live countdown, then the structured write-up, a checklist, provenance, the raw diff, and three related changes (same service, same thread, same week).
- **Front page:** the most important change of the past week (highest impact, then most recent) leads; then Due soon, the latest report, the rest of the week, the seismograph, price leaders, threads, and "Your services".
- **Due soon** (`/due-soon/`) lists every `effective` date, with a calendar file per change and a subscribable `calendar.ics`.
- **Share images** (`docs/og/*.png`) show the headline and the first blackline. They're rendered with headless Chrome when one is available (set `QC_CHROME` to its path if it isn't on `PATH`); otherwise the site-wide image is used.
- **Search** (`/search.json`) covers every change, service and thread.

## Guardrails

- `tools/seo_snapshot.py` records every page's URL, title, description and structured data. Before a big change to the build: `python3 tools/seo_snapshot.py > /tmp/before.json`, rebuild, then `python3 tools/seo_snapshot.py --compare /tmp/before.json`. It exits with an error if any page disappeared.
- Never rename `headline`s of published changes: the article URL is built from it.
- Keep `impact` honest and `effective` dates sourced. The site's value is that readers can trust both.
