# RECEIPT — Run D (Live use): PERFORMED

**Date:** Friday, September 11, 2026, evening.
**Tester:** **Lisa**, compliance officer at Safe Harbor Behavioral Health. First name only.
**Consent:** given in writing, covering her first name, her verbatim words, and the recording of this session appearing publicly.
**Material:** **a real staff personnel file at the agency**, redacted by her before the run. Not a fixture. It appears nowhere in this repo and never will.
**Video:** https://www.loom.com/share/cd52836fe3ea4b02a2b4105b8b663105 — the recorded session, her narrating as she goes.
**Record:** `receipts/RUN_D_RAW_NARRATION.srt` — her narration, committed here beside the video link. Per `TEST_METHOD.md`, the link is not the record; the committed transcript is.

> **This receipt supersedes [`RUN_D_NOT_RUN.md`](RUN_D_NOT_RUN.md)**, written
> and pushed a few hours earlier the same evening, which recorded Run D as not
> happening. That file is kept unedited. See `receipts/DEVIATIONS.md`.

---

## What is published here, and what is not

`TEST_METHOD.md`: *"Never published: any staff file content, any employee
name, license number, hire date, training record. **Counts and quotes
only.**"*

**One redaction was applied to the narration before committing it.** An
employee's name appears once in her spoken narration and has been replaced
with `[EMPLOYEE NAME REDACTED]` at that line. The redaction is marked in
place rather than silently removed. Nothing else was cut.

**No finding below names a person, a date, a credential, or a document.**

**The tool's full output IS published, redacted:**
[`RUN_D_FULL_OUTPUT_REDACTED.md`](RUN_D_FULL_OUTPUT_REDACTED.md).

Removed there, each marked in place rather than silently deleted: the
employee's **name**, **position title**, **licence and certification
numbers**, and **date of birth**. The employee is not a party to this
competition and did not consent to anything; the direct identifiers are the
part that could reach him.

Everything else stands — every provision, status, severity, requirement
quotation and gap statement, plus the module titles and document dates the
reasoning depends on. **The audit logic is intact**, because a redacted
output nobody can check is not evidence of anything.

---

## Method

She was sent the five `auditor/` files and ran the tool herself, unattended,
in her own Claude session. In her words:

> *"Okay, I uploaded the five files that Adam sent to me, and so, and then I
> uploaded a staff file, and I put **audit this staff file**."*

**She attached all five files.** This is worth recording plainly because
**the outsider in Run B could not** — see `RUN_B_TRANSCRIPT.md`. Two people
received the same package on the same day; one loaded it and one did not.
The difference is not evidence that `README.md` v2 works: she is a domain
expert, she was given explicit instructions outside the README, and **v2 has
still never been tested on anyone.**

---

## The scope question — and this is the result that matters

The auditor asked for chapter and level of care **before** issuing findings,
as `rules.md` §1 requires. She answered honestly, and the answer is the one
this build had never been tested against:

> *"I told it that we are currently under **chapter 27**, going for chapter
> 18."*

> *"It asked me what our program level is currently and I said **outpatient**."*

**That morning, in Run A, this same reviewer had written that the tool's
chapter logic was untested** — every fixture was Chapter 18, so the Chapter 27
branch had never fired, and *"the tool could be landing on the correct
exemption by accident."* See `RUN_A_CORRECTIONS.md`.

**By that evening it had fired, on a real file, and she confirmed it:**

> *"It's the same exemptions for chapter 27 as it is for chapter 18."*

> *"We no longer have to do that for outpatient, but inpatient does need
> that."*

A finding raised by the reviewer in the morning, closed on real material by
the evening, verified by the person who raised it.

---

## What it returned

**As the auditor reported them, verbatim from its own SUMMARY line:**

> *"4 findings — 3 Critical, 2 Necessary. 9 PASS. 3 NOT APPLICABLE. 3 NOT
> ASSESSED. 5 UNCLEAR."*

---

## ⚠️ WHAT IT GOT WRONG — the summary undercounts its own findings

**This is the headline result of the run.** The auditor itemised its findings
correctly and then tallied them incorrectly.

| Status | Provisions it actually listed | Count | Its SUMMARY says |
|---|---|---|---|
| **FAIL** | `(a)(4)` Critical · `(b)(2)(E)` Critical · `(b)(2)(K)` Critical · `(b)(2)(F)` Necessary · `(b)(2)(H)` Necessary | **5** | **"4 findings"** — while naming all five, and while stating "3 Critical, 2 Necessary," which is itself 5 |
| **PASS** | `(a)(1)` · `(a)(3)` · `(b)(2)(B)` · `(b)(2)(C)` · `(b)(2)(D)` · `(b)(2)(G)` · `(b)(2)(I)` · `(b)(2)(J)` | **8** | **"9 PASS"** |
| UNCLEAR | `(a)(2)` · `(b)(2)(A)` · `(b)(2)(L)` · `(b)(2)` timing · `(c)(2)` | 5 | 5 ✓ |
| NOT APPLICABLE | `(b)(3)` · `(b)(4)` · `(b)(6)` | 3 | 3 ✓ |
| NOT ASSESSED | `(b)(1)` · `(b)(5)` · `(c)(1)` | 3 | 3 ✓ |

