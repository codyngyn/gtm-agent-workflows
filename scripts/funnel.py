"""Regenerate the outreach funnel from tracker exports. Prints to stdout only.

Usage:
  python3 scripts/funnel.py --through 2026-10-30 [--max-id C065] [--data data]

Inputs: CSV exports of the tracker's Contacts, Touches and Drafts tabs, saved
as data/contacts.csv, data/touches.csv and data/drafts.csv (gitignored).

Outcome numbers are shared in conversation, not committed. Never redirect
this script's output into a file inside the repo.

Counted mechanically: contacts, flags, touches, first touches, replies, warm
vs cold, rule breaks in agent first drafts, edit share from first draft to
sent. Not counted here, because they live in free-text notes: calls held,
hiring process stages. Read those from the Contacts tab by hand.
"""
import argparse
import csv
import pathlib
import re
from collections import Counter

WARM = re.compile(r"^(Warm|Personal connection)", re.I)


def rows(path):
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def id_num(cid):
    m = re.search(r"\d+", cid or "")
    return int(m.group()) if m else 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--through", required=True, help="last touch date to count, YYYY-MM-DD")
    ap.add_argument("--max-id", default=None, help="last contact ID in the snapshot, e.g. C065")
    ap.add_argument("--data", default="data")
    a = ap.parse_args()
    d = pathlib.Path(a.data)

    contacts = rows(d / "contacts.csv")
    if a.max_id:
        contacts = [c for c in contacts if id_num(c["ID"]) <= id_num(a.max_id)]
    name = lambda c: f'{c["First name"]} {c["Last name"]}'.strip()
    source = {name(c): c.get("Source", "") for c in contacts}

    touches = [t for t in rows(d / "touches.csv") if t["Date"] <= a.through]
    first = {t["Contact"] for t in touches if t["Touch #"].strip() == "1"}
    replied = {t["Contact"] for t in touches if t["Replied"].strip().lower() == "yes"}
    warm = {c for c in first if WARM.match(source.get(c, ""))}
    cold = first - warm

    print(f"Snapshot: touches through {a.through}" + (f", contacts through {a.max_id}" if a.max_id else ""))
    print()
    print("| Stage | Count |")
    print("|---|---|")
    print(f"| Contacts in tracker | {len(contacts)} |")
    print(f"| Flagged | {sum(c.get('Triage', '').strip() == 'FLAG' for c in contacts)} |")
    print(f"| Contacts with a first touch | {len(first)} |")
    print(f"| Total touches | {len(touches)} |")
    print(f"| Contacts who replied | {len(replied & first)} of {len(first)} |")
    print()
    print("| Path | First touches | Replied |")
    print("|---|---|---|")
    print(f"| Warm | {len(warm)} | {len(warm & replied)} |")
    print(f"| Cold | {len(cold)} | {len(cold & replied)} |")
    unmatched = sorted(c for c in first if c not in source)
    if unmatched:
        print(f"\nWarning: {len(unmatched)} touched contact(s) not found on Contacts; counted as cold.")

    drafts = [r for r in rows(d / "drafts.csv") if r["Date"] <= a.through]
    v0 = [r for r in drafts if r["Version"] == "v0" and r["Author"] == "agent"]
    fails = Counter(f.strip() for r in v0 for f in r.get("Check failures", "").split(";") if f.strip())
    edits = [r["Edit % v0 to sent"] for r in drafts if r["Version"] == "sent" and r.get("Edit % v0 to sent", "").strip()]
    print()
    print("| Drafting | Value |")
    print("|---|---|")
    print(f"| Draft versions | {len(drafts)} |")
    print(f"| Agent first drafts | {len(v0)} |")
    for label, n in fails.most_common():
        print(f"| First drafts failing: {label} | {n} |")
    print(f"| Edit share, first draft to sent | {', '.join(e + '%' for e in edits) or 'none recorded'} |")
    print("\nCount by hand from Contacts notes: calls held, calls booked, hiring process stages.")


if __name__ == "__main__":
    main()
