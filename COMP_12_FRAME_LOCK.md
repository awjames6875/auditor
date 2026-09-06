# COMP #12 — THE AUDITOR · FRAME LOCK
**Locked:** Fri Sep 4, 2026 · **Deadline:** Friday Sep 11, 11:59 PM EST (hard commit freeze)
**Internal freeze (T−2):** Wednesday Sep 9, end of day — **defined precisely, because "no commits after Wednesday" contradicts Day 7:**
- **`auditor/` is frozen Wed EOD.** No change to `identity.md`, `rules.md`, `examples.md`, `auditor/README.md`, or `reference/` after that, full stop.
- **`receipts/`, the root `README.md`, and `check.py` fixes remain committable through Thursday.** Day 7 requires committing dated transcripts beside the video link; a late Run D must be loggable in `DEVIATIONS.md`. Both need Thursday commits, and neither touches the drop-in folder.
- Thursday = video + receipts + submit. Friday = nothing.
**Rule:** This frame does not change. New ideas mid-build go in `IDEAS_LATER.md`, not into the build.

---

## THE FRAME (6 answers)

**1 — The standard (real, external, citable):**
**OAC 450:1-9-5.6 — Quality clinical standards for facilities and programs**, subsections (a) Staff qualifications, (b) Staff development and training, (c) Clinical supervision.
Oklahoma Administrative Code, Title 450 (ODMHSAS), Chapter 1 (Administration). Public state administrative code — freely excerptable into `reference/`.
Safe Harbor is certified under **Chapter 18 (Alcohol & Drug)** and **Chapter 27 (Mental Health)**. 450:1-9-5.6 sits in Chapter 1 and applies across both.

> **Verify before publishing this sentence.** The Aug 2026 exit summary header reads **`Program(s): Chapter 18`** and **`Renewal: PTO`**, and the Aug 31 thread has Safe Harbor confirming **outpatient-only**. The reviewed program is Chapter 18. Whether Chapter 27 certification is current, and whether the program was outpatient **at the time of the August review**, are questions for Lisa — and the second one decides how separator #2 is framed. Do not publish a level-of-care claim on Adam's memory alone.

**2 — The artifact audited:** ONE staff personnel file.

**3 — Why this section and nothing else:**
All three **Critical Standard** entries in Safe Harbor's Aug 2026 Chapter 18 desk review fall under this one rule. Those three entries name **five provisions**:
- (a)(1) 0 of 3 staff had documentation of training specific to the clinical services they provide
- (a)(2) 0 of 3 staff files showed privileging **prior to** performing treatment services
- (b)(2) 0 of 5 staff files showed in-service within 30 days of hire and each calendar year thereafter — topics **(A)(B)(C)(D)(E)(J)(K)**
- **(b)(3) non-physical intervention training within 30 days of hire, updated each calendar year** — *the provision carrying the outpatient Chapter 18 exemption; see separator #2*
- (c)(2) 0 of 3 clinical staff records documented ongoing clinical supervision

> **Count, verified against the exit summary Sep 6:** **three Critical Standard entries covering five provisions.** The handoff's "three" counted entries; an earlier version of this list showed four because it omitted `(b)(3)`. Both are superseded by this line. Counts published in the README are printed by `check.py` (M16), never typed.

> **Language rule (non-negotiable, verified against the source Sep 6):** the document is headed **"Possible Findings"** and states verbatim that it *"does not offer any predictions regarding final scores or certification outcomes."* Therefore: **"listed as a possible Critical Standard finding."** Never "cited," never "failed," never "the state found." This applies to the README, the video, and every post.

**3b — Why (a)(b)(c) and nothing else — the scope line IS the confidentiality line:**
Every provision listed under `450:1-9-5.6` **(a)**, **(b)**, **(c)** is a **staff-file** finding. Every other item on the same summary — `450:1-9-5.5(c)(5)` tobacco, `450:1-9-5.6`**(e)** discharge summary, and the `450:18-7-*` series — is a **consumer-record** finding. Note `(e)` especially: same rule, consumer data. **Scoping to (a)(b)(c) is what keeps consumer records out of this build entirely.** State this in the README — it turns the obvious scope question into the strongest answer in the entry.

**4 — Quotable principle (video bookends):**
**"The audit shouldn't be the first time you find out."** ✅ Said out loud, locked.
- Open: "August 26th, a state reviewer read me my own files back. Zero of three. Zero of five. She knew my agency better than I did."
- Close: "The audit shouldn't be the first time you find out. Now it won't be."

