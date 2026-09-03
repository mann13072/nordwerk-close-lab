# Decision log

| Date | Decision | Reason |
|---|---|---|
| 2026-09-03 | Implement the bounded first-session smoke test before the full close | The plan explicitly gates full-data generation on a passing end-to-end sample. |
| 2026-09-03 | Use typed economic events, not randomly generated journal rows | This preserves accounting relationships and makes the ledger explainable. |
| 2026-09-03 | Keep SAP language to “ERP-shaped synthetic exports” | No live SAP instance is being claimed. |
