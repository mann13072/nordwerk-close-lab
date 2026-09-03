"""Double-entry posting rules for the five smoke-test economic events."""

from __future__ import annotations

from dataclasses import asdict, dataclass
from datetime import date
from decimal import Decimal
from typing import Iterable

from .business_events import (
    CustomerInvoice,
    CustomerReceipt,
    Event,
    FixedAssetAcquisition,
    SupplierInvoice,
    SupplierPayment,
)
from .chart_of_accounts import GLAccount, account_map
from .config import (
    COMPANY_CODE,
    DOMESTIC_COUNTRY,
    DOMESTIC_VAT_RATE,
    FUNCTIONAL_CURRENCY,
    SCENARIO_TIMESTAMP,
    local_amount,
    money,
)
from .master_data import MasterData


@dataclass(frozen=True)
class JournalHeader:
    document_id: str
    company_code: str
    document_type: str
    document_date: date
    posting_date: date
    fiscal_year: int
    fiscal_period: int
    source_system: str
    source_reference: str
    reversal_document_id: str | None
    reversal_date: date | None
    status: str
    created_timestamp: str


@dataclass(frozen=True)
class JournalLine:
    document_id: str
    line_number: int
    gl_account_id: str
    debit_credit_indicator: str
    amount_transaction_currency: Decimal
    transaction_currency: str
    exchange_rate: Decimal
    amount_local_currency: Decimal
    signed_local_amount: Decimal
    cost_center_id: str | None = None
    profit_center_id: str | None = None
    customer_id: str | None = None
    vendor_id: str | None = None
    material_id: str | None = None
    asset_id: str | None = None
    purchase_order_id: str | None = None
    sales_order_id: str | None = None
    goods_receipt_id: str | None = None
    invoice_id: str | None = None
    assignment: str | None = None
    line_text: str = ""


@dataclass(frozen=True)
class PostingResult:
    event_id: str
    event_type: str
    header: JournalHeader
    lines: tuple[JournalLine, ...]


class PostingError(ValueError):
    """Raised when an economic event cannot be posted safely."""


def _vat(net_amount: Decimal, country: str) -> Decimal:
    return money(net_amount * DOMESTIC_VAT_RATE) if country == DOMESTIC_COUNTRY else money(0)


def event_gross(event: CustomerInvoice | SupplierInvoice | FixedAssetAcquisition) -> Decimal:
    return money(event.net_amount + _vat(event.net_amount, event.country))


def _header(event: Event, document_type: str, source_reference: str) -> JournalHeader:
    posting_date = event.posting_date
    document_date = event.document_date if hasattr(event, "document_date") else event.value_date
    return JournalHeader(
        document_id=event.document_id,
        company_code=COMPANY_CODE,
        document_type=document_type,
        document_date=document_date,
        posting_date=posting_date,
        fiscal_year=posting_date.year,
        fiscal_period=posting_date.month,
        source_system="SYNTH_ERP",
        source_reference=source_reference,
        reversal_document_id=None,
        reversal_date=None,
        status="posted",
        created_timestamp=SCENARIO_TIMESTAMP,
    )


def _line(
    document_id: str,
    line_number: int,
    account_id: str,
    indicator: str,
    transaction_amount: Decimal,
    currency: str,
    exchange_rate: Decimal,
    *,
    local_override: Decimal | None = None,
    **references: str | None,
) -> JournalLine:
    transaction_amount = money(transaction_amount)
    amount_local = money(local_override if local_override is not None else local_amount(transaction_amount, exchange_rate))
    signed = amount_local if indicator == "D" else money(-amount_local)
    return JournalLine(
        document_id=document_id,
        line_number=line_number,
        gl_account_id=account_id,
        debit_credit_indicator=indicator,
        amount_transaction_currency=transaction_amount,
        transaction_currency=currency,
        exchange_rate=exchange_rate,
        amount_local_currency=amount_local,
        signed_local_amount=signed,
        **references,
    )


