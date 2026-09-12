# RECEIPT — Run B (Hostile domain outsider)

**Date:** Friday, September 11, 2026
**Tester:** **Karen** — has never worked in behavioral health, HR, or compliance, and had never used Claude before this session. First name only.
**Consent:** obtained in writing before the session, covering her first name and her verbatim words appearing in a public repository.
**Duration:** approximately 23 minutes of task time, inside the 25-minute hard stop.
**Video:** https://share.descript.com/view/KSG1sZ96pb9 — the full session, screen shared, coaching left in.
**Raw transcript:** `receipts/RUN_B_RAW_TRANSCRIPT.md`, verbatim and uncut. Per `TEST_METHOD.md`, the link is not the record; the committed transcript is.

---

## RESULT: GIVE-UP. She never located a defect.

`TEST_METHOD.md` defines a result as *"a written or spoken statement
identifying at least one specific defect in the file,"* and states that
anything short of that is **a stall or a give-up — both valid, publishable
outcomes, recorded as what they are.**

She never reached a finding. She never audited the file. In her own words at
the stop:

> **"I don't think three minutes gonna help me none, 'cause I don't know what
> this is about."**

This is recorded as a give-up. It is not softened, and it is not described as
"almost."

---

## Deviation from the method, stated before the findings

**`TEST_METHOD.md` says: *"She is given the folder and `fixture-02`."* She was
not.** The five auditor files were sent as **individual email attachments**,
because the folder would not send:

> **Adam:** *"I couldn't do it. It was too big. It wasn't allowing me to do
> that. I tried it. I did not know how to do that."*

The task prompt was then read to her verbatim as written — *"Somewhere in this
folder is a set of instructions"* — **referring to a folder that did not exist
on her end.** She had loose attachments.

This is a setup defect by the entrant, and it materially shaped the run.
Logged in `receipts/DEVIATIONS.md`.

**Consequence, stated plainly:** this run does **not** test whether
`auditor/README.md` routes a reader who actually has the folder. That remains
untested. What it tests is what happens when the package arrives the way
packages actually arrive.

---

## The no-help rule was NOT held

`TEST_METHOD.md` requires that if the rule is broken it is **not edited out**,
and that the receipt states plainly that it was not held. It was not held.

**What was said that should not have been:**

- Extended coaching through screen-sharing setup — arguably environmental, but it was coaching and it is not excluded here
- *"If you think that's the file to read, go for it"* — a nudge toward the file she had open
- *"Can I see your README file again? Can you go to it? ... Scroll up"* — directing her screen mid-task
- Repeated encouragement — *"You're doing amazing," "You're doing excellent," "This is great"* — delivered while she was failing, which is feedback about her direction whether or not it was intended as such

**What was not done:** she was never told which file to open, never told what
the defect was, and never told what the tool does. The substantive answer was
never given, and she never found it. The permitted reply was used
inconsistently; the prompt was re-read to her three times.

Every one of these remains in `receipts/RUN_B_RAW_TRANSCRIPT.md`. Nothing was
cut.

---

## What she got RIGHT — and it matters

**She opened `README.md` first, unprompted.** That is the correct first move
and the door worked to that extent:

> **Karen:** *"I just opened up the Read Me one. I figured I'd read it."*

**She then followed the README's own instruction.** She pasted it into Claude
and asked the scope questions the file told her to ask:

> **Karen:** *"Because when I was reading this other one, it says to ask for
> the scope and wait for the answer."*

So the routing did not fail at the front door. It failed at step one of "How
to use it."

---

## THE FINDING: "drop this whole folder" is not an instruction she could follow

`auditor/README.md` line 16 reads: **"Drop this whole folder into a Claude
project."** She read that line. She did not do it. Asked why, in the debrief:

> **Karen:** *"I saw where it said file, but when I said file, that's why I
> copy and pasted that particular one because I thought that was the file. I
> didn't know you meant every attachment."*

> **Karen:** *"See, I didn't know that. 'Cause to me, these say **attachments**,
> not a file."*

The word "folder" described something she had never received. The word "file"
pointed, in her vocabulary, at the one document in front of her. So she pasted
that one document and worked from it for twenty minutes.

**She then wrote the fix herself:**

> **Karen:** *"You need to put, you need to write it **add download each
> attachment**."*

That sentence is the source of `auditor/README.md` v2. `receipts/README-v1.md`
preserves the version she actually read.

---

## The measured door — README v1 → v2 (M11)

**Word counts:** v1 = **688 words**. v2 = **869 words**. The door got
*longer*, not shorter, because what was missing was information rather than
brevity.

**Both changes trace to this run. Nothing else was rewritten.**

**Change 1 — Step 1, the instruction she could not follow.**
v1: *"Drop this whole folder into a Claude project."*
v2 names the count, lists all five filenames, and covers every delivery
shape: *"However they reached you — a folder, a zip, or five separate email
attachments — download every one of them, then attach every one of them to a
single Claude chat."* Plus the warning her run earned:

> *"If you attach only this page, Claude will answer you, and it will be
> guessing. The rules are in the other files."*

**Change 2 — a new section: "Which of these am I supposed to read?"**
She spent most of twenty-three minutes reading `rules.md`, a file written for
the assistant, and hit vocabulary that stopped her cold — *"I don't know what
a schema is,"* twice. `schema` is not a word for the human operator, and it
was never meant to reach her. v1 never told her she did not have to read
those files. v2 says: **this page, that's it** — the other four are for the
assistant, readable if you want to check the tool's work, unnecessary
otherwise.

**Not changed:** the word `schema` still appears in `identity.md`, `rules.md`
and `examples.md`. Those files address the assistant, and the fix for a
reader wandering into them is to tell her she need not — not to reword files
that are not written for her.

---

## What the instructions sounded like to a non-expert

Recorded because the tool's own language is the product, and this is what it
did to a first-time reader:

> **Karen:** *"I feel like I'm reading Japanese."*

> **Karen:** *"I don't know what a schema is."* — said twice, unprompted

> **Karen:** *"Sweet Jesus."*

> **Karen:** *"This is aggravating. This is aggravating to me."*

> **Karen:** *"I didn't feel like I skipped anything, so I don't even know
> what I'm supposed to be seeing."*

> **Karen:** *"I haven't gotten anywhere since the first thing I did."*

The word **schema** appears in files written for a reader described as
non-technical. She named it twice as a blocker. That is a vocabulary defect in
the instructions, not a gap in her.

---

## What this run establishes, and what it does not

**Establishes:**
- A genuine domain outsider, never having used Claude, could not complete the task in 23 minutes
- The package cannot survive arriving as loose attachments — nothing in it says how many files there are or that all are needed
- "Folder" and "file" do not mean to a lay reader what they mean to the author
- Unexplained jargon (`schema`) stops a reader cold

**Does not establish:**
- Whether the README routes a reader who has the actual folder — the setup defect prevented that from being tested
- Anything about the auditor's accuracy. She never ran an audit, so no finding, correct or incorrect, was produced
- **n = 1.** One outsider, once, under a broken setup

---

## Not re-run

Karen is spent as a cold outsider — she has now seen the material. Running the
named backup outsider tonight to obtain a cleaner result would be shopping for
an outcome, and is not done. This run stands as the Run B of record.
