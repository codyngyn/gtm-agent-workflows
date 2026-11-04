# gtm-agent-workflows

A public portfolio repo. Each folder is one GTM workflow. Subagents live in `.claude/agents/<workflow>/`. Workflow context is in each folder's CLAUDE.md, for example `prospecting-agent/CLAUDE.md`.

## Before any commit

1. Run `git config core.hooksPath .githooks` once per clone, so the privacy hook runs.
2. Export first and last names from the tracker's Contacts tab, one per line, to `data/names.txt`. Keep `data/terms.txt` current: every Company column value, contacts' past employers, events, schools, cities, and people named in notes or meetings who are not contacts. `data/` is gitignored and never committed.
3. The hook runs `scripts/privacy_scan.py` on what is staged. If it fails, fix the file. Never bypass the hook.

## What may be committed

- Build logic and anonymized text only: [name], [target company], [role], [school], [city].
- No outcome metrics: replies, reply rates, calls, hiring stages. `scripts/funnel.py` prints them for a live conversation; never commit its output.
- No contact names, emails, profile URLs, phone numbers, target company names or target role titles.
- No em dashes or en dashes.

## Commits

Author every commit as Cody Nguyen, with his own git email. No Co-Authored-By or session trailers; the README says the repo is built with Claude Code.

## Run logs

Each Claude Code run gets one file, `runs/YYYY-MM-DD-<short-name>.md`, using the template in `runs/README.md`. Record what ran, not what was planned.
