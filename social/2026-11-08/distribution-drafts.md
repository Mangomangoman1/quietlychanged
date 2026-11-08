# Distribution drafts, 2026-11-08 (Booking.com Dec 10 US terms: We Price Match pays Wallet Credits instead of a refund)

**Nothing here has been sent or posted.** Emails go from quietlychangedbiz@gmail.com, signed only "QuietlyChanged". Bluesky and Reddit need Samuel's OK.

## Pick and why
- **Booking.com US Customer Terms "Updated 10 December 2026"** (PDF linked from the live terms page, which still says "Updated August 25, 2025"). Big consumer brand, money angle, effective in 32 days, and a primary-source diff nobody has published. Article: https://quietlychanged.com/changes/2026-11-08-booking-com-price-match-will-pay-wallet-credits-not-a-refund/
- Do NOT say Dec 10 adds forced arbitration: Section A20 is already in the Aug 25, 2025 terms.

## Primary re-check (Nov 8, ~3:00 PM MT)
- PDF (research/2026-11-08-booking/Customer_Terms_of_Service_US_December_2026.pdf; live at https://q-xx.bstatic.com/static/docs/tos-hww/Customer_Terms_of_Service_US_December_2026.pdf): "we promise you Wallet Credits for the difference" (line ~971), "claim after stay Wallet credits of the price difference" (~1010), Guest verification with "selfie" check (~1041), "dependent on the amounts actually received by Us and recoverable from the Service Provider under their policy" (~197). All confirmed.
- Live https://www.booking.com/content/terms.html (curl with browser UA): still "Updated August 25, 2025", "we promise to refund the difference" (8 hits), "5 bookings within 2 years", and links the December PDF. Confirmed.
- Genius page and the We Price Match help page (https://www.booking.com/general.html?tmpl=doc%2Frate_guarantee: "You can claim a refund for the difference") checked via search index.

## New finding that changes the framing (added to the article, commit 83bc7bd5)
- In January 2026 a r/Bookingcom user complained that an approved price match was paid as Wallet credit. A reply from the u/bookingcom account (Jan 2, 2026) said: "For We Price Match claims, compensation is provided as travel credit to your Booking.com Wallet... Once added as wallet credit, it cannot be converted back to a refund to the original payment method." (https://www.reddit.com/r/Bookingcom/comments/1pysl65/prive_match_guarantee_not_being_paid_out/ , read via search snapshot; Reddit blocks the box.) So Dec 10 may **codify existing practice**; the written promise (and the help page) said refund. That is one report; the pitches say so.
- Expedia comparison (sourced): Expedia's page https://www.expedia.com/price-guarantee-claim says the Hotel Price Guarantee "will end on July 28, 2026" and paid "the difference in OneKeyCash"; AwardWallet (https://awardwallet.com/news/hotels/one-key-expedia-changes-2026/) and Upgraded Points (https://upgradedpoints.com/news/one-key-rewards-changes-2026/) report Expedia and Hotels.com removed it with no replacement.

## Article changes (shipped)
Added "How this compares: practice today and Expedia" section, 1 FAQ, 3 sources, and a coverage-line sentence. Commit 83bc7bd5, pushed. SEO compare 206 to 206, 0 missing, 0 field changes, 1 JSON-LD change. IndexNow 200 (build, and for the article after). Vercel manual deploy (site.b64 + vercel.json): dpl_5uQpzUsHrxJMinrEARMXXqyD6cFw.

## Coverage check (Nov 8, ~3:15 PM MT; 6 WebSearch queries incl. "Wallet Credits" price match, Dec 10 terms, Genius levels, selfie verification, Expedia comparison)
- **No news story on the Dec 10 US terms, the price-match wording, the Genius number removal, or the selfie rule.** Found only: the PDF itself, Booking.com's help/terms pages, ConductAtlas (existing terms), the Jan 2026 Reddit thread (practice, not the new terms), explainers noting price match payouts often arrive as Wallet credit (plot.travel, Gadabout), and Expedia's price-guarantee end (AwardWallet, Upgraded Points, Arbitrica, HotelHops).
- Safe wording for pitches: "I haven't found coverage of the December terms." Don't claim nobody has noted credit payouts.

## Dedup / cap
- Sent from quietlychangedbiz@gmail.com in the last 2 days: only the two Nov 6 Wells Fargo follow-up/pitch emails (Kate Berry, Katie Kelton). **0 sent on Nov 8**, so 3 fit under the cap of 5.
- None of these three is in growth-log.md or memory as pitched; no one has been pitched on Booking.com.

Suggested timing: Mon Nov 9, 7–9 AM MT.

---

## 1. Email: Sean O'Neill, Skift (Senior Hospitality Editor; covers hotels and OTAs, e.g. "Why We've Been Looking at the Hotel Brands vs. OTAs War All Wrong," Nov 3, 2026)
To: so@skift.com
Email source: Skift team page, https://skift.com/team/ (listed under his bio).
Subject: Booking.com's Dec 10 US terms: price match pays Wallet Credits, Genius thresholds leave the contract

Body:
Hi Sean,

Booking.com has posted a new US Customer Terms of Service dated December 10, 2026 (PDF linked from booking.com/content/terms.html, which still shows the August 25, 2025 version). I compared the two and haven't found any coverage of the changes:

- We Price Match: "we promise to refund the difference" becomes "we promise you Wallet Credits for the difference." The after-stay step changes from "claim an after-stay refund" to "claim after stay Wallet credits." The terms don't say whether those are Travel Credits ("can't cash out") or Cash Credits. Booking.com can still amend the reservation price "if possible."
- Context: a Booking.com account told a customer on r/Bookingcom in January that price-match compensation is already paid as Wallet credit, even though the live terms and help page say refund. So this may codify practice. For comparison, Expedia and Hotels.com ended their Hotel Price Guarantee on July 28.
- Genius: the Level 2 (5 bookings in 2 years) and Level 3 (15) thresholds are removed from the terms and replaced with a pointer to the Genius page, which still lists them. "There are no membership fees" is also dropped.
- New mandatory identity verification for some bookings, including a "selfie" check, with a right to cancel and refund if it fails.
- New refund language: refunds Booking.com organizes "are dependent on the amounts actually received by Us and recoverable from the Service Provider."

The arbitration clause is not new in this version (it's already in the August 2025 terms), so I'm not treating that as the story.

Side-by-side with exact quotes: https://quietlychanged.com/changes/2026-11-08-booking-com-price-match-will-pay-wallet-credits-not-a-refund/
Primary sources: https://www.booking.com/content/terms.html ; https://q-xx.bstatic.com/static/docs/tos-hww/Customer_Terms_of_Service_US_December_2026.pdf

Happy to send the raw text diff.

QuietlyChanged
quietlychanged.com

---

## 2. Email: Linda Fox, PhocusWire (senior reporter; covers online travel and OTA marketing)
To: lfox@phocuswire.com
Email source: PhocusWire contact page, https://www.phocuswire.com/Contact-Us ("Linda Fox (senior reporter): lfox@phocuswire.com"). Her Booking/Expedia beat is from her PhocusWire author archive, https://www.phocuswire.com/Linda-Fox (via search; the page 403s the box).
Subject: Booking.com's Dec 10 US terms: price-match promise moves from refund to Wallet Credits

Body:
Hi Linda,

A quick one for your OTA coverage. Booking.com's US Customer Terms of Service dated December 10, 2026 (PDF linked from its live terms page, which still shows the August 25, 2025 version) change the We Price Match promise.

Before: "we promise to refund the difference." After: "we promise you Wallet Credits for the difference," and the after-stay claim step now says "claim after stay Wallet credits of the price difference." It can still "amend the reservation price (if possible)." The clause doesn't say Travel Credits or Cash Credits; per the same document, Travel Credits "can't 'cash out'."

A Booking.com account told a customer on r/Bookingcom in January that price-match compensation is already provided as Wallet credit, so the change may formalize practice. Booking.com's help page still says "You can claim a refund for the difference." Expedia and Hotels.com ended their Hotel Price Guarantee on July 28, which leaves Booking.com as one of the few big OTAs still price matching after booking.

Also in the document: the Genius Level 2 and 3 thresholds (5 and 15 bookings in 2 years) are removed from the contract; a new guest-verification clause includes a "selfie" check; and refunds Booking.com organizes depend on "amounts actually received by Us and recoverable from the Service Provider."

I haven't found coverage of the December terms. Quotes and links: https://quietlychanged.com/changes/2026-11-08-booking-com-price-match-will-pay-wallet-credits-not-a-refund/

QuietlyChanged
quietlychanged.com

---

## 3. Email: Christopher Elliott, Elliott Advocacy (consumer travel advocate; writes on booking-site refund disputes, e.g. "When a booking site keeps your refund: what to do")
To: chris@elliott.org
Email source: https://www.elliott.org/contact/ ("Or reach him directly Email chris@elliott.org"). The same page says the separate tips address (elliottdotorg@protonmail.com) is not for PR pitches, so this goes to his direct address, framed as a reader-useful tip, not PR.
Subject: Booking.com's new US terms turn price-match refunds into Wallet Credits (Dec 10)

Body:
Hi Chris,

In case it's useful for readers: Booking.com's US terms dated December 10, 2026 change its We Price Match promise. Today's live terms (Aug 25, 2025) say "we promise to refund the difference." The new PDF says "we promise you Wallet Credits for the difference," and the after-stay claim becomes "after stay Wallet credits." The wording doesn't say which kind of credit; the same document says Travel Credits "can't 'cash out'."

Two things a traveler would want to know:
- A Booking.com account told a customer on r/Bookingcom in January that price-match compensation is already paid as Wallet credit that "cannot be converted back to a refund," even though the terms and help page say refund. So claims filed now may not pay cash either.
- The new terms add a guest "selfie" identity check for some bookings (with cancel-and-refund if it fails) and say refunds Booking.com organizes "are dependent on the amounts actually received by Us and recoverable from the Service Provider."

I haven't found news coverage of the December terms. Exact quotes and links: https://quietlychanged.com/changes/2026-11-08-booking-com-price-match-will-pay-wallet-credits-not-a-refund/

QuietlyChanged
quietlychanged.com

---

## 4. Bluesky (needs Samuel's OK) — text post + self-reply
Post (≤300 chars):
Booking.com's new US terms (effective Dec 10) change its price match promise:

Now: "we promise to refund the difference"
Dec 10: "we promise you Wallet Credits for the difference"

Same terms also drop the Genius 5/15-booking numbers and add a "selfie" ID check for some bookings.

Self-reply:
Side-by-side with exact quotes and the Booking.com PDF link: https://quietlychanged.com/changes/2026-11-08-booking-com-price-match-will-pay-wallet-credits-not-a-refund/ (Booking.com staff told a customer in January that price-match payouts already go to the Wallet, so this may just write down current practice.)

---

## 5. Reddit: r/Bookingcom (needs Samuel's OK). Rules unread because Reddit 403s the box; check them (and the self-promo rule) in the signed-in browser first. Primary links only, no QuietlyChanged link.
Title: Booking.com's new US terms (Dec 10) say price match pays "Wallet Credits," not a refund

Body:
Booking.com has a US Customer Terms of Service PDF dated 10 December 2026, linked from the live terms page (which still says "Updated August 25, 2025"). Changes I noticed in the We Price Match section:

- Now: "we promise to refund the difference." Dec 10: "we promise you Wallet Credits for the difference."
- After claim validation they will still "amend the reservation price (if possible)"; otherwise the claim step changes from "an after-stay refund" to "after stay Wallet credits."
- It doesn't say Travel Credits or Cash Credits. In the same document Travel Credits "can't 'cash out'"; Cash Credits can be cashed out.

Other changes in the same PDF: the Genius Level 2 and 3 numbers (5 and 15 bookings in 2 years) are no longer in the terms (the Genius page still lists them), a guest verification section mentions a "selfie" check, and refunds Booking.com organizes "are dependent on the amounts actually received by Us and recoverable from the Service Provider."

Some of you have already reported price-match payouts as Wallet credit (e.g. https://www.reddit.com/r/Bookingcom/comments/1pysl65/prive_match_guarantee_not_being_paid_out/), so this may just formalize it. Have you been paid in credit or to your card?

Sources:
- Dec 10 PDF: https://q-xx.bstatic.com/static/docs/tos-hww/Customer_Terms_of_Service_US_December_2026.pdf
- Current US terms: https://www.booking.com/content/terms.html
- Genius page: https://www.booking.com/genius.html

---

## Skipped
HN (Samuel's rule); TPG/NerdWallet/Consumer Reports (no named reporter emails verified); Morgan Hines (PhocusWire; reported as no longer there per search, beat unclear); r/travel and r/privacy (off-topic/used).
