from dataclasses import replace
from decimal import Decimal

import pytest

from close_lab.business_events import CustomerReceipt, FixedAssetAcquisition, SupplierInvoice, generate_smoke_events
from close_lab.chart_of_accounts import build_chart_of_accounts
from close_lab.journal_engine import PostingError, post_events
from close_lab.master_data import build_master_data
from close_lab.validation import validate_journal_integrity


def _base():
    return build_master_data(), build_chart_of_accounts(), list(generate_smoke_events())


def test_duplicate_event_is_rejected():
    master_data, accounts, events = _base()
    events.append(events[0])
    with pytest.raises(PostingError, match="duplicate event_id"):
        post_events(events, master_data, accounts)


def test_customer_receipt_cannot_clear_another_customer_invoice():
    master_data, accounts, events = _base()
    receipt = next(event for event in events if isinstance(event, CustomerReceipt))
    events[events.index(receipt)] = replace(receipt, customer_id="C020")
    with pytest.raises(PostingError, match="does not match"):
        post_events(events, master_data, accounts)


def test_over_clearing_is_rejected():
    master_data, accounts, events = _base()
    receipt = next(event for event in events if isinstance(event, CustomerReceipt))
    events[events.index(receipt)] = replace(receipt, amount=Decimal("999999.99"))
    with pytest.raises(PostingError, match="exceeds invoice balance"):
        post_events(events, master_data, accounts)


def test_removed_journal_line_is_detected():
    master_data, accounts, events = _base()
    results = list(post_events(events, master_data, accounts))
    results[0] = replace(results[0], lines=results[0].lines[:-1])
    assert any("fewer than two lines" in issue or "not balanced" in issue for issue in validate_journal_integrity(results, accounts, master_data))


def test_unknown_account_is_detected():
    master_data, accounts, events = _base()
    results = list(post_events(events, master_data, accounts))
    results[0] = replace(results[0], lines=(replace(results[0].lines[0], gl_account_id="999999"), *results[0].lines[1:]))
    assert any("unknown account" in issue for issue in validate_journal_integrity(results, accounts, master_data))


def test_po_linked_supplier_invoice_is_deferred_until_grir_exists():
    master_data, accounts, events = _base()
    invoice = next(event for event in events if isinstance(event, SupplierInvoice))
    events[events.index(invoice)] = replace(invoice, purchase_order_id="PO-UNIMPLEMENTED")
    with pytest.raises(PostingError, match="PO-linked supplier invoices are deferred"):
        post_events(events, master_data, accounts)


def test_cross_type_invoice_id_reuse_is_rejected():
    master_data, accounts, events = _base()
    asset = next(event for event in events if isinstance(event, FixedAssetAcquisition))
    invoice = next(event for event in events if isinstance(event, SupplierInvoice))
    events[events.index(asset)] = replace(asset, invoice_id=invoice.invoice_id)
    with pytest.raises(PostingError, match="reused across event types"):
        post_events(events, master_data, accounts)
