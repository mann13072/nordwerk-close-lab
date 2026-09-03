"""Subledger projections derived from the posted event stream."""

from __future__ import annotations

from dataclasses import asdict, dataclass
from datetime import date
from decimal import Decimal
from typing import Iterable

from .business_events import CustomerInvoice, CustomerReceipt, Event, FixedAssetAcquisition, SupplierInvoice, SupplierPayment
from .config import money
from .journal_engine import event_gross
from .master_data import MasterData


@dataclass(frozen=True)
class AROpenItem:
    customer_id: str
    invoice_id: str
    invoice_date: date
    due_date: date
    currency: str
    original_amount: Decimal
    cleared_amount: Decimal
    open_amount: Decimal
    local_open_amount: Decimal
    clearing_document: str | None
    clearing_date: date | None
    days_overdue: int


@dataclass(frozen=True)
class APOpenItem:
    vendor_id: str
    invoice_id: str
    invoice_date: date
    due_date: date
    currency: str
    original_amount: Decimal
    cleared_amount: Decimal
    open_amount: Decimal
    local_open_amount: Decimal
    purchase_order_id: str | None
    clearing_document: str | None
    clearing_date: date | None


@dataclass(frozen=True)
class AssetAddition:
    asset_id: str
    invoice_id: str
    vendor_id: str
    acquisition_date: date
    net_amount: Decimal
    local_amount: Decimal
    cost_center_id: str


def build_ar_open_items(events: Iterable[Event], master_data: MasterData | None = None, as_of: date = date(2026, 3, 31)) -> tuple[AROpenItem, ...]:
    invoices = [event for event in events if isinstance(event, CustomerInvoice)]
    receipts = [event for event in events if isinstance(event, CustomerReceipt)]
    terms = {row.customer_id: row.payment_terms_days for row in master_data.customers} if master_data else {}
    by_invoice: dict[str, list[CustomerReceipt]] = {}
    for receipt in receipts:
        by_invoice.setdefault(receipt.invoice_id, []).append(receipt)
    rows: list[AROpenItem] = []
    for invoice in invoices:
        linked = sorted(by_invoice.get(invoice.invoice_id, []), key=lambda item: item.posting_date)
        original = event_gross(invoice)
        cleared = money(sum((item.amount for item in linked), Decimal("0")))
        open_amount = money(original - cleared)
        last = linked[-1] if linked else None
        due_days = terms.get(invoice.customer_id, 30)
        rows.append(
            AROpenItem(invoice.customer_id, invoice.invoice_id, invoice.document_date,
                       date.fromordinal(invoice.document_date.toordinal() + due_days), invoice.currency,
                       original, cleared, open_amount, money(open_amount * invoice.exchange_rate),
                       last.document_id if last else None, last.posting_date if last else None,
                       max(0, (as_of - invoice.document_date).days - 30)),
        )
    return tuple(sorted(rows, key=lambda row: row.invoice_id))


def build_ap_open_items(events: Iterable[Event], master_data: MasterData | None = None, as_of: date = date(2026, 3, 31)) -> tuple[APOpenItem, ...]:
    invoices = [event for event in events if isinstance(event, (SupplierInvoice, FixedAssetAcquisition))]
    payments = [event for event in events if isinstance(event, SupplierPayment)]
    terms = {row.vendor_id: row.payment_terms_days for row in master_data.vendors} if master_data else {}
    by_invoice: dict[str, list[SupplierPayment]] = {}
    for payment in payments:
        by_invoice.setdefault(payment.invoice_id, []).append(payment)
    rows: list[APOpenItem] = []
    for invoice in invoices:
        linked = sorted(by_invoice.get(invoice.invoice_id, []), key=lambda item: item.posting_date)
        original = event_gross(invoice)
        cleared = money(sum((item.amount for item in linked), Decimal("0")))
        open_amount = money(original - cleared)
        last = linked[-1] if linked else None
        due_days = terms.get(invoice.vendor_id, 30)
        due_date = date.fromordinal(invoice.document_date.toordinal() + due_days)
        rows.append(
            APOpenItem(invoice.vendor_id, invoice.invoice_id, invoice.document_date, due_date, invoice.currency,
                       original, cleared, open_amount, money(open_amount * invoice.exchange_rate),
                       getattr(invoice, "purchase_order_id", None), last.document_id if last else None,
                       last.posting_date if last else None),
        )
    return tuple(sorted(rows, key=lambda row: row.invoice_id))


def build_asset_additions(events: Iterable[Event]) -> tuple[AssetAddition, ...]:
    return tuple(
        AssetAddition(event.asset_id, event.invoice_id, event.vendor_id, event.document_date,
                      event.net_amount, money(event.net_amount * event.exchange_rate), event.cost_center_id)
        for event in events
        if isinstance(event, FixedAssetAcquisition)
    )


def projection_rows(items: Iterable[object]) -> list[dict[str, object]]:
    return [asdict(item) for item in items]
