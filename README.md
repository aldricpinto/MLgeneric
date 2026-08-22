# Ajaia AI Strategist — Core Assignment
**Candidate:** Aldric Pinto | **Client:** Westbrook Health Partners

---

## Task 1 — Opportunity Triage

**Basis for ranking:** I'm ranking by *expected effect on Priya's stated goal — visits per clinician, up 20% in a year — adjusted for implementation risk and time-to-value.* An item that's exciting but doesn't touch scheduling throughput, or that can't ship safely inside Westbrook's compliance constraints, ranks below one that's smaller but real. I apply this to every item, including the vendor platforms she's already been pitched.

### 1. Prior Authorization Clinical-Summary Drafting Assistant
**Tag:** AI
**Evidence:** Dana Reyes, directly: "My auth team will tell you they spend most of their week typing the same clinical information into eight different payer portals." 1,100 auths/month (Marcus Bell). This is the single most-cited pain point in the materials and it sits directly upstream of scheduling — nothing books until authorization clears.
**Assumption:** That most of the auth team's time is spent on reformatting/re-entry rather than genuine clinical judgment calls — reasonable given Dana's framing, but unconfirmed (see Info Gap #1).
**Worth:** Cannot size precisely yet — I don't have auth-team headcount or average minutes per submission. Rough framing: if drafting saves even 10–15 minutes per submission across 1,100/month, that's 180–275 staff-hours/month, worth roughly $6,000–$9,000/month in loaded time at Westbrook's ~$34/hr average (from the $71K loaded cost figure) — before counting the harder-to-price upside of faster first-pass approval reducing schedule delay. I'd confirm this with a time-motion sample in week one.

### 2. Records Request Single-Inbox + Auto-Triage
**Tag:** Process fix, with light automation (a routing rule, not AI)
**Evidence:** Marisol's Slack message (request sitting in the wrong inbox, attorney emailing twice) and the 12-request sample log, where 10 of 12 requests closed in under 15 minutes and 2 of 12 took 1–4 days. The operations lead's own note confirms it: "the long ones are always the ones that come into the wrong inbox."
**Assumption:** That the wrong-inbox problem, not request complexity, is the dominant cause of the outliers — supported by the note attached to the log, not independently verified across all 1,840/quarter.
**Worth:** Most of the value isn't hours saved — the typical request is already fast — it's eliminating the reputational and compliance risk of PHI requests aging for days in an unowned inbox. Cheap and fast to ship, so it's a good first move to build trust before the bigger AI build lands.

### 3. Structured, Lightweight Order Capture for High-Volume Clinicians
**Tag:** Process fix
**Evidence:** The Slack thread — Dr. K "keeps his own note template and batches his charts on the weekend," and the auth team had nothing in the EHR for the Alvarez authorization on Tuesday because of it. Rick O.: "this is like 8 of the 55 clinicians, but they are 8 of the highest volume ones."
**Assumption:** That these 8 clinicians would adopt a *faster* structured capture method (e.g., a 30-second order-only form, distinct from full chart closure) even though they've resisted the EHR's mid-clinic forms — untested.
**Worth:** Not directly sizable, but it's a dependency: the AI drafting assistant in #1 can't draft anything for these 8 clinicians' patients until their order data exists somewhere structured. Given they're disproportionately high-volume, this gates a meaningful share of #1's value.

### 4. Referral Loop Instrumentation
**Tag:** Automation (measurement first; AI-based prioritization only after instrumentation exists)
**Evidence:** Dana Reyes: "Sometimes the referral sits, and the patient goes somewhere else, and the referring physician stops sending us anybody. I do not have a number on how often that happens." Marcus confirms: "Nobody has ever connected those two systems."
**Assumption:** None yet worth stating — this is explicitly unmeasured, which is the point.
**Worth:** Cannot size. This could be the largest opportunity in the whole engagement (referral-source erosion compounds silently) or a minor one — there's no way to know without connecting referral intake to scheduling outcomes first. I'd start with instrumentation only: timestamp referral receipt and outreach, and tag whether it converts to a scheduled visit. Revisit sizing in 60 days once there's real data.

### 5. Consolidate the Prior Auth Tracker Spreadsheet
**Tag:** Process fix
**Evidence:** Artifact D — nine people have edit access, three systems (EHR, portal, spreadsheet) disagree "often enough" that ops treats the spreadsheet as the real record because it's the only place the notes column exists.
**Worth:** Real problem, but not one to solve yet — see below.

---

### What I would not touch
**The Prior Auth Tracker spreadsheet, and the underlying "EHR is the system of record" policy — not yet.** It's tempting to kill the spreadsheet and force everything back into the EHR, since that's the stated rule. But the spreadsheet exists because it's the only place staff can capture the free-text context (the "why") that the EHR and payer portals don't hold — and because the EHR entry itself is unreliable for the 8 high-volume clinicians in the first place. Ripping out the spreadsheet before fixing *that* input problem would just break the one system four people rely on daily, without fixing the root cause. Fix #3 first; the spreadsheet consolidation becomes much easier once the input data is trustworthy.

**Also would not touch: buying one of the three AI platforms Priya's already been pitched, at least not now.** None of the three vendors have a confirmed BAA (Alicia Grant is explicit: she doesn't know what unlisted tools people are already using, and wants that answered before anything new touches patient data). An off-the-shelf platform is also unlikely to match Westbrook's specific payer-format and EHR-integration reality without months of configuration — the highest-leverage move here is a narrow, purpose-built tool addressing the one bottleneck everyone names unprompted, not a platform swap.