**5 — Proof plan (`TEST_METHOD.md` frozen and committed BEFORE any run):**
| Run | Who | What |
|---|---|---|
| **0 — Control (M12)** | Fresh Claude, **no folder** | Same fixture, same question, raw standard only. Runs after fixtures exist, before any auditor file exists. |
| **A — Accuracy** | ONE named insider (Lisa or Tiffany — decide before the run) | Do findings match the rule text? Every correction logged with a date. |
| **B — Hostile outsider** ⭐ | **Karen** | Never seen a personnel file or a state rule. Cold, one task, on camera, coaching left in, failure published. |
| **C — Cold model** | Fresh Claude session | Drops folder in, audits a fixture it has never seen. Five conditions. |
| **D — Live use** | Lisa, on Safe Harbor's 3 real staff files during the actual plan of correction | Only if her real timeline allows. Publishes counts + her verbatim verdict. **Publishes zero file contents.** Her real job outranks the comp. |

**6 — Fixtures (all synthetic, written by Adam, ZERO real data):**
- 3 broken: (i) missing in-service topics, (ii) privileged AFTER first treatment date, (iii) no supervision documentation
- 1 clean control: fully compliant, proves the auditor stays quiet on honest work
- Defect *shapes* drawn from the real findings; every name, date, credential invented.

---

## REPO LAYOUT (locked)

```
staff-file-auditor/
├── README.md                    ← repo door: what this is, how judged, where receipts are
├── COMP_12_FRAME_LOCK.md
├── TEST_METHOD.md               ← frozen, never edited after Run 0
├── IDEAS_LATER.md
├── check.py                     ← the gate. OUTSIDE the drop-in. Runs bare, offline.
├── fixtures/                    ← OUTSIDE the drop-in (M10)
│   ├── fixture-01-missing-topics.md
│   ├── fixture-02-privileged-late.md
│   ├── fixture-03-no-supervision.md
│   └── fixture-04-clean.md
├── receipts/                    ← OUTSIDE the drop-in (M10)
│   ├── EXPECTED_RESULTS.md      ← the answer key. Never inside auditor/.
│   ├── RUN_0_CONTROL.md
│   ├── RUN_A_CORRECTIONS.md
│   ├── RUN_B_TRANSCRIPT.md
│   ├── RUN_C_TRANSCRIPT.md
│   ├── RUN_D_LIVE_USE.md
│   ├── DEVIATIONS.md
│   └── README-v1.md             ← the door before Karen broke it
└── auditor/                     ← THE DROP-IN FOLDER. Exactly five things.
    ├── README.md
    ├── identity.md
    ├── rules.md
    ├── examples.md
    └── reference/
        └── 450-1-9-5.6.md
```

**Why fixtures and the checker live outside:** the brief says the folder has five things. A judge who drops `auditor/` in whole must never load an answer key, a fixture, or a script.

---

## 🚨 CONFIDENTIALITY GATES (check before every commit)

- [ ] **The ODMHSAS findings letter itself never enters the repo** — not committed, not attached, not screenshotted.
- [ ] **No verbatim letter text** in any file.
- [ ] **No consumer initials or identifiers** (the letter contains some) anywhere.
- [ ] **No real employee names, license numbers, hire dates, or file contents.** Fixtures are invented. Run D publishes counts and a quote, nothing else.
- [ ] **Permitted:** the fact that a Chapter 18 desk review occurred in Aug 2026, the provisions listed, and the counts ("0 of 3"). These are Adam's own agency story, not client data, and may be spoken in the video and README.
- [ ] Repo is public. Assume every file is read by strangers.

---

## HARD GATES (Trait 8 — brief-literalism, check FIRST)

