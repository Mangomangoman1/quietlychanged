# Distribution drafts, 2026-11-04 (Pinterest Nov 12 terms and privacy policy: one arbitrator for mass claims, a new 30-day opt-out, ads to connected TVs by household)

Pick: the Oct 20 Pinterest find. It has the nearest consumer date (new terms take effect Nov 12, 8 days out; the opt-out window runs Nov 12 to Dec 12), reaches a very large audience, and still has no consumer-side coverage. Today's deep dive did not run, and the other fresh items are weaker: the Nov 3 SSA SORN modification (60-0058, Do Not Pay routine use, comments Dec 3) is impact 1 and follows the Client Data System story that was pitched Oct 30; Stripe was pitched to MediaPost and Payments Dive earlier today.

Coverage re-check (WebSearch, Nov 4 ~3:10 PM MT): nothing on the user arbitration rewrite, the 30-day opt-out or the household/connected-TV language except our own article and guide. Pinterest's own pages, PPC Land (Sep 12, advertiser side only: ad guidelines, Ad Data Terms), P&C Marketing (advertiser side), PrivacyForge (Ad Data Terms for EU/UK stores) and MediaPost's Laurie Sullivan (ad products and CTV launches, never the user terms) are the only Pinterest-terms coverage.

Re-verified against the primary sources (fetched Nov 4): policy.pinterest.com/terms-of-service-preview still says "You may opt out of this Section 11 within 30 days of first becoming subject to it by emailing litigation@pinterest.com with your name, account email, and a statement that you're opting out", "all of those Claims will be consolidated into one arbitration before one arbitrator with a single set of filing and administrative fees" (25+ similar claims within 90 days or coordinated counsel; JAMS Mass Arbitration Procedures), and "supersedes and amends any prior arbitration agreement ... including as to Claims that arose before"; the privacy preview still has "when you're streaming a show on your connected TV", "associating devices that may relate to the same person or household" and "Your connected TV may allow you to manage or limit the use of data for advertising", with "Effective date: November 12, 2026". The current terms page still carries the Nov 12 banner and the old AAA batching text. Nothing to correct.

Strengthened (commit ff21b02, Vercel dpl_FEqvUrqBVYN7AturhKDDViYYaQ2y, manual deploy of site.b64 + vercel.json; live 200 with the new text; /services/zoom/ still 301; SEO compare 187 to 187, 0 missing, 0 field changes, 3 JSON-LD changes; IndexNow 200 at build and after deploy): added a sourced Amazon comparison and 5 FAQs (opt-out, window, mass claims, Amazon comparison, connected TV) plus 2 sources. Amazon's Conditions of Use (updated Aug 14, 2026) use JAMS batches for 25+ demands within six months, with larger batches above 500 and 2,500, after a 60-day pre-filing wait, and PPC Land reports no consumer opt-out. Amazon's own page returns a captcha to the box, so the comparison is attributed to PPC Land's reading (https://ppc.land/amazon-forces-shoppers-into-arbitration-five-years-after-dropping-it/) and The Verge (https://www.theverge.com/tech/980752/amazon-class-action-arbitration-terms-and-conditions).

Article: https://quietlychanged.com/changes/2026-10-20-pinterest-nov-12-terms-mass-claims-go-to-one-arbitrator-ads-follow-you-to-your/
Guide that covers the opt-out with 10 other companies: https://quietlychanged.com/guides/how-to-opt-out-of-forced-arbitration-2026/

Dedup check: Pinterest was pitched once before, to Sarah Perez at TechCrunch on Oct 20 (plus X reply, Bluesky and HN that day; r/Pinterest skipped). Neither Laurie Sullivan nor Luis Rijo (PPC Land) has been contacted by QuietlyChanged. Not re-pitched: Sarah Perez, Proof News, Jared Newman, Janko Roettgers, Verge, NYT, MediaPost's Wendy Davis (Stripe, sent today) and Payments Dive. Skipped on purpose: The Verge's Terrence O'Brien (wrote the Amazon arbitration piece, but no public email found), r/Pinterest (marketer sub, bans self-promotion), r/privacy (posted Oct 24 and Oct 29), HN.

Everything goes from quietlychangedbiz@gmail.com and the QuietlyChanged accounts, signed only "QuietlyChanged". Suggested timing: emails now through Thu Nov 5 ~7-9 AM MT (the story is most useful before Nov 12). Note: Laurie Sullivan is at MediaPost, where Wendy Davis got the Stripe pitch today; they are different reporters on different beats, but if Samuel would rather not hit one outlet twice in a day, send hers Thu Nov 5 morning.

