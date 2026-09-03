# Smoke-test data dictionary

The five event schemas and the generated journal schemas are implemented in
`src/close_lab/business_events.py` and `src/close_lab/journal_engine.py`.

| Table | Grain | Key control |
|---|---|---|
| `gl_account` | one row per account | unique `account_id`; every account has HGB and management mappings |
| `customer` | one row per customer | unique `customer_id` |
| `vendor` | one row per vendor | unique `vendor_id` |
| `fixed_asset` | one row per asset | unique `asset_id` |
| `journal_header` | one row per accounting document | unique `document_id` |
| `journal_line` | one row per document line | unique `(document_id, line_number)` |
| `ar_open_item` | one row per customer invoice | invoice and receipt references are validated |
| `ap_open_item` | one row per vendor invoice | invoice and payment references are validated |

All monetary values are stored as decimal values, serialized with two decimal
places in CSV, and use a signed local amount convention: debits are positive
and credits are negative.
