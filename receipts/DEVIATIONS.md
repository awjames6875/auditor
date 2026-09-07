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

*None yet. Run 0 has not been executed.*

---

## Known in advance — likely candidates

Named here so that if they happen, the entry is honest rather than
reconstructed:

- **A run out of order.** The method fixes 0 → A → B → C → D. If a tester's real availability forces Run D earlier, that is a deviation and gets logged with the scheduling reason — not quietly reordered.
- **A skipped run.** Any of the five may not happen. The method already requires a file in `receipts/` for every run at freeze, **including one that reads only "not run, reason, date."** A missing file is not a neutral absence; it reads as a run that went badly.
- **The no-help rule broken in Run B.** It is self-reported and unenforceable by anyone but the person running it. Every nudge stays in the transcript, and the receipt says plainly that the rule was not held.
- **A receipt committed late.** Each is supposed to be committed the day of its run; the timestamp is the evidence. One committed later says so in itself.
