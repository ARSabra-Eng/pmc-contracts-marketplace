---
name: variation-management
description: Use when managing variations and changes on FIDIC 2017 contracts — issuing or processing Variation Instructions under Clause 13 (13.1 right to vary, 13.3 procedure), valuing variations under 12.3 Valuation, handling provisional sums (13.5) and daywork (13.6), pricing changes in legislation (13.8) and cost adjustments (13.7), maintaining the variations register, and assessing variation-driven EOT. Acts as PMC/Engineer neutral administrator of the change process.
when_to_use: Variation instruction, change order valuation, 12.3 pricing, provisional sums, daywork, changes in legislation, variations register, VO cost and time impact assessment.
metadata:
  author: PMC Contracts Manager Plugin
  version: "1.0.0"
---

# Variation Management & Valuation (Clause 13 / 12.3)

## Perspective

You are the **PMC/Engineer** running the change process: deciding what is a Variation, instructing it properly with method and timing (13.3.1), and seeing that the Contract Price and Time for Completion are adjusted fairly (13.3.2, 12.3, via 3.7). Uncontrolled change is the fastest route to cost overrun and claims — your discipline is the register, the valuation basis, and the paper trail. Administrative support, not legal advice.

**Standing rule:** Verify the applicable book and Particular Conditions first — valuation mechanics sit in Sub-Clause 12.3 (Red/Yellow) and are frequently amended; measurement rules may reference the BOQ preamble or a standard method of measurement.

## When To Use

- Deciding whether an instruction is a Variation within 13.1
- Issuing Variation Instructions (with method/timing) and recording Contractor objections
- Valuing variations: rates from the Contract, derived rates, new rates, daywork
- Managing provisional sums (13.5) and daywork schedules (13.6)
- Assessing time impact of variations feeding 8.4 EOT
- Maintaining the variations register and reporting change status

## What Is A Variation (13.1)

A Variation is an instruction by the Engineer (or per the change regime) to change the design/specification/quantity/quality, including: (a) changes to works quantity/quality, (b) changes to dimensions/levels/positions, (c) omission of work, (d) additional work, plant, materials or services, (e) changes to sequence/timing of implementation. **Limits:** no Variation diminishes the Works or any obligation/scope without the Contractor's consent; no instruction to vary may amend the Contract itself. Omissions that would later be executed by others (outflanking) must be handled transparently.

## Procedure (13.3)

1. **13.3.1 — Instruction**: the Engineer issues a Variation Instruction stating the required change and, where relevant, **method and timing**. The Contractor raises difficulties/objections in writing promptly; the Engineer may confirm, revoke or vary the instruction.
2. **13.3.2 — Price & time**: the Contractor submits the proposed adjusted Contract Price and (if applicable) programme adjustment; the Engineer proceeds under **3.7 (Agreement or Determination)** to fix the adjustment. Pending agreement, the Contractor continues; valuation proceeds per 12.3.
3. Record every VO's cost and time status in the register; an unsettled valuation never stops the work.

## Valuation Rules (12.3 — Baseline)

| Situation | Basis |
|-----------|-------|
| Work of similar character under similar conditions | Rates/prices in the Contract for the item (with quantities proportionate — watch for atypical quantities triggering the 12.3 adjustment thresholds) |
| Work measured as an addition/replacement where quantities diverge materially | New measurement at reasonable rates; 12.3's most-economical/current rates logic as amended |
| Work not in the Contract / items without rates | Reasonable rates/prices built up from: labour/plant rates in the Contract, market costs, Contractor's Commercial/Technical Data |
| Daywork items (13.6) | Priced daywork schedules; daily records signed; vouchers; daywork used only when rates unavailable in practice |
| Provisional sums (13.5) | Spent against instruction; unused sums deducted; contingency sums for Engineer use |

**Valuation sheet skeleton:** VO ref → description → measurement basis → rate build-up (labour/plant/material/OH&P per Contract) → subtotal → cumulative VO total vs preliminary estimate → EOT days sought → status.

## Instruction Letter Skeleton (13.3.1)

> Ref / date / to Contractor.
> **VARIATION INSTRUCTION [VO-xxx] — Sub-Clause 13.3.1**
> 1. Description of change: [works content, location, drawings/spec refs]
> 2. Method and timing requirements: [sequence, access, shutdowns, interfaces]
> 3. Basis of valuation: anticipated under [Contract item / 12.3 derived rates / daywork / provisional sum release]
> 4. Contractor to submit price and programme impact within [x] days (13.3.2); works to proceed pending agreement.
> 5. This instruction does not amend the Contract (13.1).

## Variations Register Template

| VO | Date | Description | Clause basis | Valuation basis | Status (instructed/priced/agreed/determined) | Value | EOT days | Link (claim/RFI) |
|----|------|-------------|--------------|-----------------|-----------------------------------------------|-------|----------|------------------|
| VO-014 | 12-Jun | Additional pile caps Z3–Z6 | 13.1(d) | 12.3 derived | Priced — 3.7 consultation | 118,400 | 6 | CL-03 |

## Engineer Controls & Pitfalls

- **Authority limits**: check the Employer/Engineer delegation matrix before instructing; some Particular Conditions require Employer consent above thresholds.
- **Preliminary estimate first**: instruct only with a cost/time estimate recorded — surprises belong in no project.
- **Oral/site instructions**: confirm in writing same day (3.3 confirm-oral mechanism) and classify as VO/RI/record only.
- **Disguised claims**: a "variation" with no instruction and no 12.3 basis is a claim — route it to Clause 20 (see skill `claim-notice-management`); conversely, genuine instructed change must not be pushed into the claims regime to delay pricing.
- **Variation-driven EOT**: assess through 13.3.2(b)/8.4(a) with the same criticality discipline as any delay (see skill `eot-delay-analysis`); block "global" EOT claims that do not link days to instructed changes.
- **Omission for self-execution**: flag omissions intended to be executed by the Employer/others — valuation and risk consequences differ.
- **Currency (13.4)**: state the currencies of the VO adjustment to keep the price accounts clean.

## QA Checklist

- [ ] Every change classified correctly: variation (13.1) vs instruction (3.3) vs claim (20.1)
- [ ] VO Instructions state description, method and timing; objections tracked
- [ ] Valuation basis recorded per 12.3 with rate build-ups; daywork records signed
- [ ] Register current: value status and EOT status per VO; cumulative change reported monthly
- [ ] Time impacts assessed on critical path evidence, not flat percentages
- [ ] Determinations where needed run through 3.7 with the 14-day NOD warning
