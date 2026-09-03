# C03 — Annual insurance prepaid expense

This folder is a self-contained dummy case study for the NordWerk March 2026
management close. It shows how one close exception moves from source evidence
to calculation, adjusting journal, reconciliation, and management reporting.

## Scenario at a glance

| Item | Value |
|---|---|
| Company | NordWerk Cooling Systems GmbH (fictional) |
| Case | C03 — annual insurance paid in advance |
| Close date | 2026-03-31 |
| Annual premium | EUR 120,000, no recoverable VAT in this case |
| Coverage period | 2026-01-01 to 2026-12-31 |
| Payment date | 2026-01-02 |
| Pre-close error | Full premium expensed on 2026-01-02 |
| Correct closing prepaid balance | EUR 90,000 |
| Adjusting journal | EUR 90,000 debit ARAP / credit insurance expense |
| Status | Simulated and internally consistent; not a real company close |

## Package contents

- `CASE_STUDY.md` — complete narrative and accounting conclusion.
- `SOURCE_EVIDENCE_REGISTER.csv` — policy, bank, ledger, calculation, and approval evidence.
- `SYNTHETIC_INSURANCE_POLICY.md` — dummy policy evidence, visibly marked for training use.
- `SYNTHETIC_BANK_PAYMENT_EXTRACT.md` — dummy bank evidence, visibly marked for training use.
- `SYNTHETIC_LEDGER_DETAIL.md` — dummy ledger evidence, visibly marked for training use.
- `SYNTHETIC_JOURNAL_APPROVAL.md` — dummy review evidence, visibly marked for training use.
- `PRE_CLOSE_LEDGER.csv` — the erroneous original posting.
- `PREPAYMENT_CALCULATION.csv` — monthly coverage and expense schedule.
- `ADJUSTING_JOURNAL.csv` — the proposed March 31 ARAP journal.
- `MANUAL_JOURNAL_REGISTER.csv` — preparer, reviewer, approval, and reversal metadata.
- `RECONCILIATION.csv` — prepaid balance tie-out to independent support.
- `CLOSE_TASK_REGISTER.csv` — simulated close tasks and ownership.
- `CONTROL_TESTS.csv` — case-specific control results and review points.
- `MANAGEMENT_OUTPUT.md` — decision-ready management output and commentary.
- `REPORT_OUTPUT.csv` — actual/budget/adjustment/post-close tie-out.
- `SOURCE_TO_REPORT_LINEAGE.md` — ten-step audit trail.
- `FORMULA_DICTIONARY.md` — calculation definitions.
- `INTERVIEW_DEFENSE.md` — concise answers for recruiter/interview challenge.
- `DECISION_LOG.md` — case judgments and assumptions.
- `AI_USE_DISCLOSURE.md` — authorship and AI-use disclosure.

## Workbook note

The calculation and control outputs are delivered as readable CSV files in this
folder. An `.xlsx` version was not generated because the required workbook
authoring runtime was unavailable in the execution environment.

## Important disclosure

This is synthetic educational material. It is an HGB-based management-close
case, not statutory financial statements, an audit conclusion, or evidence of
live SAP experience. The accounts used here (`130100` and `570100`) are
case-study accounts within the ranges defined by the main implementation plan;
they are not yet part of the 60-event smoke-test chart.
