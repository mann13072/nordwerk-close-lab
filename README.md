# NordWerk D+5 Month-End Close Lab

This portfolio project simulates the March 2026 D+5 management close of
NordWerk Cooling Systems GmbH, a fictional German automotive-components
manufacturer. It uses an HGB-based local ledger and ERP-shaped synthetic
exports. No SAP instance or proprietary company data was used.

## Current scope: first implementation session

The repository currently implements the bounded smoke test from the
implementation plan:

- deterministic master data and chart-of-accounts schemas;
- five economic event types: customer invoice, customer receipt, supplier
  invoice, supplier payment, and fixed-asset acquisition;
- exactly 100 typed events, producing balanced journal documents;
- AR/AP linkage and open-item derivation;
- CSV export under `data/raw/smoke_test/`;
- validation tests for journal integrity, master-data validity, subledger
  linkage, and deterministic regeneration.

The full March close, seeded exceptions, reconciliations, statements, and
management pack are intentionally not generated until this smoke-test gate
passes.

## Reproduce the smoke test

From this directory:

```powershell
$env:PYTHONPATH = (Join-Path (Get-Location) 'src')
python -m close_lab.cli syntax-check
python -m close_lab.cli generate-smoke
python -m close_lab.cli validate-smoke
python -m pytest -q
```

An editable install is optional. The commands above avoid requiring a
package-build temporary directory, which may be restricted in managed
environments.

`generate-smoke` writes immutable-style sample exports to
`data/raw/smoke_test/` and prints their SHA-256 hashes. The generator uses
seed `20260331`; re-running it with the same seed must reproduce the same
sorted CSV contents and hashes.

## Accounting and authorship disclosure

This is a simulated March management close, not a statutory annual close and
not evidence of live SAP experience. AI was used for research support, code
scaffolding, and adversarial review. The accounting policies, event cases,
validation rules, and output checks must be reviewed and validated by the
project author before recruiter-facing use.

See `IMPLEMENTATION_PLAN.md` for the complete target scope and
`docs/accounting_policy.md` for the initial policy memo.
