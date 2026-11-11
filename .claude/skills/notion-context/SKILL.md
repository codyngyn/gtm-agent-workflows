---
name: notion-context
description: Pull context from Cody's Notion before a task, when he says "see Notion", "it's in my Notion notes", "from the transcript in Notion", or /notion-context. Covers meeting notes, event notes and podcast transcripts stored there.
---

# Notion Context

Goal: Cody should never have to paste what he already saved in Notion. Find the right page, read the part that matters (the transcript, not only the summary), state the context back in a short brief, then do the task.

## Step 1: Find the page

1. Search with `notion-search` using the person, company, event or episode name. Run a second search with only the topic words, since titles vary.
2. Add a `created_date_range` filter when he means something recent ("the fireside", "last week's event").
3. Pick the best match and name it in your first line. If two pages could fit, ask one question listing both titles.
4. Nothing found: say so plainly, and say what you searched. Do not fall back to memory or the web without telling him.

## Step 2: Read it

- Fetch with `notion-fetch`. Meeting pages hide the transcript by default: fetch again with `include_transcript: true` when the task needs exact words, quotes, names or numbers.
- Long pages are saved to a file instead of returned. Search that file for the words you need (Python slicing or grep), then read the surrounding lines. Read the whole span before concluding anything is missing.
- **The summary is not the source.** AI summaries drop and reword details. Before saying a quote or fact is not in Notion, check the transcript itself. Say "not found in the summary" or "not found in the transcript", never "not there", unless you searched both.
- Transcripts are machine-made: speaker labels may be generic and names misheard. Confirm who is speaking from context (an introduction, a role, a self-reference) before attributing a quote.
- Honor any handling note on the page, such as "off the record" or "no posting".

## Step 3: Context brief (before the task)

- **Page:** title, date, where it sits (database or folder)
- **What it covers:** one line
- **Key points:** 3 to 6 bullets
- **Exact quotes:** only the lines the task needs, verbatim, with the timestamp when there is one
- **Gaps:** what the page does not settle
- **Source:** the page link

## Step 4: Do the task

- If he gave a task (a message, prep notes, a tracker update), do it with the brief. Use `my-writing-style` for anything sent as him.
- If he gave none, end the brief with one question: what he wants done with it.
- Push back when the page contradicts his framing, and quote the line that does.

## Rules

- Never use em dashes.
- Never send, post or file anything without Cody's explicit yes.
- Never invent a detail the page lacks; flag it as a gap.
- Keep page content private: quote what the task needs, nothing more, and never put it in the public repo.
