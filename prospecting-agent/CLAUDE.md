# Prospecting agent

This system researches, prioritizes and drafts outreach to GTM practitioners at AI companies, with one goal per message: a short conversation to learn about the individual, the team, and the opportunity. The person is Cody, who is exploring GTM opportunities at AI companies. A Google Sheet serves as the CRM. A human sends every message.

## How it actually ran

It started on Oct 21, 2026 as a Claude conversation with connectors and a file workspace, and moved into Claude Code, where this repo was built and where it runs now. Each step's instructions are a subagent file in `.claude/agents/prospecting/` at the repo root. Runs are logged in `runs/`.

## Steps

| Step | Who does it | Subagent |
|---|---|---|
| 1. Source | Cody: Sales Navigator saved lists, LinkedIn feed, intros. The agent adds people from web searches when asked. | none |
| 2. Enrich | Cody, by hand: free Apollo tier for emails. No phone numbers. | none |
| 3. Research | Agent: one specific, sourced hook per contact | `researcher` |
| 4. Triage | Agent proposes CLEAR or FLAG; Cody clears flags | `triager` |
| 5. Score | Agent rates six factors 0 to 5; a spreadsheet formula computes the score; Cody picks the day's sends | `scorer` |
| 6. Draft | Agent drafts; `prospecting-agent/eval/checks.py` runs deterministic checks; Cody rewrites and sends | `drafter` |
| 7. Log | Agent logs what Cody reports as sent and checks Gmail and meeting notes for replies | `logger` |

All subagents use one model. Effort varies by how much judgment a step needs: high for research, triage and drafting, medium for scoring, low for logging. That mapping applies Cody's stated rule ("low for low-judgment tasks, medium to high for judgment tasks"). Effort was set per session in the chat, not recorded per step.

## When Cody adds a contact

Cody gives a name, a company or a LinkedIn link, and sometimes a message he already sent. Do all of this without being asked, so he never has to repeat it:

1. Add the row to the Contacts tab with only what Cody said. Mark what is his word and what is unverified.
2. If he already sent a message, log it on the Touches tab first, with his exact text. Never log from a draft.
3. Run `researcher` right away. It enriches from the web: verified title, city, a sourced hook, and a check of every claim Cody made about the person.
4. Run `triager` on the row. If a touch already went out, triage records the verdict anyway.
5. Run `scorer` only when the row is CLEAR and nothing has been sent yet.
6. Do not draft unless Cody asks.
7. Report what the research found, and any claim of Cody's that the sources did not support.

## Tracker (Google Sheet)

- **Contacts:** one row per person: company, title, school, persona, channels, CLEAR or FLAG with reason, source, hook and hook source, score, sequence state, next touch.
- **Scoring:** six factors, weights editable in one place.
- **Touches:** every touch: date, channel, hook type, touch number, reply, outcome, next step, exact text sent.
- **Drafts:** every version of every message, agent and Cody, with check failures and edit tags. Versions are appended, never overwritten.
- **Rules, Hooks:** channel rules, pacing, and counts by hook type.

## Scoring

Score = weighted sum of six 0 to 5 factors / 5 x 100.

| Factor | Weight |
|---|---|
| Hiring proximity | 30% |
| Path similarity | 20% |
| Alumni tie | 15% |
| Warm path | 15% |
| Activity and reachability | 10% |
| Recent trigger | 10% |

## Rules every step follows

1. A human sends everything. No tool logs in to or automates Cody's LinkedIn.
2. CLEAR or FLAG before any touch. A row the agent cannot verify is flagged, never guessed.
3. At most two new cold first touches per company per day. Warm contacts and ongoing conversations do not count against this limit.
4. Any reply ends the sequence. From then on it is a human conversation.
5. At most two follow-ups, spaced 3 to 5 business days apart. Each one brings something new or closes gracefully.
6. The tracker records what was sent, not what was drafted.
7. No outcome metrics in the repo. `scripts/funnel.py` regenerates them from tracker exports for a conversation. Never commit its output.

## Connectors needed to run it in Claude Code

Web search and fetch (Exa first, then others), Google Sheets (write access to the tracker), Gmail, Google Calendar, and a meeting-notes tool. Subagents inherit these tools from the session.

## Docs this setup relies on (checked Nov 1, 2026)

- Subagent files, frontmatter fields (`name`, `description`, `model`, `effort`) and the `.claude/agents/` location: https://code.claude.com/docs/en/subagents
- CLAUDE.md loading: https://code.claude.com/docs/en/memory
