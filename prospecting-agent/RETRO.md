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

## Update, Nov 4

- **A source check caught my own errors.** The researcher found four wrong details in my description of a new contact before any reached a draft.
- **Triage only modeled hiring targets.** A contact I added on purpose was flagged. I added two categories: event contacts, and people who left a GTM role at a target company in the last 12 months.
- **The privacy scan only knew contact names.** It now also blocks employers, events, schools, cities and people named in notes, from a gitignored list.
- **Outcome metrics left the repo.** They are regenerated from the tracker for live conversations instead.