### Where the materials contradict or mislead

1. **"Everything lives in the EHR, that has always been the rule" (Dana Reyes) vs. reality.** The Slack thread shows 8 of 55 clinicians — disproportionately high-volume ones — don't chart in real time, and ops treats the spreadsheet, not the EHR, as ground truth because of it. I'm working from the Slack/spreadsheet evidence as the operating reality, while still respecting the EHR as the compliance system of record for anything requiring clinician sign-off.

2. **Marcus's "average turnaround 4.2 hours" for records requests is misleading on its own.** The 12-request sample shows a bimodal pattern: 10 of 12 requests closed in 6–13 minutes; 2 of 12 took 1–4 days. A mean gets dragged upward by two outliers and makes the whole process look worse — and the fix look bigger — than it is. The real story is "the process mostly works; roughly 1 in 6 requests falls into a hole." I sized and prioritized #2 off the median/outlier-rate reading, not the average.

3. **The 70% first-pass prior-auth approval rate — Marcus flags this himself as untrustworthy** ("it comes out of the EHR and the EHR only knows what people put in it"). Given the same 8 high-volume clinicians create EHR data gaps, this number likely undercounts or misrepresents the true rate. I'm treating it as directional, not a baseline to commit to publicly until it's re-measured (see baseline discussion in the deck).

4. **Referral volume (900/month) and "referrals get lost" are both stated as fact, but the link between them is anecdotal** ("It happens" — no number). I'm treating the *existence* of referrals as fact and the *loss rate* as an unmeasured hypothesis, not a sized problem.

---

## Task 2 — Current-State Diagram & Information Gaps

### 2A. Current-State Diagram — Prior Authorization Workflow

I picked this workflow because it's the highest-priority item from the triage and the one Priya's 20%-visits goal depends on most directly — nothing schedules until authorization clears.

```
[CLINIC] Clinician sees patient
        │
        ▼
Clinician documents visit + enters order in EHR (system of record)
        │
        ├─── 🔴 BREAK [INFERRED from Slack]: ~8 of 55 clinicians (disproportionately
        │    high-volume) do NOT chart in real time. They use a personal note template
        │    and batch entries on weekends — EHR shows nothing until then.
        ▼
[AUTH TEAM] Reviews EHR for orders requiring prior authorization
        │
        ├─── 🔴 HANDOFF BREAK: if the clinician hasn't charted yet, auth team has
        │    nothing to work from and must chase the clinician directly, ad hoc
        │    (per the Alvarez/Dr. K Slack thread — "we ask him")
        ▼
[AUTH TEAM] Gathers clinical information from the chart
        │
        ▼
[AUTH TEAM] Manually re-types/reformats clinical info into the specific payer's
portal — one of ~12 different formats, no integration between EHR and portals
        │
        ├─── 🔴 BREAK: this is the single most-cited bottleneck (Dana Reyes) —
        │    pure manual re-entry, repeated ~1,100 times/month
        ▼
[AUTH TEAM] Logs the submission in Prior Auth Tracker MASTER v7 FINAL.xlsx
(patient initials, clinician, payer, procedure, dates, status, free-text notes)
        │
        ├─── 🔴 BREAK: three systems (EHR, payer portal, spreadsheet) now hold
        │    overlapping, sometimes conflicting data. Ops treats the spreadsheet
        │    as truth because it's the only place the notes column exists.
        ▼
[PAYER — external, outside Westbrook's control] Reviews and returns a decision
        │
        ▼
[AUTH TEAM] Receives decision → updates EHR + spreadsheet
        │
        ├─── 🔴 BREAK [INFERRED]: no evidence of a systematic notification back
        │    to scheduling — appears to depend on the auth team remembering to flag it
        ▼
[SCHEDULING] Books the visit — only possible once auth is approved
```

