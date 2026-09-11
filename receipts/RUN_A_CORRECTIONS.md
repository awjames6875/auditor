# RUN_A_CORRECTIONS.md — insider accuracy pass

**Run:** A — insider accuracy, per `TEST_METHOD.md` §RUN A.
**Date of review:** September 11, 2026.
**Receipt committed:** September 11, 2026, the day of the run.

---

## Tester and consent — recorded above the findings

**Tester:** **Lisa**, compliance officer at Safe Harbor Behavioral Health.
One person, not two. First name only, per `TEST_METHOD.md`: *"Consent
covers a first name and verbatim words."*

**Consent:** given verbally by phone on September 6, 2026 and **confirmed
in writing before this receipt was committed**, covering her first name
and her verbatim words appearing in a public repository.

**Method deviation, stated before the findings:** `TEST_METHOD.md` fixes
the run order 0 → A → B → C → D. **Run A was performed after Run C**, and
after the Wednesday September 9 freeze, because it depended on a real
person's availability. Logged in `receipts/DEVIATIONS.md`.

---

## THE HEADLINE: this key was wrong, and no run had ever tested it

`fixture-02` shipped with a PROGRAM CONTEXT block reading *"File reviewed:
March 2026"* while the file itself contained an annual licensure review
dated **May 4, 2026** — a document dated two months after the file was
supposedly reviewed. The date was impossible.

**`EXPECTED_RESULTS.md` never addressed it.** It listed `(a)(4)` under
Expected PASS with no note.

**No recorded run has ever been executed against `fixture-02`.** Run 0 used
`fixture-01`; Run C, the rehearsal, and the independent zero-context agent
test all used `fixture-03`. The defect did not survive three runs missing
it — it survived because nothing ever looked at this file, and an answer key
no run had exercised still read as settled. One compliance officer, reading
it for the first time, caught it.

**`TEST_METHOD.md` gives Run B `fixture-02`.** Karen is therefore the first
run ever executed against this file, on the corrected copy.

In her words:

> "This one has a 'correct' answer already written up, and it's wrong. The
> file says it was reviewed in March 2026, but the annual licensure review
> inside it is dated May 4, 2026, two months after the file was supposedly
> already looked at. That's not a real date. The written answer marks it a
> clean pass and doesn't catch it. That's a mistake in the answer key
> itself, not just the tool."

This is the strongest single result in the run, and it is a result
**against** the build, not for it.

---

## Corrections — changes inside `auditor/`

`TEST_METHOD.md` defines the published count: *"a correction is any change
to a file inside `auditor/` traceable to A's feedback. The published count
is that number of diffs. A change cannot be reclassified as 'a
clarification' to keep it out of the count."*

### **PUBLISHED CORRECTION COUNT: 4**

| ID | Date | File | Change | Traceable to |
|---|---|---|---|---|
| **C-1** | Sep 11, 2026 | `auditor/rules.md` §8 | Added the annual-review timing limit: `(a)(4)` spells out no grace period and no first-year proration, no fixture tests whether a review is owed for a partial hire year, and the tool had **assumed** an answer without writing it down. | Named directly by Lisa. |
| **C-2** | Sep 11, 2026 | `auditor/rules.md` §8 | Added the limit that the **severity tiers are less verified than the rule text** — the rule got 0.9948 across 1,552 words, the Critical/Necessary tiers got no equivalent check. | Named directly by Lisa. |
| **C-3** | Sep 11, 2026 | `auditor/rules.md` §3 | Recorded that **`(b)(4)` has no sourced tier** in the table this build verified, that a `(b)(4)` finding ships `UNSOURCED — VERIFY`, and that it is never inferred from `(b)(3)`. Same gap noted for `(a)(3)`, `(a)(4)`, `(b)(6)`. | Downstream of her structural finding — see the chain note below. |
| **C-4** | Sep 11, 2026 | `auditor/rules.md` §5 | Rewrote the `(b)(6)` row. It said when the provision is **out** of scope but never what to report when it is **in** scope, which no fixture had ever triggered. Now: on a residential or Chapter 23 site, `NOT ASSESSED — site-level`, **even when a current card is in the file.** A card is not site coverage. | Downstream of her structural finding. |

