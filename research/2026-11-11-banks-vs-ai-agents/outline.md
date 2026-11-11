# Draft outline (do not publish): Banks vs AI agents

Comparison page idea covering Wells Fargo (Nov 24, 2026), Chase, Citi and Schwab.

**Status:** outline only. Saved November 11, 2026. Do not build or deploy this as a guide or change article until it is sourced end-to-end and reviewed.

**Primary starting point:** Erin F. Fonté, Abigail M. Lyle and Michael R. Horne, Hunton Andrews Kurth, "Major banks move to block or limit customer-directed AI agents," *National Law Review*, November 4, 2026. https://natlawreview.com/article/major-banks-move-block-or-limit-customer-directed-ai-agents (fetched November 11, 2026). Also posted on Hunton's site.

**Rule used here:** where the Hunton **table** and the Hunton **prose** disagree, go by the table. Where our own primary-source fetch disagrees with Hunton, note the difference and do not treat Hunton as the last word.

## Table vs prose in the Hunton alert

The table lists four institutions:

| Institution | Date in the table | Action in the table | What remains permitted (table) |
|---|---|---|---|
| JPMorgan Chase | Oct. 13, 2026 (Q3 earnings call) | CEO Jamie Dimon said the bank will not allow outside agents, naming Meta's Muse and Instinct, citing "rogue agents." A spokeswoman said the bank does not permit third parties to obtain customers' credentials and log in on their behalf. "An updated Digital Services Agreement (effective Jan. 1, 2027) provides that a customer who gives an AI agent access authorizes everything that AI agent does and that Chase will rely on the agent's instructions as the customer's own instructions." | Read-only data (e.g., balances) through open banking providers such as Plaid; no money movement or bill pay. No timeline for direct AI agentic access. |
| Charles Schwab | Oct. 16, 2026 | CEO Rick Wurster told Bloomberg the firm blocks unauthorized agents, including Muse, that attempt to move client money 10 to 20 times per week. | Developing controlled connections that allow information access without permitting AI agents to move money; launched an in-house AI assistant "Charley." |
| Citigroup | Oct. 16, 2026 | Citi does not permit "third-party AI agents or assistants to log into a customer's account or transact directly within our digital banking platforms." | Limited, read-only access through certain open banking providers. |
| Wells Fargo | Terms effective Nov. 24, 2026 | No outright block. New Online Access Agreement Section 15 ("Third-Party Artificial Intelligence Agents or Agentic AI") defines an AI agent broadly, states that use is "at your own risk," deems all AI agent-initiated transactions authorized by the customer, disclaims any duty to monitor AI agent activity, and reserves the right to limit or terminate AI agent access at any time. | AI agent use permitted at the customer's sole risk. |

Prose that should **not** override the table:

- The intro says that "in the span of one week" the four banks "announced that they will not permit third-party AI agents to log in to customer accounts using the customer's own credentials." The table does not say that about Wells Fargo. Wells Fargo's row is "No outright block."
- The intro then says: "Four chose a hard block; Wells Fargo instead rewrote its online access terms to put the risk for the customer's use of AI agents on the customer." That counts five postures, or miscounts the four. **Follow the table:** three hard blocks (Chase, Schwab, Citi) plus Wells Fargo's risk-shifting terms.
- The intro's later line is consistent with the table: "None of the four has banned AI outright: each continues to permit customer-authorized, read-only data sharing through open banking connectors, and several are building their own agent tools."

## Where our primary-source fetch differs from the Hunton table (Chase)

Fetched November 11, 2026: Chase Digital Services Agreement, dsa1_la.pdf, last updated October 2026, https://static.chasecdn.com/content/dam/legal-agreements/library/en/dsa1_la/versions/dsa1_la.pdf. A longer dsa_la.pdf at the same library is last updated November 2026 and opens with the same two dated cover changes.

- The PDF cover dates the External AI / automated-tools / data-aggregator **login-credential bar**, and the "you must change those credentials" line, to **October 27, 2026**, not January 1, 2027.
- The PDF cover dates **January 1, 2027** to a different rule: Chase "may require" the mobile app and a Trusted Device, and "may deny access" until the customer complies, unless an accommodation is required by law. The Hunton table does not mention the Trusted Device / mobile-app requirement.
- The "authorizes everything that AI agent does" / "rely on the agent's instructions" language is in the current October 2026 PDF body (the "Consequences of Sharing Login Credentials with Third Parties" list). Hunton's table attributes an updated DSA "effective Jan. 1, 2027" to that authorization language. Our fetch does not show a January 1 effective date on those consequence clauses.

For a published comparison page, quote Chase from the PDF, not from the Hunton date label. The Oct. 13 earnings-call remarks still need a primary source (transcript or a recording) before we quote Dimon; we did not fetch that in this session.

## Proposed page shape

Working title: "Banks vs AI agents: how Chase, Wells Fargo, Citi and Schwab now treat tools that use your login"

Dek: Three large banks say they will not let third-party AI agents sign in with your password. Wells Fargo, starting November 24, 2026, lets them in and puts the risk on you. Chase separately may require its mobile app and a Trusted Device from January 1, 2027.

Section ideas:

1. **The comparison table** (lead with this). Columns: bank; what it does with credential-sharing AI agents; when; whether money movement is allowed via the agent; official or legal-update source. Rows: Chase, Schwab, Citi, Wells Fargo, filled from the Hunton table and, for Chase and Wells Fargo, from agreements we have already fetched.
2. **Two models, not one "ban."** Hard block (Chase / Schwab / Citi, per the table) vs risk shift (Wells Fargo Section 15, already covered on the site, effective Nov 24). Do not write that all four banned login-by-agent.
3. **Chase in more detail**, from the October 2026 DSA: Oct 27 credential bar and mandatory password change if already shared; approved-API path; consequence list if you still facilitate access; Jan 1, 2027 "may require" mobile app + Trusted Device, with the FAQ's limit that tablets, laptops, desktops and iPads are not eligible. Link the change article once it is live.
4. **Wells Fargo in more detail**, from the upcoming Online Access Agreement we already quoted: broad "non-autonomous" AI Agent definition; acts "deemed" yours; "AT YOUR OWN RISK"; duty to notify and keep proof of revocation. Link the Nov 6 article.
5. **Citi and Schwab**, labeled as coming from the Hunton table / cited interviews until we fetch each bank's own terms or a transcript. Do not invent contract language for them.
6. **What still appears allowed at all four**, per the table: customer-authorized, read-only open-banking access (Plaid or similar). Call out the table's Chase qualifier: "no money movement or bill pay."
7. **What a customer can do:** change a shared password; prefer official open-banking connections; for Wells Fargo, read Section 15 before Nov 24; for Chase, be ready to enroll a personal smartphone before Jan 1, 2027.
8. **Sources and gaps:** list what we fetched vs what still needs a primary document (Citi and Schwab agreements; Dimon earnings-call transcript; Schwab/Bloomberg interview).

## Not yet verified, so leave out of any published version

- Any Citi or Schwab contract clause we have not fetched.
- Direct Dimon or Wurster quotations, until we have the transcript or article.
- Hunton's January 1, 2027 effective date for Chase's authorization clauses, which does not match the October 2026 PDF we fetched.
- The Hunton prose claim that all four "will not permit" credential login; the table says otherwise for Wells Fargo.
