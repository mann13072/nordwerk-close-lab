# Accounting Policy Memo — version 0.1

## Purpose and basis

The smoke test supports a simulated March 2026 management close for one
fictional German GmbH. The ledger follows an HGB-based educational policy; it
is not an audited or statutory annual financial statement.

The implementation applies double-entry bookkeeping, completeness, period
recognition, individual valuation, and consistent classification principles.
The complete legal references are retained in `IMPLEMENTATION_PLAN.md` and
will be researched again before judgmental close cases are implemented.

## Currency

EUR is the functional and reporting currency. Transaction amounts are stored
in transaction currency and converted to EUR at the event exchange rate. EUR
amounts are rounded to two decimals using decimal half-up rounding. The
smoke test is primarily EUR-denominated but retains the exchange-rate field so
foreign-currency cases can be added without changing the journal schema.

## VAT and invoice posting

Domestic German sales and purchases use a fictional 19% VAT rate for the
smoke-test posting engine. Customer invoices post gross trade receivables,
net product revenue, and output VAT. Supplier invoices post the expense or
asset net amount, input VAT, and gross trade payables. Non-domestic sample
counterparties are supported with zero VAT in the event model.

## Receipts, payments, and linkage

Customer receipts debit the bank and credit trade receivables while retaining
the invoice-clearing reference. Supplier payments debit trade payables and
credit the bank while retaining the invoice reference. Open-item listings are
derived from the typed events rather than generated independently.

## Fixed assets

Fixed-asset acquisitions debit the asset account, debit input VAT where
applicable, and credit trade payables. Depreciation is out of scope for this
smoke-test gate and will be added with a documented monthly convention before
the full close is generated.

## Control thresholds

The project uses an exact EUR 0.00 unexplained-difference tolerance for
document and ledger balancing. Amounts above EUR 25,000 are candidates for
manual-journal review in the full close. These are fictional internal project
thresholds, not statutory requirements.

## Disclosure

The data is synthetic and ERP-shaped. No live SAP instance, proprietary data,
or employment experience is claimed. Human review remains required for
provisions, revenue cut-off, inventory valuation, journal approval, and
reconciliation completion.
