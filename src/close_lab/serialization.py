"""Canonical UTF-8 CSV serialization for reproducible outputs."""

from __future__ import annotations

import csv
import hashlib
from datetime import date, datetime
from decimal import Decimal
from pathlib import Path
from typing import Iterable, Mapping, Sequence


def scalar(value: object) -> str:
    if value is None:
        return ""
    if isinstance(value, Decimal):
        return f"{value:.2f}"
    if isinstance(value, (date, datetime)):
        return value.isoformat()
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)


def write_csv(path: Path, columns: Sequence[str], rows: Iterable[Mapping[str, object]]) -> str:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(columns), lineterminator="\n")
        writer.writeheader()
        for row in rows:
            writer.writerow({column: scalar(row.get(column)) for column in columns})
    return sha256_file(path)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()