## 1. Email: Laurie Sullivan, MediaPost (Senior Writer, Search, Performance & Data Marketing coverage; wrote "Pinterest Brings Audience Data To CTV Through tvScientific," Apr 27, 2026, https://www.mediapost.com/publications/article/414613/pinterest-brings-audience-data-to-ctv-through-tvsc.html)
To: lauriesullivan@gmail.com. Source: the MediaPost masthead, "Laurie Sullivan, Senior Writer, Search, Performance & Data Marketing coverage", address shown there (decoded from the page's protected-email link): https://www.mediapost.com/publications/masthead/
Subject: Pinterest's Nov 12 privacy policy adds connected-TV ads and household device matching for users
Body:
Hi Laurie,

You covered Pinterest bringing its audience data to connected TV through tvScientific, so this may be useful from the user side: the privacy policy Pinterest takes live on November 12 now describes that targeting in plain language for its users. I haven't found coverage of it; PPC Land's September piece covers the advertiser documents only.

Preview policy, effective November 12, 2026 (https://policy.pinterest.com/privacy-policy-preview), quoted:
- Ad example: "we may show you ads for other outdoor products on Pinterest, or, for example, depending on your location, when you're streaming a show on your connected TV."
- Targeting now includes "associating devices that may relate to the same person or household."
- It also says Pinterest may receive information "from partners that help us power the ads we show to you on and off Pinterest" and, "Depending on where you live," "from data providers," and that "Your connected TV may allow you to manage or limit the use of data for advertising."
- "Voice transcripts" join the activity used "to make inferences about you and your preferences."

The same update rewrites the terms (https://policy.pinterest.com/terms-of-service-preview). Pinterest's help page says "Your Pinterest experience won't change," and that using Pinterest after November 12 counts as acceptance. Section 11 moves arbitration from the AAA to JAMS and says 25 or more similar claims within 90 days, or claims brought through coordinated counsel, "will be consolidated into one arbitration before one arbitrator" with a single set of fees. It also adds the first opt-out: "within 30 days of first becoming subject to it by emailing litigation@pinterest.com," which for existing users means November 12 to December 12. Amazon's August arbitration update uses a similar batching idea, without an opt-out according to PPC Land's reading.

Our write-up has the before and after text, the opt-out steps and the sources: https://quietlychanged.com/changes/2026-10-20-pinterest-nov-12-terms-mass-claims-go-to-one-arbitrator-ads-follow-you-to-your/

QuietlyChanged tracks changes to the terms, privacy policies and prices of consumer services.

QuietlyChanged

## 2. Email: Luis Rijo, PPC Land (founder and writer; wrote the Sep 12 Pinterest advertiser-terms piece and the Aug 14 Amazon arbitration piece)
To: luis@ppc.land. Source: his byline on ppc.land articles, "Tips and corrections: luis@ppc.land", e.g. https://ppc.land/amazon-forces-shoppers-into-arbitration-five-years-after-dropping-it/
Subject: Tip: Pinterest's Nov 12 user terms copy the Amazon batching idea, with an opt-out
Body:
Hi Luis,

You covered Pinterest's advertiser-side changes on Sep 12 and Amazon's August arbitration reversal, so here's the piece between them that I haven't seen anywhere: what Pinterest's November 12 Terms of Service do for ordinary users.

Section 11 (https://policy.pinterest.com/terms-of-service-preview) is rewritten from scratch:
- Arbitration moves from the AAA to JAMS, and the clause "applies to any Claim you have not filed in court or in arbitration before the date you agreed to these Terms, and supersedes and amends any prior arbitration agreement ... including as to Claims that arose before."
- Mass claims: today's terms send 25 or more similar demands within 60 days to AAA batches, "one arbitrator to resolve each batch." The new text says 25 or more claimants within 90 days, or coordinated counsel, means "all of those Claims will be consolidated into one arbitration before one arbitrator" with a single set of fees under the JAMS Mass Arbitration Procedures. The arbitrator may also divide fees "among Pinterest, the claimants, and the claimants' lawyers," and either side can make a California section 998 settlement offer.
- New: a 30-day opt-out, "by emailing litigation@pinterest.com with your name, account email, and a statement that you're opting out." The current terms have none, and your Amazon article reports none in Amazon's consumer terms, so Pinterest ends up with a mass-claims rule like Amazon's plus an exit.

The privacy policy effective the same day also describes ads "when you're streaming a show on your connected TV" and "associating devices that may relate to the same person or household," which ties to Pinterest's tvScientific connected-TV business.

I haven't found any outlet covering the user side. Full write-up with the Amazon comparison, quoted before and after text and the opt-out steps: https://quietlychanged.com/changes/2026-10-20-pinterest-nov-12-terms-mass-claims-go-to-one-arbitrator-ads-follow-you-to-your/

QuietlyChanged tracks changes to the terms, privacy policies and prices of consumer services.

QuietlyChanged

## 3. Optional Bluesky reminder (quietlychanged.bsky.social), post Wed Nov 11 or Thu Nov 12, not today
We already posted about this on Bluesky on Oct 20, so this is a later reminder with a new hook (the opt-out window opens), not a repeat. Image: social/2026-10-20/deepdive/pinterest-arbitration-optout.png (reuse). Alt text: Pinterest's Nov 12 terms: 25 or more similar claims go to one arbitrator, and users get a 30-day opt-out by emailing litigation@pinterest.com.
Post:
Pinterest's new terms start Nov 12. To keep the option of going to court, email litigation@pinterest.com between Nov 12 and Dec 12 saying you opt out of Section 11 (include your name and account email). Steps and sources: https://quietlychanged.com/changes/2026-10-20-pinterest-nov-12-terms-mass-claims-go-to-one-arbitrator-ads-follow-you-to-your/
(If the composer says over 300, put the link in the first reply. Same angle suits an X self-reply under the Oct 20 post, https://x.com/QuietlyChanged/status/2112622382947164333, on Nov 12.)
