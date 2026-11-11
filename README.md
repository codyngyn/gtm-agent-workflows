# GTM agent workflows

I'm Cody, a recent Kellogg MBA (2026) exploring GTM opportunities at AI companies. This repo shows how I build and run agents for go-to-market work: what each agent does, the judgment calls I made, and what broke along the way. Built with Claude Code.

## How I work with agents

- **Agents handle research, first drafts and record-keeping. I make the judgment calls and send every message.** Steps that are faster by hand or by spreadsheet formula stay that way.
- **I check the output with rules before judgment.** A short script catches rule breaks every time. Facts get checked against a source, not trusted from a search result.
- **I measure what happens, and I share results in conversation.** The repo shows how the system decides and checks. Outcome numbers stay out of a public repo; a script regenerates them from the tracker when I walk through them live.
- **I'm clear about what ran and what's planned.** Each workflow says how it actually ran and what has not been built yet.

## Workflows

| Workflow | What it does | Agents |
|---|---|---|
| [prospecting-agent](prospecting-agent/) | Researches, triages, scores and drafts outreach to GTM practitioners at AI companies, to start short conversations that teach me about the individual, the team, and the opportunity, with a human sending every message | researcher, triager, scorer, drafter, logger |

Each workflow folder has a 5-minute walkthrough (README), the agent definitions, anonymized examples, my decisions, and a one-page retro.

## Privacy

No contact names, emails, profile links or employer details are published. Outcome metrics are not published. Examples use placeholders such as [name] and [target company].
