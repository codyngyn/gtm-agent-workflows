"""Privacy scan. Runs before every commit (see .githooks/pre-commit).

Usage: python3 scripts/privacy_scan.py [path] [--names data/names.txt] [--terms data/terms.txt]

Fails (exit 1) on contact names, emails, LinkedIn profile URLs, phone
numbers, target company names, target role titles, other identifying
terms, and em or en dashes.

Two gitignored files feed the scan, and it refuses to run without either:
- data/names.txt: first and last names from the tracker's Contacts tab,
  one per line.
- data/terms.txt: anything else that could identify a contact, one per
  line: every value in the Company column, contacts' past employers,
  events, schools, cities, and people named in notes or meetings who are
  not contacts. Lines starting with # are comments. Matching is
  case-sensitive and whole-word.
Own-background terms are reported as INFO and do not fail.
"""
import pathlib
import re
import sys

SKIP_DIRS = {".git", "data", "__pycache__"}
SKIP_FILES = {"privacy_scan.py"}

PATTERNS = {
    "email": r"[\w.+-]+@[\w-]+\.[\w.]+",
    "linkedin url": r"linkedin\.com/in/",
    "phone": r"\b\d{3}[-. ]\d{3}[-. ]\d{4}\b",
    "target company": r"\b(Anthropic|OpenAI|Cursor|Cognition|Baseten|SpaceX\w*|xAI|x\.ai|Grok|ChatGPT|OpenRouter)\b",
    "target role title": r"\b(BDRs?|SDRs?|Account Associates?|AAs?)\b",
    "em dash": "—",
    "en dash": "–",
}
INFO = r"\b(Cisco|Cohere|Kellogg)\b"

# Names too common to block on their own; full first + last pairs still fail.
COMMON = {"brown", "green", "cook", "smith", "kim", "lam", "sun", "rose", "stern",
          "ryan", "johnson", "lewis", "burke", "james", "grace", "claire", "chase",
          "grant", "will", "reed", "dan", "matt", "alex", "john", "emily", "peter",
          "kelly", "connor", "kenny", "andrew", "david", "michael", "lauren", "adam",
          "tony", "chris", "tyler", "simon", "sophie", "casey", "kevin", "brandon",
          "anthony", "elle", "sam", "jack", "jeff", "elias", "martine", "caroline",
          "julian", "eleanor", "connie", "foster", "meyer"}


def load_names(path):
    p = pathlib.Path(path)
    if not p.exists():
        sys.exit(f"privacy scan: {path} not found. Export contact names from the tracker first.")
    full, single = set(), set()
    for line in p.read_text().splitlines():
        line = line.strip()
        if not line:
            continue
        full.add(line)
        for part in re.split(r"[\s-]+", line):
            if len(part) > 3 and part.lower() not in COMMON:
                single.add(part)
    return full, single


def load_terms(path):
    p = pathlib.Path(path)
    if not p.exists():
        sys.exit(f"privacy scan: {path} not found. Export the Company column and other identifying terms first.")
    return {t.strip() for t in p.read_text().splitlines() if t.strip() and not t.startswith("#")}


def pop_arg(args, flag, default):
    if flag in args:
        i = args.index(flag)
        value = args[i + 1]
        del args[i:i + 2]
        return value
    return default


def main():
    args = sys.argv[1:]
    names_file = pop_arg(args, "--names", "data/names.txt")
    terms_file = pop_arg(args, "--terms", "data/terms.txt")
    root = pathlib.Path(args[0] if args else ".")
    full, single = load_names(names_file)
    extra = load_terms(terms_file)
    pats = dict(PATTERNS)
    terms = sorted(full | single, key=len, reverse=True)
    if terms:
        pats["contact name"] = r"\b(" + "|".join(map(re.escape, terms)) + r")\b"
    if extra:
        pats["identifying term"] = r"(?<!\w)(" + "|".join(map(re.escape, sorted(extra, key=len, reverse=True))) + r")(?!\w)"
    fails = 0
    for p in sorted(root.rglob("*")):
        if p.is_dir() or SKIP_DIRS & set(p.parts) or p.name in SKIP_FILES or p.suffix == ".pyc":
            continue
        for n, line in enumerate(p.read_text(errors="ignore").splitlines(), 1):
            for label, pat in pats.items():
                for m in re.finditer(pat, line):
                    fails += 1
                    print(f"FAIL {label}: {p.relative_to(root)}:{n}: {m.group(0)!r}")
            for m in re.finditer(INFO, line):
                print(f"INFO own background: {p.relative_to(root)}:{n}: {m.group(0)!r}")
    print(f"{fails} blocking hits")
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
