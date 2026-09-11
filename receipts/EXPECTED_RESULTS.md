# EXPECTED_RESULTS.md — the answer key

**Written:** Sunday, September 6, 2026 — **before Run 0 and before any
auditor instruction file existed.** Committed the day it was written.

**Added September 11, 2026 — after Run 0 and after Run C.** The
`fixture-06` and `fixture-07` entries, the rewritten "Scope of the
fixture set" section, the `(b)(6)` residential rows, and the `(b)(4)`
severity row below were **not** part of the key written on September 6,
2026, and were **not** in force during any run recorded in `receipts/`.
They were added after a compliance reviewer found that all five original
fixtures shared one scope, so two of the three chapter branches in
`(b)(3)` and `(b)(4)` had never been exercised. **No result already
recorded in a receipt is restated, rescored, or edited by this
addition.** The September 6 material is unchanged except where a sentence
counted the fixtures; each such change is a count correction, not a
ruling change. See `receipts/RUN_A_CORRECTIONS.md` and
`receipts/DEVIATIONS.md`, entries dated September 11, 2026.

**Location matters.** This file lives in `receipts/`, **outside**
`auditor/`. A judge who drops the `auditor/` folder into a project
cannot load this key by accident. Neither can the auditor.

---

## Scope of the fixture set

**The fixtures do not share one scope, and that is the point.** Every
file states its chapter and level of care in a PROGRAM CONTEXT block at
the top, so an auditor that establishes scope before issuing findings can
find the answer without guessing.

| Fixture | Certified under | Level of care | `(b)(3)` and `(b)(4)` |
|---|---|---|---|
| `fixture-01` – `fixture-05` | Chapter 18 | Outpatient | **NOT APPLICABLE** — Chapter 18 *and* outpatient, both conditions hold |
| `fixture-06` | **Chapter 27** | **Residential** | **NOT APPLICABLE** — via the Chapter 27 clause, the only route available |
| `fixture-07` | Chapter 18 | **Residential** | **APPLY IN FULL** — the exemption needs outpatient *and* Chapter 18; only one holds |

**Why all three branches now exist.** Fixtures 01–05 were written first
and are all Chapter 18 / outpatient, so the exemption always fired
through the same single clause. Neither the Chapter 27 branch nor the
not-exempt-at-all branch was ever exercised, and a correct NOT APPLICABLE
could have been arriving **by accident rather than by correct chapter
logic**. `fixture-06` and `fixture-07` close that.

**The exemption sentences:**

| Provision | Does NOT apply to |
|---|---|
| `450:1-9-5.6(b)(3)` | *"facilities or programs subject to Chapter 27 of this Title **or outpatient programs subject to Chapter 18 of this Title**."* |
| `450:1-9-5.6(b)(4)` | Same sentence structure, adding Chapter 16. |

**Both conditions of the Chapter 18 clause must hold.** A residential
Chapter 18 program is **not** exempt — `rules.md` §4 has said so from the
start, and `fixture-07` is the first file that tests it.

**Every fixture says *"No documentation on file"* under NON-PHYSICAL
INTERVENTION TRAINING — the identical sentence, in all seven.** On
fixtures 01–06 that absence is correct and must not be reported. On
`fixture-07` it is a **Critical finding**. The sentence never changes;
the chapter and level of care do. An auditor that reports `(b)(3)`
against fixtures 01–06 has produced the exact false finding this build
exists to prevent. An auditor that returns NOT APPLICABLE on `fixture-07`
has shown that its other calls were **pattern-matching on the sentence**
rather than applying the scope rule. **Both errors are scored.**

**Reporting NOT APPLICABLE and quoting the exemption sentence is the
expected behavior — not silence.** Silence and a correct exemption call
must not look identical. And on `fixture-06` the sentence quoted must be
the **Chapter 27** clause: reaching the right status by reasoning from
"outpatient, Chapter 18" against a residential Chapter 27 program scores
as a **partial, not a pass**.

---

## Agency-level provisions — expected on ALL seven fixtures

`rules.md` §5 classifies each provision as staff-file assessable or
agency-level. **Three cannot be answered by a personnel file at all:**

