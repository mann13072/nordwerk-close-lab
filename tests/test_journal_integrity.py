from decimal import Decimal

from close_lab.business_events import generate_smoke_events
from close_lab.chart_of_accounts import build_chart_of_accounts
from close_lab.journal_engine import post_events
from close_lab.master_data import build_master_data
from close_lab.validation import validate_journal_integrity


def test_every_smoke_document_balances_and_has_expected_line_shape():
    master_data = build_master_data()
    results = post_events(generate_smoke_events(), master_data, build_chart_of_accounts())
    assert len(results) == 60
    assert sum(len(result.lines) for result in results) == 157
    assert validate_journal_integrity(results, build_chart_of_accounts(), master_data) == []
    assert all(sum((line.signed_local_amount for line in result.lines), Decimal("0")) == Decimal("0.00") for result in results)
