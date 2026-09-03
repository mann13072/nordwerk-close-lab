"""Positive accounting controls for the bounded smoke-test scenario."""

from __future__ import annotations

from collections import Counter
from decimal import Decimal
from typing import Iterable

from .business_events import CustomerInvoice, CustomerReceipt, Event, FixedAssetAcquisition, SupplierInvoice, SupplierPayment
from .chart_of_accounts import GLAccount
from .config import money
from .journal_engine import JournalLine, PostingResult, event_gross
from .master_data import MasterData
from .projections import build_ap_open_items, build_ar_open_items


def _duplicate(values: Iterable[object]) -> list[object]:
    counts = Counter(values)
    return sorted(value for value, count in counts.items() if count > 1)


def validate_master_data(master_data: MasterData) -> list[str]:
    issues: list[str] = []
    for name, rows, key in (
        ("cost_centers", master_data.cost_centers, "cost_center_id"),
        ("customers", master_data.customers, "customer_id"),
        ("vendors", master_data.vendors, "vendor_id"),
        ("materials", master_data.materials, "material_id"),
        ("fixed_assets", master_data.fixed_assets, "asset_id"),
    ):
        duplicates = _duplicate(getattr(row, key) for row in rows)
        if duplicates:
            issues.append(f"duplicate {name} keys: {duplicates}")
    return issues


def validate_journal_integrity(
    results: Iterable[PostingResult],
    accounts: Iterable[GLAccount],
    master_data: MasterData,
) -> list[str]:
    results = tuple(results)
    account_map = {account.account_id: account for account in accounts}
    customer_ids = {row.customer_id for row in master_data.customers}
    vendor_ids = {row.vendor_id for row in master_data.vendors}
    cost_center_ids = {row.cost_center_id for row in master_data.cost_centers}
    issues: list[str] = []
    document_ids = [result.header.document_id for result in results]
    if duplicates := _duplicate(document_ids):
        issues.append(f"duplicate document IDs: {duplicates}")

    for result in results:
        lines = result.lines
        if len(lines) < 2:
            issues.append(f"document {result.header.document_id} has fewer than two lines")
        if money(sum((line.signed_local_amount for line in lines), Decimal("0"))) != Decimal("0.00"):
            issues.append(f"document {result.header.document_id} is not balanced")
        line_keys = [(line.document_id, line.line_number) for line in lines]
        if duplicates := _duplicate(line_keys):
            issues.append(f"duplicate line keys in {result.header.document_id}: {duplicates}")
        for line in lines:
            account = account_map.get(line.gl_account_id)
            if account is None:
                issues.append(f"unknown account {line.gl_account_id} in {line.document_id}")
                continue
            if line.debit_credit_indicator not in {"D", "C"}:
                issues.append(f"invalid debit/credit indicator in {line.document_id}/{line.line_number}")
            expected_signed = line.amount_local_currency if line.debit_credit_indicator == "D" else money(-line.amount_local_currency)
            if line.signed_local_amount != expected_signed:
                issues.append(f"signed amount mismatch in {line.document_id}/{line.line_number}")
            if line.amount_transaction_currency <= 0 or line.amount_local_currency <= 0:
                issues.append(f"non-positive amount in {line.document_id}/{line.line_number}")
            if line.customer_id and line.customer_id not in customer_ids:
                issues.append(f"unknown customer {line.customer_id} in {line.document_id}")
            if line.vendor_id and line.vendor_id not in vendor_ids:
                issues.append(f"unknown vendor {line.vendor_id} in {line.document_id}")
            if line.cost_center_id and line.cost_center_id not in cost_center_ids:
                issues.append(f"unknown cost centre {line.cost_center_id} in {line.document_id}")
            if account.cost_center_required and not line.cost_center_id:
                issues.append(f"missing cost centre for {line.gl_account_id} in {line.document_id}")
            if account.account_type == "revenue" and not line.profit_center_id:
                issues.append(f"missing profit centre for revenue in {line.document_id}")
    return issues


