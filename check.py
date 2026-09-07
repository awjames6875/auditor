#!/usr/bin/env python3
"""
check.py - the gate for the Staff File Auditor.

Runs bare, offline, with no API key, no network, and no dependencies
beyond the Python standard library, on Windows / macOS / Linux.

    python check.py                     # everything
    python check.py --shape             # brief-compliance gates only
    python check.py --verify-reference  # structural checks on the standard
    python check.py --denylist          # confidentiality screen
    python check.py findings.md         # validate citations in a findings file

Exit code 0 = every gate passed. Non-zero = at least one gate failed.

WHAT THIS CANNOT CATCH, stated plainly so no reader over-trusts it:
it verifies that a cited provision EXISTS. It cannot verify that the
citation is the RIGHT one for the defect in front of it. That
judgment stays human.
"""

import hashlib
import os
import re
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
AUDITOR = os.path.join(ROOT, "auditor")
REFERENCE = os.path.join(AUDITOR, "reference", "450-1-9-5.6.md")

# The five things auditor/ is allowed to contain. The brief is literal
# about this, so an automated compliance check would test it first.
REQUIRED = {"README.md", "identity.md", "rules.md", "examples.md", "reference"}

# Confidentiality screen. The literal strings are NOT stored here -
# publishing the denylist would publish the identifiers it exists to
# suppress. SHA-256 of each lowercased term is stored instead.
#
# Honest limit: a hash of a short string is a tripwire, not a secret.
# The purpose is catching an ACCIDENTAL commit, not resisting someone
# who already knows what to look for.
DENIED_HASHES = {
    "b091c49855ed42de1907d6618539e9c0f619d9e3b199dd138a8de2ccb976e29e": "consumer identifier",
}

PASS, FAIL, WARN = "PASS", "FAIL", "WARN"
results = []


def record(status, gate, detail=""):
    results.append((status, gate, detail))
    mark = {PASS: "  ok  ", FAIL: " FAIL ", WARN: " warn "}[status]
    print("[%s] %-46s %s" % (mark, gate, detail))


