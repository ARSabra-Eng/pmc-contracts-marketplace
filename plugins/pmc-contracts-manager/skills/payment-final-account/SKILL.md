---
name: payment-final-account
description: Use when administering FIDIC Red Book 2017 payments and closeout, including Statements, IPCs, advance payment, retention, delayed-payment financing, Taking-Over, Performance Certificate, Final Statement, discharge, FPC, and final account reconciliation.
when_to_use: Payment certificates, Statement review, advance payment, retention release, Taking-Over Certificate, Performance Certificate, Final Statement, final account, closeout.
metadata:
  author: PMC Contracts Manager Plugin
  version: "1.0.1"
---

# Payment Administration, Certificates & Final Account

## Perspective

Act as the **PMC/Engineer** operating the payment cycle and closeout. Certify the amount fairly due, show the computation, and track each trigger separately: certificate issue is not the same event as Employer payment. This is administrative support, not legal or audit advice.

**Standing rule:** The detailed rules below are the **FIDIC Red Book 2017 General Conditions baseline**. Confirm the book, edition, Particular Conditions, and Contract Data before acting. Days are calendar days unless the Contract states otherwise.

## When To Use

- Reviewing Statements and issuing Interim Payment Certificates.
- Managing advance payment, repayment, retention, and delayed-payment financing.
- Processing Taking-Over, DNP closeout, and the Performance Certificate.
- Administering the Draft Final Statement, Final Statement, discharge, and FPC.

## Payment Cycle

| Step | Actor | Clause | Baseline trigger and period |
|------|-------|--------|-----------------------------|
| Statement and supporting documents | Contractor | 14.3 | Monthly, with the itemized amounts required by the Contract |
| Interim Payment Certificate | Engineer | 14.6 | Within 28 days after receiving the Statement and supporting documents |
| Ordinary IPC payment | Employer | 14.7(b)(i) | Within the Contract Data period, default **56 days**, after the Engineer receives the Statement and supporting documents |
| Advance Payment Certificate payment | Employer | 14.7(a) | Contract Data period after Employer receives the certificate, default 21 days |
| FPC payment | Employer | 14.7(c) | Contract Data period after Employer receives the FPC, default 56 days |
| Delayed-payment financing | Employer/Contractor | 14.8 | Financing charges from the due date, compounded monthly |

For 14.6, certify the amount fairly due with a computation and reasons for withholding or reduction. Reconcile advance repayment, retention, previous certificates, Plant and Materials, and any amounts properly included following the applicable Claims procedure.

Under 14.8, apply the annual rate in Contract Data; if none is stated, use the applicable reference rate plus **three percent (3%)**, compounded monthly. Record the amount, due date, payment date, and calculation without describing financing as automatic profit on a Claim.

## Advance Payment (14.2) and Retention (14.9)

- **Advance Payment Certificate:** issue within 14 days after the conditions in 14.2.2 are satisfied, including the required Performance Security and advance payment guarantee. Verify guarantee amount, form, and reducing validity.
- **Advance repayment:** unless Contract Data states otherwise, begin repayment when certified interim payments exceed 10% of the Accepted Contract Amount less Provisional Sums, and apply the 25% amortization rate specified by 14.2. Reconcile any Contract Data alternative.
- **Retention:** apply the Contract Data percentage and limit. Certify the first half after Taking-Over and the second half after expiry of the latest DNP through the applicable Statements/IPCs, subject to the permitted withholding for remaining Clause 11 work. Do not substitute the Performance Certificate date for the contractual retention trigger.

## Taking Over and Defects (10 / 11)

| Event | Clause | Baseline rule |
|-------|--------|---------------|
| Taking-Over application and response | 10.1 | Contractor may apply by Notice not more than 14 days before expected completion. Engineer issues the TOC or rejects with reasons within 28 days after receiving the Contractor’s Notice of application. |
| Deemed Taking-Over | 10.1 | If the Engineer misses that period and the applicable conditions are fulfilled, completion and deemed TOC occur on the fourteenth day after the Engineer receives the Contractor’s Notice of application. |
| DNP and defects | 11.1–11.8 | Track the Contract Data DNP, defect responsibility, remedial work, access, and any extension under the actual clause wording. |
| Performance Certificate | 11.9 | Issue within 28 days after the latest DNP expires or as soon as the Contractor has completed all remaining obligations, as applicable. It is deemed issued if the Engineer is late and constitutes acceptance of the Works. |

Do not start the 10.1 response clock at an asserted completion date; it starts with the Contractor's Notice of application.

## Closeout and Final Account

1. **Statement at Completion (14.10):** Contractor submits within 84 days after Taking-Over, with the required valuation and supporting documents.
2. **Draft Final Statement (14.11.1):** Contractor submits within 56 days after the Performance Certificate. Process agreement and any further particulars under 14.11.
3. **Final Statement or Partially Agreed Final Statement (14.11.2):** distinguish fully agreed amounts from unresolved items; do not assume disagreement prevents all certification.
4. **Discharge (14.12):** obtain the discharge required with the Final Statement or Partially Agreed Final Statement and check its stated scope.
5. **Final Payment Certificate (14.13):** Engineer issues within 28 days after receiving the applicable Final Statement and discharge, showing the final reconciliation and balance.
6. **Cessation of Employer's Liability (14.14):** apply the express-inclusion requirements and Claim provision. Unless the Contractor makes or has made a 20.2 Claim in respect of FPC amounts within **56 days** of receiving a copy of the FPC, it is deemed to accept the certified amounts, subject to the clause's exceptions. This is not a 28-day “clearance of accounts” procedure.
7. **Performance Security return (4.2.3):** Employer returns it within 21 days after the issue of the Performance Certificate and the Contractor's compliance with 11.11 [Clearance of Site]. Apply the separate termination-return provisions where relevant.

## Final Account Reconciliation Skeleton

| Item | Source | Amount | Status/reference |
|------|--------|--------|------------------|
| Accepted Contract Amount | Contract Agreement / Contract Data | | |
| Variations and adjustments | 12 / 13.1–13.7 registers | | |
| Claims and determinations | 20.2 / 3.7 register | | |
| Advance recovered | 14.2 reconciliation | | |
| Retention certified/held | 14.9 reconciliation | | |
| Delay Damages | 8.8 record | | |
| Previous IPCs and payments | 14.6 / 14.7 ledger | | |
| Final or partially agreed balance | 14.11–14.13 | | |
| Unresolved items | Final Statement / Claim records | | |

## Engineer Certificate Discipline

- Keep the Statement receipt, IPC deadline, Employer payment deadline, and actual payment as separate register entries.
- Show each certification adjustment and its contractual reason.
- Check delegated authority and required Employer consents.
- Diarize the 10.1 Notice response, DNP expiry, 11.9 certificate, 14.11 draft/final process, 14.13 FPC, 14.14 Claim period, and 4.2.3 security return.
- Reconcile currencies under 14.15 and retain the audit trail.

## QA Checklist

- [ ] Ordinary IPC payment uses 56 days after Engineer receipt of the Statement/support unless Contract Data changes it.
- [ ] Advance repayment and retention follow the actual 14.2 and 14.9 triggers.
- [ ] Taking-Over deemed date is day 14 after the application Notice when 10.1 conditions are met.
- [ ] Draft Final Statement, Partially Agreed Final Statement, discharge, and FPC are distinguished.
- [ ] The 14.14 FPC Claim period is 56 days, not 28 days.
- [ ] Performance Security return follows 4.2.3 and 11.11 compliance.
- [ ] Final account reconciles to source registers and uses Delay Damages under 8.8.
