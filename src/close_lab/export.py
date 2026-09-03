"""CSV export and canonical hash manifest for the smoke-test outputs."""

from __future__ import annotations

from dataclasses import asdict
from pathlib import Path

from .chart_of_accounts import export_chart_of_accounts
from .master_data import MasterData, export_master_data
from .projections import build_ap_open_items, build_ar_open_items, build_asset_additions, projection_rows
from .business_events import CustomerInvoice, CustomerReceipt, Event, FixedAssetAcquisition, SupplierInvoice, SupplierPayment
from .journal_engine import PostingResult, header_rows, line_rows
from .serialization import sha256_file, write_csv


def event_rows(events: tuple[Event, ...]) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for event in events:
        if isinstance(event, (CustomerInvoice, SupplierInvoice, FixedAssetAcquisition)):
            amount = event.net_amount
            counterparty_id = event.customer_id if isinstance(event, CustomerInvoice) else event.vendor_id
            source_reference = event.invoice_id
        else:
            amount = event.amount
            counterparty_id = event.customer_id if isinstance(event, CustomerReceipt) else event.vendor_id
            source_reference = event.invoice_id
        rows.append({
            "event_id": event.event_id,
            "event_type": event.event_type,
            "document_id": event.document_id,
            "posting_date": event.posting_date,
            "counterparty_id": counterparty_id,
            "invoice_id": getattr(event, "invoice_id"),
            "amount": amount,
            "currency": event.currency,
            "source_reference": source_reference,
        })
    return rows


def export_smoke(
    directory: Path,
    events: tuple[Event, ...],
    results: tuple[PostingResult, ...],
    master_data: MasterData,
) -> dict[str, str]:
    directory.mkdir(parents=True, exist_ok=True)
    hashes: dict[str, str] = {}
    files = (
        ("events.csv", ("event_id", "event_type", "document_id", "posting_date", "counterparty_id", "invoice_id", "amount", "currency", "source_reference"), event_rows(events)),
        ("journal_headers.csv", tuple(header_rows(results)[0].keys()), header_rows(results)),
        ("journal_lines.csv", tuple(line_rows(results)[0].keys()), line_rows(results)),
        ("ar_open_items.csv", tuple(projection_rows(build_ar_open_items(events))[0].keys()), projection_rows(build_ar_open_items(events))),
        ("ap_open_items.csv", tuple(projection_rows(build_ap_open_items(events))[0].keys()), projection_rows(build_ap_open_items(events))),
        ("asset_additions.csv", tuple(projection_rows(build_asset_additions(events))[0].keys()), projection_rows(build_asset_additions(events))),
    )
    for filename, columns, rows in files:
        hashes[filename] = write_csv(directory / filename, columns, rows)

    master_dir = directory / "master"
    export_chart_of_accounts(master_dir / "gl_accounts.csv")
    export_master_data(master_dir, master_data)
    for path in sorted(master_dir.glob("*.csv")):
        hashes[str(path.relative_to(directory)).replace("\\", "/")] = sha256_file(path)

    manifest_rows = [{"file": name, "sha256": digest} for name, digest in sorted(hashes.items())]
    hashes["hash_manifest.csv"] = write_csv(directory / "hash_manifest.csv", ("file", "sha256"), manifest_rows)
    return hashes