def validate_subledger_linkage(events: Iterable[Event], results: Iterable[PostingResult], master_data: MasterData) -> list[str]:
    events = tuple(events)
    results = tuple(results)
    issues: list[str] = []
    event_ids = [event.event_id for event in events]
    if duplicates := _duplicate(event_ids):
        issues.append(f"duplicate event IDs: {duplicates}")
    if len(events) != len(results):
        issues.append(f"event/result count mismatch: {len(events)} vs {len(results)}")
    for event, result in zip(events, results):
        if event.event_id != result.event_id:
            issues.append(f"event/result mismatch: {event.event_id} vs {result.event_id}")
    customers = {row.customer_id for row in master_data.customers}
    vendors = {row.vendor_id for row in master_data.vendors}
    assets = {row.asset_id for row in master_data.fixed_assets}
    invoices = {event.invoice_id for event in events if isinstance(event, (CustomerInvoice, SupplierInvoice, FixedAssetAcquisition))}
    for event in events:
        if isinstance(event, (CustomerInvoice, CustomerReceipt)) and event.customer_id not in customers:
            issues.append(f"invalid customer linkage: {event.event_id}")
        if isinstance(event, (SupplierInvoice, SupplierPayment, FixedAssetAcquisition)) and event.vendor_id not in vendors:
            issues.append(f"invalid vendor linkage: {event.event_id}")
        if isinstance(event, FixedAssetAcquisition) and event.asset_id not in assets:
            issues.append(f"invalid asset linkage: {event.event_id}")
        if isinstance(event, (CustomerReceipt, SupplierPayment)) and event.invoice_id not in invoices:
            issues.append(f"invalid clearing reference: {event.event_id}")

    ar_items = build_ar_open_items(events)
    ap_items = build_ap_open_items(events)
    if len(ar_items) != sum(isinstance(event, CustomerInvoice) for event in events):
        issues.append("AR open-item count does not equal customer invoice count")
    if len(ap_items) != sum(isinstance(event, (SupplierInvoice, FixedAssetAcquisition)) for event in events):
        issues.append("AP open-item count does not equal supplier invoice plus asset invoice count")
    return issues


def validate_control_totals(events: Iterable[Event], results: Iterable[PostingResult]) -> list[str]:
    events = tuple(events)
    results = tuple(results)
    lines: tuple[JournalLine, ...] = tuple(line for result in results for line in result.lines)
    issues: list[str] = []
    ar_items = build_ar_open_items(events)
    ap_items = build_ap_open_items(events)
    ar_gl = money(sum((line.signed_local_amount for line in lines if line.gl_account_id == "110000"), Decimal("0")))
    ar_support = money(sum((item.local_open_amount for item in ar_items), Decimal("0")))
    if ar_gl != ar_support:
        issues.append(f"AR control mismatch: GL {ar_gl} vs support {ar_support}")
    ap_gl = money(sum((line.signed_local_amount for line in lines if line.gl_account_id == "200000"), Decimal("0")))
    ap_support = money(sum((item.local_open_amount for item in ap_items), Decimal("0")))
    if money(-ap_gl) != ap_support:
        issues.append(f"AP control mismatch: GL {-ap_gl} vs support {ap_support}")

    bank_gl = money(sum((line.signed_local_amount for line in lines if line.gl_account_id == "100000"), Decimal("0")))
    receipt_total = money(sum((event.amount for event in events if isinstance(event, CustomerReceipt)), Decimal("0")))
    payment_total = money(sum((event.amount for event in events if isinstance(event, SupplierPayment)), Decimal("0")))
    if bank_gl != money(receipt_total - payment_total):
        issues.append(f"bank movement mismatch: GL {bank_gl} vs event movement {receipt_total - payment_total}")

    output_vat_gl = money(-sum((line.signed_local_amount for line in lines if line.gl_account_id == "230000"), Decimal("0")))
    expected_output_vat = money(sum((event_gross(event) - event.net_amount for event in events if isinstance(event, CustomerInvoice)), Decimal("0")))
    if output_vat_gl != expected_output_vat:
        issues.append(f"output VAT mismatch: GL {output_vat_gl} vs calculated {expected_output_vat}")
    input_vat_gl = money(sum((line.signed_local_amount for line in lines if line.gl_account_id == "140000"), Decimal("0")))
    expected_input_vat = money(sum((event_gross(event) - event.net_amount for event in events if isinstance(event, (SupplierInvoice, FixedAssetAcquisition))), Decimal("0")))
    if input_vat_gl != expected_input_vat:
        issues.append(f"input VAT mismatch: GL {input_vat_gl} vs calculated {expected_input_vat}")
    asset_gl = money(sum((line.signed_local_amount for line in lines if line.gl_account_id == "150000"), Decimal("0")))
    expected_assets = money(sum((event.net_amount * event.exchange_rate for event in events if isinstance(event, FixedAssetAcquisition)), Decimal("0")))
    if asset_gl != expected_assets:
        issues.append(f"fixed-asset movement mismatch: GL {asset_gl} vs calculated {expected_assets}")
    return issues


def validate_smoke(events: Iterable[Event], results: Iterable[PostingResult], accounts: Iterable[GLAccount], master_data: MasterData) -> list[str]:
    issues = validate_master_data(master_data)
    issues.extend(validate_journal_integrity(results, accounts, master_data))
    issues.extend(validate_subledger_linkage(events, results, master_data))
    issues.extend(validate_control_totals(events, results))
    return issues
