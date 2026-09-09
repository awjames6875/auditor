# RECEIPT — Run C (Cold Model)

**Date:** Wednesday, September 9, 2026
**Run by:** Adam James, fresh `claude.ai` session, no memory of this project.
**Video:** https://www.loom.com/share/14c7b90282ba48a68478d7a71ddd264e (covers this run and `FALSIFICATION_3_REFUSAL.md`, same continuous session)

---

## Method

All six `auditor/`-plus-fixture files attached individually, per `TEST_METHOD.md`:

- `auditor/README.md`
- `auditor/identity.md`
- `auditor/rules.md`
- `auditor/examples.md`
- `auditor/reference/450-1-9-5.6.md`
- `fixtures/fixture-03-no-supervision.md`

Prompt, verbatim: *"Audit this staff file."*

No coaching. No follow-up questions asked of the model beyond the one prompt.

---

## Full response (verbatim)

*(reproduced below exactly as returned — see the message this receipt was written from for the complete original formatting)*

**One finding: `(c)(2)` clinical supervision — FAIL, Critical Standard.** Everything else in scope either passes, is exempt, or can't be answered from a personnel file.

**SCOPE:** Chapter 18 (Alcohol and Drug Abuse Services), outpatient — read from the file's own PROGRAM CONTEXT block, not asked.

