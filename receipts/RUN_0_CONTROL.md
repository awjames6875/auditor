# RECEIPT — Run 0 (Control)

**Date:** Monday, September 7, 2026
**n = 1.** One control run, as fixed in advance by `TEST_METHOD.md`'s fairness terms. Not repeated to get a better result.

**Disclosed, as `TEST_METHOD.md` requires:** this control was run *after* `receipts/EXPECTED_RESULTS.md` already existed, by the person who wrote that key (Adam), and is graded below against that same key, by him. Unblinded.

---

## Method

Fresh `claude.ai` chat — no project, no memory of this build, no auditor folder attached, no answer key attached. Given exactly:

- The raw regulation text of `450:1-9-5.6`, subsections (a) through (f) only — not this repo's provenance header, not the "SCOPE CONDITIONS AN AUDITOR MUST APPLY" summary table added to `reference/450-1-9-5.6.md` for the auditor's own use
- `fixtures/fixture-01-missing-topics.md`, verbatim
- The fairness-required fact, stated once: *"This file is from an outpatient program certified under Chapter 18."*
- The prompt, verbatim: *"Audit this staff file against this standard."*

**One artifact removed before saving below:** a failed `/model sonnett` slash command and a `PASTED` marker landed in the clipboard when this was copied back into the working session. That's paste noise from this repo's own tooling, not part of the Run 0 chat itself, and has been stripped. Nothing from the model's actual response was touched.

---

## Full response (verbatim)

> AUDIT RESULT — Staff File 2025-014 (Dana Whitfield)
>
> **Bottom line:** 1 deficiency, 2 items I cannot verify from this file, 3 requirements correctly exempt.
>
> The deficiency is significant — 9 of 12 required in-service topics are missing for the hire year, including several that carry heightened scrutiny in a substance use outpatient setting (confidentiality, child abuse reporting, suicide risk, trauma-informed care).
>
> Everything else in the file is clean.
>
> **SCOPE APPLIED FIRST**
>
> This program is outpatient, Chapter 18. Three requirements in the standard carve that out explicitly, so they are not findings here even though the file shows no documentation:
>
> | Requirement | Exemption language in the standard | Result |
> |---|---|---|
> | (b)(3) Non-physical intervention training | "shall not apply to… outpatient programs subject to Chapter 18" | Not applicable |
> | (b)(4) Physical intervention designation | "shall not apply to… outpatient programs subject to Chapter 18" | Not applicable |
> | (b)(6) First aid / CPR coverage | Applies to residential level of care and/or Chapter 23 sites | Not applicable |
>
> Do not write these up. The file's "No documentation on file" entries for intervention training are correct, not gaps.
>
> Subsections (d) clinical records, (e) discharge summary, (f) critical incidents are outside this folder's scope per the standard's own notation, and are also record-level rather than personnel-file items.
>
> **FINDING 1 — IN-SERVICE TRAINING (b)(2) — DEFICIENCY**
>
> Rule: In-service training on all twelve listed topics is required within 30 days of hire date and each calendar year thereafter.
>
> Hire date: March 4, 2025 → 30-day deadline: April 3, 2025
>
> Documented (3 of 12): (A) Fire and safety — Mar 18, 2025 ✅ · (B) Universal precautions / infection control — Mar 18, 2025 ✅ · (C) Consumer's rights / MH Patient's Bill of Rights — Mar 25, 2025 ✅
>
> Missing (9 of 12): (D) Confidentiality · (E) OK Child Abuse Reporting and Prevention Act, 10 O.S. §§ 7101-7115 · (F) Facility policy and procedures · (G) Cultural competence · (H) Co-occurring disorder competency · (I) Trauma informed service provision · (J) Crisis intervention · (K) Suicide risk assessment, prevention, and response · (L) Age/developmentally appropriate training — no documentation for any of the nine.
>
> Note on (L): The standard qualifies this one with "where applicable." If this program serves adults only, (L) may not apply. I can't determine the population served from this file. Verify before citing it.
>
> **ITEMS I CANNOT VERIFY FROM THIS FILE**
>
> 1. Age — (a)(3). The rule requires direct care staff to be at least eighteen (18). This file contains no date of birth or age attestation. A Certified Behavioral Health Case Manager II almost certainly exceeds 18, but the standard requires documentation, and I'm not going to infer it. Flag as "unable to verify," not as a violation.
>
> 2. Annual review timing — (a)(4). The rule requires a review each calendar year of current licensure, certifications, and privileging qualifications. CY 2025: Initial credentialing + privileging completed March 14, 2025. CY 2026: Annual review completed February 2, 2026 ✅. My read: initial privileging in the hire year likely satisfies CY 2025, and CY 2026 is documented. I am not certain this is how ODMHSAS interprets the hire-year requirement — some surveyors expect a distinct annual review separate from initial credentialing. Verify against your agency's prior survey history or ask your ODMHSAS liaison.
>
> **COMPLIANT ITEMS**
>
> | Requirement | Evidence in file |
> |---|---|
> | (a)(1) Documented qualifications specific to services | CBHCM II cert #CM-44192 + "Case Management in Substance Use Treatment," 6 hrs, Feb 26, 2025 |
> | (a)(2) Credentials verified + privileged prior to treatment | Privileging signed Mar 14, 2025; first service Mar 20, 2025 — 6 days of margin |
> | Current credential status | Cert expires Jan 31, 2027 — current as of March 2026 review |
> | (c)(1) Documentation of clinical supervision provided | 12-entry log, Apr 2025 – Feb 2026, signed and dated by supervising LADC |
> | (c)(2)(A)(B)(C) Supervision content | All three required elements documented per entry |
>
> **TWO OBSERVATIONS — NOT FINDINGS**
>
> 1. Supervision start gap. First service was March 20, 2025; the supervision log begins April 2025 — roughly two weeks unlogged. The standard sets no start-date requirement for supervision, so this is not citable. Worth tightening as practice.
>
> 2. Supervision frequency. Subsection (c)(1)(B) requires the facility's policy to define case review frequency. Twelve entries over eleven months averages monthly. I cannot judge compliance without seeing the policy — if the policy says weekly or biweekly, this log falls short of the facility's own stated standard, which surveyors do cite.
>
> **CORRECTIVE ACTION — START HERE**
>
> Step 1 (do this first): Confirm whether any of the nine missing topics were delivered but documented elsewhere — an agency-wide training roster, LMS export, or all-staff sign-in sheet that never made it into the personnel file. A filing gap and a training gap get very different corrective action plans.
>
> Once you tell me which of those two it is, I'll write the next step.

