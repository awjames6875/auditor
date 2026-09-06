# TEST_METHOD.md — The Auditor (Comp #12)

**FROZEN: September 6, 2026** — the date of the commit that carries this text. Drafted Sep 4; corrected Sep 6 before any run and before first commit.
**This file is written before any test has been run. It is not edited after the first run.**

*Why the date changed: the Sep 4 draft was never committed, so "frozen Sep 4" was unprovable. Freeze is defined by the commit timestamp, not by a line of text. This is the last edit; every change after this commit is a deviation logged in `receipts/DEVIATIONS.md`.*

If something in this method turns out to be wrong or impractical, the deviation is **logged in `receipts/DEVIATIONS.md` with a date** — this file is not quietly corrected. A method that can be edited after the fact is not a method.

---

## WHAT IS BEING TESTED

A drop-in folder that audits **one staff personnel file** against **OAC 450:1-9-5.6 (a), (b), (c)** — Oklahoma Administrative Code, Title 450, Chapter 1.

**The claim being tested:** a person who has never seen a personnel file or a state regulation can drop this folder into a Claude project, feed it a staff file, and get back findings that (1) cite a real provision, (2) name what is wrong and where, (3) assign severity, and (4) report what passed as well as what failed.

**The claim is false if:** a finding cites a provision that does not exist in `reference/`, the auditor reports only failures, the auditor tries to fix the file, or a cold reader cannot get a result without being coached.

---

## RUN ORDER (fixed)

The control must run before any auditor **instruction** content — `identity.md`, `rules.md`, `examples.md` — exists. (`reference/` is committed earlier by design: it is the public rule text, and Run 0 is given that same text. Instructions are the variable under test; the standard is not.) Fixtures must exist before the control. Therefore:

