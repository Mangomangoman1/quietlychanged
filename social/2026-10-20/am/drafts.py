import re
P={}
P['r1']="""The $100 is Hulu + Live TV, which went from $89.99 to $99.99 (the no-ads version is $109.99). Plain Hulu is $12.49 with ads, $21.49 without.

If you subscribed before Sep 23, Hulu's help page says the new price hits your first bill on or after Oct 21."""
P['r2']="""Depends which $35 plan. The Disney+, Hulu, ESPN Unlimited bundle ($35.99) is a with-ads plan.

And Disney's price page puts an asterisk on every "No Ads" plan: "Ads will be served in select live and linear programming," plus possible "promotional or sponsored content." """.strip()
P['r3']="""Ad-free Hulu was $11.99 until 2021. It has gone up five times since: $12.99, $14.99, $17.99, $18.99, and now $21.49.

If you subscribed before Sep 23, the new price shows up on your first bill on or after Oct 21."""
P['o1']="""Disney+ and Hulu price hikes reach existing subscribers tomorrow.

Signed up before Sep 23? Your first bill on or after Oct 21 is the new price:
Disney+ Premium $18.99 → $21.49
Hulu Premium $18.99 → $21.49
Hulu + Live TV $89.99 → $99.99

Check your billing date before it renews."""
P['o2']="""Proton just softened a promise in its terms.

Free accounts inactive 12+ months can be deleted, mail, files and passwords included.

Old terms: "You will receive notices" 30, 15 and 7 days before.
Now: "As a mere courtesy," Proton "will aim to."

Log in once a year to stay active.

https://proton.me/legal/terms"""
for k,v in P.items():
    n=len(re.sub(r'https?://\S+','x'*23,v))
    print(k,n)
