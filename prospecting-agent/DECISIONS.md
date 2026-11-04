# Decisions

The judgment calls that shaped the system, with who made each one. The source is the original session record (Oct 21 to Nov 1, 2026). Decisions that depended on a specific company are left out.

Who:
- **Me**: I decided.
- **Agent, I approved**: the agent proposed it and I agreed.
- **Agent, unchallenged**: the agent proposed it and I never objected.

| Decision | Alternatives | Why | Who |
|---|---|---|---|
| A human sends every message | Automate LinkedIn sends | My LinkedIn account carries my reputation. Automation risks it. | Agent proposed; I approved |
| Google Sheet as the CRM | A real CRM; a chat-only log | Free, visible, and editable by both of us | Agent proposed; I approved |
| Enrich by hand on the free Apollo tier, no phones | Pay for phone credits; ask a coach for numbers | Cost. Phones held for a later decision gate (outcome not recorded) | Me |
| Two new cold first touches per company per day, no cap on conversations | The agent's reading: two active threads per company | The goal is several champions per company, not one thread | Me, correcting the agent |
| Build champions across the hiring team; drop title-based search | A second search by the exact titles of the roles I'm targeting (the agent's recommendation) | These companies title most sellers "GTM," so title search finds little | Me, overruling the agent |
| Add "warm path" as a scoring factor | The original five factors | The first replies came from warm contacts | Agent, unchallenged |
| CLEAR or FLAG before any touch; flag, never guess | Let the agent fill gaps | A wrong name or company in a cold note ends the conversation | Agent proposed; I approved |
| Peers first, leaders a few days later | Leaders first | My call. I never wrote down the reason | Me |
| Leaders get an InMail with the full pitch, then a short connection request on a later day | One message | The InMail carries the detail; the request is a light second touch | Me |
| Don't tell peers I'm "applying"; leaders may hear application intent | The same message for everyone | A peer conversation is about learning. A leader owns the decision | Me |
| Referral before application | Apply first | Referral credit | Agent proposed; I approved |
| Version every draft and run deterministic checks | Keep drafts only in chat | First drafts were being overwritten, so nothing could be measured | Me (scope and timing); agent built it |
| Company names come from Sales Navigator, not search tools | Trust search results | A search tool returned the wrong employer for a contact | Agent proposed, after I caught the error |

## For this repo (Nov 1, updated Nov 4)

| Decision | Alternatives | Why | Who |
|---|---|---|---|
| Describe it as built in Claude Code | Date each step's move from the first Claude conversation into Claude Code | The repo and agents were built and run in Claude Code; the run logs keep the dated detail | Me |
| One model with effort set per step | A different model per step | That is how I actually worked | Me |
| Keep outcome metrics out of the repo; share them live | Publish the funnel | Interviewers and people I contacted will read this. Results need context a page can't give | Me |
| No company names, no company-specific rules | Tailor to each reader | The repo is for every reader, including the people I contacted | Me |
| No links in connection notes; offer one, or link my site after they accept | Link in every note | A link costs characters and reads as a second ask | Me |
| Triage also clears event contacts and recent alumni of target companies | Hiring targets only | Advisors and connectors were being flagged | Me |
| Block employers, events, schools, cities and non-contact names in the privacy scan | Contact names only | Those details identify a contact as surely as a name | Me |
