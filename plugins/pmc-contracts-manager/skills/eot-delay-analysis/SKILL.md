---
name: eot-delay-analysis
description: Use when assessing Extension of Time (EOT) claims or delays — reviewing EOT entitlement under Sub-Clause 8.4, selecting and reviewing delay analysis methods (Time Impact Analysis, windows, as-planned vs as-built, collapsed as-built per the SCL Delay and Disruption Protocol), checking criticality and concurrency, assessing prolongation quantum, and drafting the Engineer's EOT assessment or determination. Acts as the PMC/Engineer neutral assessor of time entitlement.
when_to_use: EOT assessment, delay analysis review, TIA review, criticality and concurrency assessment, prolongation cost review, EOT determination letters, acceleration questions.
metadata:
  author: PMC Contracts Manager Plugin
  version: "1.0.0"
---

# EOT Assessment & Delay Analysis

## Perspective

You are the **PMC/Engineer** assessing whether delay events entitle the Contractor to an extension of the Time for Completion (8.4), how many days, and what prolongation Cost follows. Neutrality and method discipline are everything: a defensible EOT assessment follows a recognized methodology, works from contemporaneous records and updated programmes, and confronts concurrency explicitly. Administrative and technical assessment support, not legal advice or programming testimony.

**Standing rule:** EOT entitlement requires (i) a valid Notice of Claim under 20.2, (ii) a ground under Sub-Clause 8.4 or a delay-related Sub-Clause, (iii) demonstrated criticality on a compliant programme, (iv) proper analysis method, and (v) mitigation considered. Confirm all Particular Conditions amendments first (some contracts delete or recast 8.4).

## When To Use

- Contractor's EOT claim received — assess entitlement, method, and days
- Preparing the Engineer's assessment or 3.7 determination on time
- Deciding which delay analysis method is appropriate for the case
- Concurrency, float ownership, or acceleration questions arise
- Reviewing whether prolongation cost substantiation is adequate

## EOT Grounds Map (Sub-Clause 8.4 + delay-related clauses)

| Ground (8.4) | Basis |
|--------------|-------|
| (a) | Variation or substantial change in quantity (unless circumstantial to other ground) — 13.3.2 |
| (b) | A cause under Sub-Clause 8.5 (authorities) or a ground in other Sub-Clauses |
| (c) | Exceptional Event of the kind described in Clause 19 |
| (d) | Delay or impediment caused by or for which the Employer is responsible (e.g. 2.1 access, 1.9 drawings, 8.1 commencement issues) |
| (e) | Unforeseeable shortage of personnel/goods caused by epidemic/government action |
| (f) | Any delay/impediment attributable to the Employer, Engineer's personnel, or their contractors |
| Related | 4.12 unforeseeable physical conditions; 1.9 delayed drawings/instructions; 2.1 access; 5.x nominated subcontractor delays; 8.5 authorities; 16/19 suspension-linked; 13.7/13.8 changes |

The Contractor must give notice under 20.2 and demonstrate the delay is on the critical path to Time for Completion; the Engineer may also be obliged to revise the programme implications (8.3) and consider required steps to overcome delay (8.6 rate of progress context).

## Method Selection (SCL Delay & Disruption Protocol 2nd Ed. Baseline)

| Method | Type | Best for | Cautions |
|--------|------|----------|----------|
| Time Impact Analysis (TIA) | Prospective | Claims assessed as they occur; Contractor submits revised programme with the event inserted | Requires reliable updated programme; Engineer checks logic of inserted event |
| Windows analysis (period-by-period) | Retrospective | Final EOT at closeout; multiple overlapping delays | Depends on good progress records; choose windows defensibly (update dates/decision points) |
| As-planned vs as-built | Retrospective | Quick triage; simple, short projects | Does not by itself prove criticality or causation |
| Collapsed as-built | Retrospective | Testing "but for" the delay event | Sensitive to as-built data quality; model risk |
| Impacted as-planned | Prospective | Early estimates on static baseline | Ignores actual progress — weakest alone |

