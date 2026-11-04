# 2026-11-03: first Claude Code run of the subagents

Environment: Claude Code, cloud session, with Google Sheets, Gmail, Granola, Exa and TinyFish connectors. Each subagent ran with the model and effort in its own file's frontmatter. The main session's model is not recorded here.
Subagents run: `researcher`, `triager`, `drafter`, one contact each, in that order. Not run: `scorer`, `logger`.
Input: one new contact, added by me to the tracker, plus two links (a profile and a post). I gave a one-line description: a teacher at an event I attend this week, who moved into sales from a non-sales career and later led sales at a target company.

This is not yet an end-to-end run. Three of the five agents ran. The other two had nothing to do, for the reason in the third item under "What broke or surprised me."

## Setup

- Set `core.hooksPath` to `.githooks`, so the privacy hook runs on commit.
- Exported contact names from the tracker to `data/names.txt` (65 names, then 66 after the new contact was added). The file is gitignored.
- Scanned all 8 commits in git history for contact names, emails, profile URLs, phone numbers and target company names with the same patterns the hook uses. No hits.

## What happened

- Contacts added: 1 (CLEAR 0, FLAG 1)
- Touches logged: 0. Nothing was sent, so `logger` had nothing to record.
- Drafts written by agent: 5 versions for 4 contacts.
  - 2 versions (1 contact) by the `drafter` subagent.
  - 3 versions (3 contacts) by the main session, following `drafter.md` without launching the subagent. These came before the subagent run.
  - Edited by me before sending: not measured yet. None has been sent.
- checks.py results: 1 failure in the 5 logged versions: over 300 characters (320), in the subagent's first version. Its second version passed at 285. The 3 main-session drafts passed. Separately, 5 candidate rewrites of earlier messages were tested and not logged to the tracker; 1 was over the limit (303) and I trimmed it to 298.
- Subagent cost, counted from the harness usage line each one returned: `researcher` 119,133 tokens, 19 tool calls, about 99 seconds. `triager` 82,033 tokens, 8 tool calls, about 32 seconds. `drafter` 96,090 tokens, 15 tool calls, about 83 seconds.
- Checking the work: I read back every cell a subagent wrote. All three write-backs matched what the subagent reported.

## What broke or surprised me

1. **Four of my own claims about the contact did not match sources.** The researcher checked my description against public sources before writing. My version overstated a title, credited a named person for a break that the source credits to a company, skipped a job between school and sales, and said "coach" where the source says "teach." None reached a draft. This is the same lesson as example 2: a source catches what a rule check cannot.
2. **The triager flagged a contact I added on purpose.** The contact is an event teacher and former sales leader at a target company, now at a venture firm. Two rules fired: not at a target company, and role unrelated to the roles I want. The flag follows the rules as written. The rules only model hiring targets, so there is no category for event contacts, connectors or alumni of target companies. I have not cleared the flag. Whether to change the rules or clear this row is my call and is still open.
3. **The flag stopped the pipeline.** `scorer` rates only CLEAR contacts, and `logger` needs a send. So neither ran, and the first run exercised 3 of 5 steps.
4. **The drafter's first version broke the 300 character limit.** The check caught it, the drafter cut three clauses, and the second version passed. My instructions told it to leave out anything unverified, and it did. The checks pass this note, but they only test form. Nothing in them verifies a claim.
5. **A subagent's report is only its own account.** I treated each hand-back as unverified until the sheet read-back matched.

## What I changed afterward

- Updated the status line in the `researcher`, `triager` and `drafter` files to say each ran once on Nov 3. `scorer` and `logger` still say they have not run.
- Updated "How it actually ran" in `prospecting-agent/CLAUDE.md` and the README, and added a dated update to `RETRO.md` and a note to `DECISIONS.md`.
- Not changed: the triage rules, the checks, and the flag on the contact. Those wait for my decision.
