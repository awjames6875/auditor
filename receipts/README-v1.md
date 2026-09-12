# Staff File Auditor

**This folder reads one employee file and tells you what paperwork is
missing from it.**

It checks against one real Oklahoma regulation — `OAC 450:1-9-5.6` — that
says what has to be documented in a behavioral health worker's personnel
file: their training, their credentials, and their supervision.

> **The audit shouldn't be the first time you find out.**

---

## How to use it

**1.** Drop this whole folder into a Claude project.

**2.** Paste in one employee's file. Messy is fine — a PDF paste, a
scanned printout, typed notes. One person at a time.

**3.** Say: **"Audit this staff file."**

It will ask you two questions first. **Answer them, then it audits.**

---

## The two questions it asks first

> *"What chapter is the program certified under, and what is its level of
> care?"*

**Chapter** = which set of state rules the program is licensed under.
Chapter 18 is substance use, Chapter 27 is mental health. It is on the
certification paperwork.

**Level of care** = outpatient, residential, or inpatient.

**It asks because two of the rules don't apply to every program.** If it
guessed, it would tell you something was broken that was never required.
If you don't know, say so — it will audit everything else and mark those
two as unchecked.

---

## What you get back

One block per rule, like this:

```
Provision:  OAC 450:1-9-5.6(a)(2)
Severity:   Critical Standard
Status:     FAIL
Located:    PRIVILEGING section.
Observed:   Privileging signed July 15, 2025. First treatment service
            June 9, 2025 — 36 days earlier.
Required:   "All staff shall be documented as privileged prior to
            performing treatment services."
Gap:        Privileging is dated 36 days after services began.
```

**Status** is one of:

| | |
|---|---|
| **PASS** | The paperwork is there |
| **FAIL** | It's required and it's missing |
| **NOT APPLICABLE** | This rule doesn't apply to your program |
| **UNCLEAR** | It couldn't tell — go look yourself |

**Severity** is the state's own label, not ours. **Critical Standard** is
weighted more heavily than **Necessary Standard**.

**You get the PASS lines too.** Most files are mostly fine, and a list of
only failures makes the real problems harder to see.

---

## What it will not do

**It will not fix anything.** Ask it to draft the missing documentation,
show a compliant version, or say what the log "should have said," and it
refuses.

That is not politeness — **the output format has no field a fix could go
in.** Seven fields, and none of them holds replacement text.

The person who was in the room is the only one who can write what
happened in it.

**It also won't:** decide whether you pass, predict what a reviewer will
say, audit against your own internal policy manual, or give legal advice.

---

## What's in here

| File | What it is |
|---|---|
| `README.md` | This page |
| `identity.md` | What the auditor is and is not |
| `rules.md` | How it audits — the order, the format, the severity tiers, the exemptions |
| `examples.md` | Three worked audits, including a refusal |
| `reference/` | **The actual regulation.** Full text, not a summary. |

**`reference/450-1-9-5.6.md` is the whole point.** Every finding quotes
it. If you want to check whether the auditor is telling you the truth,
open that file and read the rule yourself — it is right there, verified
word for word against the state's own publication.

---

## What it covers, and what it doesn't

**Covers:** subsections `(a)` staff qualifications, `(b)` staff
development and training, `(c)` clinical supervision. **Staff files
only.**

**Does not cover:** consumer or client records, discharge summaries,
critical incident reporting, or any Chapter 18 consumer-file standard.

That boundary is deliberate. `(a)`, `(b)`, and `(c)` are the staff-file
parts of this regulation — **which is what keeps client information out
of this tool entirely.**

---

*Not legal advice. It audits a document, not an agency: training that
happened but was never written down reads here as missing, because for a
records review it is.*
