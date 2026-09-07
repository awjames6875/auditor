# EXPECTED_RESULTS.md — the answer key

**Written:** Sunday, September 6, 2026 — **before Run 0 and before any
auditor instruction file existed.** Committed the day it was written.

**Location matters.** This file lives in `receipts/`, **outside**
`auditor/`. A judge who drops the `auditor/` folder into a project
cannot load this key by accident. Neither can the auditor.

---

## Scope of every fixture

All five fixtures describe a program **certified under Chapter 18** at an
**outpatient** level of care. That is stated in a PROGRAM CONTEXT block
at the top of each file, so an auditor that asks for chapter and level of
care before issuing findings can find the answer without guessing.

**Consequence, applied to all five:**

| Provision | Result | Why |
|---|---|---|
| `450:1-9-5.6(b)(3)` non-physical intervention training | **NOT APPLICABLE** | *"This standard shall not apply to facilities or programs subject to Chapter 27 of this Title **or outpatient programs subject to Chapter 18 of this Title**."* |
| `450:1-9-5.6(b)(4)` physical intervention training | **NOT APPLICABLE** | Same sentence structure, adding Chapter 16. Also: no employee here is designated for it. |

Every fixture says *"No documentation on file"* for both. **That absence
is correct and must not be reported as a finding.** An auditor that
reports `(b)(3)` against any of these five has produced the exact false
finding this build exists to prevent.

**Reporting NOT APPLICABLE and quoting the exemption sentence is the
expected behavior — not silence.** Silence and a correct exemption call
must not look identical.

---

## Agency-level provisions — expected on ALL five fixtures

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

Two more, also expected on all five:

| Provision | Expected |
|---|---|
| `(a)(3)` direct care staff at least 18 | `UNCLEAR` — no fixture documents age or date of birth. **Not FAIL.** |
| `(b)(6)` first aid / CPR | `NOT APPLICABLE` — outpatient. Reaches residential and Chapter 23 sites only. |

> `(b)(6)` is the scope trap. It is a **real** provision, so `check.py`
> accepts a citation to it. Only the level-of-care check catches the
> error. See `fixture-05`.

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
| `(b)(3)` | Critical *(not applicable here — see above)* |
| `(c)(2)` | Critical |

---

## A ruling that applies to every fixture

**Calendar year 2026 is still open.** Each fixture is reviewed in
**March 2026**. `(b)(2)` requires in-service *"within thirty (30) days of
each employee's hire date and each calendar year thereafter."* A calendar
year 2026 obligation does not come due until December 31, 2026.

**No fixture may be cited for a missing 2026 in-service.** An auditor
that reports one has over-reported, and that counts as a false finding
in Run A and Run C scoring.

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

## How this key is used

| Run | Use |
|---|---|
| **Run 0 — Control** | Graded against this key. Disclosed in the receipt: written by the entrant, graded by the entrant, unblinded. |
| **Run A — Insider** | The tester rules on whether these expected results are themselves correct. Their corrections are logged with IDs, and **a correction to this key counts** — it is published like any other. |
| **Run C — Cold model** | Uses `fixture-03`, which appears in no `examples.md` worked audit. |
| **Falsification #2** | `fixture-04` — all PASS, checker silent. |
| **Falsification #5** | `fixture-05` — no invented citation. |

## What this key does NOT establish

It is the entrant's reading of the standard, written before the tool
existed. **It is not the state's reading and carries no authority.** Run
A exists precisely to have a compliance professional disagree with it,
and any disagreement is published as a correction rather than quietly
folded in.