**Assessment rules of practice:** use the most recent accepted programme compliant with 8.3; verify the critical path actually runs through the affected activities; require the analysis to show causation (event → activity → critical path → days) rather than assert it; cross-check against as-built records.

## Concurrency & Float — Working Positions

- **Dominant cause:** where multiple causes compete, apportion to the dominant effective cause of delay (SCL guidance).
- **True concurrency** (two or more events delay completion at the same time, each alone sufficient): Contractor EOT for Employer-risk periods, but generally no prolongation Cost for the concurrent Contractor-risk period (mitigation of Cost).
- **Float:** programme float belongs to the project unless the contract says otherwise; the Employer may not use the Contractor's float for its own convenience, and the Contractor's use of float is not a delay — but consuming float can convert a later event into criticality (Time-at-Risk visibility in 8.3 programmes).
- Record the position taken in the assessment with reasoning; concurrency findings must be evidence-based, not asserted.

## Assessment Workflow

1. **Notice check**: 20.2.1 notice valid (see skill `claim-notice-management`)? Note bar consequences precisely.
2. **Ground mapping**: which 8.4 ground(s)/clauses are cited; is the event Employer-risk or neutral-risk? Contractor-risk events get no EOT.
3. **Programme check**: latest accepted programme status; if analysis relies on a non-compliant model, require resubmission — note the 42-day response clock is managed via interim response where needed (20.2.5).
4. **Criticality & causation review**: does the event sit on the critical path? Inserted-event logic correct? Records corroborate the as-built sequencing?
5. **Concurrency & float**: apply the positions above; document findings.
6. **Quantify days**: state EOT days with dates (revised Time for Completion if applicable), distinguishing excusable-relevant vs excusable-neutral where the contract distinguishes Cost.
7. **Prolongation Cost review** (where Cost follows the ground): site overheads actual records first (recorded costs, not percentages); head-office overheads by actual cost or recognized formula (Eichleay in US-influenced forums; Hudson-type rates only with caution and evidence); financing charges per contract; disruption separately analyzed by measured mile; profit where the ground allows it (8.4 typically entitles Cost + reasonable profit for Employer-responsible grounds — verify the clause text).
8. **Mitigation & 8.6**: what reasonable steps were required; acceleration is not presumed — constructive acceleration needs clear elements (entitlement established, instruction/denial, notice, acceleration done, cost).
9. **Issue the assessment** (letter skeleton below); if challenged, proceed to 3.7 consultation/determination.

## Engineer's EOT Assessment Skeleton

> Ref / date / to both parties.
> **Engineer's Assessment — Extension of Time, Claim [ref], Sub-Clauses 8.4 / 20.2**
> 1. Notice compliance: [dates, validity]
> 2. Ground: [8.4 sub-paragraph / clause relied on]
> 3. Programme and method relied on: [accepted programme rev/date; TIA rev; windows]
> 4. Criticality finding: [critical path description, evidence]
> 5. Concurrency finding: [analysis]
> 6. **Determination of time:** EOT of [x] days; revised Time for Completion [date].
> 7. **Cost:** [assessment basis, amounts, or "to be assessed following substantiation under 20.2.4"]
> 8. Notice of Dissatisfaction: this assessment is subject to Sub-Clause 3.7.5 (14 days) and Clause 21.

## QA Checklist

- [ ] Notice valid before entitlement analyzed; consequences stated if barred
- [ ] Ground cited matches the event facts (employer-risk vs neutral vs contractor-risk)
- [ ] Analysis method justified; programme used is accepted/compliant with 8.3
- [ ] Critical path verified against records, not taken from the claim at face value
- [ ] Concurrency and float addressed explicitly with reasoning
- [ ] Prolongation cost built from contemporaneous records; formula use explained and evidence-backed
- [ ] Mitigation/8.6 considered; no constructive acceleration finding without all elements
- [ ] Assessment issued within the 42-day response window or via documented interim response
