from close_lab.business_events import generate_smoke_events
from close_lab.chart_of_accounts import build_chart_of_accounts
from close_lab.journal_engine import post_events
from close_lab.master_data import build_master_data
from close_lab.projections import build_ap_open_items, build_ar_open_items
from close_lab.validation import validate_control_totals, validate_subledger_linkage


def test_ar_ap_bank_vat_and_asset_controls_tie():
    master_data = build_master_data()
    events = generate_smoke_events()
    results = post_events(events, master_data, build_chart_of_accounts())
    assert validate_subledger_linkage(events, results, master_data) == []
    assert validate_control_totals(events, results) == []
    assert sum(item.open_amount > 0 for item in build_ar_open_items(events, master_data)) == 8
    assert sum(item.open_amount > 0 for item in build_ap_open_items(events, master_data)) == 11


def test_payment_terms_drive_due_dates():
    master_data = build_master_data()
    events = generate_smoke_events()
    ar_items = build_ar_open_items(events, master_data)
    ap_items = build_ap_open_items(events, master_data)
    customer_terms = {row.customer_id: row.payment_terms_days for row in master_data.customers}
    vendor_terms = {row.vendor_id: row.payment_terms_days for row in master_data.vendors}
    assert all((item.due_date - item.invoice_date).days == customer_terms[item.customer_id] for item in ar_items)
    assert all((item.due_date - item.invoice_date).days == vendor_terms[item.vendor_id] for item in ap_items)
