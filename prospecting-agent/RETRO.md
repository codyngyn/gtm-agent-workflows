# Retro (Oct 21 to Nov 1, 2026)

## What worked

- **Warm paths.** Treating each intro as a reason to ask for the next intro did more than any message tweak.
- **A human sends everything.** It kept me reading every message, and I rewrote most of each first draft before it went out.
- **Deterministic checks.** A 60-line script caught rule breaks every time, including in my own drafts. The agent drafted "I'm applying" in its first drafts the day after that rule was set. The script caught every one.
- **Flag, never guess.** Contacts the agent couldn't verify were held back. Several were enrichment mismatches: the wrong person, or the wrong company.

## Where the agent failed

- **Wrong facts from search.** A search tool returned a parent company as a contact's employer, twice. I caught it against the profile. The fix is a rule: company names come from Sales Navigator.
- **Unverified claims.** A draft cited awards nobody had verified, and it passed every check. Rule checks can't judge truth.
- **Misread instructions.** The agent turned "two new touches per day" into "two active threads," cut my venture background as a weakness, and logged a send when I had said "going to send."
- **Rules it set for itself and then skipped.** "No hook means FLAG" was agreed on Oct 27. In practice, most cold rows kept a "fellow alum" placeholder. That left the cold notes with generic hooks.
- **The checks have a known false positive.** An ask written as a statement is flagged as no ask.

## What I'd change

1. **Fix cold before sending more of it.** Enforce the FLAG rule: no specific hook, no send. A shared school is not a hook.
2. **Run the grader.** The rubric (hook specificity, accuracy, voice, ask) is written but never ran. A separate model should score accuracy, because that is where the checks are blind.
3. **Log sent text at send time.** Several touches were logged from the last draft. A reply-rate analysis by hook is only as good as that log.
4. **Port to Claude Code and schedule it.** The port is done. Next is the daily morning run: read the tracker, check replies, queue the day's drafts.

## Planned, not built

A separate-model grader, outcome analysis by hook and ask, a daily scheduled run, and phone enrichment.

## Retro: making it public (Nov 1 to 3, 2026)

### What worked

- **Checking my claims, not just the agent's.** The researcher checked my own one-line description of a new contact against sources and found four wrong details. None reached a draft.
- **The privacy scan caught the agent too.** It blocked an email address the agent had written into a config file. Rules that apply to every author are the point.
- **Reading back every write.** Each subagent reports what it changed. I treated that report as a claim and checked the sheet before moving on. Every report matched, which is what made the next step safe to run.
- **Regenerate before you delete.** I removed the results file only after a script reproduced every number in it from the tracker. Deleting stopped being a loss.

### Where it failed

- **Rules lagged behind the goal.** Triage only modeled hiring targets, so it flagged a contact I had added on purpose. I wrote two new categories instead of overriding the flag by hand.
- **The agent shipped a bug its own test caught.** The first version of the link check missed links because of an escaping mistake. Testing it on four sample notes caught it before it ran on real drafts.
- **Deleting a file doesn't delete its history.** Removed files stayed readable in old commits. A merged pull request keeps its commits even after a force-push. Getting a clean public record took a fresh repo.
- **The framing changed three times in one day.** Each rewrite of the README was right, but the scoring rules still weight the factors from the first framing. Descriptions and rules drifted apart.

### What I'd change

1. **Decide what's public before the first commit.** Outcome metrics, identifying details and commit attribution are all easier to leave out than to remove.
2. **Write the goal first, then the rules.** The scoring weights should follow from the stated goal, and a check should flag when they don't.
3. **Keep one list of identifying terms from day one.** Employers, events, schools and people named in notes identify a contact as surely as a name does.