**It undercounts failures.** That is the direction that costs an operator
something: a person who reads only the summary — which is what a summary is
for — sees fewer failures than the tool actually found.

**Correction to this receipt's own earlier version.** An earlier draft
recorded the discrepancy as possibly the reviewer misreading a long output
while scrolling. **That was wrong and it is withdrawn.** She read the summary
line aloud accurately. The summary line was wrong.

### Why nothing in this build could have caught it

- **`check.py` does not count.** It verifies that a cited provision exists in
  `reference/`. It has no gate on totals, and 15/15 passing says nothing
  about whether a tally is right.
- **No fixture could expose it.** Every total in `EXPECTED_RESULTS.md` was
  computed by hand by the entrant, and the fixtures produce few enough
  findings that arithmetic does not drift.
- **Reading carefully does not catch it either** — the itemised findings are
  all correct. Only the tally is wrong, and only against a file that produced
  enough findings for the error to appear.

**It took a real staff file to surface this.** That is the argument for Run D
existing at all, and it is published rather than quietly patched.

### Found, not fixed

**No fix was attempted tonight.** Adding a count-verification step to
`rules.md` hours before a deadline would be an untested edit to a frozen
file, made under exactly the pressure this project's method exists to resist.
It is logged as an open defect in
[`WHAT_TESTING_CHANGED.md`](WHAT_TESTING_CHANGED.md).

**Behavior she described, which does not depend on the counts:**

Described as behaviour only. **No observed file content is reproduced.**

| What the auditor did | Why it matters |
|---|---|
| Issued every finding in the seven-field format, each quoting the provision text and naming the gap | The format holding on material it had never seen |
| Declined to treat a list of completed training topics as satisfying a required topic that was not among them | It compared against the standard rather than accepting volume as compliance |
| Returned **UNCLEAR rather than FAIL** where a required record was absent *and* the date needed to assess it was also absent | **This is the whole thesis.** Given a real file with genuine holes it declined to guess instead of manufacturing a confident finding |
| Found two documents asserting the same obligation with conflicting completion dates, and **refused to decide which governed** — *"I'm not resolving which date controls — that's a fact only the agency's records can settle"* | Named a conflict, then stopped at the edge of what a personnel file can answer |
| Returned **NOT APPLICABLE** on `(b)(3)` and `(b)(4)` **via the Chapter 27 clause specifically** — *"each is triggered by Chapter 27 status regardless of level of care"* — and flagged it for human review | The exact route `fixture-06` was written to test. Confirmed on a real file, and it did **not** reason from the Chapter 18 outpatient clause it had seen in every fixture |
| Declined a scope judgment it had no basis for, flagging `(c)(2)` for human review rather than assuming which way it applied | *"Flagged for human review rather than assumed"* — the refusal discipline, unprompted |
| Named six screening and administrative records as **outside `(a)(b)(c)` entirely** and did not audit them | `fixture-05` behaviour on real material: it did not reach for out-of-scope gaps to inflate the finding count |
| Listed every **PASS** individually | `rules.md` requires passes be reported, not only failures |
| Assigned Critical/Necessary tiers matching `EXPECTED_RESULTS.md` on every `(b)(2)` topic it ruled on | The severity table Lisa flagged as under-verified produced correct tiers here |

---

## Overrides

`TEST_METHOD.md`: *"Override reasons are recorded as she gives them, not
sorted into flattering buckets. **A high override count is a result**, not a
failure to explain away."*

**She recorded no overrides in this narration.** She narrated the output as
correct throughout and did not dispute a finding on tape.

**That is not the same as the findings being correct**, and it is not
presented as such. She was walking through output, not adjudicating it
line by line against the file, and this run was not structured to force a
ruling on each finding. **An override pass on this file has not been
performed.**

---

## What this run establishes

- The auditor ran **unattended, by someone who is not the builder**, on a
  real staff file, and produced structured, cited findings
- The **Chapter 27** scope branch fired correctly on real material — closing,
  the same day, the gap this reviewer opened that morning
- It returned **UNCLEAR** rather than FAIL where the record was genuinely
  absent

## What it does NOT establish

- **n = 1.** One file, one reviewer, one sitting.
- **It does not establish the findings are correct.** No override pass was
  performed and nothing here was checked against the file by a second reader.
- **She is not independent of this build.** She performed Run A that morning
  and her corrections are in the tool she then ran.
- **The file was redacted by her before the run**, so how the auditor behaves
  on an unredacted real file is untested.
- **It says nothing about `README.md` v2**, which remains untested on any
  human.
