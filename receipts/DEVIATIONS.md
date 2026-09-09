# DEVIATIONS.md

Every departure from `TEST_METHOD.md`, logged with a date.

**The rule (`TEST_METHOD.md`):** if something in the method turns out to
be wrong or impractical, the deviation is logged here — the method is not
quietly corrected. A method that can be edited after the fact is not a
method.

**Format, fixed in advance so it cannot be shaped later:**

> **Date · What the method said · What actually happened · Why · What was done about it**

Entries are appended. Never edited, never removed.

---

## Scope of this file

`TEST_METHOD.md` is frozen as of its commit on **September 6, 2026**, and
is not edited after the **first run**. No run had occurred at that
commit.

Edits made *before* the first run — correcting the Run D premise, and
reducing third-party surnames to first names — are **not deviations**.
They are the pre-run window working as intended, and each is recorded in
the commit history with its reasoning.

**Everything after Run 0 begins is a deviation and belongs here.**

---

## Entries

**September 9, 2026 · Run C, condition 6** — **What the method said:** `TEST_METHOD.md` requires the auditor to "ask for the program's chapter and level of care before issuing findings." **What actually happened:** on the real Run C (fresh session, `fixture-03-no-supervision.md`), the auditor did not ask — it read Chapter 18/outpatient from the fixture's own PROGRAM CONTEXT block and stated that it had done so, rather than issuing a question. **Why:** `rules.md` §1, Step 0 explicitly instructs this: *"If the file states it — many do, in a header — read it there and say so rather than asking again."* All five shipped fixtures state chapter and level of care in a header by design (see `EXPECTED_RESULTS.md`, "Scope of every fixture"), so a correctly-instructed auditor will never literally ask against any of them — `TEST_METHOD.md`'s condition 6 was worded before this refinement to `rules.md` existed, and the two now disagree. **What was done about it:** condition 6 is treated as satisfied in substance — scope was established from a disclosed source before any findings were issued, which is the behavior condition 6 exists to test — rather than by its literal wording. No edit was made to `rules.md`, `TEST_METHOD.md`, or any fixture to force a literal match; this entry documents the gap instead. The other five Run C conditions were unaffected. See `receipts/RUN_C_TRANSCRIPT.md`.

---

## Known in advance — likely candidates

Named here so that if they happen, the entry is honest rather than
reconstructed:

- **A run out of order.** The method fixes 0 → A → B → C → D. If a tester's real availability forces Run D earlier, that is a deviation and gets logged with the scheduling reason — not quietly reordered.
- **A skipped run.** Any of the five may not happen. The method already requires a file in `receipts/` for every run at freeze, **including one that reads only "not run, reason, date."** A missing file is not a neutral absence; it reads as a run that went badly.
- **The no-help rule broken in Run B.** It is self-reported and unenforceable by anyone but the person running it. Every nudge stays in the transcript, and the receipt says plainly that the rule was not held.
- **A receipt committed late.** Each is supposed to be committed the day of its run; the timestamp is the evidence. One committed later says so in itself.
