from close_lab.business_events import generate_smoke_events
from close_lab.chart_of_accounts import build_chart_of_accounts
from close_lab.journal_engine import post_events
from close_lab.master_data import build_master_data
from close_lab.validation import validate_control_totals, validate_subledger_linkage


def test_ar_ap_bank_vat_and_asset_controls_tie():
    master_data = build_master_data()
    events = generate_smoke_events()
    results = post_events(events, master_data, build_chart_of_accounts())
    assert validate_subledger_linkage(events, results, master_data) == []
    assert validate_control_totals(events, results) == []
