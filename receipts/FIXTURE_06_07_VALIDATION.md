# FIXTURE_06_07_VALIDATION.md — the two new fixtures, actually executed

**Date:** September 11, 2026, immediately after the fixtures and their
answer-key entries were written.

**Why this receipt exists.** Run A found that `fixture-02` shipped with an
answer-key entry that had **never been executed against the fixture** and
was wrong. Writing two new fixtures and two new key entries and *not*
running them would have repeated that failure the same afternoon. These
runs exist so the `fixture-06` and `fixture-07` entries in
`EXPECTED_RESULTS.md` are not the same kind of unexecuted claim.

---

## Method

Two independent agent sessions, one per fixture, each with **no prior
context** on this project.

Each was told only that a set of instructions lives somewhere in
`auditor/`, and was given one fixture. Each was explicitly forbidden to
read `receipts/` (where the answer key lives), any other fixture,
`check.py`, `README.md`, `TEST_METHOD.md`, or any `COMP_*` file. Neither
saw the answer key, and neither saw the other's fixture.

Beyond the audit, each was asked to state its scope reasoning explicitly:
which chapter and level of care it determined, **which exemption route it
applied**, and where its severities came from. The route matters more than
the status here — that is the whole point of these two fixtures.

**What this is not.** These are not Run C. Run C is a genuine fresh Claude
session run by Adam, and it has already happened against `fixture-03`.
These are validation runs on new material, run by the entrant, and they
are graded by the entrant against a key the entrant wrote. Unblinded, and
disclosed.

---

## Result: both matched the answer key on every line

| | `fixture-06` expected | `fixture-06` produced | `fixture-07` expected | `fixture-07` produced |
|---|---|---|---|---|
| Findings | 0 | **0** ✓ | 2 | **2** ✓ |
| `(b)(3)` | NOT APPLICABLE | **NOT APPLICABLE** ✓ | FAIL, Critical | **FAIL, Critical** ✓ |
| `(b)(4)` | NOT APPLICABLE | **NOT APPLICABLE** ✓ | FAIL, unsourced severity | **FAIL, `UNSOURCED — VERIFY`** ✓ |
| PASS | at least 16 | **16** ✓ | at least 16 | **16** ✓ |
| NOT APPLICABLE | 2 | **2** ✓ | 0 | **0** ✓ |
| NOT ASSESSED | 4 | **4** ✓ | 4 | **4** ✓ |
| UNCLEAR | `(a)(3)` | **`(a)(3)`** ✓ | `(a)(3)` | **`(a)(3)`** ✓ |

---

## The discriminating test, which is the reason these fixtures exist

The key says reaching the right **status** by the wrong **route** scores as
a partial, not a pass. Both runs were asked to name the route.

**`fixture-06` — Chapter 27, residential.** It used the Chapter 27 clause
and volunteered, unprompted, why the other route was unavailable:

> "The exemption route I applied is the **first** category — *'facilities
> or programs subject to Chapter 27 of this Title.'* Not the Chapter 18
> route. This matters: the Chapter 18 route is a two-part test (must be
> **outpatient** *and* subject to Chapter 18), and this program would fail
> it, because it is residential. The Chapter 27 category carries **no
> level-of-care qualifier** — the words 'outpatient programs' attach only
> to the Chapter 18 clause that follows, not to the Chapter 27 clause."

**`fixture-07` — Chapter 18, residential.** It correctly found that **no**
exemption reaches the file, naming the exact condition that fails:

> "There are two exempt categories, and this file matches neither. The
> Chapter 27 category fails because the program is certified under Chapter
> 18, not 27. The Chapter 18 category fails on its **level-of-care
> condition**: it is written as '**outpatient** programs subject to
> Chapter 18,' and this program is residential. Both halves of that
> category — outpatient AND Chapter 18 — must hold together; only the
> Chapter 18 half holds."

**This is what Lisa's structural finding asked for.** Her concern was that
the tool "could be landing on the correct exemption by accident, not
because the chapter logic is actually correct." On the same sentence —
*"No documentation on file"* — the auditor returned NOT APPLICABLE for one
program and a Critical finding for the other, and in each case named the
specific clause and condition that drove it. That is the chapter logic
working, not pattern-matching on the sentence.

---

## Both over-reporting traps held

`fixture-07` is built to invite two false findings. Neither was produced.

1. **The open 2026 calendar year.** `(b)(3)` requires *"updates each
   calendar year thereafter,"* and 2026 is still open. The run rested its
   finding on the 2025 hire-window obligation alone and did not cite a
   missing 2026 update.
2. **`(b)(2)` against the one-day ordering.** First treatment service
   (September 2) precedes the in-service roster (September 3), which looks
   like a defect and is not. The run passed `(b)(2)`, citing the
   thirty-day window from hire, and did not invent a service-delivery
   condition the provision does not contain.

---

## The Run A corrections are visible in the output

All four corrections from `receipts/RUN_A_CORRECTIONS.md` show up in
behavior, not just in the files:

- **C-1** — `fixture-06`'s `(a)(4)` block surfaced the partial-hire-year
  question on its own: *"the rule text spells out no grace period and no
  first-year proration for (a)(4), so whether a 2025 review was separately
  owed is not resolved by the standard — named here rather than decided
  silently."*
- **C-2** — `fixture-07` closed with the standing caveat that the tiers are
  less verified than the rule text, citing the 0.9948 figure.
- **C-3** — `fixture-07` **refused to supply a `(b)(4)` severity**:
  *"I could not source a tier for this provision, and I am saying so
  rather than supplying one… Adjacency in the rule text is not a source."*
  It reported a real FAIL with its severity marked unknown rather than
  borrowing Critical from `(b)(3)`.
- **C-4** — both runs reported `(b)(6)` as `NOT ASSESSED — site-level` on a
  residential site while a current card was in the file, rather than
  passing it on the card. `fixture-07`: *"A current card is not site
  coverage."*

---

## Corrections arising from these runs: ZERO

Neither run produced a result that required a change to anything inside
`auditor/`. The published Run A correction count stands at **4**.

---

## What these runs do NOT establish

- **n=1 per fixture.** One run each, not three.
- **Unblinded and entrant-graded.** The entrant wrote the fixtures, wrote
  the key, ran the runs and graded them. That is disclosed, not corrected.
- **They do not make the key authoritative.** Both runs agreeing with the
  key is exactly the condition that held for `fixture-02` before Run A
  found the key wrong. Agreement between a key and the runs graded against
  it is weaker evidence than one qualified human reading the file — which
  is the single clearest lesson of Run A, and it is not undone by this
  receipt.
- **Lisa has not reviewed `fixture-06` or `fixture-07`.** Both were written
  after her review, in response to it. Her sign-off is not claimed.
