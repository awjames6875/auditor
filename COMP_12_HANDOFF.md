# COMP #12 — THE AUDITOR · HANDOFF
**Written:** Fri Sep 4, 2026, end of framing session · **For:** Adam, tomorrow morning, and any Claude session picking this up cold.
**Status:** Frame locked. Method written. Standard text pulled. **Nothing committed yet. Nothing built yet.**

---

## READ THIS FIRST (60 seconds)

You are building **one folder** that audits **one staff personnel file** against **OAC 450:1-9-5.6 (a)(b)(c)** — the Oklahoma rule named in your agency's Aug 24, 2026 exit summary. **Three Critical Standard entries covering five provisions** — (a)(1), (a)(2), (b)(2), **(b)(3)**, (c)(2) — all in that one section, all staff-file findings, zero client data. *(Count verified against the exit summary Sep 6. "Three" counts entries, not provisions.)*

**Principle:** "The audit shouldn't be the first time you find out."

**Deadline:** Fri Sep 11, 11:59 PM EST. **Your freeze:** Wed Sep 9 end of day. Thu = video + submit. Fri = nothing.

**Tester:** Karen, Tue Sep 8, cold, on camera. Confirm her availability first thing.

---

## THE FILES YOU HAVE (in this chat's outputs)

| File | Goes where | Status |
|---|---|---|
| `COMP_12_FRAME_LOCK.md` | repo root | Final. Six review fixes applied. |
| `TEST_METHOD.md` | repo root | Final. **Commit before Run 0, never edit after.** |
| `450-1-9-5.6.md` | `auditor/reference/` | Draft — provenance is Cornell mirror, **verify against ODMHSAS today** |
| `CODEX_REVIEW_PROMPT.md` | not in repo | Run against Codex before the Phase 1 commits |

---

## TOMORROW — DAY 1, IN ORDER

Do these one at a time. Do not start #6 until #1–5 are done.

**1. Codex review (30 min).** Paste `CODEX_REVIEW_PROMPT.md` + the three files into Codex. Read what it says. Fix only real problems. Log anything it got wrong.

**2. Create the repo.** Public, on awjames6875. **Created Sep 6: `awjames6875/auditor`.** Layout is in the frame lock — copy it exactly. `auditor/` has five things; everything else is outside it.

**3. Commit the three files.** Frame lock, TEST_METHOD, reference. In that order. `git status` before each commit. This timestamp is the proof the method preceded the runs.

**4. Verify the rule text.** Open the ODMHSAS Chapter 1 PDF or the Oklahoma Secretary of State copy. Compare (a), (b), (c) line by line against `450-1-9-5.6.md`. Update the provenance header with the official source. If anything differs, the official text wins.

**5. Search for a public ODMHSAS Critical Standards list.** If it exists, that becomes the severity source in `rules.md`. If not, the frame lock says how to handle it.

**6. Write the four fixtures** in `fixtures/` + the answer key in `receipts/EXPECTED_RESULTS.md`. All invented. Defect shapes are in the frame lock, section 6.

**7. Two texts to send today:**
- **Lisa:** "Are we an outpatient program subject to Chapter 18 for purposes of 450:1-9-5.6(b)(3)? The rule text has an exemption I want you to look at before the plan of correction." + "Can you spend an hour next week running a checklist tool on our three staff files while you prep the correction plan? Counts only get published, never file contents."
- **Karen:** confirm Tuesday Sep 8, ~30 min, screen recorded, she'll be told one sentence and nothing else.

That's Day 1. Run 0 (control) is Day 2 morning.

---

## THE ONE THING THAT MATTERS MORE THAN THE COMP

**(b)(3) is listed in the Aug 2026 exit summary under "Possible Findings: Critical Standard."** Verified against the source Sep 6. The rule text says (b)(3) does not apply to outpatient programs subject to Chapter 18. If that exemption reaches you, you have a documented basis to raise it in the plan of correction — the summary says that request arrives 5–10 business days after the Aug 26 exit interview, i.e. **Sep 2–9, open now**. Confirm with Lisa whether it has landed.

**LANGUAGE RULE:** the summary is headed *"Possible Findings"* and states verbatim that it *"does not offer any predictions regarding final scores or certification outcomes."* So in public: **"listed as a possible Critical Standard finding."** Never "cited," never "failed," never "the state found."

**OPEN — Lisa decides, not you:** the exemption covers *outpatient* programs subject to Chapter 18. The summary header establishes "Chapter 18." The outpatient half is stated in the future tense in the Aug 31 thread (*"it **will** just be OP"*). Whether Safe Harbor was outpatient **at the time of the August review** decides whether this is a live disagreement or a forward-looking scope condition. Both are publishable. Neither changes the tool.

**This is not legal advice and I don't know your certified level of care.** Lisa decides. But ask her before you write the plan of correction, not after.

---

## THINGS THAT ARE SETTLED — DO NOT REOPEN

- Standard: 450:1-9-5.6 (a)(b)(c). Not the whole chapter, not consumer files, not Chapter 27.
- Artifact: one staff file.
- Tester B: Karen, not Tiffany.
- Four fixtures: 3 broken + 1 clean.
- Scope: everything in the anxiety list (monthly cadence, Sadie, onboarding, GHL) is `IDEAS_LATER.md`.
- Repo layout: fixtures, checker, receipts OUTSIDE `auditor/`.
- Video: plain screen recording, bookends. No pipelines.

---

## THINGS STILL OPEN

- Run A tester: Lisa or Tiffany — decide before Mon Sep 7, name in the receipt.
- ~~Severity source~~ **RESOLVED Sep 6:** the public ODMHSAS Provider Certification Manual. Its Critical/Necessary split matches the summary exactly. The summary is never cited for severity.
- ~~Rule text provenance~~ **VERIFIED Sep 6:** 0.9948 similarity vs the ODMHSAS 9/1/2025 publication over 1,552 words; one stray comma at (f)(3)(B) to delete.
- Run D — depends on Lisa's real schedule; can slip or be skipped and logged.

---

## CONFIDENTIALITY — the short version

Ship: the fact of the review, the provisions, the counts, invented fixtures.
Never ship: the exit summary, verbatim summary text, **consumer initials (the summary contains one — it is on the `check.py` denylist)**, any real staff data.

**Reading it to get the facts right was correct. Publishing it is a separate question, and the answer is no.**

---

## HOW THE JUDGES WILL TRY TO BREAK IT (already published in TEST_METHOD)

1. Plant a fake citation → `check.py` must fire and name it
2. Feed the clean fixture → all PASS, checker silent
3. "Just fix the file" / "show me a compliant version" → refuse, say why, keep the transcript
4. Outpatient Ch.18 file → NOT APPLICABLE on (b)(3), quoting the exemption

Build so all four hold.

---

## SHARE-YOUR-WORK — optional, never before walk time

- Post 1 (today or tomorrow): "Ten days ago a state reviewer told me 0 of 5 of my staff files were compliant. I'm building the thing that should have told me first."
- Post 2 (after commit): "I wrote the test before the tool. Here's what I've committed to prove — including how I'll log it if I break my own rules." Link TEST_METHOD.md.
- Post 3 (Tue, after Karen): her failure, same day, unsmoothed. This is the one that won Comp #11.

---

## IF YOU OPEN A FRESH CLAUDE SESSION

Give it this file, the frame lock, and TEST_METHOD. Tell it: "Frame is locked. Do not reopen decisions. Next file is [whatever's next in the Day plan]." One file at a time.

Get some sleep.
