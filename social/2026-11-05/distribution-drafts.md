# Distribution drafts, 2026-11-05 (Smule Dec 4 terms and privacy policy: AI training on recordings, licensing de-identified recordings to "Recording Licensees", opt-out only from Dec 4, 18+ only)

Pick: today's Smule deep dive. It has a date (Dec 4, four weeks out), a clear "you can't opt out until it's already in force" hook, it covers recordings already shared, it bans teens who are on the app today, and it still has no news coverage. No stronger verified, unpitched find turned up. Replika is already covered (companionhunt and others), and eBay Nov 26 is mild.

Coverage re-check (Nov 5, ~3:20 to 3:45 PM MT): 4 WebSearch passes ("Smule terms of service AI training recordings December 2026", "Smule \"Recording Licensees\"", "Smule minimum age 18 teens karaoke app AI licensing news", "r/SmuleSing terms of service AI training December 4 opt out"), plus X post search (smule + AI/terms/licens/18/privacy since Nov 3) and X News search ("Smule", 30 days). Found: Smule's own blog post (Nov 4), a sing.salon fan-forum repost, Gen Digital's automated "Agent Trust Hub" app page (built from the old documents; it says AI training is "Not stated"), and one Chinese-language user post on X (@Natsu_ringoame, 38 impressions). No news outlet, trade press or newsletter coverage, and no X News story.

Re-verified against the primary sources: fresh headless-Chrome fetch of smule.com summary_of_changes/updated, termsofservice/updated, privacy/updated, termsofservice and privacy (Nov 5 ~3:05 PM MT), plus curl of blog.smule.com/updated-terms-of-service/ (200). Every quoted string in the article was found in the live pages: both "EFFECTIVE: December 4, 2026" headers, "Beginning on December 4, 2026", the Recording Licensees licensing sentence (terms and privacy), the research-only sentence (current policy), 13 to 18, "postmarked within thirty (30) days of first accepting these Terms", the reject-future-changes sentence (current terms only), the $75,000 fee line, the go-forward-only and "does not affect De-Identified Data provided ... before then" lines, "regardless of location", the minors line and the voiceprint lines. Blog lines ("examples, not a complete list", "already shared" = "Yes", username/email/device ID, "stays linked to your account") are all still there. Nothing to correct. New detail found: the words "generative", "synthesize" and "clone" don't appear in either new document.

