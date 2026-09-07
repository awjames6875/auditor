# RECEIPT — Clean clone test

**Date:** Sunday, September 6, 2026
**Run by:** Adam James, with Claude
**Purpose:** verify the repo works for someone who has only what a clone
gives them — no local files, no setup, no explanation.

---

## Why this receipt exists

A repo that works on the author's machine and nowhere else is a
demonstration, not a tool. Everything below was run against a **fresh
clone into an empty directory**, not against the working copy.

```bash
git clone <this repo> ./clonetest
cd clonetest
python check.py
```

---

## Result

```
 15 gates checked - 15 passed, 0 FAILED
 exit code 0
```

Including the citation gate firing visibly on the three planted
citations that ship in `examples/findings-broken.md`:

```
--- DEMONSTRATION: the citation gate, fired on purpose

    caught: 450:1-9-5.6(b)(7) does not exist in reference/
    caught: 450:1-9-5.6(c)(3) does not exist in reference/
    caught: 450:1-9-5.6(a)(5) does not exist in reference/

[  ok  ] citation gate fires on planted citations   5 citations checked, 3 invalid - expected 3+
```

**No API key. No network. No install step. Python 3 standard library
only.**

---

## What the clone actually contains

Verified by listing every tracked file in the fresh clone:

```
.gitignore
README.md
COMP_12_FRAME_LOCK.md
COMP_12_HANDOFF.md
TEST_METHOD.md
IDEAS_LATER.md
check.py
auditor/README.md
auditor/identity.md
auditor/rules.md
auditor/examples.md
auditor/reference/450-1-9-5.6.md
examples/findings-broken.md
fixtures/fixture-01-missing-topics.md
fixtures/fixture-02-privileged-late.md
fixtures/fixture-03-no-supervision.md
fixtures/fixture-04-clean.md
fixtures/fixture-05-invented-citation-bait.md
receipts/EXPECTED_RESULTS.md
receipts/RULE_TEXT_VERIFICATION.md
```

### The three things this confirms

**1. `auditor/` holds exactly five things.** `README.md`, `identity.md`,
`rules.md`, `examples.md`, `reference/`. Nothing else reaches a reader
who drops the folder in whole.

**2. The answer key is not in the drop-in.**
`receipts/EXPECTED_RESULTS.md` sits outside `auditor/`. A judge who
drops the folder into a project cannot load it by accident, and neither
can the auditor.

**3. Nothing private travelled.** Absent from the clone, and confirmed
absent from every commit: the ODMHSAS exit summary, any office-format
document, session and tool artifacts, working notes, and internal
competition strategy files. `check.py`'s confidentiality screen also
runs clean — it stores SHA-256 digests rather than the literal terms,
because publishing a denylist would publish the identifiers it exists to
suppress.

---

## A defect this test found, recorded because it was real

Auto-generated `CLAUDE.md` stubs kept reappearing inside
`auditor/reference/`. Each is 169 bytes with no content, written by a
local memory plugin — but a stray sixth file inside the drop-in folder
breaks the "exactly five things" requirement, and it would have shipped
without anyone noticing.

**Two fixes:** `.gitignore` denies them, so they never reach a clone;
and `check.py` skips gitignored names when counting the folder's
contents, so it reports what actually ships rather than raising a false
alarm about a local file.

**Caught by running the check rather than trusting the layout.**

> **Standing note for anyone sharing this folder by hand:** if you zip
> `auditor/` locally instead of cloning, delete any regenerated
> `CLAUDE.md` first. The clone is clean; a local copy may not be.

---

## What this receipt does NOT establish

- It shows `check.py` runs and its gates pass. It says nothing about whether the **auditor's judgment** is correct — that is what Runs A through D test, and they are separate receipts.
- It was run on Windows with Python 3. The code uses only `os`, `re`, `sys`, and `hashlib` and takes no OS-specific paths, but it has not yet been executed on macOS or Linux.
- A passing gate is not a passing audit. `check.py` verifies that a cited provision **exists**, never that it is the **right** provision for the defect in front of it.
