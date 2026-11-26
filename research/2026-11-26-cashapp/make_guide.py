import json
TOS="https://cash.app/legal/us/en-us/tos"
BLK="https://cash.app/help/us/en-us/110812-block-merchant-transactions"
DSP="https://cash.app/help/us/en-us/309115-dispute-a-cash-app-card-transaction"
LCK="https://cash.app/help/us/en-us/309112-temporarily-lock-my-card"
REG="https://www.ecfr.gov/current/title-12/chapter-X/part-1005/subpart-A/section-1005.10"
C1="2026-11-26-cash-app-cash-app-now-lets-you-stop-subscription-charges-on-your-cash-app-card"
g={
"title":"How to stop a subscription charge on your Cash App Card (Nov 2026): block the merchant 3 business days ahead",
"desc":"Cash App's Nov 25, 2026 terms give you a right to stop recurring Cash App Card charges. How to block a merchant in the app, the 3-business-day deadline, why blocking isn't cancelling, ACH debits, locking the card, and disputes. Quoted from Cash App's own pages.",
"dek":"Until this week, Cash App's terms said you had \"No Right to Stop Payment\" on Cash App Card transactions. The version dated November 25, 2026 says the opposite for subscriptions and other automatic charges. Here is exactly how to stop one, the deadline that decides whether Cash App is on the hook, and what blocking a merchant does not do, quoted from Cash App's terms and help center.",
"published":"2026-11-26","modified":"2026-11-26",
"services":["Cash App"],"changes":[C1],
"body":[
{"h":"The short version"},
{"ul":[
"**You can now stop recurring Cash App Card charges.** The terms say: \"You have the right to stop payment on preauthorized transfers originated with your Cash App Card.\" Preauthorized means \"automatic payments, subscriptions, or recurring payments\" a merchant charges to a card it has stored. We logged the change in [today's report](../../changes/"+C1+"/).",
"**The deadline is 3 business days.** Cash App \"must receive your request at least three (3) Business Days before the scheduled date of the transfer.\" Ask later and Cash App will try, but isn't responsible if the charge goes through.",
"**Fastest way:** open Cash App, go to the **Activity** tab, open a past charge from the business, tap the business's icon, and select **Block/unblock**.",
"**Blocking isn't cancelling.** \"Blocking a merchant does not automatically cancel underlying subscriptions or agreements with the merchant.\" Cancel with the business too, or you may still owe it.",
"**Already charged?** That's a dispute, not a stop payment: file it in the app within 60 days of the statement that shows the charge."]},
{"h":"What changed on November 25, 2026"},
{"table":{"headers":["","Before (terms in our Nov 25 snapshot)","Now (terms \"Last Updated: November 25, 2026\")"],"rows":[
["Section heading","\"6. No Right to Stop Payment\"","\"6. Right to Stop Payment\""],
["Rule","\"You do not have the right to stop payment on a transaction originated with your Cash App Card.\"","\"You have the right to stop payment on preauthorized transfers originated with your Cash App Card.\""],
["How","n/a","Block the merchant in the Activity tab, write to Cash App Support in the app, or call (800) 969-1940"],
["Deadline","n/a","At least three business days before the scheduled charge"],
["If Cash App misses it","n/a","\"we will be liable for your unrecoverable losses\" (if you asked in time through merchant blocking)"]]}},
{"p":"The new wording tracks the federal rule for debit-style accounts. Regulation E, 12 CFR 1005.10(c), says a consumer \"may stop payment of a preauthorized electronic fund transfer from the consumer's account by notifying the financial institution orally or in writing at least three business days before the scheduled date of the transfer.\" The same rule lets the institution ask for written confirmation within 14 days of a phone request, which Cash App's terms now also say."},
{"h":"How to stop a recurring Cash App Card charge, step by step"},
{"p":"Cash App's help article [Blocking a Business]("+BLK+") gives these steps:"},
{"ol":[
"Go to the **Activity** tab (clock icon).",
"Choose a transaction from the business you want to block.",
"Select the **business's icon** to open its profile. Cash App's tip: tap the icon or name \"at the top of the transaction details screen, not the transaction row itself.\"",
"Select **Block/unblock**.",
"Check the **Card** tab, where you \"can view and manage a list of your recently unblocked and currently blocked businesses.\"",
"Cancel the subscription with the business itself (see below)."]},
{"p":"Do it at least three business days before the next charge date. Cash App's terms define a Business Day as \"all days of the week except Saturdays, Sundays, and federal holidays,\" so for a charge due on a Monday, ask by the Wednesday before, and a day earlier if a federal holiday such as Thanksgiving falls in between."},
{"p":"Two limits from the help article: \"You must have a previous transaction with a business to follow the steps above,\" and blocking applies to the business, not one charge: it \"will result in blocking all future Cash App Card transactions from that merchant,\" per the terms. Blocking \"will not prevent you from receiving a refund.\""},
{"h":"If you don't see the Block option"},
{"ul":[
"Close and reopen Cash App, then try again, tapping the business name at the top of the transaction details.",
"Look for the business in the blocked list on the **Card** tab.",
"Remove its access: profile icon → **Linked apps and businesses** → find the business → **Remove**. Cash App warns that \"Removing access may not stop future charges if your card number is stored directly with the business.\"",
"**Apple, Google Play and Amazon** charges may not show a business profile. Cancel those in the store: on iPhone, Settings → your name → Subscriptions; in the Google Play Store, profile → Payments & subscriptions → Subscriptions.",
"Otherwise use the other two routes in the terms: \"Write us using the Cash App Support feature available in Cash App\" or \"Call us at (800) 969-1940.\" If you call, Cash App \"may also require you to put your request in writing and if you fail to do so within 14 days, the stop payment may be removed.\" Writing through in-app Support from the start avoids that step."]},
{"h":"Blocking a merchant doesn't cancel the subscription"},
{"quote":"Blocking a merchant does not automatically cancel underlying subscriptions or agreements with the merchant. If you have questions about your subscriptions with any blocked merchant, contact the merchant directly.","cite":"Cash App Terms of Service, Cash App Card section 6, Last Updated November 25, 2026","url":TOS},
{"p":"The help article says the same: blocking \"does not cancel existing subscriptions, recurring charges, or outstanding account balances.\" In practice, a business whose charge is declined may suspend your account, retry, try another card on file, or send the balance to collections. So the order that works best is: cancel with the business (and keep the confirmation email or screenshot), then block it in Cash App as a backstop against a charge the business makes anyway."},
{"h":"Card charges vs. ACH debits from your Cash App balance"},
{"p":"The new right covers charges on your **Cash App Card**. Some bills instead pull money with your Cash App account and routing numbers (an ACH debit). Those work differently:"},
{"table":{"headers":["","Cash App Card charge","ACH debit (account + routing number)"],"rows":[
["How to stop it","Block the business in the Activity tab, or in-app Support, or (800) 969-1940","Ask Cash App Support for \"merchant blocking\" (in-app Support or phone); the help article says ACH blocks \"can’t be managed directly in the app\""],
["Deadline","3 business days before the charge","3 business days before the charge"],
["Needs a past charge?","Yes, to block from the Activity tab","Yes: \"Merchant blocking is only available for existing merchants who have previously made an ACH debit from your Cash App account\""],
["Cancels the subscription?","No","No: Cash App recommends you \"contact the merchant directly to cancel any services\""]]}},
{"h":"Lock Card is not a stop payment"},
{"p":"Locking the card (Money tab → tap the card → lock icon → **Lock card**, or Money → Lock Card at cash.app/account) stops new charges from everyone, not just one business. It doesn't stop charges already in progress: the terms say it \"will not prevent processing of pending transactions initiated prior to disabling your Cash App Card,\" and the help center says \"Locking your card does not prevent pending charges from completing.\" Locking works if you've lost the card or want to stop everything for a while; blocking the one business is better for a single subscription you still want to cancel cleanly."},
{"h":"Already charged? File a dispute"},
{"p":"A stop payment only works before a charge. If a subscription already charged you after you cancelled, or you don't recognize a charge, Cash App's [dispute article]("+DSP+") says:"},
{"ol":[
"Select the profile icon, then **Support**.",
"Choose **Cash App Card → Dispute a purchase**.",
"Select **Start a dispute**. You can also call 1 (800) 969-1940, which the article lists as available daily, 8 AM to 9:30 PM Eastern."]},
{"ul":[
"**Deadline:** \"Transactions should be disputed within 60 days of you receiving the monthly statement on which the transaction appears.\"",
"**Timeline:** an update within 10 business days; if the investigation isn't done by then, Cash App gives \"a provisional credit\" while it continues. The full investigation \"may take up to 45 days\" (the terms allow up to 90 days for new accounts and point-of-sale transactions).",
"**Exception:** provisional credits \"do not include disputes concerning goods and services not received or not as described.\"",
"**Appeals:** you can appeal a denial \"within 60 days of the dispute being denied\"; appeal decisions are final."]},
{"h":"The new Bills and Subscriptions feature"},
{"p":"The same November 25 terms add section XXV, \"Bills and Subscriptions\": an optional tool to \"view and manage recurring third-party merchant bills and subscriptions connected to your Cash App Card.\" It's free (\"We do not charge a fee\"), but read what you hand over before turning it on:"},
{"ul":[
"You may need to give a third-party vendor your \"usernames, passwords, PIN numbers, and other related information\" for the merchant accounts you link.",
"You grant Cash App and the vendor \"a limited power of attorney\" to act in those accounts, including \"canceling Linked Subscriptions.\"",
"Cash App says it doesn't guarantee coverage: the tool \"may not support all external subscriptions,\" connections \"may be lost,\" and it's \"solely your responsibility\" to fix them.",
"Estimated bill amounts \"may not take into account\" other Cash App activity such as Auto Reload or Afterpay."]},
{"p":"You don't need this feature to stop a payment. The stop-payment right in section 6 works on its own through merchant blocking."},
{"h":"Checklist"},
{"ol":[
"Find the next charge date for the subscription (the business's account page or your past Cash App Activity).",
"Cancel with the business and save the confirmation.",
"At least 3 business days before the next charge: Activity → the business's past charge → business icon → **Block/unblock**.",
"Confirm the business is on the blocked list in the **Card** tab.",
"If there's no block option: try **Linked apps and businesses → Remove**, cancel app-store subscriptions in the store, or write to in-app Support.",
"If it charges you anyway: Support → Cash App Card → **Dispute a purchase**, within 60 days of the statement."]}
],
"sources":[
["Cash App Terms of Service, Last Updated November 25, 2026 (Cash App Card section 6, Right to Stop Payment; section XII, disputes; section XXV, Bills and Subscriptions)",TOS],
["Cash App Help: Blocking a Business (checked November 26, 2026)",BLK],
["Cash App Help: Dispute a Cash App Card Transaction (checked November 26, 2026)",DSP],
["Cash App Help: Temporarily Lock my Card (checked November 26, 2026)",LCK],
["12 CFR 1005.10(c), Regulation E: consumer's right to stop payment (eCFR)",REG]]}
json.dump(g,open('../../guides/how-to-stop-cash-app-card-subscription-payments.json','w'),ensure_ascii=False,indent=1)
print("ok")
