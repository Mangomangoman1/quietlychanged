# X research: tiny-office IT chores (Sep 28 – Oct 19, 2026)

Read-only via `x` MCP (`search_posts_all`, `get_posts_counts_recent`, `search_news`). No posting. Official dates cross-checked on Microsoft docs / Tech Community.

**Caveat:** On X in this window, organic posts from 1–15 person dental/CPA/law/clinic owners are scarce. Most signal is MSPs, tool builders, and PSAs. Counts below are honest (distinct substantive posts in searches, not invented). Recent 7-day API counts are noted where available.

---

## Top recurring complaints

### 1. M365 SMTP AUTH Basic auth cutoff will break scan-to-email / copiers / form senders
**Summary:** End of Dec 2026, Exchange Online turns off Basic auth for SMTP AUTH by default; devices that email with a stored username/password (copiers, scanners, website forms, ERP) can stop sending.
**Rough count:** ~12–15 distinct posts in the window (mostly PSA/vendor; almost no “my copier already broke” yet — deadline is still future). Last ~7 days API count for related query: **11**.
**What people do today:** Run EAC “SMTP AUTH clients” report; re-enable Basic auth per-tenant for now; migrate senders to OAuth / Graph; open-source or paid SMTP relays; leave leftover on-prem Exchange just for scan-to-email after M365 migration.
**Links:**
- https://x.com/mderooij/status/2104485516632625479 (MVP PSA, Sep 28)
- https://x.com/jlvardon/status/2107184917138604082 (small-office heads-up + Graph relay)
- Also: https://x.com/josepollman82/status/2110326932038684879 , https://x.com/blackoarstudio/status/2109965340679745810 , https://x.com/FirstMoverProj/status/2112174350371803608

### 2. Shared mailboxes are a mess (connectors, access delay, monitoring gaps)
**Summary:** Shared / front-desk / billing mailboxes don’t show up in many AI/Outlook connectors; access after adding someone can take ages; security tools miss them; small offices still share one password for info@.
**Rough count:** ~8–12 distinct posts. Last ~7 days API: **7** for `"shared mailbox" +(Microsoft|M365|Outlook|Exchange)`.
**What people do today:** Ask vendors for shared-mailbox support; copy files out of Shared Drives as workaround; use Full Access + wait; MSPs preach “sign in as yourself + shared mailbox, not a shared password.”
**Links:**
- https://x.com/Finchwizard/status/2107366859280663015 (organic: “disgusting how long” shared-mailbox access takes)
- https://x.com/gregnmitchell/status/2110870061418152225 (sticky-note password under keyboard for info@)
- Also: https://x.com/Axel_747/status/2111834354754191715 , https://x.com/JorgDane/status/2106400145768423926 , https://x.com/Naaackers/status/2110818986955026825

### 3. Offboarding leaves M365 / shared-mailbox access live
**Summary:** After someone quits, AD/Entra still active, licenses attached, shared-mailbox delegation untouched, phone still syncing email; mailbox permanently gone after ~30 days if no hold.
**Rough count:** ~5–8 posts (mix of MSP marketing describing a real chore + a few sharper takes).
**What people do today:** Manual multi-portal checklist (block sign-in, revoke sessions, wipe Intune, convert mailbox, reclaim license); some sell automation for it.
**Links:**
- https://x.com/infosprinttech/status/2109981933992357979
- https://x.com/gregnmitchell/status/2111864010715115868
- Also: https://x.com/gotdataa/status/2109888117956067746

### 4. Sole-admin / Authenticator MFA lockouts on M365 or Google
**Summary:** Phone dies or app updates log you out of the only 2FA device → locked out of Global Admin or Workspace; recovery is painful. (Note: search is flooded with YouTube/crypto consumer recovery spam; tiny-office signal is thin.)
**Rough count:** ~3–5 clearly business-relevant posts in window. Broader MFA+lockout+(Microsoft|Google) last ~7 days API: **14** (mostly consumer/YouTube noise).
**What people do today:** Tweet @MicrosoftHelps; set up second Global Admin; backup codes; call support / recovery forms.
**Links:**
- https://x.com/preetamrgupta/status/2104441076975325314 (sole M365 Global Admin, Android motherboard failed, Authenticator gone)
- https://x.com/CertifiedHirsch/status/2111994817987117114 (Microsoft app update logged out phone = primary 2FA → locked out everywhere)

