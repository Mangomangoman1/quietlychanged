# Distribution drafts, 2026-11-02 (Calm privacy policy and terms, Oct 13, 2026)

Pick: today's Calm deep dive. Mass audience (the app's subscribers), our own find, and nothing has been published about it. Coverage re-check (3 WebSearch passes, Nov 2 ~3:15 PM MT): only Calm's own pages, an AWS case study, a 2022-era Mozilla Calm-vs-Headspace comparison and an automated tracker; no news coverage. No reader deadline (in effect since Oct 13). Date-driven alternatives already pushed earlier: Pinterest Nov 12, Google Play Nov 17, FCC Nov 25, SSA Nov 29, Xero Dec 28; Oura Nov 4 and Toyota, Tubi already pitched.

Re-verified today against calm.com/privacy-policy and calm.com/terms (fetched Nov 2): "we may infer health-related characteristics from this information but will only process it consistent with the purpose for which it was provided" (Views and opinions); the HealthKit/Health Connect line still says "we do not infer any health-related characteristics"; the terms still carry "your emotions, well-being, stress levels, personal experiences, goals, or other wellness-related matters". Nothing to correct.

Strengthened the article (headline unchanged; commits 82f65c1, 562a18b, 6ffd9a7; Vercel dpl_EFWFhK2BaLfoawU5YYByokaRNy5u, live 200; SEO compare 182 to 182, 0 missing, 0 field changes, 1 JSON-LD change; IndexNow 200 at build and again after deploy):
- "How it compares": Headspace's privacy policy (effective Oct 28, 2026) has no feelings-inference line (it uses "infer" only in its AI definition) and says health info shared with coaches or therapists is treated "as protected health information under HIPAA where applicable".
- New finding: Calm Health (the employer / health-plan version) has its own privacy policy, also "last updated October 13, 2026" (terms Oct 14), with the identical "we may infer health-related characteristics" sentence, plus a "Health information" category (survey answers about "current mental or physical health status") and sponsor-enrollment data that "may include health information". Source: https://health.calm.com/calm-health-privacy-policy/ and https://health.calm.com/calm-health-terms/. Added as a paragraph, 2 FAQs (7 to 9 FAQs total counting the Headspace one) and 3 sources.

Dedup check: no earlier draft, outreach-log entry or send to Proof News or Annie Gilbertson. Not re-pitched: The Verge (Song, Weatherbed, Hawkins), Kashmir Hill, The Record, 404 Media, Ars, TechCrunch (Sarah P., Ivan Mehta), Jared Newman, Janko Roettgers. r/privacy got posts Oct 24 and Oct 29, so it's skipped today. Skipped on purpose: Mozilla's Nothing Personal (no named pitch contact; only an advice-column address and a generic press address), thera.news (clinician policy digest, weak fit), Hacker News.

Everything goes from quietlychangedbiz@gmail.com and the QuietlyChanged accounts, signed only "QuietlyChanged". Suggested timing: email now to Tue Nov 3 ~7–8 AM MT; Bluesky today ~4–5 PM MT or Tue ~8 AM; Reddit Tue Nov 3 ~8–10 AM MT after checking the rules in the signed-in browser (the box gets 403s from Reddit).

## 1. Email: Annie Gilbertson, Proof News (managing editor; led the April 2026 Talkspace investigation into therapy-app data and AI training)
To: annie@proofnews.org. Source: Proof News team page, "To contact Annie, email annie@proofnews.org." https://www.proofnews.org/team/. Her Talkspace piece: https://www.proofnews.org/womans-talkspace-therapy-app-sessions-exposed-in-court/ (Apr 28, 2026).
Subject: Calm's new privacy policy: it may now "infer health-related characteristics" from feelings users share (also in Calm Health)
Body:
Hi Annie,

Your Talkspace reporting on therapy-app data may connect to a smaller change at a much bigger consumer wellness app, and I haven't seen it covered anywhere.

On October 13, Calm updated both its privacy policy and its terms of service, with no announcement that I could find. The line that changed, in the privacy policy's "Views and opinions" section:

Dec 2024: "Some users also provide information about how they are feeling in connection with providing feedback or other messages to us, but we do not infer any health-related characteristics from this information and only process it consistent with the purpose for which it was provided."
Now: "...we may infer health-related characteristics from this information but will only process it consistent with the purpose for which it was provided."

