# NordWerk D+5 Month-End Close — Detailed Implementation Plan

## 1. Decision

This will be the first flagship project from the German FP&A and controller roadmap.

The final, defensible project claim is:

> Designed and executed a simulated D+5 March management close for one German manufacturing entity using an HGB-based local ledger, ERP-shaped synthetic source data, six balance-sheet reconciliations, documented adjusting entries, a controlled close workflow, and an actual-versus-budget management pack.

This wording is deliberate.

- It is a simulated close, not real employment.
- March is a management close, not a statutory annual close.
- The ledger uses HGB-based recognition, classification, and valuation policies.
- The source data resembles common ERP finance structures, but no SAP instance is being claimed.
- The project proves accounting control and management interpretation rather than software novelty.

## 2. Why this project comes first

Current German FP&A and controller roles repeatedly combine:

- Month-end reporting.
- Accruals, reclassifications, provisions, and prepayments.
- Actual-versus-budget and forecast analysis.
- SAP or another ERP.
- Excel and increasingly Power BI.
- Data quality and reconciliation.
- Management commentary and recommendations.

Examples include:

- [Redcare Graduate FP&A Analyst](https://jobs.smartrecruiters.com/Redcare-Pharmacy/744000137065155--graduate-fp-a-analyst-cost-controlling-m-f-d-), which combines budgeting, forecasting, month-end reporting, variance analysis, Excel, Power BI, Power Query, SQL, and AI.
- [AUMOVIO Controller](https://jobs.smartrecruiters.com/Aumovio/744000105134589-ff-controller), which includes fixed-cost controlling, provisions, intercompany invoices, SAP FI/CO, forecasts, review meetings, and management support.
- [Reinert-Ritz Junior Controller](https://www.reinert-ritz.de/karriere/jobs-in-der-organisation-bei-reinert-ritz/junior-controller/), which includes HGB-based close support, cost centres, inventory changes, planning, ERP, and investment analysis.
- [NielsenIQ FP&A Operations](https://jobs.smartrecruiters.com/NielsenIQ/744000136280581-senior-fp-a-analyst-operations), which explicitly mentions purchase requisitions, invoices, accruals, prepayments, forecast support, SAP, and reporting.

SAP describes month-end closing as all activities required to close a posting period, including external reporting, reconciliation, documentation, and internal evaluations. Its closing tools also emphasize task dependencies, status monitoring, comments, attachments, approvals, and audit trails. See [SAP Month-End Closing](https://help.sap.com/doc/8353d7531a4d424de10000000a174cb4/700_SFIN3E%20006/en-US/0a15d353c6244308e10000000a174cb4.html), [SAP Accounting and Financial Close](https://help.sap.com/docs/s4hana-cloud-best-practices/accounting-and-financial-close-j58-rs/purpose?locale=en-US), and [SAP Process Closing Tasks](https://help.sap.com/docs/advanced-financial-closing/administration/ae51205499f549558eadd8a2c190d1b5.html).

The project therefore targets the most important missing signal in Mann's current profile: routine, traceable, review-ready financial discipline.

## 3. Idea-challenger review and resulting scope

An independent idea-challenger reviewed the initial proposal before this implementation plan was finalized.

### Criticisms accepted

1. A close-only project could position Mann as an accountant and undersell him for FP&A.
   - Response: the project includes a serious but bounded actual-versus-budget management pack with drivers, recurrence assessment, action, owner, and expected next-period effect.

2. “Delivered a five-day close” would be an overclaim.
   - Response: the project is described as a simulated D+5 close workflow.

3. “HGB March close” could be misleading because HGB governs statutory accounts and March is not the annual reporting date.
   - Response: the project uses an HGB-based local ledger for a March management close and makes no audit or statutory-compliance claim.

4. A large random dataset would turn the project into a data-engineering exercise.
   - Response: the MVP uses approximately 3,000–5,000 GL lines with carefully designed accounting relationships and 15 seeded close issues.

5. “SAP-like” could imply experience that was not obtained.
   - Response: the disclosure will say “ERP-shaped synthetic exports modeled on common FI/MM/AA/CO concepts. No SAP instance was used.”

6. IFRS, consolidation, deferred taxes, leases, pensions, tax returns, and multiple entities would create too much technical risk.
   - Response: all are removed from the MVP. A single, peer-reviewed HGB-to-IFRS adjustment may be added in Phase 2.

7. Synthetic data could make the analysis circular.
   - Response: the build includes immutable pre-close files, an independent ground-truth manifest, negative tests, source evidence, and source-to-report lineage.

8. Authorship may be challenged because AI is used.
   - Response: the project includes Git history, a decision log, a formula dictionary, a model-change log, tests, an AI-use disclosure, and an interview question file.

### Governing principles

- Accounting correctness before visual sophistication.
- Explainable exceptions before transaction volume.
- Management action before technical novelty.
- Evidence before presentation.
- Reproducibility before automation claims.

## 4. MVP boundary

### Included

- One German GmbH.
- One manufacturing site.
- One company code.
- EUR functional and reporting currency.
- December 31, 2025 opening trial balance.
- January–March 2026 operating activity.
- March 2026 pre-close and post-close trial balances.
- Approximately 3,000–5,000 GL lines.
- AR, AP, bank, inventory, fixed-assets, and GR/IR reconciliations.
- Ten finished products and approximately 20 inventory materials/SKUs.
- Eight cost centres.
- Six foreign-currency open items.
- Fifteen deliberately designed close issues.
- Eight to twelve adjusting journals.
- D−3 to D+5 close workflow.
- HGB-formatted balance sheet and P&L mapping.
- Actual-versus-budget management analysis.
- Five- or six-page management pack.
- Automated validation tests.
- Documentation and interview-defense material.

### Explicitly excluded from the MVP

- IFRS conversion.
- Consolidation.
- Intercompany elimination.
- Deferred tax.
- IFRS 16 lease accounting.
- Pensions.
- Full VAT return.
- Corporate-income-tax calculation.
- Statutory notes or management report.
- Audit opinion or statutory-compliance claim.
- Multiple legal entities or plants.
- Multiple functional currencies.
- Live SAP, SAP configuration, or SAP screenshots.
- Custom web application.
- AI-generated journal approval.
- Power BI if it delays the reconciled Excel close.
- A full cash-flow statement.
- More than one monthly close.

### Phase 2

Only after the MVP passes every acceptance criterion:

1. April 2026 close, including reversal handling.
2. Flash-versus-final result analysis.
3. Power BI reporting from reconciled close outputs.
4. Close-process efficiency metrics.
5. Expanded business-partner action tracking.
6. One carefully researched HGB-to-IFRS adjustment.
7. Independent review by an accounting-qualified person.

The April close is more important than increasing March data volume because it proves repeatability.

## 5. Fictional company specification

### Company

**NordWerk Cooling Systems GmbH**

### Business

NordWerk produces thermal-management components for electric and hybrid vehicles. Its customers are European automotive OEMs and Tier-1 suppliers.

### Operating profile

| Attribute | Specification |
|---|---|
| Legal form | German GmbH |
| Location | Leipzig, Germany |
| Company code | DE01 |
| Controlling area | NW01 |
| Financial year | Calendar year |
| Functional currency | EUR |
| Reporting currency | EUR |
| Employees | Approximately 120 |
| Cost centres | 8 |
| Finished products | 10 |
| Raw and packaging materials | Approximately 20 |
| Customers | Approximately 25 |
| Vendors | Approximately 60 |
| Fixed assets | Approximately 30 |
| Monthly revenue | Approximately €2.5–€3.5 million |
| Annualized revenue | Approximately €35 million |
| Reporting period | March 2026 |
| Management close target | D+5 |

### Cost centres

| Code | Cost centre |
|---|---|
| CC100 | Production |
| CC110 | Maintenance |
| CC120 | Quality |
| CC130 | Warehouse and Logistics |
| CC200 | Procurement |
| CC300 | Sales |
| CC400 | Engineering |
| CC500 | Finance, HR, and Administration |

### Profit centres

| Code | Profit centre |
|---|---|
| PC10 | Cooling Pumps |
| PC20 | Thermal Valves |
| PC30 | Control Modules |

## 6. Accounting-policy memo

The accounting policy must be written before the full dataset is generated. This prevents the accounting answer from being invented after seeing the data.

### 6.1 Reporting basis

- The March management close uses policies designed to be consistent with the German Commercial Code where relevant.
- It is not an audited or statutory set of annual financial statements.
- HGB Section 252 requires, among other principles, balance continuity, individual valuation, prudence, period-based recognition of income and expenses, and consistency. See [HGB Section 252](https://www.gesetze-im-internet.de/hgb/__252.html).
- HGB Section 246 requires completeness and generally prohibits offsetting assets against liabilities or income against expenses. See [HGB Section 246](https://www.gesetze-im-internet.de/hgb/__246.html).

### 6.2 Financial-statement structure

- The balance sheet maps to the principal categories in HGB Section 266. See [HGB Section 266](https://www.gesetze-im-internet.de/hgb/__266.html).
- The P&L uses the total-cost method under HGB Section 275.
- The internal management P&L additionally presents gross margin and functional operating expenses using cost-centre and product mappings.
- Both views must reconcile to the same post-close trial balance.

HGB Section 275 permits either the total-cost or cost-of-sales format. See the [official HGB structure](https://www.gesetze-im-internet.de/hgb/BJNR002190897.html).

### 6.3 Currency

- EUR is the functional currency.
- Foreign-currency transactions are initially recorded using the transaction-date rate.
- Open foreign-currency receivables and payables are remeasured at the March 31 closing spot rate.
- HGB Section 256a requires foreign-currency assets and liabilities to be translated at the closing spot rate, subject to the section's maturity-related rules. See [HGB Section 256a](https://www.gesetze-im-internet.de/hgb/__256a.html).
- The chosen exchange-rate source and rate timestamp must be documented.

### 6.4 Prepaid expenses

- Payments made before March 31 for services relating to periods after March 31 are recognized as prepaid expenses.
- The schedule allocates expense by month unless the contract requires daily allocation.
- HGB Section 250 defines active prepaid expenses as payments before the reporting date that relate to a specified time after that date. See [HGB Section 250](https://www.gesetze-im-internet.de/hgb/__250.html).

### 6.5 Accrued expenses and payables

- A payable is used when the vendor, amount, and obligation are known and an invoice has been recorded.
- An accrued expense is used when service has been received before period end but the invoice has not yet been recorded.
- An accrual reverses on April 1 when the April invoice will be booked through the ordinary AP process.
- A GR/IR item is not automatically duplicated as an accrual. The goods-receipt and invoice-receipt flow is assessed first.

### 6.6 Provisions

- A provision is used for an uncertain liability or amount, not merely because an expense is expected.
- Warranty and bonus cases must have evidence of an obligation as of March 31.
- HGB Section 249 requires provisions for uncertain liabilities and impending losses from pending transactions and restricts other purposes. See [HGB Section 249](https://www.gesetze-im-internet.de/hgb/__249.html).
- The measurement uses the amount required under reasonable commercial judgment.
- The project will not include pensions or long-term discount-rate modeling.

### 6.7 Inventory

- Raw materials use weighted-average cost.
- Finished goods include direct material, direct labour, and allocated production overhead.
- Slow-moving and damaged items are assessed individually.
- Write-downs are based on supported recoverable value, not an arbitrary percentage.
- HGB Section 253 requires current assets to be written down when their relevant closing-date value is below carrying value. See [HGB Section 253](https://www.gesetze-im-internet.de/hgb/__253.html).

### 6.8 Fixed assets

- Fixed assets are capitalized when controlled and ready for intended use.
- Straight-line depreciation is used.
- Useful lives are defined in the asset master.
- Depreciation begins in the month the asset is placed into service under the project's documented monthly convention.
- This is a project policy assumption and will not be presented as a universal HGB rule.

### 6.9 Revenue cut-off

- Revenue is recognized when the documented delivery condition indicates that the material risks and control have passed to the customer.
- Invoice date alone is insufficient.
- Each cut-off case includes a sales order, delivery date, shipping term, invoice, and evidence of acceptance where relevant.

### 6.10 Materiality and control thresholds

These are fictional internal policy thresholds, not statutory HGB requirements.

| Control | Project threshold |
|---|---|
| Manual-journal review | Every journal above €25,000 |
| P&L variance commentary | Greater than €25,000 or 10% |
| Balance-sheet movement commentary | Greater than €50,000 |
| GR/IR aging escalation | Every item older than 90 days |
| Reconciliation difference | €0 unexplained |
| Calculation-to-journal tolerance | €0.01 |
| Management-pack rounding | Nearest €1,000, with source tie-out within €1 |

### 6.11 Period lock

- Ordinary March postings stop at the end of D+3.
- Late journals require a reason and approval status.
- The period is considered closed only after all critical reconciliations pass.
- A reopened period requires a separate log entry.

## 7. Technical architecture

The technical layer supports the accounting case; it is not the centerpiece.

### 7.1 Recommended stack

- Python for deterministic source-data generation and validation.
- CSV for immutable raw exports.
- Excel for close workpapers, reconciliations, trial balances, and statements.
- PowerPoint for the management pack.
- Git for version history.
- Markdown for policy, decisions, change log, AI disclosure, and interview preparation.
- Power BI only in Phase 2.

### 7.2 Reproducibility commands

The eventual implementation should support a small number of documented commands:

1. Validate syntax and imports.
2. Generate the 100-event smoke-test dataset.
3. Validate smoke-test accounting.
4. Generate the full pre-close dataset.
5. Build the Excel close workbook.
6. Run the full validation suite.
7. Build the management pack from the closed ledger.

The exact command names will be defined when the implementation repository is initialized. The full-data job must not be run until the smoke test passes.

### 7.3 Directory structure

    nordwerk-close/
    ├── README.md
    ├── IMPLEMENTATION_PLAN.md
    ├── pyproject.toml
    ├── src/
    │   └── close_lab/
    │       ├── __init__.py
    │       ├── config.py
    │       ├── chart_of_accounts.py
    │       ├── master_data.py
    │       ├── journal_engine.py
    │       ├── business_events.py
    │       ├── exception_cases.py
    │       ├── close_adjustments.py
    │       ├── reconciliations.py
    │       ├── financial_statements.py
    │       ├── management_reporting.py
    │       └── validation.py
    ├── config/
    │   ├── company.yml
    │   ├── accounting_policy.yml
    │   ├── close_calendar.yml
    │   └── report_mapping.yml
    ├── data/
    │   ├── raw/
    │   ├── evidence/
    │   ├── budget/
    │   ├── adjustments/
    │   ├── closed/
    │   └── qa_ground_truth/
    ├── output/
    │   ├── NordWerk_March_2026_Close.xlsx
    │   └── NordWerk_March_2026_Management_Pack.pptx
    ├── docs/
    │   ├── accounting_policy.md
    │   ├── data_dictionary.md
    │   ├── decision_log.md
    │   ├── formula_dictionary.md
    │   ├── change_log.md
    │   ├── ai_use_disclosure.md
    │   └── interview_questions.md
    └── tests/
        ├── test_journal_integrity.py
        ├── test_master_data.py
        ├── test_subledger_reconciliations.py
        ├── test_adjustments.py
        ├── test_statements.py
        └── test_reproducibility.py

Only the requested final outputs should be presented to recruiters. Intermediate files stay in the project repository for auditability.

## 8. Data model

### 8.1 Master tables

#### gl_account

| Field | Purpose |
|---|---|
| account_id | Unique G/L account |
| account_name | Plain-language account name |
| account_type | Asset, liability, equity, revenue, or expense |
| normal_balance | Debit or credit |
| open_item_managed | Whether open items are tracked |
| cost_center_required | Whether postings require a cost centre |
| fx_remeasurement | Whether open items are remeasured |
| hgb_bs_line | HGB balance-sheet mapping |
| hgb_pl_line | HGB P&L mapping |
| management_pl_line | Internal management P&L mapping |
| cash_flow_tag | Operating, investing, financing, or non-cash |

#### cost_center

- cost_center_id
- cost_center_name
- department
- manager_role
- profit_center_id
- valid_from
- valid_to

#### customer

- customer_id
- customer_name_synthetic
- country
- currency
- payment_terms_days
- credit_limit
- related_party_flag

#### vendor

- vendor_id
- vendor_name_synthetic
- country
- currency
- payment_terms_days
- vendor_category
- related_party_flag

#### material

- material_id
- material_description
- material_type
- unit_of_measure
- standard_cost
- weighted_average_cost
- product_family
- inventory_account
- write_down_group

#### fixed_asset

- asset_id
- asset_class
- description
- acquisition_date
- in_service_date
- acquisition_cost
- useful_life_months
- depreciation_method
- cost_center_id
- accumulated_depreciation_opening

### 8.2 Transaction tables

#### journal_header

- document_id
- company_code
- document_type
- document_date
- posting_date
- fiscal_year
- fiscal_period
- source_system
- source_reference
- reversal_document_id
- reversal_date
- status
- created_timestamp

#### journal_line

- document_id
- line_number
- gl_account_id
- debit_credit_indicator
- amount_transaction_currency
- transaction_currency
- exchange_rate
- amount_local_currency
- signed_local_amount
- cost_center_id
- profit_center_id
- customer_id
- vendor_id
- material_id
- asset_id
- purchase_order_id
- sales_order_id
- goods_receipt_id
- invoice_id
- assignment
- line_text

#### ar_open_item

- customer_id
- invoice_id
- invoice_date
- due_date
- currency
- original_amount
- open_amount
- local_open_amount
- clearing_document
- clearing_date
- days_overdue

#### ap_open_item

- vendor_id
- invoice_id
- invoice_date
- due_date
- currency
- original_amount
- open_amount
- local_open_amount
- purchase_order_id
- clearing_document
- clearing_date

#### bank_statement

- bank_line_id
- value_date
- booking_date
- amount
- currency
- counterparty
- reference
- matched_document_id
- matching_status

#### inventory_movement

- movement_id
- posting_date
- material_id
- movement_type
- quantity
- unit_cost
- value
- production_order_id
- delivery_id
- storage_location

#### grir_open_item

- purchase_order_id
- purchase_order_line
- goods_receipt_id
- goods_receipt_date
- invoice_id
- invoice_date
- quantity_received
- quantity_invoiced
- receipt_value
- invoice_value
- open_value
- age_days
- resolution_status

#### budget

- fiscal_period
- gl_account_id
- cost_center_id
- profit_center_id
- product_family
- budget_amount
- budget_volume

### 8.3 Close-control tables

#### close_task

- task_id
- task_name
- planned_day
- planned_start
- deadline
- owner_role
- reviewer_role
- predecessor_task_id
- critical_path_flag
- status
- evidence_reference
- completed_timestamp
- blocker
- escalation_status

#### manual_journal_register

- journal_id
- case_id
- rationale
- calculation_reference
- evidence_reference
- preparer
- preparation_date
- reviewer
- review_status
- posting_status
- reversal_required
- reversal_date
- late_journal_flag

#### reconciliation_register

- reconciliation_id
- account_id
- gl_balance
- independent_support_balance
- reconciling_items
- adjusted_support_balance
- unexplained_difference
- aging_bucket
- preparer
- reviewer
- status
- evidence_reference
- required_action
- expected_clear_date

## 9. Chart of accounts

Use a custom educational chart of accounts rather than copying DATEV or claiming SAP configuration.

| Range | Purpose | Example accounts |
|---|---|---|
| 100000–109999 | Cash | Main bank, payroll bank, cash clearing |
| 110000–119999 | Receivables | Trade AR, doubtful-debt allowance, unbilled receivable |
| 120000–129999 | Inventory | Raw materials, WIP, finished goods, inventory allowance |
| 130000–139999 | Prepayments and other current assets | Insurance prepaid, software prepaid, deposits |
| 140000–149999 | Tax control accounts | Input VAT, other tax receivables |
| 150000–159999 | Fixed assets | Machinery, IT equipment, accumulated depreciation |
| 200000–209999 | Payables | Trade AP |
| 210000–219999 | Accruals and GR/IR | Expense accruals, GR/IR |
| 220000–229999 | Payroll liabilities | Payroll payable, social-security payable, bonus accrual |
| 230000–239999 | Tax liabilities | Output VAT and payroll-related controls |
| 240000–249999 | Provisions | Warranty provision |
| 250000–259999 | Financing | Bank loans and interest payable |
| 300000–319999 | Equity | Share capital, retained earnings, current result |
| 400000–419999 | Revenue | Product revenue, sales returns, other operating income |
| 500000–519999 | Material and external production cost | Materials, external processing, inventory changes |
| 520000–539999 | Production and logistics | Direct labour, energy, freight, warehousing |
| 540000–559999 | Personnel | Salaries, employer contributions, bonus expense |
| 560000–579999 | Operating expenses | Rent, insurance, software, maintenance, professional fees |
| 580000–589999 | Depreciation and provisions | Depreciation, warranty expense, inventory write-down |
| 590000–599999 | Currency and other result | FX gains and losses |
| 700000–709999 | Finance result | Interest income and expense |
| 800000–809999 | Tax expense | Simplified income-tax expense if needed for reporting only |

Every account must have both an HGB statement mapping and an internal management mapping.

## 10. Business-event posting engine

The ledger must be built from economic events and double-entry rules, not by generating random debit and credit rows.

### 10.1 Core event patterns

#### Customer invoice

- Debit trade receivables.
- Credit product revenue.
- Credit output VAT for in-scope domestic transactions.

#### Customer receipt

- Debit bank.
- Credit trade receivables.
- Store invoice-clearing reference.

#### Purchase order

- No accounting entry.
- Creates a commitment and expected goods/service flow.

#### Goods receipt

- Debit inventory or expense-receipt account.
- Credit GR/IR.

#### Supplier invoice with purchase order

- Debit GR/IR.
- Debit input VAT where applicable.
- Credit trade payables.

#### Supplier payment

- Debit trade payables.
- Credit bank.

#### Service invoice without purchase order

- Debit the relevant expense and cost centre.
- Debit input VAT where applicable.
- Credit trade payables.

#### Payroll

- Debit salary and employer-cost accounts by cost centre.
- Credit payroll and social-security liabilities.
- Debit payroll liability and credit bank when paid.

#### Fixed-asset purchase

- Debit fixed asset.
- Debit input VAT where applicable.
- Credit trade payables.

#### Monthly depreciation

- Debit depreciation expense by cost centre.
- Credit accumulated depreciation by asset class.

#### Material issue to production

- Debit WIP.
- Credit raw-material inventory.

#### Finished-goods receipt

- Debit finished-goods inventory.
- Credit WIP.

#### Customer shipment

- Debit material expense or cost of sales in the management mapping.
- Credit finished-goods inventory.

### 10.2 Journal-engine requirements

- Every document has a unique document ID.
- Every document has at least two lines.
- Every document balances to exactly €0.00.
- Currency conversion is rounded under one documented rule.
- Subledger references are retained.
- Events cannot post to an unknown account, customer, vendor, material, asset, or cost centre.
- The same seed and configuration produce identical sorted raw outputs and hashes.

## 11. Fifteen seeded close cases

The amounts below are case-design targets. They must be confirmed during the deterministic smoke test and then frozen.

| Case | Pre-close issue | Evidence | Expected accounting response |
|---|---|---|---|
| C01 | €2,480 bank fee appears on the March bank statement but is absent from the GL | Bank statement line and fee notice | Record bank-fee expense and credit bank |
| C02 | €85,000 customer receipt is in the bank but unmatched in AR | Bank reference and customer remittance | Match receipt to customer open item; no invented revenue |
| C03 | €120,000 annual insurance paid January 1 was fully expensed | Policy covering Jan–Dec 2026 and payment | Reclass €90,000 to prepaid insurance at March 31 |
| C04 | €36,000 software contract paid February 1 covers 12 months and was fully expensed | Contract and payment | Retain only Feb–Mar expense; reclass remaining amount to prepaid software |
| C05 | March electricity consumption estimated at €48,600 has no invoice | Meter record, rate card, April invoice received later | Accrue March expense and reverse April 1 |
| C06 | €22,000 of March legal service is evidenced but not invoiced | Engagement letter and March time confirmation | Accrue professional-fee expense and reverse April 1 |
| C07 | March bonus obligation is not recorded | Headcount list, eligible salaries, YTD target attainment, approved plan | Calculate and record bonus provision/accrual under documented policy |
| C08 | Warranty provision is below the supported claim estimate | Trailing claims, eligible sales, known defect notice | Record the calculated increase, with sensitivity and management approval status |
| C09 | Open USD customer receivable remains at invoice-date EUR value | Customer invoice and approved March 31 FX rate | Remeasure receivable and record FX result |
| C10 | Open USD supplier payable remains at invoice-date EUR value | Supplier invoice and approved March 31 FX rate | Remeasure payable and record FX result |
| C11 | Three slow-moving inventory SKUs are carried above supported recoverable value | Inventory age, quantity, expected selling price, completion/selling cost | Record SKU-level write-down |
| C12 | Machine placed into service in March has no depreciation | Asset invoice, commissioning certificate, useful-life policy | Record March depreciation according to documented convention |
| C13 | €140,000 sales invoice posted March 30 relates to goods delivered April 2 | Sales order, invoice, delivery note, shipping term | Reverse premature March revenue and related cost/inventory effect |
| C14 | €180,000 goods delivered March 29 were invoiced April 2 | Sales order, delivery note, shipping term, April invoice | Record March unbilled revenue and related cost; reverse appropriately in April |
| C15 | €28,000 supplier invoice is posted to Sales rather than Engineering | Invoice, purchase request, cost-centre ownership | Reclass cost centre without changing total company expense |

### GR/IR judgment cases

Two additional items will be included in the GR/IR reconciliation but will not necessarily create journals:

- A €95,000 March 28 goods receipt with an April supplier invoice. The correct result may be to leave the item in GR/IR and avoid double accrual.
- A €62,000 GR/IR item older than 90 days arising from a quantity dispute. It must have an owner, cause, resolution, and expected clearing date before the reconciliation is complete.

### Ground-truth separation

- The user-facing pre-close case pack must not contain the expected answers.
- The qa_ground_truth folder holds the exception manifest and expected accounting outcomes.
- Automated tests compare detected cases with the ground-truth manifest.
- Each planted exception must be detected once.
- False positives must be explained or eliminated.

## 12. Source-to-report lineage

At least ten cases must show the complete chain:

> Source document → raw source table → accounting assessment → calculation → journal entry → G/L account → HGB line → management-report effect.

### Required lineage example

For the annual insurance case:

1. Source document: policy dated January 1, 2026, covering 12 months.
2. Payment: €120,000 on January 1.
3. Original posting: full €120,000 to insurance expense.
4. Accounting policy: expense recognized by service period.
5. March 31 calculation: three months consumed, nine months remaining.
6. Adjustment: debit prepaid insurance €90,000; credit insurance expense €90,000.
7. HGB mapping: prepaid expense under active Rechnungsabgrenzungsposten.
8. Management effect: March/YTD operating expense improves by €90,000 versus pre-close.
9. Reversal: none; monthly amortization schedule continues April–December.
10. Control: closing prepaid balance must equal the remaining contract schedule within €0.01.

The workbook needs a clickable case ID or source reference that supports this trace.

## 13. Six mandatory reconciliations

### 13.1 Bank

Reconcile:

> Bank statement balance  
> ± outstanding receipts/payments  
> ± bank-only items awaiting posting  
> = adjusted bank balance  
> compared with adjusted G/L bank balance

Required fields:

- Statement balance.
- G/L balance.
- Outstanding items.
- Bank fees.
- Unmatched receipts.
- Difference.
- Owner.
- Age.
- Action.
- Expected clear date.

### 13.2 Accounts receivable

- Sum customer open items.
- Tie to AR control account.
- Identify unapplied cash.
- Age by not due, 1–30, 31–60, 61–90, and over 90 days.
- Confirm foreign-currency remeasurement.
- Document doubtful-debt assessment.
- Do not post directly to the AR control account without a documented exception.

### 13.3 Accounts payable

- Sum vendor open items.
- Tie to AP control account.
- Review debit balances.
- Identify invoices blocked for mismatch.
- Confirm foreign-currency remeasurement.
- Review payments in transit.
- Do not duplicate GR/IR liabilities as AP accruals.

### 13.4 GR/IR

- Match receipt quantity and value to invoice quantity and value.
- Separate quantity differences, price differences, missing invoices, missing receipts, and old disputed items.
- Age all items.
- Escalate every item older than 90 days.
- Tie open-item report to the GR/IR G/L account.

SAP's GR/IR logic exists because goods receipts and invoice receipts frequently occur in different periods. The project must therefore demonstrate judgment, not mechanically post another accrual.

### 13.5 Inventory

- Roll opening quantity and value through receipts, issues, production, sales, and adjustments.
- Tie quantity-ledger value to the inventory G/L.
- Show raw material, WIP, and finished goods separately.
- Calculate slow-moving and NRV write-downs at SKU level.
- Preserve quantities; never repair a value mismatch with an unexplained plug.

### 13.6 Fixed assets

- Roll opening cost through additions and disposals.
- Roll accumulated depreciation through monthly expense.
- Tie asset cost and accumulated depreciation to the G/L.
- Confirm every March addition has an invoice and in-service date.
- Recalculate depreciation independently.

### Standard reconciliation template

Every reconciliation must contain:

- Account number and name.
- G/L closing balance.
- Independent supporting balance.
- Reconciling items.
- Adjusted supported balance.
- Unexplained difference.
- Aging.
- Preparer.
- Reviewer.
- Preparation date.
- Status.
- Evidence link.
- Required action.
- Expected clearing date.

No reconciliation may be marked complete while an unexplained difference remains.

## 14. D−3 to D+5 close calendar

| ID | Day | Task | Predecessor | Output | Critical |
|---|---|---|---|---|---|
| T01 | D−3 | Launch close calendar and assign responsibilities | None | Approved task list | Yes |
| T02 | D−3 | Send purchasing, shipping, payroll, and expense cut-off notice | T01 | Cut-off communication | Yes |
| T03 | D−2 | Confirm March goods movements and delivery documents | T02 | Operations confirmation | Yes |
| T04 | D−2 | Confirm services received but not invoiced | T02 | Accrual inputs | No |
| T05 | D−1 | Run preliminary trial balance and master-data checks | T01 | Preliminary TB | Yes |
| T06 | D0 | Freeze immutable March source extracts | T03, T05 | Raw-input hash manifest | Yes |
| T07 | D+1 | Run data-integrity validation | T06 | Validation report | Yes |
| T08 | D+1 | Prepare bank reconciliation | T07 | Bank workpaper | Yes |
| T09 | D+1 | Prepare AR reconciliation and aging | T07 | AR workpaper | Yes |
| T10 | D+1 | Review sales cut-off | T03, T09 | Revenue cut-off cases | Yes |
| T11 | D+1 | Prepare AP reconciliation | T07 | AP workpaper | Yes |
| T12 | D+2 | Prepare GR/IR reconciliation and aging | T11 | GR/IR workpaper | Yes |
| T13 | D+2 | Calculate service accruals | T04, T11 | Accrual workpaper | No |
| T14 | D+2 | Calculate prepayments | T07 | Prepayment schedule | No |
| T15 | D+2 | Reconcile inventory | T03, T07 | Inventory workpaper | Yes |
| T16 | D+2 | Calculate inventory write-down | T15 | Valuation workpaper | No |
| T17 | D+3 | Reconcile fixed assets and calculate depreciation | T07 | Asset workpaper | Yes |
| T18 | D+3 | Calculate bonus and warranty obligations | T07 | Provision workpapers | No |
| T19 | D+3 | Remeasure foreign-currency open items | T09, T11 | FX workpaper | No |
| T20 | D+3 | Review cost-centre coding | T07 | Reclassification list | No |
| T21 | D+3 | Submit adjusting journals before cut-off | T10–T20 | Journal register | Yes |
| T22 | D+4 | Validate and post approved adjustments | T21 | Post-close ledger | Yes |
| T23 | D+4 | Rerun all six reconciliations | T22 | Final reconciliations | Yes |
| T24 | D+4 | Prepare post-close trial balance and HGB mapping | T22 | Closed TB and mapping | Yes |
| T25 | D+4 | Perform analytical review against budget and prior month | T24 | Variance analysis | Yes |
| T26 | D+4 | Review late journals and unresolved issues | T23, T25 | Late-journal and issue log | Yes |
| T27 | D+4 | Simulate period lock | T26 | Lock record | Yes |
| T28 | D+5 | Prepare balance sheet, P&L, and management pack | T24, T25 | Reporting package | Yes |
| T29 | D+5 | Run final validation suite | T28 | Final validation report | Yes |
| T30 | D+5 | Complete controller certification and archive evidence | T29 | Signed project certification | Yes |

### Workflow statuses

- Not started.
- In progress.
- Prepared.
- Self-checked.
- Peer reviewed, only if a real peer review occurred.
- Blocked.
- Complete.

Do not create fictional reviewer approvals. Automated checks are labeled automated checks, not independent review.

## 15. Adjusting-journal workflow

Every manual journal must include:

- Case ID.
- Journal ID.
- Posting date.
- Account and cost centre.
- Debit and credit.
- Amount.
- Currency.
- Business explanation.
- Accounting-policy reference.
- Calculation reference.
- Evidence reference.
- Preparer.
- Self-check status.
- Actual peer reviewer, if one exists.
- Posting status.
- Reversal requirement and date.
- Late-journal flag.

### Journal controls

- Journal balances exactly.
- No journal uses an unknown master-data key.
- Calculation agrees to posting within €0.01.
- Reversal is generated where required.
- No unapproved journal enters the post-close ledger.
- Direct postings to AR/AP control accounts require explicit rationale.
- Every journal above €25,000 is separately highlighted for review.
- Every post-cut-off journal is recorded in the late-journal log.

## 16. Excel workbook design

The MVP workbook will be named:

**NordWerk_March_2026_Close.xlsx**

### Required tabs

1. **00_Read_Me**
   - Project disclosure.
   - Data scope.
   - Simulated D+5 wording.
   - Synthetic ERP disclaimer.
   - Navigation.

2. **01_Close_Status**
   - Task list.
   - Dependencies.
   - Status.
   - Critical-path flag.
   - Evidence link.

3. **02_Policy**
   - Accounting-policy summary.
   - Project thresholds.

4. **03_TB_Opening**
   - December 31, 2025 closing balances.

5. **04_TB_PreClose**
   - March 31, 2026 balances before adjustments.

6. **05_JE_Register**
   - All manual close journals and approvals.

7. **06_TB_PostClose**
   - Closed ledger balances.

8. **07_Bank_Recon**
9. **08_AR_Recon**
10. **09_AP_Recon**
11. **10_GRIR_Recon**
12. **11_Inventory_Recon**
13. **12_Fixed_Asset_Recon**
14. **13_Accruals**
15. **14_Prepayments**
16. **15_Provisions**
17. **16_FX**
18. **17_Cutoff**
19. **18_HGB_Mapping**
20. **19_HGB_Balance_Sheet**
21. **20_HGB_PL**
22. **21_Management_PL**
23. **22_Variance_Analysis**
24. **23_Issue_Log**
25. **24_Control_Checks**

### Workbook design rules

- Inputs, calculations, and outputs must be visually distinguishable.
- No hard-coded value may be hidden inside a formula.
- Source values must link to imported tables.
- Every adjustment must link to a case ID.
- All totals must use structured references or stable named ranges.
- Sign convention must be stated on every output.
- All monetary units must be labeled.
- Errors must be visible rather than suppressed.
- Checks should return explicit PASS/FAIL statuses.
- No management-report number may be manually typed over a linked result.

## 17. Management pack

The management pack is necessary so that the project supports FP&A and business-controller applications rather than only accounting roles.

### Page 1 — Executive summary

- Revenue.
- Gross margin.
- Operating result or EBITDA-like management measure.
- Cash.
- AR, AP, and inventory.
- Three most important variances.
- Three management actions.

### Page 2 — P&L actual versus budget and prior month

- March actual.
- March budget.
- Variance €.
- Variance %.
- February actual.
- YTD actual.
- YTD budget.
- Commentary for material movements.

### Page 3 — Revenue and gross-margin drivers

- Sales volume.
- Average selling price.
- Product-family mix.
- Material cost.
- Freight.
- Gross-margin bridge.

This is not intended to replace the later standard-cost project.

### Page 4 — Operating expenses by cost centre

- Actual versus budget.
- Personnel versus non-personnel.
- Largest over- and underspends.
- Coding correction effect.
- Owner and agreed action.

### Page 5 — Balance-sheet and working-capital risks

- AR aging.
- AP aging.
- GR/IR aging.
- Inventory aging.
- Bank-reconciliation status.
- DSO, DPO, and inventory days using documented definitions.

### Page 6 — Close quality and actions

- Critical tasks completed.
- Late journals.
- Open reconciling items.
- Manual journals.
- Largest close adjustments.
- April reversal exposure.
- Action owner and deadline.

### Commentary standard

Every material commentary must state:

1. Amount.
2. Driver.
3. Whether it is recurring or one-off.
4. Management action.
5. Owner.
6. Expected April or full-year effect.

Weak:

> Freight was above budget.

Strong:

> March freight was €74,000, €19,000 or 35% above budget, primarily because two customer orders used expedited delivery after a production delay. The variance is operational rather than price-driven. Logistics will require approval for premium freight above €5,000; expected April saving is €12,000.

## 18. Validation suite

### 18.1 Data integrity

- Every journal has a unique document ID.
- Every journal has at least two lines.
- Debits equal credits within €0.00 for every document.
- Total ledger debits equal total ledger credits within €0.00.
- All posting dates fall in a valid period.
- Every account exists in the chart of accounts.
- Every cost centre, vendor, customer, material, and asset key exists in its master.
- No duplicate primary keys exist.
- December 31 closing balances equal January 1 opening balances exactly.
- Raw source files remain immutable during the close.
- The same seed produces identical sorted data and file hashes.

### 18.2 Reconciliations

- AR control account equals the customer open-item listing within €0.00.
- AP control account equals the supplier open-item listing within €0.00.
- Fixed-asset cost and accumulated-depreciation accounts equal the asset register within €0.00.
- Inventory quantity-ledger value equals the inventory G/L within €0.00 after approved adjustments.
- GR/IR account equals the GR/IR open-item report within €0.00.
- Adjusted bank-statement balance equals adjusted bank G/L within €0.00.
- Every reconciling item has an owner, cause, amount, and expected clearing date.
- Every GR/IR item older than 90 days has a documented resolution.
- No reconciliation is complete with an unexplained difference.

### 18.3 Close adjustments

- Prepaid balances agree to contract schedules within €0.01.
- Depreciation agrees to the asset schedule within €0.01 per asset.
- FX remeasurement agrees to the approved closing rate within €0.01 per open item.
- Inventory write-down agrees to the SKU-level valuation within €0.01.
- Bonus and warranty calculations agree to approved assumptions within €0.01.
- Service accruals have evidence of March service delivery.
- Each planted exception is detected exactly once.
- No unexplained false positive remains.
- April reversals correctly unwind temporary March adjustments.

### 18.4 Statements and reporting

- Post-close trial balance balances within €0.00.
- Assets equal liabilities plus equity within €0.00.
- March result agrees between the trial balance, P&L, and equity roll-forward within €0.00.
- HGB and management P&L views reconcile to the same ledger result.
- Management-pack totals agree to the closed ledger within €1 before presentation rounding.
- Actual and budget versions cannot be mixed.
- All units and signs are consistent.
- Every material commentary has amount, driver, recurrence, action, owner, and expected effect.

### 18.5 Workflow and reproducibility

- A fresh user can reproduce the project from raw inputs using the documented run process.
- The validation suite passes before reports are released.
- D+5 sign-off is blocked while a critical task is open.
- The package clearly distinguishes simulated dates from actual elapsed performance.
- README discloses synthetic data and lack of live SAP.
- The documented end-to-end run completes without manual repair.

### 18.6 Negative tests

The validation suite must prove it can fail:

1. Remove one journal line: document-balance test fails.
2. Duplicate a document ID: primary-key test fails.
3. Replace one valid account with an unknown account: referential-integrity test fails.
4. Change an FX rate: remeasurement test fails.
5. Alter one inventory movement: inventory reconciliation fails.
6. Delete a fixed-asset addition: asset roll-forward fails.
7. Post a journal without evidence: journal-control test fails.
8. Mark a critical task incomplete: final sign-off fails.
9. Mix budget and actual versions: report-version test fails.
10. Type over a management-pack source number: output tie-out fails.

## 19. Implementation stages

### Stage 0 — Freeze the case specification

**Estimated effort:** 3–4 hours

Tasks:

- Finalize company profile.
- Freeze the MVP boundary.
- Confirm terminology and disclaimers.
- Define deliverables.
- Define acceptance criteria.
- Create the decision log.

Gate:

- No code or workbook build begins until scope and claims are fixed.

### Stage 1 — Write accounting policies

**Estimated effort:** 6–8 hours

Tasks:

- Write the accounting-policy memo.
- Define HGB mappings.
- Define cut-off policy.
- Define accrual, provision, prepayment, inventory, FX, and asset policies.
- Define thresholds and reversal rules.
- Research unclear accounting treatments before implementation.

Gate:

- Every close case has a policy reference.

### Stage 2 — Create chart of accounts and master data

**Estimated effort:** 6–8 hours

Tasks:

- Build account master.
- Build cost-centre and profit-centre masters.
- Build customer and vendor masters.
- Build material and fixed-asset masters.
- Add HGB and management-report mappings.
- Run duplicate and referential-integrity checks.

Gate:

- Every master table passes validation before transactions are generated.

### Stage 3 — Build the 100-event smoke test

**Estimated effort:** 8–10 hours

Tasks:

- Implement journal header and line schemas.
- Implement core double-entry event patterns.
- Generate a bounded 100-event dataset.
- Confirm each document balances.
- Confirm AR, AP, inventory, bank, and fixed-asset movements.
- Write deterministic tests.
- Verify output writing and Excel import on the small sample.

Gate:

- Data access, calculation logic, output writing, and basic workbook rendering all succeed on the smoke test.
- Do not generate the full dataset before this gate passes.

### Stage 4 — Generate opening balances and three months of operations

**Estimated effort:** 8–12 hours

Tasks:

- Create December 31, 2025 opening trial balance.
- Generate January and February closed activity.
- Generate March ordinary activity.
- Create budget data.
- Freeze the March pre-close raw-data hashes.
- Confirm opening/closing continuity.

Gate:

- January opening equals December closing.
- Every month balances.
- Subledgers reconcile before seeded March exceptions.

### Stage 5 — Seed and verify close exceptions

**Estimated effort:** 6–8 hours

Tasks:

- Implement the 15 close cases.
- Produce source evidence.
- Create the ground-truth exception manifest.
- Confirm the pre-close dataset contains each intended issue exactly once.
- Confirm the cases do not accidentally create unrelated differences.

Gate:

- Expected issue count and amount are frozen.
- False positives are zero or fully documented.

### Stage 6 — Build close workpapers and reconciliations

**Estimated effort:** 12–16 hours

Tasks:

- Build standard reconciliation template.
- Complete bank, AR, AP, GR/IR, inventory, and fixed-asset reconciliations.
- Build accrual, prepaid, provision, FX, cut-off, and depreciation workpapers.
- Link evidence.
- Create manual journals and reversal instructions.

Gate:

- All six mandatory reconciliations tie after approved adjustments.

### Stage 7 — Build closed trial balance and financial statements

**Estimated effort:** 6–8 hours

Tasks:

- Apply approved journals.
- Produce post-close ledger and trial balance.
- Map to HGB balance sheet and P&L.
- Produce management P&L.
- Reconcile statutory-format and management views.

Gate:

- Balance sheet balances.
- P&L and equity roll-forward agree.
- HGB and management results reconcile.

### Stage 8 — Build variance analysis and management pack

**Estimated effort:** 8–12 hours

Tasks:

- Calculate actual-versus-budget and prior-month variances.
- Identify material drivers.
- Write management commentary.
- Assign actions and owners.
- Build the six-page pack.
- Verify every reported value against the closed ledger.

Gate:

- Every material variance has decision-ready commentary.
- Management-pack totals agree to the ledger.

### Stage 9 — Run adversarial QA

**Estimated effort:** 6–8 hours

Tasks:

- Run all positive and negative tests.
- Trace ten cases end to end.
- Review disclosures.
- Check workbook formulas.
- Inspect every delivered chart and table.
- Ask an accounting-qualified reviewer to challenge at least the judgmental cases if available.
- Correct documented issues once; do not hide them.

Gate:

- Full validation suite passes.
- No unexplained differences remain.

### Stage 10 — Recruiter packaging and interview rehearsal

**Estimated effort:** 4–6 hours

Tasks:

- Finalize README.
- Finalize AI-use disclosure.
- Create a formula dictionary.
- Create a seven-minute walkthrough.
- Prepare interview questions and answers.
- Write one CV bullet and one project description.

Gate:

- Mann can trace one case from evidence to report without notes.

### Total estimated effort

- MVP: approximately 70–95 focused hours.
- At 8 hours per week: approximately 9–12 weeks.
- At 12 hours per week: approximately 6–8 weeks.
- Phase 2: approximately 25–40 additional hours.

The work should not be compressed by removing reconciliations or tests. If time is constrained, reduce data volume and presentation polish first.

## 20. Authorship and AI-use policy

### Public disclosure

> AI was used for research support, code scaffolding, and adversarial review. I defined the accounting policies, designed the test cases, validated the posting logic, reconciled the outputs, and can reproduce and explain every material adjustment.

### Evidence of authorship

- Incremental Git commits.
- Accounting decision log.
- Formula dictionary.
- Change log.
- Tests written before final reporting.
- Written explanation of every close case.
- Recorded walkthrough.
- Interview question file.
- Actual peer-review evidence only when peer review occurs.

### What AI may do

- Scaffold deterministic data-generation code.
- Suggest test cases.
- Draft documentation.
- Review formulas.
- Challenge explanations.
- Help automate repetitive workbook construction.

### What AI may not decide without human validation

- Whether an obligation qualifies as a provision.
- Whether revenue belongs in March.
- Whether inventory is impaired.
- Which evidence supports service delivery.
- Whether a journal should be approved.
- Whether a reconciliation is complete.
- What management action should be recommended.

## 21. Interview-defense questions

Mann must be able to answer these without opening notes:

1. Did you actually use SAP?
2. Why do you call this a March management close rather than an HGB statutory close?
3. What is the difference between a payable, an accrual, a provision, and a prepaid expense?
4. Why does the March 28 goods receipt remain in GR/IR?
5. Why did you not post another accrual for that goods receipt?
6. What evidence proves the legal service was delivered before March 31?
7. Why does the April invoice not create another March expense?
8. What happens to the March accrual on April 1?
9. How was the warranty estimate selected?
10. Which HGB principle supports the inventory write-down?
11. Which FX rate was used and why?
12. Why did depreciation begin in March?
13. How do you know the synthetic data did not simply encode the intended answer?
14. Which controls are preventive and which are detective?
15. What would be automated in a real company?
16. What still requires human judgment?
17. What changed between the pre-close and post-close P&L?
18. Which adjustment had the largest operating-result effect?
19. What should the operations manager do next?
20. What did AI produce and what did you validate personally?
21. Trace one transaction from source evidence to the management pack.
22. Why were VAT filing, tax, IFRS, and consolidation excluded?
23. If only one day were available, which tasks would be prioritized?
24. How could AR equal the G/L and still be wrong?
25. Would the pack be released with an unresolved €20,000 bank difference?
26. How would a reviewer challenge the warranty provision?
27. What is the difference between a reconciling item and an adjusting journal?
28. Why is a cost-centre reclassification important if total company expense does not change?
29. What would cause flash results to differ from final results?
30. Which project limitation matters most?

The strongest demonstration starts with one source-to-report trace, not the management dashboard.

## 22. Final recruiter-facing outputs

### README opening

> This portfolio project simulates the March 2026 D+5 management close of a fictional German automotive-components manufacturer. It uses an HGB-based local ledger and ERP-shaped synthetic exports. The project includes six balance-sheet reconciliations, documented adjusting entries, a controlled close calendar, HGB-formatted financial statements, and an actual-versus-budget management pack. No SAP instance or proprietary company data was used.

### CV bullet

> Built and validated a simulated D+5 management close for a German manufacturing case, reconciling bank, AR, AP, GR/IR, inventory, and fixed assets; documented close adjustments for cut-off, accruals, prepayments, provisions, FX, and depreciation; and translated the closed ledger into HGB-formatted statements and management variance commentary.

### Short interview description

> I built the project to prove the routine finance discipline behind my more advanced modeling work. The core was not the dashboard. It was taking an immutable pre-close ledger, finding and documenting close issues, producing supported journals, reconciling six balance-sheet areas to zero unexplained difference, and then explaining the closed result against budget.

## 23. Definition of done

The MVP is complete only when all of the following are true:

- Scope and claims match this plan.
- Accounting policies are written before final data generation.
- The 100-event end-to-end smoke test succeeds.
- The full ledger is event-generated and deterministic.
- Every journal balances.
- Opening balances roll correctly.
- Fifteen seeded cases are present and independently testable.
- Every material adjustment has evidence and policy support.
- Six mandatory reconciliations have zero unexplained difference.
- Post-close trial balance balances.
- Assets equal liabilities plus equity.
- P&L agrees to the equity roll-forward.
- HGB-format and management views reconcile.
- Management-pack values tie to the ledger.
- Commentary explains amount, driver, recurrence, action, owner, and expected effect.
- All positive tests pass.
- All negative tests fail in the intended way.
- Raw data remain immutable.
- A fresh run reproduces the result.
- Synthetic data and lack of live SAP are clearly disclosed.
- AI use is clearly disclosed.
- Mann can answer the interview-defense questions and perform an end-to-end transaction trace.
- The documented end-to-end run command succeeds without manual repair.

## 24. First implementation session

The next session should complete only the following bounded tasks:

1. Create the project directory.
2. Copy this implementation plan into the project as IMPLEMENTATION_PLAN.md.
3. Create README.md with the scope and disclosure.
4. Create accounting_policy.md version 0.1.
5. Create the chart-of-accounts schema.
6. Create the master-data schemas.
7. Define the journal header and journal line schemas.
8. Implement five event types:
   - Customer invoice.
   - Customer receipt.
   - Supplier invoice.
   - Supplier payment.
   - Fixed-asset acquisition.
9. Generate no more than 100 events.
10. Test per-document balance, master-data validity, AR/AP linkage, and deterministic regeneration.
11. Export the sample to CSV.
12. Import the sample into a minimal Excel workbook and visually inspect it.

The first session is successful only if that bounded sample works end to end. The full ledger must not be generated until then.

## 25. Research references

### German accounting

- [HGB Section 246 — Completeness and prohibition of offsetting](https://www.gesetze-im-internet.de/hgb/__246.html)
- [HGB Section 249 — Provisions](https://www.gesetze-im-internet.de/hgb/__249.html)
- [HGB Section 250 — Prepaid and deferred items](https://www.gesetze-im-internet.de/hgb/__250.html)
- [HGB Section 252 — General valuation principles](https://www.gesetze-im-internet.de/hgb/__252.html)
- [HGB Section 253 — Initial and subsequent measurement](https://www.gesetze-im-internet.de/hgb/__253.html)
- [HGB Section 256a — Foreign-currency translation](https://www.gesetze-im-internet.de/hgb/__256a.html)
- [HGB Section 266 — Balance-sheet structure](https://www.gesetze-im-internet.de/hgb/__266.html)
- [Complete official HGB](https://www.gesetze-im-internet.de/hgb/)

### Close process

- [SAP Month-End Closing](https://help.sap.com/doc/8353d7531a4d424de10000000a174cb4/700_SFIN3E%20006/en-US/0a15d353c6244308e10000000a174cb4.html)
- [SAP Accounting and Financial Close](https://help.sap.com/docs/s4hana-cloud-best-practices/accounting-and-financial-close-j58-rs/purpose?locale=en-US)
- [SAP Closing Cockpit](https://help.sap.com/docs/SAP_BUSINESS_BYDESIGN/2754875d2d2a403f95e58a41a9c7d6de/2c2c9e53722d1014b132b89394723f2b.html)
- [SAP General Ledger Closing Procedures](https://help.sap.com/docs/SUPPORT_CONTENT/fiaccounting/3361880855.html)
- [SAP Process Closing Tasks](https://help.sap.com/docs/advanced-financial-closing/administration/ae51205499f549558eadd8a2c190d1b5.html)

### Real-company HGB/IFRS distinction

- [adidas AG 2025 HGB financial statements](https://report.adidas-group.com/2025/en/group-management-report-financial-review/business-performance/financial-statements-and-management-report-of-adidas-ag.html)
- [adidas Group 2025 IFRS basis](https://report.adidas-group.com/2025/en/consolidated-financial-statements/notes/general-information/general.html)

The adidas example demonstrates the distinction the project must preserve: the German parent prepares its individual statements under HGB, while the consolidated group statements use IFRS as adopted by the EU.

### Controller role

- [ICV Controller Mission Statement](https://icv-controlling.com/en/vision-mission/)

The ICV frames controllers as both management partners and guardians of financial integrity. This project deliberately tests both roles.

