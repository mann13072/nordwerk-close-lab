"""Educational chart of accounts for the first smoke-test gate."""

from __future__ import annotations

from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable


@dataclass(frozen=True)
class GLAccount:
    account_id: str
    account_name: str
    account_type: str
    normal_balance: str
    open_item_managed: bool
    cost_center_required: bool
    fx_remeasurement: bool
    hgb_bs_line: str
    hgb_pl_line: str
    management_pl_line: str
    cash_flow_tag: str


GL_ACCOUNT_SCHEMA = tuple(GLAccount.__dataclass_fields__.keys())


def build_chart_of_accounts() -> tuple[GLAccount, ...]:
    """Build the compact chart required by the five smoke-test events."""

    return (
        GLAccount("100000", "Main bank", "asset", "debit", False, False, False, "B.IV Cash", "", "", "operating"),
        GLAccount("110000", "Trade receivables", "asset", "debit", True, False, True, "B.II Trade receivables", "", "", "operating"),
        GLAccount("140000", "Input VAT", "asset", "debit", False, False, False, "B.II Other assets", "", "", "operating"),
        GLAccount("120000", "Raw material inventory", "asset", "debit", False, False, False, "B.I.2 Raw materials", "", "", "operating"),
        GLAccount("150000", "Machinery", "asset", "debit", False, True, False, "A.II.2 Technical equipment and machinery", "", "", "investing"),
        GLAccount("200000", "Trade payables", "liability", "credit", True, False, True, "C.4 Trade payables", "", "", "operating"),
        GLAccount("230000", "Output VAT", "liability", "credit", False, False, False, "C.8 Other liabilities", "", "", "operating"),
        GLAccount("400000", "Product revenue", "revenue", "credit", False, False, False, "", "1. Sales revenue", "Revenue", "operating"),
        GLAccount("570000", "Professional and external services", "expense", "debit", False, True, False, "", "5. Cost of materials", "External services", "operating"),
    )


def account_map(accounts: Iterable[GLAccount] | None = None) -> dict[str, GLAccount]:
    return {account.account_id: account for account in (accounts or build_chart_of_accounts())}


def account_rows(accounts: Iterable[GLAccount] | None = None) -> list[dict[str, object]]:
    return [asdict(account) for account in (accounts or build_chart_of_accounts())]


def export_chart_of_accounts(path: Path, accounts: Iterable[GLAccount] | None = None) -> None:
    """Write a stable UTF-8 CSV representation of the schema and rows."""

    from .serialization import write_csv

    write_csv(path, GL_ACCOUNT_SCHEMA, account_rows(accounts))
