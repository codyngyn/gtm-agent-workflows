# Example 1: The checks caught a rule break; I caught a wrong fact

LinkedIn connection note to a fellow alum in sales at a target company. Limit: 300 characters. The names, companies and the person's career path are replaced with placeholders.

| Version | Author | Checks (`eval/checks.py`) | What changed |
|---|---|---|---|
| v0 | agent | Says applying; stock phrase | First draft |
| v1 | agent | Stock phrase | I fixed a wrong employer that came from search, and the "applying" line |
| v2 | agent | Pass | Hook changed to her early start in [role] |
| v3 | me | "standout" as one word | I switched the hook to her run across companies and wrote it in my voice |
| sent | me | Pass | Length and spelling fixes. 76% different from v0 |

**v0 (agent)**
> Hi [name], fellow [school] alum here. Your path from [company] and [company] into [target company]'s [team] caught my eye. I'm applying to [target company]'s [city] [role] role after GTM reps at two AI-native startups. Where does a strong [role] add the most judgment for your team: inbound, qualifying or outbound?

**v2 (agent)**
> Hi [name], fellow [school] alum here. Your path from [role] to [four companies] and now [target company] is the arc I'm hoping to build. I'm breaking into sales after corp dev/VC (backed Cohere at Cisco) and GTM reps at two AI startups. Saw [target company] is hiring [city] [role]s. What made you stand out early?

**Sent (me)**
> Hi [name], [school] alum here. Your run across [four companies] and now [target company] is one I want to emulate. I'm breaking into sales after corp dev/VC (backed Cohere at Cisco) and GTM reps at two AI startups. Saw [target company] is hiring [role]s in [city]. What separates [role]s who stand out?

## What it shows

- The deterministic checks caught the rule break and the stock phrase. Neither needed a model to judge.
- The checks could not catch the wrong employer, which came from a search tool. I caught it against her profile. Since then, company names come from Sales Navigator, not from search results.
- I overrode a draft that passed every check. Whether I improved it is debatable: my own grader rubric would rate her early-career start as the more specific hook.
