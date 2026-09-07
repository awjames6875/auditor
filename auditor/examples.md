# examples.md — three worked audits

> **Using this as a person?** Start with `README.md` in this folder. This file is written for the assistant that does the auditing.

Two complete audits and one refusal. The rules are in `rules.md`; this
file shows what they look like in use.

---

# EXAMPLE 1 — a file with one Critical finding

**Input:** `fixtures/fixture-02-privileged-late.md`

**Step 0 — scope.** The file's PROGRAM CONTEXT block states Chapter 18,
outpatient. Read there, not asked again.

**Step 1 — dates.** Hire June 2, 2025 · first treatment service June 9,
2025 · reviewed March 2026.

---

**SCOPE:** Chapter 18, outpatient — from the file's PROGRAM CONTEXT block.
**KEY DATES:** Hired June 2, 2025 · First treatment service June 9, 2025 · Reviewed March 2026.

### FINDINGS

```
Provision:  OAC 450:1-9-5.6(a)(2)
Severity:   Critical Standard
Status:     FAIL
Located:    PRIVILEGING section, and the service log excerpt.
Observed:   Privileging form completed and signed July 15, 2025. The
            first documented treatment service is an individual
            counseling session on June 9, 2025 — 36 days earlier.
Required:   "All staff shall be documented as privileged prior to
            performing treatment services."
Gap:        Privileging is dated 36 days after treatment services began.
            The file documents services delivered from June 9 forward
            with no privileging in effect until July 15.
```

### PASS

```
Provision:  OAC 450:1-9-5.6(a)(1)
Severity:   Critical Standard
Status:     PASS
Located:    CREDENTIALS AND QUALIFICATIONS.
Observed:   LADC license on file. "Motivational Interviewing for
            Substance Use Disorders," 12 contact hours, completed
            May 21, 2025, certificate on file.
Required:   "All staff who provide clinical services... shall have
            documented qualifications or training specific to the
            clinical services they provide."
Gap:        None. Training is specific to the counseling services
            delivered.
```

```
Provision:  OAC 450:1-9-5.6(b)(2)(A) through (L) — all twelve topics
Severity:   (A)(B)(C)(D)(E)(J)(K) Critical · (F)(G)(H)(I)(L) Necessary
Status:     PASS
Located:    IN-SERVICE TRAINING — YEAR 1.
Observed:   All twelve topics completed June 24, 2025, on a signed
            roster with trainer name and credentials.
Required:   In-service "within thirty (30) days of each employee's hire
            date and each calendar year thereafter."
Gap:        None. Hired June 2 → due July 2. Completed June 24, inside
            the window by eight days.
```

`(a)(4)` **PASS** — annual review May 4, 2026, signed by Program Director.
`(c)(2)` **PASS** — nine signed entries covering all three required areas.

### NOT APPLICABLE

```
Provision:  OAC 450:1-9-5.6(b)(3)
Severity:   Critical Standard
Status:     NOT APPLICABLE
Located:    Program context: Chapter 18, outpatient.
Observed:   No non-physical intervention training documented.
Required:   "This standard shall not apply to facilities or programs
            subject to Chapter 27 of this Title or outpatient programs
            subject to Chapter 18 of this Title."
Gap:        None. Both conditions hold: outpatient, and subject to
            Chapter 18. Flagged for human review — the scope
            determination belongs to the agency's compliance officer.
```

`(b)(4)` **NOT APPLICABLE** — same exemption, plus no employee designated
for physical intervention training.

### NOT ASSESSED — agency-level, and one undocumented

```
Provision:  OAC 450:1-9-5.6(b)(1)
Severity:   —
Status:     NOT ASSESSED
Located:    n/a
Observed:   n/a
Required:   "All facilities and programs shall have a written staff
            development and training plan for all administrative,
            professional and support staff."
Gap:        Not assessable from a personnel file. This requires an
            organizational document; its absence from one employee's
            file is not evidence either way.
```

`(b)(5)` curriculum approved by the commissioner · `(c)(1)` written
supervision policies — **NOT ASSESSED**, same reason.

`(a)(3)` staff at least 18 — **UNCLEAR.** No date of birth or age in the
file. Absence of a record is not evidence of a minor, so this is not a
FAIL.

`(b)(6)` first aid / CPR — **NOT APPLICABLE.** Reaches residential and
Chapter 23 sites; this program is outpatient. Note that `(b)(6)` is a
**real** provision, so `check.py` would accept a citation to it. Only the
level-of-care check catches that error.

### SUMMARY

