# Distribution drafts, 2026-11-03 (Stripe privacy policy rewrite, effective Nov 20, 2026)

Pick: today's Stripe deep dive. It has a near date (Nov 20, 17 days out), an enormous reach (Stripe powers a large share of online checkouts, so most shoppers are affected without knowing it) and no news coverage. Coverage re-check (WebSearch, Nov 3 ~3:10 PM MT): only Stripe's own pages, a B2B policy-tracker post (Venpo, Oct 23, aimed at businesses; covers the AI voice agents, call-recording AI training, card-issuer data and the GPC narrowing) and a LinkedIn post about Stripe's notice email (the email says Nov 20, a linked page says Sept 20). No outlet has covered it. Date-driven alternatives (Pinterest Nov 12, Google Play Nov 17, FCC Nov 25, SSA Nov 29, Xero Dec 28) were pushed in earlier sessions; Calm, Tubi, Toyota and Oura were pitched earlier and are excluded.

Re-verified today against the primary sources (fetched Nov 3): stripe.com/privacy still says "This Privacy Policy will be updated on November 20, 2026" and "Last updated: April 28, 2026", with the single line "Stripe honors the Global Privacy Control (GPC) opt-out preference signals." stripe.com/privacy/preview still contains every quoted line in the article: the AI-powered voice agents sentence, "train, test, and improve the artificial intelligence and machine learning models", "your IP address, email address, phone number, and shipping address—with your card-issuing bank", "transaction signals pooled across its global merchant network", the recovery-email sentence, the Link Settings opt-out, and the narrowed GPC sentence ("for the device and associated browser that transmits the signal ... you will need to opt-out or transmit a Global Privacy Control signal again"). Nothing to correct. The article went live and was deployed earlier today (commit 33cf96a, Vercel dpl_LVz8cid9v3nfJoVzMqckFqA8vF5X, live 200 verified again), so I did not rebuild it; no other changes were needed.

