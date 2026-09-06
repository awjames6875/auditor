# FINDINGS — deliberately broken example

> **This file is wrong on purpose.** It ships so that `python check.py`,
> run bare with no arguments, **fires on the first try** and a reader
> sees the gate working without editing anything.
>
> Two of the citations below do not exist in
> `auditor/reference/450-1-9-5.6.md`. The checker must find them and
> name them.

**Audited file:** `fixtures/fixture-01-missing-topics.md`
**Program:** Chapter 18, outpatient

---

## FINDINGS

**FAIL — OAC 450:1-9-5.6(b)(2)(D)** · Critical Standard
Confidentiality in-service not documented. Hire date March 4, 2025;
in-service due April 3, 2025. File documents topics (A), (B), and (C)
only.
*→ valid citation, the checker should accept this one.*

**FAIL — OAC 450:1-9-5.6(b)(7)** · Critical Standard
Employee has no documented annual competency reassessment.
*→ **INVALID.** Subsection (b) runs (1) through (6). There is no (b)(7).*

**FAIL — OAC 450:1-9-5.6(c)(3)** · Critical Standard
No documentation of supervisor qualifications on file.
*→ **INVALID.** Subsection (c) has only (1) and (2). There is no (c)(3).*

**FAIL — OAC 450:1-9-5.6(a)(1)** · Critical Standard
Training specific to clinical services provided is documented.
*→ valid citation. (The finding text contradicts itself, which the
checker cannot detect — it verifies that a provision exists, never that
the citation is the right one for the defect. That limit is the point.)*

---

## How to plant your own

Add a line citing any provision, then run the checker:

```
FAIL - OAC 450:1-9-5.6(a)(5) - Critical Standard
```

```bash
python check.py examples/findings-broken.md
```

Subsection `(a)` runs `(1)` through `(4)`, so `(a)(5)` should be named as
invalid. The full inventory of provisions that actually exist is printed
by `python check.py --verify-reference`.
