# RUN D — the auditor's full output, redacted

**Date:** Friday, September 11, 2026
**Run by:** **Lisa**, compliance officer, in her own Claude session, unattended.
**Material:** a **real staff personnel file** at the agency. Not a fixture. The file itself appears nowhere in this repo.
**Receipt:** [`RUN_D_LIVE_USE.md`](RUN_D_LIVE_USE.md) · **Narration:** [`RUN_D_RAW_NARRATION.srt`](RUN_D_RAW_NARRATION.srt) · **Video:** [loom.com/share/cd52836fe3ea4b02a2b4105b8b663105](https://www.loom.com/share/cd52836fe3ea4b02a2b4105b8b663105)

---

## What was redacted, and what was not

Redactions are marked **in place**, never silently deleted. Every one is a
direct identifier of the employee whose file this is — he is not a party to
this competition and did not consent to anything.

**Redacted:** name · position title · licence and certification numbers ·
date of birth.

**Not redacted:** every provision, status, severity, requirement quotation,
and gap statement. Training module titles. Document dates. **The audit
reasoning is intact** — the point of publishing this is that the reasoning
can be checked.

The agency name appears elsewhere in this repo by its owner's choice and is
not treated as a redaction target.

---

## Prompt

> **"Audit this staff file"**

Chapter and level of care were supplied in response to the auditor's own two
questions: **Chapter 27 currently, Chapter 18 certification in progress** ·
**outpatient**.

---

## Output

> Got it — Chapter 27 currently, with Chapter 18 certification in progress. That covers the (b)(3)/(b)(4) exemption question once I also know level of care.
>
> What is the program's level of care — outpatient, residential, or inpatient?

> Chapter 27, outpatient — both (b)(3) and (b)(4) exemptions apply on that basis alone (each is triggered by Chapter 27 status regardless of level of care), and (b)(6) is out of scope as an outpatient, non-Chapter-23 site.
>
> I read all sixteen files in the folder. Four (OSBI ×2, OIG ×2, CCRR, CSW) are background/exclusion screening records — outside 450:1-9-5.6(a)(b)(c) entirely, noted at the end and not otherwise discussed. The rest are training, licensure, and job-description records for **[EMPLOYEE NAME REDACTED]**, **[POSITION REDACTED]**.
>
> **SCOPE:** Chapter 27, outpatient (from your answers) — working toward Chapter 18.
> **KEY DATES:** Hire date — not documented anywhere in the file. First treatment-service date — not documented. Job description acknowledgment signed 9/17/2025 (not stated as a hire date; I'm not treating it as one). Audit performed against today, 9/11/2026.

### FINDINGS

```
Provision:  OAC 450:1-9-5.6(a)(4)
Severity:   Critical Standard
Status:     FAIL
Located:    Whole file — no annual-review document found.
Observed:   No dated, signed annual review of licensure/certifications/
            qualifications appears anywhere in the file. Separately, the
            two licenses that are on file are themselves past their
            stated expiration dates as of today (9/11/2026): the LADC/MH
            license (#[REDACTED]) shows "Expires: 6/30/2026," and the LPC
            license (#[REDACTED]) shows "Expiration Date: 06/30/2026." No
            renewal document for either is in the file.
Required:   "Each facility or program shall minimally perform a review
            each calendar year of current licensure, certifications, and
            current qualifications for privileges to provide specific
            treatment services."
Gap:        No review document exists, and the credentials that would be
            the subject of that review are documented as expired,
            unrenewed, as of the review date.

Provision:  OAC 450:1-9-5.6(b)(2)(E)
Severity:   Critical Standard
Status:     FAIL
Located:    Both 2025 Staff Training Attestation & Sign-In Sheets — the
            13-module list.
Observed:   Thirteen training modules are listed and attested to. None
            is titled or described as covering child abuse reporting.
Required:   "Oklahoma Child Abuse Reporting and Prevention Act, 10 O.S.
            §§ 7101-7115."
Gap:        This topic does not appear among the modules the attestation
            documents.

Provision:  OAC 450:1-9-5.6(b)(2)(K)
Severity:   Critical Standard
Status:     FAIL
Located:    Same attestation, 13-module list.
Observed:   Module 13, "Crisis Prevention & De-Escalation Techniques,"
            is the nearest topic present. No module addresses suicide
            risk specifically.
Required:   "Suicide risk assessment, prevention, and response."
Gap:        Crisis de-escalation is not suicide risk assessment; the
            attestation does not document this topic.

Provision:  OAC 450:1-9-5.6(b)(2)(F)
Severity:   Necessary Standard
Status:     FAIL
Located:    Same attestation.
Observed:   No module titled or described as facility policy and
            procedure training. Module 2, "Agency Mission, Scope of
            Services & Ethics," is the closest, but addresses mission
            and ethics, not policy and procedure.
Required:   "Facility policy and procedures."
Gap:        Not documented among the listed modules.

Provision:  OAC 450:1-9-5.6(b)(2)(H)
Severity:   Necessary Standard
Status:     FAIL
Located:    Same attestation.
Observed:   No module addresses co-occurring disorders. Module 9,
            "Treatment Planning & Documentation Standards," is generic
            documentation training, not this topic.
Required:   "Co-occurring disorder competency and treatment principles."
Gap:        Not documented among the listed modules.
```

### UNCLEAR

```
Provision:  OAC 450:1-9-5.6(a)(2)
Severity:   Critical Standard
Status:     UNCLEAR
Located:    Whole file — no privileging record found.
Observed:   No privileging document and no first-treatment-service date
            appear anywhere in the file.
Required:   "All staff shall be documented as privileged prior to
            performing treatment services."
Gap:        Cannot determine sequencing without either date. Both are
            missing, not just one.

Provision:  OAC 450:1-9-5.6(b)(2)(A)
Severity:   Critical Standard
Status:     UNCLEAR
Located:    Attestation, Module 12: "Emergency Procedures & Safety
            Protocols."
Observed:   A module addresses emergency/safety procedures generally,
            but nothing in the title or description confirms the
            specific content required — "location and use of all fire
            extinguishers and first aid supplies and equipment."
Required:   "Fire and safety, including the location and use of all
            fire extinguishers and first aid supplies and equipment."
Gap:        Adjacent topic present; the specific required content is
            not confirmed one way or the other.

Provision:  OAC 450:1-9-5.6(b)(2)(L)
Severity:   Necessary Standard
Status:     UNCLEAR
Located:    Attestation, 13-module list.
Observed:   No module addresses age/developmentally appropriate care.
Required:   "Age and developmentally appropriate trainings, where
            applicable."
Gap:        Applicability depends on the population served, which a
            personnel file doesn't establish. Cannot determine whether
            this was required at all, let alone documented.

Provision:  OAC 450:1-9-5.6(b)(2) — hire-year and 2025 calendar-year timing
Severity:   Critical Standard (governs (A)(B)(C)(D)(E)(J)(K) above)
Status:     UNCLEAR
Located:    Both attestation documents.
Observed:   Two documents exist for the same "2025 Staff Training
            Attestation & Sign-In Sheet." One (DocuSign) shows the
            administrator's certification dated 12/31/2025, with no
            visible date on the staff signature line. The other
            (non-DocuSign, filename stamped "08_07_2026") shows both
            the staff signature and the administrator's date as
            8/7/2026 — over seven months after the 2025 calendar year
            closed.
Required:   In-service "within thirty (30) days of each employee's hire
            date and each calendar year thereafter."
Gap:        Two conflicting completion dates for what is labeled the
            same obligation. Without a hire date, the 30-day hire-year
            clock also can't be checked. I'm not resolving which date
            controls — that's a fact only the agency's records can
            settle.

Provision:  OAC 450:1-9-5.6(c)(2)
Severity:   Critical Standard
Status:     UNCLEAR
Located:    Whole file — no supervision log or entries found.
Observed:   Nothing in the file documents supervision being provided to
            [EMPLOYEE NAME REDACTED]. The job description identifies this
            employee as the person providing clinical oversight and
            supervision to others, and the LADC license carries a "Board
            Approved Supervisor" designation.
Required:   Supervision "shall be provided and shall address" (A)
            appropriateness of treatment, (B) effectiveness against
            goals, and (C) feedback enhancing clinical skills.
Gap:        No documentation exists either way. Whether (c)(2) applies
            to a fully licensed, board-approved supervisor in their own
            right, versus only to staff they supervise, is not answered
            by the rule text or resolvable from this file. Flagged for
            human review rather than assumed.
```

### PASS

```
Provision:  OAC 450:1-9-5.6(a)(1)
Severity:   Critical Standard
Status:     PASS
Located:    LADCMHLicense, LPCLicense, CRCCert.
Observed:   LADC/MH license #[REDACTED] (behavioral health/SUD
            counseling), LPC license #[REDACTED], and CRC certification
            (rehabilitation counseling, valid through 9/30/2027) are all
            on file and specific to the clinical/counseling services the
            role entails.
Required:   "All staff who provide clinical services... shall have
            documented qualifications or training specific to the
            clinical services they provide."
Gap:        None on the documentation-specificity question. (Currency
            of two of these credentials is addressed separately under
            (a)(4) above.)

Provision:  OAC 450:1-9-5.6(a)(3)
Severity:   Critical Standard
Status:     PASS
Located:    OSBI background check records (DOB field).
Observed:   DOB of [DATE OF BIRTH REDACTED] is documented, making the
            employee well over 18.
Required:   "All direct care staff shall be at least eighteen (18)
            years old."
Gap:        None.
```

> **(b)(2)(B) PASS** — Module 11, "Infection Control & Universal Precautions," matches directly.
> **(b)(2)(C) PASS** — Module 3, "Client Rights, Grievances & Non-Retaliation," matches.
> **(b)(2)(D) PASS** — Module 4, "Confidentiality, HIPAA & 42 CFR Part 2," matches.
> **(b)(2)(G) PASS** — Module 5, "Cultural Competency & Trauma-Informed Care," matches (military-culture sub-component not separately confirmable).
> **(b)(2)(I) PASS** — same Module 5 covers trauma-informed service provision.
> **(b)(2)(J) PASS** — Module 13, "Crisis Prevention & De-Escalation Techniques," matches crisis intervention.
>
> (All six above carry the caveat under the UNCLEAR timing finding — which document's date actually governs completion is unresolved.)

### NOT APPLICABLE

```
Provision:  OAC 450:1-9-5.6(b)(3)
Severity:   Critical Standard
Status:     NOT APPLICABLE
Located:    Program context: Chapter 27, outpatient.
Observed:   No non-physical intervention training documented.
Required:   "This standard shall not apply to facilities or programs
            subject to Chapter 27 of this Title or outpatient programs
            subject to Chapter 18 of this Title."
Gap:        None. Chapter 27 status alone satisfies the exemption.
            Flagged for human review — scope determination belongs to
            the agency's compliance officer.
```

> **(b)(4) NOT APPLICABLE** — same Chapter 27 exemption; also no Executive Director designation for this employee is documented.
> **(b)(6) NOT APPLICABLE** — outpatient, not residential or Chapter 23. (A current CPR/first-aid card is in the file, valid through 5/7/2027, but it isn't required by this provision for this program type.)

### NOT ASSESSED

> **(b)(1)** written staff development/training plan — agency-level, not evidenced by one personnel file.
> **(b)(5)** curriculum approved by the commissioner — agency-level.
> **(c)(1)** written supervision policies and procedures — agency-level.

### SUMMARY

> 4 findings — 3 Critical ((a)(4), (b)(2)(E), (b)(2)(K)), 2 Necessary ((b)(2)(F), (b)(2)(H)). 9 PASS. 3 NOT APPLICABLE. 3 NOT ASSESSED. 5 UNCLEAR.
>
> Outside 450:1-9-5.6(a)(b)(c) entirely, not audited: OSBI criminal history checks (×2), OIG exclusion checks (×2), CCRR restricted registry, CSW registry, NPI record, job-description acknowledgment, DocuSign certificate of completion. These are screening/administrative records, not staff qualifications, training, or supervision documentation.

---

## ⚠️ That summary line is wrong, and the output above proves it

**This is why the full output is published.** Count the FINDINGS block: five
FAILs — `(a)(4)`, `(b)(2)(E)`, `(b)(2)(K)`, `(b)(2)(F)`, `(b)(2)(H)`. The
summary says **"4 findings"** while naming all five, and while stating
*"3 Critical, 2 Necessary"* — which is itself five.

Count the PASS block: eight — `(a)(1)`, `(a)(3)`, and `(b)(2)(B)(C)(D)(G)(I)(J)`.
The summary says **"9 PASS."**

UNCLEAR (5), NOT APPLICABLE (3) and NOT ASSESSED (3) are all correct.

**The itemised findings are right. The tally undercounts failures** — the
direction that costs an operator most, because the summary is the line a busy
reader actually reads.

`check.py` cannot catch this: it verifies that a cited provision **exists**,
and counts nothing. No fixture could catch it either — every answer-key total
in `receipts/EXPECTED_RESULTS.md` was computed by hand, and no fixture
produces enough findings for arithmetic to drift.

**It took a real staff file.** Found, not fixed — see
[`WHAT_TESTING_CHANGED.md`](WHAT_TESTING_CHANGED.md) **#8**.
