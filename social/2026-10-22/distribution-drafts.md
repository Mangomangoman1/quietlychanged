# Distribution drafts, 2026-10-22 (Fitbit Web API turned off Oct 30; linked apps must be re-approved in Google Health)
Article (live, HTTP 200, not changed today; it already covers MyFitnessPal, Personify Health, UMN, Strava, Fitabase's Nov 30 window and how to reconnect): https://quietlychanged.com/changes/2026-10-22-fitbit-third-party-apps-stop-getting-your-fitbit-data-oct-30-unless-you-reconne/
Primary source (re-checked Oct 22 ~3:05 PM MT via WebFetch, page "Last updated 2026-09-29"): https://developers.google.com/health/about
- "October 30, 2026 (API turn-off): The Fitbit Web API will be turned off and will no longer function or sync data to or from Fitbit users."
- Migration guide (https://developers.google.com/health/migration/data-access): "Fitbit users must re-consent to your new integration ... It is not possible for access tokens and refresh tokens to be transferred"
- Google Health Help (https://support.google.com/googlehealth/answer/14236613): reconnect before Oct 30; Google Health Support "can't restore or fix your broken connection."
Coverage (Oct 22, 3 PM MT): still none on the connected-app cutoff. WebSearch returns only Google's developer pages, the Sep 28 community extension post and a Terra developer blog; HN Algolia has no story on it (latest Fitbit stories are the Fitbit Edge and Luffu).
Why this one: 8-day deadline, affects ordinary people (MyFitnessPal, employer wellness rewards, research studies), no news coverage. Picked over ipl.org (already distributed Oct 21 on HN, Bluesky, Reddit, Tedium).
X: the Fitbit X original is held for the Oct 23 original slot (social/2026-10-22/deepdive/x-posts-deepdive.md), so nothing on X today. All drafts sign only as QuietlyChanged.

## 1. Hacker News
Title: Google turns off the Fitbit Web API on Oct 30; users must re-consent every app
URL (original source): https://developers.google.com/health/about
Optional first comment (only if it gets traction):
The user-facing part is in the migration guide: tokens can't be carried over, so every person who linked Fitbit to another app has to re-approve it through Google OAuth (https://developers.google.com/health/migration/data-access). Google's help page says that after Oct 30 support "can't restore or fix your broken connection" (https://support.google.com/googlehealth/answer/14236613). MyFitnessPal is telling people who already reconnected through Google's prompt that they'll have to do it again inside MyFitnessPal, and it lists a known step-sync issue. Employer wellness programs (Personify Health, UMN's HR office) are warning that rewards stop syncing on the 30th. Fitabase says research participants can still reconnect through Nov 30. Data already in a user's Google Health account isn't deleted.

## 2. Bluesky (quietlychanged.bsky.social), image: social/2026-10-22/deepdive/fitbit-api-off-oct30.png
Alt text: Timeline: Sep 30 support ends, Oct 30 Fitbit Web API turned off, Nov 30 last reconnect window for studies. Quote from Google: "will no longer function or sync data to or from Fitbit users."
Post (under 300 chars):
Fitbit linked to MyFitnessPal, a workplace wellness program or a study? Google turns off the old Fitbit Web API Oct 30. Linked apps stop syncing unless you re-approve them in Google Health, and Google says it can't fix broken connections after that.
https://quietlychanged.com/changes/2026-10-22-fitbit-third-party-apps-stop-getting-your-fitbit-data-oct-30-unless-you-reconne/

## 3. Reddit r/fitbit (text post, primary links only, NO quietlychanged.com link)
Open https://old.reddit.com/r/fitbit/about/rules in the signed-in u/QuietlyChanged browser first (the box couldn't fetch the rules). Skip if it bans PSAs or news, requires approval, or the account is too new. Search the sub for "Web API" or "reconnect" first; if a recent thread already covers Oct 30, skip rather than duplicate. Use a "News"/"PSA"/"Discussion" flair if required. Don't message mods.
Title: PSA: Apps linked to your Fitbit (MyFitnessPal, wellness programs, studies) stop syncing Oct 30 unless you reconnect them in Google Health
Body:
Google is turning off the old Fitbit Web API on October 30. From Google's developer page (https://developers.google.com/health/about): "The Fitbit Web API will be turned off and will no longer function or sync data to or from Fitbit users."

Old connections can't be carried over, so every linked app has to be approved again under your Google account (https://developers.google.com/health/migration/data-access). Google's help page says to reconnect before Oct 30, and that afterward support "can't restore or fix your broken connection": https://support.google.com/googlehealth/answer/14236613

How to check: Google Health app, Connections (top left), Partner Apps, and look under "Needs Action." Some apps say "Reconnect in partner app," which means you do it from inside that app.

Things worth knowing:
- MyFitnessPal says that even if you already reconnected through Google's prompt, you may need to do it again when MyFitnessPal asks, and it lists a known issue with steps/exercise not syncing (see MyFitnessPal Help, "Reconnecting Your Google Health (formerly Fitbit) Integration").
- If an employer or insurer wellness program pays points for steps, check that new days show up after you reconnect.
- Apple Health and Health Connect links aren't affected, per Google's help page.
- Your data already in Google Health isn't deleted.

Posting because I haven't seen this in the news and the deadline is next week.

## 4. Pitch email: 9to5Google news tips
To: gtips@9to5g.com (listed under "News Tips" on https://9to5google.com/contact/; Ben Schoon is listed there as Senior Editor)
From: quietlychangedbiz@gmail.com
Subject: Tip: Fitbit-linked apps (MyFitnessPal, wellness programs) stop syncing Oct 30 unless users re-approve them
Body:
Hi 9to5Google team,

A tip with a deadline next week that we haven't seen covered anywhere.

Google turns off the legacy Fitbit Web API on October 30 (https://developers.google.com/health/about): it "will no longer function or sync data to or from Fitbit users." Tokens can't be moved to the Google Health API, so every user who linked Fitbit to another app has to re-consent (https://developers.google.com/health/migration/data-access). Google's help page tells users to reconnect before Oct 30 and says that afterward support "can't restore or fix your broken connection" (https://support.google.com/googlehealth/answer/14236613).

What that looks like for people:
- MyFitnessPal's help article (updated Oct 19) says members who already reconnected through Google's prompt still have to reconnect again inside MyFitnessPal, and lists a known step and exercise sync issue as "Investigating."
- Employer wellness platforms like Personify Health, and the University of Minnesota's HR office (Oct 8), are warning that reward points stop syncing on the 30th.
- Strava's Google Health integration changes: unless users update it, only GPS bikes, runs, hikes and walks keep syncing.
- Google gave developers a one-time 30-day extension on Sep 28 (https://support.google.com/googlehealth/thread/470464840), so this date is final. Fitabase says research participants can reconnect through Nov 30.

The app's rename to Google Health got covered around Oct 12, but not this cutoff for connected apps. Our write-up, with every source linked: https://quietlychanged.com/changes/2026-10-22-fitbit-third-party-apps-stop-getting-your-fitbit-data-oct-30-unless-you-reconne/

QuietlyChanged tracks pricing, terms and shutdown notices at popular services every day.

QuietlyChanged

## Skipped
- X (Fitbit original held for the Oct 23 slot; ipl.org went out today).
- r/MyFitnessPal (one subreddit per story; revisit only if r/fitbit rules forbid it).
- More pitches (one pitch a day).
- Article rebuild/IndexNow: no article change today, so nothing to rebuild or ping.