def _validate_common(event: Event, master_data: MasterData, accounts: dict[str, GLAccount]) -> None:
    if not event.event_id or not event.document_id:
        raise PostingError("event_id and document_id are required")
    if event.currency != FUNCTIONAL_CURRENCY:
        raise PostingError(f"Smoke test only supports {FUNCTIONAL_CURRENCY} transactions")
    if event.exchange_rate <= 0:
        raise PostingError("exchange_rate must be positive")
    if event.posting_date.year != 2026 or not 1 <= event.posting_date.month <= 3:
        raise PostingError("smoke-test posting dates must fall in Q1 2026")
    if isinstance(event, (CustomerInvoice, SupplierInvoice, FixedAssetAcquisition)):
        if event.net_amount <= 0:
            raise PostingError("net_amount must be positive")
    else:
        if event.amount <= 0:
            raise PostingError("clearing amount must be positive")

    if isinstance(event, (CustomerInvoice, CustomerReceipt)):
        customer_map = {row.customer_id: row for row in master_data.customers}
        customer_ids = set(customer_map)
        if event.customer_id not in customer_ids:
            raise PostingError(f"unknown customer_id: {event.customer_id}")
        if isinstance(event, CustomerInvoice) and event.country != customer_map[event.customer_id].country:
            raise PostingError(f"customer invoice country does not match master: {event.customer_id}")
        if isinstance(event, CustomerInvoice) and event.profit_center_id not in {"PC10", "PC20", "PC30"}:
            raise PostingError(f"unknown profit_center_id: {event.profit_center_id}")
    if isinstance(event, (SupplierInvoice, SupplierPayment, FixedAssetAcquisition)):
        vendor_map = {row.vendor_id: row for row in master_data.vendors}
        vendor_ids = set(vendor_map)
        if event.vendor_id not in vendor_ids:
            raise PostingError(f"unknown vendor_id: {event.vendor_id}")
        if isinstance(event, (SupplierInvoice, FixedAssetAcquisition)) and event.country != vendor_map[event.vendor_id].country:
            raise PostingError(f"supplier invoice country does not match master: {event.vendor_id}")
    if isinstance(event, FixedAssetAcquisition):
        asset_ids = {row.asset_id for row in master_data.fixed_assets}
        if event.asset_id not in asset_ids:
            raise PostingError(f"unknown asset_id: {event.asset_id}")

    cost_center_ids = {row.cost_center_id for row in master_data.cost_centers}
    if isinstance(event, (SupplierInvoice, FixedAssetAcquisition)) and event.cost_center_id not in cost_center_ids:
        raise PostingError(f"unknown cost_center_id: {event.cost_center_id}")
    required_accounts = {"100000", "110000", "140000", "150000", "200000", "230000", "400000"}
    if not required_accounts.issubset(accounts):
        missing = sorted(required_accounts - set(accounts))
        raise PostingError(f"chart of accounts is missing required accounts: {missing}")
    if isinstance(event, SupplierInvoice) and event.expense_account_id not in accounts:
        raise PostingError(f"unknown expense account_id: {event.expense_account_id}")