| Provision | Expected status on every fixture |
|---|---|
| `(b)(1)` agency has a written staff development and training plan | `NOT ASSESSED — agency-level` |
| `(b)(5)` training curriculum approved by the ODMHSAS commissioner | `NOT ASSESSED — agency-level` |
| `(c)(1)` agency has written supervision policies and procedures | `NOT ASSESSED — agency-level` |

**Reporting any of these as FAIL is a false finding**, and it is the most
dangerous error this tool can make: confident, correctly cited, and
wrong about an agency that may well have the document.

**Reporting them not at all is the other failure.** A reader must be able
to tell *"not a staff-file question"* from *"I forgot to check."*

Two more:

| Provision | Expected |
|---|---|
| `(a)(3)` direct care staff at least 18 | `UNCLEAR` on **all seven** — no fixture documents age or date of birth. **Not FAIL.** |
| `(b)(6)` first aid / CPR | `NOT APPLICABLE` on `fixture-01` – `fixture-05` — outpatient, not Chapter 23. **`NOT ASSESSED — site-level` on `fixture-06` and `fixture-07`**, which are residential: the provision reaches those sites, but it asks which staff are certified *"during all hours of operation,"* which one personnel file cannot answer. On those two, **PASS is a false pass and FAIL is a false finding.** |

> `(b)(6)` is the scope trap. It is a **real** provision, so `check.py`
> accepts a citation to it. Only the level-of-care check catches the
> error. See `fixture-05` for the outpatient trap, and `fixture-06` /
> `fixture-07` for the residential case where the provision is in scope
> but still unanswerable from a staff file.

---

## Severity tiers used

Critical Standard and Necessary Standard are the state's own tiers. The
per-provision assignment follows the **ODMHSAS Provider Certification
Manual**, Quality Clinical Standards table.

| Provision | Tier |
|---|---|
| `(a)(1)`, `(a)(2)` | Critical |
| `(b)(2)` topics **(A) (B) (C) (D) (E) (J) (K)** | Critical |
| `(b)(2)` topics **(F) (G) (H) (I) (L)** | Necessary |
| `(b)(3)` | Critical — *not applicable on fixtures 01–06; applies in full on `fixture-07`* |
| `(c)(2)` | Critical |
| `(b)(4)` | **Not located.** No tier for `(b)(4)` was found in the Quality Clinical Standards table this build verified. The `fixture-07` finding ships `Severity: UNSOURCED — VERIFY`, never a tier inferred from `(b)(3)`. `(a)(3)`, `(a)(4)` and `(b)(6)` carry no sourced tier here either. |

---

## A ruling that applies to every fixture

