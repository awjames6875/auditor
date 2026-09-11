# The Auditor — a staff file auditor for OAC 450:1-9-5.6

**Drop `auditor/` into a Claude project, paste in one staff personnel
file, and get back what the Oklahoma Administrative Code requires, what
the file documents, and the difference — cited to the subsection, with
the state's own severity tier.**

> **The audit shouldn't be the first time you find out.**

---

## Falsify it in thirty seconds

No API key. No network. No install. Python 3, standard library only.

```bash
git clone https://github.com/awjames6875/auditor.git
cd auditor
python check.py
```

You should see **15 gates, 15 passed, exit 0** — and the citation gate
visibly firing on three planted citations that do not exist in the
standard.

**Now try to break it.** Add a line to `examples/findings-broken.md`
citing anything you like:

```
FAIL - OAC 450:1-9-5.6(a)(9) - Critical Standard
```

```bash
python check.py examples/findings-broken.md
```

It names the invalid citation and exits non-zero. `(a)` runs `(1)`
through `(4)`. The full inventory of provisions that actually exist is
printed by `python check.py --verify-reference`.

---

## The four things this was judged on, and where to check each

| | Where to look |
|---|---|
| **Audits a real, citable standard?** | `auditor/reference/450-1-9-5.6.md` — full provision text, verified word for word against the state's own publication. Receipt: [`receipts/RULE_TEXT_VERIFICATION.md`](receipts/RULE_TEXT_VERIFICATION.md) |
| **Findings specific and located, with severity?** | [`auditor/examples.md`](auditor/examples.md) — worked audits. Every finding carries a subsection citation, a location in the file, and the state's Critical/Necessary tier. |
| **Standard actually in `reference/`?** | Yes — 1,778 words of provision text. Not a summary, not a link. |
| **Can a stranger figure it out?** | [`auditor/README.md`](auditor/README.md) is the door. It was rewritten from what actually broke a tester who had never seen a personnel file or a state regulation — see `receipts/`. |

---

## It will not fix your file

Ask it to draft the missing documentation, show a compliant version, or
say what the supervision log "should have said," and it refuses.

**That refusal is structural, not behavioral.** A finding has exactly
seven fields:

```
Provision · Severity · Status · Located · Observed · Required · Gap
```

There is no `Recommendation`, no `Suggested Text`, no `Corrected
Version`. **A fix has nowhere to live.** A rule the model is asked to
follow can be talked around; a field that does not exist cannot be
filled.

The transcript of that refusal firing under a disguised ask is in
`receipts/`, not asserted here.

---

## It asks a question before it audits

> *"What chapter is the program certified under, and what is its level of
> care?"*

Two provisions — `(b)(3)` and `(b)(4)` — do not apply to certain
programs. The exemption is written into the standard itself:

> *"This standard shall not apply to facilities or programs subject to
> Chapter 27 of this Title **or outpatient programs subject to Chapter 18
> of this Title**."*

An auditor that skips this reports a confident finding against a
provision that was never in scope. **A false finding costs more than a
miss** — it sends someone to fix something that was never broken, and it
spends the credibility the real findings need.

When a provision is exempt, the auditor says so and quotes the exemption,
**flagged for human review**. It never concludes that a reviewer was
wrong. Scope determinations belong to a compliance officer and the state.

---

## Why this exists

In August 2026, a behavioral health agency in Tulsa went through an
ODMHSAS Chapter 18 desk review. The exit summary listed three Critical
Standard entries, covering five provisions — all under one section, all
staff files, no consumer records.

The counts were the part that landed: **0 of 3. 0 of 5. 0 of 3.**

I run that agency. Nothing in those files was invented, neglected, or
hidden — the training happened, the supervision happened. It was not
written down in a way a records review could see. **A state reviewer
reading your own personnel files back to you is the most expensive
possible way to learn that.**

> *Every provision, count, and severity referenced here comes from the
> agency's own exit summary, which is headed "Possible Findings" and
> states that it "does not offer any predictions regarding final scores
> or certification outcomes." So: **listed as possible findings.** Not
> cited, not failed, not "the state found." The summary itself never
> enters this repo, and no consumer information appears anywhere in it.*

---

## What it covers — and why the boundary is where it is

**Covers:** `(a)` staff qualifications · `(b)` staff development and
training · `(c)` clinical supervision. **Staff files only.**

**Does not cover:** consumer records, discharge summaries, critical
incident reporting, or Chapter 18's consumer-file standards.

That is not a convenient narrowing. Every provision under `(a)`, `(b)`,
and `(c)` is a **staff-file** requirement. Everything else on the same
review — including `(e)`, in the same section — is a **consumer record**.

**Scoping to `(a)(b)(c)` is what keeps client information out of this
tool entirely.**

---

## What's in the repo

| Path | |
|---|---|
| `auditor/` | **The drop-in folder.** Exactly five things: `README.md`, `identity.md`, `rules.md`, `examples.md`, `reference/`. |
| `check.py` | The gate. Bare run, offline, no dependencies, any OS. |
| `fixtures/` | Seven synthetic staff files, spanning Chapter 18 outpatient, Chapter 27 residential, and Chapter 18 residential scopes. Every name, date and credential invented. |
| `receipts/` | Verification, answer key, run transcripts. |
| `TEST_METHOD.md` | Written and committed **before** any test was run. Never edited after the first run; deviations are logged with dates, not quietly corrected. |
| `examples/findings-broken.md` | Deliberately wrong, so a bare `check.py` fires on the first try. |

**The answer key lives in `receipts/`, outside the drop-in.** A judge who
drops `auditor/` in whole cannot load it by accident. Neither can the
auditor.

---

## Honest limits

- **It audits a document, not an agency.** Training that happened and was never written down reads here as absent — because for a records review, it is. That is a documentation finding, not an accusation.
- **It cannot audit against an agency's internal policy manual.** Only the published standard.
- **It does not determine certification outcomes** and computes no compliance score.
- **`check.py` verifies that a cited provision exists — never that it is the right citation for the defect.** `fixtures/fixture-05` baits exactly that gap: `(b)(6)` is a real provision that applies only to residential sites, so citing it against an outpatient file is a valid citation applied out of scope. The checker cannot catch it. Only the scope rule can.
- **Not legal advice.**

---

*Built for Clief Notes ICM Comp #12. Standard text is public Oklahoma
Administrative Code. Fixtures are synthetic.*
