# RECEIPT — Run D (Live use): PERFORMED

**Date:** Friday, September 11, 2026, evening.
**Tester:** **Lisa**, compliance officer at Safe Harbor Behavioral Health. First name only.
**Consent:** given in writing, covering her first name, her verbatim words, and the recording of this session appearing publicly.
**Material:** **a real staff personnel file at the agency**, redacted by her before the run. Not a fixture. It appears nowhere in this repo and never will.
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

**Counts below are transcribed from her spoken narration**, which is the
record in hand at the time of writing:

> *"There were four findings, three critical... two necessary, some nine
> passed, three not applicable, three not assessed, five unclear."*

> ⚠️ **Her spoken counts do not reconcile: "four findings" against "three
> critical, two necessary" is five.** This is stated rather than quietly
> resolved. A spoken summary while scrolling a long output is not a reliable
> count, and **no number here has been adjusted to make the arithmetic
> work.** The exact figures require the tool's own output rather than the
> narration.

**Behavior she described, which does not depend on the counts:**

| What it did | Why it matters |
|---|---|
| Returned **FAIL** on a missing annual review, quoting the requirement and naming the gap | The seven-field format working on real material |
| Returned **FAIL** on missing child-abuse-reporting training — *"13 training modules listed and attested to but none of them described as covering child abuse reporting"* | It read what was there and named what was not, rather than accepting a count of modules as compliance |
| Returned **UNCLEAR**, not FAIL, where no privileging record existed and no first-service date appeared — *"because it couldn't determine the sequencing, or if it existed, it told us that it was unclear"* | **This is the whole thesis.** On a real file with missing records it declined to guess instead of manufacturing a confident finding |
| Flagged two documents for the same training dated a year apart, one signed *"over seven months after the calendar year closed"* | Caught an internal date conflict in a real file |
| Returned **NOT APPLICABLE** on intervention training via the Chapter 27 route | The scope logic Run A said was untested |
| Listed the **PASS** lines individually | `rules.md` requires passes be reported, not just failures |

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
