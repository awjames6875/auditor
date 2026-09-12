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

**September 11, 2026 · Run A performed out of order and after the freeze** — **What the method said:** `TEST_METHOD.md` fixes the run order 0 → A → B → C → D, and the project's own freeze was Wednesday September 9, end of day. **What actually happened:** Run A — the insider accuracy pass — was performed on **September 11**, after Run C (September 9) and after the freeze. **Why:** Run A depends on one named real person's availability, and hers fell where it fell. Her real job outranks the competition schedule; the alternative was not "Run A on time" but "no Run A at all." **What was done about it:** the run was performed and published late rather than skipped or backdated. `receipts/RUN_A_CORRECTIONS.md` states the out-of-order fact above its findings rather than in a footnote. The runs that preceded it — Run 0 and Run C — were **not** re-run, re-scored, or edited in light of it, so the published record still shows what those runs produced against the material as it stood on their own dates. This entry is the only thing reconciling the two. `DEVIATIONS.md` named "a run out of order" as an anticipated candidate before any run happened; this is that candidate arriving.

**September 11, 2026 · Fixture set extended after Run 0 and Run C** — **What the method said:** `TEST_METHOD.md` fixes the fixture set at four synthetic staff files (five, with the later citation-bait file) and is frozen at its first run; `EXPECTED_RESULTS.md` declares itself written September 6, 2026, **before Run 0 and before any auditor instruction file existed**. **What actually happened:** two fixtures — `fixture-06-chapter-27-exempt` and `fixture-07-residential-intervention-training` — and their answer-key entries were written on **September 11, 2026**, after Run 0 and Run C were already recorded. **Why:** the Run A compliance reviewer found that all five existing fixtures declared Chapter 18 / outpatient, so the `(b)(3)` and `(b)(4)` exemptions had only ever fired through one of three possible branches. Neither the Chapter 27 branch nor the not-exempt-at-all branch had been exercised, meaning a correct NOT APPLICABLE could not be distinguished from an accidental one. The gap was structural and worth closing even at the cost of a deviation. **What was done about it:** the two fixtures were added; the answer-key additions were fenced behind a dated provenance note at the head of `EXPECTED_RESULTS.md` so that file's September 6 write-date claim stays true for the original material; and **no result already recorded in a receipt was restated or rescored**. Both fixtures were then **executed against before this entry was committed** — one zero-context agent session each, neither having seen the answer key, both matching the new key entries on every line and naming the specific exemption route applied (`receipts/FIXTURE_06_07_VALIDATION.md`). That validation is the entrant's own, unblinded and entrant-graded, and it is **not** Run A: Lisa has not seen either fixture, both having been written after her review in response to it. Zero corrections arose from those runs, so the published Run A correction count stands at 4. `receipts/CLEAN_CLONE_TEST.md` still lists five fixtures because it records a clone taken on a past date; editing it would falsify a receipt, so it stands as written. `TEST_METHOD.md` was **not** edited to make its fixture table match.

**September 11, 2026 · Run D not performed** — **What the method said:** `TEST_METHOD.md` names Run D — live use — as the fifth run: the compliance officer uses the auditor against **real** staff files inside her real work, publishing counts and quotes but never file contents. The same section states in advance that *"Lisa's real job comes first. If the re-review timeline and the competition conflict, the re-review wins and Run D is skipped or delayed. A skipped Run D is logged in `DEVIATIONS.md`, not hidden."* **What actually happened:** Run D was not performed. **Why:** two reasons, both real. First, the premise it was built on no longer exists — Run D was framed around the compliance officer using the tool while preparing a plan of correction, and there is no plan of correction: the Chapter 18 review did not pass, nothing can be submitted against it, a new review must be scheduled, and the state votes September 24, 2026. Second, asked for a live session against real files, she declined and reviewed the synthetic fixtures in writing instead — a smaller commitment of her time and the form of participation she agreed to. **What was done about it:** the run was logged as not performed rather than reshaped into something that would fit before the deadline, which would have produced a run designed for a submission rather than for the work. Her judgment still reaches this entry through **Run A**, performed in writing the same day (`receipts/RUN_A_CORRECTIONS.md`), which found an error in this project's own answer key and a structural gap in the fixture set. What is missing is specifically the live, real-file run, and only that: **the auditor has never been run against a real staff file**, and `receipts/RUN_D_NOT_RUN.md` states that limit plainly rather than softening it. `DEVIATIONS.md` named "a skipped run" as an anticipated candidate before any run happened; this is that candidate arriving.

**September 11, 2026 · Run B — setup defect, and the no-help rule was not held** — **What the method said:** `TEST_METHOD.md` specifies that the outsider *"is given the folder and `fixture-02`. Nothing else,"* and fixes a no-help rule: no hints, no pointing, and *"if she asks a direct question, the only permitted reply is: 'Whatever you think it means.'"* **What actually happened:** two departures. First, the five `auditor/` files were sent as **individual email attachments rather than as a folder or an archive**, because the folder would not send — *"I couldn't do it. It was too big. It wasn't allowing me to do that."* The task prompt was nonetheless read to her verbatim as written, referring to *"this folder"* — a folder she did not have. Second, the no-help rule was broken repeatedly: extended coaching through screen-sharing setup, a nudge toward the file she had open (*"if you think that's the file to read, go for it"*), directing her screen mid-task (*"can you go to it... scroll up"*), and repeated encouragement delivered while she was failing (*"you're doing amazing," "you're doing excellent"*), which conveys direction whether or not it was intended to. The permitted reply was used inconsistently and the prompt was re-read three times. **Why:** the setup defect was an entrant packaging failure discovered only at the session; the no-help breaks were the entrant talking to a person who was visibly frustrated. Neither has a defensible reason and none is offered. **What was done about it:** nothing was cut. `receipts/RUN_B_RAW_TRANSCRIPT.md` is the uncut record, every nudge included, and `receipts/RUN_B_TRANSCRIPT.md` states above its findings both that the setup deviated and that the rule was not held. The run was **not** re-run: the tester has now seen the material and is spent as a cold outsider, and substituting the named backup outsider to obtain a cleaner result would be shopping for an outcome. The consequence is stated rather than argued away — **this run does not test whether `auditor/README.md` routes a reader who actually has the folder**, and that remains untested. `DEVIATIONS.md` named "the no-help rule broken in Run B" as an anticipated candidate before any run happened; this is that candidate arriving.

---

## Known in advance — likely candidates

Named here so that if they happen, the entry is honest rather than
reconstructed:

- **A run out of order.** The method fixes 0 → A → B → C → D. If a tester's real availability forces Run D earlier, that is a deviation and gets logged with the scheduling reason — not quietly reordered.
- **A skipped run.** Any of the five may not happen. The method already requires a file in `receipts/` for every run at freeze, **including one that reads only "not run, reason, date."** A missing file is not a neutral absence; it reads as a run that went badly.
- **The no-help rule broken in Run B.** It is self-reported and unenforceable by anyone but the person running it. Every nudge stays in the transcript, and the receipt says plainly that the rule was not held.
- **A receipt committed late.** Each is supposed to be committed the day of its run; the timestamp is the evidence. One committed later says so in itself.
