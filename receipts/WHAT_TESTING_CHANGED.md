# WHAT TESTING CHANGED

**Every defect testing found, and what happened to it.** One page, because
the alternative is sixteen receipts a reader has to assemble themselves.

**Nothing here is new.** Every row links to the receipt that proves it.

---

## The seven

| # | What broke | Found by | What was done |
|---|---|---|---|
| **1** | **The answer key was wrong.** `fixture-02` said *"File reviewed: March 2026"* while containing a licensure review dated **May 4, 2026** — a document two months after the file was supposedly read. [`EXPECTED_RESULTS.md`](EXPECTED_RESULTS.md) listed `(a)(4)` as **PASS** with no note. | Lisa · [Run A](RUN_A_CORRECTIONS.md) | Review date corrected to June 2026. **The correction is published inside the answer key itself**, not quietly applied. **No rule was invented** to catch impossible dates — an impossible date violates no provision of `450:1-9-5.6`, and inventing a standard to catch it is the exact failure `rules.md` §3 exists to prevent. |
| **2** | **The chapter logic had never actually been tested.** All five fixtures were Chapter 18 / outpatient, so `(b)(3)` and `(b)(4)` were always exempted through the same single clause. A correct `NOT APPLICABLE` could not be distinguished from an accidental one. | Lisa · [Run A](RUN_A_CORRECTIONS.md) | Two fixtures added: `fixture-06` (Chapter 27, residential — the Chapter 27 clause is the only available route) and `fixture-07` (Chapter 18, **residential** — the one configuration where `(b)(3)` and `(b)(4)` **apply in full**). Both were executed before the receipt was committed: [`FIXTURE_06_07_VALIDATION.md`](FIXTURE_06_07_VALIDATION.md). |
| **3** | **Severity tiers never got the verification the rule text got.** The regulation was checked word for word — 0.9948 across 1,552 words. The Critical/Necessary tiers came from a different document with no equivalent check. | Lisa · [Run A](RUN_A_CORRECTIONS.md) | `(b)(4)` now ships `Severity: UNSOURCED — VERIFY` and is **never** inferred from `(b)(3)`'s Critical. Adjacency is not a source: `(b)(2)` alone splits across both tiers. Limit written into `rules.md` §8. |
| **4** | **An assumption was baked in and never written down** — whether an annual licensure review is owed for a partial hire year. The rule spells out no grace period; no fixture tested it either way. | Lisa · [Run A](RUN_A_CORRECTIONS.md) | Documented as a stated limit in `rules.md` §8 rather than resolved by guess. |
| **5** | **The first instruction in the README could not be followed.** v1 said *"Drop this whole folder into a Claude project."* The tester pasted one file and worked from it for twenty minutes. | Karen · [Run B](RUN_B_TRANSCRIPT.md) | README v2 names the count, lists all five filenames, covers folder **or** zip **or** loose attachments, and warns: *"If you attach only this page, Claude will answer you, and it will be guessing."* v1 preserved at [`README-v1.md`](README-v1.md). 688 → 869 words. |
| **6** | **A human read files written for the assistant.** She spent most of her twenty-three minutes inside `rules.md` and hit vocabulary that stopped her cold. | Karen · [Run B](RUN_B_TRANSCRIPT.md) | README v2 adds **"Which of these am I supposed to read?"** — *this page, that's it.* The other four are named as written for the assistant, readable if you want to check the tool's work, unnecessary otherwise. |
| **8** | **The auditor miscounts its own findings.** Run on a real staff file, it listed **five** FAILs and summarised them as *"4 findings"*; listed **eight** PASSes and summarised them as *"9 PASS."* The itemised findings are correct — only the tally is wrong, and **it undercounts failures.** Check it yourself against the published output: [`RUN_D_FULL_OUTPUT_REDACTED.md`](RUN_D_FULL_OUTPUT_REDACTED.md) | The real file · [Run D](RUN_D_LIVE_USE.md) | **Found. Not fixed.** No count-verification step was added to `rules.md`: that would be an untested edit to a frozen file, made hours before a deadline, under exactly the pressure this project's method exists to resist. Published as an open defect instead. |
| **7** | **A receipt overstated the evidence against this build.** It claimed Run 0, Run C and the independent agent test had all run against `fixture-02` and missed the date. **None of them had.** Run 0 used `fixture-01`; the other two used `fixture-03`. | Self-audit, before the commit | Corrected in both files to the true version — **nothing had ever been run against `fixture-02`** — and the true version is the stronger one: the defect survived because nothing ever looked. |

### In her words

> *"This one has a 'correct' answer already written up, and it's wrong."*
> — Lisa, on `fixture-02`

> *"The tool has been built and tuned entirely around the exam you're
> studying for, not the one you're actually enrolled in."*
> — Lisa, on the fixture set

> *"I saw where it said file... I thought that was the file. I didn't know
> you meant every attachment."*
> — Karen, on why she never loaded the folder

> *"You need to write it — add download each attachment."*
> — Karen, writing the fix herself

---

## Still broken. Not fixed tonight.

This half is what makes the half above worth reading.

**The folder still does not ship as one downloadable bundle.** Run B's setup
failed because five loose email attachments would not send as a folder.
README v2 teaches a reader to cope with that. **It does not fix the cause.**

**README v2 has never been tested on anyone.** v1 was tested and it failed.
v2 is the entrant's implementation of what the tester said, written from her
own words — but no one has been handed v2 and asked to use it. The measured
door has been measured **once**, and the replacement is unmeasured.

**The auditor has been run against exactly one real staff file.** For most of
the day this line read *"has never been run against a real staff file"* —
that was true when it was written and stopped being true a few hours later,
when the compliance officer ran it live against a real file at the agency.
See [`RUN_D_LIVE_USE.md`](RUN_D_LIVE_USE.md). **n = 1.** One file, one
reviewer, one sitting. The earlier receipt saying it would not happen is kept
unedited at [`RUN_D_NOT_RUN.md`](RUN_D_NOT_RUN.md).

**Run B does not test what it was designed to test.** Because the files
arrived as loose attachments rather than a folder, the run cannot say whether
the README routes a reader who actually *has* the folder. That is still
untested. See [`DEVIATIONS.md`](DEVIATIONS.md).

**The no-help rule was not held in Run B.** Coaching, nudges and
encouragement while the tester was failing — all of it stays in
[`RUN_B_RAW_TRANSCRIPT.md`](RUN_B_RAW_TRANSCRIPT.md), uncut.

**Nothing verifies the summary line.** `check.py` confirms that a cited
provision exists in `reference/`. **It does not count anything.** 15 of 15
gates passing says nothing about whether a tally is correct — which is
exactly how defect **#8** above reached a real file unnoticed. The gate that
would catch it does not exist.

**n = 1 everywhere.** One insider, once. One outsider, once. One cold model,
once. One control, once. **One real staff file, once.** No result here is a
rate.

---

## Why this page exists

Four of these seven were found by other people, and two of those land
squarely against the build. The seventh was found by auditing this project's
own receipts before publishing them.

**A list of only the fixes would read as marketing.** The same reason the
audit output ships its PASS lines applies here: a report that shows only what
went wrong — or only what went right — is harder to trust than one that shows
both.

*The audit shouldn't be the first time you find out. Neither should the
demo.*
