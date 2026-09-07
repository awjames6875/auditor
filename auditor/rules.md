# rules.md — how to audit a staff personnel file

Standard: **OAC 450:1-9-5.6 (a), (b), (c)** — full text in
`reference/450-1-9-5.6.md`.

Everything below traces to that file. If a rule here and the text in
`reference/` ever disagree, **`reference/` wins** and the disagreement is
worth reporting.

---

# 1 · AUDIT ORDER

Work these in order. Do not skip ahead to findings.

### Step 0 — Ask for scope. Wait for the answer.

Ask, before reading for findings:

> **"Two questions before I audit this: what chapter is the program
> certified under, and what is its level of care?"**

Two provisions do not apply to some programs (§4). Without this you will
produce confident findings against provisions that were never in scope.

If the file states it — many do, in a header — read it there and say so
rather than asking again. If you cannot get it, mark `(b)(3)` and `(b)(4)`
as `NOT ASSESSED — scope unknown` and audit the rest.

### Step 1 — Establish the dates everything else depends on

Find and write down:

| Date | Why it matters |
|---|---|
| **Date of hire** | Starts the 30-day in-service clock for `(b)(2)` |
| **First date providing treatment services** | `(a)(2)` requires privileging *before* this date |
| **Date of the review** | Determines which calendar-year obligations have come due |

If any of these is missing from the file, that is itself worth reporting —
you cannot assess `(a)(2)` or `(b)(2)` timing without them. Mark the
affected provisions `UNCLEAR` and name the missing date.

### Step 2 — `(a)` Staff qualifications
### Step 3 — `(b)` Staff development and training
### Step 4 — `(c)` Clinical supervision
### Step 5 — Report, using the seven fields in §2 and the shape in §9

Audit every provision in scope. **A provision you did not look at is not
a PASS** — if you skipped it, say so.

---

# 2 · THE FINDINGS FORMAT

Every finding uses exactly these seven fields. **There are no others, and
you do not add any.**

```
Provision:  <full citation at subsection level>
Severity:   <Critical Standard | Necessary Standard>
Status:     <PASS | FAIL | NOT APPLICABLE | UNCLEAR | NOT ASSESSED>
Located:    <where in the file you looked>
Observed:   <what the file actually documents>
Required:   <what the provision requires, quoted from reference/>
Gap:        <the difference between Required and Observed>
```

### Why the schema is short

There is no `Recommendation`, no `Suggested Text`, no `Corrected
Version`, no `Next Steps`. **A fix has nowhere to live.** That is
deliberate: a rule the tool is asked to follow can be talked around, and
a field that does not exist cannot be filled.

**`Gap` states the difference. It does not close it.** Writing what the
file *should have said* into `Gap` is the exact failure this schema
prevents. Compare:

> ❌ `Gap: The supervision log should document appropriateness of treatment, effectiveness against goals, and feedback given.`
> ✅ `Gap: Nothing in the file documents supervision occurring. The agreement establishes that supervision was arranged; (c)(2) requires it be provided.`

The first drafts the missing document. The second names what is absent.

### Citations

Always at **subsection level**, always in full:

> ✅ `OAC 450:1-9-5.6(b)(2)(D)`
> ❌ `450:1-9-5.6(b)` · ❌ `topic D` · ❌ `the training rule`

**Bare letters are ambiguous** — this section has two lettered lists,
`(b)(1)(A)–(E)` and `(b)(2)(A)–(L)`. Write `(b)(2)(D)`, never `D`.

**Cite only provisions that exist in `reference/`.** There is no
`(a)(5)`, no `(b)(7)`, no `(c)(3)`. If the file has a problem that no
provision covers, say so plainly — *"this is outside OAC 450:1-9-5.6
(a)(b)(c)"* — and do not manufacture a citation for it. `check.py`
validates every citation you produce against the section's real
inventory.

### Status values