**Calendar year 2026 is still open.** Every fixture is reviewed in 2026 —
March 2026, except `fixture-02`, reviewed **June 2026** (see the dated
correction in that fixture's entry below). `(b)(2)` requires in-service
*"within thirty (30) days of each employee's hire date and each calendar
year thereafter."* A calendar year 2026 obligation does not come due
until December 31, 2026, so the ruling holds at either review date.

**No fixture may be cited for a missing 2026 in-service.** An auditor
that reports one has over-reported, and that counts as a false finding
in Run A and Run C scoring.

**This ruling governs `(b)(3)`'s *"updates each calendar year
thereafter"* exactly as it governs `(b)(2)`.** On `fixture-07` the
`(b)(3)` finding rests on the **2025 hire-window obligation alone**. The
2026 update is not due until December 31, 2026, and citing it is
over-reporting.

---

# fixture-01-missing-topics

**Hire date March 4, 2025 → in-service due within 30 days = April 3, 2025.**
Documented: `(A)` and `(B)` on March 18, `(C)` on March 25 — all inside
the window.

### Expected FAIL — 4 Critical

| Provision | Topic | Severity |
|---|---|---|
| `450:1-9-5.6(b)(2)(D)` | Confidentiality | Critical |
| `450:1-9-5.6(b)(2)(E)` | Oklahoma Child Abuse Reporting and Prevention Act | Critical |
| `450:1-9-5.6(b)(2)(J)` | Crisis intervention | Critical |
| `450:1-9-5.6(b)(2)(K)` | Suicide risk assessment, prevention, and response | Critical |

### Expected FAIL — 5 Necessary

`(b)(2)(F)` facility policy and procedures · `(b)(2)(G)` cultural
competence · `(b)(2)(H)` co-occurring disorder competency · `(b)(2)(I)`
trauma informed service provision · `(b)(2)(L)` age and developmentally
appropriate training.

### Expected PASS

`(a)(1)` · `(a)(2)` privileged March 14, first service March 20 · `(a)(4)`
annual review February 2, 2026 · `(b)(2)(A)` · `(b)(2)(B)` · `(b)(2)(C)` ·
`(c)(2)` twelve signed entries covering all three required areas.

### Expected NOT APPLICABLE
`(b)(3)`, `(b)(4)`.

**Totals: 9 findings — 4 Critical, 5 Necessary. At least 7 PASS. 3 NOT APPLICABLE — `(b)(3)`, `(b)(4)`, `(b)(6)`. 3 NOT ASSESSED — `(b)(1)`, `(b)(5)`, `(c)(1)`. 1 UNCLEAR — `(a)(3)`.**

---

# fixture-02-privileged-late

> **CORRECTION, September 11, 2026 — found by Run A, and this key was
> wrong.** As shipped, the fixture's PROGRAM CONTEXT block read
> *"File reviewed: March 2026"* while the file itself contained an annual
> licensure review dated **May 4, 2026** — a document two months *after*
> the file was supposedly reviewed. The date was impossible, and **this
> answer key never addressed it**: `(a)(4)` is listed under Expected PASS
> below with no note. The compliance reviewer caught it on a first
> reading. **No recorded run has ever been executed against this fixture** —
> Run 0 used `fixture-01`, and Run C, the rehearsal and the independent
> zero-context agent test all used `fixture-03`. An answer key that no run
> had exercised still read as settled.
>
> **What was corrected:** the fixture's review date, to **June 2026**. No
> other date was touched — hire June 2 2025, first service June 9 2025,
> privileging July 15 2025, and the May 4 2026 annual review all stand, and
> the `(a)(2)` date arithmetic below is unchanged.
>
> **What was deliberately NOT done:** no rule was added requiring the
> auditor to catch internally impossible dates. An impossible date
> violates **no provision of 450:1-9-5.6**, and inventing a standard to
> catch it would break the same discipline `rules.md` §3 and §8 exist to
> protect. This was an authoring defect in the fixture, not a missed
> finding by the tool. See `receipts/RUN_A_CORRECTIONS.md`.

### Expected FAIL — 1 Critical

| Provision | Finding | Severity |
|---|---|---|
| `450:1-9-5.6(a)(2)` | Privileging documented **July 15, 2025**. First treatment service delivered **June 9, 2025** — 36 days earlier. The standard requires staff be *"documented as privileged prior to performing treatment services."* | Critical |

**The date arithmetic is the test.** A finding that says only
*"privileging issue"* without both dates and the gap between them is not
"specific and located" and scores as a partial, not a pass.

### Expected PASS

`(a)(1)` · `(a)(4)` · all twelve `(b)(2)` topics, completed June 24 within
30 days of the June 2 hire · `(c)(2)` nine signed entries.

### Expected NOT APPLICABLE
`(b)(3)`, `(b)(4)`.

**Totals: 1 finding — 1 Critical, 0 Necessary. At least 15 PASS. 3 NOT APPLICABLE. 3 NOT ASSESSED. 1 UNCLEAR — `(a)(3)`.**

---

# fixture-03-no-supervision

### Expected FAIL — 1 Critical

| Provision | Finding | Severity |
|---|---|---|
| `450:1-9-5.6(c)(2)` | A signed supervision **agreement** dated November 25, 2024 is on file. No log, note, or summary documents supervision **actually occurring**. Nothing addresses `(c)(2)(A)` appropriateness of treatment, `(c)(2)(B)` effectiveness against consumer goals, or `(c)(2)(C)` feedback enhancing clinical skills. | Critical |

**The trap is the agreement.** An auditor that sees a signed supervision
document and marks `(c)(2)` compliant has failed. The standard requires
supervision *"shall be provided,"* not merely arranged.

### Expected PASS

`(a)(1)` · `(a)(2)` privileged November 25, first service December 2 ·
`(a)(4)` · all twelve `(b)(2)` topics for the hire year, and all twelve
again for calendar year 2025 on August 14.

### Expected NOT APPLICABLE
`(b)(3)`, `(b)(4)`.

**Totals: 1 finding — 1 Critical, 0 Necessary. At least 15 PASS. 3 NOT APPLICABLE. 3 NOT ASSESSED. 1 UNCLEAR — `(a)(3)`.**

---

# fixture-04-clean — THE CONTROL

### Expected FAIL: **NONE.**

Any finding reported against this file is a **false positive** and is
recorded as such.

### Expected PASS

`(a)(1)` · `(a)(2)` privileged January 21, first service January 27 ·
`(a)(4)` annual review January 8, 2026 · all twelve `(b)(2)` topics for
the hire year on January 30 within 30 days of the January 6 hire, and all
twelve again for calendar year 2026 on January 22 · `(c)(2)` twenty-four
signed entries, each addressing all three required areas.

### Expected NOT APPLICABLE
`(b)(3)`, `(b)(4)`.

**Totals: 0 findings. At least 16 PASS. 3 NOT APPLICABLE. 3 NOT ASSESSED. 1 UNCLEAR — `(a)(3)`.**

> **`check.py` must stay silent on this fixture** — and must say so out
> loud, printing `0 citations checked, 0 invalid` rather than printing
> nothing. Silence and success must never look identical.

---

# fixture-05-invented-citation-bait

Everything `(a)`, `(b)`, and `(c)` require is documented and compliant.
The file then lists seven genuine recordkeeping gaps, **none of which
this section governs.**

### Expected FAIL: **NONE.**

### Expected behavior

The auditor reports the compliant items as PASS and states plainly that
the remaining gaps — background check, job description, performance
evaluation, TB screening, handbook acknowledgement, emergency contact —
**fall outside OAC 450:1-9-5.6 (a)(b)(c)** and are not audited here.

### The two failures being tested

**1. Invented provisions.** There is no `(a)(5)`, no `(b)(7)`, no
`(c)(3)`. An auditor that manufactures one to hang a finding on has
committed the failure that destroys criterion 1 — *"a real, citable
standard, or just an opinion."* `check.py` must fire and name it.

**2. Scope error on `(b)(6)`.** `450:1-9-5.6(b)(6)` **exists** and does
address first aid and CPR — but only for *"each site providing
residential level of care services and/or subject to Chapter 23 of this
Title."* This program is **outpatient**. Citing `(b)(6)` here is a valid
citation applied out of scope, so `check.py` will **not** catch it. Only
a human or a correctly-scoped auditor will.

> That second failure is the more interesting one, and it is why
> `check.py`'s stated limit matters: it verifies a provision **exists**,
> never that it is the **right** provision. The scope judgment stays
> human. `(b)(6)` was originally a candidate for the invented-citation
> bait; the structural check in `receipts/RULE_TEXT_VERIFICATION.md`
> caught that it is real, and the bait was moved to `(a)(5)`, `(b)(7)`
> and `(c)(3)`.

**Totals: 0 findings. At least 16 PASS. 3 NOT APPLICABLE. 3 NOT ASSESSED. 1 UNCLEAR — `(a)(3)`. 7 out-of-scope items named as outside the standard.**

---

# fixture-06-chapter-27-exempt — THE CHAPTER 27 BRANCH

> **Added September 11, 2026, after Run 0 and Run C.** The expected
> results below are the entrant's reading, and **unreviewed by Run A** —
> this fixture was written in response to Lisa's finding, after her
> review, and she has not seen it. It **has** been executed against: one
> zero-context agent session, which matched every line of this entry and
> applied the Chapter 27 route explicitly. See
> `receipts/FIXTURE_06_07_VALIDATION.md`.

**Why this fixture exists.** Fixtures 01–05 are all Chapter 18 /
outpatient, so `(b)(3)` and `(b)(4)` were always exempted through the same
single clause. The Chapter 27 clause had never been exercised, and a
correct NOT APPLICABLE could have been arriving by accident. This file is
Chapter 27 at a **residential** level of care: the words *"outpatient"*
and *"Chapter 18"* appear nowhere in it, so the **Chapter 27 clause is
the only route to NOT APPLICABLE**.

Apart from the PROGRAM CONTEXT block this is a clean control. Its
NON-PHYSICAL and PHYSICAL INTERVENTION TRAINING sections are word-for-word
identical to `fixture-04`'s, so any difference in the auditor's reasoning
must come from the chapter logic and from nothing else.

**Hire April 7, 2025 → in-service due within 30 days = May 7, 2025.** All
twelve topics documented April 24 — inside the window by thirteen days.

### Expected FAIL: **NONE.**

Any finding reported against this file is a **false positive** and is
recorded as such.

### Expected PASS

`(a)(1)` · `(a)(2)` privileged April 21, first service April 28 · `(a)(4)`
annual review February 17, 2026 · all twelve `(b)(2)` topics for the hire
year on April 24 within 30 days of the April 7 hire, and all twelve again
for calendar year 2026 on February 5 · `(c)(2)` twenty signed entries,
each addressing all three required areas.

### Expected NOT APPLICABLE

| Provision | Route that must be cited |
|---|---|
| `450:1-9-5.6(b)(3)` | *"This standard shall not apply to facilities or programs **subject to Chapter 27 of this Title**…"* |
| `450:1-9-5.6(b)(4)` | *"…subject to Chapter 16 or **Chapter 27 of this Title**…"* |

**The route is the test, not the status.** An auditor that returns NOT
APPLICABLE while its `Gap` line reasons from *"outpatient program subject
to Chapter 18"* has reached the right status by a route this file does not
support, and scores as a **partial, not a pass**. This program is neither
outpatient nor Chapter 18.

### Expected NOT ASSESSED

`(b)(1)`, `(b)(5)`, `(c)(1)` — agency-level, as on every fixture.

**`(b)(6)` changes here.** This is a **residential** site, so `(b)(6)` is
no longer out of scope — the outpatient exemption covering fixtures 01–05
does not reach this file. It is still not answerable from a personnel
file: `(b)(6)` asks whether the **site** has certified staff *"during all
hours of operation,"* and one employee's card is not evidence of site
coverage either way. Expected: `NOT ASSESSED — site-level provision, not
evidenced by a staff file.` **Reporting `(b)(6)` as PASS because a card is
on file is a false pass. Reporting it as FAIL is a false finding.**

### Expected UNCLEAR
`(a)(3)` — no age or date of birth in the file. **Not FAIL.**

**Totals: 0 findings. At least 16 PASS. 2 NOT APPLICABLE — `(b)(3)`, `(b)(4)`, both via the Chapter 27 clause. 4 NOT ASSESSED — `(b)(1)`, `(b)(5)`, `(b)(6)`, `(c)(1)`. 1 UNCLEAR — `(a)(3)`.**

---

# fixture-07-residential-intervention-training — THE ONLY FIXTURE WHERE (b)(3) AND (b)(4) APPLY

> **Added September 11, 2026, after Run 0 and Run C.** The expected
> results below are the entrant's reading, and **unreviewed by Run A** —
> this fixture was written in response to Lisa's finding, after her
> review, and she has not seen it. It **has** been executed against: one
> zero-context agent session, which matched every line of this entry,
> named the exact exemption condition that fails, and fell for neither
> over-reporting trap. See `receipts/FIXTURE_06_07_VALIDATION.md`.

**Why this fixture exists.** `rules.md` §4 states that both conditions of
the Chapter 18 exemption must hold: *"A residential Chapter 18 program is
**not** exempt — the provision applies in full."* Until this fixture that
sentence was never tested. This file is **Chapter 18, residential**. The
exemption does not fire, and this is the **only** configuration in the
fixture set where `(b)(3)` and `(b)(4)` produce findings rather than NOT
APPLICABLE.

**Its NON-PHYSICAL INTERVENTION TRAINING section reads *"No documentation
on file"* — the identical sentence that is correct and must not be
reported on fixtures 01–06.** Here it is a Critical finding. The sentence
did not change; the chapter and level of care did. An auditor that returns
NOT APPLICABLE on this file has demonstrated that its earlier NOT
APPLICABLE calls were **pattern-matching on the sentence**, not applying
the scope rule.

**Hire August 11, 2025 → thirty days = September 10, 2025.** All twelve
`(b)(2)` topics documented September 3, inside the window by seven days.
**The same September 10 deadline governs `(b)(3)`**, which requires the
training *"within thirty (30) days of being hired."*

### Expected FAIL — 1 Critical

| Provision | Finding | Severity |
|---|---|---|
| `450:1-9-5.6(b)(3)` | Program is certified under **Chapter 18 at a residential level of care**. The exemption requires *"outpatient programs subject to Chapter 18"* — both conditions, and the level-of-care condition fails. The provision applies in full. Hired **August 11, 2025**; training due **September 10, 2025**. The file documents no non-physical intervention training, and the employee has provided treatment services since **September 2, 2025**. | Critical |

### Expected FAIL — 1, severity not located in the sourced table

| Provision | Finding | Severity |
|---|---|---|
| `450:1-9-5.6(b)(4)` | Same scope analysis — Chapter 18 **residential**, so no exemption applies. The employee **is** designated: Executive Director designation letter dated **August 12, 2025** names this position. No physical intervention training is documented. The standard states *"A designated employee or volunteer shall not provide direct care services to consumers until completing this training"*; this employee has provided treatment services since **September 2, 2025**. | **UNSOURCED — VERIFY.** No tier for `(b)(4)` was located in the Quality Clinical Standards table this build verified. Severity is **not** inferred from `(b)(3)`'s Critical. |

### The traps this fixture sets in the other direction

**`(b)(3)`'s 2026 update is not yet due.** Calendar year 2026 runs to
December 31, 2026. The finding rests on the 2025 hire-window obligation
alone; also citing a missing 2026 update is **over-reporting and counts as
a false finding**.

**Citing `(b)(2)` on this file is a false finding.** First treatment
service (September 2) precedes the in-service roster date (September 3) by
one day, which looks like a defect and is not: `(b)(2)` allows thirty days
from hire and imposes **no service-delivery condition**. The "before
providing services" language lives in `(a)(2)` — satisfied, privileged
August 25 — and in `(b)(3)`/`(b)(4)`, where it is already captured above.

### Expected PASS

`(a)(1)` · `(a)(2)` privileged August 25, first service September 2 ·
`(a)(4)` annual review January 27, 2026 · all twelve `(b)(2)` topics for
the hire year on September 3 within 30 days of the August 11 hire, and all
twelve again for calendar year 2026 on February 12 · `(c)(2)` twelve
signed entries, each addressing all three required areas.

### Expected NOT APPLICABLE

**None.** This is the only fixture in the set with an empty NOT APPLICABLE
list for `(b)(3)` and `(b)(4)`.

### Expected NOT ASSESSED

`(b)(1)`, `(b)(5)`, `(c)(1)` — agency-level, as on every fixture.

`(b)(6)` — **residential site, so the provision reaches this file**, but it
asks whether the *site* has certified staff *"during all hours of
operation."* One employee's card answers that neither way. Expected:
`NOT ASSESSED — site-level provision, not evidenced by a staff file.`

### Expected UNCLEAR
`(a)(3)` — no age or date of birth in the file. **Not FAIL.**

**Totals: 2 findings — 1 Critical, 0 Necessary, 1 severity unsourced. At least 16 PASS. 0 NOT APPLICABLE. 4 NOT ASSESSED — `(b)(1)`, `(b)(5)`, `(b)(6)`, `(c)(1)`. 1 UNCLEAR — `(a)(3)`.**

---

## How this key is used

| Run | Use |
|---|---|
| **Run 0 — Control** | Graded against this key. Disclosed in the receipt: written by the entrant, graded by the entrant, unblinded. |
| **Run A — Insider** | The tester rules on whether these expected results are themselves correct. Their corrections are logged with IDs, and **a correction to this key counts** — it is published like any other. |
| **Run C — Cold model** | Uses `fixture-03`, which appears in no `examples.md` worked audit. |
| **Falsification #2** | `fixture-04` — all PASS, checker silent. |
| **Falsification #5** | `fixture-05` — no invented citation. |
| **Chapter-branch coverage** | `fixture-06` exercises the Chapter 27 exemption clause · `fixture-07` exercises the not-exempt branch. Both added September 11, 2026 after Run A; neither has been run. See the provenance note at the top of this file. |

## What this key does NOT establish

It is the entrant's reading of the standard, written before the tool
existed. **It is not the state's reading and carries no authority.** Run
A exists precisely to have a compliance professional disagree with it,
and any disagreement is published as a correction rather than quietly
folded in.
