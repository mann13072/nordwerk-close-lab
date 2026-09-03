"""Typed economic events used to construct the smoke-test ledger."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from decimal import Decimal
from typing import Union

from .config import FUNCTIONAL_CURRENCY, money, smoke_date


@dataclass(frozen=True)
class CustomerInvoice:
    event_id: str
    document_id: str
    invoice_id: str
    customer_id: str
    document_date: date
    posting_date: date
    net_amount: Decimal
    currency: str
    exchange_rate: Decimal
    country: str
    profit_center_id: str
    sales_order_id: str
    description: str

    event_type: str = "customer_invoice"


@dataclass(frozen=True)
class CustomerReceipt:
    event_id: str
    document_id: str
    receipt_id: str
    invoice_id: str
    customer_id: str
    value_date: date
    posting_date: date
    amount: Decimal
    currency: str
    exchange_rate: Decimal
    bank_reference: str

    event_type: str = "customer_receipt"


@dataclass(frozen=True)
class SupplierInvoice:
    event_id: str
    document_id: str
    invoice_id: str
    vendor_id: str
    document_date: date
    posting_date: date
    net_amount: Decimal
    currency: str
    exchange_rate: Decimal
    country: str
    expense_account_id: str
    cost_center_id: str
    purchase_order_id: str | None
    description: str

    event_type: str = "supplier_invoice"


@dataclass(frozen=True)
class SupplierPayment:
    event_id: str
    document_id: str
    payment_id: str
    invoice_id: str
    vendor_id: str
    value_date: date
    posting_date: date
    amount: Decimal
    currency: str
    exchange_rate: Decimal
    bank_reference: str

    event_type: str = "supplier_payment"


@dataclass(frozen=True)
class FixedAssetAcquisition:
    event_id: str
    document_id: str
    invoice_id: str
    vendor_id: str
    asset_id: str
    document_date: date
    posting_date: date
    net_amount: Decimal
    currency: str
    exchange_rate: Decimal
    country: str
    cost_center_id: str
    purchase_order_id: str
    description: str

    event_type: str = "fixed_asset_acquisition"


Event = Union[CustomerInvoice, CustomerReceipt, SupplierInvoice, SupplierPayment, FixedAssetAcquisition]


def _currency_rate(currency: str) -> Decimal:
    # The smoke test keeps all transactions in EUR. The engine remains ready
    # for later FX cases without introducing an untested spot-rate assumption.
    if currency != FUNCTIONAL_CURRENCY:
        raise ValueError(f"Unsupported smoke-test currency: {currency}")
    return Decimal("1.00")


def _smoke_customer_country(customer_id: str) -> str:
    return ("DE", "DE", "DE", "NL", "FR")[(int(customer_id[1:]) - 1) % 5]


def _smoke_vendor_country(vendor_id: str) -> str:
    return ("DE", "DE", "AT", "PL", "NL")[(int(vendor_id[1:]) - 1) % 5]


def generate_smoke_events(event_count: int = 60, seed: int = 20260331) -> tuple[Event, ...]:
    """Generate a bounded, linked scenario from economic events.

    The first implementation session intentionally uses the advisor-reviewed
    60-event design: 20 invoices, 15 receipts, 15 supplier invoices, 8
    supplier payments, and 2 fixed-asset acquisitions.
    """

    if event_count != 60:
        raise ValueError("The smoke scenario is fixed at 60 events; full data is deferred until this gate passes.")

    # Use a local deterministic generator. It varies values without making
    # journal rows random or severing the invoice/clearing relationships.
    import random

    rng = random.Random(seed)
    events: list[Event] = []

    for i in range(1, 21):
        amount = money(70_000 + rng.randint(0, 25_000))
        # The smoke gate is EUR-only with domestic VAT, as agreed for this
        # bounded session. Non-domestic master data remains available for the
        # later FX/VAT phases.
        customer_id = f"C{((i - 1) % 3) + 1:03d}"
        customer_country = _smoke_customer_country(customer_id)
        posting = smoke_date((i * 3) % 80)
        events.append(
            CustomerInvoice(
                event_id=f"EV-CI-{i:04d}",
                document_id=f"CI-202603-{i:04d}",
                invoice_id=f"CI-202603-{i:04d}",
                customer_id=customer_id,
                document_date=posting,
                posting_date=posting,
                net_amount=amount,
                currency=FUNCTIONAL_CURRENCY,
                exchange_rate=_currency_rate(FUNCTIONAL_CURRENCY),
                country="DE",
                profit_center_id=("PC10", "PC20", "PC30")[(i - 1) % 3],
                sales_order_id=f"SO-202603-{i:04d}",
                description="Synthetic finished-goods sale",
            )
        )

    for i in range(1, 16):
        invoice = events[i - 1]
        assert isinstance(invoice, CustomerInvoice)
        gross = money(invoice.net_amount * (Decimal("1.19") if invoice.country == "DE" else Decimal("1.00")))
        amount = gross if i <= 12 else money(gross * Decimal("0.50"))
        posting = smoke_date(min(84, (i * 3) % 80 + 2))
        events.append(
            CustomerReceipt(
                event_id=f"EV-CR-{i:04d}",
                document_id=f"CR-202603-{i:04d}",
                receipt_id=f"CR-202603-{i:04d}",
                invoice_id=invoice.invoice_id,
                customer_id=invoice.customer_id,
                value_date=posting,
                posting_date=posting,
                amount=amount,
                currency=invoice.currency,
                exchange_rate=invoice.exchange_rate,
                bank_reference=f"BANK-CR-{i:04d}",
            )
        )

    for i in range(1, 16):
        amount = money(18_000 + rng.randint(0, 12_000))
        vendor_id = f"V{((i - 1) % 2) + 1:03d}"
        vendor_country = _smoke_vendor_country(vendor_id)
        posting = smoke_date((i * 4 + 1) % 78)
        events.append(
            SupplierInvoice(
                event_id=f"EV-SI-{i:04d}",
                document_id=f"SI-202603-{i:04d}",
                invoice_id=f"SI-202603-{i:04d}",
                vendor_id=vendor_id,
                document_date=posting,
                posting_date=posting,
                net_amount=amount,
                currency=FUNCTIONAL_CURRENCY,
                exchange_rate=_currency_rate(FUNCTIONAL_CURRENCY),
                country="DE",
                expense_account_id="570000",
                cost_center_id=("CC100", "CC110", "CC120", "CC130", "CC200", "CC300", "CC400", "CC500")[(i - 1) % 8],
                purchase_order_id=None,
                description="Synthetic non-PO external service",
            )
        )

    for i in range(1, 9):
        invoice = events[35 + i - 1]
        assert isinstance(invoice, SupplierInvoice)
        gross = money(invoice.net_amount * (Decimal("1.19") if invoice.country == "DE" else Decimal("1.00")))
        amount = gross if i <= 6 else money(gross * Decimal("0.50"))
        posting = smoke_date(min(84, (i * 4 + 1) % 78 + 3))
        events.append(
            SupplierPayment(
                event_id=f"EV-SP-{i:04d}",
                document_id=f"SP-202603-{i:04d}",
                payment_id=f"SP-202603-{i:04d}",
                invoice_id=invoice.invoice_id,
                vendor_id=invoice.vendor_id,
                value_date=posting,
                posting_date=posting,
                amount=amount,
                currency=invoice.currency,
                exchange_rate=invoice.exchange_rate,
                bank_reference=f"BANK-SP-{i:04d}",
            )
        )

    for i in range(1, 3):
        asset_id = f"FA{i:03d}"
        posting = smoke_date(55 + i * 5)
        events.append(
            FixedAssetAcquisition(
                event_id=f"EV-FA-{i:04d}",
                document_id=f"FA-202603-{i:04d}",
                invoice_id=f"FA-202603-{i:04d}",
                vendor_id=f"V{30 + i:03d}",
                asset_id=asset_id,
                document_date=posting,
                posting_date=posting,
                net_amount=money(85_000 + i * 7_500),
                currency=FUNCTIONAL_CURRENCY,
                exchange_rate=_currency_rate(FUNCTIONAL_CURRENCY),
                country="DE",
                cost_center_id="CC400",
                purchase_order_id=f"PO-202603-FA-{i:04d}",
                description="Synthetic production equipment acquisition",
            )
        )

    if len(events) != event_count:
        raise AssertionError(f"Expected {event_count} events, generated {len(events)}")
    return tuple(events)