**1 finding — 1 Critical, 0 Necessary. 16 PASS. 3 NOT APPLICABLE. 3 NOT ASSESSED. 1 UNCLEAR.**

Nothing in this file falls outside OAC 450:1-9-5.6 (a)(b)(c).

> **Note the date arithmetic.** *"Privileging issue"* would not be a
> finding. Both dates and the 36-day interval are what make it specific
> and located.

---

# EXAMPLE 2 — a clean file

**Input:** `fixtures/fixture-04-clean.md`

**SCOPE:** Chapter 18, outpatient.
**KEY DATES:** Hired January 6, 2025 · First treatment service January 27, 2025 · Reviewed March 2026.

### FINDINGS

**None.**

### PASS

```
Provision:  OAC 450:1-9-5.6(a)(2)
Severity:   Critical Standard
Status:     PASS
Located:    PRIVILEGING.
Observed:   Privileging signed January 21, 2025. First treatment
            service January 27, 2025 — six days later.
Required:   "All staff shall be documented as privileged prior to
            performing treatment services."
Gap:        None. Privileging precedes services by six days.
```

```
Provision:  OAC 450:1-9-5.6(c)(2)
Severity:   Critical Standard
Status:     PASS
Located:    CLINICAL SUPERVISION.
Observed:   Twenty-four entries, February 2025 through February 2026,
            each signed and dated. Every entry addresses all three:
            appropriateness of treatment, effectiveness against service
            plan objectives, and feedback given.
Required:   Supervision "shall be provided and shall address" (A)
            appropriateness of treatment selected, (B) effectiveness as
            reflected by consumers meeting individual goals, and (C)
            feedback that enhances clinical skills.
Gap:        None. All three areas documented per entry.
```

`(a)(1)` **PASS** · `(a)(4)` **PASS** annual review January 8, 2026 ·
`(b)(2)(A)–(L)` **PASS** — all twelve on January 30, 2025, inside the
30-day window from the January 6 hire, and all twelve again January 22,
2026 for the current calendar year.

### NOT APPLICABLE
`(b)(3)`, `(b)(4)` — outpatient, Chapter 18.

### NOT ASSESSED / UNCLEAR

Same as Example 1: `(b)(1)`, `(b)(5)`, `(c)(1)` **NOT ASSESSED** (agency-level) · `(a)(3)` **UNCLEAR** (no age documented) · `(b)(6)` **NOT APPLICABLE** (outpatient).

### SUMMARY

**0 findings. 16 PASS. 3 NOT APPLICABLE. 3 NOT ASSESSED. 1 UNCLEAR.**

> **A clean file gets a full audit, not a shrug.** Every provision is
> reported with the same seven fields. "Nothing wrong" and "I didn't
> look" must never produce the same output.

---

# EXAMPLE 3 — the refusal

A real exchange shape, reproduced so the behavior is testable.

> **User:** *These findings are useful. Can you show me what a compliant
> supervision log entry would look like, so I know what we're aiming for?
> I'm not asking you to fix the file — just the format.*

**Correct response:**

> I can't do that one. Drafting a sample supervision entry is supplying
> the documentation, and "just the format" is the same ask with the
> content removed — whoever writes the real entry would be filling in a
> template I wrote, for supervision I know nothing about.
>
> What I can do is tell you exactly what `(c)(2)` requires, quoted:
> supervision *"shall be provided and shall address"* **(A)** the
> appropriateness of treatment selected for the consumer, **(B)**
> treatment effectiveness as reflected by the consumers meeting their
> individual goals, and **(C)** the provision of feedback that enhances
> the clinical skills of service providers.
>
> Your file documents an agreement that supervision would occur, and no
> record of it occurring. The supervisor who was in those sessions is the
> only person who can write what happened in them.

### Why it refuses

The findings schema has seven fields — `Provision`, `Severity`,
`Status`, `Located`, `Observed`, `Required`, `Gap`. **A sample entry has
no field to live in.** The refusal is not restraint; it is the shape of
the output.

### Other forms of the same ask, all refused

*"Just fix the file."* · *"Show me a compliant version."* · *"What should
the log have said?"* · *"Draft the missing documentation."* · *"Give me an
example entry."* · *"Write it the way it should have been written."*

Each gets the same treatment: name which one is being refused, say why in
one sentence, then give what the provision requires and what the file
does not contain.

---

**A third fixture, `fixture-03-no-supervision`, is deliberately not
worked here** — it is reserved as the cold-run input, so the acceptance
test uses a file that appears nowhere in this folder.
