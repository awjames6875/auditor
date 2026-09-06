# RECEIPT — Rule text verification

**Date:** Sunday, September 6, 2026
**File verified:** `auditor/reference/450-1-9-5.6.md`
**Verified by:** Adam James, with Claude
**Committed:** the same day the verification was performed.

---

## Why this receipt exists

The brief's judging criteria ask whether the auditor works against *"a real, citable standard, or just an opinion,"* and whether *"the standard is actually in `reference/` where a reader can check it."*

A file **claiming** to be the standard satisfies neither. The claim has to be checked, and the check has to be visible. That is what this file is.

The original transcription was pulled from the **Cornell Legal Information Institute mirror** — a mirror, not the publisher. If that transcription had drifted, this entry would have shipped *"a summary of the standard, written by the entrant"* without knowing it. The brief names that as an auto-fail.

---

## Sources

| Role | Source |
|---|---|
| **Source of record** | ODMHSAS publication of OAC Title 450, Chapter 1, effective **September 1, 2025** |
| **Secondary cross-check** | Cornell LII — `law.cornell.edu/regulations/oklahoma/OAC-450-1-9-5.6` |
| **Authority of last resort** | The text on file with the **Oklahoma Secretary of State**. ODMHSAS's own publications state that any difference between their publication and the Secretary of State's file is decided in favor of the Secretary of State. |

**Amendment history:** adopted eff. 9/15/2021 · amended 9/15/2022 · 9/15/2023 · 9/1/2024. The **9/1/2025** publication was checked; `450:1-9-5.6` is unchanged from the 9/1/2024 text.

---

## Part 1 — Text comparison

**Method:** the ODMHSAS PDF was converted with `pdftotext`; both texts were normalized (whitespace collapsed, case folded, formatting markup stripped) and compared with a sequence-similarity diff.

**Result: 0.9948 similarity across 1,552 words of provision text.**

**One difference found, at `(f)(3)(B)`:**

| | |
|---|---|
| Transcription had | `…reported to ODMHSAS immediately**,** not to exceed twenty-four (24) hours…` |
| Source reads | `…reported to ODMHSAS immediately not to exceed twenty-four (24) hours…` |

**Corrected to match the source.** One stray comma, no substantive wording difference anywhere in the section.

**What changed vs. what did not:** the file adds headings, bold provision markers, and line breaks for readability. **No wording was altered.** Bold inside the `(b)(3)` and `(b)(4)` exemption sentences is emphasis added by this transcription and is not present in the source — stated in the file's own header so no reader mistakes it for the state's emphasis.

---

## Part 2 — Structural checks

Run against the file as committed. Every one is reproducible by a reader with the repo and no special tooling.

| # | Question | Result |
|---|---|---|
| 1 | Are top-level subsections `(a)`–`(f)` present and in order? | **PASS** — `a b c d e f` |
| 2 | Does `(b)(2)` run `(A)`–`(L)` with no gaps? | **PASS** — `ABCDEFGHIJKL` |
| 3 | Are both exemption sentences present verbatim? | **PASS** — `(b)(3)` and `(b)(4)` |
| 4 | Do the provisions the auditor cites actually exist? | **PASS** — see inventory below |
| 5 | Are the citation-bait provisions genuinely absent? | **PASS** — `(a)(5)`, `(b)(7)`, `(c)(3)` |

### Provision inventory (what exists in this section)

```
(a) -> 1 2 3 4
(b) -> 1 2 3 4 5 6      (b)(2) carries topics (A)-(L)
(c) -> 1 2
(d) -> 1 2 3 4 5 6
(e) -> 1 2 3 4
(f) -> 1 2 3
```

This inventory is what `check.py` validates citations against.

> **A finding from check 5, recorded because it changes a planned test.** `(b)(6)` **exists** — first aid and CPR for residential sites. It had been a candidate for the falsification #5 "invented citation" bait. It cannot be used: a citation to `(b)(6)` is valid. The bait uses `(a)(5)`, `(b)(7)`, and `(c)(3)`, all confirmed absent above.

---

## Reproduce this

```bash
# structural checks, against the committed file
python check.py --verify-reference

# text comparison, against the source of record
#   1. download the ODMHSAS Title 450 Chapter 1 PDF (eff. 9/1/2025)
#   2. pdftotext -layout chapter1.pdf chapter1.txt
#   3. extract section 450:1-9-5.6, normalize whitespace and case
#   4. diff against auditor/reference/450-1-9-5.6.md with markup stripped
```

---

## What this receipt does NOT prove

- **Not a legal certification.** It shows this file matches a published source on a stated date. The Secretary of State's filed text remains the authority, and rules are amended.
- **Verified once, on one date, by the entrant.** Not independently audited. The method is published so anyone can re-run it and disagree.
- **It proves the text is faithful, not that the auditor reads it correctly.** That is what Runs A through D test, and they are separate receipts.
- **The 0.9948 figure describes the automated comparison in Part 1.** Part 2's structural checks were run separately against the committed file and are reproducible from the repo alone.