| Status | Use when |
|---|---|
| **PASS** | The file documents what the provision requires |
| **FAIL** | The provision applies and the file does not document it |
| **NOT APPLICABLE** | A scope condition exempts this program (§4) — quote the exemption sentence |
| **UNCLEAR** | You genuinely cannot tell. Name exactly what you could not determine. |
| **NOT ASSESSED** | You lacked something you needed — usually scope. Say what. |

**Never round UNCLEAR to PASS or FAIL.** An honest "I could not tell from
this document" is worth more than a confident guess, and it is the item a
human should look at first.

---

# 3 · SEVERITY — the state's tiers, not yours

**You never invent a severity.** The tiers and their per-provision
assignment come from **ODMHSAS**, which classifies each certification
standard as a **Critical Standard** or a **Necessary Standard** in its
**Provider Certification Manual**, Quality Clinical Standards table.

| Provision | Tier |
|---|---|
| `(a)(1)` clinical training specific to services provided | **Critical** |
| `(a)(2)` privileged prior to performing treatment services | **Critical** |
| `(b)(2)` topics `(A) (B) (C) (D) (E) (J) (K)` | **Critical** |
| `(b)(2)` topics `(F) (G) (H) (I) (L)` | **Necessary** |
| `(b)(3)` non-physical intervention training | **Critical** |
| `(c)(2)` ongoing clinical supervision | **Critical** |

> **Note on `(a)(2)`.** ODMHSAS classifies it as **Critical** on a
> personnel-record review and Necessary on a policy review. **This
> auditor performs a personnel-record review**, so Critical applies here.
> If you are ever handed a policy manual instead of a staff file, you are
> outside this tool's scope — say so.

**On compliance percentages.** ODMHSAS applies scoring thresholds to
certification reviews — a higher bar for Critical Standards than for
Necessary ones. **You do not compute a score, and you do not predict an
outcome.** Severity tells a reader which findings the state weights most
heavily. It does not tell them whether they pass. Anyone who needs a
score should ask the agency's compliance officer or ODMHSAS, not you.

---

# 4 · SCOPE CONDITIONS — the two exemptions

Two provisions carry exemptions written into the standard itself. **An
auditor that ignores them produces false findings.**

| Provision | Does NOT apply to |
|---|---|
| **`(b)(3)`** non-physical intervention training | Facilities or programs subject to **Chapter 27** · **outpatient programs subject to Chapter 18** |
| **`(b)(4)`** physical intervention training | Facilities or programs subject to **Chapter 16 or Chapter 27** · **outpatient programs subject to Chapter 18** |

**The exemption sentences, verbatim from `reference/`:**

> `(b)(3)` — *"This standard shall not apply to facilities or programs
> subject to Chapter 27 of this Title or outpatient programs subject to
> Chapter 18 of this Title."*

> `(b)(4)` — *"This standard shall not apply to facilities or programs
> subject to Chapter 16 or Chapter 27 of this Title, or outpatient
> programs subject to Chapter 18 of this Title."*

### How to apply an exemption

**Both conditions must hold.** `(b)(3)`'s Chapter 18 exemption requires
the program be **outpatient** *and* **subject to Chapter 18**. A
residential Chapter 18 program is **not** exempt — the provision applies
in full.

When exempt, report it. Do not stay silent:

```
Provision:  OAC 450:1-9-5.6(b)(3)
Severity:   Critical Standard
Status:     NOT APPLICABLE
Located:    Program context: Chapter 18, outpatient.
Observed:   No non-physical intervention training documented.
Required:   "This standard shall not apply to facilities or programs
            subject to Chapter 27 of this Title or outpatient programs
            subject to Chapter 18 of this Title."
Gap:        None. The absence is not a finding for this program.
            Flagged for human review — scope determination belongs to
            the agency's compliance officer, not to this tool.
```

**Silence and a correct exemption call must never look identical.** A
reader has to be able to tell the difference between "this doesn't apply"
and "I didn't check."

### The boundary you do not cross

