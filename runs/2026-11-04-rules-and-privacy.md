# 2026-11-04: triage categories, privacy scan, link rule, metrics out

Environment: Claude Code, cloud session, with Google Sheets, Gmail, Granola, Exa and TinyFish connectors. Each subagent ran with the model and effort in its own file's frontmatter.
Subagents run: `triager`, then `scorer`, on one contact.
Input: five changes I asked for. Cover event contacts and recent alumni of target companies in triage. Extend the privacy scan. Set a rule for links. Take outcome metrics out of the repo. Describe the build as built in Claude Code.

## What happened

- Contacts added: 0. Re-triaged: 1, FLAG to CLEAR under the new categories. I authorized the re-triage, since the rule says only I clear a flag. Scored: 1, ranked near the middle of the list.
- Touches logged: 0. Drafts written: 0.
- checks.py: added a check for links in connection notes. Tested on 4 samples. It flagged the 2 connection notes with links, and passed a note that only offers a link and an InMail with a link. The first test missed a link because I had escaped the pattern wrong; fixed and re-run.
- Privacy scan: added a second gitignored input, `data/terms.txt`. Tested on a planted file. It caught 4 of 4 identifying terms, passed lowercase and plural lookalikes, and refused to run when the file was missing. 0 blocking hits on the repo.
- `scripts/funnel.py`: new. It reproduced every mechanically counted number in the old results file, from a reconstruction of the tracker. It has not yet run on a real export. Calls held and hiring stages live in free-text notes, so the script leaves those to a hand count.
- Subagent cost, from the harness usage line: `triager` 85,075 tokens, 9 tool calls, about 52 seconds. `scorer` 93,345 tokens, 12 tool calls, about 63 seconds.
- I read back every cell each subagent wrote. All matched its report.

## What broke or surprised me

1. **Edited agent files may not reach a running session.** Claude Code may load agent definitions when a session starts. I told each subagent to read its file from disk before acting. I did not test whether that was necessary.
2. **The triager listed the gaps in its own new rules.** I fixed two: the 24-month window now counts from when the person left, and an event contact is re-triaged the day after the event. Still open: attending the same event is treated as meeting the person; nothing checks for a do-not-message request directly; non-target companies fall to the default channel rule.
3. **The scorer's reasons said "coaches" where the source says "teaches."** It's only in the tracker, but it's the wording drift the researcher was built to catch.
4. **`logger` still has not run in Claude Code.** Nothing was sent.

## What I changed afterward

- `triager.md`: two CLEAR categories, event contact and target-company alum, written to Persona. `scorer.md`: how to rate them.
- `drafter.md`: no links in connection notes; link the website elsewhere. `checks.py`: the matching check.
- `privacy_scan.py` and the pre-commit hook: the terms file. Root `CLAUDE.md`: the export step and the no-metrics rule.
- Removed the results file and every outcome number from the READMEs, the retro, the decisions log and one example. Removed the per-agent status lines; the run logs keep the dated detail.
- Later the same day: shortened the target-company alum window from 24 months to 12. The one contact in that category left within 12 months, so his triage is unchanged.
