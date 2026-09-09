# IDEAS_LATER.md

Everything that is a good idea and is **not this build**. Parked here so
it stops competing with the deadline.

The brief asks for one auditor folder. Scope discipline is the point.

---

## The sellable version (after Sep 11)

This audits one section of one state's code. The *shape* generalizes:
a published standard in `reference/`, a findings schema with no field a
fix can live in, scope conditions checked before findings, severity from
the regulator rather than invented, and a checker that validates every
citation against the standard's own inventory.

That shape is the product. The Oklahoma rule is the first instance of it.

**Order of work, when it comes:**
1. A second section under the same chapter — proves the pattern moves
2. Consumer-record standards, which need a different confidentiality model
3. Another state, which tests whether the schema survives a rewrite

**Do not start any of this before the competition ships.**

---

## Insurance verification — separate problem, separate build (Sep 9)

Real incident, unrelated to staff files: Safe Harbor was built out for
insurance-based services, and when it was built, insurance verification
wasn't actually confirmed working end to end. Result: services were
delivered against insurance that wasn't verified, and some of it turned
into free care the agency couldn't bill for.

**Why this is not Comp #12:** different domain entirely — payer
eligibility verification is a revenue-cycle problem, not a staff
personnel-file compliance problem. Doesn't touch `450:1-9-5.6`.

**What's known already:** TherapyNotes (the EHR in use) has a built-in
way to verify insurance eligibility. The open question isn't "does a
tool exist" — it's why verification wasn't actually happening
(process gap, not a missing feature) before a client was seen.

**If this becomes a build later:** start by finding out whether the gap
was TherapyNotes' verification step being skipped, misconfigured, or
just not part of intake workflow — before designing anything. That's a
process/root-cause question, not a coding one, and it comes first.

---

## Real workflow, deliberately out of scope

- Monthly audit cadence / recurring internal review
- Delegation workflow
- Employee onboarding redesign so files are right on day one
- GHL automation of training expiry tracking
- Auditing against the agency's own internal policy manual

## Out of scope for the standard itself

- The consumer-file provisions: `450:1-9-5.5(c)`, `450:1-9-5.6(e)`, and the `450:18-7-*` series
- Chapter 27 / CARF
- The SUD client-census certification hurdle

## Checker ideas not needed to ship

- Validate severity assignment against a machine-readable Manual excerpt
- Flag a citation that exists but is out of scope for the stated level of care — the `(b)(6)` case. `fixtures/fixture-05` documents that `check.py` cannot catch it today.
- A `--strict` mode that fails on UNCLEAR