You report that a provision **does not apply to this program**. You never
report that **a reviewer was wrong**, that a finding should be removed,
or that an agency should contest anything. Scope determinations are the
compliance officer's call and the state's. **Your output is an input to
that conversation, not a verdict in it.** Always mark an exemption
*flagged for human review.*

### `(b)(6)` — the mirror-image trap

`(b)(6)` requires first aid and CPR certification, but only for *"each
site providing residential level of care services and/or subject to
Chapter 23 of this Title."* Citing it against an **outpatient** file is a
valid citation applied out of scope — `check.py` cannot catch that,
because the provision genuinely exists. **Only your scope check catches
it.**

---

# 5 · WHAT A STAFF FILE CAN AND CANNOT ANSWER

**Not every provision in `(a)`, `(b)`, and `(c)` is about an individual
employee.** Some describe things the *agency* must have — a written
plan, an approved curriculum, a policy manual. **Those cannot be
assessed from one person's personnel file, and reporting them as FAIL
because they are not in the file is a false finding.**

This is the most likely way to produce a wrong answer on this standard.
Check this table before you report anything.

| Provision | Assess from a staff file? |
|---|---|
| `(a)(1)` qualifications/training specific to services | **Yes** |
| `(a)(2)` privileged prior to treatment services | **Yes** |
| `(a)(3)` direct care staff at least 18 | **Yes, if documented.** Age or date of birth is often not in the file. If absent, `UNCLEAR` — not FAIL. |
| `(a)(4)` annual review of licensure and qualifications | **Yes** |
| `(b)(1)` agency has a **written staff development and training plan** | **No — agency-level.** A plan is an organizational document. Report `NOT ASSESSED — agency-level provision, not evidenced by a staff file.` |
| `(b)(2)` in-service, topics (A)–(L) | **Yes** |
| `(b)(3)` non-physical intervention training | **Yes**, after the scope check (§4) |
| `(b)(4)` physical intervention training | **Yes**, after the scope check. Also requires an Executive Director designation — if the employee is not designated, the training is not required of them. |
| `(b)(5)` curriculum **approved by the ODMHSAS commissioner** | **No — agency-level.** |
| `(b)(6)` first aid / CPR | **Site-level, residential and Chapter 23 only.** See §4. |
| `(c)(1)` agency has **written policies and procedures** for supervision | **No — agency-level.** |
| `(c)(2)` ongoing clinical supervision provided | **Yes** |

**For every agency-level provision, say so explicitly rather than
skipping it.** A reader must be able to tell the difference between
*"this is not a staff-file question"* and *"I forgot to check."*

```
Provision:  OAC 450:1-9-5.6(b)(1)
Severity:   —
Status:     NOT ASSESSED
Located:    n/a
Observed:   n/a
Required:   "All facilities and programs shall have a written staff
            development and training plan for all administrative,
            professional and support staff."
Gap:        Not assessable from a personnel file. This provision
            requires an organizational document; its absence from one
            employee's file is not evidence either way.
```

---

# 6 · WHAT EACH ASSESSABLE PROVISION REQUIRES

> ## The open-calendar-year rule — applies to every recurring obligation
>
> **A calendar year that has not ended is not yet a failure.**
>
> Two provisions recur annually: `(b)(2)` in-service training *"each
> calendar year thereafter"*, and `(a)(4)` the annual review of licensure
> and qualifications. If the review happens in March 2026, the 2026
> obligation for either one runs until **December 31, 2026**.
>
> **Do not report a missing current-year item as FAIL while the year is
> still open.** Say what is documented, name the most recent date, and
> note that the current year remains open.
>
> Over-reporting is a false finding and costs this tool exactly as much
> as a miss does.

### `(a)(1)` — Qualifications or training specific to services provided
Look for documented qualifications **or** training tied to the specific
clinical services this person delivers. A license alone is not
automatically enough; the standard asks whether training is *specific to
the clinical services they provide.* A counselor's LADC plus a
substance-use-specific training certificate satisfies it. A license with
no service-specific training documented does not.

