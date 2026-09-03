from close_lab.chart_of_accounts import build_chart_of_accounts
from close_lab.master_data import build_master_data
from close_lab.validation import validate_master_data


def test_master_data_has_required_shapes_and_unique_keys():
    master_data = build_master_data()
    assert len(master_data.cost_centers) == 8
    assert len(master_data.customers) == 25
    assert len(master_data.vendors) == 60
    assert len(master_data.materials) == 20
    assert len(master_data.fixed_assets) == 30
    assert {account.account_id for account in build_chart_of_accounts()} >= {
        "100000", "110000", "140000", "150000", "200000", "230000", "400000", "570000"
    }
    assert validate_master_data(master_data, build_chart_of_accounts()) == []