### 5. M365 July 2026 price hike (Business Basic/Standard) — reminders, few fresh anger posts
**Summary:** Business Basic $6→$7, Standard $12.50→$14 (Premium $22 unchanged); existing customers until renewal. Posts in this window are mostly reseller/PSA reminders, not new owner outrage (hike already effective Jul 1, 2026).
**Rough count:** ~4–6 distinct pricing posts; almost no organic Google Workspace price-hike hits in this window.
**What people do today:** Audit seats before renewal; shop reseller pricing; compare Workspace vs M365 on workflow not price.
**Links:**
- https://x.com/Frankly_Alen/status/2111502956478758930
- https://x.com/Mauricio_Cass/status/2108520625740419323

### 6. Tiny-tenant M365 license / send-mail setup pain
**Summary:** Bought Business Basic (even without Teams) and couldn’t send mail / got stuck in domain verification — worst support experience.
**Rough count:** 1–2 clear owner posts (not a large cluster, but real).
**What people do today:** Fight Microsoft support; nonprofit/Basic setup guides.
**Links:**
- https://x.com/Ghost_Pilot_MD/status/2111556837623431593

### 7. Google Shared Drives / permission hell for tools
**Summary:** Company files live on Shared Drives; connectors fail (“Requested entity was not found”) without API flags; workaround is copy to My Drive.
**Rough count:** ~3–4 posts (one multi-company CFO thread).
**What people do today:** Copy files to My Drive; wait for connector fixes; forward to a shared mailbox as an agent inbox.
**Links:**
- https://x.com/KraJan_303/status/2110128984084156892

### 8. “Tool that just does X every week” — weak on X
**Summary:** Lots of SEO/AI “save hours every week” spam; little genuine “is there a tool that does this weekly chore?” from small offices. Closest: MSP audits unused M365 seats weekly; teams still copy data between tools by hand.
**Rough count:** ~0–2 genuine asks; 10+ promotional listicles.
**Links (closest):**
- https://x.com/virtualitgroup/status/2105254361001578630 (MSP: audits M365 tenants every week for dormant seats)
- https://x.com/vanavance95/status/2110831264085475487 (“What do you still copy by hand every week?”)

---

## Posts suggesting someone would pay a local tech / MSP / done-for-you

Sparse and mostly generic (not SMTP/MFA-specific):

| Signal | Link |
|--------|------|
| “A lot of us would pay for that yesterday” — AI back office for family shops | https://x.com/DerekMusial/status/2107154771312595015 |
| “Most small business owners… will happily pay someone who does [done-for-you]” | https://x.com/DorNoyAI/status/2108961430917832990 |
| “I would pay someone to help with this” — Google product transition headache | https://x.com/freeconlon/status/2110906878423347672 |
| Poll: admin job Aussie sole traders would pay to offload | https://x.com/relentless_ops/status/2107314786685894656 |
| Poll: admin task SMB would pay most to never do again | https://x.com/TheCapexDesk/status/2110271974727450954 |
| MSP pricing content implying demand for flat managed IT vs hourly | https://x.com/ValleyCISO/status/2110485804816437605 |

No clear posts in this window of a dental/CPA/clinic owner saying “I’ll pay a local tech to fix scan-to-email / MFA.”

---

## Official dates found

**Microsoft SMTP AUTH Basic auth (verified):**
- Source: [Exchange Team Tech Community](https://techcommunity.microsoft.com/blog/exchange/updated-exchange-online-smtp-auth-basic-authentication-deprecation-timeline/4489835) (Jan 27, updated Jan 29, 2026); MC786329 cited on X.
- Through Dec 2026: behavior unchanged.
- **End of December 2026:** Basic auth for SMTP AUTH **disabled by default** for existing Exchange Online tenants; admins can re-enable.
- New tenants after Dec 2026: Basic SMTP AUTH unavailable by default (OAuth).
- **Final removal date:** Microsoft to announce in **H2 2027**.

**Microsoft 365 commercial pricing (verified):**
- Source: [Microsoft Licensing](https://www.microsoft.com/en-us/licensing/news/2026-m365-packaging-pricing-updates); Reuters Dec 4, 2025.
- **Effective July 1, 2026:** Business Basic $6→$7, Business Standard $12.50→$14, Business Premium unchanged $22 (USD/user/month). Existing customers stay on old price until renewal.

**Google Workspace price changes:** No clear official date or hike cluster in X posts for this window.

**Related news (not a chore, but MSP-relevant):** ConnectWise Cloud Backup (ex-SkyKick) OAuth secret abuse hitting M365 tenants ~Oct 15–17, 2026 — service shut down Oct 17.

---

## Method notes for Automation Mango
- Window: 2026-09-28 → 2026-10-19 via `search_posts_all` + date params.
- Topics searched: SMTP/scan-to-email, MFA lockouts, M365/Workspace pricing, shared mailbox/drive, hire MSP / would pay, weekly tool asks, offboarding.
- X is a weak channel for this ICP right now; Reddit (r/msp, r/smallbusiness, r/sysadmin) likely denser for owner complaints.
