# Case study — C03 annual insurance prepaid expense

## Executive summary

During the simulated March 2026 management close, NordWerk’s insurance
expense appeared EUR 90,000 above the year-to-date budget. The cause was not an
operating overspend. An annual EUR 120,000 insurance premium paid on January 2
had been expensed in full, even though the policy provides coverage through
December 31.

The close review reclassified the nine unconsumed months, EUR 90,000, to an
active prepaid expense. Year-to-date insurance expense therefore becomes EUR
30,000, matching the three months consumed through March.

## Business facts

NordWerk Cooling Systems GmbH is a fictional Leipzig-based manufacturer. The
company paid its annual property and production-liability insurance premium on
January 2, 2026. The policy names NordWerk as the insured party and states a
coverage period from January 1 through December 31, 2026. The payment date is
January 2, which does not change the coverage start date. The case assumes no
recoverable VAT on the insurance premium; no input-VAT journal is posted.

The pre-close ledger contained this posting:

```text
Dr 570100 Insurance expense       EUR 120,000
Cr 100000 Main bank               EUR 120,000
```

The bank payment is valid. The error is the period classification of the
expense, not the cash movement. January and February are treated as already
closed, so the March entry is a catch-up correction in the March management
close.

## Accounting assessment

The policy supports a specified future service period. At March 31, three of
the twelve coverage months have elapsed:

```text
Monthly insurance expense = EUR 120,000 / 12 = EUR 10,000
Consumed Jan–Mar          = EUR 10,000 x 3 = EUR 30,000
Unconsumed Apr–Dec        = EUR 10,000 x 9 = EUR 90,000
```

The EUR 90,000 relates to periods after March 31 and is reclassified to active
prepaid expenses. The case uses the HGB presentation line
`C. Rechnungsabgrenzungsposten` for the balance-sheet mapping.

## Proposed March close adjustment

```text
Dr 130100 Aktiver Rechnungsabgrenzungsposten (ARAP)       EUR 90,000
Cr 570100 Insurance expense               EUR 90,000
```

The journal balances to zero and requires manual review because it exceeds the
fictional EUR 25,000 review threshold.

## Closing result

| Measure | Pre-close | Adjustment | Post-close |
|---|---:|---:|---:|
| YTD insurance expense | EUR 120,000 | (EUR 90,000) | EUR 30,000 |
| Prepaid insurance asset | EUR 0 | EUR 90,000 | EUR 90,000 |
| Unexplained reconciliation difference | n/a | n/a | EUR 0 |

The adjustment does not reverse on April 1. It is a balance-sheet
reclassification supported by a continuing schedule. From April through
December, EUR 10,000 is recognized each month:

```text
Dr 570100 Insurance expense       EUR 10,000
Cr 130100 Prepaid insurance       EUR 10,000
```

## Management conclusion

The apparent EUR 90,000 insurance overspend is a timing and classification
error. It should not trigger an operating-cost reduction action. The control
action is to add an annual-prepayment review to the monthly close checklist and
retain the coverage schedule with the journal evidence.

## Realism and limitation

This case is deliberately bounded. It demonstrates source-to-report lineage,
period recognition, evidence, journal review, reconciliation, and management
interpretation. It does not claim that the insurance contract was reviewed by
an external auditor, that a live ERP was used, or that this is a statutory
annual close.