**Chain note on C-3 and C-4, stated rather than argued away.** Lisa did
not name `(b)(4)`'s severity or `(b)(6)`'s in-scope behavior. Both defects
were exposed by the two fixtures written **in response to** her structural
finding, and would not have been found without it. `TEST_METHOD.md` says
traceable, not named, so they are counted. They are not reclassified as
clarifications to hold the number at two.

---

## Changes made OUTSIDE `auditor/` — logged, not counted

These do not enter the published correction count, by the method's own
definition. They are listed so the count cannot be read as the whole of
what changed.

| File | Change |
|---|---|
| `fixtures/fixture-02-privileged-late.md` | Review date corrected March 2026 → **June 2026**. One line. No other date touched. |
| `receipts/EXPECTED_RESULTS.md` | Dated correction note on the `fixture-02` entry; rewritten scope section; `(b)(4)` severity row; `(b)(6)` residential rows; `fixture-06` and `fixture-07` entries; dated provenance note at the head of the file. |
| `fixtures/fixture-06-chapter-27-exempt.md` | **New.** Chapter 27, residential. |
| `fixtures/fixture-07-residential-intervention-training.md` | **New.** Chapter 18, residential. |

---

## What was deliberately NOT changed

**No rule was added requiring the auditor to catch internally impossible
dates.** An impossible date violates **no provision of 450:1-9-5.6**.
Adding a rule to catch it would invent a standard, which is the exact
discipline `rules.md` §3 (*"You never invent a severity"*) and §8 exist to
protect. `fixture-02`'s date was an **authoring defect in the fixture**,
not a finding the tool missed. That distinction is the reason the
published count is 4 and not 5.

**`(b)(4)`'s severity was not inferred from `(b)(3)`'s Critical.** They sit
adjacent in the rule text, and adjacency is not a source — `(b)(2)` alone
splits across both tiers. The finding ships with its severity marked
unknown instead.

**`TEST_METHOD.md` was not edited** to make its four-fixture table match a
seven-fixture set. That mismatch is a deviation and is logged as one.

---

## Her structural finding — and it required no change to the tool

Her largest finding was that **every fixture was Chapter 18, outpatient**:

> "Every single test file is Chapter 18. None are Chapter 27. That's not
> just a gap in the sample data, it means the tool has been built and
> tuned entirely around the exam you're studying for, not the one you're
> actually enrolled in. Almost all of (a), (b), (c), training, privileging,
> supervision already apply to you right now under Chapter 27, no matter
> what you're working toward. The only two rules that even depend on
> chapter are the intervention-training ones, and Chapter 27 and Chapter 18
> get exempted differently: Chapter 27 is exempt outright, Chapter 18 only
> if you're outpatient. Since every test file is Chapter 18 and outpatient,
> that difference has never actually been exercised. **The tool could be
> landing on the correct exemption by accident, not because the chapter
> logic is actually correct.**"

**This is correct, and it was a coverage defect rather than a rules
defect.** `auditor/rules.md` §4 already carried both exemption branches,
including *"A residential Chapter 18 program is **not** exempt — the
provision applies in full."* The rules were right. Nothing in them could
be shown to be right, because only one of the three branches had ever
fired.

**Zero corrections to `auditor/` came from this finding directly.** What
came from it were two fixtures:

- **`fixture-06`** — Chapter 27, residential. The strings "outpatient" and
  "Chapter 18" appear nowhere in it, so the Chapter 27 clause is the only
  available route to NOT APPLICABLE.
- **`fixture-07`** — Chapter 18, **residential**. The exemption does not
  fire. `(b)(3)` and `(b)(4)` apply in full and produce findings. Its
  NON-PHYSICAL INTERVENTION TRAINING section reads *"No documentation on
  file"* — the identical sentence that is **correct** on fixtures 01–06.