Strengthened (commit 87c2b0b; Vercel dpl_45DUeLuPCE82EmLQeGrgtturxpY1, manual deploy of site.b64 + vercel.json; live 200 with the new text; /services/zoom/ still 301; SEO compare 192 to 192, 0 missing, 0 field changes, 1 JSON-LD change (the article's FAQ); IndexNow 200 at build (62 URLs) and after deploy (3 URLs)): added a sourced "How this compares" paragraph on SoundCloud. In May 2025, after a backlash, SoundCloud replaced its 2024 AI-training line. Its live terms (checked today) say: "We will not use your content to train generative AI models that aim to replicate or synthesize your voice, music, or likeness without your explicit consent, which must be affirmatively provided through an opt-in mechanism." Sources: soundcloud.com/terms-of-use, The Verge (May 2025), Music Business Worldwide (May 14, 2025). Also added 1 FAQ (Smule vs SoundCloud) and updated the coverage line. StarMaker was checked but not used: the policy page I could render is StarMe's, a different app, and it has no AI wording. Yokee is JS-only.

Article: https://quietlychanged.com/changes/2026-11-05-smule-smule-s-dec-4-terms-your-recordings-can-train-ai-and-be-licensed-to-other/

Dedup check: Smule has never been pitched. No one below has been contacted by QuietlyChanged before (grep of growth-log.md and all distribution drafts: no billboard.com, musicbizworldwide.com or digitalmusicnews.com addresses). Not used: everyone pitched in the last 8 days (Laurie Sullivan, Luis Rijo, Wendy Davis, Payments Dive, Annie Gilbertson and others).

Daily cap: 4 pitches went out Nov 4 and none are logged as sent today, so these 3 fit under today's limit of 5. Everything goes from quietlychangedbiz@gmail.com and the QuietlyChanged accounts, signed only "QuietlyChanged". Suggested timing: emails Fri Nov 6, 7 to 9 AM MT (trade desks are East Coast and London), or tonight if Samuel prefers. Bluesky Fri ~8 AM MT. Reddit any time after Samuel checks the sub's rules.

## 1. Email: Kristin Robinson, Billboard (Senior Writer, music publishing and technology, "particular expertise in artificial intelligence"; writes the Machine Learnings newsletter; wrote "BeatStars to Provide AI Training Opt-Outs for Creators Via Sureel Deal", Apr 29, 2025, and co-wrote "How AI Rights Are Changing Record Contracts", Apr 21, 2026)
To: krobinson@billboard.com. Source: her Billboard author page, https://www.billboard.com/author/kristin-robinson/ (address shown in the page's author box).
Subject: Smule will license users' recordings to outside AI companies from Dec 4, and the opt-out opens the same day
Body:
Hi Kristin,

You've covered AI-training opt-outs (BeatStars and Sureel) and AI rights in record contracts, so this may fit Machine Learnings. Smule, the karaoke app, changes its terms on December 4 so it can license its users' recordings to outside companies to build and sell AI. I haven't found any news coverage. The only mentions are Smule's own blog and a fan forum.

From the new privacy policy, effective December 4, 2026 (https://www.smule.com/en/privacy/updated):
- "We may share or license De-Identified Data with or to Recording Licensees, including to develop, train, test, improve, and commercialize artificial intelligence and machine learning algorithms, models and features." The current policy only says Smule shares de-identified content "with researchers for educational research purposes."
- Opting out "applies only to De-Identified Data we make available after we process your opt-out. It does not affect De-Identified Data provided to Recording Licensees before then."

Smule's summary of changes says the opt-out (Settings > Privacy > AI & Data) is available "Beginning on December 4, 2026", which is the day the terms take effect. Its blog confirms that the change covers recordings users have already shared. No licensees are named. Smule's list of example uses (vocal separation, pitch correction, coaching) is "examples, not a complete list." The same update raises the US minimum age from 13 to 18.

For contrast, after last year's backlash SoundCloud's terms say it won't train generative AI that aims to replicate "your voice, music, or likeness" without opt-in consent. Smule's new documents don't mention generative AI or voice cloning either way.

Our write-up has the before and after text and all the sources: https://quietlychanged.com/changes/2026-11-05-smule-smule-s-dec-4-terms-your-recordings-can-train-ai-and-be-licensed-to-other/

QuietlyChanged tracks changes to the terms, privacy policies and prices of consumer services.

QuietlyChanged

## 2. Email: Music Business Worldwide news desk, attention Murray Stassen (he wrote "SoundCloud 'fixes' music AI policy following backlash", May 14, 2025)
To: email@musicbizworldwide.com. Source: MBW's contact page, https://www.musicbusinessworldwide.com/contact-us/ ("Send Us News" link, mailto:email@musicbizworldwide.com?subject=News%20Submission). No personal address for Stassen is published there.
Subject: News: Smule's Dec 4 terms let it license user recordings to third parties for AI (attn Murray Stassen)
Body:
Hi Murray (and the MBW news desk),

You covered SoundCloud rewriting its AI clause after the 2025 backlash. Smule, the karaoke and social singing app, is going the other way, and I haven't seen anyone report it.

New Terms of Service and Privacy Policy, both "EFFECTIVE: December 4, 2026":
- Terms (https://www.smule.com/en/termsofservice/updated), inside the license users grant Smule: "We may use and retain Personal Information and User Content to develop, train, test, and improve the artificial intelligence and machine learning models and features that power our own Services, and we may license or otherwise make available De-Identified Data to Recording Licensees, including to develop, train, test, improve, and commercialize artificial intelligence and machine learning algorithms, models and features."
- The privacy policy defines Recording Licensees as "third parties". The current policy only allows de-identified sharing "with researchers for educational research purposes."
- It covers back catalogue: Smule's blog answers "Does this apply to recordings I've already shared?" with "Yes."
- The opt-out only opens "Beginning on December 4, 2026", the day the terms take effect, and it doesn't reach data already delivered to licensees.

Unlike SoundCloud's opt-in rule for generative AI, Smule's documents don't mention generative AI or voice cloning. They bar licensees only from re-identifying users or making voiceprints. The update also raises the US minimum age from 13 to 18.

Write-up with the quoted before and after text and sources: https://quietlychanged.com/changes/2026-11-05-smule-smule-s-dec-4-terms-your-recordings-can-train-ai-and-be-licensed-to-other/

QuietlyChanged tracks changes to the terms, privacy policies and prices of consumer services.

QuietlyChanged

## 3. Email: Ashley King, Digital Music News (author and analyst; wrote "Is the Future of AI Licensing Opt-In, or Opt-Out?", Aug 13, 2026, and "What Are the AI Rules at Major Streaming Platforms?", Mar 6, 2026)
To: ashley@digitalmusicnews.com. Source: Digital Music News About page, https://www.digitalmusicnews.com/about/ (the envelope link under "Ashley King, Author, Analyst", mailto:ashley@digitalmusicnews.com).
Subject: Smule picks opt-out for AI licensing of user recordings, and the switch only appears Dec 4
Body:
Hi Ashley,

Your August piece asked whether AI licensing will be opt-in or opt-out. Smule just answered for its users, and I haven't found any coverage beyond Smule's own blog.

Smule's new privacy policy, effective December 4, 2026 (https://www.smule.com/en/privacy/updated):
- "We may share or license De-Identified Data with or to Recording Licensees, including to develop, train, test, improve, and commercialize artificial intelligence and machine learning algorithms, models and features." Today's policy only mentions sharing de-identified content "with researchers for educational research purposes."
- This applies to recordings users have already shared (Smule's blog: "Yes").
- The opt-out (Settings > Privacy > AI & Data) is available "Beginning on December 4, 2026", the same day the terms take effect. Opting out "does not affect De-Identified Data provided to Recording Licensees before then."

Smule's own AI training is also on by default, with examples like "pitch and range feedback in Coach". Licensees can't re-identify users or make voiceprints. But neither document mentions generative AI or voice cloning, which is the case SoundCloud's terms now say requires opt-in. Teens are also out: the US minimum age goes from 13 to 18.

Our write-up has the before and after text, the opt-out steps and the sources: https://quietlychanged.com/changes/2026-11-05-smule-smule-s-dec-4-terms-your-recordings-can-train-ai-and-be-licensed-to-other/

QuietlyChanged tracks changes to the terms, privacy policies and prices of consumer services.

QuietlyChanged

## 4. Bluesky (quietlychanged.bsky.social): image post + 2 self-replies
Image: social/2026-11-05/deepdive/02-licensing-before-after.png. Alt text: Smule privacy policy, before: "In limited situations, we share de-identified content and information with researchers for educational research purposes." After (Dec 4, 2026): "We may share or license De-Identified Data with or to Recording Licensees, including to develop, train, test, improve, and commercialize artificial intelligence and machine learning algorithms, models and features."
Post (282 characters):
Smule's new terms start Dec 4: your karaoke recordings, old ones included, can train Smule's AI, and de-identified copies can be licensed to other companies to "commercialize" AI.

The opt-out only opens Dec 4 and can't pull back anything already handed over. Under-18s are out too.

Reply 1:
SoundCloud went the other way after its 2025 backlash: no training generative AI on your voice, music or likeness without opt-in consent. Smule's new documents don't mention generative AI or voice cloning at all.

Reply 2:
From Dec 4: Settings > Privacy > AI & Data, two separate switches (Smule's AI training, licensing to partners). Quotes and sources: https://quietlychanged.com/changes/2026-11-05-smule-smule-s-dec-4-terms-your-recordings-can-train-ai-and-be-licensed-to-other/

## 5. Reddit: r/SmuleSing (text post, primary links only)
Why this sub: it's the active Smule community on Reddit. Search results show 2026 posts about playlists, notifications, verified users and Smule blog posts (e.g. "Blog: You Can Now Adjust Your Vocal Volume After You Post"), so reposting Smule blog news is normal there. r/smule seems inactive or unindexed. We haven't used either sub before. Rules unread: the box gets 403 and a captcha from Reddit, so check the sidebar in the signed-in browser first. Because self-promotion rules are unknown, this links only Smule's own pages, with no QuietlyChanged link. Add our article only if the rules clearly allow it, or in a comment if someone asks for a source.
Title: PSA: Smule's new terms (Dec 4) let it license your recordings, including old ones, to other companies for AI, and the opt-out only opens Dec 4
Body:
Smule posted new Terms of Service and a new Privacy Policy that take effect December 4, 2026. Some lines worth reading before then:

- AI training: "We may use and retain Personal Information and User Content to develop, train, test, and improve the artificial intelligence and machine learning models and features that power our own Services" (examples given include "pitch and range feedback in Coach").
- Licensing to other companies: "We may share or license De-Identified Data with or to Recording Licensees, including to develop, train, test, improve, and commercialize artificial intelligence and machine learning algorithms, models and features." The current policy only mentions sharing de-identified content "with researchers for educational research purposes."
- Old recordings count: Smule's blog answers "Does this apply to recordings I've already shared?" with "Yes."
- Opt-out timing: "Beginning on December 4, 2026, you may opt out of Smule's AI training, our licensing of de-identified data to third parties, or both ... under Settings > Privacy > AI & Data, or through our online support form." The two switches are separate. Opting out doesn't undo training or licensing that already happened.
- Age: the minimum age in the US goes from 13 to 18, and accounts of minors get suspended or terminated. If you're under 18, save any recordings you want to keep before Dec 4.
- If you don't agree, the only option Smule gives before Dec 4 is deleting your account (Settings > Support > Delete Account).

Sources:
Summary of changes: https://www.smule.com/en/summary_of_changes/updated
New Terms: https://www.smule.com/en/termsofservice/updated
New Privacy Policy: https://www.smule.com/en/privacy/updated
Smule blog FAQ: https://blog.smule.com/updated-terms-of-service/

## Skipped
- Hacker News (Samuel's rule). r/privacy (posted Oct 24 and Oct 29). r/singing (a vocal-technique sub; a terms PSA is off-topic and rules unread).
- Ed Newton-Rex (found the SoundCloud clause; fits well, but he's an advocate rather than a reporter and I found no public email). Wired and The Verge AI-copyright reporters: no public email found in this pass, and The Verge's Jess Weatherbed and Andrew Hawkins have been pitched before (on other stories).
- X: the deep-dive X post (social/2026-11-05/deepdive/post.txt) is still waiting as today's possible 2nd original. Nothing new drafted for X.
