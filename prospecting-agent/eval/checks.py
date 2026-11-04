"""Deterministic pre-send checks and draft-vs-sent diff for prospecting outreach.

Usage: python3 checks.py versions.json
versions.json: list of {contact, version, author, format, text}

Published as it ran from Oct 28, 2026, with two changes: the em dash pattern
is written as the escape "\\u2014" instead of the literal character, and a
check for links in connection notes was added on Nov 4, 2026.
Known issue: an ask written as a statement ("let's do a quick call") is
flagged "No question or ask". Not yet fixed.
"""
import json, sys, re, difflib

BANNED = [
    (r"\bapplying\b|\bapply to\b|\bapply for\b", "Says applying (goal is a meeting, not an application)"),
    ("\u2014", "Em dash"),
    (r"caught my eye", "Stock phrase: caught my eye"),
    (r"\bstandout\b", "'standout' as one word where verb 'stand out' is meant"),
    (r"(?i)sorry|apologi", "Apology"),
    (r"(?i)hope this finds you", "Stock opener"),
]

LINK = r"https?://|www\.|\b[\w-]+\.(com|net|org|io|ai|dev)\b"

LIMITS = {"connection note": 300, "text": None, "inmail": None, "email": None}


def ask_count(t):
    return t.count("?")


def check(text, fmt="connection note"):
    issues = []
    lim = LIMITS.get(fmt.lower())
    if lim and len(text) > lim:
        issues.append(f"Over {lim} characters ({len(text)})")
    for pat, label in BANNED:
        if re.search(pat, text, flags=re.I if "(?i)" not in pat else 0):
            issues.append(label)
    if fmt.lower() == "connection note" and re.search(LINK, text, flags=re.I):
        issues.append("Link in a connection note (offer it, or send it after they accept)")
    q = ask_count(text)
    if q == 0:
        issues.append("No question or ask")
    if q > 1:
        issues.append(f"{q} questions (one ask per note)")
    if re.search(r"(?i)would love to connect|let's (do a )?(quick )?call", text) and q >= 1:
        issues.append("Second ask stacked on the question")
    return issues


def edit_pct(a, b):
    return round(100 * (1 - difflib.SequenceMatcher(None, a, b).ratio()))


if __name__ == "__main__":
    rows = json.load(open(sys.argv[1]))
    by = {}
    for r in rows:
        by.setdefault(r["contact"], []).append(r)
    out = []
    for c, vs in by.items():
        v0 = next((v for v in vs if v["author"] == "agent"), None)
        sent = next((v for v in vs if v["version"] == "sent"), None)
        for v in vs:
            v["chars"] = len(v["text"])
            v["issues"] = check(v["text"], v.get("format", "connection note"))
        if v0 and sent:
            out.append({"contact": c, "edit_pct_v0_to_sent": edit_pct(v0["text"], sent["text"]),
                        "versions": len(vs)})
    json.dump({"rows": rows, "pairs": out}, sys.stdout, indent=1)