**Both fixtures were executed against before this receipt was
committed** — writing an answer key beside a fixture and never running it
is precisely the failure this run exposed in `fixture-02`, and repeating
it the same afternoon was not acceptable. One zero-context agent session
per fixture, neither having seen the key. **Both matched their new key
entries on every line**, each named the specific exemption route it
applied, and `fixture-07` fell for neither of its two over-reporting
traps. **Zero corrections arose, so the count above stands at 4.** See
`receipts/FIXTURE_06_07_VALIDATION.md`.

That validation is the entrant's own — unblinded, entrant-written,
entrant-graded — and is **not** Run A. **Lisa has not seen either
fixture.** Both were written after her review, in response to it, and her
sign-off on them is not claimed. Agreement between a key and runs graded
against it is also exactly the condition that held for `fixture-02` right
up until she read it.

---

## Where the tester confirmed the tool rather than correcting it

**Two of her four fixture verdicts were corroboration, and the receipt
says so rather than presenting the run as four corrections.**

**`fixture-01`** — she independently re-derived the finding: three of
twelve required topics documented, the other nine genuinely missing, and
privileging, supervision and the intervention-training exemptions all
clean. Matches the key.

**`fixture-04`** — *"The clean file. Went through it and found nothing
wrong. If a run flags anything here, that's a false alarm, not a real
finding."* Matches the key.

**`fixture-03` — a corroboration that also revealed a method problem.**
She wrote: *"No answer key exists for this one, so it's the one to check
most carefully by hand,"* then derived the supervision failure by hand —
a signed November 2024 agreement with no logs, no notes:

> "That should be a hard fail. A signed promise to supervise isn't
> documentation that supervision occurred."

**An answer key for `fixture-03` did exist**, at `EXPECTED_RESULTS.md`,
expecting exactly that `(c)(2)` finding under a heading reading *"The trap
is the agreement,"* and `auditor/rules.md` §6 already stated *"A
supervision agreement is not supervision."* Her independent derivation
matching the key without having seen it is the strongest corroboration in
the run.

**It also means she reviewed an incomplete copy of the material.**
`TEST_METHOD.md` specifies the tester receives *"the folder and all four
fixtures"* and is silent on whether the key is included. She had the
fixtures; she did not have all of the key. **A future Run A must state
exactly what the tester was handed.** That is a defect in the method, not
in her review, and it is not corrected here because `TEST_METHOD.md` is
frozen.

---

## The scope question the method required her to rule on

`TEST_METHOD.md`: *"is Safe Harbor an outpatient program subject to
Chapter 18 for purposes of the (b)(3) exemption? If unresolved, it is
marked VERIFY and shipped unresolved rather than guessed."*

**Her ruling, September 6 and restated in this review:** Safe Harbor is
**certified under Chapter 27 right now**. Outpatient-only Chapter 18 is
what the agency is **applying for**, not what it was at the time of the
August review.

**Consequence for the tool:** the `(b)(3)` exemption is **forward-looking**
and is **not** a basis for claiming the August listing was wrong. The
separator is *"the auditor handles a scope condition correctly,"* never
*"the state was wrong."*

**Marked VERIFY, not resolved:** whether the Chapter 27 certification and
the Chapter 18 application interact for `(b)(3)` purposes in any way
beyond the above is **not** settled by this run, and nothing further is
inferred from it.

---

## Open questions carried to the compliance officer

Four provisions carry **no sourced severity tier** in this build —
`(b)(4)`, `(a)(3)`, `(a)(4)`, `(b)(6)`. The tier source is the ODMHSAS
Provider Certification Manual, Quality Clinical Standards table. She is
the one person positioned to close all four in a single pass, and they are
carried to her rather than guessed.

---

## What this run does NOT establish

- **It is one reviewer, once.** n=1.
- **It does not establish that the auditor is correct.** It establishes
  that one compliance officer, reading the fixtures and the key, found one
  real defect in the key, one real structural gap in the fixture set, two
  documentation gaps, and corroborated two fixtures.
- **It does not cover `fixture-05`.** She reviewed four fixtures; the
  citation-bait fixture was not among them.
- **It does not validate `fixture-06` or `fixture-07`.** Both were written
  after her review, in response to it, and she has not seen them.
- **The corrections are the entrant's implementation of her feedback**,
  not her sign-off on that implementation. She has not reviewed this
  receipt's technical changes.