def _validate_references(events: tuple[Event, ...]) -> None:
    customer_invoices = {event.invoice_id: event for event in events if isinstance(event, CustomerInvoice)}
    supplier_invoices = {event.invoice_id: event for event in events if isinstance(event, SupplierInvoice)}
    asset_invoices = {event.invoice_id: event for event in events if isinstance(event, FixedAssetAcquisition)}
    if len(customer_invoices) != sum(isinstance(event, CustomerInvoice) for event in events):
        raise PostingError("duplicate customer invoice_id")
    if len(supplier_invoices) != sum(isinstance(event, SupplierInvoice) for event in events):
        raise PostingError("duplicate supplier invoice_id")
    all_invoice_ids = set(customer_invoices) | set(supplier_invoices) | set(asset_invoices)
    cleared: dict[str, Decimal] = {}
    for event in events:
        if isinstance(event, CustomerReceipt):
            invoice = customer_invoices.get(event.invoice_id)
            if invoice is None:
                raise PostingError(f"receipt {event.event_id} references unknown customer invoice {event.invoice_id}")
            if event.customer_id != invoice.customer_id or event.currency != invoice.currency:
                raise PostingError(f"receipt {event.event_id} does not match its customer invoice")
            if event.posting_date < invoice.posting_date:
                raise PostingError(f"receipt {event.event_id} predates its invoice")
            original = event_gross(invoice)
            cleared[event.invoice_id] = money(cleared.get(event.invoice_id, Decimal("0")) + event.amount)
            if cleared[event.invoice_id] > original:
                raise PostingError(f"receipt clearing exceeds invoice balance: {event.invoice_id}")
        if isinstance(event, SupplierPayment):
            invoice = supplier_invoices.get(event.invoice_id)
            if invoice is None:
                raise PostingError(f"payment {event.event_id} references unknown supplier invoice {event.invoice_id}")
            if event.vendor_id != invoice.vendor_id or event.currency != invoice.currency:
                raise PostingError(f"payment {event.event_id} does not match its supplier invoice")
            if event.posting_date < invoice.posting_date:
                raise PostingError(f"payment {event.event_id} predates its invoice")
            original = event_gross(invoice)
            cleared[event.invoice_id] = money(cleared.get(event.invoice_id, Decimal("0")) + event.amount)
            if cleared[event.invoice_id] > original:
                raise PostingError(f"payment clearing exceeds invoice balance: {event.invoice_id}")
        if isinstance(event, FixedAssetAcquisition) and event.invoice_id in all_invoice_ids:
            # Asset invoices use a separate namespace in the smoke scenario;
            # this catches accidental double-posting if that convention breaks.
            if sum(
                isinstance(candidate, FixedAssetAcquisition) and candidate.invoice_id == event.invoice_id
                for candidate in events
            ) > 1:
                raise PostingError(f"duplicate fixed-asset invoice_id: {event.invoice_id}")