Dedup check: no earlier draft, outreach-log entry or send to MediaPost, Wendy Davis or Payments Dive. Not re-pitched: Proof News (Calm, Nov 2), Jared Newman, Janko Roettgers, The Verge, Kashmir Hill, The Record, 404 Media, Ars, TechCrunch, Arizent/American Banker (already pitched on other stories). Skipped on purpose: Fintech Business Weekly (Jason Mikula's only public address is listed for sponsorship), Fintech Takes (only a sponsorship form and a podcast booking address), IAPP (press office, not a reporter), r/privacy (posted Oct 24 and Oct 29), Hacker News.

Everything goes from quietlychangedbiz@gmail.com and the QuietlyChanged accounts, signed only "QuietlyChanged". Suggested timing: emails now to Wed Nov 4 ~7-9 AM MT; Bluesky today ~4-5 PM MT or Wed ~8 AM MT; Reddit (optional) Wed ~8-10 AM MT after checking the rules in the signed-in browser (the box gets 403s from Reddit).

## 1. Email: Wendy Davis, MediaPost (senior writer, policy and regulatory coverage; has written repeatedly on the Global Privacy Control, e.g. the Aug 3, 2026 Wyden letter story)
To: wdavis@mediapost.com. Source: MediaPost masthead, "Wendy Davis, Senior Writer/Policy & Regulatory Coverage wdavis@mediapost.com" https://www.mediapost.com/publications/masthead/ (also her author page https://www.mediapost.com/publications/author/3220/wendy-davis/).
Subject: Stripe's Nov 20 privacy update narrows how it honors Global Privacy Control signals
Body:
Hi Wendy,

Since you've covered how companies handle universal opt-out signals, this may be useful: Stripe, whose payment forms sit behind a large share of online checkouts, is rewriting its privacy policy effective November 20, and the update narrows its Global Privacy Control language. I haven't found any coverage of it.

Current policy (last updated April 28, 2026), in full: "Stripe honors the Global Privacy Control (GPC) opt-out preference signals."

Preview policy (effective November 20, 2026): "Where we detect a Global Privacy Control ("GPC") signal, we will honor it as a request to opt out of "sales" and "sharing" (for behavioral advertising) for the device and associated browser that transmits the signal. Note that if you or your browser clear or expire cookies, you will need to opt-out or transmit a Global Privacy Control signal again to opt-out."

So the commitment goes from a one-line promise to one tied to a single device and browser that has to be re-sent after cookies are cleared. The same policy still says that some of Stripe's data provision to third parties "may be considered a data 'sale' or 'sharing' (for behavioral advertising)" under California and other state laws. I'm not claiming this conflicts with any state law; the point is the wording shrank in a policy that applies to people who only ever used a Stripe-powered checkout.

The rest of the rewrite, for context (all quoted in our write-up):
- Stripe may use "AI-powered voice agents" to contact people for "sales, marketing, and lead qualification," and may use call recordings and transcripts "to train, test, and improve the artificial intelligence and machine learning models." The only opt-out offered is for recording, at the start of the call.
- At payment authorization, Stripe may share "your IP address, email address, phone number, and shipping address" with "your card-issuing bank."
- Transaction patterns "pooled across its global merchant network" may inform how Stripe handles a person's payments at other merchants.
- Abandoned-checkout "recovery emails" can be sent on a merchant's instruction if you typed an email and didn't finish paying.

Primary sources:
Current policy: https://stripe.com/privacy
Preview of the Nov 20 policy: https://stripe.com/privacy/preview
Our write-up with the full before/after text: https://quietlychanged.com/changes/2026-11-03-stripe-stripe-s-nov-20-privacy-rewrite-ai-voice-agents-your-data-to-your-bank-a/

QuietlyChanged tracks changes to the terms, privacy policies and prices of consumer services.

QuietlyChanged

## 2. Email: Payments Dive newsroom (attention: Justin Bachman, senior reporter, who wrote the latest Stripe stories there)
To: payments.dive.editors@paymentsdive.com. Source: the "Get in touch" address on Payments Dive reporter pages (https://www.paymentsdive.com/editors/jpothen/); the reporter Justin Bachman lists no personal email there. Fallback if it bounces: info@industrydive.com (https://www.paymentsdive.com/contact/).
Subject: Stripe's Nov 20 privacy rewrite: AI voice agents, data to card issuers, pooled merchant signals
Body:
Hi Justin and the Payments Dive team,

Stripe's privacy policy changes on November 20, and the preview has consumer-facing additions beyond the AI voice agents that Stripe itself lists in its summary. I couldn't find news coverage; the only write-up is a B2B policy-tracker post (Venpo, Oct 23) that focuses on businesses using Stripe.

Where the preview (https://stripe.com/privacy/preview) differs from the current April 28 policy (https://stripe.com/privacy), quoted:
- Card issuers: "During payment authorization, Stripe may also share fraud risk signals—including Stripe's risk assessment, and your IP address, email address, phone number, and shipping address—with your card-issuing bank to help approve genuine transactions and reduce unnecessary payment failures. Card issuers are independent data controllers for signals they receive."
- Pooled signals: "Stripe uses transaction signals pooled across its global merchant network to optimize payment authorization rates. This means transaction patterns from your payments at one merchant may inform how Stripe routes authorization requests at other merchants."
- Signup and login: its fraud services "may collect device and behavioral signals at the time of account registration and login on platforms that have enabled Stripe's risk API services," and "Merchants using these services are required by their Stripe agreement to disclose this collection to their customers."
- AI voice agents: Stripe "may leverage automated dialing systems and AI technologies, such as AI-powered voice agents ... for operational, support, sales, marketing, and lead qualification purposes," and may use call recordings and transcripts "to train, test, and improve the artificial intelligence and machine learning models." The only opt-out offered is for recording, at the start of the call.
- Link: transaction data tied to a Link account may be used "to derive insights, personalize offers and communications, and make them available to Business Users," with opt-out through Link Settings; Link is moving to its own policy.
- Abandoned checkout: merchants can instruct Stripe to send a "recovery email" if you entered an email and didn't finish paying.
- Global Privacy Control: the one-line promise becomes a signal honored only for "the device and associated browser that transmits the signal," to be re-sent after clearing cookies.

One oddity that may matter to merchants: Stripe's notice email gives the effective date as November 20, while a page it links to has been reported (a LinkedIn post by Melanie Ensign) as saying September 20. The preview page itself says November 20.

Full write-up with before/after text and a plain-language list of what people can do: https://quietlychanged.com/changes/2026-11-03-stripe-stripe-s-nov-20-privacy-rewrite-ai-voice-agents-your-data-to-your-bank-a/

QuietlyChanged tracks changes to the terms, privacy policies and prices of consumer services.

QuietlyChanged

## 3. Bluesky (quietlychanged.bsky.social): image post plus two self-replies
Image: social/2026-11-03/distribution/01-bank-and-gpc.png (1200x675; same file as deepdive/03, the card with the card-issuer line and the GPC before/after). Check the image upload size; the file is a normal PNG.
Alt text: Stripe privacy policy comparison. Sent to your card's bank during payment, new text: "Stripe may also share fraud risk signals, including Stripe's risk assessment, and your IP address, email address, phone number, and shipping address, with your card-issuing bank." Global Privacy Control, before (April 2026): "Stripe honors the Global Privacy Control (GPC) opt-out preference signals." Now (effective November 20): "...for the device and associated browser that transmits the signal. If you or your browser clear or expire cookies, you will need to opt-out or transmit a Global Privacy Control signal again."
Post (279 characters):
Stripe's privacy policy changes on Nov 20.

Today it says: "Stripe honors the Global Privacy Control (GPC) opt-out preference signals."

The new version: only for "the device and associated browser that transmits the signal," and you have to send it again after clearing cookies.
Self-reply 1 (289 characters):
Same update: your card's bank may get your IP, email, phone and shipping address at checkout, and AI voice agents may call you (recordings can train AI). Details: https://quietlychanged.com/changes/2026-11-03-stripe-stripe-s-nov-20-privacy-rewrite-ai-voice-agents-your-data-to-your-bank-a/
Self-reply 2 (108 characters):
Sources: https://stripe.com/privacy (in force now) and https://stripe.com/privacy/preview (effective Nov 20)
(Check the 300-grapheme limit in the composer; Reply 1 is close. If over, cut "at checkout".)
Note: the X deep-dive post for Stripe (social/2026-11-03/deepdive/post.txt) is a separate X original awaiting Samuel's OK; this Bluesky post uses a different angle (GPC) so the two don't duplicate.

## 4. Reddit r/stripe (optional, u/QuietlyChanged): text post, primary-source links only, NO quietlychanged.com link, no image
Rules: unread (the box gets 403 from Reddit). Before posting, check the sidebar rules and flair in the signed-in browser; r/stripe is mostly merchants, and many subreddits ban self-promotion and off-topic policy posts. If a policy-change post isn't allowed or looks off-topic, skip it. Do not also post in r/privacy (posted Oct 24 and Oct 29) or any other subreddit today.
Title: Heads up if you use Stripe checkout: the privacy policy changes Nov 20 (AI voice agents, data sent to card issuers, narrower GPC, abandoned-checkout emails)
Body:
Stripe added a notice at the top of its Privacy Policy saying it "will be updated on November 20, 2026," with a preview at stripe.com/privacy/preview. I compared the preview with the current April 28 version. Things that stood out for people running checkouts:

1. Card issuers: "Stripe may also share fraud risk signals, including Stripe's risk assessment, and your IP address, email address, phone number, and shipping address, with your card-issuing bank" during payment authorization. These lines are not in the April policy.
2. Pooled signals: "transaction patterns from your payments at one merchant may inform how Stripe routes authorization requests at other merchants."
3. Signup and login: fraud services may collect device and behavioral signals at registration and login on platforms using Stripe's risk API, and "Merchants using these services are required by their Stripe agreement to disclose this collection to their customers." If you use those services, your own privacy notice may need updating.
4. Abandoned checkout: "the merchant may instruct Stripe to send you a recovery email as a reminder" when someone enters an email and doesn't pay. The opt-out is the unsubscribe link or the merchant.
5. AI voice agents may be used for Stripe's own outreach, with call recordings and transcripts used "to train, test, and improve the artificial intelligence and machine learning models." Opt-out is only for recording, at the start of the call.
6. GPC: the old line was "Stripe honors the Global Privacy Control (GPC) opt-out preference signals." The new one honors it "for the device and associated browser that transmits the signal" and says you'll need to send it again after clearing cookies.

Sources: https://stripe.com/privacy (current) and https://stripe.com/privacy/preview (effective Nov 20, 2026).
