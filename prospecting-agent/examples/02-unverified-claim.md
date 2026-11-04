# Example 2: A draft passed every check and still had an unverified claim

LinkedIn connection note to a fellow alum, an account director at a target company. Names, companies and awards are replaced with placeholders.

| Version | Author | Checks | What changed |
|---|---|---|---|
| v0 | agent | Says applying | First draft |
| v1 | agent | Pass | Hook changed to two sales awards from her profile |
| v2 | me | Pass | I dropped the awards because I couldn't verify them, and the hook went generic |
| v3 | agent | Pass | Specificity restored with a fact that was verified |

**v1 (agent)**
> Hi [name], fellow [school] alum! [Award] to [award] at [prior company] is the ramp I'm aiming for. I'm breaking into sales after corp dev/VC (backed Cohere at Cisco) and GTM reps at two AI startups. Saw [target company] is hiring [role]s in [city]. What makes one stand out?

**v2 (me)**
> Hi [name], [school] alum reaching out. Your path breaking into being a top performer in sales is the ramp I'm aiming for. I'm breaking into sales after corp dev/VC (backed Cohere at Cisco) and GTM reps at two AI startups. Saw [target company] is hiring [role]s in [city]. What makes one stand out?

**v3 (agent)**
> Hi [name], [school] alum reaching out. Your climb to top performer at [prior company] and now [target company] is the ramp I'm aiming for. I'm breaking into sales after corp dev/VC (backed Cohere at Cisco) and GTM reps at two AI startups. Saw [target company] is hiring [role]s in [city]. What makes one stand out?

The message went out Oct 28. The exact sent text was not logged in the Drafts tab, so the final version is missing.

## What it shows

- Rule checks can't judge truth. v1 passed every check and still contained a claim nobody had verified.
- The correction went both ways. I removed the claim but made the hook generic. The agent then restored the specificity using only a verified fact.
- This is why the rubric has an accuracy score that caps any draft containing an unverified fact. That rubric was written but never run.
