# Distribution drafts, 2026-11-06 (Wells Fargo Nov 24 OAA §15 AI Agents: non-autonomous definition, prove-revocation, registration, under-18, Delegates/indemnity/security-procedure)

Pick: today's Wells Fargo deep dive. Effective Nov 24, 2026 (~18 days). Near deadline, big bank, and still has underreported angles even though trade press already hit the liability/revocation headline. Proton (12→24 inactivity) is niche/positive — skipped. FCC Nov 25 already used today's X original slot. Smule already pitched Billboard + DMN Nov 5 — do not re-pitch them; MBW was blocked but Wells is the stronger unused story today.

Primary re-check (Nov 6, ~3:05–3:10 PM MT): live upcoming OAA at https://www.wellsfargo.com/online-banking/online-access-agreement/upcoming/ still "Version Effective November 24, 2026." Research save section15-full.txt still matches: §15(a) non-autonomous definition; §15(d)/(e) deemed authorization / AT YOUR OWN RISK; §15(f) retain evidence + notify §17(d); §15(g) may require registering AI Agents; §15(h) under-18 ban. Current May 21 OAA research save has **zero** "AI Agent" string matches. Customer summary still lists Third-party AI tools under Sections 15, 17(c) and 20(c).

Coverage re-check (Nov 6 PM, honest):
- **Already covered (do not claim scoop on these):** Penny Crosman, American Banker, Nov 2 — prove-you-revoked / stay-liable ("Wells Fargo wants customers to prove they've revoked AI agents", https://www.americanbanker.com/news/wells-fargo-wants-customers-to-prove-theyve-revoked-ai-agents). National Law Review — bank comparison table; WF permits at customer's risk (https://natlawreview.com/article/major-banks-move-block-or-limit-customer-directed-ai-agents). Captain Compliance, Nov 3 — deep §15 walkthrough including non-autonomous definition, registration, Chase Digital Services Agreement comparison, Regulation E questions (https://captaincompliance.com/news/wells-fargo-ai-agent-revocation-liability-regulation-e/). ACA International and TokenPost largely follow AB / those reports.
- **Still thin / useful for pitches:** under-18 ban in §15(h) (no news hit found on that clause specifically); Delegates' AI Agents + §20(c) indemnification + §8(b)/§17(c) security-procedure risk as a package; full blackline vs May 21 (zero "AI Agent" mentions). Prior Oct 29 rejection of a thinner WF AI-agent framing still stands for *general* bank-AI-agent coverage (USA Today / Axios / Chase Oct 27); this pitch is about THIS Nov 24 §15 text and the underreported clauses above — not "nobody has written about bank AI agents."

Strengthened + shipped (Nov 6 PM): added sourced "How this compares" vs Chase Terms of Use AI Agent notices (primary: https://www.chase.com/digital/resources/terms-of-use — Chase = autonomous/semi-autonomous only; WF adds non-autonomous, revocation-evidence, registration, under-18, Delegates stack). Updated coverage paragraph to name AB/Penny Crosman, NatLawReview, Captain Compliance, ACA, TokenPost. Added 1 FAQ (WF vs Chase definition) and 2 sources. Note: Captain Compliance already compared Chase's Digital Services Agreement; we quote Chase's live Terms of Use because that is the primary page we could re-fetch today. Rebuild `python3 build_site.py` (IndexNow 200 / 62 URLs). Manual Vercel deploy of site.b64 + vercel.json — see growth-log for deployment id.

Article: https://quietlychanged.com/changes/2026-11-06-wells-fargo-wells-fargo-s-nov-24-online-access-agreement-ai-agents-act-as-you-a/

Dedup check (grep growth-log.md + social/*/distribution-drafts.md):
- Never pitched Wells Fargo as a story.
- Kate Berry (kate.berry@arizent.com) was pitched Oct 15 on **Bank of America OBSA** — different story; OK for Wells. She did **not** write the Nov 2 AB Wells piece (Penny Crosman did) — so space her carefully and lead with underreported angles, not a rehash of Penny's revocation headline.
- Do **not** pitch Penny Crosman on this (she already wrote it).
- Katie Kelton (kkelton@bankrate.com) was pitched Oct 15 on BofA — different story; OK.
- Caitlin Mullen (cmullen@industrydive.com, Banking Dive) — never contacted.
- Not used today: everyone pitched Nov 1–5 on other stories (Smule/Billboard/DMN, Pinterest, Stripe, Calm, Tubi, Toyota, Canva). Payments Dive editors already got Stripe Nov 4 — skip for Wells.

Daily cap: Nov 6 so far **0 sent**. These 3 drafts fit under the limit of 5 from quietlychangedbiz@gmail.com. Sign only "QuietlyChanged". Suggested timing: emails Fri Nov 6 late afternoon / early evening MT (East Coast desks still reachable) or Sat AM if Samuel prefers. Bluesky/Reddit need Samuel OK. Skip X original (day's 1 slot used by FCC AM); deepdive X drafts remain under social/2026-11-06/deepdive/ for a possible 2nd original / evening — do not auto-post.

## 1. Email: Caitlin Mullen, Banking Dive (Senior Editor; covers M&A, regulation, AI and technology; ex-Payments Dive)
To: cmullen@industrydive.com. Source: her Banking Dive editor page, https://www.bankingdive.com/editors/cmullen/ ("You can reach her at cmullen@industrydive.com").
Subject: Wells Fargo's Nov 24 AI-agent terms also ban under-18s and may require agent registration
Body:
Hi Caitlin,

American Banker already covered Wells Fargo's prove-you-revoked AI-agent clause. A few nearby lines in the same Nov 24 Online Access Agreement still look underreported, and they may fit Banking Dive's AI/tech beat.

Upcoming Online Access Agreement, "Version Effective November 24, 2026" (https://www.wellsfargo.com/online-banking/online-access-agreement/upcoming/), brand-new Section 15:
- Definition: an "AI Agent" is "any software, application, program, or other technology that takes autonomous, semi-autonomous, or non-autonomous action on behalf of any person or entity." (Section 15(a))
- Under-18 ban: "you will not permit any AI Agent to access or use the Service or any Eligible Account on your behalf if you are under 18 years of age." (Section 15(h))
- Registration: Wells Fargo may, "at any time," change rules for agents "including requiring that you register your AI Agents with us." (Section 15(g))
- Delegates stack: Section 2 treats Delegates' AI Agent transactions as yours; Section 20(c) extends indemnification to AI Agents of you/Authorized Representatives/Delegates; Sections 8(b) and 17(c) say letting an AI Agent in "may adversely impact the commercially reasonable security procedures" you agreed to.

The May 21, 2026 agreement in force today has zero "AI Agent" mentions. Chase's public Terms of Use (https://www.chase.com/digital/resources/terms-of-use) defines AI agents as autonomous or semi-autonomous only — no "non-autonomous," no under-18 ban, no registration/revocation-evidence package like Wells Fargo's.

Write-up with the quoted Section 15 text, May 21 blackline and Chase comparison: https://quietlychanged.com/changes/2026-11-06-wells-fargo-wells-fargo-s-nov-24-online-access-agreement-ai-agents-act-as-you-a/

QuietlyChanged tracks changes to the terms, privacy policies and prices of consumer services.

QuietlyChanged

## 2. Email: Katie Kelton, Bankrate (Lead Community Reporter, CCC; invites story tips on her author page)
To: kkelton@bankrate.com. Source: her Bankrate author page, https://www.bankrate.com/authors/katie-kelton/ ("If you have a question about money or a story to tell, send her an email at kkelton@bankrate.com.").
Subject: Before Nov 24: Wells Fargo will treat AI/automation in your account as you — and bars under-18s from using agents
Body:
Hi Katie,

This may be a useful "what to do before the date" piece for Bankrate readers. Wells Fargo's Online Access Agreement updates on November 24, 2026. Trade press has covered the prove-you-revoked liability angle; a few consumer-facing details are still easy to miss.

From the upcoming agreement (https://www.wellsfargo.com/online-banking/online-access-agreement/upcoming/):
- If you give an AI agent (or, read literally, other automation) your login, its "instructions, actions, or transactions" are "deemed to have been initiated and authorized directly by you, without further verification." Use is "AT YOUR OWN RISK."
- To cut an agent off you must revoke it, "retain evidence of such revocation," and notify Wells Fargo; until then you "remain responsible for all the AI Agent's activities, to the extent permitted by law or regulation."
- People under 18 may not permit an AI Agent on their behalf.
- Wells Fargo may later require you to register AI Agents, and may block them.

The bank's customer notice says "You don't need to take any action" and that keeping online/mobile banking after Nov 24 means the new agreement applies (https://www.wellsfargo.com/mobile-online-banking/updates/). The May 21 version has no AI Agent section.

Practical steps and quotes: https://quietlychanged.com/changes/2026-11-06-wells-fargo-wells-fargo-s-nov-24-online-access-agreement-ai-agents-act-as-you-a/

QuietlyChanged tracks changes to the terms, privacy policies and prices of consumer services.

QuietlyChanged

## 3. Email: Kate Berry, American Banker (Reporter; CFPB, consumer regulation, big banks; did not write the Nov 2 Wells AI-agent piece — Penny Crosman did)
To: kate.berry@arizent.com. Source: American Banker Contact Us / her author page listing (mailto kate.berry@arizent.com), previously confirmed at https://www.americanbanker.com/author/kate-berry and https://www.americanbanker.com/contact-us.
Subject: Follow-up angles on Wells Fargo's Nov 24 §15: under-18 ban, Delegates' agents, May 21 blackline
Body:
Hi Kate,

Penny Crosman's Nov 2 piece correctly flagged Wells Fargo's prove-you-revoked AI-agent language. A few adjacent clauses in the same upcoming Online Access Agreement (effective Nov 24) still look thin in coverage and may fit a consumer-protection follow-up.

Primary: https://www.wellsfargo.com/online-banking/online-access-agreement/upcoming/
- Section 15(h): "you will not permit any AI Agent to access or use the Service or any Eligible Account on your behalf if you are under 18 years of age."
- Section 15(a): the definition includes "non-autonomous" action — broader than Chase's Terms of Use, which stops at "autonomous or semi-autonomous."
- Section 15(g): Wells Fargo may require customers to "register your AI Agents with us."
- Outside §15: Section 2 pulls Delegates' AI Agents into authorized transactions; Section 20(c) extends indemnification to those agents; Sections 8(b) and 17(c) warn that permitting an AI Agent "may adversely impact the commercially reasonable security procedures" customers agreed to.
- The May 21, 2026 agreement in force today contains zero "AI Agent" mentions — Section 15 is brand new, not a tweak.

Happy to send the blackline excerpts. Our write-up: https://quietlychanged.com/changes/2026-11-06-wells-fargo-wells-fargo-s-nov-24-online-access-agreement-ai-agents-act-as-you-a/

QuietlyChanged tracks changes to the terms, privacy policies and prices of consumer services.

QuietlyChanged

## 4. Bluesky (quietlychanged.bsky.social): image post + 2 self-replies
Image: social/2026-11-06/deepdive/02-non-autonomous-def.png (alt: Wells Fargo upcoming Online Access Agreement Section 15(a) defining AI Agent to include autonomous, semi-autonomous, or non-autonomous action). Optional second image: social/2026-11-06/deepdive/03-revoke-register-under18.png.
Post (keep under ~300 chars):
Wells Fargo's Nov 24 Online Access Agreement adds Section 15 on AI agents.

"Non-autonomous" tools count. Agent acts = you. Keep proof you revoked. May require registration. Under-18s barred.

May 21 version: zero "AI Agent" mentions.

Reply 1:
Chase's Terms of Use stops at "autonomous or semi-autonomous" and tells agents to identify themselves. Wells Fargo's upcoming §15 goes further on revocation evidence, registration and under-18.

Reply 2:
Quotes + sources: https://quietlychanged.com/changes/2026-11-06-wells-fargo-wells-fargo-s-nov-24-online-access-agreement-ai-agents-act-as-you-a/

Needs Samuel OK before posting.

## 5. Reddit: r/personalfinance (text post, primary links only)
Why this sub: consumer "what changes Nov 24 / what should I do" fit; high traffic. Rules unread from the box (Reddit often 403s here) — check sidebar in the signed-in browser before posting. Because self-promo rules are unknown, this links only Wells Fargo / Chase primary pages, with no QuietlyChanged link. Add our article only if the rules clearly allow it, or in a comment if someone asks for a source.
Title: PSA: Wells Fargo Online Access Agreement (Nov 24) — AI/automation in your account counts as you; under-18s barred from using agents
Body:
Wells Fargo posted an upcoming Online Access Agreement effective November 24, 2026. New Section 15 covers "Third-Party Artificial Intelligence Agents or Agentic AI." Worth reading if you ever let a tool log into online banking.

Highlights from the upcoming text:
- Definition includes software that takes "autonomous, semi-autonomous, or non-autonomous action" for you.
- If you give an agent your login (or otherwise authorize it), its instructions/actions/transactions are "deemed to have been initiated and authorized directly by you, without further verification." Use is "AT YOUR OWN RISK."
- To revoke: you must revoke properly, "retain evidence of such revocation," provide it if asked, and notify Wells Fargo; you stay responsible until then "to the extent permitted by law or regulation."
- Wells Fargo may require you to register AI Agents and may block them.
- Under 18: you may not permit an AI Agent on your behalf.
- Delegates: if someone you've authorized uses their own AI Agent on your account, that can count as you too.

The May 21, 2026 agreement currently in force has no AI Agent section. Wells Fargo's customer summary says you don't need to take action and that continued use after Nov 24 accepts the update.

Sources (primary):
Upcoming OAA: https://www.wellsfargo.com/online-banking/online-access-agreement/upcoming/
Current OAA (May 21): https://www.wellsfargo.com/online-banking/online-access-agreement/
Customer summary: https://www.wellsfargo.com/mobile-online-banking/updates/

Not legal advice — read the agreement yourself.

## 6. Reddit: r/WellsFargo (text post, primary links only) — optional second
Why: account-holders most affected. Rules unread (box 403) — confirm before posting; if the sub is quiet or bans PSAs, skip. Same primary-links-only rule as above.
Title: Upcoming Online Access Agreement (Nov 24): new Section 15 on AI agents — non-autonomous tools, prove revocation, under-18 ban
Body:
Same substance as the r/personalfinance draft above; lead with the Nov 24 date and link the three Wells Fargo URLs. No QuietlyChanged link unless rules allow.

## Skipped
- Hacker News (Samuel's Oct 26 rule).
- Penny Crosman / American Banker (already wrote the Nov 2 piece).
- Payments Dive editors (pitched Stripe Nov 4).
- X original for distribution (day's 1 original already used by FCC AM). Optional evening 2nd original: use social/2026-11-06/deepdive/ drafts — do not auto-post.
- r/banking: lower traffic than r/personalfinance for consumer PSA; optional alternate if PF rules block.

## For parent
- **SEND now** (from quietlychangedbiz@gmail.com via user-Gmail-8175303--qc), up to 3 of 5 daily cap:
  1. cmullen@industrydive.com — subject above
  2. kkelton@bankrate.com — subject above
  3. kate.berry@arizent.com — subject above (follow-up angles only; she did not write the AB Wells piece)
- **Need Samuel OK:** Bluesky post + self-replies; Reddit r/personalfinance and optional r/WellsFargo.
- **Do not send/post from this executor.** Cap if parent sends all 3 emails: **3 of 5** used Nov 6.
