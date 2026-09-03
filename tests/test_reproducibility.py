import csv
from collections import defaultdict
from decimal import Decimal
from pathlib import Path

from close_lab.business_events import generate_smoke_events
from close_lab.chart_of_accounts import build_chart_of_accounts
from close_lab.export import export_smoke
from close_lab.journal_engine import post_events
from close_lab.master_data import build_master_data


def _hashes(path: Path):
    master_data = build_master_data()
    accounts = build_chart_of_accounts()
    events = generate_smoke_events(seed=20260331)
    results = post_events(events, master_data, accounts)
    return export_smoke(path, events, results, master_data)


def test_same_seed_produces_same_csv_hashes():
    project_root = Path(__file__).resolve().parents[1]
    output_dir = project_root / "data" / "raw" / "smoke_test"
    first = _hashes(output_dir)
    second = _hashes(output_dir)
    assert first == second


def test_different_seed_changes_transaction_values():
    master_data = build_master_data()
    accounts = build_chart_of_accounts()
    first = generate_smoke_events(seed=20260331)
    second = generate_smoke_events(seed=20260332)
    assert first != second
    assert post_events(first, master_data, accounts)
    assert post_events(second, master_data, accounts)


def test_serialized_journal_lines_rehydrate_and_balance():
    project_root = Path(__file__).resolve().parents[1]
    output_dir = project_root / "data" / "raw" / "smoke_test"
    _hashes(output_dir)
    sums = defaultdict(Decimal)
    with (output_dir / "journal_lines.csv").open(encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            sums[row["document_id"]] += Decimal(row["signed_local_amount"])
    assert len(sums) == 60
    assert all(value == Decimal("0.00") for value in sums.values())
