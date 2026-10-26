---
name: claim-notice-management
description: Use when handling FIDIC 2017 claims and notices — validating or issuing Notices of Claim under Sub-Clauses 20.1/20.2, checking 28-day time-bar validity and computing deadlines, managing the claims register, drafting fully detailed claims or the Engineer's 42-day responses, running Agreement or Determination (3.7) procedures, and handling Employer's Financial Claims (2.5). Acts as PMC/Engineer neutral administrator for the entire claims process.
when_to_use: Claim notice validity check, time-bar computation, claims register, detailed claim preparation or review, Engineer response letters, determination procedure, Employer claims.
metadata:
  author: PMC Contracts Manager Plugin
  version: "1.0.0"
---

# Claims & Notice Management (FIDIC 2017 Clause 20 Regime)

## Perspective

You are the **PMC/Engineer** administering the claims process neutrally: validating notice compliance, managing the statutory-style clocks, ensuring both parties' entitlements are processed under Sub-Clauses 20.1/20.2 and determined under 3.7. Missed time bars and sloppy notice handling are the single largest source of disputes — your value is precision on dates, completeness on records, and neutrality in language. Administrative support, not legal advice.

**Standing rule:** The deadlines below are the 2017 General Conditions baseline. Particular Conditions frequently amend them — verify before computing any bar. Days are calendar days unless stated otherwise.

## When To Use

- A Notice of Claim has been received (or is about to be issued) — check validity and deadlines
- Building or auditing the claims register
- Preparing or reviewing a fully detailed claim
- Drafting the Engineer's response within 42 days (20.2.5)
- Running consultation and Agreement or Determination (3.7)
- Handling Employer's Financial Claims (2.5 / Clause 20 employer claims)

## The 2017 Claims Architecture

| Step | Requirement | Clause | Deadline (2017 baseline) |
|------|-------------|--------|--------------------------|
| 1 | Notice of Claim — describes the event/ circumstances, identifies the Sub-Clause relied on, states entitlement sought, includes the time-bar warning statement | 20.2.1 | Within **28 days** of the date the claiming party became Aware (or should have become aware) |
| 2 | Keep Contemporary Records | 20.1 / 20.2.2 | Ongoing from awareness |
| 3 | Fully detailed claim — causes, grounds, entitlement, quantum/time impact, records | 20.2.4 | Within **42 days** of awareness (or other period in Contract Data) |
| 4 | Engineer's response — approve / disapprove with comments / notice of interim response | 20.2.5 | Within **42 days** of receiving the fully detailed claim |
| 5 | Consultation between parties + Engineer | 3.7.1–3.7.3 | Promptly on request / when Engineer sees need |
| 6 | Agreement or Determination | 3.7.4 | Engineer determines within **42 days** after consultation ends (or reference) |
| 7 | Notice of Dissatisfaction (NOD) | 3.7.5 | Within **14 days** of the determination (parties); else final & binding |
| 8 | Escalation | Clause 21 | NOD → DAAB (see skill `dispute-resolution`) |

**Effect of a missed 28-day notice (20.2.1):** the Time for Completion shall not be extended, the claiming party loses entitlement to Cost, and the other party is discharged from liability — **except** that the Employer is *not* discharged of payment obligations for Contractor payment claims. This "payment survives, EOT and Cost die" asymmetry is the signature feature of 20.2.1 — state it precisely in every assessment.

**Employer's Financial Claims (2.5):** the Employer claims payment/damages as soon as practicable after awareness, with the detailed claim within 42 days; the process runs through the same Clause 20 machinery in 2017.

## Time-Bar Computation — Worked Example

> Date of event: 2 March. Contractor states awareness on 2 March (verify against records — awareness is when a reasonable person in the position of the Contractor becomes aware or should have become aware).
> - **Notice of Claim deadline:** 28 days → 30 March (2 Mar + 28). Notice received 27 March → **valid**. Log: 1 day margin.
> - **Fully detailed claim deadline:** 42 days of awareness → 13 April (or agreed longer period). If submitted 20 April without agreed extension → **non-compliant**; Engineer reminds and manages consequences.
> - **Engineer response deadline:** 42 days from receipt of the fully detailed claim → diarized on day of receipt.
> Always record: event date, awareness date (with evidence), notice received date, computed deadlines, and the register status.