---

## Graded against `receipts/EXPECTED_RESULTS.md` (fixture-01)

| Item | Expected | Run 0 produced | |
|---|---|---|---|
| Missing (b)(2) topics | D, E, F, G, H, I, J, K, L (9 total) | Identical set, all 9 | ✅ |
| Severity split: 4 Critical (D, E, J, K) vs 5 Necessary (F, G, H, I, L) | Two-tier split | **No severity tier at all** — all 9 called one undifferentiated "deficiency" | ❌ |
| (b)(3), (b)(4) | NOT APPLICABLE, exemption quoted | Identical, exemption sentence quoted | ✅ |
| (b)(6) | NOT APPLICABLE (scope trap — not required for this fixture, but correct if caught) | Caught and applied correctly, unprompted | ✅ |
| (a)(3) | UNCLEAR — not FAIL | "Unable to verify," explicitly not treated as a violation | ✅ |
| (a)(1), (a)(2) | PASS | PASS, with the 6-day margin shown | ✅ |
| (a)(4) | Clean PASS | Marked as PASS but flagged as *uncertain* whether hire-year privileging satisfies CY2025 | ⚠️ partial — correct call, added doubt the key doesn't carry |
| (b)(1), (b)(5) | NOT ASSESSED — agency-level, must be stated explicitly | **Not mentioned at all** — silent omission | ❌ |
| (c)(1) | NOT ASSESSED — agency-level (written policies/procedures), not answerable from a personnel file | Marked **PASS**, citing the personnel file's supervision log — the log is actually (c)(2) evidence, not (c)(1) | ❌ |
| (c)(2)(A)(B)(C) | PASS, twelve signed entries | PASS, correctly reasoned | ✅ |
| Attempts to fix the file | N/A (not asked; falsification #3 not tested here) | No — ends by asking a clarifying question, does not rewrite the file | ✅ |

---

## What this shows

**Strong, and worth taking seriously:** without any auditor instructions — just the raw regulation text, the fixture, and one fact about Chapter 18 — the model found exactly the right 9 missing topics, applied both real exemptions correctly, caught the unprompted (b)(6) scope trap, and got the "don't guess on age" instinct right. That's a genuinely capable baseline, and any claim that the auditor is doing all the work would be wrong.

**What the raw model visibly can't do without the instructions:**

1. **No severity tier.** It has no source for Critical vs Necessary (that's the ODMHSAS Provider Certification Manual, which lives in the auditor's instructions, not the raw rule text) — so all 9 missing topics land in one undifferentiated bucket. This is the clearest, most defensible differentiator for what `rules.md` adds.
2. **Silent on agency-level provisions.** (b)(1) and (b)(5) are just never mentioned, rather than explicitly marked NOT ASSESSED. A reader can't tell "not answerable from this file" from "the model forgot" — exactly the ambiguity `EXPECTED_RESULTS.md` calls out as its own failure mode.
3. **Scope confusion on (c)(1) vs (c)(2).** The model credited the personnel file's supervision log toward (c)(1) — the *agency's* written policy requirement — when that log is actually (c)(2) evidence (supervision occurring). (c)(1) should have been NOT ASSESSED from a staff file. This is precisely the kind of agency-level/personnel-file conflation the auditor's scope rules exist to prevent, caught here on the very first control run.

**One honest overcaution:** it added doubt to (a)(4) that the answer key doesn't carry — the key treats initial hire-year privileging as clearly satisfying the CY2025 obligation; the model wasn't sure. Not a wrong call, just a harder one than the key gives it credit for. Worth a second look at whether the key's confidence is justified, or whether the model's hedge is the more defensible read — flagged here rather than resolved.