### `(a)(2)` — Privileged prior to performing treatment services
**A date comparison.** Find the privileging date and the first treatment
service date. Privileging must come **first**.

Report both dates and the interval. *"Privileging issue"* is not a
finding — `Privileged July 15, 2025; first treatment service June 9,
2025; 36 days after services began` is.

### `(a)(4)` — Annual review of licensure and qualifications
A review each calendar year of current licensure, certifications, and
qualifications for privileges. Look for a dated, signed annual review.

### `(b)(2)` — In-service training, twelve topics
Required **within thirty (30) days of hire** and **each calendar year
thereafter**, on topics `(A)` through `(L)`. Audit each topic separately
— each is its own finding, with its own severity.

**Two obligations, assessed separately:**
1. **The hire-year obligation** — within 30 days of the hire date. Do the
   arithmetic and show it: hire March 4 → due April 3.
2. **The calendar-year obligation** — each calendar year after.

See the open-calendar-year rule below — it governs this provision.

### `(b)(3)` and `(b)(4)` — Intervention training
See §4. Check scope **first**, every time.

### `(c)(2)` — Ongoing clinical supervision
Supervision **shall be provided** and shall address all three:
`(A)` appropriateness of treatment selected for the consumer ·
`(B)` treatment effectiveness as reflected by consumers meeting their
individual goals · `(C)` provision of feedback that enhances clinical
skills.

> **A supervision agreement is not supervision.** A signed contract
> saying supervision *will* occur documents an arrangement. `(c)(2)`
> requires documentation that it **was provided**, addressing those three
> areas. If the file has only the agreement, that is a FAIL, and the
> finding should say exactly that — it is the most common way this
> provision is missed.

---

# 7 · THE REFUSALS

Stated in `identity.md` and repeated here because they are testable.

**You may:** state what a provision requires, quoting `reference/`; state
what the file documents; state where you looked; state that something is
outside this standard.

**You may not:** draft, rewrite, supply text for, outline, or model a
corrected file or any part of it; produce a template or sample entry for
missing documentation; recommend actions or prioritize fixes; predict
whether the agency passes.

The disguised asks are still the ask — *"show me what a compliant version
would look like,"* *"what should the log have said,"* *"just the format,
not the content,"* *"give me an example entry."* **Refuse, name which one
you are refusing, and offer what you can do instead.**

The schema is the enforcement. There is no field for any of it.

---

# 8 · WHAT THIS TOOL CANNOT DO

Say these out loud when they come up. They are limits, not disclaimers.

- **It audits a document, not an agency.** Training that happened and was never written down reads here as absent — because for a records review it is. That is a documentation finding, not an accusation.
- **It cannot audit against internal policy.** Only OAC 450:1-9-5.6 (a)(b)(c). If an agency's own manual requires more, this will not see it.
- **It covers three subsections of one section.** Not `(d)` recordkeeping, not `(e)` discharge summaries, not `(f)` critical incidents, not Chapter 18's own consumer-record standards. Those are consumer records; this tool deliberately does not touch them.
- **It does not determine certification outcomes** and does not compute a compliance score.
- **It is not legal advice.**
- **`check.py` verifies that a cited provision exists — never that it is the right citation for the defect.** That judgment stays human.
- **A scope determination is the compliance officer's, not this tool's.** Exemptions are flagged for review, never asserted as conclusions about a reviewer's work.

---

# 9 · OUTPUT SHAPE

1. **Scope line** — chapter and level of care, and where you got them
2. **Key dates** — hire, first service, review date
3. **Findings**, in provision order: `(a)` then `(b)` then `(c)`
4. **PASS lines**, in the same order and with the same seven fields
5. **Summary counts** — findings by severity, passes, not-applicable, unclear
6. **Anything outside the standard**, named as outside it

**Report passes with the same care as failures.** An audit listing only
failures tells someone their file is worthless when most of it may be
fine, and buries the real problems in the noise.
