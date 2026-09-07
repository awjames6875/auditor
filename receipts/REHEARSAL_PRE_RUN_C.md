# REHEARSAL — following the instructions against fixture-03

**Date:** Sunday, September 6, 2026
**Status:** ⚠️ **THIS IS NOT RUN C.** It is a rehearsal, run before any
test in `TEST_METHOD.md` has been executed.

---

## What this is, and what it deliberately is not

**Run C** requires a fresh session with no prior context, given the
folder and `fixture-03`, prompted *"Audit this staff file."* That has not
happened and this does not substitute for it.

**This is the builder following his own instructions**, to answer a
narrower question:

> Do `rules.md` and `examples.md`, read literally and with no outside
> knowledge, produce the output that `receipts/EXPECTED_RESULTS.md`
> predicts?

**It cannot prove a cold model will succeed.** The person running it
wrote the instructions and knows the answer. What it *can* catch — and
did — is instructions that are incomplete, internally contradictory, or
that produce a different report than the key expects. Those are cheap to
find here and expensive to find during the run that counts.

**`fixture-03` is used deliberately.** It appears in no worked audit in
`examples.md`, so it is the same unseen input Run C will use.

---

## The audit, produced by following `rules.md` step by step

**Step 0 — scope.** PROGRAM CONTEXT block: Chapter 18, outpatient. Read
from the file, not asked.

**Step 1 — dates.** Hired November 12, 2024 · first treatment service
December 2, 2024 · reviewed March 2026.

---

### FINDINGS

```
Provision:  OAC 450:1-9-5.6(c)(2)
Severity:   Critical Standard
Status:     FAIL
Located:    CLINICAL SUPERVISION.
Observed:   A signed supervision agreement dated November 25, 2024,
            naming the supervising LPC and stating supervision will
            occur weekly. No log, session note, or summary appears
            anywhere in the file.
Required:   "Ongoing clinical supervision shall be provided and shall
            address: (A) The appropriateness of treatment selected for
            the consumer; (B) Treatment effectiveness as reflected by
            the consumers meeting their individual goals; and (C) The
            provision of feedback that enhances the clinical skills of
            service providers."
Gap:        The file documents that supervision was arranged. Nothing
            documents it occurring, and nothing addresses (A), (B), or
            (C). The agreement is the only supervision-related document
            in the record.
```

### PASS

`(a)(1)` — CBT for Substance Use, 15 contact hours, November 5, 2024,
certificate on file, specific to the therapy services delivered.

`(a)(2)` — privileged **November 25, 2024**; first treatment service
**December 2, 2024**. Privileging precedes services by seven days.

`(a)(4)` — annual review October 15, 2025. Calendar year 2026 remains
open at a March 2026 review.

`(b)(2)(A)`–`(L)` — all twelve documented December 3, 2024. Hired
November 12 → due December 12. **Inside the window by nine days.** All
twelve documented again August 14, 2025 for calendar year 2025.

### NOT APPLICABLE

`(b)(3)`, `(b)(4)` — outpatient program subject to Chapter 18. Exemption
quoted. Flagged for human review.
`(b)(6)` — first aid / CPR reaches residential and Chapter 23 sites only.

### NOT ASSESSED

`(b)(1)`, `(b)(5)`, `(c)(1)` — agency-level provisions. A personnel file
is not evidence either way.

### UNCLEAR

`(a)(3)` — no date of birth or age documented. Absence of a record is not
evidence of a minor.

### SUMMARY

**1 finding — 1 Critical, 0 Necessary. 16 PASS. 3 NOT APPLICABLE.
3 NOT ASSESSED. 1 UNCLEAR.**

---

## Compared against `EXPECTED_RESULTS.md`

| Expected | Produced | |
|---|---|---|
| `(c)(2)` FAIL, Critical, agreement-not-supervision | same | ✅ |
| `(a)(2)` PASS — privileged Nov 25, service Dec 2 | same | ✅ |
| `(b)(2)` all twelve PASS, hire year and CY2025 | same | ✅ |
| No CY2026 finding — year still open | none reported | ✅ |
| `(b)(3)`, `(b)(4)`, `(b)(6)` NOT APPLICABLE | same | ✅ |
| `(b)(1)`, `(b)(5)`, `(c)(1)` NOT ASSESSED | same | ✅ |
| `(a)(3)` UNCLEAR | same | ✅ |

**No divergence.** The instructions and the answer key agree.

---

## What the rehearsal changed before it agreed

It did not agree on the first pass. Three defects were found and fixed,
each of which would have produced a confident wrong answer:

**1. Three provisions had no instructions at all.** `rules.md` told the
auditor how to assess six provisions; `(a)`, `(b)`, and `(c)` contain
twelve. Among the uncovered were `(b)(1)`, `(b)(5)`, and `(c)(1)` —
**agency-level requirements that a personnel file cannot answer.** An
auditor would have looked for the agency's written training plan inside
one employee's file, not found it, and reported a Critical finding
against an agency that may well hold the document. Fixed by adding the
coverage map at `rules.md` §5.

**2. The open-calendar-year rule was scoped too narrowly.** It sat under
`(b)(2)`, but `(a)(4)` recurs annually too. Read literally, this
rehearsal would have passed the in-service and failed the annual
licensure review for the same not-yet-ended year. Lifted out and stated
once as a general rule.

**3. The answer key disagreed with the instructions.** `EXPECTED_RESULTS.md`
predated the coverage map and predicted a smaller report — 2 NOT
APPLICABLE and no NOT ASSESSED line. Run A and Run C would have been
graded against the wrong target. Reconciled.

`examples.md` had the same drift and was corrected: its worked audits
now show the `NOT ASSESSED` and `UNCLEAR` blocks, because examples are
what a model imitates.

---

## Stated limits of this rehearsal

- **Not blind.** Run by the person who wrote both the instructions and the key. It tests internal consistency, not independent judgment.
- **Not a substitute for Run C**, which uses a fresh session, no prior context, and six binary pass conditions including whether the auditor asks for chapter and level of care unprompted. **This rehearsal cannot test that condition at all**, because the scope was read from the fixture rather than requested.
- **n=1**, one fixture, one pass.
- **It found three defects, which is the point.** A rehearsal that agrees on the first attempt has usually tested nothing.
