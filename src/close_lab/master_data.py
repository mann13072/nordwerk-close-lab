"""Deterministic synthetic master data and its explicit table schemas."""

from __future__ import annotations

from dataclasses import asdict, dataclass
from datetime import date
from decimal import Decimal
from pathlib import Path
from typing import Iterable

from .config import money


@dataclass(frozen=True)
class CostCenter:
    cost_center_id: str
    cost_center_name: str
    department: str
    manager_role: str
    profit_center_id: str
    valid_from: date
    valid_to: date


@dataclass(frozen=True)
class Customer:
    customer_id: str
    customer_name_synthetic: str
    country: str
    currency: str
    payment_terms_days: int
    credit_limit: Decimal
    related_party_flag: bool


@dataclass(frozen=True)
class Vendor:
    vendor_id: str
    vendor_name_synthetic: str
    country: str
    currency: str
    payment_terms_days: int
    vendor_category: str
    related_party_flag: bool


@dataclass(frozen=True)
class Material:
    material_id: str
    material_description: str
    material_type: str
    unit_of_measure: str
    standard_cost: Decimal
    weighted_average_cost: Decimal
    product_family: str
    inventory_account: str
    write_down_group: str


@dataclass(frozen=True)
class FixedAsset:
    asset_id: str
    asset_class: str
    description: str
    acquisition_date: date
    in_service_date: date
    acquisition_cost: Decimal
    useful_life_months: int
    depreciation_method: str
    cost_center_id: str
    accumulated_depreciation_opening: Decimal


@dataclass(frozen=True)
class MasterData:
    cost_centers: tuple[CostCenter, ...]
    customers: tuple[Customer, ...]
    vendors: tuple[Vendor, ...]
    materials: tuple[Material, ...]
    fixed_assets: tuple[FixedAsset, ...]


def _rows(items: Iterable[object]) -> list[dict[str, object]]:
    return [asdict(item) for item in items]


def build_master_data() -> MasterData:
    cost_centers = (
        CostCenter("CC100", "Production", "Operations", "Production Manager", "PC10", date(2026, 1, 1), date(2099, 12, 31)),
        CostCenter("CC110", "Maintenance", "Operations", "Maintenance Manager", "PC10", date(2026, 1, 1), date(2099, 12, 31)),
        CostCenter("CC120", "Quality", "Operations", "Quality Manager", "PC10", date(2026, 1, 1), date(2099, 12, 31)),
        CostCenter("CC130", "Warehouse and Logistics", "Operations", "Logistics Manager", "PC10", date(2026, 1, 1), date(2099, 12, 31)),
        CostCenter("CC200", "Procurement", "Commercial", "Procurement Manager", "PC20", date(2026, 1, 1), date(2099, 12, 31)),
        CostCenter("CC300", "Sales", "Commercial", "Sales Director", "PC20", date(2026, 1, 1), date(2099, 12, 31)),
        CostCenter("CC400", "Engineering", "Technical", "Engineering Manager", "PC30", date(2026, 1, 1), date(2099, 12, 31)),
        CostCenter("CC500", "Finance HR and Administration", "Corporate", "Finance Manager", "PC30", date(2026, 1, 1), date(2099, 12, 31)),
    )

    customer_countries = ("DE", "DE", "DE", "NL", "FR")
    customers = tuple(
        Customer(
            f"C{i:03d}",
            f"Synthetic Customer {i:03d}",
            customer_countries[(i - 1) % len(customer_countries)],
            "EUR",
            30 if i % 3 else 45,
            money(250_000 + i * 25_000),
            False,
        )
        for i in range(1, 26)
    )

    vendor_countries = ("DE", "DE", "AT", "PL", "NL")
    vendor_categories = ("services", "maintenance", "logistics", "consulting", "utilities")
    vendors = tuple(
        Vendor(
            f"V{i:03d}",
            f"Synthetic Vendor {i:03d}",
            vendor_countries[(i - 1) % len(vendor_countries)],
            "EUR",
            30 if i % 2 else 45,
            vendor_categories[(i - 1) % len(vendor_categories)],
            False,
        )
        for i in range(1, 61)
    )

    materials = tuple(
        Material(
            f"MAT{i:03d}",
            f"Synthetic material {i:03d}",
            "raw" if i <= 14 else "packaging",
            "EA",
            money(12.50 + i * 1.35),
            money(12.70 + i * 1.32),
            ("Cooling Pumps", "Thermal Valves", "Control Modules")[(i - 1) % 3],
            "120000",
            "standard",
        )
        for i in range(1, 21)
    )

    fixed_assets = tuple(
        FixedAsset(
            f"FA{i:03d}",
            "machinery" if i <= 20 else "IT equipment",
            f"Synthetic asset {i:03d}",
            date(2025, 1, 15),
            date(2025, 2, 1),
            money(50_000 + i * 2_500),
            84 if i <= 20 else 36,
            "straight_line",
            cost_centers[(i - 1) % len(cost_centers)].cost_center_id,
            money(0),
        )
        for i in range(1, 31)
    )

    return MasterData(cost_centers, customers, vendors, materials, fixed_assets)


def master_rows(master_data: MasterData) -> dict[str, list[dict[str, object]]]:
    return {
        "cost_centres": _rows(master_data.cost_centers),
        "customers": _rows(master_data.customers),
        "vendors": _rows(master_data.vendors),
        "materials": _rows(master_data.materials),
        "fixed_assets": _rows(master_data.fixed_assets),
    }


def export_master_data(directory: Path, master_data: MasterData | None = None) -> None:
    from .serialization import write_csv

    master_data = master_data or build_master_data()
    for name, rows in master_rows(master_data).items():
        columns = tuple(rows[0].keys()) if rows else ()
        write_csv(directory / f"{name}.csv", columns, rows)
