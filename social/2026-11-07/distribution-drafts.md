# Distribution drafts, 2026-11-07 (BeReal Nov 3 privacy policy: 5-year inactive-account retention + new "advertising measurement partners" incl. store-visit measurement)

**Nothing here has been sent or posted.** Emails go from quietlychangedbiz@gmail.com, signed only "QuietlyChanged". Bluesky and Reddit need Samuel's OK.

## Pick and why
- **BeReal (Nov 3 privacy policy)** is the only candidate today with **no news coverage**: two WebSearch passes (~3:05 and ~3:15 PM MT, Nov 7) found only BeReal's own page and automated trackers (TermsWatch / Open Terms Archive, ConductAtlas, TOSTracker). It's our own primary-source diff. No reader deadline (already in effect), but the store-visit angle in a Gen-Z app whose minimum age is 13 is a real ad-tech/privacy story.
- **JetBlue bag fees (Nov 3): rejected for pitching.** Widely covered: AP (Nov 4), CNBC (Nov 3), The Points Guy (Nov 3), PointsFrog. The peak calendar, including all-December-peak, is printed in TPG's piece too. It stays an X/viral item (social/2026-11-07/deepdive/). Side note for the site: AP and TPG say the old off-peak first-bag fee was "$39"; JetBlue's own Oct 12 page (Wayback) and CNBC say $45. Our article already notes this.
- **Starlink dynamic pricing: rejected.** Not our find. PCMag (2 pieces), Techdirt (Nov 6) and Notebookcheck already cover it.
- Already pitched, so excluded: Wells Fargo, Smule, Pinterest, Stripe, Calm, Tubi, Toyota, Canva, SSA and the others in growth-log.md.

## Primary re-check (Nov 7, ~3:00 PM MT)
- https://bereal.com/privacy (curl 200): "Last updated: November 3, 2026". Live text confirmed: "five (5) years of continuous inactivity"; "Before your account is deleted, BeReal will send you a prior notice via text message (SMS)"; the new Section 3 "Advertising measurement partners" paragraph; the Section 2 row with "where you agree, measuring whether advertising campaigns result in visits to physical locations" and "provided to us in aggregated form". "To minimize data retention" appears 0 times live and is present in the June 30 text (research/2026-11-07-bereal/privacy-2026-09-30.txt). "minor" appears only in the intro and the GPS-on-posts defaults, with nothing minor-specific in ad measurement.
- Before: https://web.archive.org/web/20260930012030/https://bereal.com/privacy (June 30, 2026 text; 200).
- **New finding:** both "list of our partners" links (Ad Partners and the new measurement partners) point to https://help.bereal.com/hc/en-us/articles/19494197955101-Ad-Partners. It lists 93 distinct companies (Mobile Fuse appears twice), all ad exchanges, networks and DSPs. None is labeled a measurement partner, and none of AppsFlyer, Adjust, Branch, Kochava or Singular, or any store-visit firm, is listed.

