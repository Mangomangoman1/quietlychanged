# Distribution drafts, 2026-10-29 (SSA "Client Data System" 60-0392, new Privacy Act system of records, comments close Nov 29, 2026)

Why this one: it affects anyone who has been issued a Social Security number, it has a fixed public comment deadline (Nov 29, 2026, 30 days after the Oct 30 publication, when the routine uses also take effect), and it still has zero coverage. Re-checked ~3:10 PM MT Oct 29: WebSearch and X full-archive search (posts since Oct 26) turned up nothing on "Client Data System" or 60-0392, and the Federal Register public-inspection API showed 23 page views. Grindr (Oct 28) is a smaller audience; Oura (Nov 4) and FCC (Nov 25) were already pitched.

Article (live 200, strengthened today, commit 723844b, Vercel dpl_prVsSz7X7zRcMTrt3xEx2pufwQYE): https://quietlychanged.com/changes/2026-10-29-social-security-social-security-is-building-one-client-data-system-profile-on-e/

Primary sources (re-verified Oct 29 ~3:00 PM MT against the public-inspection PDF):
- Public inspection page (live now): https://www.federalregister.gov/public-inspection/2026-22173/privacy-act-systems-of-records
- PDF: https://public-inspection.federalregister.gov/2026-22173.pdf ("scheduled to be published in the Federal Register on 2026-10-30"; [Docket No. SSA-2025-0030]; "Notice of a new system of records"; "Client Data System (60-0392)")
- Document page from Oct 30: https://www.federalregister.gov/d/2026-22173
- Regulations.gov docket: https://www.regulations.gov/docket/SSA-2025-0030 (the API still returned 404 for the docket on Oct 29, so it should open when the notice publishes)
- Quotes used below, all checked in the PDF: covers "individuals who have been issued a Social Security number (SSN), including those who have conducted business with SSA beyond enumeration"; "primarily from existing SSA systems of records such as" followed by 12 named SORNs (60-0058, 0059, 0089, 0090, 0103, 0222, 0321, 0325, 0350, 0373, 0378, 0383); "customer interaction history, including notes or remarks entered by technicians"; "reason for marriage end"; "electronic block, high-risk, and special indicator warnings"; "Wounded Warrior and Department of Veterans Affairs 100% Permanent and Total Disability" indicators; "We may also use contact information (e.g., email addresses) ... for program outreach (e.g., notification about our programs, online services, SSA events, and surveys)"; 30 routine uses, including No. 17 (DHS, "upon request, to identify and locate aliens", already in 60-0058).
- 2007 context (added to the article today): SSA privacy impact assessment for the Integrated Client Database (ICDB), which said ICDB "does not require a new Privacy Act system of records": https://www.ssa.gov/privacy/pia/Integrated%20Client%20Data%20Base%20System.updtd%20Sept%2028.htm
- Related, Oct 20, 2026 SSA press release: about 25 million records with missing citizenship information updated using DHS SAVE data, and 8.5 million records with inaccurate citizenship status being corrected: https://www.ssa.gov/news/en/press/releases/2026-10-20.html

Images: social/2026-10-29/deepdive/02-whats-in-the-file.png (Bluesky; 1200x675), 03-notice-quotes.png (optional second image). 01-ssa-seal.png is for X only (see the seal caveat in deepdive/x-posts-deepdive.md).

Timing: send the emails and post Fri Oct 30 morning, after the notice publishes (~6 AM ET), so the federalregister.gov/d/ link resolves. Sent from quietlychangedbiz@gmail.com. Every draft signs only as QuietlyChanged. Nothing has been sent or posted.