1. Write the four fixtures and `receipts/EXPECTED_RESULTS.md`
2. **Run 0 — Control** (no folder)
3. Build `identity.md`, `rules.md`, `examples.md`, `check.py`
4. **Run A — Insider accuracy** (one named tester, chosen before the run)
5. Fix only what A broke
6. **Run B — Hostile outsider (Karen)**
7. Rewrite the README from B's failure; keep v1 in-repo
8. **Run C — Cold model**
9. **Run D — Live use** (whenever the compliance officer's real timeline allows; see rules below)

No run is repeated to get a better result. If a run is repeated, both runs are published and the reason is stated.

---

## THE FIXTURES

Four synthetic staff files. Every name, date, and credential is invented. No real employee, no real client, no real Safe Harbor record appears in any fixture.

| File | Defect | Expected severity |
|---|---|---|
| `fixture-01-missing-topics` | In-service documented for `(b)(2)(A)`, `(b)(2)(B)`, `(b)(2)(C)` only — `(b)(2)(D)`, `(b)(2)(E)`, `(b)(2)(J)`, `(b)(2)(K)` absent | Critical |
| `fixture-02-privileged-late` | Privileging dated after the first treatment service date | Critical |
| `fixture-03-no-supervision` | No documentation of ongoing clinical supervision | Critical |
| `fixture-04-clean` | Fully compliant | No findings — all PASS |

**Notation rule (M-notation):** every lettered topic is written as a full provision — `(b)(2)(D)`, never a bare "D". The standard carries two lettered lists, `(b)(1)(A)–(E)` and `(b)(2)(A)–(L)`; bare letters are ambiguous. This applies to fixtures, expected results, findings, and severity notes.

**Fixtures live in `fixtures/` and expected results in `receipts/EXPECTED_RESULTS.md` — both at repo root, OUTSIDE the `auditor/` drop-in folder** (M10). A reader who drops `auditor/` in whole cannot load a fixture or an answer key by accident.

---

## RUN 0 — CONTROL (M12)

**Purpose:** establish what a model produces with the raw standard and no auditor. Without this, any good result from the auditor could just be the model being competent.

**Method:**
- Fresh Claude session, no project, no memory of this build
- Attach `fixture-01-missing-topics` and the raw text of OAC 450:1-9-5.6
- **Do NOT attach the auditor folder**
- Prompt, verbatim: *"Audit this staff file against this standard."*
- Save the full response to `receipts/RUN_0_CONTROL.md`, verbatim, including anything wrong

**What is recorded:** whether findings cite subsection-level provisions, whether severity is assigned, whether passes are reported, whether the (b)(3) exemption is applied, whether it tries to fix the file.

**Fairness terms (fixed in advance — the control must not be set up to lose):**
- **Same facts.** Run 0 is told the same chapter and level-of-care information the auditor asks for: *"This file is from an outpatient program certified under Chapter 18."* Without this, the control cannot apply the `(b)(3)` exemption and the auditor's headline separator would be measuring information the control was never given, not the folder.
- **One matched pair.** The control is also run on `fixture-03-no-supervision` with Run C's exact prompt (*"Audit this staff file."*), so at least one control/treatment pair differs by the folder alone and by nothing else.
- **n is stated in the headline, not the footnote.** If the control runs once, the receipt and any public claim say **n=1**. Three runs are preferred; all three are published, including the best one.
- **Unblinded, and disclosed.** The control is run after the answer key exists, by the person who wrote it, and graded by him. One sentence in the receipt says so.

**What this control does NOT prove:** it does not prove the auditor is better in general, only what one model did on one fixture in one run with no folder. That limitation is stated in the receipt itself.

---

## RUN A — INSIDER ACCURACY

**Tester:** ONE person, decided and named in `receipts/RUN_A_CORRECTIONS.md` before the run begins — Lisa (Safe Harbor compliance officer) or Tiffany. Not both, not "whoever is free."

**First names only, by design.** Consent covers a first name and verbatim words. A candidate who is never used should not carry a published surname, and the one who is used consented to a first name -- not more.

**Consent:** tester agrees in advance to their first name and corrections being published in a public repo. Recorded above the findings.

**Purpose:** are the auditor's findings actually correct against the rule — not "is the folder easy to use."

**Method:**
- Tester receives the folder and all four fixtures
- Tester answers, per fixture: does each finding cite the right provision? Is the severity right? Is anything missed? Is anything a false finding?
- **Every correction is logged with a date and a sequential ID (C-1, C-2, …) in `receipts/RUN_A_CORRECTIONS.md`**
- The count of corrections is published, whatever it is

**Definition of "broke" (so "fix only what A broke" is not elastic):** a correction is **any change to a file inside `auditor/` traceable to A's feedback.** The published count is that number of diffs. A change cannot be reclassified as "a clarification" to keep it out of the count. If a change is made that A did **not** prompt, it is listed separately as an uncorrected edit with its own reason.

**Specific question the tester is asked to rule on:** is Safe Harbor an outpatient program subject to Chapter 18 for purposes of the (b)(3) exemption? If unresolved, it is marked VERIFY and shipped unresolved rather than guessed.

---

## RUN B — HOSTILE DOMAIN OUTSIDER ⭐

**Tester:** Karen — has never worked in behavioral health, HR, or compliance, and has not seen this repo or any prior Cartographer build.

**Why her:** she will say it does not make sense rather than being kind about it. That is the qualification.

**Consent:** obtained and recorded **before** the session, covering first name and verbatim words being published in a public repo for judges. The consent basis is stated in the receipt above any findings. If she declines, the run does not happen and a different outsider is found.

**Setup:** screen and audio recorded. She is given the folder and `fixture-02-privileged-late`. Nothing else.

**Task, read to her verbatim, once:**
> "Somewhere in this folder is a set of instructions. Use them to check this staff file and tell me what's wrong with it."

**The no-help rule:**
- No hints, no pointing, no "try opening that one"
- If she asks a direct question, the only permitted reply is: *"Whatever you think it means."*
- **If the rule is broken, it is not edited out.** Every prompt, nudge, and confirmation stays in the transcript, and the receipt states plainly that the rule was not held. (This rule was broken in Comp #11 Test B and logging it plainly was rewarded.)

**Definition of "a result":** a written or spoken statement **identifying at least one specific defect in the file.** Not "I think this is about training." Not naming a file she opened. Anything short of a located defect is a **stall** or a **give-up** — both are valid, publishable outcomes, and both are recorded as what they are.

**Hard stop:** 25 minutes, or when she produces a result as defined above, or when she gives up — whichever comes first.

**The no-help rule is self-reported and that is stated plainly.** No one but Adam can enforce it. The receipt says: the rule is self-reported, the verbatim transcript is the only check, and every nudge remains in it. This is stronger than claiming a rigor no reader can verify.

**Backup outsider, named in advance:** if Karen declines, is unavailable, or withdraws consent, the run goes to **a second outsider meeting the same bar — never worked in behavioral health, HR, or compliance, and has not seen this repo.** The substitution and the reason are recorded in `receipts/RUN_B_TRANSCRIPT.md`. The run is not quietly dropped, and the bar is not lowered to whoever is free.

**Recorded:** where she goes first, what she opens, where she stalls, what she says in her own words, and whether she ever reaches a finding.

**Deliverables:** `receipts/RUN_B_TRANSCRIPT.md`, verbatim, with a dated transcript committed beside any hosted video link (M17). Video links are not the record — the committed transcript is.

**Then, mandatory (M11 — the measured door):**
- **The README in question is `auditor/README.md`** — the door Karen actually reads. The root `README.md` is the repo door and is not what this test measures.
- `auditor/README.md` is rewritten from what actually broke, not from what I think might break
- `README-v1.md` is kept in the repo so the diff is visible
- The word count of both versions is recorded

---

## RUN C — COLD MODEL

**Purpose:** prove the folder routes a reader who has no context at all.

**Method:**
- Fresh Claude session, no memory, no prior context
- All folder files attached individually
- `fixture-03-no-supervision` provided — a fixture that appears nowhere in `examples.md`
- Prompt, verbatim: *"Audit this staff file."*

**Six conditions, all must pass:**
1. Reads the README first and follows it rather than improvising
2. Produces findings that cite subsection-level provisions present in `reference/`
3. Assigns severity using the Critical / Necessary tiers
4. Reports at least one PASS, not only failures
5. Does not rewrite or fix the staff file
6. **Asks for the program's chapter and level of care before issuing findings** — the scope-condition behavior that drives the `(b)(3)`/`(b)(4)` exemptions. The build's most distinctive move belongs in its own acceptance test.

**Anything less than all six is recorded as a failure, not a partial pass.** The transcript is saved verbatim to `receipts/RUN_C_TRANSCRIPT.md`, including a failed run if one occurs.

---

## RUN D — LIVE USE (the real window)

**Tester:** Lisa, Safe Harbor compliance officer.

**Purpose:** the auditor is used on the agency's three real personnel files while Lisa prepares for the agency's **re-review**. This is a live regulatory window with the agency's certification genuinely at stake.

**Corrected Sep 6, before any run.** An earlier draft said "while Lisa prepares the actual plan of correction." **There is no plan of correction, and there will not be one.** A plan of correction is issued when a provider is going to pass and needs to adjust a few items — that is what happened on the agency's Chapter 27 review. The Chapter 18 desk review did not go that way: nothing can be submitted against it, and the agency must schedule a **new review** and apply again. The state votes **Sep 24**. The findings remain usable to fix what they name; they are not a document to respond to.

**Rules — all fixed in advance:**
- Lisa's real job comes first. If the re-review timeline and the competition conflict, **the re-review wins** and Run D is skipped or delayed. A skipped Run D is logged in `DEVIATIONS.md`, not hidden.
- Lisa uses the auditor as one input to her own review. She is not asked to trust it.
- **Published:** number of findings the auditor produced per file, number Lisa agreed with, number she overrode, her stated reasons for overrides, and her verbatim verdict on whether it helped.
- **Never published:** any staff file content, any employee name, license number, hire date, training record, or supervision entry. Counts and quotes only.
- Consent from Lisa for her name and words to appear, recorded before the run.
- **Override reasons are recorded as she gives them, not sorted into flattering buckets.** Any reason is publishable: the auditor was wrong on the rule, right on the rule but wrong for this file, right but not useful, duplicated something she already knew, or she simply disagreed. **A high override count is a result, not a failure to explain away.**
- **Lisa reviews `receipts/RUN_D_LIVE_USE.md` before it is committed.** She is quoted in public above her own name at her own employer; she sees the text first. If she asks for a change, the change is made and the fact that she reviewed it is stated in the receipt.

**Deliverable:** `receipts/RUN_D_LIVE_USE.md`.

**What this does NOT prove:** that the auditor is correct — Lisa's overrides are the correction record, and a high override count is published as-is.

---

## THE CHECKER

`check.py`, at repo root — **outside the `auditor/` drop-in** so the folder still has exactly five things. Runs bare, with no arguments, offline, with no API key, on Windows / macOS / Linux (M15). Defaults to the shipped fixtures.

**What it reads (the hole this closes):** fixtures are *inputs* to the auditor, not outputs of it — so "the folder's outputs" needed a file on disk to point at. It is now defined: **a findings artifact.** Paste the auditor's output into a `.md` and `check.py` reads it.

```
python check.py                      # bare: reads the shipped example findings
python check.py path/to/findings.md  # a judge's own run, pasted into a file
```

**It asserts:** every provision cited in a findings artifact exists in `reference/450-1-9-5.6.md`.

**It ships with** `examples/findings-broken.md` — a deliberately invalid citation — **so a bare run fires on the very first try** and a judge sees the gate work without editing anything. Planting their own takes one line, documented in the root README.

**It ships with** the fixtures — those that make the auditor fire and one clean control that must leave the checker silent (M14).

**Silence and success must never look identical.** On a clean artifact the checker prints `0 citations checked, 0 invalid` rather than nothing. A checker that says nothing is indistinguishable from a checker that did not run.

**It states in its own output what it cannot catch** — it verifies that a citation exists, not that the citation is the *right* one for the defect. That is a judgment the human still makes.

**Every count published in the README is printed by the script, never typed by hand** (M16).

---

## WHAT WOULD FALSIFY THIS BUILD

Stated in advance so a judge can try:

1. Plant a citation to a provision that does not exist in `reference/` → the checker must fire and name it
2. Feed the clean fixture → the auditor must report PASS and the checker must stay silent
3. Ask the auditor to "just fix the file" or, disguised, "show me what a compliant version would look like" → it must refuse and say why (M9)
4. Feed a staff file from an outpatient Chapter 18 program → it must return NOT APPLICABLE on (b)(3)/(b)(4), quoting the exemption sentence, rather than a false Critical finding
5. **Feed a staff file whose defect invites a citation to a provision that does not exist** — there is no `(b)(7)`, no `(c)(3)`, no `(a)(5)`. The auditor must not invent one to fit. This is the exact failure that destroys criterion 1 — *"a real, citable standard, or just an opinion"* — and it is what `check.py` exists to catch. Shipped as `fixtures/fixture-05-invented-citation-bait.md` with a documented judge recipe.
6. *(if time)* Feed an **ambiguous but compliant** file — in-service dated day 31 after hire. Tests whether findings are "specific and located" (criterion 2) with the date calculation shown, or merely vague.

Attempts 3 and 5 are run deliberately and their transcripts kept, whether or not they fire correctly.

---

## RECEIPTS

All receipts live in `receipts/` — **outside the drop-in folder** — so no walk can leak its own answers.

Run ordering is provable by **git commit timestamps, not file modification times.** A clone resets mtimes; commits survive.

**Every run has a file at freeze.** At the freeze, each of Run 0, A, B, C, and D has a file in `receipts/` — **including runs that did not happen**, whose entire content may be *"not run, reason, date."* A missing file is not a neutral absence; it reads as a run that went badly.

**Each receipt is committed the day of its run.** The commit timestamp is the evidence. A receipt written Wednesday describing Monday's run is indistinguishable from one written Monday — committing day-of is what closes that gap. A receipt committed late says so, in itself.

**`receipts/DEVIATIONS.md` format (fixed now, so it cannot be shaped later):** one entry per deviation — **date · what the method said · what actually happened · why · what was done about it.** Entries are appended, never edited or removed.

---

## SIGNED

Written and committed before Run 0. Adam James, September 4, 2026.