- [ ] Premium/VIP eligibility confirmed (was confirmed for Comp #11 — reconfirm nothing changed)
- [ ] Deliverable = ONE auditor folder, droppable into a Claude project
- [ ] `auditor/` contains exactly five things: `identity.md` · `rules.md` · `examples.md` · `reference/` · `README.md`
- [ ] **`reference/` contains the actual standard text** — not a summary, not a link. The named auto-fail this cycle.
- [ ] Every finding cites a provision at subsection level (e.g. "fails OAC 450:1-9-5.6(b)(2)(D)")
- [ ] Findings are **specific and located**, with severity
- [ ] Auditor reports **PASS and FAIL** — not just fail
- [ ] Severity uses two tiers: **Critical Standard** / **Necessary Standard** — see Severity Source below
- [ ] Auditor applies the **(b)(3)/(b)(4) scope exemptions** — asks chapter + level of care before findings; returns NOT APPLICABLE rather than a false finding
- [ ] `examples.md` smaller than `rules.md`
- [ ] Answer key, fixtures, checker, receipts all OUTSIDE `auditor/` (M10)
- [ ] Submit: public repo link + 2–3 sentences (what it checks, which standard) + **disclose AI authorship** (M18)

## SEVERITY SOURCE (decide Day 1)
The Critical / Necessary tiers are the state's own. The specific split observed in the Aug 2026 review: topics **A, B, C, D, E, J, K** listed as Critical; **F, G, H, I, L** as Necessary. **Confirmed Sep 6 against both the exit summary and the public Provider Certification Manual — they agree exactly. `rules.md` cites the Manual; the summary is never the severity source.**
**Day 1 task:** search for a published ODMHSAS Critical Standards list. If it exists, `rules.md` cites *that* and the letter is never the source. If it does not exist, `rules.md` says plainly: "tiering follows how ODMHSAS classified these provisions in the agency's own August 2026 certification review" — and owns that choice.

## JUDGING CRITERIA (verbatim — score against THESE four first)
1. "Does it audit against a real, citable standard? Or is it just an opinion?"
2. "Are findings specific and located, with severity?"
3. "Is the standard actually in reference/ where a reader can check it?"
4. "README quality. Can a stranger figure this out?"

---

## 7-DAY PLAN (corrected — fixtures before control, freeze Wed)

| Day | Date | Work |
|---|---|---|
| **1** | Fri Sep 4 | Commit frame lock + `TEST_METHOD.md` + `reference/`. **Verify rule text against ODMHSAS/SoS copy.** Search for ODMHSAS Critical Standards list. Write the 4 fixtures + `receipts/EXPECTED_RESULTS.md`. Text Lisa (b)(3) question + Run D ask. Confirm Karen for Tue Sep 8. |
| **2** | Sat Sep 5 | **Run 0 — Control.** Then `identity.md` + `rules.md` (audit order, citation format, severity source, scope exemptions, the three refusals, honest limits incl. "cannot audit against Safe Harbor's internal policy"). |
| **3** | Sun Sep 6 | `check.py` (bare, offline, cross-OS, prints every count). `examples.md` — 2–3 worked audits, PASS lines present, smaller than `rules.md`. `auditor/README.md` v1. |
| **4** | Mon Sep 7 | **Run A** — one named insider. Log every correction. Fix only what broke. Run the disguised-ask refusal (falsification #3) and keep the transcript. |
| **5** | Tue Sep 8 | **Run B — Karen, cold, on camera.** README v2 rewritten from her failure; v1 copied to `receipts/README-v1.md`. Word counts recorded. |
| **6** | Wed Sep 9 | **Run C — cold model.** M10 sweep. **FREEZE `auditor/` end of day.** *(Day 6 Codex pass **CUT** Sep 6: a cold review whose findings land on freeze day cannot be acted on. The cold review ran Sep 6 instead — before the first commit, when its findings could still change frozen files.)* |
| **7** | Thu Sep 10 | Video (plain screen recording, bookends). Dated transcripts committed beside every video link. **Submit.** |
| — | Fri Sep 11 | Nothing. Run D whenever Lisa's real timeline allows, before Wed freeze if possible; if it lands after, it is logged in `DEVIATIONS.md` and not counted. |

---

## OUT OF SCOPE — goes in IDEAS_LATER.md, not this build

- Monthly audit cadence / recurring internal review process
- Delegation workflow to Sadie
- Employee onboarding process redesign
- GHL automation of training tracking
- Auditing against Safe Harbor's own internal policy manual (real, valuable, October)
- The consumer-file findings (450:18-7-23, -61, -81, -101, -121, 450:18-13-2, tobacco, discharge summary)
- Chapter 27 / CARF accreditation
- The SUD "find 5 clients" certification hurdle

**Why:** the brief asks for ONE auditor folder. ~7 entries lost a tier in Comp #11 on shape errors. The auditor is the judgment core; the workflow wraps around it AFTER Sep 11.

---

## THE FOUR SEPARATORS (evidence moves, not build moves)
1. **Run D** — real compliance officer, real files, live plan-of-correction window, license on the line (Comp #9's winning shape)
2. **The disagreement** — the auditor returns NOT APPLICABLE on (b)(3) for an outpatient Ch.18 program, quoting the exemption sentence. Framed as *flagged for human review*, never "the state was wrong." Verified with Lisa first; either outcome is publishable.
3. **Severity from the regulator**, not invented
4. **Scope conditions as a first-class rule** — asks chapter + level of care before auditing

---

## ICM PRIMITIVE THIS COMP TEACHES
**A gate a stranger can run against a public standard.** The empty row in the mastery map since Comp #11 — the judges' own named next build. Rule carried from #11: never trade walk time for checker time.

## COMP #11 LESSON APPLIED
Hand the work to people who can make you look bad. Publish the failure unsmoothed. Rebuild the door from it. Keep v1 in the repo.