## 1. Email: John Davisson, Director of Litigation, EPIC (Electronic Privacy Information Center)
Why: EPIC led the 14-organization comments on SSA's 60-0058 SORN (Dec 2025) and regularly comments on SSA SORNs. A heads-up about the comment window is directly useful to them.
To: davisson@epic.org (named as the contact in EPIC's published SSA comments: "please contact John Davisson, EPIC Director of Litigation, at davisson@epic.org", https://epic.org/documents/comments-of-epic-12-organizations-to-the-u-s-social-security-administration-on-the-system-of-records-notice-for-ssa-master-files/)
Subject: New SSA SORN (Client Data System, 60-0392) publishes Oct 30, comments due Nov 29
Body:
Hi John,

A heads-up in case it isn't on your radar yet, since EPIC commented on SSA's 60-0058 notice last December. SSA filed a notice of a new system of records, the Client Data System (60-0392). It publishes in the Federal Register today, Oct 30 (FR Doc. 2026-22173, docket SSA-2025-0030). Comments and the new routine uses are both due/effective Nov 29. I haven't found any coverage of it.

What stands out:
- Scope: it covers "individuals who have been issued a Social Security number (SSN), including those who have conducted business with SSA beyond enumeration," and records are retrieved by SSN.
- Sources: "primarily from existing SSA systems of records such as" 12 named SORNs (60-0058, 0059, 0089, 0090, 0103, 0222, 0321, 0325, 0350, 0373, 0378, 0383), plus contractors, vendors and federal, state and local agencies.
- What's in one profile: country of citizenship, yearly earnings, benefit and SSI payment amounts, marriage details including the spouse's SSN and "reason for marriage end," "customer interaction history, including notes or remarks entered by technicians," "electronic block, high-risk, and special indicator warnings," and Wounded Warrior and VA 100% disability indicators.
- New purpose: "We may also use contact information (e.g., email addresses) ... for program outreach (e.g., notification about our programs, online services, SSA events, and surveys)."
- 30 routine uses, including No. 17 (DHS "upon request, to identify and locate aliens," the same use 60-0058 carries) plus "law enforcement agencies and private security contractors" (No. 7), private collection contractors recovering overpayments (No. 26) and Treasury's Do Not Pay (No. 30). No exemptions are claimed.
- In 2007, SSA's privacy impact assessment for its Integrated Client Database said that shared client-data layer "does not require a new Privacy Act system of records." This notice now gives a much broader combined profile its own SORN.

Notice (public inspection PDF): https://public-inspection.federalregister.gov/2026-22173.pdf
FR page (live from Oct 30): https://www.federalregister.gov/d/2026-22173
2007 PIA: https://www.ssa.gov/privacy/pia/Integrated%20Client%20Data%20Base%20System.updtd%20Sept%2028.htm
Our side-by-side with SSA's earlier notices: https://quietlychanged.com/changes/2026-10-29-social-security-social-security-is-building-one-client-data-system-profile-on-e/

QuietlyChanged tracks changes to the terms, privacy notices and prices people live under.

QuietlyChanged

## 2. Email: The Record from Recorded Future News, attn. Suzanne Smalley (covers digital privacy, surveillance and government data)
Why: Suzanne Smalley's author bio says she covers "digital privacy, surveillance technologies and cybersecurity policy." The Record publishes no individual reporter emails, so this goes to the newsroom tips address and is addressed to her.
To: therecord@recordedfuture.com (The Record contact page: "For tips, general inquiries, and error reports, please get in touch with us directly at therecord@recordedfuture.com", https://therecord.media/contact ; bio: https://therecord.media/author/suzanne-smalley)
Subject: Tip for Suzanne Smalley: SSA creates a single SSN-indexed "Client Data System," comments due Nov 29
Body:
Hi Suzanne (and The Record team),

A privacy notice that published today, Oct 30, and that nobody seems to have written about: the Social Security Administration is creating a new Privacy Act system of records called the Client Data System (60-0392), FR Doc. 2026-22173.

The short version:
- It covers "individuals who have been issued a Social Security number (SSN)," not just beneficiaries, and records are retrieved by SSN.
- It draws "primarily from existing SSA systems of records," and the notice names 12 of them, from the SSN master file and earnings records to the Digital Identity File and Customer Engagement Tools systems, plus contractors and other agencies.
- The single profile holds country of citizenship, yearly earnings, benefit amounts, marriage details (spouse's SSN, "reason for marriage end"), technicians' notes on your calls and visits, "high-risk" and other warning flags, and VA and Wounded Warrior indicators.
- New: SSA says it may use your email address "for program outreach (e.g., notification about our programs, online services, SSA events, and surveys)."
- 30 routine uses take effect Nov 29, including DHS "upon request, to identify and locate aliens" (already allowed under the SSN master-file notice), law enforcement and private security contractors.

For context: SSA said on Oct 20 that it had filled in citizenship information on about 25 million records using DHS's SAVE data and is correcting another 8.5 million. "Country of citizenship" is one of the fields in the new profile. The notice doesn't mention that project, so I'm only pointing out that the two overlap.

Public comments are open until Nov 29 at regulations.gov, docket SSA-2025-0030.

Notice: https://www.federalregister.gov/d/2026-22173 (PDF: https://public-inspection.federalregister.gov/2026-22173.pdf)
SSA's Oct 20 release: https://www.ssa.gov/news/en/press/releases/2026-10-20.html
Our breakdown, comparing it with SSA's earlier notices and a 2007 privacy impact assessment: https://quietlychanged.com/changes/2026-10-29-social-security-social-security-is-building-one-client-data-system-profile-on-e/

QuietlyChanged

## 3. Email: Drew Friedman, Reporter, Federal News Network (covers SSA operations, staffing and service)
Why: Drew Friedman covers SSA regularly at FNN (telework, staffing, union stories in 2026). The notice describes this system as a customer-service tool ("one main location to view information concerning the customer"), which fits his SSA operations beat. FNN's Jory Heckman was pitched Oct 19 on USPS; Drew is a different reporter and hasn't been pitched before.
To: drew.friedman@federalnewsnetwork.com (listed under "REPORTERS: Drew Friedman, Reporter" on FNN's contact page https://federalnewsnetwork.com/contact-us/)
Subject: SSA's new "Client Data System": one profile per SSN for front-line staff, comments due Nov 29
Body:
Hi Drew,

An SSA item from today's Federal Register (Oct 30) that I haven't seen covered. SSA is creating a new Privacy Act system of records, the Client Data System (60-0392), FR Doc. 2026-22173.

SSA says the system will "track and manage information about a customer including personal information and customer interactions" and give employees "one main location to view information concerning the customer," across pre-claims, claims and post-entitlement work. It covers everyone who has been issued an SSN. The notice names 12 existing SSA record systems as sources, among them the SSN master file, earnings, the Master Beneficiary Record, the SSI record, representative payee and appointed representative files, accommodation requests and the Customer Engagement Tools system.

Among the fields in one place: technicians' notes on calls and visits, communication preferences, accommodation needs, high-risk and special-indicator warnings, earnings, payment amounts and marriage details. It also adds a stated use of people's email addresses "for program outreach (e.g., notification about our programs, online services, SSA events, and surveys)."

Comments are open until Nov 29 (docket SSA-2025-0030), which is also when the 30 routine uses take effect.

Questions this raises: which front-line tools this supports, whether it ties into SSA's online-services and phone-service changes, and who builds and maintains it (the notice lists contractors and vendors among its sources).

Notice: https://www.federalregister.gov/d/2026-22173 (PDF: https://public-inspection.federalregister.gov/2026-22173.pdf)
Our breakdown: https://quietlychanged.com/changes/2026-10-29-social-security-social-security-is-building-one-client-data-system-profile-on-e/

QuietlyChanged

## 4. Email (optional fourth; send only if 1–3 are out): Joseph Cox, 404 Media (surveillance and data)
To: joseph@404media.co (404 Media About page: "Email him: joseph@404media.co", https://www.404media.co/about/)
Subject: SSA's new single profile on every SSN holder, with "high-risk" flags and staff notes (comments due Nov 29)
Body:
Hi Joseph,

Something in today's Federal Register (Oct 30) that nobody seems to have picked up: the Social Security Administration is creating a "Client Data System" (60-0392), a new system of records that keeps one SSN-indexed profile on "individuals who have been issued a Social Security number."

That profile pulls from 12 named SSA systems plus "contractor or vendor" and "Federal, State, and local agencies." It holds country of citizenship, earnings, benefit amounts, marriage history including "reason for marriage end," technicians' notes from your calls and visits, and "electronic block, high-risk, and special indicator warnings." It can be shared under 30 routine uses that take effect Nov 29, among them DHS "upon request, to identify and locate aliens," "law enforcement agencies and private security contractors," and private collection contractors recovering overpayments. SSA also says it may use your email for "outreach" and "surveys." In 2007 SSA said its shared client database didn't need its own system-of-records notice, because existing notices covered the data.

Notice: https://www.federalregister.gov/d/2026-22173 (PDF: https://public-inspection.federalregister.gov/2026-22173.pdf)
Comments: regulations.gov, docket SSA-2025-0030, until Nov 29
Our breakdown, which notes which routine uses are carried over from older notices: https://quietlychanged.com/changes/2026-10-29-social-security-social-security-is-building-one-client-data-system-profile-on-e/

QuietlyChanged

## 5. Bluesky (quietlychanged.bsky.social): image post plus a self-reply with links
Image: social/2026-10-29/deepdive/02-whats-in-the-file.png
Alt text: Card titled "One profile per Social Security number." SSA Client Data System (60-0392), new system of records, Oct 30, 2026. Pulled from 12 existing SSA record systems, plus contractors and other agencies. Contents: name, SSN, sex, birth date, parents, place of birth; country of citizenship; earnings by year; benefit and SSI payment amounts; marriages, including spouse SSN and "reason for marriage end"; call and office notes "entered by technicians"; "high-risk" and special warning flags; payee, representative and fee agreements; accommodation needs; Wounded Warrior and VA 100% disability flags. Covers "individuals who have been issued a Social Security number." Source: Federal Register, FR Doc. 2026-22173.
Post (272 chars):
Social Security is setting up one records profile per SSN: citizenship, earnings, benefits, marriage details, staff call notes, "high-risk" flags. It names 12 existing SSA systems as sources, and says your email can be used for outreach and surveys. Comments close Nov 29.
Self-reply (263 chars):
How to comment (docket SSA-2025-0030) and how it compares to older SSA notices: https://quietlychanged.com/changes/2026-10-29-social-security-social-security-is-building-one-client-data-system-profile-on-e/
The notice: https://www.federalregister.gov/d/2026-22173

## 6. Reddit r/privacy: link post to the Federal Register, primary sources only, NO quietlychanged.com link
Rules (from the Oct 24 ChatterAPI copy; the box still gets 403 from Reddit, so open https://old.reddit.com/r/privacy/about/rules in the signed-in browser first): R3 "No Self-Promotion Or Other Promotional Content"; R5 "Use Original, Credible Source And DO NOT Editorialize The Title"; R6 "Topic Already Covered"; R11 "No Astroturfing Of Any Kind". Search the sub for "Client Data System" / "60-0392" / "SSA system of records" first and skip if there's already a thread. Our last r/privacy post was Oct 24 (FCC), and that was a different story.
Title (the notice's own words: agency + "Notice of a new system of records" + system name; no editorializing): Social Security Administration: Notice of a new system of records, "Client Data System (60-0392)"
URL: https://www.federalregister.gov/d/2026-22173 (before ~6 AM ET Oct 30 use https://www.federalregister.gov/public-inspection/2026-22173/privacy-act-systems-of-records)
First comment (post right after submitting; primary links only):
Plain-English summary of what's in the notice:

- Who's covered: "individuals who have been issued a Social Security number (SSN), including those who have conducted business with SSA beyond enumeration." Records are retrieved by SSN.
- Where the data comes from: "primarily from existing SSA systems of records," and it names 12 of them (SSN master file 60-0058, earnings 60-0059, claims folders, Master Beneficiary Record, SSI record, rep payee file, Medicare database, appointed reps, office visits, Digital Identity File 60-0373, accommodation requests, Customer Engagement Tools), plus contractors, vendors and federal, state and local agencies.
- What sits in the one profile: country of citizenship, yearly earnings, benefit/SSI amounts, marriage details including spouse's SSN and "reason for marriage end," "notes or remarks entered by technicians," "electronic block, high-risk, and special indicator warnings," Wounded Warrior and VA 100% disability indicators.
- New stated use: contact info like email may be used "for program outreach (e.g., notification about our programs, online services, SSA events, and surveys)."
- 30 routine uses take effect Nov 29. Most already appear in SSA's other notices; one example is DHS "upon request, to identify and locate aliens," which the SSN master-file notice (60-0058) already allows.
- You can't opt out of a system of records. You can request or contest your record under SSA's Privacy Act rules.

Comments are due Nov 29, 2026 at https://www.regulations.gov/docket/SSA-2025-0030, or by mail to SSA's Head of Privacy and Disclosure Policy (address in the notice). Questions: LP.PDP.SORN@ssa.gov. PDF: https://public-inspection.federalregister.gov/2026-22173.pdf

## 7. X: no new draft
The deep-dive X original (277 chars, 3 images) is already held for the Fri Oct 30 AM session: social/2026-10-29/deepdive/x-posts-deepdive.md and post.txt. Reply targets checked Oct 29: the big posts on SSA's Oct 20 SSN cleanup (e.g., @GOP_is_Gutless https://x.com/GOP_is_Gutless/status/2115257910787797139, 79 replies ahead, posted Oct 27 7:42 PM MT) are politically charged and too crowded, which per the reply lesson means about 500 impressions. No reply drafted.

## Skipped (and why)
- r/SocialSecurity: a mod post ("Stop posting non questions", https://www.reddit.com/r/SocialSecurity/comments/1qejvtq/stop_posting_non_questions/) says non-question posts and rants get removed, and ThreadOtter (https://www.threadotter.com/subreddit-rules/socialsecurity) shows no written rules, so a PSA would likely be removed. Only comment (primary links only) if a user asks about SSA emails/surveys or a new SSA data system in an existing thread.
- Christian Robles (Nextgov/FCW; wrote the Oct 26 SSN-cleanup story): his author page lists only Signal (crobles808.12), no email. Optional Signal tip if Samuel wants it; not drafted.
- Natalie Alms (Nextgov) and Erich Wagner (GovExec): no public email found (GovExec/Nextgov only list feedback@govexec.com).
- WIRED, The Verge, Washington Post (Lisa Rein): no public reporter emails found from the box.
- Hacker News: per Samuel, not used.
- Grindr ToS, Oura Nov 4, FCC Nov 25: not re-pitched (Grindr is a smaller audience; Oura and FCC were pitched earlier).