**Decision points:** (1) Was the chart closed in real time, or does auth team have to chase it? (2) Approved / denied / pending — pending cases appear to sit with no visible SLA or escalation path in the materials.

**Actors:** Clinician, Auth Team, Payer (external), Scheduling, and implicitly the patient (who is calling to ask when they can be scheduled, per the Tanya/Rick Slack exchange, with no clear answer available to give them).

**Systems touched:** EHR, ~12 payer portals, Prior Auth Tracker spreadsheet, and an ad hoc channel (Slack, in-person) that isn't a system at all — it's a workaround for the chart-timing gap.

---

### 2B. Information Gaps

| Question | Ask Who | Changes in the plan |
|---|---|---|
| How many people work prior auth, and what's the average time per submission today? | Dana Reyes / ops lead | Determines the real ROI of the drafting assistant and how to staff the pilot. Without this I'm estimating savings, not committing to a number in front of Priya. |
| Do any of the 12 payer portals support structured upload or an API, or is every one a manual web form? | IT / Dana Reyes | Decides whether Phase 2 can include actual submission automation (bigger win) or stays draft-only forever, with auth team always doing the final manual entry. |
| What does the 8 high-volume clinicians' personal note template actually contain? | Rick O. and the clinicians directly | Determines whether we can parse their existing notes into structured data, or need to design a new lightweight capture form from scratch — very different engineering scope. |
| Which vendors/tools currently touch patient data that Alicia Grant hasn't been told about? | Alicia Grant, and separately IT/ops for an honest inventory | This is a go/no-go gate — if an LLM vendor isn't BAA-covered, nothing in the AI build can touch real patient data until that's resolved. Changes the day-one sequencing of the whole project. |
| What exactly counts as a "visit" in Priya's 20% target — unique patients, filled slots, or billed visits? | Priya Raman directly | Changes which metric we report against and whether records-request or referral work even counts toward her number, versus being adjacent-but-separate wins. |
| Does the EHR already capture referral source and date anywhere, even loosely? | Ops/IT | Determines whether referral-loop instrumentation is a same-week reporting task or a multi-week data-capture build. |

---

## Task 4 — Build Specification: Prior Authorization Clinical-Summary Drafting Assistant

**Problem (as an outcome, not a feature):** Reduce the elapsed time between a clinician's order being entered and a complete, payer-formatted prior authorization submission reaching the payer's portal — without removing the clinician's or the auth team's judgment from the process — so that authorization stops being the reason a visit can't be scheduled.

**In scope:**
- Read a patient's chart/order from the EHR once it's been entered
- Generate a draft clinical-necessity summary, formatted to the specific payer's known requirements, for auth-team review
- Let the auth team edit and approve the draft before it leaves the building
- Log status and timestamps back into the tracking system (spreadsheet or its replacement)

