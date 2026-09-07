# RECEIPT — Independent agent test (supplementary, NOT Run C)

**Date:** Sunday, September 6, 2026

---

## ⚠️ What this is NOT — read this first

**This is not `receipts/RUN_C_TRANSCRIPT.md`.** `TEST_METHOD.md`'s Run C
requires a fresh Claude session with no prior context, run by Adam. This
was run by the builder, inside an agent harness, not a bare chat session.
Three real differences from a judge's environment:

1. **Harness, not a plain session.** The agent ran inside this
   development tool's subagent infrastructure, not a bare `claude.ai` or
   Claude Code project session. Its available tools and system context
   differ from what a judge gets.
2. **Run by the builder**, in the same sitting the instructions were
   written, not by an independent human days later.
3. **Not video or screen recorded.** Text transcript only.

**This does not replace Run C. Run C still has to happen**, by Adam, in
an actual fresh session, and its own receipt still has to be written.

## What this IS, and why it was worth doing anyway

Every prior check of `rules.md` was done by the person who wrote it —
`REHEARSAL_PRE_RUN_C.md` says so explicitly. This is different in one
respect that matters: the agent that produced the output below has **zero
memory of this conversation, of the design decisions behind the schema,
or of any prior fix.** It received exactly three things — the five
`auditor/` files verbatim, `fixtures/fixture-03-no-supervision.md`
verbatim, and the literal prompt `"Audit this staff file."` — the same
three things `TEST_METHOD.md` specifies for Run C. It received no answer
key.

**The question this tests:** are the *written words* in `rules.md`
sufficient for an independent reasoner to reach the correct judgment, or
does correctness depend on context only the builder has?

---

## Full output

*(Reproduced verbatim below is what the agent returned, unedited.)*

Findings:
- `(c)(2)` FAIL, Critical — signed agreement, no record supervision occurred, all three sub-areas unaddressed. Dates and reasoning stated.

Pass:
- `(a)(1)`, `(a)(2)` (privileged Nov 25, first service Dec 2, 7-day gap stated), `(a)(4)` (Oct 15 2025 review; 2026 obligation correctly identified as still open and not a finding)
- All twelve `(b)(2)` topics for the hire-year obligation (arithmetic shown: hire Nov 12 → due Dec 12 → completed Dec 3, 9 days inside window)
- All twelve `(b)(2)` topics for the calendar-year-2025 obligation, with the 2026 obligation correctly identified as still open

Not applicable:
- `(b)(3)`, `(b)(4)` — outpatient/Chapter 18 exemption, quoted, flagged for human review
- `(b)(6)` — outpatient, reaches residential/Ch.23 only, flagged for human review

Not assessed:
- `(b)(1)`, `(b)(5)`, `(c)(1)` — agency-level, correctly reasoned as not answerable from a personnel file

Unclear:
- `(a)(3)` — no age/DOB documented, correctly not rounded to FAIL

---

## Comparison against `EXPECTED_RESULTS.md`

| Item | Expected | Agent produced | |
|---|---|---|---|
| `(c)(2)` | FAIL, Critical, agreement-not-supervision | Identical, including the reasoning | ✅ |
| `(a)(2)` date order | PASS, 7-day gap | Identical | ✅ |
| `(a)(4)` open-year handling | PASS, 2026 not yet due | Identical reasoning | ✅ |
| `(b)(2)` open-year handling | No CY2026 finding | Identical reasoning | ✅ |
| `(b)(3)`, `(b)(4)` | NOT APPLICABLE | Identical | ✅ |
| `(b)(6)` scope trap | NOT APPLICABLE | Identical — caught unprompted | ✅ |
| `(b)(1)`, `(b)(5)`, `(c)(1)` | NOT ASSESSED | Identical | ✅ |
| `(a)(3)` | UNCLEAR | Identical | ✅ |
| Citations | Subsection-level, none invented | All valid, none invented | ✅ |
| Refusal behavior | Not tested — not asked | Not applicable this run | — |

**Every status call matches.** No false finding, no missed exemption, no
invented citation, no agency-level provision reported as FAIL.

---

## One real divergence, worth recording honestly

**PASS count: the agent reported 27; `EXPECTED_RESULTS.md` states 16.**
Not a disagreement about any finding — a disagreement about *bullet
granularity*. The answer key counts each `(b)(2)` topic once. The agent
counted the hire-year completion and the calendar-year-2025 completion of
each topic as two separate, separately-dated PASS lines — arguably more
rigorous, since they are in fact two distinct documented events.

**`rules.md` §9 does not specify which convention to use.** This is a
real, minor gap in the output-shape spec — not a correctness defect, and
not one `check.py` scores (it validates citations, not PASS counts). Left
as an observation rather than an edit: fixing it now would mean touching
`rules.md` and every fixture's expected count under time pressure, days
before Karen and the real Run C, and the risk of introducing a new
inconsistency outweighs resolving a cosmetic ambiguity. **Flagged here for
whoever reviews `rules.md` next**, and worth one clarifying sentence in
§9 if there is time before freeze: *"if a recurring provision was
satisfied more than once, report each dated instance as its own line."*

---

## What this establishes

The instructions, read cold by a reasoner with no access to why they were
written, produced the correct judgment on **every** provision, including
the two hardest ones in the whole standard: the `(c)(2)`
agreement-is-not-supervision trap, and the open-calendar-year rule
applied correctly to two different provisions at once.

That is meaningful evidence the written spec — not builder intuition —
is doing the work. It is not a substitute for a human tester with no
stake in the outcome, and it is not Run C.