## Article changes (shipped)
- Added "Who the 'measurement partners' are" (the partner-list finding) and "How five years compares" (Google's inactive-account policy is 2 years, https://support.google.com/accounts/answer/12418290; the removed "To minimize data retention" phrase). Added 2 FAQs and 2 sources, and updated the coverage line.
- Commit 8fe10ff. Built with build_site.py (IndexNow 200, 63 URLs). Vercel **dpl_72f43ZaEzgcxq8GUsBDPHWn7WTBh** (manual, site.b64 + vercel.json), READY and aliased to quietlychanged.com. Live 200 (Googlebot UA) with the new text. /, sitemap, services.html and /services/bereal/ return 200; /services/zoom/ still 301s to /services.html#zoom. SEO compare: 202 to 202 pages, 0 missing, 0 field changes, 1 JSON-LD change (this article). IndexNow after deploy: 200 (article + /services/bereal/).
- Article: https://quietlychanged.com/changes/2026-11-07-bereal-inactive-accounts-kept-5-years-and-ad-partners-can-now-measure-store-vis/

## Dedup / cap
- 0 emails sent from quietlychangedbiz@gmail.com on Nov 7 (Gmail sent search: last sends were Nov 6 at 3:11 PM MT). 3 pitches below leaves room for 2 more today.
- None of the three has been pitched on BeReal. Suzanne Smalley got the SSA tip Oct 29/30 via The Record's tips address, a different story more than a week ago. No overlap with Wendy Davis or Laurie Sullivan (MediaPost, pitched Nov 4); Colin Kirkland is a different MediaPost reporter (social media beat).

Suggested timing: Mon Nov 9, 7–9 AM MT (trade desks are quiet on weekends). Sending Saturday afternoon is fine too.

---

## 1. Email: Allison Schiff, AdExchanger (editor-in-chief; covers mobile, measurement, privacy, app economy; writes the weekly data-privacy roundup)
To: allison@adexchanger.com
Email source: her byline sign-off, "feel free to drop me a line at allison@adexchanger.com", on https://www.adexchanger.com/data-privacy-roundup/ai-is-moving-fast-the-law-not-so-much/ (Apr 1, 2026). Also listed on https://www.adexchanger.com/contact-form/.
Subject: BeReal adds store-visit "measurement partners" to its privacy policy, but the partner list it links names none

Body:
Hi Allison,

Here's a small app-economy privacy item that might fit the roundup. BeReal quietly updated its privacy policy on Nov 3 (bereal.com/privacy, "Last updated: November 3, 2026"; the previous version was dated June 30). I haven't found any press coverage, only automated policy trackers.

What's new:

- A new third-party category in Section 3, "Advertising measurement partners": "To measure advertising performance, including app-install attribution and, where you agree, visits to physical locations following advertising exposure, we may share mobile advertising IDs, device identifiers and advertising-exposure data with measurement partners."
- The ad-measurement row in Section 2 now adds Geolocation Data and advertising-exposure data. It says "Visit and physical-location outcomes are derived by our measurement partners and provided to us in aggregated form." The legal basis for the whole row is "Your consent, where required by applicable law; otherwise, our legitimate interest." So "where you agree" applies to the store-visit part only.
- The "list of our partners" link for measurement partners goes to the same Help Center page used for ad partners (https://help.bereal.com/hc/en-us/articles/19494197955101-Ad-Partners). Today it lists 93 ad companies (Google Ad Manager, Meta, Amazon, AppLovin, The Trade Desk, Vistar Media and others). None is marked as a measurement partner, and no attribution or store-visit firm (AppsFlyer, Adjust, Branch, Kochava, Singular) appears.
- Separately, inactive accounts are now kept 5 years before deletion, up from 3 years in the US and 2 in Europe and elsewhere. The phrase "To minimize data retention" was removed.

The documents don't say who the measurement partners are, whether "where you agree" is its own in-app toggle (the policy's description of "Modify my consents" wasn't updated), or what location signal partners use to decide a visit happened.

Side-by-side with all quotes: https://quietlychanged.com/changes/2026-11-07-bereal-inactive-accounts-kept-5-years-and-ad-partners-can-now-measure-store-vis/
Primary sources: current policy https://bereal.com/privacy ; June 30 version https://web.archive.org/web/20260930012030/https://bereal.com/privacy

Happy to send the raw text diff.

QuietlyChanged
quietlychanged.com

---

## 2. Email: Colin Kirkland, MediaPost (Reporter, Social Media coverage; wrote "BeReal Competes With TikTok, Launches Ads", Apr 10, 2025)
To: colin@mediapost.com
Email source: MediaPost masthead, https://www.mediapost.com/publications/masthead/ ("Colin Kirkland, Reporter, Social Media & Web3 coverage"; the address is Cloudflare-obfuscated on the page and decoded from it). Article: https://www.mediapost.com/publications/article/404974/bereal-competes-with-tiktok-launches-ads.html
Subject: BeReal's ad business adds store-visit measurement (Nov 3 privacy policy)

Body:
Hi Colin,

You covered BeReal's US ad launch last year, so here's a follow-up that hasn't been reported. BeReal's privacy policy was updated on Nov 3, 2026 (bereal.com/privacy; the previous version was June 30). It now lets BeReal tie ads to store visits.

- New in Section 3: "Advertising measurement partners: To measure advertising performance, including app-install attribution and, where you agree, visits to physical locations following advertising exposure, we may share mobile advertising IDs, device identifiers and advertising-exposure data with measurement partners."
- Section 2 adds Geolocation Data to ad measurement and says visit outcomes "are derived by our measurement partners and provided to us in aggregated form."
- The partner list the policy links to (https://help.bereal.com/hc/en-us/articles/19494197955101-Ad-Partners) is the existing Ad Partners page: 93 ad companies, none marked as a measurement partner.
- Retention: inactive accounts are now kept 5 years, up from 3 in the US and 2 in Europe. BeReal points to its Memories archive, and the phrase "To minimize data retention" is gone.

For advertisers it's a step toward closed-loop, foot-traffic measurement on BeReal. For users, the policy doesn't say whether "where you agree" means a separate prompt.

Full before/after: https://quietlychanged.com/changes/2026-11-07-bereal-inactive-accounts-kept-5-years-and-ad-partners-can-now-measure-store-vis/
Old version (June 30): https://web.archive.org/web/20260930012030/https://bereal.com/privacy

QuietlyChanged
quietlychanged.com

---

## 3. Email: Suzanne Smalley, The Record from Recorded Future News (covers digital privacy, surveillance technologies, cybersecurity policy)
To: suzanne.smalley@therecord.media
Email source: her tip line at the end of https://therecord.media/kroger-facial-recognition-lawmakers-concerns ("send an email to suzanne.smalley@therecord.media"). Beat from https://therecord.media/author/suzanne-smalley.
Subject: BeReal now shares ad IDs for store-visit tracking and keeps dormant accounts 5 years (Nov 3 policy, no coverage yet)

Body:
Hi Suzanne,

BeReal, the Paris-based photo app (minimum age 13), changed its privacy policy on Nov 3, 2026. I haven't seen it reported.

1. Location-based ad measurement. A new "Advertising measurement partners" category: "we may share mobile advertising IDs, device identifiers and advertising-exposure data with measurement partners," including, "where you agree, visits to physical locations following advertising exposure." BeReal says the visit results come back to it "in aggregated form," but the partners themselves get device-level IDs. The policy has teen-specific defaults for GPS on posts, but nothing teen-specific for this ad-measurement sharing. The partner list it links names 93 ad companies and none is marked as a measurement partner (https://help.bereal.com/hc/en-us/articles/19494197955101-Ad-Partners).

2. Longer retention. Inactive accounts used to face deletion after 3 years in the US and 2 years in Europe. Now it's 5 years everywhere. The old text began "To minimize data retention," and that phrase is gone. For comparison, Google can delete an inactive personal account after 2 years. BeReal SAS is the controller, so the CNIL would be the lead EU regulator.

Primary sources:
- Current policy: https://bereal.com/privacy
- June 30 version: https://web.archive.org/web/20260930012030/https://bereal.com/privacy
- Our side-by-side with every quote: https://quietlychanged.com/changes/2026-11-07-bereal-inactive-accounts-kept-5-years-and-ad-partners-can-now-measure-store-vis/

QuietlyChanged
quietlychanged.com

---

## 4. Bluesky (needs Samuel's OK) — text post + self-reply
Post (278 chars):
BeReal updated its privacy policy on Nov 3. Two changes:

• Unused accounts are now kept 5 years before deletion (was 2 years in Europe, 3 in the US)
• New "advertising measurement partners" get your ad ID, including to measure store visits after you see an ad "where you agree"

Self-reply:
Old vs new wording side by side, plus how to limit it (BeReal → Settings → Privacy → "Modify my consents", and reset your phone's ad ID): https://quietlychanged.com/changes/2026-11-07-bereal-inactive-accounts-kept-5-years-and-ad-partners-can-now-measure-store-vis/

---

## 5. Reddit: r/bereal_app (needs Samuel's OK; ~10K members, BeReal staff participate). Rules unread because the box gets a 403 from Reddit, so check them in the signed-in browser first. Primary links only, no QuietlyChanged link.
Title: PSA: BeReal's privacy policy changed Nov 3. Inactive accounts are now kept 5 years, and ad IDs go to new "measurement partners" (incl. store visits)

Body:
BeReal's privacy policy now says "Last updated: November 3, 2026" (it was June 30 before). Two changes worth knowing about:

**1. Inactive accounts are kept much longer.** Old: an account "may be deleted after three (3) years of continuous inactivity" in the US, or two years in Europe and everywhere else. New: "five (5) years of continuous inactivity," everywhere. The reason given is Memories, "so that you can find it again whenever you come back to the App." The deletion warning only goes by SMS to the phone number on your account, so keep that number current, or delete old posts or your account if you don't want them kept.

**2. New "Advertising measurement partners."** Quote: "To measure advertising performance, including app-install attribution and, where you agree, visits to physical locations following advertising exposure, we may share mobile advertising IDs, device identifiers and advertising-exposure data with measurement partners."

To limit it:
- In BeReal: Settings → Privacy → "Modify my consents"
- On your phone, reset or delete your advertising ID (iOS: Settings → Privacy & Security → Tracking; Android: Settings → Privacy → Ads)

Sources:
- Current policy: https://bereal.com/privacy
- June 30 version (Wayback): https://web.archive.org/web/20260930012030/https://bereal.com/privacy
- Partner list the policy links to: https://help.bereal.com/hc/en-us/articles/19494197955101-Ad-Partners

---

## Skipped
- HN (Samuel's rule). r/privacy (posted Oct 24, drafted Oct 29; keep it for a bigger story). Digiday's Krystal Scanlon (covers BeReal ads, but I found no published email). TechCrunch (no public email found for the relevant reporter). Wendy Davis and Laurie Sullivan (pitched Nov 4 on other stories; too soon). JetBlue and Starlink pitches (already widely covered).