**Out of scope (explicitly):**
- Automatic submission into payer portals (RPA) — Phase 2, gated on Info Gap #2
- Any clinical judgment or medical-necessity attestation generated without a licensed clinician's review — the tool drafts, it never attests (per Alicia Grant's compliance note)
- Replacing the EHR or the tracker spreadsheet
- Orders from the 8 high-volume clinicians until their chart-timing/capture problem (triage item #3) is solved — there's nothing structured to draft from yet

**Systems and data involved:** EHR (read access to chart notes and orders), a documented set of per-payer format/requirement templates (these need to be built — they don't exist as structured data today, per the materials), and the Prior Auth Tracker (write access for status logging). For this to work at all, the EHR chart must exist and be reasonably complete at the time of drafting — garbage in, garbage out, and a stale or incomplete chart is worse than no draft at all.

**Where a human stays in the loop, and why:** The auth team reviews and edits every draft before submission — no draft goes to a payer unedited. Any statement of medical necessity requires the treating clinician's review and sign-off before it's submitted, per Alicia Grant: "A machine can draft it. A machine cannot be the one who attests to it." That's a hard compliance gate, not a design preference.

**Acceptance criteria:**
- Given a complete EHR chart with an order requiring prior authorization, the system produces a payer-formatted draft within a defined time window (target: under 5 minutes)
- Piloted against 3 payers first (not all 12), measuring: (a) % of drafts the auth team submits with only minor edits vs. a full rewrite, (b) time from order to submission, before vs. after, (c) first-pass approval rate, before vs. after, over a 4-week window
- Pilot is considered a pass if full-rewrite rate stays under 50% and time-to-submission drops measurably against the pre-pilot baseline

**Most likely production failure modes:**
1. **Stale or incomplete chart at draft time** → wrong or missing clinical detail in the draft. Mitigate with a pre-draft completeness check that flags missing required fields instead of drafting around gaps.
2. **Payer changes their portal format without notice** → draft no longer matches what's actually required. Mitigate with versioned per-payer templates and a simple flag-back mechanism so the auth team can report a mismatch the moment they see one.
3. **PHI touches a non-BAA-covered vendor** → compliance violation. Mitigate by hard-gating any real patient data behind Alicia Grant's written BAA confirmation; pilot and development use synthetic/de-identified data until that's signed.

**What's needed from the client before day one:** Confirmed BAA coverage for whichever AI vendor is used (Alicia Grant, blocking); EHR read access; documented submission requirements for the first 3 pilot payers; a named auth-team point of contact for the review workflow; and access to the current tracker spreadsheet structure.

**Kill condition:** If, after two pilot iterations, the full-rewrite rate is still above 50% or time-to-submission hasn't measurably improved, or if it becomes clear that no payer allows anything but fully manual re-entry regardless of draft quality — kill this and redirect the budget to a pure process fix instead: a single standardized internal intake form that at least stops the auth team from re-deriving the same information by hand every time, even without AI involved.

---

## Task 5 — AI Workflow Note

**Tools and models used, and on what:** Claude (Sonnet) for structuring the triage against the stated ranking basis, drafting the current-state diagram, writing the engineering specification, and producing the CEO deck. I fed it the raw case materials directly rather than my own summary of them, specifically so it could catch details I might skim past under time pressure.

**What I deliberately kept human:** Every judgment call that touches compliance, business risk tolerance, or Priya's specific priorities — the BAA gating decision, the kill-condition threshold, and which item to rank #1 given her stated goal. I also kept the final wording of anything resembling a clinical or attestation statement entirely out of the AI's hands, consistent with what I'm recommending Westbrook do in their own build.

**One specific thing I checked and corrected:** The first pass treated Marcus's "average turnaround of 4.2 hours" for records requests as representative of the whole process. Going back to the 12-request sample log, the real distribution is bimodal — 10 of 12 requests closed in under 15 minutes, and 2 of 12 took 1 to 4 days. The average alone would have led me to recommend a heavier process overhaul than the evidence supports; the corrected reading — a small number of requests falling into an ownerless inbox — is what's actually driving the sizing and the fix in the triage and the deck.

---

## Video Scripts

### Video 1 — The C-Suite Presentation (10 min)
Structure to actually *present*, not read, the deck:

1. **Open (30 sec):** Lead with the recommendation cold — no context first. "Priya, my recommendation is [X]. Here's why, and here's what I need from you at the end."
2. **What we found (90 sec):** Compress discovery into 3 sentences max per finding — she lived it, don't replay it. Name the prior-auth bottleneck, the records-request outlier pattern, and the referral blind spot, and immediately connect each to her 20% goal or explicitly say it doesn't move that number.
3. **Expect the interruption around minute 2** — "why not just buy one of the three platforms I've already been pitched?" Answer live, don't dodge: none of the three have confirmed BAA coverage yet, none are built around Westbrook's specific payer formats, and a narrow tool solving the bottleneck everyone already named beats a platform re-implementation that takes months before it's worth anything.
4. **90-day sequence (2 min):** Walk the phases in order and say *why that order* — quick win first to build trust and buy time for the harder build, root-cause fix in parallel, AI pilot on 3 payers before scaling to 12.
5. **Cost (1 min):** State it in both dollars and staff hours, plainly.
6. **Committed outcome (1 min):** State the number you're committing to and how it's measured — and be upfront that the baseline itself needs to be captured first, because the current data (70% approval rate, 4.2-hour average) can't be trusted as a starting point.
7. **Biggest risk (1 min):** Name it — likely the BAA/compliance gate or the 8 high-volume clinicians not adopting the new capture method — and what you're doing about it before it lands, not after.
8. **Close (30 sec):** One decision, stated as a yes/no she can actually make on the spot.

### Video 2 — You (2–3 min)
- Why this role, why Ajaia — connect to your pattern of building working prototypes before being asked (the same approach as this exercise), and your interest in the intersection of AI product judgment and real operating constraints
- What you enjoyed: probably the ambiguity-to-structure work — turning messy, contradictory source material into a rankable, defensible plan
- What you didn't enjoy: be honest here — if something felt underspecified or like it was testing format-following over judgment, say so plainly, not diplomatically
- Salary expectations: state a number or range directly, don't hedge
