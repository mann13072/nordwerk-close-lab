"""Shared smoke-test configuration and decimal/date conventions."""

from __future__ import annotations

from datetime import date
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
COMPANY_CODE = "DE01"
CONTROLLING_AREA = "NW01"
FUNCTIONAL_CURRENCY = "EUR"
REPORTING_PERIOD = "2026-03"
SMOKE_SEED = 20260331
SCENARIO_TIMESTAMP = "2026-04-01T08:00:00+02:00"
DOMESTIC_COUNTRY = "DE"
DOMESTIC_VAT_RATE = Decimal("0.19")
CENT = Decimal("0.01")


def money(value: Decimal | int | str | float) -> Decimal:
    """Return a currency amount rounded to cents with one documented rule."""

    return Decimal(str(value)).quantize(CENT, rounding=ROUND_HALF_UP)


def local_amount(transaction_amount: Decimal, exchange_rate: Decimal) -> Decimal:
    """Convert transaction currency into EUR at the event exchange rate."""

    return money(transaction_amount * exchange_rate)


def smoke_date(day_offset: int) -> date:
    """Return a deterministic date within January–March 2026."""

    # 2026-01-05 + 0..84 days stays inside the first quarter.
    return date(2026, 1, 5).fromordinal(date(2026, 1, 5).toordinal() + day_offset)