**KEY DATES:** Date of hire Nov 12, 2024 · First treatment service Dec 2, 2024 · File reviewed March 2026. Employee is a licensure candidate under supervision (LPC-C, cand. #LC-3054).

**FINDING — `OAC 450:1-9-5.6(c)(2)`, Critical, FAIL.** A signed supervision agreement dated Nov 25, 2024 names the supervising LPC and states supervision will occur weekly. No supervision log, session note, summary, or other record of supervision *occurring* appears anywhere in the file, covering Dec 2, 2024 through the March 2026 review — roughly 15 months. Required: ongoing clinical supervision "shall be provided" addressing appropriateness of treatment, treatment effectiveness, and feedback. Gap: the agreement documents supervision was *arranged*; `(c)(2)` requires documentation it was *provided*. Nothing documents supervision occurring.

**PASS:**
- `(a)(1)` — licensure candidacy verification + CBT-for-substance-use training, 15 hrs, specific to services delivered
- `(a)(2)` — privileged Nov 25, 2024; first service Dec 2, 2024 — 7-day margin
- `(a)(4)` — annual review completed Oct 15, 2025 for CY2025; CY2026 still open until Dec 31, 2026 (correctly not cited); flagged an open question about whether initial credentialing satisfies the hire-year (2024) obligation — "the rule text does not settle" this, sent for human review
- `(b)(2)(A)` through `(L)`, all twelve topics, twice — hire-year (completed Dec 3, 2024, 9 days inside the 30-day window from Nov 12 hire) and again for calendar year 2025 (Aug 14, 2025). Severity split correctly: `(A)(B)(C)(D)(E)(J)(K)` Critical, `(F)(G)(H)(I)(L)` Necessary.

**NOT APPLICABLE:**
- `(b)(3)` — outpatient/Chapter 18 exemption, quoted, flagged for human review
- `(b)(4)` — same exemption, plus employee not designated for it, flagged for human review
- `(b)(6)` — outpatient, not Chapter 23, not required — caught unprompted, flagged for human review

**NOT ASSESSED — agency-level:** `(b)(1)`, `(b)(5)`, `(c)(1)` (written supervision policy — explicitly distinguished from `(c)(2)`'s supervision-occurring question)

**UNCLEAR:** `(a)(3)` — no age/DOB in file, correctly not rounded to FAIL

**SUMMARY:** 1 finding (1 Critical, 0 Necessary) · 15 PASS · 3 NOT APPLICABLE · 3 NOT ASSESSED · 1 UNCLEAR. Closed with two stated limits: it audits the document not the agency, and the in-service roster is read at topic level, not sub-content level.

---

## Graded against the six Run C conditions

| # | Condition | Result |
|---|---|---|
| 1 | Reads the README first and follows it, doesn't improvise | ✅ Output shape matches `rules.md` §9 exactly (scope line → key dates → findings → PASS → summary → stated limits); seven-field finding schema followed with no extra fields |
| 2 | Findings cite subsection-level provisions present in `reference/` | ✅ Every citation real, full, subsection-level — `(c)(2)`, `(a)(1)`, `(a)(2)`, `(a)(4)`, `(b)(2)(A)`–`(L)`, `(b)(3)`, `(b)(4)`, `(b)(6)`, `(b)(1)`, `(b)(5)`, `(c)(1)`, `(a)(3)` |
| 3 | Assigns severity using Critical/Necessary tiers | ✅ Correctly tiered where `rules.md` §3 assigns a tier; explicitly wrote "no tier assigned for this provision in rules.md" rather than inventing one where it doesn't — matches the "never invent a severity" rule exactly |
| 4 | Reports at least one PASS, not only failures | ✅ 15 PASS lines |
| 5 | Does not rewrite or fix the staff file | ✅ No suggested text, no template, no corrected version anywhere |
| 6 | Asks for chapter and level of care before issuing findings | ⚠️ **See note below** |

### Note on condition 6

The model did **not** ask a question. It read Chapter 18/outpatient from the fixture's own PROGRAM CONTEXT block and said so — *"read from the file's own PROGRAM CONTEXT block, not asked."*

That is not a deviation from `rules.md` — it's the literal instruction. `rules.md` §1, Step 0: *"If the file states it — many do, in a header — read it there and say so rather than asking again."* Every one of the five shipped fixtures states chapter/level-of-care in a PROGRAM CONTEXT block by design (per `EXPECTED_RESULTS.md`'s "Scope of every fixture" section), so a correctly-instructed auditor will **never** literally ask against any of them — it will always find the answer already there.

**`TEST_METHOD.md`'s condition 6 was worded before this refinement existed and doesn't match the tool's actual, better-designed behavior.** The intent behind condition 6 — establish scope from a disclosed source *before* issuing findings, rather than guessing — was fully met. The literal wording ("asks") was not. This is exactly the kind of method/tool mismatch `DEVIATIONS.md` exists to log honestly rather than silently reinterpreting.

**Logged.** See `receipts/DEVIATIONS.md`, September 9, 2026 entry — condition 6 is recorded there as satisfied in substance (scope established from a disclosed source before any findings issued) rather than by its literal wording, with the reasoning stated plainly rather than quietly reinterpreted.

---

## Graded against `receipts/EXPECTED_RESULTS.md` (fixture-03)

| Item | Expected | Produced | |
|---|---|---|---|
| Finding | `(c)(2)` FAIL, Critical, agreement-not-supervision | Identical, same trap named the same way | ✅ |
| `(a)(1)`, `(a)(2)` | PASS, 7-day margin | Identical | ✅ |
| `(a)(4)` | PASS | PASS, plus an added (unrequired) hedge about hire-year timing — same pattern seen in Run 0 | ⚠️ minor over-caution, not wrong |
| `(b)(2)` all 12, hire-year + CY2025 | PASS, both cycles | Identical, arithmetic shown both times | ✅ |
| `(b)(3)`, `(b)(4)` | NOT APPLICABLE | Identical, plus unprompted `(b)(6)` | ✅ |
| `(b)(1)`, `(b)(5)`, `(c)(1)` | NOT ASSESSED | Identical — and correctly separated from `(c)(2)` | ✅ |
| `(a)(3)` | UNCLEAR | Identical | ✅ |
| Totals | 1 finding / 15+ PASS / 3 N/A / 3 N/ASSD / 1 UNCLEAR | Exact match on every count | ✅ |

**Every status call matches the answer key.** No false finding, no missed exemption, no invented citation, no agency-level provision reported as FAIL.

---

## What this shows, compared to Run 0

The single clearest before/after: **Run 0** (raw model, no instructions) credited the personnel file's supervision log toward `(c)(1)` — the agency's *written policy* requirement — conflating it with `(c)(2)`'s supervision-occurring question. **Run C** (with `auditor/`'s instructions) correctly separates them: `(c)(1)` NOT ASSESSED as agency-level, `(c)(2)` FAIL as the personnel-file question. That's `rules.md` §5's scope table doing exactly the work it was written to do — caught on the first real cold run, on a fixture the instructions were never trained against.

The only open item is condition 6's wording, noted above.