def post_event(event: Event, master_data: MasterData, accounts: Iterable[GLAccount] | None = None) -> PostingResult:
    """Post one already-linked economic event into one balanced document."""

    account_lookup = account_map(accounts)
    _validate_common(event, master_data, account_lookup)

    if isinstance(event, CustomerInvoice):
        vat = _vat(event.net_amount, event.country)
        local_net = local_amount(event.net_amount, event.exchange_rate)
        local_vat = local_amount(vat, event.exchange_rate)
        lines = (
            _line(event.document_id, 1, "110000", "D", event.net_amount + vat, event.currency, event.exchange_rate,
                  local_override=local_net + local_vat, customer_id=event.customer_id, sales_order_id=event.sales_order_id,
                  invoice_id=event.invoice_id, assignment=event.invoice_id, line_text="Trade receivable"),
            _line(event.document_id, 2, "400000", "C", event.net_amount, event.currency, event.exchange_rate,
                  local_override=local_net, customer_id=event.customer_id, profit_center_id=event.profit_center_id,
                  sales_order_id=event.sales_order_id, invoice_id=event.invoice_id, assignment=event.invoice_id,
                  line_text="Product revenue"),
        )
        if vat:
            lines += (_line(event.document_id, 3, "230000", "C", vat, event.currency, event.exchange_rate,
                             local_override=local_vat, customer_id=event.customer_id, invoice_id=event.invoice_id,
                             assignment=event.invoice_id, line_text="Output VAT"),)
        return PostingResult(event.event_id, event.event_type, _header(event, "DR", event.invoice_id), lines)

    if isinstance(event, CustomerReceipt):
        lines = (
            _line(event.document_id, 1, "100000", "D", event.amount, event.currency, event.exchange_rate,
                  customer_id=event.customer_id, invoice_id=event.invoice_id, assignment=event.invoice_id,
                  line_text="Customer receipt to bank"),
            _line(event.document_id, 2, "110000", "C", event.amount, event.currency, event.exchange_rate,
                  customer_id=event.customer_id, invoice_id=event.invoice_id, assignment=event.invoice_id,
                  line_text="Clear customer receivable"),
        )
        return PostingResult(event.event_id, event.event_type, _header(event, "DZ", event.receipt_id), lines)

    if isinstance(event, SupplierInvoice):
        vat = _vat(event.net_amount, event.country)
        local_net = local_amount(event.net_amount, event.exchange_rate)
        local_vat = local_amount(vat, event.exchange_rate)
        lines = (
            _line(event.document_id, 1, event.expense_account_id, "D", event.net_amount, event.currency, event.exchange_rate,
                  local_override=local_net, vendor_id=event.vendor_id, cost_center_id=event.cost_center_id,
                  invoice_id=event.invoice_id, assignment=event.invoice_id, line_text="External service expense"),
        )
        if vat:
            lines += (_line(event.document_id, 2, "140000", "D", vat, event.currency, event.exchange_rate,
                             local_override=local_vat, vendor_id=event.vendor_id, invoice_id=event.invoice_id,
                             assignment=event.invoice_id, line_text="Input VAT"),)
        lines += (_line(event.document_id, len(lines) + 1, "200000", "C", event.net_amount + vat, event.currency, event.exchange_rate,
                        local_override=local_net + local_vat, vendor_id=event.vendor_id, invoice_id=event.invoice_id,
                        assignment=event.invoice_id, line_text="Trade payable"),)
        return PostingResult(event.event_id, event.event_type, _header(event, "KR", event.invoice_id), lines)

    if isinstance(event, SupplierPayment):
        lines = (
            _line(event.document_id, 1, "200000", "D", event.amount, event.currency, event.exchange_rate,
                  vendor_id=event.vendor_id, invoice_id=event.invoice_id, assignment=event.invoice_id,
                  line_text="Clear supplier payable"),
            _line(event.document_id, 2, "100000", "C", event.amount, event.currency, event.exchange_rate,
                  vendor_id=event.vendor_id, invoice_id=event.invoice_id, assignment=event.invoice_id,
                  line_text="Supplier payment from bank"),
        )
        return PostingResult(event.event_id, event.event_type, _header(event, "KZ", event.payment_id), lines)

    if isinstance(event, FixedAssetAcquisition):
        vat = _vat(event.net_amount, event.country)
        local_net = local_amount(event.net_amount, event.exchange_rate)
        local_vat = local_amount(vat, event.exchange_rate)
        lines = (
            _line(event.document_id, 1, "150000", "D", event.net_amount, event.currency, event.exchange_rate,
                  local_override=local_net, vendor_id=event.vendor_id, asset_id=event.asset_id,
                  cost_center_id=event.cost_center_id, purchase_order_id=event.purchase_order_id,
                  invoice_id=event.invoice_id, assignment=event.asset_id, line_text="Machinery acquisition"),
            _line(event.document_id, 2, "140000", "D", vat, event.currency, event.exchange_rate,
                  local_override=local_vat, vendor_id=event.vendor_id, asset_id=event.asset_id,
                  invoice_id=event.invoice_id, assignment=event.asset_id, line_text="Input VAT on asset"),
            _line(event.document_id, 3, "200000", "C", event.net_amount + vat, event.currency, event.exchange_rate,
                  local_override=local_net + local_vat, vendor_id=event.vendor_id, asset_id=event.asset_id,
                  invoice_id=event.invoice_id, assignment=event.asset_id, line_text="Asset trade payable"),
        )
        return PostingResult(event.event_id, event.event_type, _header(event, "AA", event.invoice_id), lines)

    raise PostingError(f"unsupported event type: {type(event).__name__}")


def post_events(events: Iterable[Event], master_data: MasterData, accounts: Iterable[GLAccount] | None = None) -> tuple[PostingResult, ...]:
    event_tuple = tuple(events)
    if len({event.event_id for event in event_tuple}) != len(event_tuple):
        raise PostingError("duplicate event_id")
    if len({event.document_id for event in event_tuple}) != len(event_tuple):
        raise PostingError("duplicate document_id")
    account_lookup = account_map(accounts)
    for event in event_tuple:
        _validate_common(event, master_data, account_lookup)
    _validate_references(event_tuple)
    results = tuple(post_event(event, master_data, account_lookup.values()) for event in event_tuple)
    return results


def header_rows(results: Iterable[PostingResult]) -> list[dict[str, object]]:
    return [asdict(result.header) for result in results]


def line_rows(results: Iterable[PostingResult]) -> list[dict[str, object]]:
    return [asdict(line) for result in results for line in result.lines]