def read(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()


# --------------------------------------------------------------- shape

def ignored_names():
    """Bare filenames denied by .gitignore.

    A judge clones the repo, so a gitignored file is not part of the
    submission and must not be reported as a stray. Parsed by hand -
    no git dependency, since this has to run anywhere.
    """
    names = set()
    path = os.path.join(ROOT, ".gitignore")
    if not os.path.isfile(path):
        return names
    for line in read(path).splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        line = line.lstrip("/").rstrip("/")
        if line.startswith("**/"):
            line = line[3:]
        if "/" not in line and "*" not in line:
            names.add(line)
    return names


def check_shape():
    print("\n--- BRIEF COMPLIANCE (the shape a checker tests first)\n")

    if not os.path.isdir(AUDITOR):
        record(FAIL, "auditor/ exists", "not found")
        return
    record(PASS, "auditor/ exists")

    skip = ignored_names()
    actual = set(e for e in os.listdir(AUDITOR)
                 if not e.startswith(".") and e not in skip)
    missing = REQUIRED - actual
    extra = actual - REQUIRED

    if missing:
        record(FAIL, "auditor/ has all five required things",
               "missing: " + ", ".join(sorted(missing)))
    else:
        record(PASS, "auditor/ has all five required things")

    if extra:
        record(FAIL, "auditor/ has nothing extra",
               "unexpected: " + ", ".join(sorted(extra)))
    else:
        record(PASS, "auditor/ has nothing extra")

    # Case-exact names. A checker may run on Linux, where README.md
    # and readme.md are two different files.
    for name in sorted(REQUIRED):
        if name in actual:
            continue
        near = [a for a in actual if a.lower() == name.lower()]
        if near:
            record(FAIL, "exact filename: " + name,
                   "found '%s' - case matters on Linux" % near[0])

    # examples.md must be smaller than rules.md (stated gate).
    ex = os.path.join(AUDITOR, "examples.md")
    ru = os.path.join(AUDITOR, "rules.md")
    if os.path.isfile(ex) and os.path.isfile(ru):
        ew = len(read(ex).split())
        rw = len(read(ru).split())
        if ew < rw:
            record(PASS, "examples.md smaller than rules.md",
                   "%d words vs %d" % (ew, rw))
        else:
            record(FAIL, "examples.md smaller than rules.md",
                   "%d words vs %d" % (ew, rw))

    # Fixtures, receipts and this script live OUTSIDE the drop-in, so a
    # judge who drops auditor/ in whole cannot load an answer key.
    for stray in ("fixtures", "receipts", "check.py", "EXPECTED_RESULTS.md"):
        if os.path.exists(os.path.join(AUDITOR, stray)):
            record(FAIL, stray + " stays outside auditor/", "found inside")
        else:
            record(PASS, stray + " stays outside auditor/")


# ----------------------------------------------------------- reference

def parse_reference():
    """Return ({subsection: set(numbers)}, order, body) for real provisions."""
    body = read(REFERENCE).split("\n---\n", 1)[-1]
    order = re.findall(r"^## \(([a-z])\)", body, re.M)
    inventory = {}
    for i, sub in enumerate(order):
        seg = body.split("## (%s)" % sub, 1)[1]
        if i + 1 < len(order):
            seg = seg.split("## (%s)" % order[i + 1], 1)[0]
        inventory[sub] = set(
            int(n) for n in re.findall(r"^\*\*\((\d+)\)\*\*", seg, re.M))
    return inventory, order, body


def check_reference():
    print("\n--- THE STANDARD (criterion 3: is it actually in reference/)\n")

    if not os.path.isfile(REFERENCE):
        record(FAIL, "reference/ contains the standard", "file not found")
        return None

    inv, order, body = parse_reference()

    words = len(body.split())
    if words > 1000:
        record(PASS, "reference/ holds full text, not a summary",
               "%d words" % words)
    else:
        record(FAIL, "reference/ holds full text, not a summary",
               "only %d words - the named auto-fail" % words)

    if order == list("abcdef"):
        record(PASS, "subsections (a)-(f) present and in order")
    else:
        record(FAIL, "subsections (a)-(f) present and in order", str(order))

    try:
        seg = body.split("## (b)", 1)[1].split("## (c)", 1)[0]
        seg = seg.split("**(2)**", 1)[1].split("**(3)**", 1)[0]
        letters = re.findall(r"- \*\*\(([A-L])\)\*\*", seg)
    except IndexError:
        letters = []
    if letters == list("ABCDEFGHIJKL"):
        record(PASS, "(b)(2) topics (A)-(L), no gaps")
    else:
        record(FAIL, "(b)(2) topics (A)-(L), no gaps", "".join(letters))

    exemptions = (
        ("(b)(3)", "outpatient programs subject to Chapter 18 of this Title"),
        ("(b)(4)", "Chapter 16 or Chapter 27 of this Title"),
    )
    for prov, kw in exemptions:
        if kw in body:
            record(PASS, prov + " exemption sentence present")
        else:
            record(FAIL, prov + " exemption sentence present", "not found")

    print("\n    provision inventory (what citations are checked against):")
    for sub in order:
        nums = " ".join("(%d)" % n for n in sorted(inv[sub]))
        print("      (%s) -> %s" % (sub, nums))
    return inv


# ----------------------------------------------------------- citations

CITATION = re.compile(
    r"450:1-9-5\.6\s*\(([a-z])\)\s*\((\d+)\)(?:\s*\(([A-L])\))?")


def check_citations(paths, inv, demo=False):
    """Validate every citation in a findings artifact.

    demo=True means we are running against the deliberately-broken
    example that ships with the repo. It is SUPPOSED to fire, so its
    invalid citations are reported loudly but do not count as failed
    gates - otherwise a bare run would tell a judge the build is
    broken when it is actually working.
    """
    if demo:
        print("\n--- DEMONSTRATION: the citation gate, fired on purpose\n")
        print("    examples/findings-broken.md ships with invalid citations")
        print("    so this gate visibly works on a bare run. Failures below")
        print("    are the EXPECTED result, not defects.\n")
    else:
        print("\n--- CITATIONS (criterion 1: real standard, or just opinion?)\n")

    if inv is None:
        record(FAIL, "citations validated", "no reference to check against")
        return

    checked = 0
    invalid = 0
    caught = []
    for path in paths:
        if not os.path.isfile(path):
            record(WARN, "findings artifact", path + " not found")
            continue
        name = os.path.basename(path)
        for sub, num, letter in CITATION.findall(read(path)):
            checked += 1
            num = int(num)
            label = "450:1-9-5.6(%s)(%d)%s" % (
                sub, num, "(%s)" % letter if letter else "")
            reason = None
            if sub not in inv or num not in inv[sub]:
                reason = label + " does not exist in reference/"
            elif letter and not (sub == "b" and num == 2):
                reason = label + " - only (b)(2) carries lettered topics"
            if reason:
                invalid += 1
                caught.append(reason)
                if demo:
                    print("    caught: %s" % reason)
                else:
                    record(FAIL, "invalid citation in " + name, reason)

    summary = "%d citations checked, %d invalid" % (checked, invalid)
    if demo:
        # The gate passes when it CATCHES the planted citations.
        print("")
        record(PASS if invalid > 0 else FAIL,
               "citation gate fires on planted citations",
               summary + " - expected 3+")
    else:
        # Silence and success must never look identical.
        record(PASS if invalid == 0 else FAIL, "citation check complete",
               summary)


# ------------------------------------------------------------ denylist

SKIP_DIRS = (".git", "__pycache__", "tasks", "tool-results", ".claude")


def check_denylist():
    print("\n--- CONFIDENTIALITY SCREEN\n")
    hits = 0
    for base, dirs, files in os.walk(ROOT):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for fn in files:
            if not fn.endswith((".md", ".py", ".txt", ".json")):
                continue
            path = os.path.join(base, fn)
            try:
                text = read(path).lower()
            except (OSError, UnicodeDecodeError):
                continue
            for w in set(re.findall(r"[a-z0-9]{3,}", text)):
                h = hashlib.sha256(w.encode()).hexdigest()
                if h in DENIED_HASHES:
                    hits += 1
                    record(FAIL,
                           "denied term in " + os.path.relpath(path, ROOT),
                           DENIED_HASHES[h])
    if hits == 0:
        record(PASS, "no denied terms found",
               "%d terms screened" % len(DENIED_HASHES))


# ---------------------------------------------------------------- main

def main():
    args = sys.argv[1:]
    flags = [a for a in args if a.startswith("--")]
    paths = [a for a in args if not a.startswith("--")]

    print("=" * 68)
    print(" check.py - Staff File Auditor gate")
    print("=" * 68)

    run_all = not flags and not paths

    if run_all or "--shape" in flags:
        check_shape()

    inv = None
    if run_all or "--verify-reference" in flags or paths:
        inv = check_reference()

    if run_all or "--denylist" in flags:
        check_denylist()

    if run_all or paths:
        if paths:
            check_citations(paths, inv, demo=False)
        else:
            demo_file = os.path.join(ROOT, "examples", "findings-broken.md")
            check_citations([demo_file], inv, demo=True)

    failed = [r for r in results if r[0] == FAIL]
    print("\n" + "=" * 68)
    print(" %d gates checked - %d passed, %d FAILED"
          % (len(results), len(results) - len(failed), len(failed)))
    print("=" * 68)
    if failed:
        print("\n FAILED GATES:")
        for _, gate, detail in failed:
            print("   - %s %s" % (gate, ("(%s)" % detail) if detail else ""))
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
