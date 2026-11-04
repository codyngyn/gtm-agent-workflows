# Prospecting agent

I built this to prospect into GTM practitioners at AI companies: sellers, sales leaders and peers. The goal of every message is a short conversation to learn about the individual, the team, and the opportunity.

**Started:** Oct 21, 2026. Built in Claude Code.

## The problem

I had a saved list of about 40 alumni working in GTM at AI companies, plus intros coming in. I needed to decide who to reach out to first, write messages specific enough to start a real conversation, and keep track of every thread across LinkedIn, email and text, without automating my LinkedIn account.

## The workflow

| Step | Who does it | Why |
|---|---|---|
| 1. Source | Me: saved lead lists, LinkedIn, intros | I know which relationships matter |
| 2. Enrich | Me, by hand, on a free tool | Fast enough at this volume. No paid data |
| 3. Research | Agent: one specific, sourced hook per person | Reading profiles, posts and podcasts is slow by hand |
| 4. Triage | Agent marks CLEAR or FLAG; I clear flags | A wrong name or company in a cold note ends the conversation |
| 5. Score | Agent rates six factors; a sheet formula ranks; I pick | The ranking is judgment, the math is a formula |
| 6. Draft | Agent drafts, a script checks, I rewrite and send | My voice and my account. The agent gives me a starting point |
| 7. Log | Agent logs what I report as sent and checks for replies | Record-keeping I would otherwise skip |

A Google Sheet serves as the CRM. A human sends every message.

## The agents

Five subagent definitions are in [`.claude/agents/prospecting/`](../.claude/agents/prospecting/) at the repo root, so Claude Code finds them from any session opened on the repo: `researcher`, `triager`, `scorer`, `drafter` and `logger`. Each file lists its rules and what it reads and writes. They all use one model, with effort set by how much judgment the step needs (high for research, triage and drafting, low for logging).

**How it runs:** in Claude Code, with connectors for web search, Google Sheets, Gmail and meeting notes. It started as a Claude conversation with the same connectors and moved into Claude Code, where this repo was built. Each run is logged in [`runs/`](../runs/).

[`eval/checks.py`](eval/checks.py) is the deterministic check script that ran on drafts from Oct 28. It flags messages over 300 characters, links in connection notes, "applying" in a peer note, em dashes, stock phrases, apologies and stacked asks, and it measures how much I rewrote each draft.

## Results

Outcome numbers are not published here. I share them in conversation. [`scripts/funnel.py`](../scripts/funnel.py) regenerates them from tracker exports, so a number is counted the same way every time I quote it.

## Examples

Two anonymized messages, each shown version by version with the check results:

1. [The checks caught a rule break; I caught a wrong fact](examples/01-rule-and-fact-fix.md)
2. [A draft passed every check and still had an unverified claim](examples/02-unverified-claim.md)

## Lessons

- **Rules catch rule breaks; only a source catches a wrong fact.** The script caught every agent first draft that said "applying." It could not catch a wrong employer from a search tool or an unverified award. Those took me, or a grader that checks accuracy.
- **Warm paths get their own factor.** Referrals, intros and prior relationships moved first, so the score weights them.
- **The agent breaks its own rules.** "No specific hook means FLAG" was agreed and then skipped on most cold rows. Agreeing to a rule doesn't enforce it. Enforcement has to be a check.

More in [DECISIONS.md](DECISIONS.md) (what I decided vs. what the agent proposed) and [RETRO.md](RETRO.md) (what worked, where the agent failed, what I'd change).

## Not built yet

A separate-model grader (the rubric exists), outcome analysis by hook and ask, a daily scheduled run, and phone enrichment.