Context that makes it more than a wording tweak:
- The new terms add an "Artificial Intelligence Features" section saying Calm and its third-party providers may process what users submit, including "your emotions, well-being, stress levels, personal experiences, goals, or other wellness-related matters," to "generate personalized Outputs and improve your experience." The same terms say Calm is "not a healthcare provider, mental health provider, therapist, counselor."
- The same inference sentence appears in the Calm Health privacy policy (the employer and health-plan version, last updated Oct 13), which also lists health information it collects, such as survey answers about "current mental or physical health status."
- The user-content license now covers AI outputs and was widened from "operating, marketing, and providing the Services" to include "developing, testing, validating, enhancing, and improving."
- One narrower point: the separate line about Apple Health and Google Health Connect data still says Calm does not infer health characteristics from it, so the inference carve-out is specifically about what people type.

For comparison, Headspace's policy (effective Oct 28) has no equivalent line. I'm not claiming Calm is doing anything beyond what its policy now allows; the point is that the promise was removed and AI inputs were added in the same update.

Sources, all primary:
Calm privacy policy (Oct 13, 2026): https://www.calm.com/privacy-policy
Previous version (Dec 12, 2024), Internet Archive: https://web.archive.org/web/20261011203550/https://www.calm.com/privacy-policy
Calm terms (Oct 13, 2026): https://www.calm.com/terms
Calm Health privacy policy: https://health.calm.com/calm-health-privacy-policy/
Our write-up with the full before and after lines: https://quietlychanged.com/changes/2026-11-02-calm-calm-says-it-may-now-infer-health-traits-from-feelings-you-share-and-adds/

QuietlyChanged tracks changes to the terms, privacy policies and prices of consumer services.

QuietlyChanged

## 2. Bluesky (quietlychanged.bsky.social): image post plus a self-reply with links
Image: social/2026-11-02/distribution/01-calm-infer-before-after.png (1024x576, the before/after card; same file as deepdive/02)
Alt text: Calm's privacy policy, "Views and opinions" section, before and after. December 12, 2024: "Some users also provide information about how they are feeling in connection with providing feedback or other messages to us, but we do not infer any health-related characteristics from this information and only process it consistent with the purpose for which it was provided." October 13, 2026: "...we may infer health-related characteristics from this information but will only process it consistent with the purpose for which it was provided."
Post (about 260 chars):
Calm updated its privacy policy on Oct 13 and changed one sentence.

If you tell Calm how you're feeling in a message, it used to say "we do not infer any health-related characteristics."

Now it says "we may infer health-related characteristics."
Self-reply (about 250 chars):
The new AI terms also cover your "emotions, well-being, stress levels." Calm Health's policy has the same line. Full before/after: https://quietlychanged.com/changes/2026-11-02-calm-calm-says-it-may-now-infer-health-traits-from-feelings-you-share-and-adds/
Source: https://www.calm.com/privacy-policy
(Check the length in the composer; if over 300 graphemes, cut "Calm Health's policy has the same line.")

## 3. Reddit r/Meditation (u/QuietlyChanged): text post, primary-source links only, NO quietlychanged.com link, no image
Rules: r/Meditation bans self-promotion, so link only calm.com and the Internet Archive. I could not read the subreddit rules from the box (403). Before posting, check the rules and flair in the signed-in browser; if text posts about apps' policies are not allowed, skip it. Do not also post in r/Calm-type communities or r/privacy today.
Title: Heads up for Calm users: its Oct 13 privacy policy now says it "may infer health-related characteristics" from feelings you share in messages
Body:
Calm updated its privacy policy and terms of service on October 13, 2026. Two things Calm users may want to know:

1. In the privacy policy's "Views and opinions" section, the old version (Dec 2024) said that when users share how they're feeling in feedback or other messages, "we do not infer any health-related characteristics from this information." The new one says "we may infer health-related characteristics from this information but will only process it consistent with the purpose for which it was provided." The line about Apple Health and Google Health Connect data still says Calm does not infer health characteristics from it.
2. The new terms add an "Artificial Intelligence Features" section. It says some AI features may take information about "your emotions, well-being, stress levels, personal experiences, goals, or other wellness-related matters," and that Calm and its third-party providers may process it to "generate personalized Outputs and improve your experience." The same terms say you "do not own or acquire any permanent rights in Paid Content," including downloads, once your subscription ends.

If you'd rather not have it: you can opt out of ad "sales" and "sharing" at calm.com/optout, leave feelings out of feedback and support messages, and new users can opt out of arbitration by emailing notices@calm.com within 30 days.

Sources: https://www.calm.com/privacy-policy, https://www.calm.com/terms, and the old privacy policy: https://web.archive.org/web/20261011203550/https://www.calm.com/privacy-policy
