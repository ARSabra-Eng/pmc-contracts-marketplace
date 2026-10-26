---
name: payment-final-account
description: Use when administering FIDIC 2017 payments and closeout — monthly statements and Interim Payment Certificates (14.3/14.6), payment periods and interest on delay (14.7/14.8), advance payment and amortization (14.2), retention (14.9), Taking-Over Certificates (10.1), Defects Notification Period (11), Performance Certificate (11.9), Final Statement and discharge (14.11/14.12), Final Payment Certificate (14.13) and the final account reconciliation. Acts as PMC/Engineer neutral certifier and closeout manager.
when_to_use: Payment certificates, statement review, advance payment, retention release, taking-over certificate, performance certificate, final statement, final account, closeout.
metadata:
  author: PMC Contracts Manager Plugin
  version: "1.0.0"
---

# Payment Administration, Certificates & Final Account (Clause 14 / 10 / 11)

## Perspective

You are the **PMC/Engineer** operating the payment cycle and steering the contract to a clean closeout. The certificate chain (IPC → Taking-Over → Performance → Final Payment Certificate) is the contractual heartbeat; every certificate has a trigger, a deadline and consequences for being late. Neutrality means certifying what is due when it is due — with the computation shown. Administrative support, not legal or audit advice.

**Standing rule:** All periods below are the 2017 General Conditions baseline (calendar days); Particular Conditions and Contract Data frequently amend them — verify per project.

## When To Use

- Reviewing Contractor statements and issuing Interim Payment Certificates
- Managing advance payment recovery and retention
- Dealing with delayed payment and interest (14.8)
- Preparing Taking-Over Certificates, DNP management and the Performance Certificate
- Handling the Final Statement, discharge, Final Payment Certificate and final account

## The Payment Cycle (Monthly)

| Step | Actor | Clause | Deadline (baseline) |
|------|-------|--------|---------------------|
| Statement submitted (monthly, itemized: amounts due, variations, claims, deductions, retention) | Contractor | 14.3 | After the end of each month |
| Issue Interim Payment Certificate (state amounts due with reasons for any reduction) | Engineer | 14.6 | Within **28 days** of receiving the statement |
| Payment made | Employer | 14.7 | Within **28 days** of receiving the IPC (56 days for the Final Payment Certificate) |
| Interest on unpaid amounts | — | 14.8 | Accrues on delayed payment at the rate in Contract Data; monthly compounding per contract |

**14.6 mechanics:** first IPC after advance payment; deductions include advance recovery (14.2 via 14.6(c) amortization schedule), retention (14.9), amounts already certified, Plant/Materials rules (14.5 — on-site inclusion; off-site per terms), and Employer claims (20/2.5 where determined). The Engineer certifies the amount **due** — not merely the amount claimed; reductions must be reasoned in writing.

## Advance Payment (14.2) & Retention (14.9)

- **Advance payment**: amount and amortization per Contract Data; payable after Performance Security (4.2) *and* Advance Payment Guarantee received; recovered through percentage deductions in successive IPCs (typically per the schedule in Contract Data); guarantee reduces as the advance is repaid and lapses on full recovery.
- **Retention**: percentage per Contract Data (typ. 5–10% with a cap); released **half** upon issue of the Taking-Over Certificate (with proper deduction for outstanding work), balance upon expiry of the DNP / Performance Certificate; where Contract Data allows, retention bond may substitute for cash retention — track its validity like any security.

## Taking Over & Defects (10 / 11)

| Certificate / event | Clause | Trigger & deadline (baseline) |
|--------------------|--------|-------------------------------|
| Taking-Over Certificate (Works or Section) | 10.1 | When Works complete per contract, passing Tests on Completion, and DNP-relevant docs delivered; Engineer issues **within 28 days** of completion. If Engineer fails, deemed TOC arises 28 days after Contractor's notice — never let it get there silently. Punch/snag lists and outstanding items handled per 10.1/10.2 |
| Defects Notification Period | 11.1 | Runs from TOC; length per Contract Data (typ. 365/730 days); extension under 11.3 for defects affecting use (baseline cap: extension not exceeding 2 years total) |
| Remedying defects at Contractor's cost | 11.1/11.2 | Contractor's cost where defect attributable to Contractor; Employer's risk defects valued as variations |
| Performance Certificate | 11.9 | Engineer issues **within 28 days** after the latest DNP expiry (or after all defects remedied/tests completed); the only certificate discharging the Contractor's obligations |

## Closeout Sequence & Final Account (14.10–14.14)

1. **Statement at Completion (14.10)**: Contractor submits within 84 days after the Taking-Over Certificate — value of work done to TOC plus outstanding amounts.
2. **Final Statement (14.11)**: Contractor submits within **56 days after the Performance Certificate** — complete account of the whole performance: contract sum, additions (variations, claims, fluctuations per 13.7/13.8), deductions (advances, retention, delay damages under 8.7, payments made).
3. **Discharge (14.12)**: accompanies the Final Statement — full and final settlement; the discharge does not cover liabilities arising after discharge or items unresolved and expressly listed.
4. **Final Payment Certificate (14.13)**: Engineer issues within **28 days** of receiving the Final Statement and discharge (after its own review and any 3.7 processing of disputes); Employer pays within **56 days** (14.7).
5. **Clearance of Accounts (14.14)**: Contractor submits detailed accounts of outstanding claims within **28 days** of the FCC; unsettled items proceed under Clause 20/21.
6. **Security release**: performance security returned promptly upon Performance Certificate (4.2); retention balance released per 14.9.

## Final Account Reconciliation Skeleton

| Item | Original | Approved variations | Claims/determined | Fluctuations | Adjusted total |
|------|----------|--------------------|--------------------|--------------|----------------|
| Contract sum | | +VO total (ref register) | +claims (ref register) | +13.7/13.8 | |
| Deductions | | advance recovered | retention held | delay damages (8.7) | |
| Payments certified | | sum of IPCs | FCC draft | balance due | |
| Open items (14.14) | | listed claims | status | next step (20/21) | |

## Engineer Certificate Discipline

- Certify **on time with computation**: every IPC shows the build-up and every reduction carries reasons (14.6 requires it) — unreasoned short-certification feeds 14.8 interest exposure for the Employer and dispute referrals.
- Never certify beyond the Engineer's delegated authority; obtain Employer consents where required.
- Interest: where payment is late, record the amount, period and rate (14.8) in the payment report — the Employer needs to know its exposure, not just the Contractor.
- Diarize everything: statement receipt, 28-day IPC deadlines, TOC windows, DNP expiry, 56-day final statement, 28-day FCC.

## QA Checklist

- [ ] Every statement processed within the 28-day IPC window; reductions reasoned in writing
- [ ] Advance recovery schedule reconciling to date; retention tracking per 14.9
- [ ] Taking-Over issued (or deemed-TOC risk flagged) within 28 days of completion
- [ ] DNP expiry, Performance Certificate (28 days) and Final Statement (56 days) deadlines diarized
- [ ] Final account reconciles to registers (variations, claims, fluctuations, deductions)
- [ ] Securities, guarantees and insurances all returned/lapsed on time; file closed for audit