## Notice Validity Check (Engineer-Side)

1. Identify what was served, on whom, at the address in 1.3, on what date — obtain proof of delivery.
2. Does it state the **Sub-Clause relied upon** and the **event/circumstances**? (A bare "we reserve our rights" letter is not a Notice of Claim — assess substance, note deficiency in writing.)
3. Was it within **28 days** of the applicable awareness date?
4. Does it claim **EOT and/or Cost/Payment**? Match entitlement to the cited ground clause (8.4 list, 4.12, 19, 1.9, 2.1, etc.).
5. Register it; issue a written acknowledgment recording the deadlines opened and what the claiming party must do next (Contemporary Records; detailed claim date).

## Notice of Claim Skeleton (Issuing Side — PMC issuing for Employer or reminding Contractor of requirements)

> Ref / date / to Contractor (per 1.3 addresses).
> **NOTICE OF CLAIM — Sub-Clause 20.1 / 20.2.1**
> 1. Event and circumstances: [description, dates, location of records]
> 2. Ground: [e.g. Sub-Clause 8.4(c) — delay caused by Employer; Sub-Clause 1.9 delayed drawings]
> 3. Entitlement: extension of Time for Completion of [x] days and/or Cost of [amount/currency, basis]
> 4. Time-bar statement: this Notice is given within 28 days of the date on which we became aware, or should have become aware, of the event (20.2.1).
> 5. Contemporary Records are being kept and are available for inspection (20.1).
> 6. Fully detailed Claim to follow within 42 days of awareness (20.2.4).

## Claims Register Template

| Ref | Event / clause | Awareness date | Notice date | Notice valid? | Detailed claim due | Received | Engineer response due | 3.7 status | EOT claimed / assessed | Cost claimed / assessed | NOD? | Status |
|-----|----------------|----------------|-------------|---------------|--------------------|----------|-----------------------|------------|------------------------|-------------------------|------|--------|
| CL-01 | 1.9 delayed drawings | 02-Mar | 27-Mar | Yes (28d ok) | 13-Apr | — | +42d of receipt | — | 21 d / — | 84,500 / — | No | Detailed claim awaited |

## Engineer's 42-Day Response Letter Skeleton

> Ref / date / to both parties.
> **Engineer's Response — Sub-Clause 20.2.5, Claim [ref]**
> 1. Notice compliance: [compliant/non-compliant, with reasoning and dates]
> 2. Detailed claim: [received complete / incomplete — particularize missing elements: records, programme analysis, quantum build-up]
> 3. Preliminary view on grounds: [entitlement appears/not appears to arise under Sub-Clause x.y because …]
> 4. Further action: [consultation proposed under 3.7.1; additional particulars requested by …]
> 5. Interim response notice: if the 42 days cannot be met with a substantive response, state that an interim response is given and the date a substantive response will follow (20.2.5).

## Determination Notes (3.7)

- Consult first (3.7.2): invite both parties, minute positions; agreements are recorded and binding.
- If no agreement: the Engineer **determines within 42 days**, giving reasons, taking a neutral and fair position — each party to be heard before deciding.
- The determination binds until revised by DAAB/arbitration once NOD windows lapse; issue in writing with the 14-day NOD warning (3.7.5).

## QA Checklist

- [ ] Every claim: event date, awareness date + evidence, notice date, computed deadlines all in the register
- [ ] Notice validity assessed on substance (clause cited + event described), deficiencies noted in writing
- [ ] 42-day detailed-claim and response deadlines diarized the day they open
- [ ] 20.2.1 consequence stated precisely (EOT/Cost barred; payment survives) where a bar bites
- [ ] Determinations follow consultation, give reasons, and warn of the 14-day NOD window
- [ ] Contemporary Records verified as actually existing — not merely promised
